# 部署 DCE 5.0 商业版时，etcd 组件采用 host 模式部署与控制平面分离

安装器在 v0.13.0 版本之后进行部署 DCE 5.0 时，能够支持 host 模式部署 etcd（即 etcd 所在节点 和 master 节点之间分离），以便与控制平面分离解耦，实现独立的高可用 etcd。

## 前提条件

- 准备 3 台 Master 节点（兼 Worker 节点）
- 准备 3 台 ETCD 节点
- 准备一台火种机，并按照[安装依赖项](../install-tools.md)完成前置依赖组件的部署

## 离线安装

1. 在火种机上下载全模式离线包，可以在[下载中心](../../download/index.md)下载最新版本。

    | CPU 架构 | 版本   | 下载地址 |
    | -------- | ----- | ------- |
    | AMD64    | v0.13.0 | <https://proxy-qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-v0.13.0-amd64.tar> |
    | ARM64     | v0.13.0 | <https://proxy-qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-v0.13.0-arm64.tar> |

    下载完毕后解压离线包：

    ```bash
    ## 以 amd64 架构离线包为例
    tar -xvf offline-v0.13.0-amd64.tar
    ```

2. 设置[集群配置文件 clusterConfig.yaml](../commercial/cluster-config.md)，可以在离线包 `offline/sample` 下获取该文件并修改，此处示例主要描述如何使用 host 模式部署 etcd。

    参考配置为：

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
        etcd_deployment_type: host # 配置 etcd 的部署模式为 host
    ```

    1. 配置 etcd 节点信息

    !!! note

        - 配置 `etcdNodes`。
        - 在 kubeanConfig 配置 `etcd_deployment_type: host`。

3. 配置 manifest 文件（可选），可以在离线包 `offline/sample` 下获取该文件并按需修改。

4. 开始安装 DCE 5.0。

    ```bash
    ./offline/dce5-installer cluster-create -c ./offline/sample/clusterConfig.yaml -m ./offline/sample/manifest.yaml 
    ```

5. 安装完成后，查看验证当前集群及控制面节点是否部署了 etcd？

    - 当前集群没有 etcd 相关的 Pod

        ![etcd01](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/install/images/etcd01.png)

    - 当前集群控制面节点没有 etcd 系统服务

        ![etcd02](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/install/images/etcd02.png)

   综上 etcd 均未被检测到，说明当前集群及控制面节点无 etcd 服务，执行下一步。

6. 执行命令 `pf -ef | grep etcd` ，查看 apiserver 连接的是外部 etcd 地址，如下图，连接正常。

    ![etcd03](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/install/images/etcd03.png)

7. 在 etcd 节点上执行命令 `systemctl status etcd` 来判断运行情况，如下图，etcd 运行正常。

    ![etcd04](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/install/images/etcd04.png)
