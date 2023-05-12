# access cluster

Clusters accessed or created using the DCE 5.0 [Container Management](../../intro/what.md) platform can not only be accessed directly through the UI interface, but also can be controlled in two other ways:

- Online access via CloudShell
- Access through kubectl after downloading the cluster certificate

!!! note
  
    To access the cluster, the user should have the [`Cluster Admin`](../permissions/permission-brief.md) permission or higher.

## Access via CloudShell

1. On the `Cluster List` page, select the cluster that needs to be accessed through CloudShell, click the `...` operation icon on the right and click `Console` in the drop-down list.

    

2. Execute the `kubectl get node` command on the CloudShell console to verify the connectivity between CloudShell and the cluster. As shown in the figure, the console will return the node information under the cluster.

    

You can now access and manage the cluster through CloudShell.

## Access via kubectl

When accessing and managing cloud clusters through local nodes, the following conditions need to be met:

- Network interconnection between local nodes and cloud clusters.
- The cluster certificate has been downloaded to the local node.
- The kubectl tool has been installed on the local node. For detailed installation methods, please refer to Installing [kubectl](https://kubernetes.io/docs/tasks/tools/).

1. On the `Cluster List` page, select the cluster that needs to download the certificate, click `...` on the right, and click `Get Certificate` in the pop-up menu.

    

2. Select the certificate validity period and click `Download Certificate`.

    

3. Open the downloaded cluster certificate, and copy the content of the certificate to the `config` file of the local node.

    By default, the kubectl tool will look for a file named `config` from the `$HOME/.kube` directory of the local node. This file stores the access credentials of the relevant cluster, and kubectl can connect to the cluster with this configuration file.

4. run the following command on the local node to verify the connectivity of the cluster:

    ```sh
    kubectl get pod -n default
    ```

    The expected output is something like:

    ```none
    NAME READY STATUS RESTARTS AGE
    dao-2048-2048-58c7f7fc5-mq7h4 1/1 Running 0 30h
    ```

You can now access and manage the cluster locally with kubectl.