# Microservice namespace

Microservice namespaces can be used to isolate services, configuration, and other resources in different environments, such as production, development, and testing. The namespace in the microservice engine module refers to the microservice namespace, that is, the namespace in the [Nacos](https://nacos.io/docs/what-is-nacos.html) context, not in the Kubernetes scenario.

!!! note

    - When you create a managed registry instance, the system automatically creates a default namespace named ** public **. The namespace cannot be edited or deleted. It belongs to the reserved namespace of the system.
    - Services and configurations in different namespaces are strictly isolated and cannot reference each other. For example, A service in namespace A cannot reference a configuration in namespace B.

## Create the microservice namespace

1. Enter `Microservices` -> __Traditional Microservices__ -> __Hosted Registry__ module, click the name of the target registry.

    ![](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/skoala/images/ns-1.png)

2. Click __Microservice Namespace__ in the left navigation bar, then click __Create__ in the upper right corner.

    ![](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/skoala/images/create-ns-1.png)

3. Enter the ID, and name and click __OK__ in the lower right corner of the page.

    If you do not enter an ID, the system automatically generates an ID.
    **The namespace ID cannot be changed after creation.**

    ![](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/skoala/images/create-ns-2.png)

## Update the microservice namespace

1. In the right operation bar of the corresponding namespace, click __Edit__ to enter the update page.

    ![](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/skoala/images/update-ns-1.png)

2. To modify the namespace name, click __OK__ .

    ![](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/skoala/images/update-ns-2.png)

## Delete the microservice namespace

Click __Delete__ in the right operation bar of the corresponding namespace, and then click __Delete Now__ in the pop-up box.

!!! note

    Before deleting a namespace, it is necessary to clean up all the resources within that namespace. Otherwise, the namespace cannot be deleted.

![](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/skoala/images/delete-ns-1.png)
