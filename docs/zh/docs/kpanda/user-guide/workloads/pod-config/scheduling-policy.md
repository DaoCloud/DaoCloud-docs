# 调度策略

在 Kubernetes 集群中，节点也有[标签](https://kubernetes.io/zh-cn/docs/concepts/overview/working-with-objects/labels/)。您可以[手动添加标签](https://kubernetes.io/zh-cn/docs/tasks/configure-pod-container/assign-pods-nodes/#add-a-label-to-a-node)。 Kubernetes 也会为集群中所有节点添加一些标准的标签。参见[常用的标签、注解和污点](https://kubernetes.io/zh-cn/docs/reference/labels-annotations-taints/)以了解常见的节点标签。通过为节点添加标签，您可以让 Pod 调度到特定节点或节点组上。您可以使用这个功能来确保特定的 Pod 只能运行在具有一定隔离性，安全性或监管属性的节点上。

`nodeSelector` 是节点选择约束的最简单推荐形式。您可以将 `nodeSelector` 字段添加到 Pod 的规约中设置您希望目标节点所具有的[节点标签](https://kubernetes.io/zh-cn/docs/concepts/scheduling-eviction/assign-pod-node/#built-in-node-labels)。Kubernetes 只会将 Pod 调度到拥有指定每个标签的节点上。`nodeSelector` 提供了一种最简单的方法来将 Pod 约束到具有特定标签的节点上。亲和性和反亲和性扩展了您可以定义的约束类型。使用亲和性与反亲和性的一些好处有：

- 亲和性、反亲和性语言的表达能力更强。`nodeSelector` 只能选择拥有所有指定标签的节点。亲和性、反亲和性为您提供对选择逻辑的更强控制能力。

- 您可以标明某规则是“软需求”或者“偏好”，这样调度器在无法找到匹配节点时，会忽略亲和性/反亲和性规则，确保 Pod 调度成功。

- 您可以使用节点上（或其他拓扑域中）运行的其他 Pod 的标签来实施调度约束，而不是只能使用节点本身的标签。这个能力让您能够定义规则允许哪些 Pod 可以被放置在一起。

您可以通过设置亲和（affinity）与反亲和（anti-affinity）来选择 Pod 要部署的节点。

## 容忍时间

当工作负载实例所在的节点不可用时，系统将实例重新调度到其它可用节点的时间窗。默认为 300 秒。

## 节点亲和性（nodeAffinity）

节点亲和性概念上类似于 `nodeSelector`， 它使您可以根据节点上的标签来约束 Pod 可以调度到哪些节点上。 节点亲和性有两种：

- **必须满足：（`requiredDuringSchedulingIgnoredDuringExecution`）** 调度器只有在规则被满足的时候才能执行调度。此功能类似于 `nodeSelector`， 但其语法表达能力更强。您可以定义多条硬约束规则，但只需满足其中一条。

- **尽量满足：（`preferredDuringSchedulingIgnoredDuringExecution`）** 调度器会尝试寻找满足对应规则的节点。如果找不到匹配的节点，调度器仍然会调度该 Pod。您还可为软约束规则设定权重，具体调度时，若存在多个符合条件的节点，权重最大的节点会被优先调度。同时您还可以定义多条硬约束规则，但只需满足其中一条。

#### 标签名

对应节点的标签，可以使用默认的标签也可以用户自定义标签。

#### 操作符

- In：标签值需要在 values 的列表中
- NotIn：标签的值不在某个列表中
- Exists：判断某个标签是存在，无需设置标签值
- DoesNotExist：判断某个标签是不存在，无需设置标签值
- Gt：标签的值大于某个值（字符串比较）
- Lt：标签的值小于某个值（字符串比较）

#### 权重

仅支持在“尽量满足”策略中添加，可以理解为调度的优先级，权重大的会被优先调度。取值范围是 1 到 100。

## 工作负载亲和性

与节点亲和性类似，工作负载的亲和性也有两种类型：

- **必须满足：（`requiredDuringSchedulingIgnoredDuringExecution`）** 调度器只有在规则被满足的时候才能执行调度。此功能类似于 `nodeSelector`， 但其语法表达能力更强。您可以定义多条硬约束规则，但只需满足其中一条。
- **尽量满足：（`preferredDuringSchedulingIgnoredDuringExecution`）** 调度器会尝试寻找满足对应规则的节点。如果找不到匹配的节点，调度器仍然会调度该 Pod。您还可为软约束规则设定权重，具体调度时，若存在多个符合条件的节点，权重最大的节点会被优先调度。同时您还可以定义多条硬约束规则，但只需满足其中一条。

工作负载的亲和性主要用来决定工作负载的 Pod 可以和哪些 Pod部 署在同一拓扑域。例如，对于相互通信的服务，可通过应用亲和性调度，将其部署到同一拓扑域（如同一可用区）中，减少它们之间的网络延迟。

#### 标签名

对应节点的标签，可以使用默认的标签也可以用户自定义标签。

#### 命名空间

指定调度策略生效的命名空间。

#### 操作符

- In：标签值需要在 values 的列表中
- NotIn：标签的值不在某个列表中
- Exists：判断某个标签是存在，无需设置标签值
- DoesNotExist：判断某个标签是不存在，无需设置标签值

#### 拓扑域

指定调度时的影响范围。例如，如果指定为 `kubernetes.io/Clustername` 表示以 Node 节点为区分范围。

## 工作负载反亲和性

与节点亲和性类似，工作负载的反亲和性也有两种类型：

- **必须满足：（`requiredDuringSchedulingIgnoredDuringExecution`）** 调度器只有在规则被满足的时候才能执行调度。此功能类似于 `nodeSelector`， 但其语法表达能力更强。您可以定义多条硬约束规则，但只需满足其中一条。
- **尽量满足：（`preferredDuringSchedulingIgnoredDuringExecution`）** 调度器会尝试寻找满足对应规则的节点。如果找不到匹配的节点，调度器仍然会调度该 Pod。您还可为软约束规则设定权重，具体调度时，若存在多个符合条件的节点，权重最大的节点会被优先调度。同时您还可以定义多条硬约束规则，但只需满足其中一条。

工作负载的反亲和性主要用来决定工作负载的 Pod 不可以和哪些 Pod 部署在同一拓扑域。例如，将一个负载的相同 Pod 分散部署到不同的拓扑域（例如不同主机）中，提高负载本身的稳定性。

#### 标签名

对应节点的标签，可以使用默认的标签也可以用户自定义标签。

#### 命名空间

指定调度策略生效的命名空间。

#### 操作符

- In：标签值需要在 values 的列表中
- NotIn：标签的值不在某个列表中
- Exists：判断某个标签是存在，无需设置标签值
- DoesNotExist：判断某个标签是不存在，无需设置标签值

#### 拓扑域

指定调度时的影响范围。例如，如果指定为 `kubernetes.io/Clustername` 表示以 Node 节点为区分范围。
