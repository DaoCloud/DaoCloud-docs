# etcd components deployed in host mode and separated from the control plane

When deploying DCE 5.0 using the installer version 0.13.0 or later, it supports the
host mode deployment of etcd, which allows for decoupling from the control plane and
achieving an independent high-availability etcd.

## Prerequisites

- Prepare 3 Master nodes (also serving as Worker nodes)
- Prepare 3 ETCD nodes
- Prepare a seed machine and complete the deployment of pre-requisite components according to the [installation dependencies](../install-tools.md)

## Offline installation

1. Download the full mode offline package on the seed machine. You can download the
   latest version from the [download center](../../download/index.md).

    | CPU Architecture | Version | Download Link |
    | ---------------- | ------- | ------------- |
    | AMD64            | v0.13.0 | <https://proxy-qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-v0.13.0-amd64.tar>       |
    | ARM64            | v0.13.0 | <https://proxy-qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-v0.13.0-arm64.tar>       |

    After downloading, extract the offline package:

    ```bash
    ## Taking the amd64 architecture offline package as an example
    tar -xvf offline-v0.13.0-amd64.tar
    ```

2. Set up the [cluster configuration file clusterConfig.yaml](../commercial/cluster-config.md).
   You can obtain this file from the offline package `offline/sample` and modify it. The following
   example mainly describes how to deploy etcd using host mode.

    The reference configuration is as follows:

    ```yaml
    apiVersion: provision.daocloud.io/v1alpha3
    kind: ClusterConfig
    metadata:
    spec:
      clusterName: my-cluster
      # Configure etcd node information
      etcdNodes:
        - nodeName: "k8s-master"
          ip: 10.6.112.50      
          ansibleUser: "root"
          ansiblePass: "dangerous"
        - nodeName: "k8s-node1"
          ip: 10.6.112.51
          ansibleUser: "root"
          ansiblePass: "dangerous"
        - nodeName: "k8s-node2"
          ip: 10.6.112.52
          ansibleUser: "root"
          ansiblePass: "dangerous"
      masterNodes:
        - nodeName: poc-master1
          ip: 10.5.14.31
          ansibleUser: root
          ansiblePass: dangerous@2022
        - nodeName: poc-master2
          ip: 10.5.14.32
          ansibleUser: root
          ansiblePass: dangerous@2022
        - nodeName: poc-master3
          ip: 10.5.14.33
          ansibleUser: root
          ansiblePass: dangerous@2022
      workerNodes: []
      .....
      
      # Configure the deployment mode of etcd as host
      kubeanConfig: |-
        etcd_deployment_type: host
    ```

    !!! note

        - Configure `etcdNodes`.
        - Configure `etcd_deployment_type: host` in kubeanConfig.

3. Configure the manifest file (optional). You can obtain this file from the
   offline package `offline/sample` and modify it as needed.

4. Start the installation of DCE 5.0.

    ```bash
    ./offline/dce5-installer cluster-create -c ./offline/sample/clusterConfig.yaml -m ./offline/sample/manifest.yaml 
    ```

5. After the installation is complete, check if the cluster has deployed etcd.

    - There are no etcd-related Pods in the current cluster.

        ![etcd01](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/install/images/etcd01.png)

    - There are no etcd system services on the current cluster nodes.

        ![etcd02](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/install/images/etcd02.png)

6. Run the command `pf -ef | grep etcd` to check if the apiserver is connected to the external etcd address.

    ![etcd03](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/install/images/etcd03.png)

7. Run the command `systemctl status etcd` on the etcd nodes to check their running status.

    ![etcd04](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/install/images/etcd04.png)
