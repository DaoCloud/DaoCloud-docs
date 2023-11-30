# Access Clusters

This page introduces how to access a cluster through kubectl and DCE 5.0 CloudShell.

Clusters integrate into or created in the DCE 5.0 Container Management module can be accessed through the UI interface, CloudShell, and kubectl.

!!! note

    To access a cluster, you should have the [`Cluster Admin`](../clusters/cluster-role.md) permission or higher.

## Access via CloudShell

1. Enter the Container Management module, find your target cluster, click `...` on the right, and select `Console` in the drop-down list.

    ![screen](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/kpanda/images/cluster-access01.png)

2. Run `kubectl get node` command in the Console to verify the connectivity between CloudShell and the cluster. If the console returns node information of the cluster, you can access and manage the cluster through CloudShell.

    <!--![screen](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/kpanda/images/cluster-access01.png)-->

## Access via kubectl

If you want to access and manage remote clusters from a local node, make sure you have met these prerequisites:

- Your local node and the cloud cluster are in a connected network.
- The cluster certificate has been downloaded to the local node.
- The kubectl tool has been installed on the local node. For detailed installation guides, see [Installing tools](https://kubernetes.io/docs/tasks/tools/).

If everything is in place, follow these steps to access a cluster via kubectl from your local environment.

1. Enter the Container Management module, find your target cluster, click `...` on the right, and select `Download kubeconfig` in the drop-down list.

    ![screen](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/kpanda/images/cluster-access02.png)

2. Set the certificate validity period and click `Download kubeconfig`.

    ![screen](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/kpanda/images/cluster-access02.png)

3. Open the downloaded certificate and copy its content to the `config` file of the local node.

    By default, the kubectl tool will look for a file named `config` in the `$HOME/.kube` directory on the local node. This file stores access credentials of clusters. If found, kubectl can access the cluster with that configuration file.

4. Run the following command on the local node to verify its connectivity with the cluster:

    ```sh
    kubectl get pod -n default
    ```

    The expected output is something like:

    ```none
    NAME READY STATUS RESTARTS AGE
    dao-2048-2048-58c7f7fc5-mq7h4 1/1 Running 0 30h
    ```

Now you can access and manage the cluster locally with kubectl.
