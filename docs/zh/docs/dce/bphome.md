---
hide:
  - toc
---

# DCE 5.0 最佳实践汇总

本页汇总了 DCE 5.0 各模块的最佳实践文档。
这些最佳实践是指在使用和管理 DCE 5.0 平台过程中，通过长期经验积累和验证，被广泛认可为比较有效、可靠的方法和流程。
这些内容涵盖了安装、集群创建和接入、应用管理、多云编排、中间件等方面，旨在帮助用户更高效、更稳定地运行和维护容器化应用。

!!! tip "有人说"

    :man_factory_worker: 遵循最佳实践，确保卓越性能 
    <span style="color: green;">Practice Makes You Perfect.</span>

## 安装与工作台

<div class="grid cards" markdown>

- :fontawesome-solid-jet-fighter-up:{ .lg .middle } __安装__

    ---

    支持离线和在线安装方式，可安装到各种 Linux 和 K8s 发行版上

    - [在一体机上部署 DCE 5.0](../install/best-practices/all-in-one-machine.md)
    - [Bootstrap 火种节点高可用方案](../install/best-practices/thinder-ha.md)
    - [安装时 etcd 采用 host 模式与控制平面分离](../install/best-practices/etcd-host-deploy.md)
    - [安装到不同 Linux 发行版](../install/os-install/uos-v20-install-dce5.0.md)
    - [安装到 OpenShift 和阿里云上](../install/k8s-install/ocp-install-dce5.0.md)

- :material-microsoft-azure-devops:{ .lg .middle } __应用工作台__

    ---

    基于容器的 DevOps 云原生应用平台，是创建应用的统一入口

    - [基于流水线和 GitOps 实现 CI/CD](../amamba/quickstart/argocd-jenkins.md)
    - [使用流水线实现代码扫描](../amamba/quickstart/scan-with-pipeline.md)
    - [集成 Harbor 实现镜像安全扫描](../amamba/quickstart/scan-with-harbor.md)
    - [基于 Contour 的灰度发布实践](../amamba/quickstart/contour-argorollout.md)
    - [应用工作台技术概览](../amamba/intro/tech-overview.md)

</div>

## 容器

<div class="grid cards" markdown>

- :octicons-container-16:{ .lg .middle } __容器管理之一__

    ---

    基于 K8s 构建工作集群和节点，它是 DCE 5.0 的核心

    - [在 CentOS 上创建 Ubuntu 工作集群](../kpanda/best-practice/create-ubuntu-on-centos-platform.md)
    - [在 CentOS 上创建 RedHat 9.2 工作集群](../kpanda/best-practice/create-redhat9.2-on-centos-platform.md)
    - [从 DCE 4.0 迁移到 DCE 5.0](../kpanda/best-practice/dce4-5-migration.md)
    - [部署与升级 Kubean 向下兼容版本](../kpanda/best-practice/kubean-low-version.md)
    - [在 DCE 5.0 上使用 NVIDIA GPU](../kpanda/user-guide/gpu/nvidia/index.md)

- :octicons-container-16:{ .lg .middle } __容器管理之二__

    ---

    采用原生多集群架构，便捷创建和接入 K8s 集群

    - [为工作集群添加异构节点](../kpanda/best-practice/multi-arch.md)
    - [工作集群离线升级](../kpanda/best-practice/update-offline-cluster.md)
    - [工作集群的控制节点扩容](../kpanda/best-practice/add-master-node.md)
    - [替换工作集群的首个控制节点](../kpanda/best-practice/replace-first-master-node.md)
    - [为全局服务集群的工作节点扩容](../kpanda/best-practice/add-worker-node-on-global.md)

- :material-warehouse:{ .lg .middle } __镜像仓库__

    ---

    支持多实例的镜像托管服务，支持 Harbor 和 Docker 等仓库

    - [托管 Harbor 应选择什么访问类型](../kangaroo/best-practice/managed-harbor-select-access-type.md)
    - [登录非安全的镜像仓库](../kangaroo/best-practice/insecure_registry.md)
    - [Harbor Nginx 配置实践](../kangaroo/best-practice/harbor-nginx.md)
    - [镜像仓库容量资源规划](../kangaroo/best-practice/capacity-planning.md)
    - [通过 LB 模式部署 Harbor](../kangaroo/best-practice/lb.md)

- :material-dot-net:{ .lg .middle } __云原生网络__
    
    ---

    基于多个开源技术构建，支持单个和多个 CNI 网络方案

    - [网卡和网络规划](../network/plans/ethplan.md)
    - [性能测试报告](../network/performance/cni-performance.md)
    - [集成 Spiderpool](../network/modules/spiderpool/index.md)
    - [集成 Calico](../network/modules/calico/index.md)
    - [集成 Cilium](../network/modules/cilium/index.md)

