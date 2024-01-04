# 创建定时任务（CronJob）

本文介绍如何通过镜像和 YAML 文件两种方式创建定时任务（CronJob）。

定时任务（CronJob）适用于于执行周期性的操作，例如备份、报告生成等。这些任务可以配置为周期性重复的（例如：每天/每周/每月一次），可以定义任务开始执行的时间间隔。

## 前提条件

创建定时任务（CronJob）之前，需要满足以下前提条件：

- 在[容器管理](../../intro/index.md)模块中[接入 Kubernetes 集群](../clusters/integrate-cluster.md)或者[创建 Kubernetes 集群](../clusters/create-cluster.md)，且能够访问集群的 UI 界面。

- 创建一个[命名空间](../namespaces/createns.md)和[用户](../../../ghippo/user-guide/access-control/user.md)。

- 当前操作用户应具有 [NS Edit](../permissions/permission-brief.md#ns-edit) 或更高权限，详情可参考[命名空间授权](../namespaces/createns.md)。

- 单个实例中有多个容器时，请确保容器使用的端口不冲突，否则部署会失效。

## 镜像创建

参考以下步骤，使用镜像创建一个定时任务。

1. 点击左侧导航栏上的 __集群列表__ ，然后点击目标集群的名称，进入 __集群详情__ 页面。

    ![集群详情](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/deploy01.png)

2. 在集群详情页面，点击左侧导航栏的 __工作负载__ -> __定时任务__ ，然后点击页面右上角的 __镜像创建__ 按钮。

    ![工作负载](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/cronjob01.png)

3. 依次填写[基本信息](create-cronjob.md#_3)、[容器配置](create-cronjob.md#_4)、[定时任务配置](create-cronjob.md#_5)、[高级配置](create-cronjob.md#_6)后，在页面右下角点击 __确定__ 完成创建。

    系统将自动返回 __定时任务__ 列表。点击列表右侧的 __︙__ ，可以对定时任务执行执行更新、删除、重启等操作。

    ![操作菜单](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/cronjob06.png)

### 基本信息

在 __创建定时任务__ 页面中，根据下表输入信息后，点击 __下一步__ 。

![基本信息](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/cronjob02.png)

- 负载名称：最多包含 63 个字符，只能包含小写字母、数字及分隔符（“-”），且必须以小写字母或数字开头及结尾。同一命名空间内同一类型工作负载的名称不得重复，而且负载名称在工作负载创建好之后不可更改。
- 命名空间：选择将新建的定时任务部署在哪个命名空间，默认使用 default 命名空间。找不到所需的命名空间时可以根据页面提示去[创建新的命名空间](../namespaces/createns.md)。
- 描述：输入工作负载的描述信息，内容自定义。字符数量应不超过 512 个。

### 容器配置

容器配置分为基本信息、生命周期、健康检查、环境变量、数据存储、安全设置六部分，点击下方的相应页签可查看各部分的配置要求。

> 容器配置仅针对单个容器进行配置，如需在一个容器组中添加多个容器，可点击右侧的 __+__ 添加多个容器。

=== "基本信息（必填）"

    ![基本信息](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/cronjob03.png)

    在配置容器相关参数时，必须正确填写容器的名称、镜像参数，否则将无法进入下一步。参考以下要求填写配置后，点击 __确认__ 。

    - 容器名称：最多包含 63 个字符，支持小写字母、数字及分隔符（“-”）。必须以小写字母或数字开头及结尾，例如 nginx-01。
    - 容器镜像：输入镜像地址或名称。输入镜像名称时，默认从官方的 [DockerHub](https://hub.docker.com/) 拉取镜像。接入 DCE 5.0 的[镜像仓库](../../../kangaroo/intro/index.md)模块后，可以点击右侧的 __选择镜像__ 来选择镜像。
    - 更新策略：勾选 __总是拉取镜像__ 后，负载每次重启/升级时都会从仓库重新拉取镜像。如果不勾选，则只拉取本地镜像，只有当镜像在本地不存在时才从镜像仓库重新拉取。更多详情可参考[镜像拉取策略](https://kubernetes.io/zh-cn/docs/concepts/containers/images/#image-pull-policy)。
    - 特权容器：默认情况下，容器不可以访问宿主机上的任何设备，开启特权容器后，容器即可访问宿主机上的所有设备，享有宿主机上的运行进程的所有权限。
    - CPU/内存配额：CPU/内存资源的请求值（需要使用的最小资源）和限制值（允许使用的最大资源）。请根据需要为容器配置资源，避免资源浪费和因容器资源超额导致系统故障。默认值如图所示。
    - GPU 独享：为容器配置 GPU 用量，仅支持输入正整数。GPU 配额设置支持为容器设置独享整张 GPU 卡或部分 vGPU。例如，对于一张 8 核心的 GPU 卡，输入数字 __8__ 表示让容器独享整长卡，输入数字 __1__ 表示为容器配置 1 核心的 vGPU。

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

    通过 Linux 内置的账号权限隔离机制来对容器进行安全隔离。您可以通过使用不同权限的账号 UID（数字身份标记）来限制容器的权限。例如，输入 __0__ 表示使用 root 账号的权限。

    ![安全设置](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/deploy10.png)

### 定时任务配置

![定时任务配置](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/cronjob04.png)

- 并发策略：是否允许多个 Job 任务并行执行。

    - __Allow__ ：可以在前一个任务未完成时就创建新的定时任务，而且多个任务可以并行。任务太多可能抢占集群资源。
    - __Forbid__ ：在前一个任务完成之前，不能创建新任务，如果新任务的执行时间到了而之前的任务仍未执行完，CronJob 会忽略新任务的执行。
    - __Replace__ ：如果新任务的执行时间到了，但前一个任务还未完成，新的任务会取代前一个任务。

    > 上述规则仅适用于同一个 CronJob 创建的多个任务。多个 CronJob 创建的多个任务总是允许并发执行。

- 定时规则：基于分钟、小时、天、周、月设置任务执行的时间周期。支持用数字和 `*` 自定义 Cron 表达式，**输入表达式后下方会提示当前表达式的含义**。有关详细的表达式语法规则，可参考 [Cron 时间表语法](https://kubernetes.io/zh-cn/docs/concepts/workloads/controllers/cron-jobs/#cron-schedule-syntax)。
- 任务记录：设定保留多少条任务执行成功或失败的记录。 __0__ 表示不保留。
- 超时时间：超出该时间时，任务就会被标识为执行失败，任务下的所有 Pod 都会被删除。为空时表示不设置超时时间。默认值为 360 s。
- 重试次数：任务可重试次数，默认值为 6。
- 重启策略：设置任务失败时是否重启 Pod。

### 高级配置

定时任务的高级配置主要涉及标签与注解。

可以点击 __添加__ 按钮为工作负载实例 Pod 添加标签和注解。

![定时任务配置](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/cronjob05.png)

## YAML 创建

除了通过镜像方式外，还可以通过 YAML 文件更快速地创建创建定时任务。

1. 点击左侧导航栏上的 __集群列表__ ，然后点击目标集群的名称，进入 __集群详情__ 页面。

    ![集群详情](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/deploy01.png)

2. 在集群详情页面，点击左侧导航栏的 __工作负载__ -> __定时任务__ ，然后点击页面右上角的 __YAML 创建__ 按钮。

    ![工作负载](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/cronjob07.png)

3. 输入或粘贴事先准备好的 YAML 文件，点击 __确定__ 即可完成创建。

    ![工作负载](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/cronjob08.png)

??? note "点击查看创建定时任务的 YAML 示例"

    ```yaml
    apiVersion: batch/v1
    kind: CronJob
    metadata:
      creationTimestamp: '2022-12-26T09:45:47Z'
      generation: 1
      name: demo
      namespace: default
      resourceVersion: '92726617'
      uid: d030d8d7-a405-4dcd-b09a-176942ef36c9
    spec:
      concurrencyPolicy: Allow
      failedJobsHistoryLimit: 1
      jobTemplate:
        metadata:
          creationTimestamp: null
        spec:
          activeDeadlineSeconds: 360
          backoffLimit: 6
          template:
            metadata:
              creationTimestamp: null
            spec:
              containers:
                - image: nginx
                  imagePullPolicy: IfNotPresent
                  lifecycle: {}
                  name: container-3
                  resources:
                    limits:
                      cpu: 250m
                      memory: 512Mi
                    requests:
                      cpu: 250m
                      memory: 512Mi
                  securityContext:
                    privileged: false
                  terminationMessagePath: /dev/termination-log
                  terminationMessagePolicy: File
              dnsPolicy: ClusterFirst
              restartPolicy: Never
              schedulerName: default-scheduler
              securityContext: {}
              terminationGracePeriodSeconds: 30
      schedule: 0 0 13 * 5
      successfulJobsHistoryLimit: 3
      suspend: false
    status: {}
    ```
