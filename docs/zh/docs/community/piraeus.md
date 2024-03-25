# Piraeus 数据存储 - Kubernetes 的高可用性数据存储

Piraeus 是一个高性能、高可用、简单、安全且与云无关的存储解决方案，适用于 Kubernetes。

Piraeus 项目包括：

* [Kubernetes Operator](https://github.com/piraeusdatastore/piraeus-operator)，用于创建、配置和维护 Piraeus 的所有组件。
* [CSI Driver](https://github.com/piraeusdatastore/linstor-csi)，用于在 Piraeus 维护的存储集群上提供持久卷和快照。
* [高可用性控制器](https://github.com/piraeusdatastore/piraeus-ha-controller)，用于加速有状态工作负载的故障转移过程。
* [卷关联控制器](https://github.com/piraeusdatastore/linstor-affinity-controller)，保持 Kubernetes 持久卷上报的关联与集群同步。
* Piraeus 构建在开源组件的容器映像上：
    * [DRBD](https://github.com/LINBIT/drbd) 用作集群节点之间的基础存储复制机制。
      [文档](https://docs.linbit.com/docs/users-guide-9.0/)由 [LINBIT](https://www.linbit.com/) 提供。
    * [LINSTOR](https://github.com/LINBIT/linstor-server)根据 CSI Driver 的请求创建和管理卷，使用 DRBD 设置复制并准备后备存储设备。
      [文档](https://docs.linbit.com/docs/linstor-guide/)由 [LINBIT](https://www.linbit.com/) 提供。

Piraeus 是一个 [CNCF 沙盒项目](https://www.cncf.io/sandbox-projects/)。

## 入门

安装 Piraeus 可能就像这样简单：

```bash
$ kubectl apply --server-side -k "https://github.com/piraeusdatastore/piraeus-operator//config/default?ref=v2"
namespace/piraeus-datastore configured
...
$ kubectl wait pod --for=condition=Ready -n piraeus-datastore -l app.kubernetes.io/component=piraeus-operator
pod/piraeus-operator-controller-manager-dd898f48c-bhbtv condition met
$ kubectl apply -f - <<EOF
apiVersion: piraeus.io/v1
kind: LinstorCluster
metadata:
  name: linstorcluster
spec: {}
EOF
```

请查看[Piraeus Operator 文档](https://github.com/piraeusdatastore/piraeus-operator/tree/v2/docs)以了解更多信息。其中包含有关如何开始使用 Piraeus 的详细说明。

它还包含一个基本的 Helm 图表。请参见[这里](https://github.com/piraeusdatastore/piraeus-operator/tree/v2/charts/piraeus)。

### 社区

活跃的沟通渠道：

- [Slack](https://piraeus-datastore.slack.com/join/shared_invite/enQtOTM4OTk3MDcxMTIzLTM4YTdiMWI2YWZmMTYzYTg4YjQ0MjMxM2MxZDliZmEwNDA0MjBhMjIxY2UwYmY5YWU0NDBhNzFiNDFiN2JkM2Q)

Piraeus 数据存储主要是一个将 LINSTOR 和 DRBD 连接到 Kubernetes 的粘合项目。因此，对于对 Piraeus 数据存储感兴趣的人来说，[LINSTOR]和[DRBD]的沟通渠道也是相关的。这包括...

- [LINBIT 社区 Slack](https://linbit-community.slack.com/join/shared_invite/enQtOTg0MTEzOTA4ODY0LTFkZGY3ZjgzYjEzZmM2OGVmODJlMWI2MjlhMTg3M2UyOGFiOWMxMmI1MWM4Yjc0YzQzYWU0MjAzNGRmM2M5Y2Q#/shared-invite/email)
- [DRBD 相关邮件列表](https://lists.linbit.com/)
- [LINBIT 社区会议](https://linbit.com/community-meeting/)

## 参考链接

- [Piraeus 仓库](https://github.com/piraeusdatastore/piraeus)
- [Piraeus 网站](https://piraeus.io/)
