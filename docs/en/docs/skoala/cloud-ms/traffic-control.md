# Service Governance

Before you start to govern cloud-native microservices, you need to import the services first.
Currently, only the services under a mesh in the [DCE Service Mesh](../../mspider/intro/index.md) module can be imported.

## Import Service

Supported

1. Enter the __Microservice Engine__ module, click __Cloud Native Microservices__ -> __Traffic Control__ on the left,
   and then click __Manual Import__ in the upper right corner.

    ![](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/skoala/images/cloudms-import01.png)

2. Filter the service mesh and namespace where the target service is located, select the service, and then click __OK__ .

    ![](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/skoala/images/cloudms-import02.png)

## View Service

View all the imported cloud-native microservices. Click a service name to further view the exposed ports and protocols of the service.

![](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/skoala/images/cloudms-import03.png)

## Remove Service

Remove the microservices that are no longer needed in the operation column on the right.

![](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/skoala/images/cloudms-import04.png)

Service governance refers to the east-west traffic governance of the services in the
[DCE Service Mesh](../../mspider/intro/index.md) based on Service Mesh.

After the mesh services are imported into the cloud-native microservice engine, you can set
different east-west traffic policies for different exposed ports of the service.

1. Click a service name.

    ![](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/skoala/images/cloudms-traffic01.png)

2. Go to the governance capability page.

    ![](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/skoala/images/cloudms-traffic02.png)

3. Create rules on the port as needed, and finally click __OK__ 

<!-- Specific descriptions of each policy will be added later -->
