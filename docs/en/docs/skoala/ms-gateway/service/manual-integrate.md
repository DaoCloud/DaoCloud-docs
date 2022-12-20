# Manually access the service

The successfully added service will appear on the service list page, and you can also select the service in the list as the target backend service when adding an API. The microservice gateway supports adding services through manual access and automatic discovery. This page describes how to manually access the service.

**Prerequisites**

You need to add the corresponding service source in the source management <!--to-be-supplemented link--> in advance, so that you can select the corresponding service source type when manually accessing the service.

## access service

1. Click the name of the target gateway on the `Microservice Gateway List` page, enter the gateway overview page, and click `Service Access`-->`Service List` in the left navigation bar.

    ![Service List](imgs/service-list.png)

2. On the `Service List` page, click `Manual Access`-->`Add Service`.

    ![Service List](imgs/manual.png)

3. Select the service source, configure the service connection information, and click `OK`.

    - Cluster service: Select the cluster and namespace where the target service is located, and fill in the access protocol, address, and port.

        ![Add cluster service](imgs/config1.png)

        For the access method of the cluster service, you can click the service name in `Container Management`->`Container Network`->`Service` to view:

        ![Get service access address](imgs/service-access.png)

    - mesh Services:

        The function of accessing mesh services is under development, so stay tuned.

    - Registration Center Service: Select the registration center where the target service is located, and fill in the access protocol, address and port.

        ![Add registry service](imgs/config3.png)

    - External service: fill in service name, access protocol, address, port.
  
        ![Add external service](imgs/config4.png)

## View service details

1. Click the name of the target service on the service list page to enter the service details page.

    ![Service Details](imgs/service-details0.png)

2. Check the service source, connection information, associated API and other information.

    ![Service Details](imgs/service-details2.png)

## Update service

### Update basic information

1. Find the service that needs to be updated on the `Service List` page, click **`ⵗ`** on the right side of the service, and select `Basic Information`.

    ![Update Service](imgs/update1.png)

2. Update the basic information and click `OK`.

    ![Update Service](imgs/update1.png)

!!! danger

    If other services are selected when updating basic information, the original service will be deleted, which is equivalent to adding a new service. But the API associated with the original service will be automatically associated with the new service.

![update-danger](imgs/update-danger.png)

### Update policy configuration

1. Find the service that needs to be updated on the `Service List` page, click **`ⵗ`** on the right side of the service, and select `Policy Configuration`.

    ![Update Service](imgs/update3.png)

2. Update the policy configuration and click `OK`.

    ![Update Service](imgs/update4.png)

## delete service

Find the service to be deleted on the `Service List` page, click **`ⵗ`** on the right side of the service, and select `Delete`.

![delete service](imgs/delete.png)

Before deleting a service, you need to make sure that no APIs are using the service. If the service is being used by an API, you need to follow the page prompts and click `API Management` to delete the associated API before deleting the service.

![Delete service](imgs/delete1.png)