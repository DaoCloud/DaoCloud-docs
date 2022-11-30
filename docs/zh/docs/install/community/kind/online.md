# 使用 Kind 集群在线安装 DCE 5.0 社区版

本页说明如何使用 Kind 集群安装 DCE 5.0 社区版的在线安装步骤。

!!! note

    点击[在线安装社区版](../../../videos/install.md#3)可观看视频演示。

## 准备工作

- 准备一台机器，机器资源建议：CPU > 10 核、内存 > 12 GB、磁盘空间 > 100 GB。
- 确保节点上已经安装 Docker、Kubectl。

## 步骤一：安装 Kind 集群

1. 在 机器上下载 Kind 的二进制文件包。

    ```shell
    curl -Lo ./kind https://qiniu-download-public.daocloud.io/Kind/v0.17.0/kind-linux-amd64
    ```

    为 `kind` 添加可执行权限：

    ```bash
    chmod +x ./kind
    ```

2. 在环境变量中加入 Kind。

    ```bash
    mv ./kind /usr/bin/kind
    ```

3. 查看 Kind 版本。

    ```shell
    kind version
    # 预期输出如下：
    kind v0.17.0 go1.19.2 linux/amd64
    ```

4. 设置 kind_cluster.yaml 的配置文件。

    注意，暴露集群内的 32000 端口到 kind 对外的 8888 端口（可自行修改），配置文件如下：

    ```shell
    apiVersion: kind.x-k8s.io/v1alpha4
    kind: Cluster
    nodes:
    - role: control-plane
      extraPortMappings:
      - containerPort: 32088
        hostPort: 8888
    ```

5. 创建一个名为 fire-kind-cluster 的 v1.21.1 集群。

    ```shell
    kind create cluster --image release.daocloud.io/kpanda/kindest-node:v1.21.1 --name=fire-kind-cluster --config=kind_cluster.yaml 
    # 预期输出如下
    Creating cluster "fire-kind-cluster" ...
     ✓ Ensuring node image (release.daocloud.io/kpanda/kindest-node:v1.21.1) 🖼 
     ✓ Preparing nodes 📦  
     ✓ Writing configuration 📜 
     ✓ Starting control-plane 🕹️ 
     ✓ Installing CNI 🔌 
     ✓ Installing StorageClass 💾 
    Set kubectl context to "kind-fire-kind-cluster"
    ```

6. 查看新创建的集群。

    ```
    kind get clusters
    # 预期输出如下：
    fire-kind-cluster
    ```

## 步骤二：在线安装 DCE 5.0 社区版

1. [安装依赖项](../../install-tools.md)。

    !!! note

      如果集群中已安装所有依赖项，请确保依赖项版本符合要求：

      - helm ≥ 3.9.4
      - skopeo ≥ 1.9.2
      - kubectl ≥ 1.22.0
      - yq ≥ 4.27.5

2. 获取 Kind 所在主机的 IP，假定为 `10.6.3.1`，进行安装。

    ```shell
    ./dce5-installer install-app -z -k 10.6.3.1:8888
    ```

    !!! note

        Kind 集群仅支持 NodePort 模式。

3. 安装完成后，命令行会提示安装成功。恭喜您！:smile: 现在可以通过屏幕提示的 URL 使用 **默认的账户和密码（admin/changeme）** 探索全新的 DCE 5.0 啦！

    ![安装成功](../../images/success.png)

    !!! success

        请记录好提示的 URL，方便下次访问。


    另外，安装 DCE 5.0 成功之后，您需要正版授权后使用，请参考[申请社区免费体验](https://file+.vscode-resource.vscode-cdn.net/Users/jiazenghui/DaoCloud-docs/docs/zh/docs/dce/license0.md)。

!!! note

    如果安装过程中遇到什么问题，欢迎扫描二维码，与开发者畅快交流：

    ![社区版交流群](../../images/wechat.png)
