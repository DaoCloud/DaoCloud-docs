---
hide:
  - toc
---

# 云原生启航

在当今时代，云原生容器化技术正在迅猛发展，席卷全球。想要抓住这一市场趋势，获得巨大的商业机遇，必须紧跟时代的脉搏。
而将数据中心转型为 Kubernetes（简称 K8s）底座，无疑是实现云原生图景的最佳途径。

DCE 5.0 以 K8s 作为开发底座，提供了高度可扩展、强大灵活的各项生产级功能，使得企业能够轻松构建和管理分布式应用程序。
借助 DCE 5.0 的云原生天赋，企业可以充分利用云上云下优势，实现资源的最优利用，提高 IT 系统的可靠性和弹性，极大地加速应用程序的交付速度。

!!! tip

    掌握容器化浪潮，畅享 DaoCloud Enterprise 5.0，从这里启航！

## 安装和教程

<div class="grid cards" markdown>

- :fontawesome-solid-jet-fighter-up:{ .lg .middle } __安装__

    ---

    DCE 5.0 支持离线和在线两种安装方式，可以安装到不同的 Linux 发行版上。

    - [安装依赖项](../install/install-tools.md)
    - [安装社区版](../install/community/resources.md)
    - [安装商业版](../install/commercial/deploy-requirements.md)
    - [安装到各种 Linux 发行版](../install/os-install/uos-v20-install-dce5.0.md)
    - [安装到不同 K8s 版本](../install/k8s-install/ocp-install-dce5.0.md)

- :material-microsoft-azure-devops:{ .lg .middle } __视频教程__

    ---

    我们为 DCE 5.0 的各个模块和场景制作了精良的视频教程。

    - [场景化视频](../videos/use-cases.md)
    - [应用工作台视频](../videos/amamba.md)
    - [容器管理视频](../videos/kpanda.md)
    - [微服务视频](../videos/skoala.md)
    - [中间件视频](../videos/mcamel.md)
    - [全局管理视频](../videos/ghippo.md)

</div>

## 产品模块

<div class="grid cards" markdown>

- :material-microsoft-azure-devops:{ .lg .middle } __应用工作台__

    ---

    这是基于容器的 DevOps 云原生应用平台，在 DCE 5.0 中是创建应用的统一入口。

    - [基于向导创建应用](../amamba/user-guide/wizard/create-app-git.md)
    - [流水线](../amamba/user-guide/pipeline/create/custom.md)
    - [GitOps](../amamba/user-guide/gitops/create-argo-cd.md)
    - [灰度发布](../amamba/user-guide/release/canary.md)
    - [集成工具链](../amamba/user-guide/tools/integrated-toolchain.md)

- :octicons-container-16:{ .lg .middle } __容器管理__

    ---

    这是基于 K8s 构建的面向云原生应用的容器化管理模块，它是 DCE 5.0 的核心。

    - [集群管理](../kpanda/user-guide/clusters/create-cluster.md)
    - [节点管理](../kpanda/user-guide/nodes/add-node.md)
    - [命名空间管理](../kpanda/user-guide/namespaces/createns.md)
    - [工作负载：Deployment, StatefulSet, DamemonSet, Job, CronJob](../kpanda/user-guide/workloads/create-deployment.md)
    - [Helm 应用](../kpanda/user-guide/helm/helm-app.md)

</div>

<div class="grid cards" markdown>

- :material-cloud-check:{ .lg .middle } __多云编排__

    ---

    这是以应用为中心、开箱即用的多云应用编排平台，实现了多云和混合云的集中管理。

    - [多云工作集群](../kairship/cluster.md)
    - [多云工作负载](../kairship/workload/deployment.md)
    - [多云自定义资源](../kairship/crds/crd.md)
    - [服务/路由/命名空间等资源管理](../kairship/resource/service.md)
    - [策略管理](../kairship/policy/propagation.md)

- :material-warehouse:{ .lg .middle } __镜像仓库__

    ---

    支持多实例生命期管理的云原生镜像托管服务，支持集成 Harbor 和 Docker 等镜像仓库。

    - [镜像空间](../kangaroo/space/index.md)
    - [仓库集成(工作空间)](../kangaroo/integrate/integrate-ws.md)
    - [仓库集成(管理员)](../kangaroo/integrate/integrate-admin.md)
    - [托管 Harbor](../kangaroo/managed/intro.md)

</div>

<div class="grid cards" markdown>

- :material-engine:{ .lg .middle } __微服务引擎__

    ---

    这是面向业界主流微服务生态的一站式微服务管理平台，主要提供微服务治理中心和微服务网关两个维度的功能。

    - [云原生网关](../skoala/gateway/index.md)
    - [云原生微服务](../skoala/cloud-ms/index.md)
    - [传统微服务](../skoala/trad-ms/hosted/index.md)
    - [插件中心](../skoala/plugins/intro.md)

