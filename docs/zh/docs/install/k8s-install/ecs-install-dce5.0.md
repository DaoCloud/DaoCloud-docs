# 在阿里云 ECS 上安装 DCE 5.0 商业版

本文将介绍如何阿里云 ECS 上安装 DCE 5.0。

## 前提条件

- 准备好阿里云 ECS 虚拟机，本示例创建 3 台 ubuntu22.10 server 64bit 的云服务器，每台配置为 8 核 16 GB
- 请按照[准备工作](../commercial/prepare.md)完成相关准备

## 开始部署

在阿里云 ECS 部署 DCE 5.0 时主要是负载均衡的能力需要特殊处理，由于虚拟机中不会安装 CloudProvider，LoadBalancer类型的 svc 无法被识别，所以要么是手动安装相关 CloudProvider，要么使用用 NodePort 的方式，所以目前提供了以下三种方案：

- 方案 1：NodePort + 阿里云 SLB
- 方案 2：cloudLB + 部署 CCM 组件
- 方案 3：NodePort + 部署 CCM 组件

### 方案 1 ：NodePort + 阿里云 SLB

1. 登录一台机器，下载 dce5-installer 二进制文件。

    假定 VERSION 为 v0.16.0

    ```shell
    export VERSION=v0.16.0
    curl -Lo ./dce5-installer https://proxy-qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/dce5-installer-$VERSION
    chmod +x ./dce5-installer
    ```

2. 配置集群配置文件 `clusterConfig.yaml`。

    参考以下配置，注意设置 `loadBalancer.type = NodePort`，并填写主机的私网 IP 地址：

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

3. 开始安装

    ```shell
    ./dce5-installer cluster-create -c sample/clusterConfig.yaml
    ```

4. 安装成功

    ![success](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/install/images/4.1.png)

5. 查询 svc `istio-ingressgateway` 的 https 服务暴露在 NodePort 端口，本示例是 32060

    ```shell
    kubectl get svc -A | grep NodePort
    ```

    ![gateway](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/install/images/5.1.png)

6. 创建阿里 SLB ，将 SLB 的公网 TCP 流量指向 ECS 主机的 32060 端口，3 台主机均需要添加。

    ![slb01](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/install/images/6.1.png)

    ![slb02](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/install/images/6.2.png)

    ![slb03](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/install/images/6.3.png)

    ![slb04](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/install/images/6.4.png)

7. 修改 ghippo 反向代理配置，参考文档 https://docs.daocloud.io/ghippo/install/reverse-proxy/#_1，修改后直接通过 SLB 的公网 IP +Port 访问 DCE 5.0。如下图：

    ![ghippo](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/install/images/7.1.png)

    ![ghippo](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/install/images/7.2.png)

### 方案2 ：cloudLB + 部署 CCM 组件

1. 登录一台机器，下载 dce5-installer 二进制文件。

    假定 VERSION 为 v0.16.0

    ```shell
    export VERSION=v0.16.0
    curl -Lo ./dce5-installer https://proxy-qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/dce5-installer-$VERSION
    chmod +x ./dce5-installer
    ```

2. 配置集群配置文件 `clusterConfig.yaml`。

    参考以下配置，注意设置 `loadBalancer.type = cloudLB`，并填写主机的私网 IP 地址：

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

3. 开始安装，先部署集群

    通过 -j 参数指定 1,2,3,4,5,6 步骤，完成 k8s 集群的部署。

    ```shell
    ./dce5-installer cluster-create -c sample/clusterConfig.yaml -j 1,2,3,4,5,6
    ```

    成功后输出结果如下图：

    ![dce5.01](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/install/images/dce503.png)

4. 安装阿里云 CCM

    参考[阿里云文档](https://help.aliyun.com/document_detail/377517.html)进行部署。

    文件 `ccm.yaml` 中的 `nodeSelector` 参数需要改动为 `node-role.kubernetes.io/control-plane: ""`

    安装成功后如下图：

    ![cc01](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/install/images/ccm01.png)

    ![cc02](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/install/images/ccm01.png)

5. 继续安装 DCE 5.0，将所有产品组件安装

    通过 -j 参数指定 7+ 完成剩余步骤的执行。

    ```shell
    ./dce5-installer cluster-create -c sample/clusterConfig.yaml -j 7+
    ```

6. 安装成功后，会默认创建公网的 LB 实例，并且可基于分配的 IP 来访问 DCE 5.0。

    ![dce5.02](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/install/images/dce501.png)

    ![dce5.03](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/install/images/dce502.png)

### 方案 3：NodePort + 部署 CCM 组件

1. 登录一台机器，下载 dce5-installer 二进制文件。

    假定 VERSION 为 v0.16.0

    ```shell
    export VERSION=v0.16.0
    curl -Lo ./dce5-installer https://proxy-qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/dce5-installer-$VERSION
    chmod +x ./dce5-installer
    ```

2. 配置集群配置文件 `clusterConfig.yaml`。

   参考以下配置，注意设置 `loadBalancer.type = NodePort`，并填写主机的私网 IP 地址：

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

3. 开始安装

    ```shell
    ./dce5-installer cluster-create -c sample/clusterConfig.yaml
    ```

4. 安装成功

    ![success](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/install/images/4.1.png)

5. 安装后的 svc `istio-ingressgateway` 如下图所示：

    ![svc](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/install/images/svc01.png)

6. 安装 CCM，参考方案 2 中的步骤

7. 修改 svc `istio-ingressgateway` 的 type 为 `LoadBalancer`

    修改前：

    ![svc2](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/install/images/svc02.png)

    修改后：

    ![svc3](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/install/images/svc03.png)

8. 修改 ghippo 反向代理配置

    参考文档 [自定义反向代理服务器地址](../../ghippo/install/reverse-proxy.md#_1)，其中代理地址为上一步中
    `istio-ingressgateway` 的 type 为 `LoadBalancer` 时分配的 IP 地址。修改成功后即可通过该 IP 地址进行访问。

    ![ghippo](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/install/images/ghippo01.png)
