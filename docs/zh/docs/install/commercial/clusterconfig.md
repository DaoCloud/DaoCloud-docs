---
hide:
  - toc
---

# 编辑 clusterConfig.yaml

此 YAML 文件包含了集群的各项配置字段，安装之前必须先配置此文件。
该文件将定义部署的负载均衡类型、部署模式、集群节点信息等关键参数。默认位于 `offline/sample/` 目录。

## ClusterConfig 示例

以下是一个 ClusterConfig 文件示例（假设火种节点 IP 是 10.6.127.220）。

```yaml title="clusterConfig.yaml"
apiVersion: provision.daocloud.io/v1alpha2
kind: ClusterConfig
metadata:
  creationTimestamp: null
spec:
  clusterName: my-cluster
  loadBalancer:
    type: metallb # (1)
    istioGatewayVip: 10.6.127.253/32 # (2)
    insightVip: 10.6.127.254/32      # (3)
  # privateKeyPath: /root/.ssh/id_rsa_sample  # (4)
  masterNodes:
    - nodeName: "g-master1" # (5)
      ip: 10.6.127.230
      ansibleUser: "root" # (6)
      ansiblePass: "dangerous"  # (7)
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
      # nodeTaints: # (8)
      #  - "node.daocloud.io/es-only=true:NoSchedule"
  ntpServer: # (9)
    - "172.30.120.197 iburst"
    - 0.pool.ntp.org
    - ntp1.aliyun.com
    - ntp.ntsc.ac.cn
  registry:
    type: built-in # (10)
    builtinRegistryDomainName: built-in-registry.daocloud.io # (11)
  imageConfig: # (12)
    imageRepository: built-in-registry.daocloud.io # (13)
    binaryRepository: http://10.6.127.220:9000/kubean # (14)
  repoConfig: # (15)
    repoType: centos
    isoPath: "/root/CentOS-7-x86_64-DVD-2207-02.iso" # (16)
    dockerRepo: "http://10.6.127.220:9000/kubean/centos/$releasever/os/$basearch"
    extraRepos:
      - http://10.6.127.220:9000/kubean/centos-iso/\$releasever/os/\$basearch
      - http://10.6.127.220:9000/kubean/centos/\$releasever/os/\$basearch
  k8sVersion: v1.24.7 # (17)
  auditConfig: # (18)
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
    # criVersion: 1.6.8 # (19)
  addons:
    ingress:
      version: 1.2.3
    dns:
      type: CoreDNS
      version: v1.8.4
```

1. 有 3 个可选项：`NodePort` (default)、`metallb`、`cloudLB` (Cloud Controller)
2. 当 loadBalancer.type 是 `metallb` 时必填，为 DCE 提供 UI 和 OpenAPI 访问权限
3. 别丢弃/32, 当 loadBalancer.type 是 metallb 时必填，用作 GLobal 集群的 Insight 数据采集入口，子集群的 insight-agent 可以向这个 VIP 报告数据
4. 如果用免密方式 SSH 接入节点，需指定密钥文件地址
5. nodeName 将覆盖 hostName，应符合 RFC1123 标准
6. SSH 用户名
7. SSH 密码
8. 在 7 节点及以上模式，为了保证集群稳定，ES 将使用专享主机。则至少 3 个 worker 节点需要有污点
9. 时间同步服务器
10. 有几个可选项：built-in、external、online
11. 只需替换所有 /etc/hosts。如果空白，所有镜像将使用火种节点 IP 作为镜像仓库
12. kubean 镜像仓库和 MinIO 仓库的 配置
13. kubean 镜像仓库
14. kubean 二进制来源的 minio 仓库
15. kubean rpm/deb 源配置, `centos` 表示 CentOS、RedHat、AlmaLinux 或 Fedora；`debian` 表示 Debian；`ubuntu` 表示 Ubuntu
16. 在离线模式下，isoPath 不能为空
17. k8sVersion 字段仅适用于在线模式，离线模式时无需设置
18. 是否开启 k8s apisever 的审计日志及相关配置
19. criVersion 字段仅适用于在线模式，离线模式时无需设置

## 关键字段

该 YAML 文件中的关键字段说明，请参阅下表。

| 字段                     | 说明                                  | 默认值               |
| ----------------------- | ------------------------------------ | ------------------- |
| clusterName                        | 在 KuBean Cluster 里的 Global 集群命名                                                                    | - |
| loadBalancer.type                  | 所使用的 LoadBalancer 的模式，物理环境用 metallb，POC 用 NodePort，公有云和 SDN CNI 环境用 cloudLB   | NodePort (default)、metallb、cloudLB (Cloud Controller) |
| loadBalancer.istioGatewayVip       | 如果负载均衡模式是 metallb，则需要指定一个 VIP，供给 DCE 的 UI 界面和 OpenAPI 访问入口                   | -     |
| loadBalancer.insightVip            | 如果负载均衡模式是 metallb，则需要指定一个 VIP，供给 GLobal 集群的 insight 数据收集入口使用，子集群的 insight-agent 可上报数据到这个 VIP | -     |
| privateKeyPath                     | kuBean 部署集群的 SSH 私钥文件路径，参考全模式主机清单 SSH 连接设置                            | -     |
| masterNodes                        | Global 集群：Master 节点列表，包括 nodeName/ip/ansibleUser/ansiblePass 几个关键字段                        | -     |
| workerNodes                        | Global 集群：Worker 节点列表，包括 nodeName/ip/ansibleUser/ansiblePass 几个关键字段                           | -     |
| registry.type                      | k8s 组件和 DCE 组件的镜像拉取仓库的类型，有 online (在线环境)、built-in (使用火种节点内置的仓库)、external (使用已有的外置仓库)     | online     |
| registry.builtinRegistryDomainName | 如果使用 built-in (使用火种节点内置的仓库)，如果需要自动化植入仓库域名到各个节点的 /etc/hosts 和 CoreDNS 的 hosts，可指定域名            | -     |
| registry.externalRegistry          | 指定 external 仓库的 IP 或者域名(使用已有的外置仓库)，如果使用 Harbor，需要提前创建相应 Project                                          | -     |
| registry.externalRegistryUsername  | 外置仓库的用户名，用于推送镜像                                             | -     |
| registry.externalRegistryPassword  | 外置仓库的密码，用于推送镜像                                                    | -     |
| imageConfig.imageRepository        | 如果是离线安装，kuBean 安装集群时的本地镜像仓库来源                                | -     |
| imageConfig.binaryRepository       | 如果是离线安装，kuBean 安装集群时的本地二进制仓库来源                                  | https://files.m.daocloud.io                             |
| repoConfig                         | RPM 或者 DEB 安装的源头，如果离线模式下,是安装器启动的 MinIO                             | -     |
| repoConfig.isoPath                 | 操作系统 ISO 文件的路径 ，离线模式下不能为空                                          | -     |
| k8sVersion                         | kuBean 安装集群的 K8s 版本必须跟 KuBean 和离线包相匹配                           | -     |
| ntpServer                          | 可用的 NTP 服务器，供给新节点同步时间                                           | -     |
| network.cni                        | CNI 选择，比如 Calico、Cilium                                                | calico                                                  |
| network.clusterCIDR                | Cluster CIDR                                                            | -     |
| network.serviceCIDR                | Service CIDR                                                              | -     |
| auditConfig                        | k8s api-server 的审计日志配置                                                    | 默认关闭                       |
