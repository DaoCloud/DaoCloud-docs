---
hide:
  - toc
---

# 常见问题

1. Karmada 的版本是多少？能否指定版本？是否可以升级？

    当前默认版本 v1.4.0，支持用户自主升级。

2. 单集群应用如何无缝迁移到多云编排？

    可以使用我们的新功能 [一键升级为多云工作负载](../workload/promote.md)。

3. 是否支持跨集群的应用日志收集？

    暂不支持，之后会增加该功能。

4. 分发到多个集群的工作负载，是否可以在一个视图呈现监控信息？

    支持在统一的视图来查看多云应用，可以监控他们部署到了什么集群，对应的 Service、传播策略等等。

5. 工作负载是否可以跨集群通信？

    Karmada 本身不支持，产品可以借助开源社区 Submariner  来支持，未来多云编排会提供方案性的支持。

6. Service 能否实现跨集群服务发现？

    Karmada 本身不支持，产品可以借用外部方案 multi-dns 来支持，未来多云编排会提供方案性的支持。

7. Karmada 是否有生产级别支持？

    目前还处于 TP 阶段，很多内部组件高可用有待解决 (Karmada 依赖的 etcd 等等)。

8. 如何做到故障转移？

    Karmada 原生支持故障转移的功能，在成员集群出现故障的时候，Karmada 会进行智能的重调度，完成故障转移。

9. 多集群的权限问题

    紧密的结合 5.0 现有的权限体系，与 workspace 打通，完成 Karmada 实例与 workspaces 的绑定，解决权限问题。

10. 如何查询多集群的事件？

    多云编排完成了产品级别的整合，会展示所有 Karmada 实例级别的事件。

11. 通过多云编排创建一个多云应用之后，通过 容器管理 怎么能获取的相关资源信息？

    了解 Karmada 的小伙伴都知道，Karmada control-plane 其本质也就是一个完整 kubernetes 控制面，只是没有任何承载 workload 的节点。因此多云编排在创建多云编排实例的时候，采用了一个取巧的动作，会把实例本身作为一个隐藏的 cluster 加入到容器管理中(不在容器管理中显示)。这样就可以完全借助容器管理的能力(搜集加速检索各个 K8s 集群的资源，CRD 等)，当在界面中查询某个多云编排实例的资源（Deployment、PropagationPolicy、OverridePolicy 等) 就可以直接通过容器管理进行检索，做到读写分离，加快响应时间。

12. 如何自定义 `karmada` 镜像来源仓库地址？

    Kairship 采用开源的 `karmada-operator` 进行多实例 LCM 管理；Operator 提供了丰富的自定义能力。支持在启动参数中自定义 karmada 资源镜像的仓库地址。

    可以在启动命令中增加对应的参数配置，`--chat-repo-url`

    ![image](https://docs.daocloud.io/daocloud-docs-images/docs/kairship/images/faq01.png)
