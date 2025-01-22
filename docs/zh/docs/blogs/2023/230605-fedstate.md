# 云原生联邦中间件--FedState 正式开源上线

![image](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/blogs/images/fedstate01.png)

在云原生的场景下，有状态的服务，也有了很大的发展。有的玩法是基于 Yaml 的包装来手动安装，
有的基于 Helm Charts 的方式封装，有的是基于 Operator 的方式的来封装的。目前社区的玩法中，
以 Helm Chart 和 Operator 偏多，特别是基于 Operator 的方式，因为它是面向编程友好的方式，
可以根据需求进行各种能力的开发。现在社区开源的各种中间件，数据库的 Operator 也是层出不穷的，
但是主要是集中在单集群的玩法，这个和 Operator 的框架本身是有关系的。在多云/联邦的环境下，
怎么设计和实现基于多集群、多数据中心以及混合云场景下，有状态服务的编排、调度、部署和自动化运维等能力？
最新开源的 FedState 项目正是在尝试解决这样的场景问题。

FedState 的开源仓库地址在：https://github.com/fedstate/fedstate 。
接下来，整体介绍一下 FedState，同时结合 MongoDB 为例来分析。

## 需求分析

首先先来大概分析一下，客户对中间件在多云场景下的使用需求大概有哪些。

- 跨容器集群/数据中心部署中间件
- 统一控制面和数据面的多层架构规范
- 成员容器集群的资源统计能力
- 根据成员容器集群资源合理调度中间件负载
- 根据不同中间件的特性灵活适配去完成调度
- 跨容器集群中间件组件之间的发现
- 集群的统一外部访问入口
- 中间件集群的跨多集群的拓扑
- 中间件集群的扩容
- 中间件集群的缩容
- 跨容器集群的数据复制/容灾能力
- 中间件集群的自动化运维能力
- 云原生方式提供服务
- 页面化管理中间件集群的能力
- 开放的 API 能力，方便上层能力的建设
- 存储的开放性，适配 CSI
- 租户隔离
- 多版本中间件支持
- 监控，告警等能力

## 架构介绍

目前 FedState 除了实现了联邦中间件的框架之外，还内置实现了联邦 MongoDB 和单集群 MongoDB 的中间件能力。
控制平面和数据平面是相对独立的。可以直接用单集群的 MongoDB Manager 在单集群的场景下使用，
也可以使用联邦场景下的 MongoDB 能力。同时，联邦的 MongoDB 是使用了单集群模式的 MongoDB Manager。

这里，以联邦 MongoDB 为例。以下架构图介绍了 FedState 在多云/多集群环境中，围绕 MongoDB 副本集，提供的整体能力。

![图片](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/blogs/images/fedstate02.png)

FedState 自身包含以下组件：

Multicloud-Middleware-Scheduler : 负责收集工作集群的资源使用情况，根据资源使用情况给出合理的调度方式。
同时不同的中间件有自己的特性，会有对应中间件的特殊调度逻辑，帮助各种中间件更好的选择适合自己的调度结果。
可以根据需要扩展对不同类型的中间件的调度策略和实现。

Federation-Mongo-Manager ：可以理解成 MongoDB 控制面的 Operator，主要负责这些中间件服务按需配置、
进行合理调度以及通过 Karmada 进行分发。可以根据需要扩展不同的中间件进来。

Mongo-Manager：可以理解成 MongoDB 数据面的 Operator，主要负责真正的服务负载的处理。
可以根据需要扩展不同的中间件进来。这里也可以选择优秀的开源的 Operator，
只要这个 Operator 本身满足控制平面对于数据平面 Operator 的要求就可以，
只要在控制平面进行扩展，就可以支持这种中间件，让其具备联邦中间件的能力。

## 关键能力

![图片](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/blogs/images/fedstate03.png)

