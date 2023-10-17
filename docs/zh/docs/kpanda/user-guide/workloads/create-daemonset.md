# 创建守护进程(DaemonSet)

本文介绍如何通过镜像和 YAML 文件两种方式创建守护进程（DaemonSet）。

守护进程（DaemonSet）通过[节点亲和性](https://kubernetes.io/zh-cn/docs/tasks/configure-pod-container/assign-pods-nodes-using-node-affinity/)与[污点](https://kubernetes.io/zh-cn/docs/concepts/scheduling-eviction/taint-and-toleration/)功能确保在全部或部分节点上运行一个 Pod 的副本。对于新加入集群的节点，DaemonSet 自动在新节点上部署相应的 Pod，并跟踪 Pod 的运行状态。当节点被移除时，DaemonSet 则删除其创建的所有 Pod。

守护进程的常见用例包括：

- 在每个节点上运行集群守护进程。

- 在每个节点上运行日志收集守护进程。

- 在每个节点上运行监控守护进程。

简单起见，可以在每个节点上为每种类型的守护进程都启动一个 DaemonSet。如需更精细、更高级地管理守护进程，也可以为同一种守护进程部署多个 DaemonSet。每个 DaemonSet 具有不同的标志，并且对不同硬件类型具有不同的内存、CPU 要求。

## 前提条件

创建 DaemonSet 之前，需要满足以下前提条件：

- 在[容器管理](../../intro/index.md)模块中[接入 Kubernetes 集群](../clusters/integrate-cluster.md)或者[创建 Kubernetes 集群](../clusters/create-cluster.md)，且能够访问集群的 UI 界面。

- 创建一个[命名空间](../namespaces/createns.md)和[用户](../../../ghippo/user-guide/access-control/user.md)。

- 当前操作用户应具有 [`NS Edit`](../permissions/permission-brief.md#ns-edit) 或更高权限，详情可参考[命名空间授权](../namespaces/createns.md)。

- 单个实例中有多个容器时，请确保容器使用的端口不冲突，否则部署会失效。

## 镜像创建

参考以下步骤，使用镜像创建一个守护进程。

1. 点击左侧导航栏上的`集群列表`，然后点击目标集群的名称，进入`集群详情`页面。

    ![集群详情](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/deploy01.png)

2. 在集群详情页面，点击左侧导航栏的`工作负载` -> `守护进程`，然后点击页面右上角的`镜像创建`按钮。

    ![工作负载](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/daemon01.png)

3. 依次填写[基本信息](create-daemonset.md#_3)、[容器配置](create-daemonset.md#_4)、[服务配置](create-daemonset.md#_5)、[高级配置](create-daemonset.md#_6)后，在页面右下角点击`确定`完成创建。

    系统将自动返回`守护进程`列表。点击列表右侧的 `︙`，可以对守护进程执行执行更新、删除、重启等操作。

    ![操作菜单](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/daemon05.png)

### 基本信息

在`创建守护进程`页面中，根据下表输入信息后，点击`下一步`。

![基本信息](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/daemon02.png)

- 负载名称：最多包含 63 个字符，只能包含小写字母、数字及分隔符（“-”），且必须以小写字母或数字开头及结尾。同一命名空间内同一类型工作负载的名称不得重复，而且负载名称在工作负载创建好之后不可更改。
- 命名空间：选择将新建的守护进程部署在哪个命名空间，默认使用 default 命名空间。找不到所需的命名空间时可以根据页面提示去[创建新的命名空间](../namespaces/createns.md)。
- 描述：输入工作负载的描述信息，内容自定义。字符数量应不超过 512 个。

### 容器配置

容器配置分为基本信息、生命周期、健康检查、环境变量、数据存储、安全设置六部分，点击下方的相应页签可查看各部分的配置要求。

> 容器配置仅针对单个容器进行配置，如需在一个容器组中添加多个容器，可点击右侧的 `+` 添加多个容器。

=== "基本信息（必填）"

    ![基本信息](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/daemon06.png)

    在配置容器相关参数时，必须正确填写容器的名称、镜像参数，否则将无法进入下一步。参考以下要求填写配置后，点击`确认`。

    - 容器名称：最多包含 63 个字符，支持小写字母、数字及分隔符（“-”）。必须以小写字母或数字开头及结尾，例如 nginx-01。
    - 容器镜像：输入镜像地址或名称。输入镜像名称时，默认从官方的 [DockerHub](https://hub.docker.com/) 拉取镜像。接入 DCE 5.0 的[镜像仓库](../../../kangaroo/intro/index.md)模块后，可以点击右侧的`选择镜像`来选择镜像。
    - 更新策略：勾选`总是拉取镜像`后，负载每次重启/升级时都会从仓库重新拉取镜像。如果不勾选，则只拉取本地镜像，只有当镜像在本地不存在时才从镜像仓库重新拉取。更多详情可参考[镜像拉取策略](https://kubernetes.io/zh-cn/docs/concepts/containers/images/#image-pull-policy)。
    - 特权容器：默认情况下，容器不可以访问宿主机上的任何设备，开启特权容器后，容器即可访问宿主机上的所有设备，享有宿主机上的运行进程的所有权限。
    - CPU/内存配额：CPU/内存资源的请求值（需要使用的最小资源）和限制值（允许使用的最大资源）。请根据需要为容器配置资源，避免资源浪费和因容器资源超额导致系统故障。默认值如图所示。
    - GPU 独享：为容器配置 GPU 用量，仅支持输入正整数。GPU 配额设置支持为容器设置独享整张 GPU 卡或部分 vGPU。例如，对于一张 8 核心的 GPU 卡，输入数字 `8` 表示让容器独享整长卡，输入数字 `1` 表示为容器配置 1 核心的 vGPU。

        > 设置 GPU 独享之前，需要管理员预先在集群节点上安装 GPU 卡及驱动插件，并在[集群设置](../clusterops/cluster-settings.md)中开启 GPU 特性。

=== "生命周期（选填）"

    设置容器启动时、启动后、停止前需要执行的命令。详情可参考[容器生命周期配置](pod-config/lifecycle.md)。

    ![生命周期](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/deploy06.png)

=== "健康检查（选填）"

    用于判断容器和应用的健康状态，有助于提高应用的可用性。详情可参考[容器健康检查配置](pod-config/health-check.md)。

    ![健康检查](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/deploy07.png)

=== "环境变量（选填）"

    配置 Pod 内的容器参数，为 Pod 添加环境变量或传递配置等。详情可参考[容器环境变量配置](pod-config/env-variables.md)。

    ![环境变量](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/deploy08.png)

=== "数据存储（选填）"

    配置容器挂载数据卷和数据持久化的设置。详情可参考[容器数据存储配置](pod-config/env-variables.md)。

    ![数据存储](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/deploy09.png)

=== "安全设置（选填）"

    通过 Linux 内置的账号权限隔离机制来对容器进行安全隔离。您可以通过使用不同权限的账号 UID（数字身份标记）来限制容器的权限。例如，输入 `0` 表示使用 root 账号的权限。

    ![安全设置](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/deploy10.png)

### 服务配置

为守护进程创建[服务（Service）](../network/create-services.md)，使守护进程能够被外部访问。

1. 点击`创建服务`按钮。

    ![服务配置](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/daemon03.png)

2. 配置服务参数，详情请参考[创建服务](../network/create-services.md)。

    ![创建服务](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/deploy13.png)

3. 点击`确定`，点击`下一步`。

### 高级配置

高级配置包括负载的网络配置、升级策略、调度策略、标签与注解四部分，可点击下方的页签查看各部分的配置要求。

=== "网络配置"

    应用在某些场景下会出现冗余的 DNS 查询。Kubernetes 为应用提供了与 DNS 相关的配置选项，能够在某些场景下有效地减少冗余的 DNS 查询，提升业务并发量。

    ![DNS 配置](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/deploy17.png)

    - DNS 策略

        - Default：使容器使用 kubelet 的 `--resolv-conf` 参数指向的域名解析文件。该配置只能解析注册到互联网上的外部域名，无法解析集群内部域名，且不存在无效的 DNS 查询。
        - ClusterFirstWithHostNet：应用对接主机的域名文件。
        - ClusterFirst：应用对接 Kube-DNS/CoreDNS。
        - None：Kubernetes v1.9（Beta in v1.10）中引入的新选项值。设置为 None 之后，必须设置 dnsConfig，此时容器的域名解析文件将完全通过 dnsConfig 的配置来生成。

    - 域名服务器：填写域名服务器的地址，例如 `10.6.175.20`。
    - 搜索域：域名查询时的 DNS 搜索域列表。指定后，提供的搜索域列表将合并到基于 dnsPolicy 生成的域名解析文件的 search 字段中，并删除重复的域名。Kubernetes 最多允许 6 个搜索域。
    - Options：DNS 的配置选项，其中每个对象可以具有 name 属性（必需）和 value 属性（可选）。该字段中的内容将合并到基于 dnsPolicy 生成的域名解析文件的 options 字段中，dnsConfig 的 options 的某些选项如果与基于 dnsPolicy 生成的域名解析文件的选项冲突，则会被 dnsConfig 所覆盖。
    - 主机别名：为主机设置的别名。

=== "升级策略"

    ![升级策略](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/deploy14.png)

    - 升级方式：`滚动升级`指逐步用新版本的实例替换旧版本的实例，升级的过程中，业务流量会同时负载均衡分布到新老的实例上，因此业务不会中断。`重建升级`指先删除老版本的负载实例，再安装指定的新版本，升级过程中业务会中断。
    - 最大无效 Pod 数：指定负载更新过程中不可用 Pod 的最大值或比率，默认 25%。如果等于实例数有服务中断的风险。
    - 最大浪涌：更新 Pod 的过程中 Pod 总数超过 Pod 期望副本数部分的最大值或比率。默认 25%。
    - 最大保留版本数：设置版本回滚时保留的旧版本数量。默认 10。
    - Pod 可用最短时间：Pod 就绪的最短时间，只有超出这个时间 Pod 才被认为可用，默认 0 秒。
    - 升级最大持续时间：如果超过所设置的时间仍未部署成功，则将该负载标记为失败。默认 600 秒。
    - 缩容时间窗：负载停止前命令的执行时间窗（0-9,999秒），默认 30 秒。

=== "调度策略"

    ![调度策略](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/deploy15.png)

    - 容忍时间：负载实例所在的节点不可用时，将负载实例重新调度到其它可用节点的时间，默认为 300 秒。
    - 节点亲和性：根据节点上的标签来约束 Pod 可以调度到哪些节点上。
    - 工作负载亲和性：基于已经在节点上运行的 Pod 的标签来约束 Pod 可以调度到哪些节点。
    - 工作负载反亲和性：基于已经在节点上运行的 Pod 的标签来约束 Pod 不可以调度到哪些节点。
    - 拓扑域：即 topologyKey，用于指定可以调度的一组节点。例如，`kubernetes.io/os` 表示只要某个操作系统的节点满足 labelSelector 的条件就可以调度到该节点。

    > 具体详情请参考[调度策略](pod-config/scheduling-policy.md)。

=== "标签与注解"

    可以点击`添加`按钮为工作负载和容器组添加标签和注解。

    ![标签与注解](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/deploy16.png)

## YAML 创建

除了通过镜像方式外，还可以通过 YAML 文件更快速地创建创建守护进程。

1. 点击左侧导航栏上的`集群列表`，然后点击目标集群的名称，进入`集群详情`页面。

    ![集群详情](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/deploy01.png)

2. 在集群详情页面，点击左侧导航栏的`工作负载` -> `守护进程`，然后点击页面右上角的 `YAML 创建`按钮。

    ![工作负载](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/daemon07.png)

3. 输入或粘贴事先准备好的 YAML 文件，点击`确定`即可完成创建。

    ![工作负载](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/daemon08.png)

??? note "点击查看创建守护进程的 YAML 示例"

    ```yaml
    kind: DaemonSet
    apiVersion: apps/v1
    metadata:
      name: hwameistor-local-disk-manager
      namespace: hwameistor
      uid: ccbdc098-7de3-4a8a-96dd-d1cee159c92b
      resourceVersion: '90999552'
      generation: 1
      creationTimestamp: '2022-12-15T09:03:44Z'
      labels:
        app.kubernetes.io/managed-by: Helm
      annotations:
        deprecated.daemonset.template.generation: '1'
        meta.helm.sh/release-name: hwameistor
        meta.helm.sh/release-namespace: hwameistor
    spec:
      selector:
        matchLabels:
          app: hwameistor-local-disk-manager
      template:
        metadata:
          creationTimestamp: null
          labels:
            app: hwameistor-local-disk-manager
        spec:
          volumes:
            - name: udev
              hostPath:
                path: /run/udev
                type: Directory
            - name: procmount
              hostPath:
                path: /proc
                type: Directory
            - name: devmount
              hostPath:
                path: /dev
                type: Directory
            - name: socket-dir
              hostPath:
                path: /var/lib/kubelet/plugins/disk.hwameistor.io
                type: DirectoryOrCreate
            - name: registration-dir
              hostPath:
                path: /var/lib/kubelet/plugins_registry/
                type: Directory
            - name: plugin-dir
              hostPath:
                path: /var/lib/kubelet/plugins
                type: DirectoryOrCreate
            - name: pods-mount-dir
              hostPath:
                path: /var/lib/kubelet/pods
                type: DirectoryOrCreate
          containers:
            - name: registrar
              image: k8s-gcr.m.daocloud.io/sig-storage/csi-node-driver-registrar:v2.5.0
              args:
                - '--v=5'
                - '--csi-address=/csi/csi.sock'
                - >-
                  --kubelet-registration-path=/var/lib/kubelet/plugins/disk.hwameistor.io/csi.sock
              env:
                - name: KUBE_NODE_NAME
                  valueFrom:
                    fieldRef:
                      apiVersion: v1
                      fieldPath: spec.nodeName
              resources: {}
              volumeMounts:
                - name: socket-dir
                  mountPath: /csi
                - name: registration-dir
                  mountPath: /registration
              lifecycle:
                preStop:
                  exec:
                    command:
                      - /bin/sh
                      - '-c'
                      - >-
                        rm -rf /registration/disk.hwameistor.io 
                        /registration/disk.hwameistor.io-reg.sock
              terminationMessagePath: /dev/termination-log
              terminationMessagePolicy: File
              imagePullPolicy: IfNotPresent
            - name: manager
              image: ghcr.m.daocloud.io/hwameistor/local-disk-manager:v0.6.1
              command:
                - /local-disk-manager
              args:
                - '--endpoint=$(CSI_ENDPOINT)'
                - '--nodeid=$(NODENAME)'
                - '--csi-enable=true'
              env:
                - name: CSI_ENDPOINT
                  value: unix://var/lib/kubelet/plugins/disk.hwameistor.io/csi.sock
                - name: NAMESPACE
                  valueFrom:
                    fieldRef:
                      apiVersion: v1
                      fieldPath: metadata.namespace
                - name: WATCH_NAMESPACE
                  valueFrom:
                    fieldRef:
                      apiVersion: v1
                      fieldPath: metadata.namespace
                - name: POD_NAME
                  valueFrom:
                    fieldRef:
                      apiVersion: v1
                      fieldPath: metadata.name
                - name: NODENAME
                  valueFrom:
                    fieldRef:
                      apiVersion: v1
                      fieldPath: spec.nodeName
                - name: OPERATOR_NAME
                  value: local-disk-manager
              resources: {}
              volumeMounts:
                - name: udev
                  mountPath: /run/udev
                - name: procmount
                  readOnly: true
                  mountPath: /host/proc
                - name: devmount
                  mountPath: /dev
                - name: registration-dir
                  mountPath: /var/lib/kubelet/plugins_registry
                - name: plugin-dir
                  mountPath: /var/lib/kubelet/plugins
                  mountPropagation: Bidirectional
                - name: pods-mount-dir
                  mountPath: /var/lib/kubelet/pods
                  mountPropagation: Bidirectional
              terminationMessagePath: /dev/termination-log
              terminationMessagePolicy: File
              imagePullPolicy: IfNotPresent
              securityContext:
                privileged: true
          restartPolicy: Always
          terminationGracePeriodSeconds: 30
          dnsPolicy: ClusterFirst
          serviceAccountName: hwameistor-admin
          serviceAccount: hwameistor-admin
          hostNetwork: true
          hostPID: true
          securityContext: {}
          schedulerName: default-scheduler
          tolerations:
            - key: CriticalAddonsOnly
              operator: Exists
            - key: node.kubernetes.io/not-ready
              operator: Exists
              effect: NoSchedule
            - key: node-role.kubernetes.io/master
              operator: Exists
              effect: NoSchedule
            - key: node-role.kubernetes.io/control-plane
              operator: Exists
              effect: NoSchedule
            - key: node.cloudprovider.kubernetes.io/uninitialized
              operator: Exists
              effect: NoSchedule
      updateStrategy:
        type: RollingUpdate
        rollingUpdate:
          maxUnavailable: 1
          maxSurge: 0
      revisionHistoryLimit: 10
    status:
      currentNumberScheduled: 4
      numberMisscheduled: 0
      desiredNumberScheduled: 4
      numberReady: 4
      observedGeneration: 1
      updatedNumberScheduled: 4
      numberAvailable: 4
    ```
