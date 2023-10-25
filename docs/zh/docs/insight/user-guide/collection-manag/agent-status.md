# insight-agent 组件状态说明

在 DCE 5.0 中可观测性 Insight 作为多集群观测产品，为了实现多集群观测数据的统一采集，需要用户安装 Helm 应用 `insight-agent`
（默认安装在 insight-system 命名空间）。参阅[如何安装 `insight-agent`](../../quickstart/install/install-agent.md)。

## 状态说明

在 `可观测性` -> `采集管理`部分可查看各集群安装 `insight-agent` 的情况。

- `未安装`：该集群中未在 insight-system 命名空间下安装 `insight-agent`
- `运行中`：该集群中成功安装 `insight-agent`，且部署的所有组件均处于运行中状态
- `异常`：若 insight-agent 处于此状态，说明 helm 部署失败或存在部署的组件处于非运行中状态

可通过以下方式排查：

1. 执行以下命令，若状态为 `deployed`，则执行下一步。若为 `failed`，由于会影响应用的升级，建议在 `容器管理 -> helm 应用` 卸载后重新安装 :

    ```bash
    helm list -n insight-system
    ```

2. 执行以下命令或在 `可观测性 -> 采集管理` 中查看该集群部署的组件的状态，若存在非 `运行中`状态的容器组，请重启异常的容器组。

    ```bash
    kubectl get pods -n insight-system
    ```

## 补充说明

1. `insight-agent` 中指标采集组件 Prometheus 的资源消耗与集群中运行的容器组数量存在正比关系，
   请根据集群规模调整 Prometheus 的资源，请参考：[Prometheus 资源规划](../../quickstart/res-plan/prometheus-res.md)

2. 由于全局服务集群中指标存储组件 vmstorage 的存储容量与各个集群容器组数量总和存在正比关系。

    - 请联系平台管理员根据集群规模调整 vmstorage 的磁盘容量，参阅 [vmstorage 磁盘容量规划](../../quickstart/res-plan/vms-res-plan.md)
    - 根据多集群规模调整 vmstorage 磁盘，参阅 [vmstorge 磁盘扩容](../../quickstart/res-plan/modify-vms-disk.md)
