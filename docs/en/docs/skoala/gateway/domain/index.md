# Add domain name

The microservice gateway supports the full lifecycle management of domain names, including adding, updating, and deleting domain names. Through domain name management, you can apply a domain name to multiple apis of the gateway and configure gateway policies at the domain name level. This page explains how to add a domain name.

To add a domain name, perform the following steps:

1. Click the name of the target gateway to enter the gateway overview page. Then click `Domain Management` in the left navigation bar and `Add Domain` in the upper right corner of the page.

    ![add domain](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/skoala/gateway/domain/images/add-domain-1.png)

2. Fill in the configuration information

    The domain name configuration information consists of `Basic Info` (mandatory) and `Policy Settings` (optional) and `Security Settings`(optional).

    - Domain name: cannot be modified after a domain name is created.
    - Protocol: HTTP is selected by default. If you select HTTPS, you need to provide an HTTPS certificate.

        > Currently, only existing certificates can be selected. Automatic certificate issuance and manual certificate upload features are being developed.

        ![https](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/skoala/gateway/domain/images/add-domain-https.png)

    - Local current limiting: refer to [Local Rate Limit](../api/api-policy.md#_6)
    - Cross-domain: refer to [Cross-domain](domain-policy.md#_2)

        ![fill in configuration](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/skoala/gateway/domain/images/add-domain-2.png)


3. Click `OK` in the lower right corner of the page

    Click `OK`, and the `Domain Management` page is automatically displayed. You can view the newly created domain name in the domain name list.

    ![add successfully](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/skoala/gateway/domain/images/domain-bingo.png)
