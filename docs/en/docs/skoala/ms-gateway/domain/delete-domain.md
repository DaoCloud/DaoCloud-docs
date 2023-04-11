# delete domain name

The microservice gateway supports full lifecycle management of domain names hosted in a unified manner, including adding, updating, and deleting domain names. Through domain name management, a domain name can be applied to multiple APIs in the gateway, and gateway policies at the domain name level can be configured.

!!! danger

    - The domain name being used by the API cannot be deleted. You need to delete the related API before deleting the domain name.
    - Once a domain name is deleted, it cannot be restored.

There are two ways to delete a domain name.

- Find the domain name that needs to be deleted on the `Domain Management` page, click **`ⵗ`** and select `Delete`.

    

- Click the domain name to enter the details page of the domain name, click the **`ⵗ`** operation in the upper right corner of the page and select `Delete`.

    

    If the domain name is being used by an API, you need to be prompted on the page to click `View Service Details` to delete the corresponding API. <!--Update the description after the ui is updated-->

    