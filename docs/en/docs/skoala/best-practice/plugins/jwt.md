# Using JWT Plugin in Cloud-Native Microservices

DCE 5.0 Microservice Engine supports the use of the JWT plugin in cloud-native microservices to add security authentication to services.

## Prerequisites

To use the JWT plugin in cloud-native microservices, the following prerequisites must be met.

### Create a Service Mesh

First, you need to create a service mesh for the cluster where the target service resides in the Service Mesh module of DCE 5.0.
Currently, three types of meshes are supported: Managed Mesh, Dedicated Mesh, and External Mesh.

For specific steps on creating a mesh, refer to [Creating a Managed/Dedicated Mesh](../../../mspider/user-guide/service-mesh/README.md) or [Creating an External Mesh](../../../mspider/user-guide/service-mesh/external-mesh.md).



### Enable Sidecar Injection

Deploy the application in the target cluster and enable sidecar injection for the demo application in the service mesh.



!!! note

    - Since the demo uses the opentelemetry-demo-lite service, the application is deployed using Helm templates.
    - If you are using a different service, you can deploy the application in the cluster using [Creating Workloads](../../../kpanda/user-guide/workloads/create-deployment.md) or [Helm Templates](../../../kpanda/user-guide/helm/helm-app.md) or other methods.

### Bind Workspace to the Mesh

Bind a workspace to the target mesh to allow the mesh to use resources from the corresponding workspace.



### Connect Services in the Microservice Engine

Go to the Microservice Engine module and import the demo application into the cloud-native microservice module. For detailed steps, refer to [Importing Services](../../cloud-ms/index.md).



## Connect and Bind the Plugin

After meeting the above prerequisites, connect the JWT plugin and bind it to the microservice port to use the plugin in the microservice.

1. Go to the Microservice Engine, click on `Plugin Center` in the left navigation bar, and then click `Connect Plugin` in the upper right corner of the page.



2. Fill in the plugin configuration and click `Confirm` in the lower right corner of the page.



3. In the left navigation bar of the Microservice Engine, click on `Cloud-Native Microservices`, and then click on the name of the target service.



4. In the service details, click on the `Plugin Capability` tab, and then click on `Plugin Capability` on the right.



5. Fill in the plugin configuration and bind the plugin to the service port.



## Verify the Plugin Effect

After completing the above steps, you can verify the plugin effect by calling the service. As expected, you must include the authentication request header to successfully access the service; otherwise, the service cannot be accessed.

1. Access the service without the request header, and it will return "missing", indicating that the service cannot be accessed, which is the expected result.



2. Access the service again with the authentication request header, and this time it will return the interface content correctly, confirming the expected result.

