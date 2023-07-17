package org.keycloak.broker.oauth;
 
import com.fasterxml.jackson.databind.JsonNode;
import org.jboss.logging.Logger;
import org.keycloak.broker.oidc.OIDCIdentityProvider;
import org.keycloak.broker.oidc.OIDCIdentityProviderConfig;
import org.keycloak.broker.oidc.mappers.AbstractJsonUserAttributeMapper;
import org.keycloak.broker.provider.BrokeredIdentityContext;
import org.keycloak.broker.provider.IdentityBrokerException;
import org.keycloak.broker.provider.util.SimpleHttp;
import org.keycloak.common.util.Time;
import org.keycloak.constants.AdapterConstants;
import org.keycloak.events.EventBuilder;
import org.keycloak.jose.jws.JWSInput;
import org.keycloak.jose.jws.JWSInputException;
import org.keycloak.models.KeycloakSession;
import org.keycloak.models.RealmModel;
import org.keycloak.models.UserSessionModel;
import org.keycloak.protocol.oidc.OIDCLoginProtocol;
import org.keycloak.representations.AccessTokenResponse;
import org.keycloak.representations.IDToken;
import org.keycloak.representations.JsonWebToken;
import org.keycloak.services.resources.IdentityBrokerService;
import org.keycloak.services.resources.RealmsResource;
import org.keycloak.util.JsonSerialization;
 
import javax.ws.rs.core.*;
import java.io.IOException;
 
/*
Here, we inherit some of the functionalities from OIDC,
it can be written like this.
Keycloak does not have inheritance capabilities, please refer to how the OIDCIdentityProvider code is written.
public class OAuthIdentityProvider extends OIDCIdentityProvider {
}
 */

public class OAuthIdentityProvider extends OIDCIdentityProvider {
    protected static final Logger logger = Logger.getLogger(OAuthIdentityProvider.class);
 
    public static final String SCOPE_OPENID = "openid";
    public static final String FEDERATED_ID_TOKEN = "FEDERATED_ID_TOKEN";
    public static final String USER_INFO = "UserInfo";
    public static final String FEDERATED_ACCESS_TOKEN_RESPONSE = "FEDERATED_ACCESS_TOKEN_RESPONSE";
    public static final String VALIDATED_ID_TOKEN = "VALIDATED_ID_TOKEN";
    public static final String ACCESS_TOKEN_EXPIRATION = "accessTokenExpiration";
    public static final String EXCHANGE_PROVIDER = "EXCHANGE_PROVIDER";
    private static final String BROKER_STATE_PARAM = "BROKER_STATE";
 
    public OAuthIdentityProvider(KeycloakSession session, OIDCIdentityProviderConfig config) {
        super(session, config);
    }
 
    @Override
    public Object callback(RealmModel realm, AuthenticationCallback callback, EventBuilder event) {
        return new OAuthEndpoint(callback, realm, event);
    }
 
    @Override
    public Response keycloakInitiatedBrowserLogout(KeycloakSession session, UserSessionModel userSession, UriInfo uriInfo, RealmModel realm) {
        if (getConfig().getLogoutUrl() == null || getConfig().getLogoutUrl().trim().equals("")) return null;
        String idToken = getIDTokenForLogout(session, userSession);
        if (idToken != null && getConfig().isBackchannelSupported()) {
            backchannelLogout(userSession, idToken);
            return null;
        } else {
            String sessionId = userSession.getId();
            UriBuilder logoutUri = UriBuilder.fromUri(getConfig().getLogoutUrl())
                    .queryParam("state", sessionId);
            if (idToken != null) logoutUri.queryParam("id_token_hint", idToken);
            String redirect = RealmsResource.brokerUrl(uriInfo)
                    .path(IdentityBrokerService.class, "getEndpoint")
                    .path(OIDCEndpoint.class, "logoutResponse")
                    .build(realm.getName(), getConfig().getAlias()).toString();
            logoutUri.queryParam("post_logout_redirect_uri", redirect);
            Response response = Response.status(302).location(logoutUri.build()).build();
            return response;
        }
    }
 
    private String getIDTokenForLogout(KeycloakSession session, UserSessionModel userSession) {
        String tokenExpirationString = userSession.getNote(FEDERATED_TOKEN_EXPIRATION);
        long exp = tokenExpirationString == null ? 0 : Long.parseLong(tokenExpirationString);
        int currentTime = Time.currentTime();
        if (exp > 0 && currentTime > exp) {
            String response = refreshTokenForLogout(session, userSession);
            AccessTokenResponse tokenResponse = null;
            try {
                tokenResponse = JsonSerialization.readValue(response, AccessTokenResponse.class);
            } catch (IOException e) {
                throw new RuntimeException(e);
            }
            return tokenResponse.getIdToken();
        } else {
            return userSession.getNote(FEDERATED_ID_TOKEN);
 
        }
    }
 
