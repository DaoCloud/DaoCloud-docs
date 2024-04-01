# ArgoCD 高可用安装

### 主要组件说明

#### argocd-repo-server

argocd-repo-server 负责克隆 Git 存储库、使其保持最新。
存储库克隆到 /tmp(或环境变量中指定的路径 TMPDIR )。如果 Pod 具有太多存储库或存储库包含大量文件，则 Pod 可能会耗尽磁盘空间。
为了避免此问题请安装持久卷。

#### argocd-controller

用于获取生成的 manifest 和请求 Kubernetes API 服务器来获取实际 argocd-application-controller 的 argocd-repo-server 集群状态。  
每个控制器副本使用两个单独的队列来处理应用程序的协调(毫秒)和应用程序的同步(秒)。
生成 manifest 时通常在协调期间花费最多时间，如果清单生成花费太多时间，应用程序协调会失败并出现错误，作为一种解决方法，可以增加部署的价值 --repo-server-timeout-seconds 并考虑扩大 argocd-repo-server 部署规模。  
如果控制器管理太多集群，这将使用太多内存，您可以跨多个控制器副本对集群进行分片。要启用分片，请增加环境变量中的副本数 argocd-application-controller StatefulSet 并重复环境变量中的副本数 ARGOCD_CONTROLLER_REPLICAS。  
默认情况下，控制器每10秒更新一次集群信息。如果您的集群网络环境存在问题，导致更新时间较长，您可以尝试修改环境变量，ARGO_CD_UPDATE_CLUSTER_INFO_TIMEOUT 增加超时时间（单位为秒）。

#### argocd-server

这是无状态的，并且最不可能引起问题。为了确保升级期间不会出现停机，请考虑将副本数量增加到3或更多，并在环境变量中复制该数字 ARGOCD_API_SERVER_REPLICAS。
环境 ARGOCD_GRPC_MAX_SIZE_MB 变量允许指定服务器响应消息的最大大小（以兆字节为单位）。默认值为 200。对于管理 3000 多个应用程序的 ArgoCD 实例，您可能需要增加此值。

#### argocd-dex-server

使用 argocd-dex-server 内存数据库，两个或多个实例的数据会不一致。

### 安装

下面是一个HA安装模式的 values.yaml 文件内容
基于官方文档修改的环境变量(只是一个必要的示例,实际安装建议安装持久卷)

```yaml
argo-cd:
  crds:
    install: false #如果之前安装果argo-cd则设为false
    keep: false
  configs:
    params:
      reposerver.parallelism.limit: 4
      controller.status.processors: 20 # 按需设置 
      controller.operation.processors: 10 # 按需设置
      controller.repo.server.timeout.seconds: 60 # 如果管控的仓库比较多,建议增加数值
      timeout.reconciliation: 180s #轮询时间
  repoServer:
    replicas: 2
    autoscaling:
      enabled: true
      minReplicas: 2
      maxReplicas: 5
    env:
      - name: ARGOCD_GIT_ATTEMPTS_COUNT
        value: "3"
      - name: ARGOCD_EXEC_TIMEOUT
        value: "2m30s"
    extraArgs:
      - --repo-cache-expiration=1h
  controller:
    replicas: 2 #如果仓库较多建议增加部署规格
    env: 
      - name: WORKQUEUE_BUCKET_SIZE
        value: "500"
      - name: ARGOCD_RECONCILIATION_JITTER
        value: "60"
      - name: ARGO_CD_UPDATE_CLUSTER_INFO_TIMEOUT
        value: "60" #单位是秒
      - name: ARGOCD_CLUSTER_CACHE_LIST_PAGE_SIZE
        value: "500"
      - name: ARGOCD_CLUSTER_CACHE_LIST_PAGE_BUFFER_SIZE
        value: "5"
  server:
    autoscaling:
      enabled: true
      minReplicas: 2 #不能是1
      maxReplicas: 5
    env:
      - name: ARGOCD_API_SERVER_REPLICAS
        value: "2" # 建议和minReplicas一致,不得小于minReplicas
      - name: ARGOCD_GRPC_MAX_SIZE_MB
        value: "200"
  dex: # argo自身的内存存储组件,ha模式下会导致数据不一致,可设置replica数量为1
    enabled: true
  redis-ha:
    enabled: true
```

