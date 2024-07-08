# 离线升级容器管理模块

本页说明[下载容器管理模块](../../download/modules/kpanda.md)后，应该如何安装或升级。

!!! info

    下述命令或脚本内出现的 `kpanda` 字样是容器管理模块的内部开发代号。

## 从安装包中加载镜像

### 从下载的安装包中加载镜像

您可以根据下面两种方式之一加载镜像，当环境中存在镜像仓库时，建议选择 chart-syncer 同步镜像到镜像仓库，该方法更加高效便捷。

#### 方式一：使用 chart-syncer 同步镜像

使用 chart-syncer 可以将您下载的安装包中的 chart 及其依赖的镜像包上传至安装器部署 DCE 时使用的镜像仓库和 helm 仓库。

首先找到一台能够连接镜像仓库和 helm 仓库的节点（如火种节点），在节点上创建 load-image.yaml 配置文件，填入镜像仓库和 helm 仓库等配置信息。

1. 创建 load-image.yaml

    !!! note  

        该 YAML 文件中的各项参数均为必填项。

    === "已添加 Helm repo"

        若当前环境已安装 chart repo，chart-syncer 也支持将 chart 导出为 tgz 文件。

        ```yaml title="load-image.yaml"
        source:
          intermediateBundlesPath: kpanda # (1)!
        target:
          containerRegistry: 10.16.10.111 # (2)!
          containerRepository: release.daocloud.io/kpanda # (3)!
          repo:
            kind: HARBOR # (4)!
            url: http://10.16.10.111/chartrepo/release.daocloud.io # (5)!
            auth:
              username: "admin" # (6)!
              password: "Harbor12345" # (7)!
          containers:
            auth:
              username: "admin" # (8)!
              password: "Harbor12345" # (9)!
        ```

        1. 使用 chart-syncer 之后 .tar.gz 包所在的路径
        2. 镜像仓库地址
        3. 镜像仓库路径
        4. Helm Chart 仓库类别
        5. Helm 仓库地址
        6. 镜像仓库用户名
        7. 镜像仓库密码
        8. Helm 仓库用户名
        9. Helm 仓库密码

    === "未添加 Helm repo"

        若当前节点上未添加 helm repo，chart-syncer 也支持将 chart 导出为 tgz 文件，并存放在指定路径。

        ```yaml title="load-image.yaml"
        source:
          intermediateBundlesPath: kpanda # (1)!
        target:
          containerRegistry: 10.16.10.111 # (2)!
          containerRepository: release.daocloud.io/kpanda # (3)!
          repo:
            kind: LOCAL
            path: ./local-repo # (4)!
          containers:
            auth:
              username: "admin" # (5)!
              password: "Harbor12345" # (6)!
        ```

        1. 使用 chart-syncer 之后 .tar.gz 包所在的路径
        2. 镜像仓库 url
        3. 镜像仓库路径
        4. chart 本地路径
        5. 镜像仓库用户名
        6. 镜像仓库密码

1. 执行同步镜像命令。

    ```shell
    charts-syncer sync --config load-image.yaml
    ```

#### 方式二：使用 Docker 或 containerd 加载镜像

解压并加载镜像文件。

1. 解压 tar 压缩包。

    ```shell
    tar xvf kpanda.bundle.tar
    ```

    解压成功后会得到 3 个文件：

    - hints.yaml
    - images.tar
    - original-chart

2. 从本地加载镜像到 Docker 或 containerd。

    === "Docker"

        ```shell
        docker load -i images.tar
        ```

    === "containerd"

        ```shell
        ctr -n k8s.io image import images.tar
        ```

!!! note

    每个 node 都需要做 Docker 或 containerd 加载镜像操作，
    加载完成后需要 tag 镜像，保持 Registry、Repository 与安装时一致。

### 升级

有两种升级方式。您可以根据前置操作，选择对应的升级方案：

!!! note

    从 kpanda 的 v0.21.0 版本开始，redis 支持设置 sentinal 密码，如果使用哨兵模式的 redis，升级时需要变更 --set global.db.redis.url。例如：
    
    - 原来是：`redis+sentinel://:3wPxzWffdn@rfs-mcamel-common-redis-cluster.mcamel-system.svc.cluster.local:26379/mymaster`
    - 现在就要改成：`redis+sentinel://:3wPxzWffdn@rfs-mcamel-common-redis-cluster.mcamel-system.svc.cluster.local:26379/mymaster?master_password=3wPxzWffdn`

