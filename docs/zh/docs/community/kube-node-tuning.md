# kube-node-tuning

kube-node-tuning 旨在通过 Kubernetes 进行内核调优。它对以下情况很有用：

- 高性能应用程序
- 大规模集群
- 网络调优

## 快速开始

```bash
export VERSION=v0.3.1
helm repo add kube-node-tuning https://kubean-io.github.io/kube-node-tuning/
helm install -n kube-node-tuning kube-node-tuning kube-node-tuning/kube-node-tuning --version $VERSION --create-namespace
```

!!! 提示

    如果机器位于中国，请按照以下步骤进行：[在中国快速开始](docs/quick-start-in-china.md)

内核的 sysctl 设置将应用于节点的 `/etc/99-kube-node-tuning.conf` 文件。

通过以下命令检查设置是否已应用。
SSH 到集群的节点

```bash
cat /etc/sysctl.d/99-kube-node-tuning.conf
sysctl -a # 查看sysctl设置
```

## 配置

```bash
# 修改配置
kubectl -n kube-node-tuning edit cm/kube-node-tuning-config -o yaml

# 重启DaemonSet
kubectl -n kube-node-tuning rollout restart ds kube-node-tuning
```

## 路线图

- 不同操作系统支持（Ubuntu，CentOS，RHEL 等）
- 多个配置文件
- 使用 Operator 替代 DaemonSet

## 参考链接

- [kube-node-tunning 仓库](https://github.com/kubean-io/kube-node-tuning)
