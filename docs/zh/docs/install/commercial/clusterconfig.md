---
hide:
  - toc
---

# 集群配置（ClusterConfig）文件说明

在[离线安装 DCE 5.0 商业版](start-install.md)的过程中，执行安装命令时需要指定集群配置文件，需要根据实际部署场景来配置该文件。
该文件可以定义部署的负载均衡类型、部署模式、集群节点信息等关键参数。

## ClusterConfig 示例

以下是一个 ClusterConfig 文件示例。

```yaml
apiVersion: provision.daocloud.io/v1alpha1
kind: ClusterConfig
metadata:
  creationTimestamp: null
spec:
  loadBalancer: NodePort  # NodePort(default), metallb, cloudLB (Cloud Controller)
  istioGatewayVip: 10.6.127.254/32 # 当 loadBalancer 是 metallb 时必填
                                   # 为 DCE 提供 UI 和 OpenAPI 访问权限
  registryVip: 10.6.127.253/32     # 当 loadBalancer 是 metallb 时必填
                                   # Global 集群的镜像仓库访问入口
  insightVip: 10.6.127.252/32 # 当 loadBalancer 是 metallb 时必填
                              # 用作 GLobal 集群的 Insight 数据采集入口
                              # 子集群的 insight-agent 可以向这个 VIP 报告数据
  compactClusterMode: false
  globalClusterName: my-global-cluster
  mgmtClusterName: my-mgmt-cluster
  mgmtMasterNodes:
    - nodeName: "rm-master1" # nodeName 将覆盖 hostName，应符合 RFC1123 标准
      ip: 10.6.127.232
      ansibleUser: "root"   # 用户名
      ansiblePass: "123456" # 密码
  mgmtWorkerNodes:
    - nodeName: "rm-worker1" # nodeName 将覆盖 hostName，应符合 RFC1123 标准
      ip: 10.6.127.230
      ansibleUser: "root"   # 用户名
      ansiblePass: "123456" # 密码
  globalMasterNodes:        # 简约模式时此字段不起作用
    - nodeName: "rg-master1"
      ip: 10.6.127.231
      ansibleUser: "root"
      ansiblePass: "123456"
  globalWorkerNodes:        # 简约模式时此字段不起作用
    - nodeName: "rg-worker1"
      ip: 10.6.127.234
      ansibleUser: "root"
      ansiblePass: "123456"
  ntpServer:                # 时间同步服务器
    - "172.30.120.197 iburst"
    - 0.pool.ntp.org
    - ntp1.aliyun.com
    - ntp.ntsc.ac.cn
  persistentRegistryDomainName: temp-registry.daocloud.io # 本地镜像仓库
  imageConfig: # kubean 镜像配置
    imageRepository: temp-registry.daocloud.io
    binaryRepository: http://temp-registry.daocloud.io:9000/kubean
  repoConfig: # kubean rpm/deb 源配置
    # `centos` 表示 CentOS, RedHat, AlmaLinux 或 Fedora
    # `debian` 表示 Debian
    # `ubuntu` 表示 Ubuntu
    repoType: centos
    dockerRepo: "http://temp-registry.daocloud.io:9000/kubean/centos/$releasever/os/$basearch"
    extraRepos:
    - http://temp-registry.daocloud.io:9000/kubean/centos-iso/\$releasever/os/\$basearch
    - http://temp-registry.daocloud.io:9000/kubean/centos/\$releasever/os/\$basearch
    # k8sVersion 字段仅适用于在线模式，离线模式时无需设置
    # k8sVersion: v1.24.6
  auditConfig:
    logPath: /var/log/audit/kube-apiserver-audit.log
    logHostPath: /var/log/kubernetes/audit
    # policyFile: /etc/kubernetes/audit-policy/apiserver-audit-policy.yaml
    # logMaxAge: 30
    # logMaxBackups: 10
    # logMaxSize: 100
    # policyCustomRules: >
    #   - level: None
    #     users: []
    #     verbs: []
    #     resources: []
  network:
    cni: calico
    clusterCIDR: 100.96.0.0/11
    serviceCIDR: 100.64.0.0/13
  cri:
    criProvider: containerd
    # criVersion 字段仅适用于在线模式，离线模式时无需设置
    # criVersion: 1.6.8
  addons:
    ingress:
      version: 1.2.3
    dns:
      type: CoreDNS
      version: v1.8.4
```

