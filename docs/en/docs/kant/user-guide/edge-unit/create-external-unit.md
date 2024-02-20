# Creating External Edge Unit

**External Edge Unit** refers to integrating the existing KubeEdge installed in the enterprise system into DCE 5.0 Cloud Edge for unified management.

KubeEdge: An open-source system that extends native containerized application orchestration capabilities to edge nodes.

- CloudCore: The core component of KubeEdge on the cloud side.
- ControllerManager: KubeEdge CRD extension currently used for edge applications and edge node groups.

The following explains the steps to create an external edge unit:

1. Select __Cloud Edge__ from the left navigation bar to enter the edge unit list page. Click the __Create Edge Unit__ button at the top right of the page, and select __Create External Edge Unit__ from the dropdown list;

    <!-- Add image soon -->

2. Fill in the basic information;

    - Edge Unit Name: A combination of lowercase letters, numbers, hyphens (-), and dots (.), with no consecutive symbols; must start and end with a letter or number; can contain up to 253 characters.
    - Cluster: The cluster running the edge unit control plane.
    - KubeEdge Version: A specific version of the KubeEdge open-source system for extending containerized application orchestration capabilities to edge hosts, built on Kubernetes and providing infrastructure support for network applications.

    <!--- Edge Component Replicas: The number of replicas of cloud-side edge components to ensure high availability of edge components in case of cloud-side node failures.-->

    - Description: Description information of the edge unit.

    <!-- Add image soon  -->

3. Component repository settings. Settings for KubeEdge and Kant cloud-side component repositories;

    - Kant Image Repository: The image repository required by the system for cloud-side components, where Kant refers to the Cloud Edge module.
        - Default: The default image repository address provided by the system, storing the images of cloud-side components required by the Cloud Edge module, such as kant-worker-admission;
        - Custom: If users store the system's cloud-side component images in their own image repository, they can choose a custom repository address.

    - Kant Helm Repository: The helm application repository required by the system for cloud-side components, where Kant refers to the Cloud Edge module. If the desired helm repository is not available in the dropdown options, click the __Create Repository__ button on the right to create a new helm repository.

    - KubeEdge Image Repository (optional): KubeEdge cloud-side component image repository.

    !!! note

        When edge nodes are accessed, the KubeEdge edge-side image repository can reference the cloud-side address, which is recommended to be filled in.

    <!-- Add image soon -->

4. Access configuration. Settings for accessing KubeEdge cloud-side components, allowing edge nodes to establish connections with the cloud side;

    - Access Address: The access address of the CloudCore component of KubeEdge on the cloud side, which needs to be accessible by edge nodes.

    - Ports:

        - WebSocketPort: WebSocket protocol port for access, default is 10000.
        - QUICPort: QUIC protocol port for access, default is 10001.
        - HTTPServerPort: HTTP service port, default is 10002.
        - CloudStreamPort: Port for cloud-side streaming interface, default is 10003.
        - TunnelPort: Port for edge node business data channel, default is 10004.

    !!! note

        If there is a conflict with the NodePort port, please modify it.

    <!-- Add image soon -->

5. After completing the above information configuration, click the __OK__ button to finish creating the edge unit, and automatically return to the edge unit list.

Next step: [Managing Edge Units](./manage-unit.md)