1. 联邦 MongoDB 实例的对外访问方式：Vip0:NodePort0, Vip1:NodePort1...
2. 各个成员集群间 MongoDB 服务的东西向流量以及服务发现，使用来对应集群 VIP+服务所对应的 NodePort 方式
3. 除了支持联邦 MongoDB 副本集的创建与更新等能力以外，还可以直接用数据面的 Operator 来在单集群的模式线，创建和管理 MongoDB 的集群
4. 根据不同的中间件的特性，分布不同的角色的节点部署在不同的集群中，保证中间件的高可用的要求
5. 支持手动方式，调整集群规模，来完成扩容和缩容的能力
6. 支持故障迁移，基于 Karmada 和自定义的迁移策略
7. 支持 Prometheus 方式的监控，收集 MongoDB 各个节点的 metrics 数据
8. 自定义配置文件，可以根据需要，设置 MongoDB 支持的各种配置项
9. 支持 MongoDB 集群认证，完成客户端连接的认证
10. 支持 CSI 存储，持久化中间件数据
11. 支持 MongoDB 集群的拓扑，清晰地观测各个 MongoDB 节点的运行状态
12. 支持 MongoDB 副本集的方式，组建 MongoDB 集群

## 业务模型

以 MongoDB 为例，介绍在联邦和单集群下提供的一些常见能力介绍：

### 联邦模式下的 MongoDB 集群

创建和管理联邦有状态服务的资源对象，会根据配置分发有状态服务到各成员集群，
设置需要的存储，开启监控，密码配置等，创建成功后，会在状态中展示 MongoDB 在各个成员集群上的部署拓扑以及访问地址。
这种模式适合联邦集群下，使用控制平面和数据平面的 MongoDB Operator 安装和管理跨集群的 MongoDB 集群的场景。

??? note "点击查看 MultiCloudMongoDB YAML 示例"

    ```yaml
    apiVersion: middleware.fedstate.io/v1alpha1
    kind: MultiCloudMongoDB
    metadata:
      name: multicloudmongodb-sample
    spec:
      replicaset: 5 # 副本数
      export: # 监控配置
        enable: true
        resource:
          limits:
            cpu: "500m"
            memory: 512Mi
          requests:
            cpu: "200m"
            memory: 256Mi
      resource: # 有状态服务资源配置
        limits:
          cpu: "2"
          memory: 512Mi
        requests:
          cpu: "1"
          memory: 512Mi
      storage: # 存储设置
        storageClass: managed-nfs-storage
        storageSize: 1Gi
      imageSetting: # 镜像设置
        image: mongo:3.6
        imagePullPolicy: Always
        imagePullSecret: "my-image-secret"
      auth: # 密码设置
        rootPasswd: "mypasswd"
      config: # 有状态服务配置设置
        arbiter: false
        configRef: "my-custome-configmap"
      scheduler: # 调度设置，调度模型等配置
        schedulerMode: Uniform
      spreadConstraints: # 调度配置，节点选择等相关配置
        nodeSelect:
          deploy: mongo
    ```

### 单集群模式下的 MongoDB 集群

创建和管理有状态服务的资源对象，这种模式适合单集群下，使用数据平面的 MongoDB Operator 直接安装和管理 MongoDB 集群的场景。

??? note "点击查看 MongoDB YAML 示例"

    ```yaml
    apiVersion: middleware.fedstate.io/v1alpha1
    kind: MongoDB
    metadata:
      name: mongodb-sample
    spec:
      members: 1 # 副本数
      image: mongo:3.6 # 可以指定某个mongo版本进行部署，默认为mongo 6.0版本
      imagePullSecret: # 镜像拉取认证信息
        username: admin
        password: admin
      imagePullPolicy: Always # 镜像拉取策略
      config: # 参考mongo的配置进行填入
         - name: LOG_LEVEL
           value: info
      customConfigRef: mongo-operator-mongo-default-config # 自定义mongo config, 指定cm name, 默认为mongo-default-config
      rootPassword: "123456" # 指定初始密码
      resources:
        limits:
          cpu: "1"
          memory: 512Mi
        requests:
          cpu: "1"
          memory: 512Mi
      persistence: # 持久化参数
        storage: 1Gi
        storageClassName: "" # 存储类型，默认为空，使用默认sc
      metricsExporterSpec:
        enable: true # 监控是否开启，默认为true
        resources:
          limits:
            cpu: "0.1"
            memory: 128Mi
          requests:
            cpu: "0.1"
            memory: 128Mi
      podSpec:
        nodeSelector: # 节点选择器
        securityContext: # pod 安全上下文
        topologySpreadConstraints: # 拓扑分布约束
        affinity: # 亲和和反亲和
        tolerations: # 污点容忍
    ```

## 案例介绍

虽然支持联邦和单集群两种模式，这里的案例以联邦的方式展示案例。

### 在控制平面下发联邦 MongoDB 集群的 CR

