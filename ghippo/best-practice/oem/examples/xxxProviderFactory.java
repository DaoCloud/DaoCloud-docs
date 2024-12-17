package org.keycloak.broker.oauth;
 
import org.keycloak.broker.oidc.OIDCIdentityProviderConfig;
import org.keycloak.broker.provider.AbstractIdentityProviderFactory;
import org.keycloak.models.IdentityProviderModel;
import org.keycloak.models.KeycloakSession;
 
/*
一定要这样写
public class xxxProviderFactory extends AbstractIdentityProviderFactory<OAuthIdentityProvider> {
    ...
}
 
剩下的根据 services/src/main/java/org/keycloak/broker/oidc/KeycloakOIDCIdentityProviderFactory.java 缺什么补什么
如果你用 ide，ide 会提示你缺啥
*/
public class OAuthIdentityProviderFactory extends AbstractIdentityProviderFactory<OAuthIdentityProvider> {
 
    public static final String PROVIDER_ID = "oauth"; // 留意这个变量，后面定义 html 要用
 
    /*
    定义了在页面上的名称
     */
    @Override
    public String getName() {
        return "OAuth";
    }
 
    /*
    就这样些，如果你自定义了 ProviderConfig，请把 OIDCIdentityProviderConfig 改一下
     */
    @Override
    public OAuthIdentityProvider create(KeycloakSession session, IdentityProviderModel model) {
        return new OAuthIdentityProvider(session, new OIDCIdentityProviderConfig(model));
    }
     
    /*
    定义了 id，建议唯一不要重复，也要在页面显示的
     */
    @Override
    public String getId() {
        return PROVIDER_ID;
    }
 
    /*
    复用 oidc 的 config, 你也可以自己定义，参考 OIDCIdentityProviderConfig 文件
     */
    @Override
    public OIDCIdentityProviderConfig createConfig() {
        return new OIDCIdentityProviderConfig();
    }
}