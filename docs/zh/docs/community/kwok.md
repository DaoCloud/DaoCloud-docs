---
hide:
  - toc
---

# KWOK (`K`ubernetes `W`ith`O`ut `K`ubelet)

![kwok](./images/kwok.png){ align=right }

kwok 是 DaoCloud 自主开源并被 Kubernetes 社区接纳和管理一个开源项目。

[kwok](https://sigs.k8s.io/kwok) 可以在几秒钟内搭建由数千个节点组成的集群。
在此场景下，所有模拟节点与真实的节点行为一样，所以整体上占用的资源很少，你可以轻松在一台笔记本电脑实现这点。

到目前为止，提供了两个工具：

- **Kwok:** 模拟数千个假节点。
- **Kwokctl:** 一个 CLI，用于简化创建和管理 Kwok 模拟的集群。

请参阅 [https://kwok.sigs.k8s.io](https://kwok.sigs.k8s.io) 了解更深入的信息。

![管理集群](./images/manage-clusters.svg)

## 社区、讨论、贡献和支持

可以通过以下方式联系该项目的维护者：

- [Slack](https://kubernetes.slack.com/messages/sig-scheduling)
- [邮件列表](https://groups.google.com/forum/#!forum/kubernetes-sig-scheduling)

[了解 kwok 社区](https://github.com/kubernetes-sigs/kwok){ .md-button }
[kwok 博文](../blogs/230301-kwok.md){ .md-button }