```yaml
apiVersion: middleware.fedstate.io/v1alpha1
kind: MultiCloudMongoDB
metadata:
  name: multicloudmongodb-sample
spec:
  replicaset: 5
  export:
    enable: false
  resource:
    limits:
      cpu: "2"
      memory: 512Mi
    requests:
      cpu: "1"
      memory: 512Mi
  storage:
    storageClass: managed-nfs-storage
    storageSize: 1Gi
  imageSetting:
    image: mongo:3.6
    imagePullPolicy: Always
```

### 查看控制平面的 MongoDB CR 实例状态

??? note "点击查看 MultiCloudMongoDB YAML 示例"

    ```yaml
    apiVersion: middleware.fedstate.io/v1alpha1
    kind: MultiCloudMongoDB
    metadata:
      annotations:
        kubectl.kubernetes.io/last-applied-configuration: |
          {"apiVersion":"middleware.fedstate.io/v1alpha1","kind":"MultiCloudMongoDB","metadata":{"annotations":{},"name":"multicloudmongodb-sample","namespace":"federation-mongo-operator"},"spec":{"export":{"enable":false},"imageSetting":{"image":"mongo:3.6","imagePullPolicy":"Always"},"replicaset":5,"resource":{"limits":{"cpu":"2","memory":"512Mi"},"requests":{"cpu":"1","memory":"512Mi"}},"storage":{"storageClass":"managed-nfs-storage","storageSize":"1Gi"}}}
        schedulerResult: '{"ClusterWithReplicaset":[{"cluster":"10-29-14-21","replicaset":4},{"cluster":"10-29-14-25","replicaset":1}]}'
      creationTimestamp: "2023-05-25T07:06:26Z"
      finalizers:
      - multiCloudMongoDB.finalizers.middleware.fedstate.io
      generation: 1
      name: multicloudmongodb-sample
      namespace: federation-mongo-operator
      resourceVersion: "72770747"
      uid: 56c69f88-6c52-4886-a922-9ebf7c156ba5
    spec:
      auth:
        rootPasswd: 39nZzksAmXE=
      config: {}
      export:
        resource: {}
      imageSetting:
        image: mongo:3.6
        imagePullPolicy: Always
        imagePullSecret: {}
      member: {}
      replicaset: 5
      resource:
        limits:
          cpu: "2"
          memory: 512Mi
        requests:
          cpu: "1"
          memory: 512Mi
      scheduler:
        schedulerMode: Uniform
        schedulerName: multicloud-middleware-scheduler
      spreadConstraints: {}
      storage:
        storageClass: managed-nfs-storage
        storageSize: 1Gi
    status:
      conditions:
      - lastTransitionTime: "2023-05-25T07:07:57Z"
        message: Service Dispatch Successful And Ready For External Service
        reason: ServerReady
        status: "True"
        type: ServerReady
      - lastTransitionTime: "2023-05-25T07:06:26Z"
        message: 'The number of member clusters is the same as the number of control plane
          copies, check, SpecReplicaset: 5'
        reason: CheckSuccess
        status: "True"
        type: ServerCheck
      - lastTransitionTime: "2023-05-25T07:06:26Z"
        message: 'Get Scheduler Result From MultiCloudMongoDB Annotations Success (federation-mongo-operator/multicloudmongodb-sample):
          {"ClusterWithReplicaset":[{"cluster":"10-29-14-21","replicaset":4},{"cluster":"10-29-14-25","replicaset":1}]}'
        reason: GetSchedulerSuccess
        status: "True"
        type: ServerScheduledResult
      externalAddr: 10.29.5.103:33498,10.29.5.103:38640,10.29.5.103:37661,10.29.5.103:35880,10.29.5.107:38640
      result:
      - applied: true
        cluster: 10-29-14-21
        connectAddrWithRole:
          10.29.5.103:33498: SECONDARY
          10.29.5.103:35880: SECONDARY
          10.29.5.103:37661: SECONDARY
          10.29.5.103:38640: PRIMARY
        currentRevision: multicloudmongodb-sample-666cb9cb8
        replicasetSpec: 4
        replicasetStatus: 4
        state: Running
      - applied: true
        cluster: 10-29-14-25
        connectAddrWithRole:
         10.29.5.107:38640: SECONDARY
        currentRevision: multicloudmongodb-sample-866554df84
        replicasetSpec: 1
        replicasetStatus: 1
        state: Running
      state: Health
    ```

