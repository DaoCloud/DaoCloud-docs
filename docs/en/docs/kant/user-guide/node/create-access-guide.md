# Create an Integration Guide

Nodes of the same type can be configured with the same edge node configuration. By creating an integration guide, you can obtain the edge node configuration file and installation program. The relationship between the installation guide and the edge nodes follows a one-to-many relationship, which improves management efficiency and saves operational costs.

The following explains the steps to create an integration guide and manage integration guides.

## Steps

1. On the Edge Node List page, click the **Guide Management** button to enter the guide management list page, then click the **Create Integration Guide** button in the top right corner.

    <!-- ![Guide Management](../../images/integration-guide-01.png) -->

2. Fill in the registration information.

    - Guide Name: The guide name cannot be empty and is limited to 253 characters.
    - Node Prefix: The node name consists of "node prefix-random code".
    - Driver Mode: The control group (CGroup) driver used for resource management and configuration of Pods and containers, such as CPU and memory resource requests and limits.
    - CRI Service Address: The socket file or TCP address for communication between the CRI Client and CRI Server locally, for example, `unix:///run/containerd/containerd.sock`.
    - KubeEdge Edge Image Repository: The repository address for storing KubeEdge components (Mosquitto, installation package, pause) images. If the edge and cloud images are in the same repository, you can click the **Reference Cloud Address** button to quickly fill it in.
    - Description: Description information for the integration guide.
    - Tags: Tags information for the integration guide.

    <!-- ![Create Integration Guide](../../images/integration-guide-02.png) -->

3. After completing the information filling, click the **OK** button to complete the creation of the integration guide.

## Next Steps

After creating the guide, you can view the **Integration Guide** and follow the integration process prompts to complete the onboarding operation for the edge nodes. For details, please refer to the [Node Integration Guide](./integration-guide.md).
