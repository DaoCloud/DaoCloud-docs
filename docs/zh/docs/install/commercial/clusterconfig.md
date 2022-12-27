---
hide:
  - toc
---

# 编辑 clusterConfig.yaml

此 YAML 文件包含了集群的各项配置字段，安装之前必须先配置此文件。
该文件将定义部署的负载均衡类型、部署模式、集群节点信息等关键参数。默认位于 `offline/sample/` 目录。

## ClusterConfig 示例

以下是一个 ClusterConfig 文件示例。（假设火种节点 IP 是10.6.127.220）

```yaml

apiVersion: provision.daocloud.io/v1alpha2
kind: ClusterConfig
metadata:
  creationTimestamp: null
spec:
  clusterName: my-cluster
  loadBalancer:
    type: metallb # NodePort(default), metallb, cloudLB (Cloud Controller)
    istioGatewayVip: 10.6.127.253/32 ## 当 loadBalancer.type 是 metallb 时必填.
                                     ## 为 DCE 提供 UI 和 OpenAPI 访问权限
    insightVip: 10.6.127.254/32      ## 别丢弃/32
                                     ## 当 loadBalancer 是 metallb 时必填
                                     ## 用作 GLobal 集群的 Insight 数据采集入口
                                     ## 子集群的 insight-agent 可以向这个 VIP 报告数据
  # privateKeyPath: /root/.ssh/id_rsa_sample  # 如果用免密方式 SSH 接入节点，需指定密钥文件地址
  masterNodes:
    - nodeName: "g-master1" ## nodeName 将覆盖 hostName，应符合 RFC1123 标准
      ip: 10.6.127.230
      ansibleUser: "root"       # SSH 用户名
      ansiblePass: "dangerous"  # SSH 密码
    - nodeName: "g-master2"
      ip: 10.6.127.231
      ansibleUser: "root"
      ansiblePass: "dangerous"
    - nodeName: "g-master3"
      ip: 10.6.127.232
      ansibleUser: "root"
      ansiblePass: "dangerous"
  workerNodes:
    - nodeName: "g-worker1"
      ip: 10.6.127.233
      ansibleUser: "root"
      ansiblePass: "dangerous"
    - nodeName: "g-worker2"
      ip: 10.6.127.234
      ansibleUser: "root"
      ansiblePass: "dangerous"
      #nodeTaints:                       # 在 7 节点及以上模式，为了保证集群稳定，ES 将使用专享主机。则至少 3 个 worker 节点需要有污点
      #  - "node.daocloud.io/es-only=true:NoSchedule"
  ntpServer:                        # 时间同步服务器
    - "172.30.120.197 iburst"
    - 0.pool.ntp.org
    - ntp1.aliyun.com
    - ntp.ntsc.ac.cn
  registry:
    type: built-in # options: built-in, external, online
    builtinRegistryDomainName: built-in-registry.daocloud.io # just to replace all /etc/hosts. if blank, all images use bootstrap node IP as registry
  imageConfig:      # kubean 镜像仓库和 MinIO 仓库的 配置
    imageRepository: built-in-registry.daocloud.io          # kubean 镜像仓库
    binaryRepository: http://10.6.127.220:9000/kubean       # kubean 二进制来源的 minio 仓库
  repoConfig: # kubean rpm/deb 源配置
    # `centos` 表示 CentOS, RedHat, AlmaLinux 或 Fedora
    # `debian` 表示 Debian
    # `ubuntu` 表示 Ubuntu
    repoType: centos
    # 在离线模式下，isoPath 不能为空
    isoPath: "/root/CentOS-7-x86_64-DVD-2207-02.iso"
    dockerRepo: "http://10.6.127.220:9000/kubean/centos/$releasever/os/$basearch"
    extraRepos:
      - http://10.6.127.220:9000/kubean/centos-iso/\$releasever/os/\$basearch
      - http://10.6.127.220:9000/kubean/centos/\$releasever/os/\$basearch
  # k8sVersion 字段仅适用于在线模式，离线模式时无需设置
  k8sVersion: v1.24.7
  auditConfig: # 是否开启 k8s apisever 的审计日志及相关配置
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
| clusterName | 在 KuBean Cluster 里的 Global 集群命名 | NA |
| loadBalancer.type | 所使用的LoadBalancer的模式，物理环境用metallb，POC用NodePort，公有云和SDN CNI环境用cloudLB | NodePort(default), metallb, cloudLB (Cloud Controller) |
| loadBalancer.istioGatewayVip |  如果负载均衡模式是metallb，则需要指定一个VIP，供给DCE的UI界面和OpenAPI访问入口 | NA |
| loadBalancer.insightVip |  如果负载均衡模式是metallb，则需要指定一个VIP，供给 GLobal 集群的insight数据收集入口使用，子集群的insight-agent可上报数据到这个VIP | NA |
| registry.type | k8s 组件和 DCE 组件的镜像拉取仓库的类型，有online(在线环境), built-in(使用火种节点内置的仓库), external(使用已有的外置仓库)| online |
| registry.builtinRegistryDomainName| 如果使用 built-in(使用火种节点内置的仓库), 如果需要自动化植入仓库域名到各个节点的/etc/hosts和CoreDNS的hosts，可指定域名 | NA |
| registry.externalRegistry | 指定external仓库的IP或者域名(使用已有的外置仓库), 如果使用Harbor，需要提前创建相应Project | NA |
| registry.externalRegistryUsername | 外置仓库的用户名，用于推送镜像| NA |
| registry.externalRegistryPassword | 外置仓库的密码，用于推送镜像| NA |
| imageConfig.imageRepository | 如果是离线安装，kuBean安装集群时的本地镜像仓库来源 | NA |
| imageConfig.binaryRepository | 如果是离线安装，kuBean安装集群时的本地二进制仓库来源 | https://files.m.daocloud.io |
| repoConfig | RPM或者DEB安装的源头，如果离线模式下,是安装器启动的MinIO| NA|
| repoConfig.isoPath | 操作系统 ISO 文件的路径 ，离线模式下不能为空 | NA|
| k8sVersion | kuBean安装集群的k8s版本-必须跟KuBean和离线包相匹配 | NA |
| privateKeyPath | kuBean部署集群的SSH私钥文件路径, 参考: [全模式主机清单SSH连接设置](./inventory_ssh_connect.md) | NA |
| masterNodes | Global 集群：Master节点列表，包括nodeName/ip/ansibleUser/ansiblePass几个关键子段 | NA |
| workerNodes | Global 集群：Worker节点列表，包括nodeName/ip/ansibleUser/ansiblePass几个关键子段 | NA |
| ntpServer | 可用的NTP服务器，供给新节点同步时间| NA|
| network.cni | CNI选择，比如calico, cilium |calico |
| network.clusterCIDR| Cluster CIDR| NA|
| network.serviceCIDR| Service CIDR| NA|
| auditConfig| k8s api-server的审计日志配置| 默认关闭|


