# Access cluster

Clusters accessed or created using the DCE 5.0 [Container Management](../../03ProductBrief/WhatisKPanda.md) platform can not only be accessed directly through the UI interface, but also can be accessed through two other methods:

- Online access via CloudShell
- Access through kubectl after downloading the cluster certificate

## Prerequisites

- Ability to access the UI interface of container management, and create or join a cluster in container management.
- The current operating user should have [`Cluster Admin`](../Permissions/PermissionBrief.md) permission or higher.

## Access the cluster via CloudShell

1. On the `Cluster List` page, select the cluster to be accessed through CloudShell, click the `...` operation icon on the right and click `Console` in the drop-down list.

    ![Invoke CloudShell console](../../images/access-cloudshell.png)

2. Execute the `kubectl get node` command on the CloudShell console to verify the connectivity between CloudShell and the cluster. As shown in the figure, the console will return the node information under the cluster.

    ![Verify Connectivity](../../images/access-get-node.png)

You can now access and manage the cluster through CloudShell.

## Access via cluster certificates and kubectl

If you need to access and manage the cloud cluster through a local node, you need to download the cluster certificate to the local node, and then use the kubectl tool to access the cluster.
Before starting, the following conditions need to be met:

- Ensure the network interconnection between local nodes and cloud clusters.
- Make sure the kubectl tool is installed on the local node. For detailed installation methods, please refer to Installing [kubectl](https://kubernetes.io/docs/tasks/tools/).

### Download cluster certificate

1. On the `Cluster List` page, select the cluster that needs to download the certificate, click `...` on the right, and click `Get Certificate` in the pop-up menu.

    ![Enter the download certificate page](../../images/access-get-cert.png)

2. Select the certificate validity period and click `Download Certificate`.

    ![Download Certificate](../../images/access-download-cert.png)

### Access the cluster through kubectl

By default, the kubectl tool will look for a file named `config` from the `$HOME/.kube` directory of the local node.
This file stores the access credentials of the relevant cluster, and kubectl can use this configuration file to connect to the cluster.

1. Find and open the downloaded cluster certificate, and copy its content to the `config` file of the local node.

2. Execute the following command on the local node to verify the connectivity of the cluster:

    ```sh
    kubectl get pod -n default
    ```

    The expected output is something like:

    ```none
    NAME READY STATUS RESTARTS AGE
    dao-2048-2048-58c7f7fc5-mq7h4 1/1 Running 0 30h
    ```

You can now access and manage the cluster locally with kubectl.