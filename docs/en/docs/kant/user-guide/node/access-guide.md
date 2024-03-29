# Edge Node Onboarding

According to the node access guide, obtain the installation files and access commands, install the EdgeCore edge core software on the node, so that the edge node can establish a connection with the platform and be included in platform management.

When the edge node is first onboarded, the latest version of the EdgeCore edge core software is automatically installed.

!!! note

    The relationship between the access guide and the actual edge node machine is one-to-many. The installation files and access commands from one access guide can be used on multiple actual edge nodes.

## Prerequisites

- The node has been prepared as required and the node environment has been configured, please refer to [Edge Node Access Requirements](./join-rqmt.md) for details
- The edge node access guide has been created, please refer to [Creating an Access Guide](./create-access-guide.md) for details

<!-- Add screenshot later -->

## Steps

1. On the Edge Node List page, click the **Access Guide** button, and a pop-up window with the access guide will appear on the right.

1. Based on the node environment configuration, select the corresponding access guide.

1. Click the **Download File** button, which will redirect you to the download center. In the download list, select the edge installation package corresponding to the version and architecture: `kantadm_{version}_{architecture}.tar.gz`. It is recommended to choose the latest version.

    <!-- Add screenshot later -->

1. Copy the edge installation package to the edge node to be accessed and unzip it.

    Unzip command:

    ```shell
    tar -zxf kantadm_{version}_{architecture}.tar.gz
    ```

    !!! note

        Place the unpacked kantadm binary file in the `/usr/local/bin` directory.

1. Access the node by executing the command using either a token or certificate.

    **Token Installation**

    1. On the access guide interface, click the __Token Installation__ tab in the third step to display the token installation steps.

        !!! note

            The token in the installation command is valid for 24 hours. For a long-term valid installation method, please use certificate installation.

    1. Access the node by executing the following command.

        ```shell
        kantadm join --cloudcore-host=10.31.226.14 --websocket-port=30000 --node-prefix=edge --token=b2d6bb5d9312c39ffac08ecfd5030bed006b8b67d0799d632d381f19fca9e765.eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2OTQ2NTk3NDV9.0sdaWbYSTURmAYmQwDn_zF7P9TwcRTSMhwPw6l87U7E --cgroup-driver=cgroupfs --remote-runtime-endpoint= --version=v1.12.2 --batch-name=edge --edge-registry=docker.m.daocloud.io/kubeedge --quic-port=30001 --http-port=30002 --stream-port=30003  --tunnel-port=30004 --labels=test=1,test1=1
        ```

    **Certificate Installation**

    1. On the access guide interface, click the __Certificate Installation__ tab in the third step to display the certificate installation steps.

    1. Click the __Download Certificate__ button to download the certificate to your local machine.

    1. Save the certificate and execute the following command.

        ```shell
        mkdir -p /etc/kant && mv ./cert.tar /etc/kant/cert.tar
        ```

    1. Access the node by executing the following command.

        ```shell
        kantadm join --cloudcore-host=10.2.129.13 --websocket-port=30000 --node-prefix=sh --remote-runtime-endpoint=unix:///run/containerd/containerd.sock --cgroup-driver=cgroupfs --version=v1.12.6 --batch-name=guide-test --edge-registry=docker.m.daocloud.io/kubeedge --quic-port=30001 --http-port=30002 --stream-port=30003 --tunnel-port=30004
        ```

1. Verify if the edge node has been successfully onboarded.

    1. Select __Edge Computing__ -> __Cloud-Edge Collaboration__ from the left navigation bar to enter the edge unit list page.

    1. Click on the edge unit name to enter the edge unit details page.

    1. Select __Edge Resources__ -> __Edge Nodes__ from the left navigation bar to enter the edge node list page.

    1. Check the status of the edge node. If the current status is __Healthy__, it means the onboarding was successful.

        <!-- Add screenshot later -->
