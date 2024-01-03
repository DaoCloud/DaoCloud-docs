# 启用命名空间独享节点

命名空间独享节点指在 kubernetes 集群中，通过污点和污点容忍的方式实现特定命名空间对一个或多个节点 CPU、内存等资源的独享。为特定命名空间配置独享节点后，其它非此命名空间的应用和服务均不能运行在被独享的节点上。使用独享节点可以让重要应用独享一部分计算资源，从而和其他应用实现物理隔离。

!!! note

    在节点被设置为独享节点前已经运行在此节点上的应用和服务将不会受影响，依然会正常运行在该节点上，仅当这些 Pod 被删除或重建时，才会调度到其它非独享节点上。

## 准备工作

检查当前集群的 kube-apiserver 是否启用了 __PodNodeSelector__ 和 __PodTolerationRestriction__ 准入控制器。

使用命名空间独享节点功能需要用户启用 kube-apiserver 上的 __PodNodeSelector__ 和 __PodTolerationRestriction__ 两个特性准入控制器（Admission Controllers），关于准入控制器更多说明请参阅 [kubernetes Admission Controllers Reference](https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers/)。

您可以前往当前集群下任意一个 Master 节点上检查 __kube-apiserver.yaml__ 文件内是否启用了这两个特性，也可以在 Master 节点上执行执行如下命令进行快速检查：

    ```bash
    [root@g-master1 ~]# cat /etc/kubernetes/manifests/kube-apiserver.yaml | grep  enable-admission-plugins
    
    # 预期输出如下：
    - --enable-admission-plugins=NodeRestriction,PodNodeSelector,PodTolerationRestriction
    ```

## 在 Global 集群上启用命名空间独享节点

由于 Global 集群上运行着 kpanda、ghippo、insight 等平台基础组件，在 Global 启用命名空间独享节点将可能导致当系统组件重启后，系统组件无法调度到被独享的节点上，影响系统的整体高可用能力。因此，**通常情况下，我们不推荐用户在 Global 集群上启用命名空间独享节点特性**。

如果您确实需要在 Global 集群上启用命名空间独享节点，请参考以下步骤进行开启：

1. 为 Global 集群的 kube-apiserver 启用了 __PodNodeSelector__ 和 __PodTolerationRestriction__ 准入控制器

    !!! note

        如果集群已启用了上述的两个准入控制器，请跳过此步，直接前往配置系统组件容忍。

    前往当前集群下任意一个 Master 节点上修改 __kube-apiserver.yaml__ 配置文件，也可以在 Master 节点上执行执行如下命令进行配置：

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

    找到 __--enable-admission-plugins__ 参数，加入（以英文逗号分隔的） __PodNodeSelector__ 和 __PodTolerationRestriction__ 准入控制器。参考如下：

    ```bash
    # 加入 __ ,PodNodeSelector,PodTolerationRestriction__ 
    - --enable-admission-plugins=NodeRestriction,PodNodeSelector,PodTolerationRestriction 
    ```

2. 为平台组件所在的命名空间添加容忍注解

    完成准入控制器的开启后，您需要为平台组件所在的命名空间添加容忍注解，以保证平台组件的高可用。

    目前 DCE 5.0 的系统组件命名空间如下表：

    | 命名空间            | 所包含的系统组件                                             |
    | ------------------- | ------------------------------------------------------------ |
    | kpanda-system       | kpanda                                                       |
    | hwameiStor-system   | hwameiStor                                                   |
    | istio-system        | istio                                                        |
    | metallb-system      | metallb                                                      |
    | cert-manager-system | cert-manager                                                 |
    | contour-system      | contour                                                      |
    | kubean-system       | kubean                                                       |
    | ghippo-system       | ghippo                                                       |
    | kcoral-system       | kcoral                                                       |
    | kcollie-system      | kcollie                                                      |
    | insight-system      | insight、insight-agent:                                      |
    | ipavo-system        | ipavo                                                        |
    | kairship-system     | kairship                                                     |
    | karmada-system      | karmada                                                      |
    | amamba-system       | amamba、jenkins                                              |
    | skoala-system       | skoala                                                       |
    | mspider-system      | mspider                                                      |
    | mcamel-system       | mcamel-rabbitmq、mcamel-elasticsearch、mcamel-mysql、mcamel-redis、mcamel-kafka、mcamel-minio、mcamel-postgresql |
    | spidernet-system    | spidernet                                                    |
    | kangaroo-system     | kangaroo                                                     |
    | gmagpie-system      | gmagpie                                                      |
    | dowl-system         | dowl                                                         |

    检查当前集群中所有命名空间是否存在上述的命名空间，执行如下命令，分别为每个命名空间添加注解： `scheduler.alpha.kubernetes.io/defaultTolerations:     '[{"operator": "Exists", "effect": "NoSchedule", "key": "ExclusiveNamespace"}]'` 。

    ```bash
    kubectl annotate ns <namespace-name> scheduler.alpha.kubernetes.io/defaultTolerations: '[{"operator": "Exists", "effect": 
    "NoSchedule", "key": "ExclusiveNamespace"}]'
    ```
    请确保将 `<namespace-name>` 替换为要添加注解的平台命名空间名称。