- :material-table-refresh:{ .lg .middle } __服务网格__

    ---

    基于 Istio 开源技术构建的面向云原生应用的下一代服务网格。

    - [流量治理](../mspider/user-guide/traffic-governance/README.md)
    - [安全治理](../mspider/user-guide/security/README.md)
    - [边车管理](../mspider/user-guide/sidecar-management/workload-sidecar.md)
    - [流量监控](../mspider/user-guide/traffic-monitor/README.md)

</div>

<div class="grid cards" markdown>

- :material-middleware:{ .lg .middle } __中间件之一__

    ---

    DCE 5.0 针对实际应用场景，选用经典的中间件来处理数据。

    - [Elasticsearch 搜索服务](../middleware/elasticsearch/intro/index.md)
    - [MinIO 对象存储](../middleware/minio/intro/index.md)
    - [MySQL 数据库](../middleware/mysql/intro/index.md)
    - [PostgreSQL 数据库](../middleware/postgresql/intro/index.md)

- :material-middleware:{ .lg .middle } __中间件之二__

    ---

    DCE 5.0 针对实际应用场景，选用经典的中间件来处理数据。

    - [MongoDB 数据库](../middleware/mongodb/intro/index.md)
    - [Redis 缓存服务](../middleware/redis/intro/index.md)
    - [RabbitMQ 消息队列](../middleware/rabbitmq/intro/index.md)
    - [Kafka 消息队列](../middleware/kafka/intro/index.md)

</div>

<div class="grid cards" markdown>

- :fontawesome-solid-user-group:{ .lg .middle } __全局管理__

    ---

    以用户为中心的综合性服务板块，包含用户与访问控制、工作空间与层级、审计日志、平台设置等基础服务。

    - [用户与访问控制](../ghippo/user-guide/access-control/user.md)
    - [工作空间与层级](../ghippo/user-guide/workspace/workspace.md)
    - [审计日志](../ghippo/user-guide/audit/open-audit.md)
    - [运营管理和系统设置](../ghippo/user-guide/platform-setting/appearance.md)

- :material-monitor-dashboard:{ .lg .middle } __可观测性__

    ---

    这是以应用为中心、开箱即用的新一代可观测平台，实时监控应用及资源，采集各项指标、日志及事件等数据分析应用健康状态。

    - [基础设施监控](../insight/user-guide/scenario-insight/cluster.md)
    - [日志查询](../insight/user-guide/data-query/log.md)
    - [链路追踪](../insight/user-guide/data-query/trace.md)
    - [告警](../insight/user-guide/alert-center/index.md)

</div>

<div class="grid cards" markdown>

- :material-dot-net:{ .lg .middle } __云原生网络__
    
    ---

    基于多个开源技术构建，不仅提供单个 CNI 网络支持，也提供多个 CNI 网络的组合方案。

    - [网卡和网络规划](../network/plans/ethplan.md)
    - [性能测试报告](../network/performance/cni-performance.md)
    - [如何集成不同的 CNI](../network/modules/calico/install.md)

- :floppy_disk:{ .lg .middle } __云原生存储__
    
    ---

    DCE 5.0 云原生存储基于 Kubernetes CSI 标准，可根据不同 SLA 要求及用户场景对接符合 CSI 标准的存储。

    - [什么是 DCE 5.0 云原生存储](../storage/index.md)
    - [HwameiStor 本地存储](../storage/hwameistor/intro/index.md)
    - [集成开源存储方案](../storage/solutions/rook-ceph.md)

</div>

## 下载和开源生态

<div class="grid cards" markdown>

- :material-download:{ .lg .middle } __下载中心__
    
    ---

    下载中心包含了 DCE 5.0 社区版、商业版以及各个子模块的离线安装包。

    - [下载社区版](../download/free/dce5-installer-history.md)
    - [下载商业版](../download/business/dce5-installer-history.md)
    - [下载子模块](../download/index.md#_3)

- :simple-opensourceinitiative:{ .lg .middle } __DaoCloud 开源生态__
    
    ---

    DaoCloud 秉承开源企业文化，已有多项开源技术入选 CNCF Sandbox。

    - [Clusterpedia 多集群百科全书](../community/clusterpedia.md)
    - [HwameiStor 本地化存储](../community/hwameistor.md)
    - [Merbridge 服务网格加速](../community/merbridge.md)

</div>

!!! success

    ```yaml
    是什么让一个企业走向成功？
      是方向一致的梦想，
        是开源分享的喜悦，
          是日夜贡献成功构建魔法后的欣喜若狂。
    
    让我们一起，
      致敬曾经、现在和未来的努力吧！
    ```

[下载 DCE 5.0](../download/index.md){ .md-button .md-button--primary }
[安装 DCE 5.0](../install/index.md){ .md-button .md-button--primary }
[申请社区免费体验](./license0.md){ .md-button .md-button--primary }

![启航图](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/dce/images/sail.jpg)
