# 命名空间独享节点

命名空间独享节点指在 kubernetes 集群中，通过污点和污点容忍的方式实现特定命名空间对一个或多个节点 CPU、内存等资源的独享。为特定命名空间配置独享节点后，其它非此命名空间的应用和服务均不能运行在被独享的节点上。使用独享节点可以让重要应用独享一部分计算资源，从而和其他应用实现物理隔离。

!!! note

    在节点被设置为独享节点前已经运行在此节点上的应用和服务将不会受影响，依然会正常运行在该节点上，仅当这些 Pod 被删除或重建时，才会调度到其它非独享节点上。

## 前提条件：

使用命名空间独享节点功能需要用户启用集群 API 服务器上的 `PodNodeSelector` 和 `PodTolerationRestriction` 两个特性准入控制器（Admission Controllers），关于准入控制器更多说明请参阅 [kubernetes Admission Controllers Reference](https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers/)。

1. 检查当前集群的 API 服务器是否启用了 `PodNodeSelector` 和 `PodTolerationRestriction` 准入控制器。您可以前往当前集群下任意一个 Master 节点上检查 `kube-apiserver.yaml` 文件内是否启用了这两个特性，也可以在 Master 节点上执行执行如下命令进行快速检查：

    ```bash
    [root@g-master1 ~]# cat /etc/kubernetes/manifests/kube-apiserver.yaml | grep  enable-admission-plugins

    # 预期输出如下：
    - --enable-admission-plugins=NodeRestriction,PodNodeSelector,PodTolerationRestriction
    ```

2. 为未启用 `PodNodeSelector` 和 `PodTolerationRestriction` 准入控制器的集群开启 `PodNodeSelector` 和 `PodTolerationRestriction` 特性。

!!! note

    如果上一步输出的结果包含 `PodNodeSelector` 和 `PodTolerationRestriction` 两个参数，请跳过这一步，直接前往使用界面为命名空间设置独享节点。

前往当前集群下任意一个 Master 节点上修改 `kube-apiserver.yaml` 配置文件，也可以在 Master 节点上执行执行如下命令进行配置：

    ```bash
    [root@g-master1 ~]# vi /etc/kubernetes/manifests/kube-apiserver.yaml

    # 预期输出如下：
    apiVersion: v1
    kind: Pod
    metadata:
        ......
    spec:
    containers:
    - command:
        - kube-apiserver
        ......
        - --default-not-ready-toleration-seconds=300
        - --default-unreachable-toleration-seconds=300
        - --enable-admission-plugins=NodeRestriction   #启用的准入控制器列表
        - --enable-aggregator-routing=False
        - --enable-bootstrap-token-auth=true
        - --endpoint-reconciler-type=lease
        - --etcd-cafile=/etc/kubernetes/ssl/etcd/ca.crt
        ......
    ```

找到 `--enable-admission-plugins` 参数，加入（以英文逗号分隔的）`PodNodeSelector` 和 `PodTolerationRestriction` 准入控制器。参考如下：

    ```bash
    # 加入`,PodNodeSelector,PodTolerationRestriction`
    - --enable-admission-plugins=NodeRestriction,PodNodeSelector,PodTolerationRestriction 
    ```

## 使用界面为命名空间设置独享节点

当您确认集群 API 服务器上的 `PodNodeSelector` 和 `PodTolerationRestriction` 两个特性准入控制器已经开启后，请参考如下步骤使用 DCE 5.0 的 UI 管理界面为命名空间设置独享节点了。

1. 在集群列表页面点击集群名称，然后在左侧导航栏点击`命名空间`。

    ![命名空间](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/exclusive01.png)

2. 点击命名空间名称，然后点击`独享节点` 页签，在下方右侧点击`添加节点`。

    ![命名空间](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/exclusive02.png)

3. 在页面左侧选择让该命名空间独享哪些节点，在右侧可以清空或删除某个已选节点，最后在底部点击`确定`。

    ![命名空间](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/exclusive03.png)

4. 可以在列表中查看此命名空间的已有的独享节点，在节点右侧可以选择`取消独享`。

    > 取消独享之后，其他命名空间下的 Pod 也可以被调度到该节点上。

    ![命名空间](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/exclusive04.png)