3. 使用界面为命名空间设置独享节点

    当您确认集群 API 服务器上的 __PodNodeSelector__ 和 __PodTolerationRestriction__ 两个特性准入控制器已经开启后，请参考如下步骤使用 DCE 5.0 的 UI 管理界面为命名空间设置独享节点了。

    1. 在集群列表页面点击集群名称，然后在左侧导航栏点击 __命名空间__ 。

        ![命名空间](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/exclusive01.png)

    2. 点击命名空间名称，然后点击 __独享节点__ 页签，在下方右侧点击 __添加节点__ 。

        ![命名空间](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/exclusive02.png)

    3. 在页面左侧选择让该命名空间独享哪些节点，在右侧可以清空或删除某个已选节点，最后在底部点击 __确定__ 。

        ![命名空间](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/exclusive03.png)

    4. 可以在列表中查看此命名空间的已有的独享节点，在节点右侧可以选择 __取消独享__ 。

        > 取消独享之后，其他命名空间下的 Pod 也可以被调度到该节点上。

        ![命名空间](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/exclusive04.png)

## 在 非 Global 集群上启用命名空间独享节点

在 非 Global 集群上启用命名空间独享节点，请参考以下步骤进行开启：

1. 为当前集群的 kube-apiserver 启用了 __PodNodeSelector__ 和 __PodTolerationRestriction__ 准入控制器

    !!! note

        如果集群已启用了上述的两个准入控制器，请跳过此步，直接前往界面为命名空间设置独享节点

    前往当前集群下任意一个 Master 节点上修改 __kube-apiserver.yaml__ 配置文件，也可以在 Master 节点上执行执行如下命令进行配置：

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

    找到 __--enable-admission-plugins__ 参数，加入（以英文逗号分隔的） __PodNodeSelector__ 和 __PodTolerationRestriction__ 准入控制器。参考如下：

    ```bash
    # 加入 __ ,PodNodeSelector,PodTolerationRestriction__ 
    - --enable-admission-plugins=NodeRestriction,PodNodeSelector,PodTolerationRestriction 
    ```

2. 使用界面为命名空间设置独享节点

    当您确认集群 API 服务器上的 __PodNodeSelector__ 和 __PodTolerationRestriction__ 两个特性准入控制器已经开启后，请参考如下步骤使用 DCE 5.0 的 UI 管理界面为命名空间设置独享节点了。

    1. 在集群列表页面点击集群名称，然后在左侧导航栏点击 __命名空间__ 。

        ![命名空间](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/exclusive01.png)

    2. 点击命名空间名称，然后点击 __独享节点__ 页签，在下方右侧点击 __添加节点__ 。

        ![命名空间](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/exclusive02.png)

    3. 在页面左侧选择让该命名空间独享哪些节点，在右侧可以清空或删除某个已选节点，最后在底部点击 __确定__ 。

        ![命名空间](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/exclusive03.png)

    4. 可以在列表中查看此命名空间的已有的独享节点，在节点右侧可以选择 __取消独享__ 。

        > 取消独享之后，其他命名空间下的 Pod 也可以被调度到该节点上。

        ![命名空间](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/exclusive04.png)

3. 为需要高可用的组件所在的命名空间添加容忍注解（可选）

    执行如下命令，需要高可用的组件所在的命名空间添加注解：`scheduler.alpha.kubernetes.io/defaultTolerations: '[{"operator": "Exists", "effect": 
    "NoSchedule", "key": "ExclusiveNamespace"}]'`。

    ```bash
    kubectl annotate ns <namespace-name> scheduler.alpha.kubernetes.io/defaultTolerations: '[{"operator": "Exists", "effect": 
    "NoSchedule", "key": "ExclusiveNamespace"}]'
    ```
   
    请确保将 `<namespace-name>` 替换为要添加注解的平台命名空间名称。
