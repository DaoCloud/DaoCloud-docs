# Edge Node Onboarding

According to the node access configuration, obtain the installation files and access commands, and install the EdgeCore edge core software on the node, so that the edge node can establish a connection with DCE Cloud Edge Collaboration and be included in platform management.

When the edge node is first onboarded, the latest version of the EdgeCore edge core software is automatically installed.

!!! note

    - The relationship between the access configuration and the actual edge node machine is one-to-one. The installation files and access commands from one access configuration can only be used on a single actual edge node.
    - This onboarding guide only applies to Cloud Edge Collaboration module v0.20 and later versions. If your version is earlier than v0.20, refer to the archived [Edge Node Onboarding Guide](./access-guide-v0.19.md).

This document mainly describes the single-node onboarding procedure. If you want to onboard nodes in batches quickly, refer to [Batch Onboard Edge Nodes](./batch-access-guide.md).

## Prerequisites

- The node has been prepared as required and the node environment has been configured, please refer to [Requirements to Join Edge Node](./join-rqmt.md) for details.
- The edge node access configuration has been created, please refer to [Create an Access Configuration](./create-access-guide.md) for details.

!!! note

    If you are onboarding heterogeneous nodes in an offline environment, first perform the multi-architecture merge of Helm applications. For the procedure, refer to [Multi-Architecture Merge and Upgrade Import Steps for Helm Applications](../../../kpanda/user-guide/helm/multi-archi-helm.md).

## Steps

1. On the Edge Node List page, click the **Onboard Node** button to enter the node onboarding page.

    ![Node List](../../images/access-guide-06.png)

1. Based on the node environment configuration, select the corresponding access configuration, enter the node name, and then click **Get Onboarding Steps**.

    ![Onboard Node](../../images/access-guide-07.png)

1. Onboard the node by executing the operations for the online or offline onboarding method.

    === "Online Onboarding"

        If your environment can access the Internet, the online onboarding method is recommended.

        1. In the onboarding steps drawer, click the __Online Onboarding__ tab to display the online onboarding steps.

            ![Online Onboarding](../../images/access-guide-08.png)

        1. Use the script to prepare the keadm tool, and execute the command displayed in the interface.

            !!! note

                It is recommended to create an empty working directory first and run the script in that directory.

            ```shell
            curl -sfL https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/keadm_init.sh | sudo MULTI_ARCH=false WITH_CONTAINERD=false bash -s --
            ```

        1. Execute the onboarding command displayed in the interface to onboard the node.

            !!! note

                Pay attention to the validity period of the token in the onboarding command. If the token expires, refresh the page to obtain a new one.

            Command example:

            ```shell
            keadm join \
              --cgroupdriver=cgroupfs \
              --cloudcore-ipport=10.64.24.29:30000 \
              --hub-protocol=websocket \
              --certport=30002 \
              --image-repository=docker.m.daocloud.io/kubeedge \
              --labels=batch-node.kant.io/protocol-type=websocket,kant.io/batch=test \
              --kubeedge-version=v1.20.0 \
              --remote-runtime-endpoint=unix:///run/containerd/containerd.sock \
              --set \
                modules.edgeStream.server=10.64.24.29:30004,\
                modules.edgeStream.enable=true,\
                modules.metaManager.enable=true,\
                modules.metaManager.metaServer.enable=true,\
                modules.serviceBus.enable=true,\
                modules.edgeHub.websocket.server=10.64.24.29:30000 \
              --token=f06150c1f9469047fd459187f6c1eb539b2778373ff874e55786c1c721ff8a29.eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3NTEwNzY3ODd9.ATFgzWCHJhGGTYDwCk7E6SrbXh0STv40JuZwCUgX2H0
            ```

    === "Offline Onboarding"

        If your environment cannot access the Internet, choose the offline onboarding method.

        1. In the onboarding steps drawer, click the __Offline Onboarding__ tab to display the offline onboarding steps.

            ![Online Onboarding](../../images/access-guide-09.png)

        1. Click the **Download File** button, which will redirect you to the download center. In the download list, select the edge installation package and initialization script for the corresponding architecture.

        1. Copy the installation package file and the script file to the same directory on the edge node to be onboarded, and run the initialization script in that directory.

            !!! note

                It is recommended to create an empty working directory to store the related files.

            ```shell
            sudo MULTI_ARCH=false WITH_CONTAINERD=false bash -c keadm_init.sh
            ```

        1. Onboard the node by executing the following command.

            ```shell
            keadm join \
              --cgroupdriver=cgroupfs \
              --cloudcore-ipport=10.64.24.29:30000 \
              --hub-protocol=websocket \
              --certport=30002 \
              --image-repository=docker.m.daocloud.io/kubeedge \
              --labels=batch-node.kant.io/protocol-type=websocket,kant.io/batch=test \
              --kubeedge-version=v1.20.0 \
              --remote-runtime-endpoint=unix:///run/containerd/containerd.sock \
              --set \
                modules.edgeStream.server=10.64.24.29:30004,\
                modules.edgeStream.enable=true,\
                modules.metaManager.enable=true,\
                modules.metaManager.metaServer.enable=true,\
                modules.serviceBus.enable=true,\
                modules.edgeHub.websocket.server=10.64.24.29:30000 \
              --token=f06150c1f9469047fd459187f6c1eb539b2778373ff874e55786c1c721ff8a29.eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3NTEwNzY3ODd9.ATFgzWCHJhGGTYDwCk7E6SrbXh0STv40JuZwCUgX2H0
            ```

1. Verify if the edge node has been successfully onboarded.

    1. Select __Edge Computing__ -> __Cloud-Edge Collaboration__ from the left navigation bar to enter the edge unit list page.

    1. Click the edge unit name to enter the edge unit details page.

    1. Select __Edge Resources__ -> __Edge Nodes__ from the left navigation bar to enter the edge node list page.

    1. Check the status of the edge node. If the current status is __Healthy__, it means the onboarding was successful.

    ![Edge Node Onboarded Successfully](../../images/access-guide-05.png)
