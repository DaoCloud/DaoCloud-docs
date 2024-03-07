# Microservice Gateway Authentication Server - Integrating OIDC Authentication

The Microservice Engine Gateway's OIDC authentication service demo consists of two parts.

1. Authentication service, code repository: <https://github.com/projectsesame/contour-authserver>
2. Identity Provider (referred to as IDP), code repository: <https://github.com/projectsesame/dex>

Deploy the ldp service by deploying it in a Kubernetes cluster according to the contents of the dex-all-in-one.yaml file.
The DEX_ISSUER environment variable should point to the nodeport or load balancer address of the ldp service + /dex. This service must be exposed for external access.
The DEX_STATIC_CLIENT_REDIRECT_URI environment variable should list the allowed client redirect URIs in the format `http(s)://+domain+port+redirectPath`,
where the path is the redirectPath of the authentication service that will be deployed later.
Other environment variables are not recommended to be modified. If you wish to experiment, you can refer to the config.docker.yaml file for modifications and rebuild the image.
After successful deployment, you can start deploying the authentication service. Deploy it in a Kubernetes cluster according to the contents of the auth-oidc-all-in-one.yaml file.
Some parts of the content in the configMap need to be configured according to your own environment. Here are the meanings of each configuration item:

| Parameter Name | Parameter Type | Parameter Meaning | Parameter Example | Note |
| ------ | -------- | ------- | ------- | --- |
| address | string | Address where the service is provided | :10083 | Indicates that the service can be accessed through port 10083 from any address. The port should match the service port |
| issuerURL | string | Identity Provider | `http://10.6.222.22:30051/dex` | Fill in the address of the *IDP* service nodePort or loadBalancer + /dex. In the example, it is accessed via nodePort |
| clientID | string | Client ID | `example-app` | Client ID and secret for the example application are hardcoded |
| clientSecret | string | Client Secret | `ZXhhbXBsZS1hcHAtc2VjcmV0` | |
| scopes | []string | Access scopes | openid, profile, email, `offline_access` | |
| redirectURL | string | Redirect callback URL | `https://yangyang.daocloud.io:30443` | Example is `https://+domain+https port` |
| redirectPath | string | Redirect path | /oauth2/callback | The gateway API configuration should include this path in the authentication path |

The above configuration items in this demo are issuerURL and redirectURL. These two should be modified according to the deployment environment, and other parameters are not recommended to be changed! The following documentation will explain using the example configurations mentioned above.

Once both services are successfully deployed, you can proceed with the configuration through the Microservice Engine web interface. Here are the configuration steps:

1. Create a Plugin

    <!--![]()screenshots-->

2. Select the gateway, create a domain, and select the security authentication plugin created in the first step

    <!--![]()screenshots-->

    <!--![]()screenshots-->

3. Create an API and select the newly created domain

    <!--![]()screenshots-->

4. After successfully creating the API, access it through a browser

    Access <https://yangyang.daocloud.io:30443/>
    
    Since we have configured the domain for authentication, the page will redirect to the ldp service's login page. The right image shows the redirection process.
    In the example code, the username is: admin@example.com, and the password is: password.

    <!--![]()screenshots-->

    After logging in, an authorization page will be displayed. Click **Grant Access**

    <!--![]()screenshots-->

    After a few redirects, you should be able to access the backend API successfully:

    <!--![]()screenshots-->

With this, the complete logic of implementing OIDC authentication using the Microservice Engine has been completed.
