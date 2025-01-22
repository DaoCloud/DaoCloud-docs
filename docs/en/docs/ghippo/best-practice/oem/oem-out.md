---
MTPE: WANG0608GitHub
Date: 2024-08-15
---

# Integrate DCE 5.0 into Customer System (OEM OUT)

OEM OUT refers to integrating DCE 5.0 as a sub-module into other products, appearing in their menus.
You can directly access DCE 5.0 without logging in again after logging into other products.
The OEM OUT integration involves 5 steps:

1. [Unify domain name](#unify-domain-name)
2. [User system integration](#user-system-integration)
3. [Navigation bar integration](#navigation-bar-integration)
4. [Customize appearance](#customizie-appearance)
5. [Permission system integration (optional)](#permission-system-integration-optional)

For detailed instructions, refer to the [OEM OUT Best Practices video tutorial](../../../videos/use-cases.md#integrating-dce-50-into-customer-systems-oem-out).

## Unify Domain Name

1. Deploy DCE 5.0 (Assuming the access address after deployment is `https://10.6.8.2:30343/`).

2. To achieve cross-domain access between the customer system and DCE 5.0, you can use an nginx reverse proxy.
   Use the following example configuration in __vi /etc/nginx/conf.d/default.conf__ :

    ```nginx
    server {
        listen       80;
        server_name  localhost;
    
        location /dce5/ {
          proxy_pass https://10.6.8.2:30343/;
          proxy_http_version 1.1;
          proxy_read_timeout 300s; # This line is required for using kpanda cloudtty, otherwise it can be removed
          proxy_send_timeout 300s; # This line is required for using kpanda cloudtty, otherwise it can be removed
    
          proxy_set_header Host $host;
          proxy_set_header X-Real-IP $remote_addr;
          proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    
          proxy_set_header Upgrade $http_upgrade; # This line is required for using kpanda cloudtty, otherwise it can be removed
          proxy_set_header Connection $connection_upgrade; # This line is required for using kpanda cloudtty, otherwise it can be removed
        }
        
        location / {
            proxy_pass https://10.6.165.50:30443/; # Assuming this is the customer system address (e.g., Yiyun)
            proxy_http_version 1.1;
    
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        }
    }
    ```

3. Assuming the nginx entry address is 10.6.165.50, follow the
   [Customize DCE 5.0 Reverse Proxy Server Address](../install/reverse-proxy.md) to
   set the DCE_PROXY reverse proxy as `http://10.6.165.50/dce5`. Ensure that DCE 5.0
   can be accessed via `http://10.6.165.50/dce5`. The customer system also needs
   to configure the reverse proxy based on its specific requirements.

    ![Reverse Proxy](../../images/agent.png)

## User System Integration

Integrate the customer system with DCE 5.0 using protocols like OIDC/OAUTH,
allowing users to access DCE 5.0 without logging in again after logging into
the customer system. Fill in the OIDC information of the customer system in
 __Global Management__ -> __Access Control__ -> __Identity Provider__ .

After integration, the DCE 5.0 login page will display the OIDC (custom) option.
When accessing DCE 5.0 from the customer system for the first time,
select OIDC login, and subsequent logins will directly enter DCE 5.0 without needing to choose again.

## Navigation Bar Integration

Navigation bar integration means adding DCE 5.0 to the menu of the customer system.
You can directly access DCE 5.0 by clicking the proper menu item. The navigation bar
integration depends on the customer system and needs to be handled based on specific circumstances.

## Customizie Appearance

Use __Global Management__ -> __Settings__ -> __Appearance__ to customize
the platform's background color, logo, and name. For detailed instructions,
refer to [Appearance Customization](../user-guide/platform-setting/appearance.md).

## Permission System Integration (optional)

Permission system integration is complex.
If you have such requirements, please contact the Global Management team.

## Reference

- [OEM IN](./oem-in.md)