# 单集群跨机房高可用部署

## 场景需求

客户机房环境为单一 k8s 集群横跨 __机房A__ 、 __机房B__ ，期望可以部署一套 3 主 3 从 RocketMQ 实现跨机房服务高可用，当任一机房整体离线时，RocketMQ 仍可以正常提供服务。

![mutizone](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/middleware/rocketmq/images/crosszone01.png){ width=700px}

## RocketMQ 5.1.4 各组件镜像地址

docker pull ghcr.io/ksmartdata/rocketmq-controller:v5.1.4
docker pull ghcr.io/ksmartdata/rocketmq-nameserver:v5.1.4
docker pull ghcr.io/ksmartdata/rocketmq-broker:v5.1.4

## 解决方案

RocketMQ 5.0 通过 Dledger controller 实现 broker 高可用自动主从切换能力，该模式通过独立的 controller 实现主从切换，broker 节点无需遵循 craft 协议，不足半数 master 也可以进行选举。

    ??? warn " DCE 数据服务目前不支持 RocketMQ 5.0 ，请手动操作"

        1. 在通过 mcamel 创建完 rocektmq 集群后，需要手动将 broker cr 中的 .spec.clusterMode 从 STATIC 修改为 CONTROLLER（修改完成后，operator 应该会新建出 controller 模式下的 broker pod）；
        2. 删除掉 STATIC 模式下的生成的 broker pod 以及 pvc（pod 名字中带有 master 和 replica 字样）。

        注：新建的 CONTROLLER 模式的 broker pod 名字中没有 master 和 replica 字样。

结合 Dledger controller 能力，做以下部署设计：

- 确保 6 个 broker 分布在不同的集群 node；
- 确保每一对主/从 broker 分别分布在不同的机房；
- 尽量形成两机房的 broker master 1:2 的关系，避免所有 master 运行在同一机房
- name_srv 在两个机房分别存在副本

![mutizone](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/middleware/rocketmq/images/crosszone02.png){ width=700px}

本方案采用了工作负载的调度策略，通过具有权重的节点亲和性策略和工作负载反亲和策略达成以上部署目标。

!!! Info

    请保证各节点资源充足，避免因资源不足导致调度器无法完成正确调度。

## 操作步骤

### 创建配置

1. 创建时键入以下配置参数：

```yaml
inSyncReplicas=2
totalReplicas=2
minInSyncReplicas=1
enableAutoInSyncReplicas=true
```

![mutizone](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/middleware/rocketmq/images/crosszone03.png){ width=700px}

2. 完成创建后，修改 CR，并 重启 broker sts：

```yaml
apiVersion: rocketmq.apache.org/v1alpha1
kind: Controller
metadata:
  name: controller
  namespace: mcamel-name-work6
spec:
  controllerImage: ghcr.io/ksmartdata/rocketmq-controller:v5.1.4
  hostPath: /data/rocketmq/controller
  imagePullPolicy: IfNotPresent
  resources:
    limits:
      memory: 2Gi
    requests:
      memory: 2Gi
  size: 1
  storageMode: StorageClass #注意修改该项
  volumeClaimTemplates:
  - metadata:
      name: controller-storage
    spec:
      accessModes:
      - ReadWriteOnce
      resources:
        requests:
          storage: 1Gi
```

### 标签配置

**RocketMQ 工作负载标签**

broker 标签用于工作负载反亲和（自带标签，不用配置）：

| RocketMQ 组 | 工作负载 | 标签|
| -- | -- | -- |
| group-0 | broker-0-0/broker-0-1 | broker_cr:{RocketMQ 名称} |
| group-1 | broker-1-0/broker-1-1 | broker_cr:{RocketMQ 名称} |
| group-2 | broker-2-0/broker-2-1 | broker_cr:{RocketMQ 名称} |

**集群节点标签**

为了把 broker 按预期分配在两个机房，为两个机房的节点配置不同标签，用于确保主从 broker 落在不同的机房。

|拓扑域 |  |集群节点 | 标签  |
| -- |--|--|-- |
| az |机房 A|k8s-node-01|az:az1 |
|  |  |k8s-node-02|az:az1|
|  |  |k8s-node-03|az:az1|
|  |机房 B|k8s-node-04| az:az2 |
|  |  |k8s-node-05|az:az2|
|  |  |k8s-node-06|az:az2|

### 调度配置

- RocketMQ 采用 1 个 CR 创建 6 个 broker sts（3 主 3 从）的方式，因此每一 broker 实例需单独配置亲和性策略。

- 每两个 broker（broker-x-0 和 broker-x-1）为一组，分别担任 master 和 slave，但并无标签可以标识角色，因此配置目标是每一组内的两 broker 运行于不同机房，以此保证主、从运行在不同的机房。

- 经观察，operator 创建 broker 的过程是按编号顺序创建，尽量避免所有 master 调度在同一机房。

配置内容如下：

**1. 工作负载：broker-0-1 / broker-1-1 / broker-2-0**

