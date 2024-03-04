# Update/Delete domain

The microservice gateway supports the full lifecycle management of domains, including adding, updating, and deleting domains. Through domain management, you can apply a domain to multiple apis of the gateway and configure gateway policies at the domain level.

## Update

You can modify the basic information and policy configuration of a domain in two ways.

- In the __Domain Management__ page find need to update the domain, on the right side click __ⵗ__  choose __Edit Basic Settings__ or  __Edit Policy Settings__ or  __Edit Security Settings__ .
     
    ![Update the basic information on the list page](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/skoala/gateway/domain/images/update-domain-1.png) 

- Click the domain to go to the domain details page. Click __Edit Basic Settings__ at the upper right corner of the page to update basic information and  __Edit Policy Settings__ to update policy and  __Edit Security Settings__ to update security settings.

    ![Updated on the details page](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/skoala/gateway/domain/images/update-domain-2.png)

## Delete

!!! danger

    - A domain name that is being used by the API cannot be deleted. You need to delete the API before deleting the domain name.
    - The domain name cannot be restored after being deleted.

You can delete a domain name in two ways.

- In the __Domain Management__ page to find the need to delete the domain name, the click __ⵗ__  and select __Delete__ .

    ![delete-domain-1](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/skoala/gateway/domain/images/delete-domain-1.png)

- Click the page to enter details of the domain name, domain name at the upper right corner of the page by clicking on the   __ⵗ__  hold and select __Delete__ .

    ![delete-domain-2](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/skoala/gateway/domain/images/delete-domain-2.png)

    If the domain name is being used by an API, click __Check Service Details__ to delete the corresponding API. 

    ![delete-domain-3](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/skoala/gateway/domain/images/delete-domain-3.png)
