---
MTPE: windsonsea
date: 2024-05-11
---

# etcd components deployed in host mode and separated from the control plane

Starting from version v0.13.0, the installer supports deploying DCE 5.0 in host mode for etcd
(i.e., separating the etcd node from the master node). This allows for decoupling from the
control plane, thereby achieving an independent high-availability etcd.

## Prerequisites

- Prepare 3 Master nodes (also serving as Worker nodes)
- Prepare 3 ETCD nodes
- Prepare a bootstrap machine and complete the deployment of pre-requisite components according to the [installation dependencies](../install-tools.md)

## Offline installation

1. Download the full mode offline package on the bootstrap machine. You can download the
   latest version from the [download center](../../download/index.md).

    | CPU Architecture | Version | Download Link |
    | ---------------- | ------- | ------------- |
    | AMD64            | v0.13.0 | <https://proxy-qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-v0.13.0-amd64.tar> |
    | <font color="green">ARM64</font> | v0.13.0 | <https://proxy-qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-v0.13.0-arm64.tar> |

    After downloading, extract the offline package:

    ```bash
    # Taking the amd64 architecture offline package as an example
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
      etcdNodes: # (1)!
        - nodeName: "k8s-master"
          ip: 172.30.41.**
          ansibleUser: "root"
          ansiblePass:  ******
        - nodeName: "k8s-node1"
          ip: 172.30.41.**  
          ansibleUser: "root"
          ansiblePass:  ******
        - nodeName: "k8s-node2"
          ip: 172.30.41.**  
          ansibleUser: "root"
          ansiblePass:  ******
      masterNodes:
        - nodeName: gmaster1
          ip: 172.30.41.**  
          ansibleUser: root
          ansiblePass:  ******
        - nodeName: gmaster2
          ip: 172.30.41.**  
          ansibleUser: root
          ansiblePass:  ******
        - nodeName: gmaster3
          ip: 172.30.41.**  
          ansibleUser: root
          ansiblePass: ******
      workerNodes: []
      .....
      
      kubeanConfig: |-
        etcd_deployment_type: host # Set deployment type of etcd to host
    ```

    1. Set the etcd node

    !!! note

        - Configure `etcdNodes`.
        - Configure `etcd_deployment_type: host` in kubeanConfig.

3. Configure the manifest file (optional). You can obtain this file from the
   offline package `offline/sample` and modify it as needed.

4. Start the installation of DCE 5.0.

    ```bash
    ./offline/dce5-installer cluster-create -c ./offline/sample/clusterConfig.yaml -m ./offline/sample/manifest.yaml 
    ```

5. After the installation is complete, check whether etcd has been deployed on the
   current cluster and control plane nodes.

    - no etcd-related Pods in the current cluster.

        ![etcd01](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/install/images/etcd01.png)

    - no etcd system services on the current cluster nodes.

        ![etcd02](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/install/images/etcd02.png)

    In summary, etcd was not detected, indicating that there is no etcd
    service on the current cluster and control plane nodes. Proceed to the next step.

6. Run the command `pf -ef | grep etcd` to check if the apiserver is connected to the external etcd address.

    ![etcd03](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/install/images/etcd03.png)

7. Run the command `systemctl status etcd` on the etcd nodes to check their running status.

    ![etcd04](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/install/images/etcd04.png)
