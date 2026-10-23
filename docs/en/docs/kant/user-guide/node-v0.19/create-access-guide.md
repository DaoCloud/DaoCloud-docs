# Create an Access Configuration

Nodes of the same type can be configured with the same edge node configuration. By creating an access configuration, you can obtain the edge node configuration file and installation program.
The relationship between the access configuration and the edge nodes is one-to-many, which improves management efficiency and saves operational costs.

The following describes the steps to create an access configuration and how to manage access configurations.

## Steps

1. Click the **Edge Node** menu in the left navigation bar to enter the page, select **Access Configuration** to enter the configuration management list page, and click the **Create Access Configuration** button in the top right corner.

    ![Guide Management](../../images/access-guide-01.png)

2. Fill in the registration information.

    - Guide Name: The guide name cannot be empty and is limited to 253 characters.
    - Node Prefix: The node name consists of "node prefix-random code".
    - Driver Mode: The control group (CGroup) driver used for resource management and configuration of Pods and containers, such as CPU and memory resource requests and limits.
    - CRI Service Address: The socket file or TCP address for communication between the CRI Client and CRI Server locally, for example, `unix:///run/containerd/containerd.sock`.
    - KubeEdge Edge Container Registry: The repository address for storing KubeEdge components (Mosquitto, installation-package, pause) images. If the edge and cloud images are in the same repository, you can click the **Reference Cloud Address** button to quickly fill it in.
    - Description: Description information for the access configuration.
    - Tags: Tags information for the access configuration.

    ![Create Access Configuration](../../images/access-guide-02.png)

3. After completing the information, click the **OK** button to complete the creation of the access configuration.

## Next Steps

After creating the access configuration, you can view the **Access Configuration** on its details page and follow the onboarding process prompts to complete the onboarding operation for the edge nodes. For details, please refer to the [Node Onboarding Guide](./access-guide.md).
