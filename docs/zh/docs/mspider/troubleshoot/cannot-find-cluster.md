# 创建网格时找不到所属集群

## 原因分析

主要原因在于所属集群的 __MeshCluster__ 状态不是 "CLUSTER_RUNNING"，可登录 global 集群查看所属集群的 MeshCluster CRD 状态。

```bash
kubectl get meshcluster -n mspider-system
```

造成这种问题的情况有几种：

### 情况 1

如果先前未使用该所属集群创建过网格，执行上述命令未发现该所属集群的 meshcluster CRD，
可能是因为 gsc-controller 从容器管理（kpanda）同步集群异常。

### 情况 2

针对已创建的网格移除集群，执行上述命令。发现该集群的 __meshcluster__ 状态可能处于如下状态之一：

- MANAGED_RECONCILING
- MANAGED_SUCCEED
- MANAGED_EVICTING
- MANAGED_FAILED

原因可能是正在清理资源或者存在 meshconfig 未清理干净。

## 解决方案

1. 针对情况 1，只需要重启 global 集群的 gsc-controller 即可。

    ```bash
    kubectl -n mspider-system delete pod $(kubectl -n mspider-system get pod -l app=mspider-gsc-controller -o 'jsonpath={.items.metadata.name}')
    ```

2. 针对情况 2，由于环境可能未清理干净。请确保所属集群(控制面集群)控制面组件清理干净，否则影响下一次网格创建。

    1. 删除未清理干净导致装态异常的 meshconfig

        ```bash
        kubectl delete meshcluster -n mspider-system ${clustername}
        ```

    1. 重启 gsc-controller 重新同步集群

        ```bash
        kubectl delete po -n mspider-system ${gsc-coontroller-xxxxxxxxxx}
        ```
