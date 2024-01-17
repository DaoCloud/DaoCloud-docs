package org.keycloak.broker.oauth;
 
import org.keycloak.broker.oidc.OIDCIdentityProviderConfig;
import org.keycloak.broker.provider.AbstractIdentityProviderFactory;
import org.keycloak.models.IdentityProviderModel;
import org.keycloak.models.KeycloakSession;
 
```java
/*
Make sure to write it this way
public class xxxProviderFactory extends AbstractIdentityProviderFactory<OAuthIdentityProvider> {
    ...
}

Add the missing parts based on services/src/main/java/org/keycloak/broker/oidc/KeycloakOIDCIdentityProviderFactory.java.
If you are using an IDE, it will prompt you for any missing parts.
*/

public class OAuthIdentityProviderFactory extends AbstractIdentityProviderFactory<OAuthIdentityProvider> {

    public static final String PROVIDER_ID = "oauth"; // Note this variable, it will be used when defining the HTML

    /*
    Define the name displayed on the page
     */
    @Override
    public String getName() {
        return "OAuth";
    }

    /*
    Just write it like this. If you have custom ProviderConfig, change OIDCIdentityProviderConfig accordingly
     */
    @Override
    public OAuthIdentityProvider create(KeycloakSession session, IdentityProviderModel model) {
        return new OAuthIdentityProvider(session, new OIDCIdentityProviderConfig(model));
    }

    /*
    Define the ID, it is recommended to be unique and also visible on the page
     */
    @Override
    public String getId() {
        return PROVIDER_ID;
    }

    /*
    Reuse oidc's config, or you can define your own. Refer to the OIDCIdentityProviderConfig file for guidance.
     */
    @Override
    public OIDCIdentityProviderConfig createConfig() {
        return new OIDCIdentityProviderConfig();
    }
}
```