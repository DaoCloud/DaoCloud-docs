# Installing DCE 5.0 Enterprise Package on Alibaba Cloud ECS

This page will guide you through the process of installing DCE 5.0 on Alibaba Cloud ECS.

## Prerequisites

- Prepare Alibaba Cloud ECS virtual machines. In this example, we will create three Ubuntu 22.10 Server 64-bit instances, each with a configuration of 8 cores and 16 GB RAM.
- Complete the necessary preparations as described in the [preparation guide](../commercial/prepare.md).

## Deployment Steps

When deploying DCE 5.0 on Alibaba Cloud ECS, special handling is required for load balancing capability. Since CloudProvider is not installed in the virtual machines, LoadBalancer-type services cannot be recognized. Therefore, we provide three possible solutions:

- Solution 1: NodePort + Alibaba Cloud SLB
- Solution 2: cloudLB + CCM component deployment
- Solution 3: NodePort + CCM component deployment

### Solution 1: NodePort + Alibaba Cloud SLB

1. Log in to a machine and download the dce5-installer binary file.

    Assuming VERSION is v0.13.0:

    ```shell
    export VERSION=v0.13.0
    curl -Lo ./dce5-installer https://proxy-qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/dce5-installer-$VERSION
    chmod +x ./dce5-installer
    ```

2. Configure the cluster configuration file `clusterConfig.yaml`.

    Use the following configuration, making sure to set `loadBalancer.type = NodePort` and fill in the private IP addresses of the hosts:

    ```yaml title="clusterConfig.yaml"
    apiVersion: provision.daocloud.io/v1alpha3
    kind: ClusterConfig
    spec:
      loadBalancer:
        type: NodePort
      masterNodes:
        - nodeName: "g-master1"
          ip: xx.xx.xx.xx
          ansibleUser: "root"
          ansiblePass: "dangerous"
        - nodeName: "g-master2"
          ip: xx.xx.xx.xx
          ansibleUser: "root"
          ansiblePass: "dangerous"
        - nodeName: "g-master3"
          ip: xx.xx.xx.xx
          ansibleUser: "root"
          ansiblePass: "dangerous"
    ```

3. Begin the installation.

    ```shell
    ./dce5-installer cluster-create -c sample/clusterConfig.yaml
    ```

4. Installation successful.

    ![success](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/install/images/4.1.png)

5. Check the NodePort port on which the `istio-ingressgateway` service is exposed. In this example, it's 32060.

    ```shell
    kubectl get svc -A | grep NodePort
    ```

    ![gateway](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/install/images/5.1.png)

6. Create an Alibaba Cloud SLB and direct the public TCP traffic of the SLB to the ECS hosts' port 32060. This needs to be done for all three hosts.


7. Modify the ghippo reverse proxy configuration following the documentation at [Custom Reverse Proxy Server Address](../../ghippo/install/reverse-proxy.md#_1). After modification, you can directly access DCE 5.0 using the SLB's public IP address + Port, as shown in the following image:

    ![ghippo](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/install/images/7.1.png)

### Solution 2: cloudLB + CCM Component Deployment

1. Log in to a machine and download the dce5-installer binary file.

    Assuming VERSION is v0.13.0:

    ```shell
    export VERSION=v0.13.0
    curl -Lo ./dce5-installer https://proxy-qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/dce5-installer-$VERSION
    chmod +x ./dce5-installer
    ```

2. Configure the cluster configuration file `clusterConfig.yaml`.

    Use the following configuration, making sure to set `loadBalancer.type = cloudLB` and fill in the private IP addresses of the hosts:

    ```yaml title="clusterConfig.yaml"
    apiVersion: provision.daocloud.io/v1alpha3
    kind: ClusterConfig
    spec:
      loadBalancer:
        type: cloudLB
      masterNodes:
        - nodeName: "g-master1"
          ip: xx.xx.xx.xx
          ansibleUser: "root"
          ansiblePass: "dangerous"
        - nodeName: "g-master2"
          ip: xx.xx.xx.xx
          ansibleUser: "root"
          ansiblePass: "dangerous"
        - nodeName: "g-master3"
          ip: xx.xx.xx.xx
          ansibleUser: "root"
          ansiblePass: "dangerous"
    ```

3. Start the installation and deploy the cluster

    Use the -j parameter to specify steps 1, 2, 3, 4, 5, and 6 to complete the deployment of the k8s cluster.

    ```shell
    ./dce5-installer cluster-create -c sample/clusterConfig.yaml -j 1,2,3,4,5,6
    ```

    After successful installation, the output result is as shown in the following figure:

    ![dce5.01](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/install/images/dce503.png)

4. Install Alibaba Cloud CCM

    Refer to the [Alibaba Cloud documentation](https://help.aliyun.com/document_detail/377517.html) for deployment.

    The `nodeSelector` parameter in the `ccm.yaml` file needs to be modified to `node-role.kubernetes.io/control-plane: ""`

    After successful installation, it should appear as shown in the following figures:

    ![cc01](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/install/images/ccm01.png)

    ![cc02](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/install/images/ccm01.png)

5. Continue the installation of DCE 5.0 and install all product components

    Use the -j parameter to specify step 7 and above to complete the remaining steps.

    ```shell
    ./dce5-installer cluster-create -c sample/clusterConfig.yaml -j 7+
    ```

6. After successful installation, a public LB instance will be created by default, and DCE 5.0 can be accessed based on the assigned IP.

    ![dce5.02](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/install/images/dce501.png)

    ![dce5.03](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/install/images/dce502.png)

### Solution 3: NodePort + CCM Component Deployment

1. Log in to a machine and download the dce5-installer binary file.

    Assuming VERSION is v0.13.0:

    ```shell
    export VERSION=v0.13.0
    curl -Lo ./dce5-installer https://proxy-qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/dce5-installer-$VERSION
    chmod +x ./dce5-installer
    ```

2. Configure the cluster configuration file `clusterConfig.yaml`.

    Use the following configuration, making sure to set `loadBalancer.type = NodePort`
    and fill in the private IP addresses of the hosts:

    ```yaml title="clusterConfig.yaml"
    apiVersion: provision.daocloud.io/v1alpha3
    kind: ClusterConfig
    spec:
      loadBalancer:
        type: NodePort
      masterNodes:
        - nodeName: "g-master1"
          ip: xx.xx.xx.xx
          ansibleUser: "root"
          ansiblePass: "dangerous"
        - nodeName: "g-master2"
          ip: xx.xx.xx.xx
          ansibleUser: "root"
          ansiblePass: "dangerous"
        - nodeName: "g-master3"
          ip: xx.xx.xx.xx
          ansibleUser: "root"
          ansiblePass: "dangerous"
    ```

3. Start the installation

    ```shell
    ./dce5-installer cluster-create -c sample/clusterConfig.yaml
    ```

4. Installation successful

    ![success](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/install/images/4.1.png)

5. The installed `istio-ingressgateway` service looks as shown in the following image:

    ![svc](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/install/images/svc01.png)

6. Install CCM by following the steps mentioned in Solution 2.

7. Modify the `istio-ingressgateway` service's type to `LoadBalancer`.

    Before modification:

    ![svc2](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/install/images/svc02.png)

    After modification:

    ![svc3](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/install/images/svc03.png)

8. Modify the ghippo reverse proxy configuration.

    Refer to the documentation on [Custom Reverse Proxy Server Address](../../ghippo/install/reverse-proxy.md#_1), where the proxy address should be set to the IP address assigned to `istio-ingressgateway` when its type was changed to `LoadBalancer`. After successful modification, you can access it using this IP address.