=== "通过 helm repo 升级"

    1. 检查容器管理 helm 仓库是否存在。

        ```shell
        helm repo list | grep kpanda
        ```

        若返回结果为空或如下提示，则进行下一步；反之则跳过下一步。

        ```none
        Error: no repositories to show
        ```

    1. 添加容器管理的 helm 仓库。

        ```shell
        helm repo add kpanda http://{harbor url}/chartrepo/{project}
        ```

    1. 更新容器管理的 helm 仓库。

        ```shell
        helm repo update kpanda
        ```

    1. 选择您想安装的容器管理版本（建议安装最新版本）。

        ```shell
        helm search repo kpanda/kpanda --versions
        ```

        输出类似于：
        
        ```none
        NAME                   CHART VERSION  APP VERSION  DESCRIPTION
        kpanda/kpanda  0.20.0          v0.20.0       A Helm chart for kpanda
        ...
        ```

    1. 备份 `--set` 参数。

        在升级容器管理版本之前，建议您执行如下命令，备份老版本的 `--set` 参数。

        ```shell
        helm get values kpanda -n kpanda-system -o yaml > bak.yaml
        ```

    1. 更新 kpanda crds

        ```shell
        helm pull kpanda/kpanda --version 0.21.0 && tar -zxf kpanda-0.21.0.tgz
        kubectl apply -f kpanda/crds
        ```

    1. 执行 `helm upgrade` 。

        升级前建议您覆盖 bak.yaml 中的 `global.imageRegistry` 字段为当前使用的镜像仓库地址。

        ```shell
        export imageRegistry={你的镜像仓库}
        ```

        ```shell
        helm upgrade kpanda kpanda/kpanda \
          -n kpanda-system \
          -f ./bak.yaml \
          --set global.imageRegistry=$imageRegistry \
          --version 0.21.0
        ```

=== "通过 chart 包升级"

    1. 备份 `--set` 参数。

        在升级容器管理版本之前，建议您执行如下命令，备份老版本的 `--set` 参数。

        ```shell
        helm get values kpanda -n kpanda-system -o yaml > bak.yaml
        ```

    1. 更新 kpanda crds

        ```shell
        kubectl apply -f ./crds
        ```

    1. 执行 `helm upgrade` 。

        升级前建议您覆盖 bak.yaml 中的 `global.imageRegistry` 为当前使用的镜像仓库地址。

        ```shell
        export imageRegistry={你的镜像仓库}
        ```

        ```shell
        helm upgrade kpanda . \
          -n kpanda-system \
          -f ./bak.yaml \
          --set global.imageRegistry=$imageRegistry
        ```

## 通过页面方式升级

### 前提条件

在安装 DCE 5.0 或在产品模块升级前已执行以下命令：

```shell
~/dce5-installer cluster-create -c /home/dce5/sample/clusterConfig.yaml -m /home/dce5/sample/manifest.yaml -d -j 14,15
```

### 操作步骤

1. 在 __集群列表__ 页面中，搜索找到 kpanda-global-cluster 集群，进入集群详情

    ![集群列表](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/create001.png)

2. 在左侧导航栏中找到 Helm 应用，搜索 kpanda 找到容器管理模块，展开右侧操作栏，点击 __更新__ 按钮，进行升级。

    ![集群列表](../images/update-kpanda.png)

### 升级已知问题

#### 1、升级到 v0.25.1 或更高版本

问题描述：通过页面方式将 kpanda 低版本升级到 v0.25.1 或更高版本时，
可能存在镜像地址拼接问题，导致升级失败，报错提示如下：

![镜像地址报错](../images/imagequest.png)

解决办法：

在 Helm 应用中更新 kpanda 时，修改 yaml 文件，将 repository 地址修改成 `repository: xxx/xxx` 形式。