### 查看数据平面派生出来的 MongoDB CR 实例

??? note "点击查看 MongoDB YAML 示例"

    ```yaml
    apiVersion: middleware.fedstate.io/v1alpha1
    kind: MongoDB
    metadata:
      annotations:
        resourcebinding.karmada.io/name: multicloudmongodb-sample-mongodb
        resourcebinding.karmada.io/namespace: federation-mongo-operator
        resourcetemplate.karmada.io/uid: 66c5d156-88f7-445f-b068-15dcb327e452
      creationTimestamp: "2023-05-25T07:06:26Z"
      finalizers:
      - mongodb.finalizers.middleware.fedstate.io
      generation: 1
      labels:
        app.kubernetes.io/instance: multicloudmongodb-sample
        app.multicloudmongodb.io/vip: 10.29.5.103
        propagationpolicy.karmada.io/name: multicloudmongodb-sample
        propagationpolicy.karmada.io/namespace: federation-mongo-operator
        resourcebinding.karmada.io/key: 8484fbdb6f
        work.karmada.io/name: multicloudmongodb-sample-8484fbdb6f
        work.karmada.io/namespace: karmada-es-10-29-14-21
      name: multicloudmongodb-sample
      namespace: federation-mongo-operator
      resourceVersion: "232973338"
      selfLink: /apis/middleware.fedstate.io/v1alpha1/namespaces/federation-mongo-operator/mongodbs/multicloudmongodb-sample
      uid: f53b0751-ba6e-4172-b52a-e4ba611b522f
    spec:
      dbUserSpec: {}
      image: mongo:3.6
      imagePullPolicy: IfNotPresent
      imagePullSecret: {}
      memberConfigRef: multicloudmongodb-sample-hostconf
      members: 4
      metricsExporterSpec:
        enable: false
      persistence:
        storage: 1Gi
      resources:
        limits:
          cpu: "2"
          memory: 512Mi
        requests:
          cpu: "1"
          memory: 512Mi
      rootPassword: 39nZzksAmXE=
      rsInit: true
      type: ReplicaSet
    status:
      conditions:
      - lastTransitionTime: "2023-05-25T07:07:25Z"
        message: replset-0
        status: "True"
        type: rsInit
      - lastTransitionTime: "2023-05-25T07:07:38Z"
        message: replset-0
        status: "True"
        type: userRoot
      - lastTransitionTime: "2023-05-25T07:07:38Z"
        message: replset-0
        status: "True"
        type: userClusterAdmin
      currentInfo:
        members: 4
        resources:
          limits:
            cpu: "2"
            memory: 512Mi
          requests:
            cpu: "1"
            memory: 512Mi
      currentRevision: multicloudmongodb-sample-666cb9cb8
      replset:
      - _id: 0
        health: 1
        name: 10.29.5.103:33498
        state: 2
        stateStr: SECONDARY
        syncSourceHost: 10.29.5.107:38640
        syncingTo: 10.29.5.107:38640
      - _id: 1
        health: 1
        name: 10.29.5.103:38640
        state: 1
        stateStr: PRIMARY
        syncSourceHost: ""
        syncingTo: ""
      - _id: 2
        health: 1
        name: 10.29.5.107:38640
        state: 2
        stateStr: SECONDARY
        syncSourceHost: 10.29.5.103:38640
        syncingTo: 10.29.5.103:38640
      - _id: 3
        health: 1
        name: 10.29.5.103:37661
        state: 2
        stateStr: SECONDARY
        syncSourceHost: 10.29.5.107:38640
        syncingTo: 10.29.5.107:38640
      - _id: 4
        health: 1
        name: 10.29.5.103:35880
        state: 2
        stateStr: SECONDARY
        syncSourceHost: 10.29.5.107:38640
        syncingTo: 10.29.5.107:38640
      state: Running
    ```

## 社区

随着对有状态服务的跨云分发和自动化运维能力的需求不断增加，围绕这个场景的方案探索和实践，将变得更加有意义。

现在云原生联邦中间件 - FedState 项目已经在 Github 开源上线了，欢迎对多云、联邦场景有状态服务感兴趣的开发者，
来一起体验和试用，也非常欢迎大家一起参与进来一起贡献。

项目地址：https://github.com/fedstate/fedstate
