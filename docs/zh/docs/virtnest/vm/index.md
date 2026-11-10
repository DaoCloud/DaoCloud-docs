---
hide:
  - toc
---

# 虚拟机管理

虚拟机创建完成后，可在同一平台完成密钥配置、快照与克隆、迁移与漂移、网络与存储调整，以及监控与健康检查等日常运维。本页按任务汇总虚拟机管理相关文档，可按需跳转。

<div class="grid cards" markdown>

-   :one: [配置与安全](#vm-config)
-   :two: [快照与克隆](#vm-snapshot)
-   :three: [迁移与漂移](#vm-migration)
-   :four: [网络与存储](#vm-network)
-   :five: [监控与健康](#vm-health)

</div>

## 配置与安全 {: #vm-config }

<div class="grid cards" markdown>

-   :material-key-outline:{ .lg .middle } __[创建密钥](create-secret.md)__

    使用 S3 对象存储作为镜像来源时，创建用于访问验证的密钥

</div>

## 快照与克隆 {: #vm-snapshot }

<div class="grid cards" markdown>

-   :material-content-save-move:{ .lg .middle } __[快照管理](snapshot.md)__

    为虚拟机创建快照，并从快照恢复

-   :material-calendar-clock:{ .lg .middle } __[定时快照](scheduled-snapshot.md)__

    按计划定期自动创建快照

-   :material-content-copy:{ .lg .middle } __[克隆虚拟机](clone.md)__

    基于已有虚拟机克隆出一台新虚拟机

</div>

## 迁移与漂移 {: #vm-migration }

<div class="grid cards" markdown>

-   :material-swap-horizontal:{ .lg .middle } __[实时迁移](live-migration.md)__

    在虚拟机运行状态下将其迁移到其他节点

-   :material-arrow-right-bold-outline:{ .lg .middle } __[集群内冷迁移](migratiom.md)__

    在关机状态下，于同一集群内迁移虚拟机

-   :material-transit-connection-variant:{ .lg .middle } __[虚拟机跨集群迁移](cross-cluster-migrate.md)__

    在集群之间迁移虚拟机，当前需按命令行步骤操作，暂无 UI 界面

-   :material-autorenew:{ .lg .middle } __[虚拟机自动漂移](auto-migrate.md)__

    节点断电或网络故障时，自动将该节点上的虚拟机迁移到可用节点

</div>

## 网络与存储 {: #vm-network }

<div class="grid cards" markdown>

-   :material-lan:{ .lg .middle } __[虚拟机网络](vm-network.md)__

    创建虚拟机时配置网络模式、多网卡与固定 IP

-   :material-harddisk:{ .lg .middle } __[虚拟机存储](vm-sc.md)__

    创建虚拟机时配置系统盘、数据盘与存储类

</div>

## 监控与健康 {: #vm-health }

<div class="grid cards" markdown>

-   :material-chart-line:{ .lg .middle } __[虚拟机监控](monitor.md)__

    基于 KubeVirt Grafana Dashboard 查看每台虚拟机的监控看板

-   :material-stethoscope:{ .lg .middle } __[健康检查](health-check.md)__

    通过 YAML 配置存活（Liveness）与就绪（Readiness）探针

</div>

## 相关文档

<div class="grid cards" markdown>

-   :material-view-grid-outline:{ .lg .middle } __功能特性总览__

    ---

    查看虚拟机支持的全部操作，以及每项操作对应的虚拟机状态。

    [:arrow_forward: 虚拟机功能特性](../intro/features.md)

-   :material-cube-outline:{ .lg .middle } __创建虚拟机__

    ---

    通过镜像、模板或 YAML 创建虚拟机，并配置网络与存储。

    [:arrow_forward: 快速入门](../quickstart/index.md)

-   :material-monitor-eye:{ .lg .middle } __连接虚拟机__

    ---

    使用 VNC / 终端登录虚拟机，查看虚拟机详情与监控信息。

    [:arrow_forward: 访问虚拟机](../quickstart/access.md)

</div>

[下载中心](https://docs.daocloud.io/download/){ .md-button }
[了解 Token 工厂效能平台](https://docs.daocloud.io/tf/){ .md-button }
[了解 d.run AI 操作系统](https://docs.daocloud.io/drun/){ .md-button }
