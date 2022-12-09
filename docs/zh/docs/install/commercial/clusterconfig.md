---
hide:
  - toc
---

# 编辑 clusterConfig.yaml

此 YAML 文件包含了集群的各项配置字段，安装之前必须先配置此文件。
该文件将定义部署的负载均衡类型、部署模式、集群节点信息等关键参数。默认位于 `offline/sample/` 目录。

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
| compactClusterMode           | 简约模式：如果开启后会把[全局服务集群](../../kpanda/07UserGuide/Clusters/ClusterRole.md)建立在管理集群上，系统也会忽略 `globalXXXNode` 字段的设置，只需要设置 `mgmtXXXNode` 字段的参数信息，此模式也适用于一体机。简约模式是默认选项。<br />如果设置为 `false`，则为经典模式。 | true                                                   |
| loadBalancer                 | 所使用的 LoadBalancer 的模式，物理环境用 metallb，POC 用 NodePort，公有云和 SDN CNI 环境用 cloudLB | NodePort(default), metallb, cloudLB (Cloud Controller) |
| xxVIP                        | 不同作用的 VIP（专供 Metallb），注意格式为 10.6.229.58/32 或 1.2.3.4-1.2.3.5 | -                                                     |
| mgmtClusterName              | 在 KuBean 中的管理集群的名称                                   | -                                                     |
| globalClusterName            | 在 KuBean 中的全局服务集群的名称                               | -                                                     |
| istioGatewayVip              | 如果负载均衡模式是 metallb，则需要指定一个 VIP，用作 DCE 的 UI 界面和 OpenAPI 访问入口 | -                                                     |
| registryVip                  | 如果负载均衡模式是 metallb，则需要指定一个 VIP，用作 Global 集群的镜像仓库的访问入口 | -                                                     |
| insightVip                   | 如果负载均衡模式是 metallb，则需要指定一个 VIP，用作 GLobal 集群的 insight 数据收集入口使用，子集群的 insight-agent 可上报数据到这个 VIP | -                                                     |
| persistentRegistryDomainName | 如果是离线安装，需要指定该字段，指定临时和未来的仓库域名   | -                                                     |
| imageConfig.imageRepository  | 如果是离线安装，kuBean 安装集群时的本地镜像仓库来源          | -                                                     |
| imageConfig.binaryRepository | 如果是离线安装，kuBean 安装集群时的本地二进制仓库来源        | https://xxx.yy.zz                           |
| repoConfig                   | RPM 或者 DEB 安装的源头。在离线模式下，安装器启动的是 MinIO | -                                                     |
| k8sVersion                   | kuBean 安装集群的 K8s 版本，必须与 KuBean 以及离线包相匹配      | -                                                     |
| mgmtMasterNodes              | 管理集群：Master 节点列表，包括 nodeName/ip/ansibleUser/ansiblePass 几个关键字段 | -                                                     |
| mgmtWorkerNodes              | 管理集群：Worker 节点列表，包括 nodeName/ip/ansibleUser/ansiblePass 几个关键字段 | -                                                     |
| globalMasterNodes            | 全局服务集群：Master 节点列表，包括 nodeName/ip/ansibleUser/ansiblePass 几个关键字段 | -                                                     |
| globalWorkerNodes            | 全局服务集群：Worker 节点列表，包括 nodeName/ip/ansibleUser/ansiblePass 几个关键字段 | -                                                     |
| ntpServer                    | 可用的 NTP 服务器，用作新节点同步时间                        | -                                                     |
| network.cni                  | 选择一个 CNI，例如 calico、cilium                                | calico                                                 |
| network.clusterCIDR          | Cluster CIDR                                                 | -                                                     |
| network.serviceCIDR          | Service CIDR                                                 | -                                                     |
| auditConfig                  | K8s api-server 的审计日志配置                                | 默认关闭                                               |
