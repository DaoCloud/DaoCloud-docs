# OEM OUT

OEM OUT refers to the integration of DCE 5.0 as a submodule into other products,
appearing in the menu of those products. Users can directly access DCE 5.0 without
logging in again after logging into other products.

Identity Provider (IdP): When DCE 5.0 needs to use the customer's system as the user source
and perform login authentication through the customer's system login interface, the customer's
system is referred to as the Identity Provider for DCE 5.0.

## How to Implement OEM OUT

### Integration of User Systems

Use the customer's system as the user source to achieve unified login authentication. This step is necessary.

1. Create a client in the customer's system (refer to [Ghippo OIDC Configuration](../user-guide/access-control/oidc.md))
   and obtain some integration parameters. If the customer's system requires a callback URL,
   you can use the domain or IP of the entrance address of DCE 5.0.

2. Configure the parameters from the previous step in the Identity Provider interface of DCE 5.0.
   using protocols such as OIDC/OAUTH to integrate with the customer's user system.

    ![oidc](./images/oem-out01.png)

!!! tip

    If customization is required for the integration protocol supported by the customer,
    refer to [How to Customize DCE 5.0 to Integrate with External Identity Providers (IdP)](custom-idp.md).

## Embedding DCE 5.0 Pages in the Customer System Interface

Insert certain functional menu items of DCE 5.0 into the navigation bar of
customer's system to use the customer's system as a portal (optional).

### Method

Prerequisite: The customer system (e.g., WYCloud) supports embedding sub-module pages using iframes.

1. Deploy DCE 5 (assuming the access address after deployment is https://10.6.8.2:30343/).

2. Use an Nginx reverse proxy between the customer system and DCE 5 to achieve same-domain access.
   Route `/` to the customer's system and route `/dce5` to the DCE 5.0 system.
   Refer to the [/etc/nginx/conf.d/default.conf example](./examples/default2.conf).

3. Assuming the Nginx entry address is 10.6.165.50, follow the steps in
   [Setting Up DCE 5.0 Reverse Proxy](../install/reverse-proxy.md) to set the DCE_PROXY as http://10.6.165.50/dce5/.

4. Access http://10.6.165.50/dce5/. In DCE 5.0, go to `Platform Settings` -> `Appearance` -> `Advanced Customization`
   to modify the page style of DCE 5.0 to make it consistent with the customer's system style.

5. Encode the DCE 5.0 access address (http://10.6.165.50/dce5/) into the src attribute of the iframe
   in the customer's system. You can modify the style of the embedded page by writing CSS in the iframe.
   See [App.vue code example](./examples/App.vue).

## Permission Integration (Optional)

Customized teams can implement a custom module. DCE 5.0 can provide webhook registration functionality
to notify the custom module of every user login event through webhooks. The custom module can then use the
[OpenAPI](https://docs.daocloud.io/openapi/) of WYCloud and DCE 5.0 to synchronize the user's permission information.

## Reference Documentation

- Refer to [OEM IN Documentation](oem-in.md)
- Refer to [GProduct-demo integration tar package](./examples/gproduct-demo-main.tar.gz)
