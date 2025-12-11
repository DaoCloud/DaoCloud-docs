# Unifabric 安装指南

## 前提条件

1. **Kubernetes 集群**：确保您有一个正常运行的 Kubernetes 集群
2. **Helm 3.x**：用于安装 Unifabric
3. **RDMA 网络环境**：需要 RDMA 网络环境，支持 RoCE 协议
4. **交换机 LLDP 支持**：确保网络交换机已启用 LLDP 协议

## 安装步骤

> 如果需要使用 RDMA 邻居检测功能，请确保网络交换机已启用 LLDP 协议

### 1. 节点标签配置

Unifabric Controller 只会运行在具有 `unifabric.io/deploy=true` 的节点上，需要为运行 Unifabric Controller 的节点添加标签：

```bash
kubectl label node <node-name> unifabric.io/deploy=true
```

Unifabric Agent 只应该运行在具有 RDMA 网络能力的节点上，而对于不支持 RDMA 网络能力的节点或虚拟机节点，我们应该为此类节点设置标签: `unifabric.io/deploy=false`，禁止运行 Unifabric Agent。

```bash
kubectl label node <node-name> unifabric.io/deploy=false
```

### 2. 添加 Helm 仓库

```bash
helm repo add unifabric https://release.daocloud.io/chartrepo/unifabric
helm repo update
```

### 3. 配置安装参数

```shell
$ helm upgrade --install unifabric unifabric/unifabric \
  --namespace unifabric \
  --create-namespace \
  --set features.rdmaNeighbor.storageRdmaNicFilter="interface=ens2f0*"
```

其中 `storageRdmaNicFilter` 指定节点哪些 RDMA 网卡作为 RDMA 存储网卡。
其他 RDMA 网卡作为 GPU 算力网络网卡，如果未配置本字段，则所有 RDMA 网卡都作为 GPU 算力网络网卡。

### 4. 验证安装

#### 检查 Pod 状态

```bash
kubectl get pods -n unifabric -o wide
```

预期输出：

```
NAME                         READY   STATUS    RESTARTS   AGE
unifabric-746d4f8d75-qbknh   1/1     Running   0          2m
unifabric-agent-4rpbw        2/2     Running   0          2m
unifabric-agent-fgpkc        2/2     Running   0          2m
```

注意：`unifabric-agent` Pod 包含两个容器：`lldpd` 和 `unifabric-agent`。

- 检查 FabricNode CRD 状态：

    ```bash
    kubectl get fabricnodes.unifabric.io
    ```

    查看具体节点的邻居信息：

    ```bash
    kubectl get fabricnodes.unifabric.io <node-name> -o yaml
    ```

    确认 `status.computeNics` 和 `status.storageNics` 字段包含正确的 LLDP 邻居信息。

- 验证 ScaleoutGroup 自动分组功能, 检查 ScaleoutLeafGroup CRD：

    ```bash
    kubectl get scaleoutleafgroup.unifabric.io
    ```

    查看节点是否添加了scaleoutleafgroup 的标签：

    ```bash
    kubectl get nodes -l dce.unifabric.io/scaleout-group
    ```

- 检查指标是否正常收集：

    ```bash
    kubectl get pods -n unifabric -o jsonpath='{.items[0].status.podIP}' | xargs -I {} curl {}:5026/metrics
    ```

## 故障排除

参考 [故障排除](troubleshooting.md)

## 升级

升级 Unifabric 到新版本：

```bash
helm upgrade unifabric unifabric/unifabric \
  --namespace unifabric \
  --values values.yaml \
  --wait
```

## 卸载

卸载 Unifabric：

```bash
helm uninstall unifabric --namespace unifabric
```

如需完全清理，还需要删除 CRD 和命名空间：

```bash
kubectl delete namespace unifabric
```

## 监控和可视化

如果安装了 Grafana 仪表板，可以通过 DCE Insight 或直接访问 Grafana 来查看 Unifabric 的监控数据和网络拓扑可视化。