    protected class OAuthEndpoint extends OIDCEndpoint {
        public OAuthEndpoint(AuthenticationCallback callback, RealmModel realm, EventBuilder event) {
            super(callback, realm, event);
        }
 
        @Override
        public SimpleHttp generateTokenRequest(String authorizationCode) {
            session.setAttribute(OAUTH2_PARAMETER_CODE, authorizationCode);
            return super.generateTokenRequest(authorizationCode)
                    .param(AdapterConstants.CLIENT_SESSION_STATE, "n/a");
            // hack to get backchannel logout to work
        }
    }
 
    /**
     * Logic to resolve
     */
    @Override
    public BrokeredIdentityContext getFederatedIdentity(String response) {
        AccessTokenResponse tokenResponse = null;
        try {
 
            tokenResponse = JsonSerialization.readValue(response, AccessTokenResponse.class);
        } catch (IOException e) {
            throw new IdentityBrokerException("Could not decode access token response.", e);
        }
        String accessToken = verifyAccessToken(tokenResponse);
        String encodedIdToken = tokenResponse.getIdToken();
        JsonWebToken idToken = (encodedIdToken != null) ? validateToken(encodedIdToken) : null;
 
        try {
            BrokeredIdentityContext identity = extractIdentity(tokenResponse, accessToken, idToken);
 
            if ((idToken != null) && (!identity.getId().equals(idToken.getSubject()))) {
                throw new IdentityBrokerException("Mismatch between the subject in the id_token and the subject from the user_info endpoint");
            }
 
            if (idToken != null) {
                identity.getContextData().put(BROKER_STATE_PARAM, idToken.getOtherClaims().get(OIDCLoginProtocol.STATE_PARAM));
            }
 
            if (getConfig().isStoreToken()) {
                if (tokenResponse.getExpiresIn() > 0) {
                    long accessTokenExpiration = Time.currentTime() + tokenResponse.getExpiresIn();
                    tokenResponse.getOtherClaims().put(ACCESS_TOKEN_EXPIRATION, accessTokenExpiration);
                    response = JsonSerialization.writeValueAsString(tokenResponse);
                }
                identity.setToken(response);
            }
 
            return identity;
        } catch (Exception e) {
            throw new IdentityBrokerException("Could not fetch attributes from userinfo endpoint.", e);
        }
    }
 
    private static final MediaType APPLICATION_JWT_TYPE = MediaType.valueOf("application/jwt");
 
