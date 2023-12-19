# 访问集群

使用 DCE 5.0 [容器管理](../../intro/index.md)平台接入或创建的集群，不仅可以通过 UI 界面直接访问，也可以通过其他两种方式进行访问控制：

- 通过 CloudShell 在线访问
- 下载集群证书后通过 kubectl 进行访问

!!! note
  
    访问集群时，用户应具有 [Cluster Admin](../permissions/permission-brief.md) 权限或更高权限。

## 通过 CloudShell 访问

1. 在 __集群列表__ 页选择需要通过 CloudShell 访问的集群，点击右侧的 __⋮__ 操作图标并在下拉列表中点击 __控制台__ 。

    ![调用 CloudShell 控制台](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/access-cloudshell.png)

2. 在 CloudShell 控制台执行 __kubectl get node__ 命令，验证 CloudShell 与集群的连通性。如图，控制台将返回集群下的节点信息。

    ![验证连通性](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/access-get-node.png)

现在，您可以通过 CloudShell 来访问并管理该集群了。

## 通过 kubectl 访问

通过本地节点访问并管理云端集群时，需要满足以下条件：

- 本地节点和云端集群的网络互联互通。
- 已经将集群证书下载到了本地节点。
- 本地节点已经安装了 kubectl 工具。关于详细的安装方式，请参阅安装 [kubectl](https://kubernetes.io/zh-cn/docs/tasks/tools/)。

满足上述条件后，按照下方步骤从本地访问云端集群：

1. 在 __集群列表__ 页选择需要下载证书的集群，点击右侧的 __⋮__ ，并在弹出菜单中点击 __证书获取__ 。

    ![进入下载证书页面](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/access-get-cert.png)

2. 选择证书有效期并点击 __下载证书__ 。

    ![下载证书](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/access-download-cert.png)

3. 打开下载好的集群证书，将证书内容复制至本地节点的 __config__ 文件。

    kubectl 工具默认会从本地节点的 __$HOME/.kube__ 目录下查找名为 __config__ 的文件。该文件存储了相关集群的访问凭证，kubectl 可以凭该配置文件连接至集群。

4. 在本地节点上执行如下命令验证集群的连通性：

    ```sh
    kubectl get pod -n default
    ```

    预期的输出类似于:

    ```none
    NAME                            READY   STATUS      RESTARTS    AGE
    dao-2048-2048-58c7f7fc5-mq7h4   1/1     Running     0           30h
    ```

现在您可以在本地通过 kubectl 访问并管理该集群了。
