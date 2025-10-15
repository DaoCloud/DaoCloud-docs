# Troubleshooting

## Grafana Dashboard data is not displayed

1. Run `kubectl get pods -n unifabric -o wide` to check the status of the unifabric pods.
2. Run `curl unifactric-pod:5026` to check metrics of Pod are available.
3. Run `curl unifactric-svc:5026` to check metrics of Service available.
4. Run `kubectl get switchendpoint` to check the status of the switch if connected.

## 常见问题

### 1. lldpd 容器启动失败

**症状:** lldpd 容器无法启动或频繁重启

**排查步骤:**

```bash
# 查看容器日志
kubectl logs -l app=unifabric-agent -c lldpd

# 检查容器状态
kubectl describe pod <pod-name>
```

**可能原因:**

- 权限不足：确保容器具有 `privileged: true` 权限
- 网络接口不存在：检查配置的接口是否存在

### 2. 无法发现邻居设备

**症状:** `lldpcli show neighbors` 返回空结果

**排查步骤:**

```bash
# 检查 LLDP 服务状态
kubectl exec -it <pod-name> -c lldpd -- lldpcli -v

# 查看接口状态
kubectl exec -it <pod-name> -c lldpd -- lldpcli show interfaces

# 检查网络连接
kubectl exec -it <pod-name> -c lldpd -- ip link show
```

**可能原因:**

- 邻居设备未启用 LLDP
- 网络接口未正确配置
- 防火墙阻止 LLDP 报文

### 3. JSON 解析错误

**症状:** unifabric-agent 日志中出现 JSON 解析错误

**排查步骤:**

```bash
# 查看 agent 日志
kubectl logs -l app=unifabric-agent -c unifabric-agent

# 手动测试 JSON 输出
kubectl exec -it <pod-name> -c unifabric-agent -- lldpcli show neighbors -f json0
```

**解决方案:**

- 检查 lldpcli 版本兼容性
- 验证 JSON 输出格式

### 4. ScaleoutGroup 相关问题

**症状:** ScaleoutGroup 未创建或状态异常

**排查步骤:**

```bash
# 查看所有 ScaleoutGroup
kubectl get scaleoutgroups.unifabric.io

# 查看特定组的详细信息
kubectl get scaleoutgroups.unifabric.io scaleoutgroup-a1b2c3d4 -o yaml

# 查看控制器日志
kubectl logs -l app=unifabric-controller -n unifabric
```

**解决方案:**

检查 FabricNode 的 LLDP 邻居信息

```bash
kubectl get fabricnodes.unifabric.io -o jsonpath='{range .items[*]}{.metadata.name}{": "}{.status.computeNics[*].lldpNeighbor.hostname}{"\n"}{end}'

# 检查特定节点的邻居信息
kubectl get fabricnodes.unifabric.io sh-cube-gpu-13 -o jsonpath='{.status.computeNics[*].lldpNeighbor.hostname}'
```

## 调试命令

```bash
# 查看 LLDP 邻居（详细信息）
lldpcli show neighbors -f keyvalue

# 查看 LLDP 统计信息
lldpcli show statistics

# 查看 LLDP 配置
lldpcli show configuration

# 查看本地信息
lldpcli show chassis
```
