# Configure domain name policy

The microservice gateway provides domain-level policy configuration capabilities. After configuring domain-level policies, there is no need to repeatedly configure policies for multiple APIs under the same domain name. Currently, two domain-level policies are supported: cross-domain and local traffic limiting.

There are two ways to configure domain name policies:

- Set policies during the process of creating a domain name, refer to [Add Domain Name](add-domain.md).
- Make adjustments through [Modify Domain Name](update-domain.md) after the domain name is created.

The detailed description of cross-domain and local traffic limiting policies is as follows:

## Local current limit

After configuring local rate limiting for a domain name, the configuration will be automatically applied to all APIs using this domain name.

For detailed configuration instructions on local rate limiting, please refer to [Local rate limiting](../api/api-policy.md#_6).

!!! note

    If there is a conflict between the rate limiting policy at the API level and the domain name level, the rate limiting policy at the API level shall prevail.

## cross-domain

<!--to be added: explain what is cross-domain, cross-domain function, effect, etc. -->

Note when filling in the configuration:

- Enable Credentials: When enabled, credential checks are required for cross-origin requests. After the check is passed, the cross-domain request can be processed.
- Allowed request method: Select the HTTP protocol request method. For detailed descriptions of various request methods, refer to W3C's official document [Method Definitions](https://www.rfc-editor.org/rfc/rfc9110.html#name-method-definitions).
- Allowed request sources: Limit multiple specific request sources, usually using IP.
- Preflight duration: the time it takes to check credentials, request methods, etc. before processing cross-domain requests, and the time unit is seconds, minutes, and hours.
- Allowed headers: Qualify specific HTTP header keywords. After adding the keyword, you need to add the corresponding keyword in the request header to access the target service normally.
- Exposed request headers: Control the exposed request header keywords, and you can configure multiple items.

    ![cross-domain](imgs/cross-domain.png)