    /**
     * Please modify this block of code if you encounter any issues with the specific parsing logic.
     * Do not modify other parts of the code. If you need to make changes, please consult the ghippo developers for assistance.
     */
    protected BrokeredIdentityContext extractIdentity(AccessTokenResponse tokenResponse, String accessToken, JsonWebToken idToken) throws IOException {
        String id = (idToken != null) ? idToken.getSubject() : null;
        BrokeredIdentityContext identity = (id != null) ? new BrokeredIdentityContext(id) : null;
        String name = (idToken != null) ? (String) idToken.getOtherClaims().get(IDToken.NAME) : null;
        String givenName = (idToken != null) ? (String) idToken.getOtherClaims().get(IDToken.GIVEN_NAME) : null;
        String familyName = (idToken != null) ? (String) idToken.getOtherClaims().get(IDToken.FAMILY_NAME) : null;
        String preferredUsername = (idToken != null) ? (String) idToken.getOtherClaims().get(getusernameClaimNameForIdToken()) : null;
        String email = (idToken != null) ? (String) idToken.getOtherClaims().get(IDToken.EMAIL) : null;
 
        if (!getConfig().isDisableUserInfoService()) {
            String userInfoUrl = getUserInfoUrl();
            if (userInfoUrl != null && !userInfoUrl.isEmpty() && (id == null || name == null || preferredUsername == null || email == null)) {
                if (accessToken != null) {
                    SimpleHttp.Response response = executeRequest(userInfoUrl, SimpleHttp.doGet(userInfoUrl, session)
                            .param("access_token", accessToken)
                            .param("code", (String) session.getAttribute("code"))
                            .header("Authorization", "Bearer " + accessToken));
 
                    logger.info(session.getAttribute("code"));
                    String contentType = response.getFirstHeader(HttpHeaders.CONTENT_TYPE);
                    MediaType contentMediaType;
                    try {
                        contentMediaType = MediaType.valueOf(contentType);
                    } catch (IllegalArgumentException ex) {
                        contentMediaType = null;
                    }
                    if (contentMediaType == null || contentMediaType.isWildcardSubtype() || contentMediaType.isWildcardType()) {
                        throw new RuntimeException("Unsupported content-type [" + contentType + "] in response from [" + userInfoUrl + "].");
                    }
                    JsonNode userInfo;
 
                    if (MediaType.APPLICATION_JSON_TYPE.isCompatible(contentMediaType)) {
                        userInfo = response.asJson();
                    } else if (APPLICATION_JWT_TYPE.isCompatible(contentMediaType)) {
                        JWSInput jwsInput;
 
                        try {
                            jwsInput = new JWSInput(response.asString());
                        } catch (JWSInputException cause) {
                            throw new RuntimeException("Failed to parse JWT userinfo response", cause);
                        }
 
                        if (verify(jwsInput)) {
                            userInfo = JsonSerialization.readValue(jwsInput.getContent(), JsonNode.class);
                        } else {
                            throw new RuntimeException("Failed to verify signature of userinfo response from [" + userInfoUrl + "].");
                        }
                    } else {
                        throw new RuntimeException("Unsupported content-type [" + contentType + "] in response from [" + userInfoUrl + "].");
                    }
 
                    id = getJsonProperty(userInfo, "UserId");                     // WeChat only has UserId, without sub 
                    name = getJsonProperty(userInfo, "name");
                    givenName = getJsonProperty(userInfo, IDToken.GIVEN_NAME);
                    familyName = getJsonProperty(userInfo, IDToken.FAMILY_NAME);
                    preferredUsername = getUsernameFromUserInfo(userInfo);
                    email = getJsonProperty(userInfo, "email");
 
                    identity = (id != null) ? new BrokeredIdentityContext(id) : null;
                    AbstractJsonUserAttributeMapper.storeUserProfileForMapper(identity, userInfo, getConfig().getAlias());
                }
            }
        }
        if (idToken != null) {
            identity.getContextData().put(VALIDATED_ID_TOKEN, idToken);
        }
 
        identity.setId(id);
 
        if (givenName != null) {
            identity.setFirstName(givenName);
        }
 
        if (familyName != null) {
            identity.setLastName(familyName);
        }
 
        if (givenName == null && familyName == null) {
            identity.setName(name);
        }
 
        identity.setEmail(email);
 
        identity.setBrokerUserId(getConfig().getAlias() + "." + id);
 
        if (preferredUsername == null) {
            preferredUsername = email;
        }
 
        if (preferredUsername == null) {
            preferredUsername = id;
        }
 
        identity.setUsername(preferredUsername);
        if (tokenResponse != null && tokenResponse.getSessionState() != null) {
            identity.setBrokerSessionId(getConfig().getAlias() + "." + tokenResponse.getSessionState());
        }
        if (tokenResponse != null) identity.getContextData().put(FEDERATED_ACCESS_TOKEN_RESPONSE, tokenResponse);
        if (tokenResponse != null) processAccessTokenResponse(identity, tokenResponse);
 
        return identity;
    }
 
 
    private String verifyAccessToken(AccessTokenResponse tokenResponse) {
        String accessToken = tokenResponse.getToken();
 
        if (accessToken == null) {
            throw new IdentityBrokerException("No access_token from server. error='" + tokenResponse.getError() +
                    "', error_description='" + tokenResponse.getErrorDescription() +
                    "', error_uri='" + tokenResponse.getErrorUri() + "'");
        }
        return accessToken;
    }
 
    private SimpleHttp.Response executeRequest(String url, SimpleHttp request) throws IOException {
        SimpleHttp.Response response = request.asResponse();
        if (response.getStatus() != 200) {
            String msg = "failed to invoke url [" + url + "]";
            try {
                String tmp = response.asString();
                if (tmp != null) msg = tmp;
 
            } catch (IOException e) {
 
            }
            throw new IdentityBrokerException("Failed to invoke url [" + url + "]: " + msg);
        }
        return response;
    }
 
 
    @Override
    public void preprocessFederatedIdentity(KeycloakSession session, RealmModel realm, BrokeredIdentityContext context) {
 
    }
}