- :simple-googlecloudstorage:{ .lg .middle } __云原生存储__
    
    ---

    可根据不同 SLA 要求及场景对接符合 CSI 标准的存储

    - [通过应用商店部署 Rook-ceph](../storage/solutions/dce-rook-ceph.md)
    - [通过应用商店部署 Longhorn](../storage/solutions/dce-longhorn.md)
    - [通过 Helm 部署并验证 OpenEBS](../storage/solutions/openebs-helm.md)
    - [集成部署 TiDB](../storage/hwameistor/application/tidb.md)
    - [通过 Helm 模板部署 Fluid](../storage/solutions/fluid.md)

- :material-cloud-check:{ .lg .middle } __多云编排和虚拟机__

    ---

    **多云编排** 实现了多云和混合云的集中管理。
    **虚拟机** 是基于 KubeVirt 构建的容器化虚拟机平台。

    - [跨集群弹性伸缩](../kairship/best-practice/fhpa.md)
    - [DCE 4.0 一键转换为 DCE 5.0 多云应用](../kairship/best-practice/one-click-conversion.md)
    - [将 VMWare 虚拟机导入到 DCE 5.0](../virtnest/import/import-ubuntu.md)

</div>

## 微服务

<div class="grid cards" markdown>

- :material-monitor-dashboard:{ .lg .middle } __可观测性__

    ---

    实时监控应用及资源，采集各项指标、日志及事件等数据来分析应用健康与否

    - [Insight 部署资源规划](../insight/quickstart/res-plan/index.md)
    - [ElasticSearch 数据塞满时如何操作](../insight/faq/expand-once-es-full.md)
    - [使用 Insight 定位应用异常](../insight/best-practice/find_root_cause.md)
    - [使用 OTel 赋予应用可观测性](../insight/quickstart/otel/otel.md)
    - [使用 OTel SDK 为应用暴露指标](../insight/quickstart/otel/meter.md)

- :material-engine:{ .lg .middle } __微服务引擎__

    ---

    主要提供微服务治理中心和微服务网关两个维度的功能

    - [示例应用体验微服务治理](../skoala/best-practice/use-skoala-01.md)
    - [在云原生微服务中使用 JWT 插件](../skoala/best-practice/plugins/jwt.md)
    - [微服务网关接入认证服务器](../skoala/best-practice/auth-server.md)
    - [网关 API 策略](../skoala/best-practice/gateway02.md)
    - [通过网关访问微服务](../skoala/best-practice/gateway01.md)

- :material-table-refresh:{ .lg .middle } __服务网格__

    ---

    基于 Istio 开源技术构建面向云原生应用的下一代服务网格

    - [网格漏洞修复标准与计划](../mspider/intro/sla.md)
    - [服务网格应用接入规范](../mspider/intro/app-spec.md)
    - [使用网格完成定向服务访问限制](../mspider/best-practice/use-egress-and-authorized-policy.md)
    - [网格支持接入的自定义工作负载类型](../mspider/best-practice/use-custom-workloads.md)
    - [多云互联网格服务访问及流量精准控制](../mspider/best-practice/multinet-control.md)

</div>

## 数据服务和管理

<div class="grid cards" markdown>

- :material-middleware:{ .lg .middle } __中间件__

    ---

    针对实际场景选用经典中间件来处理数据

    - [MySQL 跨集群同步方案](../middleware/mysql/best-practice/crossclusterssync.md)
    - [Redis 单集群跨机房高可用部署](../middleware/redis/best-practice/singleclustercrosszone.md)
    - [基于 Hwameistor 的 ES 迁移实践](../middleware/elasticsearch/user-guide/migrate-es.md)
    - [Kafka 双机房部署灾备方案](../middleware/kafka/bestpractice/kafkain2IDC.md)
    - [RabbitMQ 单集群跨机房高可用部署](../middleware/rocketmq/best-pratice/singleclustercrosszone.md)

- :fontawesome-solid-user-group:{ .lg .middle } __全局管理__

    ---

    以用户为中心的综合服务板块，包含用户与访问控制、工作空间与层级、审计日志、平台设置等

    - [工作空间(租户)绑定跨集群命名空间](../ghippo/best-practice/ws-to-ns.md)
    - [将单集群分配给多个工作空间(租户)](../ghippo/best-practice/cluster-for-multiws.md)
    - [超大型企业的架构管理](../ghippo/best-practice/super-group.md)
    - [GProduct 对接全局管理](../ghippo/best-practice/gproduct/intro.md)
    - [OEM IN 和 OEM OUT](../ghippo/best-practice/oem/oem-in.md)

- :material-slot-machine:{ .lg .middle } __智能算力和云边协同__

    ---

    **智能算力** 训推一体化平台，软硬一体，整合异构算力，优化 GPU 性能。
    而 **云边协同** 则将容器能力扩展到了边缘。

    - [部署 NFS 做数据集预热](../baize/best-practice/deploy-nfs-in-worker.md)
    - [智能设备控制](../kant/best-practice/device-control.md)
    - [开发设备驱动应用 mapper](../kant/best-practice/develop-device-mapper.md)

</div>

![best practices](../images/bphome.jpeg)
