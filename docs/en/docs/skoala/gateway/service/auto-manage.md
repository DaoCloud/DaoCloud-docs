# Automatic management service

The services that are successfully added will be displayed on the service list page. You can also select the services in the list as the target back-end services when adding apis. The microservice gateway supports manual access and automatic management to add services. This page describes how to automatically manage services.

After [created a gateway](../index.md) succeeds, the services in the service source are automatically added to the service list of the gateway instance without manual addition.

## View automatic managed services

1. In the __Gateway List__ page click the name of the target gateway, enter the gateway overview page, in the left navigation bar click __Add Service__ -> __Service List__ .

    ![service list](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/skoala/gateway/service/images/service-list.png)

2. On the __Service List__ page click __Auto Add__ .

    ![automatic discovery service](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/skoala/gateway/service/images/auto.png)

## Configure service policy

1. In the __Service List__ -> __Auto Add__ page to find the target service, on the right side click __ⵗ__ , choose __Policy Settings__ .

    ![policy configuration](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/skoala/gateway/service/images/policy1.png)

2. To adjust the service policy configuration as required, click __OK__ in the lower right corner of the pop-up box.

    - HTTPS certificate verification: After HTTPS is enabled, you must pass certificate verification to access the service successfully.
    - Service circuit breaker: When the maximum number of connections, processing connections, parallel requests, and parallel retries Any one reaches the threshold, service calls are automatically cut off to protect the overall system availability. When the metric drops to a set threshold, calls to the service are automatically resumed.

    ![policy configuration](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/skoala/gateway/service/images/policy2.png)

## View service details

1. Locate the target service on the __Service List__ -> __Auto Add__ page and click the service name.

    ![service details](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/skoala/gateway/service/images//service-details.png)

2. View information such as the service name, source, and associated API. Supports sorting by installing __Last Update__ .

    ![service details](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/skoala/gateway/service/images/service-details1.png)

!!! info
    
    For automatically managed services, only the preceding operations are supported. Update or delete services are not supported
