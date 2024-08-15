---
MTPE: windsonsea
Date: 2024-07-10
---

# Domain Name Management

The microservice gateway supports the full lifecycle management of domain names, including adding, updating, and deleting domain names. Through domain name management, you can apply a domain name to multiple apis of the gateway and configure gateway policies at the domain name level.

## Add domain name

To add a domain name, perform the following steps:

1. Click the name of the target gateway to enter the gateway overview page. Then click __Domain Management__ in the left navigation bar and __Add Domain__ in the upper right corner of the page.

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

3. Click __OK__ in the lower right corner of the page

    Click __OK__ , and the __Domain Management__ page is automatically displayed. You can view the newly created domain name in the domain name list.

    ![add successfully](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/skoala/gateway/domain/images/domain-bingo.png)

## Update domain name

You can modify the basic information and policy configuration of a domain in two ways.

- In the __Domain Management__ page find need to update the domain, on the right side click __ⵗ__ , choose __Edit Basic Settings__ or __Edit Policy Settings__ or __Edit Security Settings__ .
     
    ![Update the basic information on the list page](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/skoala/gateway/domain/images/update-domain-1.png) 

- Click the domain to go to the domain details page. Click __Edit Basic Settings__ at the upper right corner of the page to update basic information and __Edit Policy Settings__ to update policy and __Edit Security Settings__ to update security settings.

    ![Updated on the details page](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/skoala/gateway/domain/images/update-domain-2.png)

## Delete domain name

!!! danger

    - A domain name that is being used by the API cannot be deleted. You need to delete the API before deleting the domain name.
    - The domain name cannot be restored after being deleted.

You can delete a domain name in two ways.

- In the __Domain Management__ page to find the need to delete the domain name, the click __ⵗ__ and select __Delete__ .

    ![delete-domain-1](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/skoala/gateway/domain/images/delete-domain-1.png)

- Click the page to enter details of the domain name, domain name at the upper right corner of the page by clicking on the right __ⵗ__ and select __Delete__ .

    ![delete-domain-2](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/skoala/gateway/domain/images/delete-domain-2.png)

    If the domain name is being used by an API, click __Check Service Details__ to delete the corresponding API. 

    ![delete-domain-3](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/skoala/gateway/domain/images/delete-domain-3.png)
