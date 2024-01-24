# Scaling the Worker Nodes of the Global Service Cluster

This article will explain how to manually scale the worker nodes of the global service cluster in offline mode.
By default, it is not recommended to scale the global service cluster after deploying the platform.
Please plan your resources before deploying the platform.

!!! note

    Note: The control nodes of the global service cluster do not support scaling.

## Prerequisites

- DCE platform deployment has been completed through [Bootstrap Node](../../install/commercial/deploy-arch.md),
  and the kind cluster on the Bootstrap Node is running normally.
- You must log in with a user account that has admin privileges on the platform.

## Obtain the kubeconfig for the kind cluster on the Bootstrap Node

1. Run the following command to log in to the Bootstrap Node:

    ```bash
    ssh root@seed-node-ip-address
    ```

2. On the Bootstrap Node, run the following command to get the __CONTAINER ID__ of the kind cluster:

    ```bash
    [root@localhost ~]# podman ps

    # Expected output:
    CONTAINER ID  IMAGE                                      COMMAND     CREATED      STATUS      PORTS                                                                                                         NAMES
    220d662b1b6a  docker.m.daocloud.io/kindest/node:v1.26.2              2 weeks ago  Up 2 weeks  0.0.0.0:443->30443/tcp, 0.0.0.0:8081->30081/tcp, 0.0.0.0:9000-9001->32000-32001/tcp, 0.0.0.0:36674->6443/tcp  my-cluster-installer-control-plane
    ```

3. Run the following command to enter the kind cluster container:

    ```bash
    podman exec -it {CONTAINER ID} bash # Replace {CONTAINER ID} with your actual container ID
    ```

4. Inside the kind cluster container, run the following command to obtain the kubeconfig configuration
   information for the kind cluster:

    ```bash
    kubectl config view --minify --flatten --raw # Replace {CONTAINER ID} with your actual container ID
    ```
   After the console output, copy the kubeconfig configuration information of the kind cluster for the next step.

## Create `cluster.kubean.io` resources in the kind cluster on the Bootstrap Node

1. Use the __podman exec -it {CONTAINER ID} bash__ command to enter the kind cluster container.

2. Copy and run the following command to create the `cluster.kubean.io` resources in the kind cluster:

    ```bash
    kubectl apply -f - <<EOF
    apiVersion: kubean.io/v1alpha1
    kind: Cluster
    metadata:
      labels:
        clusterName: kpanda-global-cluster
      name: kpanda-global-cluster
    spec:
      hostsConfRef:
        name: my-cluster-hosts-conf
        namespace: kubean-system
      kubeconfRef:
        name: my-cluster-kubeconf
        namespace: kubean-system
      varsConfRef:
        name: my-cluster-vars-conf
        namespace: kubean-system
    EOF
    ```

3. Run the following command in the kind cluster to verify if the `cluster.kubean.io` resource
   is created successfully:

    ```bash
    root@my-cluster-installer-control-plane:/# kubectl get clusters

    # Expected output:
    NAME                    AGE
    kpanda-global-cluster   3s
    my-cluster              16d
    ```

## Update the containerd configuration in the kind cluster on the Bootstrap Node

1. Run the following command to log in to one of the control nodes of the global service cluster:

    ```bash
    ssh root@global-service-cluster-control-node-ip-address
    ```

2. On the control node of the global service cluster, run the following command to copy the containerd configuration file __config.toml__ from the control node to the Bootstrap Node:

    ```bash
    scp /etc/containerd/config.toml root@{seed-node-ip-address}:/root
    ```

3. On the Bootstrap Node, run the following command to copy the __config.toml__ configuration file to the kind cluster:

    ```bash
    cd /root
    podman cp config.toml {CONTAINER ID}:/etc/containerd # Replace {CONTAINER ID} with your actual container ID
    ```

4. Inside the kind cluster, run the following command to restart the containerd service:

    ```bash
    systemctl restart containerd
    ```

## Add the kind cluster to the DCE cluster list

1. Log in to the DCE management console, go to Container Management, click the "Access Cluster "Add" button on the right side of the cluster list page to enter the cluster access page.

2. In the access configuration section, enter and edit the kubeconfig configuration of the kind cluster that was copied earlier. The following parameters need to be configured:

    * __Cluster Name__ : Enter the name for the accessed cluster, default is __my-cluster__ .
    * __insecure-skip-tls-verify: true__ : Used to skip TLS verification, manually add this parameter.
    * __server__ : Replace the IP in the default parameter `https://my-cluster-installer-control-plane:6443` with the IP of the Bootstrap Node. Replace __6443__ with the port mapped on the node. You can use the command __podman ps | grep 6443__ to check.

3. Click the "Confirm" button to complete the access of the kind cluster.

## Add labels to the global service cluster

1. Log in to the DCE management console, go to Container Management, find the __kapnda-glabal-cluster__ cluster,
   and click the __Basic Configuration__ operation button on the right side to enter the basic configuration page.

2. On the basic configuration page, add the label `kpanda.io/managed-by=my-cluster` to the global service cluster,
   as shown in the following image:

!!! note

    Note: In the label "kpanda.io/managed-by=my-cluster", the value corresponds to the cluster name specified during cluster access, which is __my-cluster__ by default. Adjust it according to your actual situation.

## Add nodes to the global service cluster

1. Go to the node list page of the global service cluster, find the __Integrate Node__ button
   on the right side of the node list, and click to enter the node configuration page.

2. Enter the IP and authentication information of the node to be added.

3. Add the following custom parameters in the __Custom Parameters__ section:

    ```bash
    download_run_once: false
    download_container: false
    download_force_cache: false
    download_localhost: false
    ```

4. Click the __OK__ button and wait for the node to be added.