字段说明


| 字段                                                                         | 推荐值   | 说明                                                                                                                           |
|----------------------------------------------------------------------------|-------|------------------------------------------------------------------------------------------------------------------------------|
| argo-cd.configs.params.reposerver.parallelism.limit                        | 10    | 用于配置管理工具同时操作的清单数量,当内存不够或者系统线程数量不足会导致 git 拉去仓库失败                                                                              |
| argo-cd.configs.params.controller.status.processors                        | 20    | 用于配置 controller 处理 app 的协调队列(处理时间为毫秒级别)默认长度位20(建议每1000个 app 对应长度为50)                                                         |
| argo-cd.configs.params.controller.operation.processors                     | 10    | 用于配置 controller 处理 app 的同步队列(处理时间为秒级别)默认长度为10(建议每1000个 app 对应长度为25)                                                          |
| argo-cd.configs.params.controller.repo.server.timeout.seconds              | 60    | 用于配置 controller 处理清单生成时防止 timeout 导致队列溢出的超时时间                                                                                |
| argo-cd.configs.params.timeout.reconciliation                              | 180s  | 用于配置 controller 的 git 仓库的轮询周期                                                                                                |
| argo-cd.reposerver.env[0].name: ARGOCD_GIT_ATTEMPTS_COUNT                  | 3     | 用于配置 git 仓库请求失败的重试次数                                                                                                         |
| argo-cd.reposerver.env[1].name: ARGOCD_EXEC_TIMEOUT                        | 2m30s | 用于配置 reposerver 处理 git 仓库或 helm 仓库的执行超时时间                                                                                    |
| argo-cd.reposerver.extraArgs[0]: --repo-cache-expiration=1h                | 1h    | 用于配置 reposerver 的缓存过期时间                                                                                                      |
| argo-cd.controller.env[0].name: WORKQUEUE_BUCKET_SIZE                      | 500   | 用于配置 controller 在处理并发事件中的队列长度                                                                                                |
| argo-cd.controller.env[1].name: ARGOCD_RECONCILIATION_JITTER               | 60    | 用于配置应用同步超时时候的抖动时间防止超时时存储服务器组件出现峰值,单位 s                                                                                       |
| argo-cd.controller.env[2].name: ARGO_CD_UPDATE_CLUSTER_INFO_TIMEOUT        | 60    | 用于配置 controller 更新集群信息的间隔(当集群网络环境存在问题导致更新时间较长时可以增加这个变量,或者对集群更新情况较少的时候增加这个变量)                                                 |
| argo-cd.controller.env[3].name: ARGOCD_CLUSTER_CACHE_LIST_PAGE_SIZE        | 500   | 用于配置 controller 检索集群资源的页的大小(ARGOCD_CLUSTER_CACHE_LIST_PAGE_SIZE*ARGOCD_CLUSTER_CACHE_LIST_PAGE_BUFFER_SIZE 应该大于预估的集群内最大资源计数) |
| argo-cd.controller.env[4].name: ARGOCD_CLUSTER_CACHE_LIST_PAGE_BUFFER_SIZE | 5     | 可以适当增加 buffer 的大小防止控制器抛出内存溢出的错误(单位是M)                                                                                        |
| argo-cd.server.env[1].name: ARGOCD_GRPC_MAX_SIZE_MB                        | 200   | 单位是 Mb 允许服务器响应消息的最大的大小,如果数量较多建议设置为较大的值(3000 projects should set 200+)                                                        |

### 参考资料

https://argo-cd.readthedocs.io/en/stable/operator-manual/high_availability/