??? note "点击查看详细的 YAML 示例"

    ```yaml
    global:
      imageRegistry: 10.6.135.222/release.daocloud.io
      imagePullSecrets: []
      storageClass: ''
      kpanda:
        imageTag: v0.25.1
        enableGhippoRoutes: true
        enableSidecar: true
      db:
        builtIn: false
        redis:
          url: >-
            redis+sentinel://rfs-mcamel-common-redis-cluster.mcamel-system.svc.cluster.local:26379/mymaster?master_password=XFDYqKEyJU
          image:
            registry: release.daocloud.io
            repository: kpanda/redis
            tag: 7.0.5-alpine
            pullPolicy: IfNotPresent
      telemetry:
        tracing:
          enabled: true
          addr: >-
            insight-agent-opentelemetry-collector.insight-system.svc.cluster.local:4317
        metrics:
          enabled: true
          path: /metrics
          port: 81
      busybox:
        image:
          registry: release.daocloud.io
          repository: library/busybox
          tag: 1.34.1
          pullPolicy: IfNotPresent
      shell:
        image:
          registry: release.daocloud.io
          repository: kpanda/kpanda-shell
          tag: v0.0.9
          pullPolicy: IfNotPresent
    controllerManager:
      labels:
        app: kpanda-controller-manager
      replicaCount: 2
      podAnnotations: {}
      podLabels:
        app: kpanda-controller-manager
      image:
        registry: release.daocloud.io
        repository: kpanda/kpanda-controller-manager
        tag: ''
        pullPolicy: IfNotPresent
        pullSecrets: []
      livenessProbe:
        enabled: true
        initialDelaySeconds: 30
        timeoutSeconds: 5
        periodSeconds: 30
        successThreshold: 1
        failureThreshold: 3
        scheme: HTTP
      readinessProbe:
        enabled: true
        initialDelaySeconds: 30
        timeoutSeconds: 5
        periodSeconds: 30
        successThreshold: 1
        failureThreshold: 3
        scheme: HTTP
      resources:
        requests:
          cpu: 200m
          memory: 200Mi
      nodeSelector: {}
      affinity:
        podAntiAffinity:
          preferredDuringSchedulingIgnoredDuringExecution:
            - weight: 60
              podAffinityTerm:
                labelSelector:
                  matchExpressions:
                    - key: app
                      operator: In
                      values:
                        - kpanda-controller-manager
                topologyKey: kubernetes.io/hostname
      tolerations: []
    apiServer:
      createDefaultOrderIndex: true
      insightAgentRegistryOverride: true
      labels:
        app: kpanda-apiserver
      replicaCount: 2
      podAnnotations: {}
      podLabels: {}
      image:
        registry: release.daocloud.io
        repository: kpanda/kpanda-apiserver
        tag: ''
        pullPolicy: IfNotPresent
        pullSecrets: []
      livenessProbe:
        enabled: true
        initialDelaySeconds: 30
        timeoutSeconds: 5
        periodSeconds: 30
        successThreshold: 1
        failureThreshold: 3
        scheme: HTTP
      readinessProbe:
        enabled: true
        initialDelaySeconds: 30
        timeoutSeconds: 5
        periodSeconds: 30
        successThreshold: 1
        failureThreshold: 3
        scheme: HTTP
      resources:
        requests:
          cpu: 200m
          memory: 200Mi
      hostNetwork: false
      nodeSelector: {}
      affinity: {}
      tolerations: []
      serviceType: ClusterIP
      nodePort: null
      configMap:
        addon:
          repo:
            - URL: http://10.6.135.222:8081
              name: addon
              password: rootpass123
              username: rootuser
    kpanda-proxy:
      enabled: true
      proxyIngress:
        replicaCount: 2
        podAnnotations: {}
        podLabels: {}
        resources:
          requests:
            cpu: 100m
            memory: 128Mi
        nodeSelector: {}
        affinity: {}
        tolerations: []
      proxyEgress:
        replicaCount: 2
        podAnnotations: {}
        podLabels: {}
        resources:
          requests:
            cpu: 100m
            memory: 128Mi
        nodeSelector: {}
        affinity: {}
        tolerations: []
    clusterpedia:
      enabled: true
      podLabels:
        sidecar.istio.io/inject: 'true'
      mysql:
        enabled: false
        image:
          registry: release.daocloud.io
          repository: kpanda/mysql
          tag: 8.0.29
        primary:
          persistence:
            enabled: false
          resources:
            limits:
              cpu: 1
              memory: 1Gi
            requests:
              cpu: 100m
              memory: 128Mi
      postgresql:
        enabled: false
        image:
          registry: release.daocloud.io
          repository: kpanda/postgresql
          tag: 15.3.0-debian-11-r7
        primary:
          persistence:
            enabled: false
          resources:
            limits:
              cpu: 1
              memory: 1Gi
            requests:
              cpu: 100m
              memory: 128Mi
      storageInstallMode: external
      externalStorage:
        type: mysql
        dsn: >-
          kpanda:@tcp(mcamel-common-kpanda-mysql-cluster-mysql-master.mcamel-system.svc.cluster.local:3306)/kpanda?charset=utf8mb4&multiStatements=true&parseTime=true
        host: ''
        port: null
        user: ''
        password: ihKhByQ2Af
        database: ''
        accessType: readwrite
        connMaxIdleSeconds: 1800
        connMaxLifetimeSeconds: 3600
        maxIdleConns: 10
        maxOpenConns: 100
      installCRDs: true
      persistenceMatchNode: None
      apiserver:
        replicaCount: 2
        podAnnotations: {}
        podLabels:
          sidecar.istio.io/inject: 'true'
        image:
          registry: release.daocloud.io
          repository: clusterpedia/apiserver
          tag: v0.7.1-rc.0
          pullPolicy: IfNotPresent
          pullSecrets: []
        featureGates:
          RemainingItemCount: false
          AllowRawSQLQuery: true
        resources: {}
        tolerations: []
      clustersynchroManager:
        replicaCount: 2
        podAnnotations: {}
        podLabels:
          sidecar.istio.io/inject: 'true'
          app: kpanda-clusterpedia-clustersynchro-manager
        image:
          registry: release.daocloud.io
          repository: clusterpedia/clustersynchro-manager
          tag: v0.7.1-rc.0
          pullPolicy: IfNotPresent
          pullSecrets: []
        featureGates:
          PruneManagedFields: true
          PruneLastAppliedConfiguration: true
          AllowSyncAllCustomResources: true
          AllowSyncAllResources: true
          HealthCheckerWithStandaloneTCP: true
        resources: {}
        nodeSelector: {}
        affinity:
          podAntiAffinity:
            preferredDuringSchedulingIgnoredDuringExecution:
              - weight: 60
                podAffinityTerm:
                  labelSelector:
                    matchExpressions:
                      - key: app
                        operator: In
                        values:
                          - kpanda-clusterpedia-clustersynchro-manager
                  topologyKey: kubernetes.io/hostname
        tolerations: []
        leaderElect:
          leaseDuration: 60s
          renewDeadline: 50s
          retryPeriod: 5s
          resourceLock: leases
      controllerManager:
        labels: {}
        replicaCount: 1
        podAnnotations: {}
        podLabels:
          sidecar.istio.io/inject: 'true'
        image:
          registry: release.daocloud.io
          repository: clusterpedia/controller-manager
          tag: v0.7.1-rc.0
          pullPolicy: IfNotPresent
          pullSecrets: []
      hookJob:
        image:
          registry: release.daocloud.io
          repository: kpanda/kpanda-shell
          tag: v0.0.9
          pullPolicy: IfNotPresent
    ui:
      enabled: true
      replicaCount: 2
      podAnnotations: {}
      podLabels: {}
      image:
        registry: release.daocloud.io
        repository: kpanda/kpanda-ui
        tag: v0.24.1
        pullPolicy: IfNotPresent
        pullSecrets: []
      resources: {}
      nodeSelector: {}
      affinity: {}
      tolerations: []
    cloudtty:
      enabled: true
      labels: {}
      replicaCount: 1
      podAnnotations: {}
      podLabels:
        sidecar.istio.io/inject: 'true'
      image:
        registry: release.daocloud.io
        repository: cloudtty/cloudshell-operator
        tag: v0.6.3
        pullPolicy: IfNotPresent
        pullSecrets: []
      resources:
        requests:
          cpu: 100m
          memory: 128Mi
      nodeSelector: {}
      affinity: {}
      tolerations: []
      cloudshellImage:
        registry: release.daocloud.io
        # 将 repository 地址修改成 repository: xxx/xxx 形式，如 repository: cloudtty/cloudshell
        repository: cloudtty/cloudshell
        tag: v0.6.3
    hookJob:
      image:
        registry: release.daocloud.io
        repository: kpanda/kpanda-shell
        tag: v0.0.9
        pullPolicy: IfNotPresent
    helmJobImageOverride:
      enabled: true
      registry: release.daocloud.io
      repository: kpanda/kpanda-shell
      tag: v0.0.9
    etcdBackupRestore:
      image:
        registry: release.daocloud.io
        repository: kpanda/etcdbrctl
        tag: v0.22.0
    ```
#### 2、升级到 v0.29.0 或更高版本

问题描述：将 kpanda 低版本升级到 v0.29.0 或更高版本时，节点如果是 GPU MIG 模式，系统会将原来的 GPU MIG 模式强制切换成 GPU 整卡模式，影响业务运行，执行如下操作可避免此问题。

业务中断式升级（使用场景：已开启 GPU MIG 模式，但实际未使用）：
1. 停止所有GPU应用
2. 并且卸载 gpu-operator 以及 nvidia-vgpu
3. 升级完成后重新安装 gpu-operator，并且保证 gpu-operator 版本大于v23.9.0+1

业务连续式升级（使用场景：已开启 GPU MIG 模式，并且有实际业务正在使用 MIG 模式）：
1. 手动 修改node标签 gpu.node.kpanda.io/nvidia-gpu-mode: mig 
2. 升级kpanda版本
3. 升级gpu-operator 版本 >= v23.9.0+1