```yaml
# 执行工作负载反亲和，确保每个集群节点仅调度一个 broker 副本。
      affinity:
        podAntiAffinity:
          requiredDuringSchedulingIgnoredDuringExecution:
            - labelSelector:
                matchExpressions:
                  - key: broker_cr
                    operator: In
                    values:
                      - {RocketMQ 名称}
              topologyKey: kubernetes.io/hostname
# 优先在机房 A 部署，通常每一组内先部署注册的 sts 会作为 master
        nodeAffinity:
          preferredDuringSchedulingIgnoredDuringExecution:
            - weight: 100
              preference:
                matchExpressions:
                  - key: az
                    operator: In
                    values:
                      - az1
            - weight: 90
              preference:
                matchExpressions:
                  - key: az
                    operator: In
                    values:
                      - az2
```

**2. 工作负载：broker-0-0 / broker-1-0 / broker-2-1**

```yaml

# 执行工作负载反亲和，确保每个集群节点仅调度一个 broker 副本。
      affinity:
        podAntiAffinity:
          requiredDuringSchedulingIgnoredDuringExecution:
            - labelSelector:
                matchExpressions:
                  - key: broker_cr
                    operator: In
                    values:
                      - {RocketMQ 名称}
              topologyKey: kubernetes.io/hostname
# 与同组的 sts 相反的调度优先顺序，避免调度在同一机房
        nodeAffinity:
          preferredDuringSchedulingIgnoredDuringExecution:
            - weight: 100
              preference:
                matchExpressions:
                  - key: az
                    operator: In
                    values:
                      - az2
            - weight: 90
              preference:
                matchExpressions:
                  - key: az
                    operator: In
                    values:
                      - az1
```

**3. 工作负载：namesrv**

```
# 两副本，每个机房部署一个 namesrv，无在线 namesrv 将导致 broker 工作异常。
       affinity:
        podAntiAffinity:
          requiredDuringSchedulingIgnoredDuringExecution:
            - labelSelector:
                matchExpressions:
                  - key: name_service_cr
                    operator: In
                    values:
                      - {namesrv 名称}
              topologyKey: az
```

**4. 工作负载：controller（可选）**

```
# 单副本，如果对外主要提供业务的是机房 A，可以优先部署在机房 B，该配置由具体业务情况决定。
        nodeAffinity:
          preferredDuringSchedulingIgnoredDuringExecution:
            - weight: 100
              preference:
                matchExpressions:
                  - key: az
                    operator: In
                    values:
                      - az2
             - weight: 90
              preference:
                matchExpressions:
                  - key: az
                    operator: In
                    values:
                      - az1
```

## 机房离线处理
经由上述部署方式，3 个主从组会把 master/slave broker 分别部署在不同机房。

### 机房 A 

controller 运行于机房 B，基于 Dledger controller 的主从转换机制，可以实现机房 B 的 broker slave -> master 自动升级，无需人工干预。

![mutizone](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/middleware/rocketmq/images/crosszone04.png){ width=700px}

### 机房 B 离线

![mutizone](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/middleware/rocketmq/images/crosszone05.png){ width=700px}

- 负责调度的 controller 离线，将暂时无法 slave -> master 转换，需要手动删除 Pod 漂移至其他节点。
- controller 重新调度至现存节点，才能继续完成机房 A 的 slave -> master 自动升级。


## 一些注意事项：

1. broker 角色升级失败：经实际测试，controller 稳定性不是很好，broker 的 slave -> master 自动升级有一定几率失败，可通过重启 controller 的方式，即可解决该问题。
2. 谨慎使用 sts 的 __删除__ 操作：删除重建 broker 会导致配置在实例中的调度策略丢失，但不会丢失配置在 CR 的策略，因此建议谨慎使用 __删除__ 操作。 __重启__ sts 的操作不会造成以上的丢失情况。

    ![mutizone](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/middleware/rocketmq/images/crosszone06.png){ width=700px}

3. 机房离线导致 console 无法获取数据：如果采用 2 副本 console，一个机房离线可能导致 console 无法连接 name_srv。
    - 解决办法：重启现存 console 工作负载。
4. dashboard 异常查看 broker 列表：如果 dashboard 不可访问，也可以通过其他方式获取 broker 列表信息，建议在部署完成后立即使用一下方式查看节点分布，确保符合预期。
    - 方法 1：进入 name_srv Pod，执行以下命令：

    ```
    ./mqadmin clusterList -n 127.0.0.1:9876
    ````

    ![mutizone](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/middleware/rocketmq/images/crosszone07.png){ width=700px}

    BID = 0：表示该节点为 Master
    BID <> 0：表示该节点为 slave

    - 方法 2：进入 controller，执行以下命令：

    ```
    ./mqadmin getSyncStateSet -a 127.0.0.1:9878 -c {实例名} -b {rocketmq 主从组名}
    例：./mqadmin getSyncStateSet -a 127.0.0.1:9878 -c rmq-ha-i -b rmq-ha-i-0
    ```