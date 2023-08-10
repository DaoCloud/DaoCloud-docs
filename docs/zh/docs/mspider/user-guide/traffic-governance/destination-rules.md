# 目标规则

目标规则（DestinationRule）同样是服务治理中重要的组成部分，目标规则通过端口、服务版本等方式对请求流量进行划分，并对各请求分流量订制 envoy 流量策略，应用到流量的策略不仅有负载均衡，还有最小连接数、离群检测等。

## 字段概念介绍

几个重要字段如下：

- Host

    使用 Kubernetes Service 的短名称。含义同 VirtualService 中 `destination` 的 `host` 字段一致。服务一定要存在于对应的服务注册中心中，否则会被忽略。

- LoadBalancer

    默认情况下，Istio 使用轮询的负载均衡策略，实例池中的每个实例依次获取请求。
    Istio 同时支持如下的负载均衡模型，可以在 DestinationRule 中为流向某个特定服务或服务子集的流量指定这些模型。

    - 随机：请求以随机的方式转到池中的实例。
    - 权重：请求根据指定的百分比转到实例。
    - 最少请求：请求被转到最少被访问的实例。

- Subsets

    `subsets` 是服务端点的集合，可以用于 A/B 测试或者分版本路由等场景。
    可以将一个服务的流量切分成 N 份供客户端分场景使用。
    `name` 字段定义后主要供 VirtualService 里 `destination` 使用。
    每个子集都是在 `host` 对应服务的基础上基于一个或多个 `labels` 定义的，在 Kubernetes 中它是附加到像 Pod 这种对象上的键/值对。
    这些标签应用于 Kubernetes 服务的 Deployment 并作为元数据信息（Metadata）来识别不同的版本。

- OutlierDetection

    离群检测是减少服务异常和降低服务延迟的一种设计模式，主要是无感的处理服务异常并保证不会发生级联甚至雪崩。
    如果在一定时间内服务累计发生错误的次数超过了预先定义的阈值，就会将该错误的服务从负载均衡池中移除，并持续关注服务的健康状态，当服务回复正常后，又会将服务再移回到负载均衡池。

## 目标规则列表介绍

目标规则列表展示了网格下的目标规则 CRD 信息，并提供了目标规则生命期管理能力。
用户可以基于规则名称、规则标签做 CRD 筛选，规则标签如下：

- 服务版本
- 负载均衡
- 地域负载均衡
- HTTP 连接池
- TCP 连接池
- 客户端 TLS
- 离群检测

![目标规则列表](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/images/destirule06.png)

## 操作步骤

服务网格提供了两种创建方式：图形向导创建和 YAML 创建。通过图形向导创建的具体操作步骤如下：

1. 在左侧导航栏点击`流量治理` -> `目标规则`，点击右上角的`创建`按钮。

    ![创建](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/images/destirule01.png)

2. 在`创建目标`界面中，先进行基本配置后点击`下一步`。

    ![创建目标](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/images/destirule02.png)

3. 按屏幕提示选择策略类型，并配置对应的治理策略后，点击`确定`。

    ![治理策略](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/images/destirule03.png)

4. 返回目标规则列表，屏幕提示创建成功。

    ![创建成功](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/images/destirule04.png)

5. 在列表右侧，点击操作一列的 `⋮`，可通过弹出菜单进行更多操作。

    ![更多操作](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/images/destirule05.png)

YAML 创建方式与虚拟服务相似，您可以直接借助内置模板创建 YAML 文件，如下图所示。

![YAML 创建](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/images/destirule07.png)

以下是一个 目标规则的 YAML 示例：

```yaml
apiVersion: networking.istio.io/v1beta1
kind: DestinationRule
metadata:
  annotations:
    ckube.daocloud.io/cluster: dywtest3
    ckube.daocloud.io/indexes: '{"activePolices":"","cluster":"dywtest3","createdAt":"2023-08-10T02:18:04Z","host":"kubernetes","is_deleted":"false","labels":"","name":"dr01","namespace":"default"}'
  creationTimestamp: "2023-08-10T02:18:04Z"
  generation: 1
  managedFields:
    - apiVersion: networking.istio.io/v1beta1
      fieldsType: FieldsV1
      fieldsV1:
        f:spec:
          .: {}
          f:host: {}
          f:trafficPolicy:
            .: {}
            f:portLevelSettings: {}
      manager: cacheproxy
      operation: Update
      time: "2023-08-10T02:18:04Z"
  name: dr01
  namespace: default
  resourceVersion: "708763"
  uid: ff95ba70-7b92-4998-b6ba-9348d355d44c
spec:
  host: kubernetes
  trafficPolicy:
    portLevelSettings:
      - port:
          number: 9980
status: {}
```

## 策略介绍

### 地域负载均衡

地域负载均衡是 Istio 具备的一个基于工作负载部署所在的 Kubernetes 集群工作节点上的地域标签，用作流量转发优化的策略。
配置方式主要有：流量分发规则（权重分布）和流量转移规则（故障转移）：

- 流量分发规则：主要配置源负载位置访问到目标负载位置在不同的区域之间的流量权重分配
- 流量转移规则：流量的故障转移一般需要配合离群检测功能使用，可以达到更及时检测工作负载故障进行流量转移

注意，地域标签是在网格成员集群的工作节点上的 label，注意检查节点的标签配置：

- 地区：`topology.kubernetes.io/region`
- 可用区域：`topology.kubernetes.io/zone`
- 分区：`topology.istio.io/subzone` 分区是 istio 特有的配置，以实现更细粒度划分

另外地域是根据分层顺序进行匹配排列的，不同 `region` 的 `zone` 是两个不同的可用区域。

详情请参阅 Istio 官方文档： <https://istio.io/latest/zh/docs/tasks/traffic-management/locality-load-balancing/>
