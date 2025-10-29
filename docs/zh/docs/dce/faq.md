# 常见问题

这是一个 DCE 5.0 常见问题和故障排查的索引页面。

## 安装

- UI 访问问题
    - [安装结束后打不开 DCE 5.0 界面，可执行 diag.sh 脚本快速排障](../install/faq.md#dce-50-diagsh)
    - [安装使用 Metallb 时因 VIP 访问不通导致 DCE 5.0 登录界面无法打开](../install/faq.md#metallb-vip-dce)
- 火种节点问题
    - [火种节点关机重启后，kind 集群无法正常重启](../install/faq.md#kind)
    - [Ubuntu 20.04 作为火种机器部署时缺失 ip6tables](../install/faq.md#ubuntu-2004-ip6tables)
    - [安装时禁用 IPv6 后，火种节点 Podman 无法创建容器](../install/faq.md#ipv6-podman)
    - [火种节点 kind 容器重启后，kubelet 服务无法启动](../install/faq.md/#kind-kubelet)
    - [如何卸载火种节点的数据](../install/faq.md#_3)
- 证书问题
    - [全局服务集群的 kubeconfig 在火种的副本需要更新](../install/faq.md#kubeconfig)
    - [火种节点的 kind 集群本身的证书更新以及 kubeconfig](../install/faq.md#kind-kubeconfig)
    - [Contour 安装后，证书默认有效期仅一年，且不会自动 renew，过期后导致 contour-envoy 组件不断重启](../install/faq.md#contour-renew-contour-envoy)
- 操作系统相关问题
    - [在 CentOS 7.6 安装时报错](../install/faq.md#centos-76)
    - [CentOS 环境准备问题](../install/faq.md#centos)
    - [osRepos 的 external 模式 externalRepoURLs 检查失败](../install/faq.md#osrepos-external-externalrepourls)
    - [Manifest 开启 MySQL MGR 模式无效](../install/faq.md#manifest-mysql-mgr)
    - [MGR 模式 MySQL Common 实例初始化失败导致 DCE 安装失败](../install/faq.md#mgr-mysql-common-dce)
- 社区版安装问题
    - [kind 集群重装 DCE 5.0 时 Redis 卡住](../install/faq.md#kind-dce-50-redis)
    - [社区版安装 fluent-bit 失败](../install/faq.md#fluent-bit)

## 应用工作台

- 流水线相关问题
    - [执行流水线时报错](../amamba/faq/faq-jenkins.md#_2)
    - [如何更新内置 Label 的 podTemplate 镜像？](../amamba/faq/faq-jenkins.md#label-podtemplate)
    - [流水线构建环境为 maven 时，如何在 settings.xml 中修改依赖包来源？](../amamba/faq/faq-jenkins.md#maven-settingsxml)
    - [通过 Jenkins 构建镜像时，容器无法访问私有镜像仓库](../amamba/faq/faq-jenkins.md#jenkins)
    - [如何修改 Jenkins 流水线并发执行数量](../amamba/faq/faq-jenkins.md#jenkins_1)
    - [流水线运行状态更新不及时怎么办？](../amamba/faq/faq-jenkins.md#_3)
- GitOps 相关问题
    - [在 GitOps 模块下添加 GitHub 仓库时报错](../amamba/faq/faq-gitops.md#gitops-github)
    - [在某个工作空间下在 GitOps 模块中添加仓库时提示仓库已经存在](../amamba/faq/faq-gitops.md#gitops_1)
- 工具链相关问题
    - [当流水线运行代理为 Maven 且使用集成的 SonarQube Java 代码语言扫描时报错](../amamba/faq/faq-toochain.md#maven-sonarqube-java)
    - [部署 GitLab 时有哪些注意事项](../amamba/faq/faq-toochain.md#gitlab)

## 容器管理

- [容器管理和全局管理模块的权限问题](../kpanda/intro/faq.md#permissions)
- Helm 安装：
    - [Helm 应用安装失败，提示 “OOMKilled”](../kpanda/intro/faq.md#oomkilled)
    - [Helm 安装应用时，无法拉取 kpanda-shell 镜像](../kpanda/intro/faq.md#kpanda-shell)
    - [Helm Chart 界面未显示最新上传到 Helm Repo 的 Chart](../kpanda/intro/faq.md#no-chart)
    - [Helm 安装应用失败时卡在安装中无法删除应用重新安装](../kpanda/intro/faq.md#cannot-remove-app)
- [工作负载 -> 删除节点亲和性等调度策略后，调度异常](../kpanda/intro/faq.md#scheduling-exception)
- 应用备份：
    - [Kcoral 应用备份检测工作集群 Velero 状态的逻辑是什么](../kpanda/intro/faq.md#kcoral-logic-for-velero)
    - [在跨集群备份还原时，Kcoral 如何获取可用集群](../kpanda/intro/faq.md#kcoral-get-cluster)
    - [Kcoral 备份了相同标签的 Pod 和 Deployment，但还原备份后出现 2 个 Pod](../kpanda/intro/faq.md#2pod-with-same-label)
- [卸载 VPA、HPA、CronHPA 之后，为什么对应弹性伸缩记录依然存在](../kpanda/intro/faq.md#autoscaling-log)
- [为什么低版本集群的控制台打开异常](../kpanda/intro/faq.md#console-error)
- 创建和接入集群：
    - [如何重置创建的集群](#reset-cluster)
    - [接入集群安装插件失败](#failed-plugin)
    - [创建集群时在高级设置中启用 **为新建集群内核调优** ，集群创建为什么会失败](../kpanda/intro/faq.md#conntrack)
    - [集群解除接入后，`kpanda-system` 命名空间一直处于 Terminating 状态](../kpanda/intro/faq.md#ns-terminating)

## 多云编排

- [多云编排的内核是 Karmada，目前支持的 Karmada 版本是多少？能否指定版本？是否可以升级？](../kairship/intro/faq.md#no1)
- [多云编排时单集群应用如何无缝迁移到多云编排？](../kairship/intro/faq.md#no2)
- [多云编排是否支持跨集群的应用日志收集？](../kairship/intro/faq.md#no3)
- [多云编排分发到多个集群的工作负载，是否可以在一个视图呈现监控信息？](../kairship/intro/faq.md#no4)
- [多云编排工作负载是否可以跨集群通信？](../kairship/intro/faq.md#no5)
- [多云编排 Service 能否实现跨集群服务发现？](../kairship/intro/faq.md#no6)
- [多云编排是否有生产级别支持？](../kairship/intro/faq.md#no7)
- [多云编排如何做到故障转移？](../kairship/intro/faq.md#no8)
- [多集群的权限问题](../kairship/intro/faq.md#no9)
- [多云编排如何查询多集群的事件？](../kairship/intro/faq.md#no10)
- [通过多云编排创建一个多云应用之后，通过容器管理怎么能获取的相关资源信息？](../kairship/intro/faq.md#no11)
- [多云编排如何自定义 Karmada 镜像来源仓库地址？](../kairship/intro/faq.md#no12)
- [如何连接多云集群？](../kairship/intro/faq.md#no13)
- [是否可以仅删除多云实例，但是不删除多云编排的组件？](../kairship/intro/faq.md#no14)
- [多云实例内多个工作集群如何实现网络互通？](../kairship/intro/faq.md#no15)

## 云原生网络

- kube-proxy 问题
    - [IPVS 模式](../network/intro/issues.md#ipvs)
    - [iptables 模式](../network/intro/issues.md#iptables)
    - [externalIPs 在 `externalTrafficPolicy: Local` 下不工作](../network/intro/issues.md#externalips-externaltrafficpolicy-local)
    - [Service 的 endpoint 更新时新 endpoint 的规则等到很久以后才生效](../network/intro/issues.md#service-endpoint-endpoint)
    - [nftables 模式下 LoadBalancerSourceRanges 无法正常工作](../network/intro/issues.md#nftables-loadbalancersourceranges)
    - [iptables nft 和 legacy 模式选择问题](../network/intro/issues.md#iptables-nft-legacy)
- Calico 问题
    - [offload VXLAN 导致访问延迟](../network/intro/issues.md#offload-vxlan)
    - [VXLAN 父设备改了但路由没更新](../network/intro/issues.md#vxlan)
    - [集群 calico-kube-controllers 的缓存不同步，导致内存泄漏](../network/intro/issues.md#calico-kube-controllers)
    - [IPIP 模式下 Pod 跨节点网络不通](../network/intro/issues.md#ipip-pod)
    - [iptables nft 和 legacy 模式选择问题](../network/intro/issues.md#iptables-nft-legacy_1)
- Spiderpool v0.9 已知问题
    - [SpiderCoordinator 同步 status 时出错，但状态仍为 running](../network/intro/issues.md#spidercoordinator-status-running)
    - [`Values.multus.multusCNI.uninstall` 设置后不生效，导致 multus 资源没有正确删除](../network/intro/issues.md#valuesmultusmultuscniuninstall-multus)
    - [缺失 kubeadm-config 时无法从 kubeControllerManager Pod 获取 serviceCIDR](../network/intro/issues.md#kubeadm-config-kubecontrollermanager-pod-servicecidr)
    - [从 v0.7.0 升级到 v0.9.0 时 SpiderCoordinator CRD 新增的 TxQueueLen 属性会导致 panic](../network/intro/issues.md#v070-v090-spidercoordinator-crd-txqueuelen-panic)
    - [由于集群部署方式不同，导致 SpiderCoordinator 返回空的 serviceCIDR，从而无法创建 Pod](../network/intro/issues.md#spidercoordinator-servicecidr-pod)
- Spiderpool v0.8 已知问题
    - [ifacer 无法使用 vlan 0 创建 bond](../network/intro/issues.md#ifacer-vlan-0-bond)
    - [禁用 multus 功能，仍创建了 multus CR 资源](../network/intro/issues.md#multus-multus-cr)
    - [SpiderCoordinator 无法检测 Pod 的 netns 中的网关连接](../network/intro/issues.md#spidercoordinator-pod-netns)
    - [当 kubevirt 固定 IP 功能关闭时 spiderpool-agent Pod crash](../network/intro/issues.md#kubevirt-ip-spiderpool-agent-pod-crash)
    - [SpiderIPPool 资源未继承 SpiderSubnet 的 gateway 和 route 属性](../network/intro/issues.md#spiderippool-spidersubnet-gateway-route)
- Spiderpool v0.7 已知问题
    - [StatefulSet 类型的 Pod 重启后获取 IP 分配时，提示 IP 冲突](../network/intro/issues.md#statefulset-pod-ip-ip)
    - [Spiderpool 无法识别某些第三方控制器，导致 StatefulSet 的 Pod 无法使用固定 IP](../network/intro/issues.md#spiderpool-statefulset-pod-ip)
    - [空的 `spidermultusconfig.spec`, 将导致 spiderpool-controller Pod crash](../network/intro/issues.md#spidermultusconfigspec-spiderpool-controller-pod-crash)
    - [Cilium 模式获取到错误的 overlayPodCIDR](../network/intro/issues.md#cilium-overlaypodcidr)
    - [Pod 与 IP 数 1:1 的场景，出现 IPAM 分配阻塞，导致一些 Pod 无法运行，对分配 IP 性能产生影响](../network/intro/issues.md#pod-ip-11-ipam-pod-ip)
    - [禁用 IP GC 功能，spiderpool-controller 组件将由于 readiness 健康检查失败而无法正确启动](../network/intro/issues.md#ip-gc-spiderpool-controller-readiness)
    - [`IPPool.Spec.MultusName` 指定 namespace/multusName 时 namespace 解析错误导致找不到关联的 multusName](../network/intro/issues.md#ippoolspecmultusname-namespacemultusname-namespace-multusname)

## 云原生存储

- [HwameiStor 调度器在 Kubernetes 平台中是如何工作的？](../storage/hwameistor/faqs.md#hwameistor-kubernetes)
- [HwameiStor 如何应对应用多副本工作负载的调度？与传统通用型共享存储有什么不同？](../storage/hwameistor/faqs.md#hwameistor_1)
- [如何运维一个 Kubernetes 节点上的数据卷?](../storage/hwameistor/faqs.md#kubernetes)
- [LocalStorageNode 查看出现报错如何处理？](../storage/hwameistor/faqs.md#localstoragenode)
- [使用 hwameistor-operator 安装后为什么没有自动创建 StorageClass](../storage/hwameistor/faqs.md#hwameistor-operator-storageclass)

## 虚拟机

- [虚拟机页面 API 报错](../virtnest/faq/index.md)
- [虚拟机创建成功但无法使用](../virtnest/faq/cannot-use.md)
- [Windows 虚拟机无法识别新增磁盘](../virtnest/faq/recog-disk.md)

## 可观测性

- [链路数据中的时钟偏移](../insight/faq/traceclockskew.md)
- [日志采集排障指南](../insight/best-practice/debug-log.md)
- [链路采集排障指南](../insight/best-practice/debug-trace.md)
- [使用 Insight 定位应用异常](../insight/best-practice/find_root_cause.md)
- [ElasticSearch 数据塞满如何操作？](../insight/faq/expand-once-es-full.md)
- [如何配置容器日志黑名单](../insight/faq/ignore-pod-log-collect.md)

## 微服务引擎

- [skoala-init 的 x-kubernets-validations 报错问题](../skoala/troubleshoot/auth-server.md)
- [Nacos 版本降级问题](../skoala/troubleshoot/nacos.md)

## 服务网格

- [创建网格时找不到所属集群](../mspider/troubleshoot/cannot-find-cluster.md)
- [创建网格时一直处于“创建中”，最终创建失败](../mspider/troubleshoot/always-in-creating.md)
- [创建的网格异常，但无法删除网格](../mspider/troubleshoot/failed-to-delete.md)
- [托管网格纳管集群失败](../mspider/troubleshoot/failed-to-add-cluster.md)
- [托管网格纳管集群时 istio-ingressgateway 异常](../mspider/troubleshoot/hosted-mesh-errors.md)
- [网格空间无法正常解绑](../mspider/troubleshoot/mesh-space-cannot-unbind.md)
- [DCE 4.0 接入问题追踪](../mspider/troubleshoot/dce4.0-issues.md)
- [命名空间边车配置与工作负载边车冲突](../mspider/troubleshoot/sidecar.md)
- [托管网格多云互联异常](../mspider/troubleshoot/cluster-interconnect.md)
- [边车占用大量内存](../mspider/troubleshoot/sidecar-memory-err.md)
- [创建网格时，集群列表存在未知集群](../mspider/troubleshoot/cluster-already-exist.md)
- [托管网格 APIServer 证书过期处理办法](../mspider/troubleshoot/hosted-apiserver-cert-expiration.md)
- [服务网格中常见的 503 报错](../mspider/troubleshoot/503-issue.md)
- [如何使集群中监听 localhost 的应用被其它 Pod 访问](../mspider/troubleshoot/localhost-by-pod.md)

## 中间件

- MySQL 排障
    - [MySQL 健康检查](../middleware/mysql/faq/quick-check.md)
    - [MySQL Pod 问题](../middleware/mysql/faq/faq-pod.md)
    - [MySQL Operator 问题](../middleware/mysql/faq/faq-operator.md)
    - [MySQL 主备关系问题](../middleware/mysql/faq/faq-master-slave.md)
    - [MySQL MGR 参数配置问题](../middleware/mysql/faq/faq-mgr-parameter.md)
    - [MySQL MGR 排障手册](../middleware/mysql/faq/mgr-troubleshooting.md)
    - [MySQL 主从模式应对网络闪断](../middleware/mysql/faq/faq-mtsql-net.md)
    - [CR 创建数据库失败报错](../middleware/mysql/faq/faq-others.md#cr)
    - [出现提示 `The MySQL server is running with the read-only option so it cannot execute this statement`](../middleware/mysql/faq/faq-others.md#the-mysql-server-is-running-with-the-read-only-option-so-it-cannot-execute-this-statement)
    - [Operator 或者相关 MySQL 资源中出现错误码 1045](../middleware/mysql/faq/faq-others.md#operator-mysql-1045)
- Elasticsearch 排障
    - [Elasticsearch PVC 磁盘容量满](../middleware/elasticsearch/faq/common-question-es.md#elasticsearch-pvc)
    - [Elasticsearch 业务索引别名被占用](../middleware/elasticsearch/faq/common-question-es.md#elasticsearch_1)
    - [报错 Error setting GoMAXPROCS for operator](../middleware/elasticsearch/faq/common-question-es.md#error-setting-gomaxprocs-for-operator)
    - [报错 Terminating due to java.lang.OutOfMemoryError: Java heap space](../middleware/elasticsearch/faq/common-question-es.md#terminating-due-to-javalangoutofmemoryerror-java-heap-space)
    - [OCP 环境安装 Elasticsearch 时报错 Operation not permitted](../middleware/elasticsearch/faq/common-question-es.md#ocp-elasticsearch-operation-not-permitted)
    - [某个节点磁盘读吞吐异常、CPU workload 很高](../middleware/elasticsearch/faq/common-question-es.md#cpu-workload)
    - [数据写入 Elasticsearch 时报错 status:429](../middleware/elasticsearch/faq/common-question-es.md#elasticsearch-status429)

## AI Lab

- [AI Lab 集群下拉列表中找不到集群](../baize/troubleshoot/cluster-not-found.md)
- [AI Lab Notebook 不受队列配额控制](../baize/troubleshoot/notebook-not-controlled-by-quotas.md)
- [AI Lab 队列初始化失败](../baize/troubleshoot/local-queue-initialization-failed.md)

## 全局管理

- [重启集群（虚拟机）istio-ingressgateway 无法启动？](../ghippo/troubleshooting/ghippo01.md)
- [登录无限循环，报错 401 或 403](../ghippo/troubleshooting/ghippo02.md)
- [Keycloak 无法启动](../ghippo/troubleshooting/ghippo03.md)
- [单独升级全局管理时升级失败](../ghippo/troubleshooting/ghippo04.md)

## 权限问题

- [容器管理权限说明](../ghippo/permissions//kpanda.md)
- [微服务引擎权限说明](../ghippo/permissions/skoala.md)
- [应用工作台权限说明](../ghippo/permissions/amamba.md)
- [服务网格权限说明](../ghippo/permissions/mspider.md)
- [中间件权限说明](../ghippo/permissions/mcamel.md)
- [AI Lab 权限说明](../ghippo/permissions/baize.md)
