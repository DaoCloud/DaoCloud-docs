# 集群配置（ClusterConfig）文件说明

[离线安装 DCE 5.0 商业版](start-install.md)时，在第三步执行安装命令时需要指定集群配置文件，需要根据实际部署场景来配置该文件。
其中集群配置文件可以定义部署的负载均衡类型、部署模式、集群节点信息等关键参数。以下描述了该文件的模式以及对关键字段进行了说明。

## 文件内容

```yaml
apiVersion: provision.daocloud.io/v1alpha1
kind: ClusterConfig
metadata:
    creationTimestamp: null
spec:
    loadBalancer: NodePort  # NodePort(default), metallb, cloudLB (Cloud Controller)
    istioGatewayVip: 10.6.127.254/32 # if loadBalancer is metallb，is requireded. Provides UI and OpenAPI access to DCE
    registryVip: 10.6.127.253/32 # if loadBalancer is metallb，is requireded. Access entry for the mirror repository of the Global cluster
    insightVip: 10.6.127.252/32 # if loadBalancer is metallb，is requireded. It is used for the insight data collection portal of the GLobal cluster, and the insight-agent of the sub-cluster can report data to this VIP
    compactClusterMode: false
    globalClusterName: my-global-cluster
    mgmtClusterName: my-mgmt-cluster
    mgmtMasterNodes:
        - nodeName: "rm-master1" # Node Name will override the hostName, should align with RFC1123 stsandard
        ip: 10.6.127.232
        ansibleUser: "root" # username
        ansiblePass: "123456" # password
    mgmtMasterNodes:
        - nodeName: "rm-master1" # Node Name will override the hostName, should align with RFC1123 stsandard
        ip: 10.6.127.230
        ansibleUser: "root" # username
        ansiblePass: "123456" # password
    globalMasterNodes:
        - nodeName: "rg-master1"
        ip: 10.6.127.231
        ansibleUser: "root"
        ansiblePass: "123456"
    globalWorkerNodes:
        - nodeName: "rg-worker1"
        ip: 10.6.127.234
        ansibleUser: "root"
        ansiblePass: "123456"
    ntpServer:
        - "172.30.120.197 iburst" # time synchronization server
        - 0.pool.ntp.org
        - ntp1.aliyun.com
        - ntp.ntsc.ac.cn
    persistentRegistryDomainName: temp-registry.daocloud.io # The local image registry which images come from.
    imageConfig: # the kubean image config as below
        imageRepository: temp-registry.daocloud.io
        binaryRepository: http://temp-registry.daocloud.io:9000/kubean
    repoConfig: # the kubean rpm/deb source configuration as below
        # `centos` using CentOS, RedHat, AlmaLinux or Fedora
        # `debian` using Debian
        # `ubuntu` using Ubuntu
        repoType: centos
        dockerRepo: "http://temp-registry.daocloud.io:9000/kubean/centos/$releasever/os/$basearch"
        extraRepos:
        - http://temp-registry.daocloud.io:9000/kubean/centos-iso/\$releasever/os/\$basearch
        - http://temp-registry.daocloud.io:9000/kubean/centos/\$releasever/os/\$basearch
    # k8sVersion only take effect in online mode, dont set it in offline mode
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
        # criVersion only take effect in online mode, dont set it in offline mode
        # criVersion: 1.6.8
    addons:
        ingress:
        version: 1.2.3
        dns:
        type: CoreDNS
        version: v1.8.4

```



## 关键字段说明

| 字段                         | 说明                                                         | 默认值                                                 |
| ---------------------------- | ------------------------------------------------------------ | ------------------------------------------------------ |
| compactClusterMode           | 简约模式：如果开启后会把全局服务集群建立在管理集群上，系统也会忽略 globalXXXNode 的设置，一体机模式也适用。默认使用简约模式。<br />如果设置为 `false` ，部署模式则为经典模式。 | true                                                   |
| loadBalancer                 | 所使用的LoadBalancer的模式，物理环境用metallb，POC用NodePort，公有云和SDN CNI环境用cloudLB | NodePort(default), metallb, cloudLB (Cloud Controller) |
| xxVIP                        | 不同作用的VIP（专供Metallb），注意格式如10.6.229.58/32， 或者1.2.3.4-1.2.3.5 | NA                                                     |
| mgmtClusterName              | 在 KuBean 里的管理集群命名                                   | NA                                                     |
| globalClusterName            | 在 KuBean 里的Global集群命名                                 | NA                                                     |
| istioGatewayVip              | 如果负载均衡模式是metallb，则需要指定一个VIP，供给DCE的UI界面和OpenAPI访问入口 | NA                                                     |
| registryVip                  | 如果负载均衡模式是metallb，则需要指定一个VIP，供给Global集群的镜像仓库的访问入口 | NA                                                     |
| insightVip                   | 如果负载均衡模式是metallb，则需要指定一个VIP，供给GLobal集群的insight数据收集入口使用，子集群的insight-agent可上报数据到这个VIP | NA                                                     |
| persistentRegistryDomainName | 如果是离线安装，需要指定该字段，指定临时和未来的仓库的域名   | NA                                                     |
| imageConfig.imageRepository  | 如果是离线安装，kuBean安装集群时的本地镜像仓库来源           | NA                                                     |
| imageConfig.binaryRepository | 如果是离线安装，kuBean安装集群时的本地二进制仓库来源         | https://files.m.daocloud.io                            |
| repoConfig                   | RPM或者DEB安装的源头，如果离线模式下,是安装器启动的MinIO     | NA                                                     |
| k8sVersion                   | kuBean安装集群的k8s版本-必须跟KuBean和离线包相匹配           | NA                                                     |
| mgmtMasterNodes              | 管理集群：Master节点列表，包括nodeName/ip/ansibleUser/ansiblePass几个关键子段 | NA                                                     |
| mgmtWorkerNodes              | 管理集群：Worker节点列表，包括nodeName/ip/ansibleUser/ansiblePass几个关键子段 | NA                                                     |
| globalMasterNodes            | 全局集群：Master节点列表，包括nodeName/ip/ansibleUser/ansiblePass几个关键子段 | NA                                                     |
| globalWorkerNodes            | 全局集群：Worker节点列表，包括nodeName/ip/ansibleUser/ansiblePass几个关键子段 | NA                                                     |
| ntpServer                    | 可用的NTP服务器，供给新节点同步时间                          | NA                                                     |
| network.cni                  | CNI选择，比如calico, cilium                                  | calico                                                 |
| network.clusterCIDR          | Cluster CIDR                                                 | NA                                                     |
| network.serviceCIDR          | Service CIDR                                                 | NA                                                     |
| auditConfig                  | k8s api-server的审计日志配置                                 | 默认关闭                                               |