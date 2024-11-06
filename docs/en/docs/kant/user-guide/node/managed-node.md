---
MTPE: FanLin
Date: 2024-01-22
---

# Connect Edge Nodes

Connecting and managing edge nodes refers to the process of installing the EdgeCore software on actual edge nodes based on the installation guide obtained from batch registering edge nodes. This allows the edge nodes to establish a connection with the platform and be managed within it.

When a new edge node is connected, the latest version of the EdgeCore software is automatically installed.

!!! note

    The batch tasks registered on the platform can be used on multiple actual edge nodes. One set of installation files and access commands from a batch task can be used on multiple edge nodes.

## Prerequisites

- The nodes have been prepared according to the requirements and the node environment has been configured as specified in the [Edge Node Access Requirements](./join-rqmt.md).
- The batch task for registering the nodes has been successfully created, and the installation guide has been obtained as described in [Batch Registration of Edge Nodes](./batch-registration.md).

![Installation Guide](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/kant/images/node-managed-01.png)

## Connect Edge Nodes

1. Log in to the edge node with a user account that has sudo privileges.

1. Depending on the runtime environment of the node, execute the corresponding commands to retrieve the installation files from the container registry.

    - Case 1: The edge node can directly access the container registry. The operation is as follows.

        Copy the image address directly from the installation guide::

        ```shell
        release.daocloud.io/kant/kantadm-installation:v0.5.0-dev-7c54ddd4
        ```

        To obtain the installation file, you can refer to the following example:

        ```shell
        docker run --rm release.daocloud.io/kant/kantadm-installation:v0.5.0-dev-7c54ddd4 cat /usr/local/bin/kantadm > /usr/local/bin/kantadm && chmod +x /usr/local/bin/kantadm
        ```

    - Case 2: The edge node cannot access the container registry. The operation is as follows.

        1. On the installation guide interface, click the __Get Installation File__ button in the first step, and the __Get Installation File__ drawer will pop up on the right.

        1. Depending on the runtime environment of the node, copy the following image installation package file to the specified folder.
            
            For the image of Kant installation package:
            
            ```config
            release.daocloud.io/kant/kantadm-installation:v0.5.1
            ```

            For the KubeEdge Mosquitto image:
              
            ```config
            docker.m.daocloud.io/kubeedge/eclipse-mosquitto:1.6.15
            ```

            For the KubeEdge container sandbox image:
            
            ```config
            kubeedge/pause:3.1
            ```

            For the image of KubeEdge installation package:
            
            ```config
            docker.m.daocloud.io/kubeedge/installation-package:v1.12.5
            ```

            Here is an example of the operations:

            1. On a machine that can access the container registry, run the command to get the edge installation resource image.

                ```shell
                docker pull release.daocloud.io/kant/kantadm-installation:v0.5.1
                ```

            1. Package the resource image and upload it to the target node after completion.

                ```shell
                docker save release.daocloud.io/kant/kantadm-installation:v0.5.0-dev-7c54ddd4 > kantadm-installation.tar
                ```

            1. Log in to the node and load the uploaded resource image package.

                ```shell
                docker load -i kantadm-installation.tar
                ```

1. Run the following command to connect the edge node.

    - Register via token.

        ```shell
        kantadm join --cloudcore-host=10.31.226.14 --websocket-port=30000 --node-prefix=edge --token=b2d6bb5d9312c39ffac08ecfd5030bed006b8b67d0799d632d381f19fca9e765.eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2OTQ2NTk3NDV9.0sdaWbYSTURmAYmQwDn_zF7P9TwcRTSMhwPw6l87U7E --cgroup-driver=cgroupfs --remote-runtime-endpoint= --version=v1.12.2 --batch-name=edge --edge-registry=docker.m.daocloud.io/kubeedge --quic-port=30001 --http-port=30002 --stream-port=30003  --tunnel-port=30004 --labels=test=1,test1=1
        ```

    - Register via certificate.

        1. On the installation guide page, click __Certificate Installation__ in Step 2 to display the installation prompt information.

        2. Click the __Download Certificate__ button to download the certificate to your local machine.

        3. Save the certificate and run the following command:

            ```shell
            mkdir -p /etc/kant && mv ./cert.tar /etc/kantcert.tar
            ```

        4. Connect the managed node by executing the following command:

            ```shell
            kantadm join --cloudcore-host=10.31.226.14 --websocket-port=30000 --node-prefix=edge --remote-runtime-endpoint= --cgroup-driver=cgroupfs --version=v1.12.2 --batch-name=edge --edge-registry=docker.m.daocloud.io/kubeedge --quic-port=30001 --http-port=30002 --stream-port=30003 --tunnel-port=30004 --labels=test=1,test1=1
            ```

1. Verify if the edge node has been successfully connected.

    1. Select __Edge Computing__ -> __Cloud Edge Collaboration__ from the left navigation bar to access the Edge Unit list page.

    2. Click the name of an edge unit to view its details.

    3. Select __Edge Resources__ -> __Edge Nodes__ from the left navigation bar to access the Edge Node list page.

    4. Check the status of the edge node. If the current status is "Healthy," it indicates a successful connection.

        ![Successful Management of Edge Node](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/kant/images/node-managed-02.png)