## 关键字段

该 YAML 文件中的关键字段说明，请参阅下表。

| 字段                         | 说明                                                         | 默认值                                                 |
| ---------------------------- | ------------------------------------------------------------ | ------------------------------------------------------ |
| compactClusterMode           | 简约模式：如果开启后会把全局服务集群建立在管理集群上，系统也会忽略 globalXXXNode 的设置，只需要设置 mgmtXXXNode 的参数信息，一体机模式也适用。默认使用简约模式。<br />如果设置为 `false` ，部署模式则为经典模式。 | true                                                   |
| loadBalancer                 | 所使用的 LoadBalancer 的模式，物理环境用 metallb，POC 用 NodePort，公有云和 SDN CNI 环境用 cloudLB | NodePort(default), metallb, cloudLB (Cloud Controller) |
| xxVIP                        | 不同作用的 VIP（专供 Metallb），注意格式如 10.6.229.58/32， 或者 1.2.3.4-1.2.3.5 | NA                                                     |
| mgmtClusterName              | 在 KuBean 里的管理集群命名                                   | NA                                                     |
| globalClusterName            | 在 KuBean 里的 Global 集群命名                               | NA                                                     |
| istioGatewayVip              | 如果负载均衡模式是 metallb，则需要指定一个 VIP，供给 DCE 的 UI 界面和 OpenAPI 访问入口 | NA                                                     |
| registryVip                  | 如果负载均衡模式是 metallb，则需要指定一个 VIP，供给 Global 集群的镜像仓库的访问入口 | NA                                                     |
| insightVip                   | 如果负载均衡模式是 metallb，则需要指定一个 VIP，供给 GLobal 集群的 insight 数据收集入口使用，子集群的 insight-agent 可上报数据到这个 VIP | NA                                                     |
| persistentRegistryDomainName | 如果是离线安装，需要指定该字段，指定临时和未来的仓库的域名   | NA                                                     |
| imageConfig.imageRepository  | 如果是离线安装，kuBean 安装集群时的本地镜像仓库来源          | NA                                                     |
| imageConfig.binaryRepository | 如果是离线安装，kuBean 安装集群时的本地二进制仓库来源        | https://files.m.daocloud.io                            |
| repoConfig                   | RPM 或者 DEB 安装的源头，如果离线模式下,是安装器启动的 MinIO | NA                                                     |
| k8sVersion                   | kuBean 安装集群的 k8s 版本-必须跟 KuBean 和离线包相匹配      | NA                                                     |
| mgmtMasterNodes              | 管理集群：Master 节点列表，包括 nodeName/ip/ansibleUser/ansiblePass 几个关键字段 | NA                                                     |
| mgmtWorkerNodes              | 管理集群：Worker 节点列表，包括 nodeName/ip/ansibleUser/ansiblePass 几个关键字段 | NA                                                     |
| globalMasterNodes            | 全局集群：Master 节点列表，包括 nodeName/ip/ansibleUser/ansiblePass 几个关键字段 | NA                                                     |
| globalWorkerNodes            | 全局集群：Worker 节点列表，包括 nodeName/ip/ansibleUser/ansiblePass 几个关键字段 | NA                                                     |
| ntpServer                    | 可用的 NTP 服务器，供给新节点同步时间                        | NA                                                     |
| network.cni                  | CNI 选择，比如 calico、cilium                                | calico                                                 |
| network.clusterCIDR          | Cluster CIDR                                                 | NA                                                     |
| network.serviceCIDR          | Service CIDR                                                 | NA                                                     |
| auditConfig                  | k8s api-server 的审计日志配置                                | 默认关闭                                               |
