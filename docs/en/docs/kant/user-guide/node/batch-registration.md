# Batch Register Edge Nodes

Nodes of the same type can have the same edge node configuration by creating a batch task to obtain the edge node configuration file and installer. Batch registering nodes allows for efficient management and reduces operational costs.

The following steps explain how to perform batch registration of edge nodes.

## Create Batch Task

1. On the Edge Node List page, click the __Batch Management__ button to enter the __Batch Management__ page.


## Managing Departmental Batch Workloads After Node Group Changes

### Application Synchronization to New Nodes
Provide detailed instructions on how applications can be automatically or manually synchronized to newly added nodes after a node group change. Include the tools or commands used for synchronization.

### Differentiated Configuration Adjustments
Offer steps for making differentiated configuration adjustments post-deployment to ensure that the new node configurations are consistent with the existing environment, reducing potential configuration conflicts.

### New Application Deployment
    ![Batch Management](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/kant/images/batch-register01.png)

1. Select the __Batch Register__ tab and click the __Create Batch Job__ button in the upper right corner.

    ![Batch Management](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/kant/images/batch-register02.png)

1. Fill in the registration information.

    - Task Name: The name of the batch task, which cannot be empty and has a length limit of 253 characters.
    - Name Prefix: The nodes accessed through the batch task will have names consisting of the "prefix + random code".
    - CGroup Driver: The control group (CGroup) driver used for managing resources and configurations of pods and containers, such as CPU and memory resource requests and limits.
    - CRI Service Address: The socket file or TCP address for local communication between CRI Client and CRI Server, for example, `unix:///run/containerd/containerd.sock`.
    - KubeEdge Container Registry: The container registry for KubeEdge cloud components, automatically filled with the KubeEdge container registry address set in the edge unit but can be modified by the user.
    - Description: Description of the batch task.
    - Labels: Labels for the batch task.

    ![Create Batch Task](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/kant/images/batch-register03.png)

1. After completing the registration information, click the __OK__ button to finish creating the batch task for the nodes.

## What's Next

After registration is complete, you will be automatically redirected to the __Installation Guide__ page,
where you need to perform the onboarding operation for the edge nodes.
For more details, please refer to the [Onboarding Edge Nodes](./managed-node.md) documentation.
