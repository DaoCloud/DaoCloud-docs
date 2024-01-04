# Update/Delete domain

The microservice gateway supports the full lifecycle management of domains, including adding, updating, and deleting domains. Through domain management, you can apply a domain to multiple apis of the gateway and configure gateway policies at the domain level.

## Update

You can modify the basic information and policy configuration of a domain in two ways.

- In the `Domain Management` page find need to update the domain, on the right side click  `ⵗ`  choose `Edit Basic Settings` or `Edit Policy Settings` or `Edit Security Settings`.
     
    ![Update the basic information on the list page](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/skoala/gateway/domain/images/update-domain-1.png) 

- Click the domain to go to the domain details page. Click `Edit Basic Settings` at the upper right corner of the page to update basic information and `Edit Policy Settings` to update policy and `Edit Security Settings` to update security settings.

    ![Updated on the details page](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/skoala/gateway/domain/images/update-domain-2.png)

## Delete

!!! danger

    - A domain name that is being used by the API cannot be deleted. You need to delete the API before deleting the domain name.
    - The domain name cannot be restored after being deleted.

You can delete a domain name in two ways.

- In the `Domain Management` page to find the need to delete the domain name, the click  `ⵗ`  and select `Delete`.

    ![delete-domain-1](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/skoala/gateway/domain/images/delete-domain-1.png)

- Click the page to enter details of the domain name, domain name at the upper right corner of the page by clicking on the  `ⵗ`  hold and select `Delete`.

    ![delete-domain-2](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/skoala/gateway/domain/images/delete-domain-2.png)

    If the domain name is being used by an API, click `Check Service Details` to delete the corresponding API. 

    ![delete-domain-3](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/skoala/gateway/domain/images/delete-domain-3.png)
