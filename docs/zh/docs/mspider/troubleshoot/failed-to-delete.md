---
hide:
  - toc
---

# 创建的网格异常但无法删除

## 原因分析

网格处于失败状态，无法点击网格实例。
由于该网格中纳管了集群、创建了网格网关实例、或启用了边车注入，导致移除网格时检测总是失败，所以无法被正常删除。

## 解决方案

建议排查具体网格失败的原因并解决，如果想要强制删除，请执行以下操作：

1. 禁用纳管集群的边车注入

    1. 禁用命名空间边车自动注入。

        在 __容器管理__ 中，选择该集群 –> __命名空间__ –> 修改标签 —> 移除 `istio-injection: enabled` 标签，重启该命名空间下的所有 Pod。

        ![移除标签](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/troubleshoot/images/delete01.png)

    1. 禁用工作负载边车注入：

        在 __容器管理__ 中，选择该集群 –> __工作负载__ —> __无状态负载__ —> __标签与注解__ —> 移除 `sidecar.istio.io/inject: true` 标签。

        ![禁用边车注入](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/troubleshoot/images/delete02.png)

1. 删除创建的网格网关实例。

1. 移除集群。

    在 __容器管理__ 中，选择 global 集群，自定义资源搜索 `globalmeshes.discovery.mspider.io` 。
    在 mspider-system 命名空间下选择要移除集群的网格，编辑 YAML：

    ![编辑yaml](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/troubleshoot/images/delete03.png)

1. 返回服务网格，删除该网格实例。
