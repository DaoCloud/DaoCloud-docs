# 集群配置文件 clusterConfig.yaml

此 YAML 文件包含了集群的各项配置字段，安装之前必须先配置此文件。
该文件将定义部署模式、集群节点信息等关键参数。默认位于 `offline/sample/` 目录。

## ClusterConfig 示例

以下是一个 ClusterConfig 文件示例。

```yaml title="clusterConfig.yaml"
apiVersion: provision.daocloud.io/v1alpha3
kind: ClusterConfig
metadata:
spec:
  clusterName: my-cluster
   
  # 火种节点的域名或IP，默认解析为火种节点默认网关所在网卡的IP；可手动填入IP或域名，若为域名，如果检测到无法解析，将自动建立此域名和火种节点默认IP的映射
  # bootstrapNode: auto

  # kind 火种集群的配置，以下为默认值
  # tinderKind:
  #  # kind 集群的容器名称
  #  instanceName: my-cluster-installer
  #  # kind 集群挂载的主机路径
  #  resourcesMountPath: /home/kind
  #  registryPort: 443
  #  minioServerPort: 9000
  #  minioConsolePort: 9001
  #  chartmuseumPort: 8081

  loadBalancer:
 
    # NodePort(default), metallb, cloudLB (Cloud Controller 暂不支持)
    type: metallb
    istioGatewayVip: xx.xx.xx.xx/32 # 当 loadBalancer.type 是 metallb 时必填，为 DCE 提供 UI 和 OpenAPI 访问权限
    insightVip: xx.xx.xx.xx/32 # 别丢弃 /32，当 loadBalancer.type 是 metallb 时必填，用作 global 集群的 Insight 数据采集入口，子集群的 insight-agent 可以向这个 VIP 报告数据
    SourceIP: auto # 默认值auto表示开启审计日志获取源IP功能，设置为false则关闭审计日志获取源IP功能
 
  # 指定 ssh 私钥，定义后无需再定义节点的 ansibleUser、ansiblePass
  # privateKeyPath: /root/.ssh/id_rsa_sample
 
  masterNodes:
    - nodeName: "g-master1" # nodeName 将覆盖 hostName，应符合 RFC1123 标准
      ip: xx.xx.xx.xx
      ansibleUser: "root"
      ansiblePass: "dangerous"
      #ansibleSSHPort: "22"
      #ansibleExtraArgs: ""  # "ansible_shell_executable='/bin/sh'  ansible_python_interpreter='/usr/local/bin/python'" , format: "k='v'  k1='v1'  k2='v2' "
    - nodeName: "g-master2"
      ip: xx.xx.xx.xx
      ansibleUser: "root"
      ansiblePass: "dangerous"
      #ansibleSSHPort: "22"
      #ansibleExtraArgs: ""
    - nodeName: "g-master3"
      ip: xx.xx.xx.xx
      ansibleUser: "root"
      ansiblePass: "dangerous"
      #ansibleSSHPort: "22"
      #ansibleExtraArgs: ""
  workerNodes:
    - nodeName: "g-worker1"
      ip: xx.xx.xx.xx
      ansibleUser: "root"
      ansiblePass: "dangerous"
      #ansibleSSHPort: "22"
      #ansibleExtraArgs: ""
      nodeTaints:                       # 对于 7 节点模式：至少 3 个 worker 节点应打污点（仅 ES 节点），如果使用外接 ES 则不需要添加该污点
       - "node.daocloud.io/es-only=true:NoSchedule"
      # nodeLabels:
      #   daocloud.io/hostname: g-worker1
    - nodeName: "g-worker2"
      ip: xx.xx.xx.xx
      ansibleUser: "root"
      ansiblePass: "dangerous"
      #ansibleSSHPort: "22"
      #ansibleExtraArgs: ""
      nodeTaints:
       - "node.daocloud.io/es-only=true:NoSchedule"
      # nodeLabels:
      #   daocloud.io/hostname: g-worker2
    - nodeName: "g-worker3"
      ip: xx.xx.xx.xx
      ansibleUser: "root"
      ansiblePass: "dangerous"
      #ansibleSSHPort: "22"
      #ansibleExtraArgs: ""
      nodeTaints:
       - "node.daocloud.io/es-only=true:NoSchedule"
      # nodeLabels:
      #   daocloud.io/hostname: g-worker3
 
  # ntpServer:
    # - 0.pool.ntp.org
    # - ntp1.aliyun.com
    # - ntp.ntsc.ac.cn
  
  fullPackagePath: "/root/offline" # 解压后的离线包的路径，离线模式下该字段必填
  
  osRepos: # 操作系统软件源
 
    # 支持 official-service(default), builtin
    type: builtin
    isoPath: "/root/CentOS-7-x86_64-DVD-2009.iso"
    osPackagePath: "/root/os-pkgs-centos7-v0.4.4.tar.gz"

    # type: external
    # Set the block below only if target is S3-compatible storage which need to upload files automatically(e.g. minio).
    # isoPath: "/root/CentOS-7-x86_64-DVD-2009.iso"
    # osPackagePath: "/root/os-pkgs-centos7-v0.4.4.tar.gz"
    # externalRepoEndpoint: https://external-repo.daocloud.io
    # externalRepoUsername: rootuser
    # externalRepoPassword: rootpass123
 
    # type: external
    # Set the block below if target is other storage which cannot or does not need to upload automatically(e.g. nginx).
    # That requires you to import the required packages(iso, os-pkgs) manually if not all the required offline resources exist.
    # `centos` as CentOS, RedHat, kylin, AlmaLinux, Fedora or Openeuler
    # `debian` as Debian
    # `ubuntu` as Ubuntu
    # externalRepoType: centos
    # externalRepoURLs: ['https://extertal-repo.daocloud.io/kubean/centos/\$releasever/os/\$basearch/']
 
  imagesAndCharts: # 镜像仓库和 Chart仓库源
 
    # official-service(default), builtin or external
 
    type: builtin
 
    # type: external
    # IP or domain name
    # externalImageRepo: https://external-registry.daocloud.io
    # Set user and password. Optional
    # externalImageRepoUsername: admin
    # externalImageRepoPassword: Harbor12345
    # chartmuseum or harbor
    # externalChartRepoType: chartmuseum
    # IP or domain name
    # externalChartRepo: https://external-charts.daocloud.io:8081
    # Set user and password. Optional
    # externalChartRepoUsername: rootuser
    # externalChartRepoPassword: rootpass123
 
  addonPackage: # 应用商店 addon 离线包，定义后会对 addon 进行离线部署
    # path: "/root/addon-offline-full-package-v0.4.8-amd64.tar.gz"
   
  binaries: # 二进制可执行文件
 
    # official-service(default), builtin
    type: builtin
 
    # type: external
    # IP or domain name
    # externalRepository: https://external-binaries.daocloud.io:9000/kubean
 
 #externalMiddlewares:
  #  database:
  #    kpanda:
  #      - dbDriverName: "mysql"
  #        # Please refer https://gorm.io/docs/connecting_to_the_database.html
  #        dataSourceName: "user:password@tcp(localhost:3306)/dbname"
  #        # readwrite(default) or readonly
  #        accessType: readwrite
  #        # The maximum number of open connections to the database.
  #        #maxOpenConnections: 100
  #        # The maximum number of connections in the idle connection pool.
  #        #maxIdleConnections: 10
  #        # The maximum amount of time a connection may be reused.
  #        #connectionMaxLifetimeSeconds: 3600
  #        # The maximum amount of time a connection may be idle.
  #        #connectionMaxIdleSeconds: 1800
  #    ghippoApiserver:
  #      - dbDriverName: "mysql"
  #        dataSourceName: "user:password@tcp(localhost:3306)/dbname"
  #    ghippoKeycloak:
  #      - dbDriverName: "mysql"
  #        dataSourceName: "user:password@tcp(localhost:3306)/dbname"
  #    ghippoAuditserver:
  #      - dbDriverName: "mysql"
  #        dataSourceName: "user:password@tcp(localhost:3306)/dbname"
  #  elasticsearch:
  #    insight:
  #      endpoint: "https://xx.xx.xx.xx:9200"
  #      # login with basic auth or bearer auth
  #      #anonymous: false
  #      # basic auth
  #      username: "username"
  #      password: "password"
  #  kafka:
  #    brokers:
  #      - host1:9092
  #      - host2:9092
  #    # the username and password of kafka is not necessary
  #    username: "username"
  #    password: "password"
  #  S3Storage:
  #    default:
  #      endpoint: "xx.xx.xx.xx:9000"
  #      # Set if you dont want to verify the certificate.
  #      insecure: true
  #      bucket: "bucketname"
  #      accessKey: "YOUR-ACCESS-KEY-HERE"
  #      secretKey: "YOUR-SECRET-KEY-HERE"
  
  # Examples as below. More refer to kubespray options setting documentations.
  #kubeanConfig: |-
  #  this config will set the timezone of nodes , and it won't change timezone if this config is commented out.
  #  ntp_timezone: Asia/Shanghai
  #  # Enable recommended node sysctl settings
  #  node_sysctl_tuning: true
  #  # Extra node sysctl settings while node_sysctl_tuning is enabled
  #  extra_sysctl: [{ name: net.ipv4.tcp_keepalive_time, value: 700 }]
  #  bin_dir: /usr/local/bin
  #  http_proxy: ""
  #  https_proxy: ""
  #  upstream_dns_servers:
  #    - 8.8.8.8
  #    - 8.8.4.4
  #  docker_mount_device: /dev/sdc
  #  docker_storage_options: "-s overlay2 --storage-opt overlay2.size=1G"

  # k8sVersion only take effect in online mode, don't set it in offline mode.
  # Unless to install a non-latest k8s version with offline pkg in place.
  #k8sVersion: v1.29.5
  #auditConfig:
  #  logPath: /var/log/audit/kube-apiserver-audit.log
  #  logHostPath: /var/log/kubernetes/audit
  #  #policyFile: /etc/kubernetes/audit-policy/apiserver-audit-policy.yaml
  #  #logMaxAge: 30
  #  #logMaxBackups: 10
  #  #logMaxSize: 100
  #  #policyCustomRules: >
  #  #  - level: None
  #  #    users: []
  #  #    verbs: []
  #  #    resources: []
  #network:
  #  cni: calico
  #  clusterCIDR: 10.233.64.0/18
  #  serviceCIDR: 10.233.0.0/18
  #cri:
  #  criProvider: containerd
  #  # criVersion only take effect in online mode, don't set it in offline mode
  #  #criVersion: 1.7.0
  #  # skip provision of CRI, default false. Currently only works with docker.
  #  #skipProvision: false

  #renewCerts:
  #  # there are only 2 modes of renew certs: `onetime` or `cyclical`, default value is `cyclical`.
  #  #mode: cyclical
  #  # 1. When mode is set to `cyclical`, certificate renewal will be performed on a timer in a cyclical manner.
  #  #mode: cyclical
  #  # 2. When mode is set to `onetime`, certificate renewal will be completed at once, and you can set the validity days of the certificate.
  #  #mode: onetime
  #  # valid days can be set when in `onetime` mode, default valid days is 3650.
  #  #oneTimeValidDays: 3650  

```

## 关键字段

该 YAML 文件中的关键字段说明，请参阅下表。

| 字段 | 说明 | 默认值 |
| :---- | :----- | :----- |
| clusterName | 在 KuBean Cluster 里的 Global 集群命名 | - |
| tinderKind | 火种 kind 集群配置 | - |
| tinderKind.instanceName | 火种 kind 集群的容器名称 | - |
| tinderKind.resourcesMountPath | kind 集群挂载的主机路径 | /home/kind |
| tinderKind.registryPort | kind 集群中镜像仓库的端口 | 443 |
| tinderKind.minioServerPort | kind 集群中 MinIO Server 的端口 | 9000 |
| tinderKind.minioConsolePort | kind 集群中 MinIO Console 的端口 | 9001 |
| tinderKind.chartmuseumPort | kind 集群中 ChartMuseum 的端口 | 8081 |
| masterNodes | Global 集群：Master 节点列表，包括 nodeName/ip/ansibleUser/ansiblePass 几个关键字段 | - |
| masterNodes.nodeName | 节点名称，将覆盖 hostName | - |
| masterNodes.ip | 节点 IP | - |
| masterNodes.ansibleUser | 节点账号 | - |
| masterNodes.ansiblePass | 节点密码 | - |
| masterNodes.ansibleSSHPort | ssh 的端口，默认为22 | 22 |
| masterNodes.ansibleExtraArgs | 指定 ansible 主机清单参数 | - |
| workerNodes | Global 集群：Worker 节点列表，包括 nodeName/ip/ansibleUser/ansiblePass 几个关键字段 | - |
| privateKeyPath | kuBean 部署集群的 SSH 私钥文件路径，如果填写则不需要定义 ansibleUser、ansiblePass | - |
| k8sVersion | kuBean 安装集群的 K8s 版本必须跟 KuBean 和离线包相匹配 | - |
| loadBalancer.insightVip | 如果负载均衡模式是 metallb，则需要指定一个 VIP，供给 GLobal 集群的 insight 数据收集入口使用，子集群的 insight-agent 可上报数据到这个 VIP | - |
| loadBalancer.istioGatewayVip | 如果负载均衡模式是 metallb，则需要指定一个 VIP，供给 DCE 的 UI 界面和 OpenAPI 访问入口 | - |
| loadBalancer.type | 所使用的 LoadBalancer 的模式，物理环境用 metallb，POC 用 NodePort，公有云和 SDN CNI 环境用 cloudLB（暂时还未未支持 cloudLB 模式） | NodePort (default)、metallb、cloudLB (Cloud Controller) |
| loadBalancer.SourceIP | 审计日志获取源IP，副作用：在节点层面无法进行负载均衡 | auto |
| fullPackagePath | 解压后的离线包的路径，离线模式下该字段必填 | - |
| addonPackage.path | 应用商店 addon 包本地文件系统路径 | - |
| imagesAndCharts | 镜像仓库和 Chart仓库源 | - |
| imagesAndCharts.externalChartRepo | 外置 Chart 仓库的 IP 或域名 | - |
| imagesAndCharts.externalChartRepoPassword | 外置 Chart 仓库的密码，用于推送镜像 | - |
| imagesAndCharts.externalChartRepoType | 外置 Chart 仓库的类型，取值为 chartmuseum，harbor | - |
| imagesAndCharts.externalChartRepoUsername | 外置 Chart 仓库的用户名，用于推送镜像 | - |
| imagesAndCharts.externalImageRepo | 指定 external 仓库的 IP 或者域名(需指定协议头) | - |
| imagesAndCharts.externalImageRepoPassword | 外置镜像仓库的密码，用于推送镜像 | - |
| imagesAndCharts.externalImageRepoUsername | 外置镜像仓库的用户名，用于推送镜像 | - |
| imagesAndCharts.type | 镜像与 Chart 的访问模式，取值为 official-service(在线), buitin(火种内置 registry 和 chartmuseum), external(外置) | official-service |
| auditConfig | k8s api-server 的审计日志配置 | 默认关闭 |
| binaries | 二进制可执行文件 | - |
| binaries.externalRepository | 外置二进制可执行文件仓库的访问地址，URL 形式 | - |
| binaries.type | 二进制可执行文件的访问模式，取值为 official-service(在线), builtin(火种节点内置的minio) | official-service |
| network.clusterCIDR | Cluster CIDR | - |
| network.cni | CNI 选择，比如 Calico、Cilium | calico |
| network.serviceCIDR | Service CIDR | - |
| ntpServer | 可用的 NTP 服务器，供给新节点同步时间 | - |
| osRepos | 操作系统软件源 | - |
| osRepos.externalRepoType | 外置软件源服务的操作系统类型, 取值为 centos(所有红帽系列), debian, ubuntu | - |
| osRepos.externalRepoURLs | 外置软件源的访问地址 | - |
| osRepos.isoPath | 操作系统 ISO 文件的路径, type 为 builtin 时不能为空 | - |
| osRepos.osPackagePath | 系统包文件的路径 ，type 为 builtin 时不能为空 | - |
| osRepos.type | 操作系统软件源的访问模式，取值为 official-service(在线), builtin(火种节点内置的minio) | official-service |
| kubeanConfig.ntp_timezone | 设置节点的时区，如果不配置该参数，默认按照节点中的时区 | - |
| kubeanConfig.node_sysctl_tuning | 开启后默认调整 Global 集群的 Systemctl 内核参数 | false |
| kubeanConfig.extra_sysctl | 设置额外的 Systemctl 内核参数 | /usr/local/bin |
| externalMiddlewares | 外置中间件 | - |
| externalMiddlewares.database | 外置数据库 | - |
| externalMiddlewares.database.ghippoApiserver | ghippoApiserver 外置数据库的配置 | - |
| externalMiddlewares.database.ghippoAuditserver | ghippoAuditserver 外置数据库的配置 | - |
| externalMiddlewares.database.ghippoKeycloak | ghippoKeycloak 外置数据库的配置 | - |
| externalMiddlewares.database.kpanda | kpanda 外置数据库的配置 | - |
| externalMiddlewares.database.kpanda[0].accessType | kpanda 外置数据库的访问类型，取值：readwrite，readonly | readwrite |
| externalMiddlewares.database.kpanda[0].driver | kpanda 外置数据库的类型，取值：mysql | mysql |
| externalMiddlewares.database.kpanda[0].dataSourceName | kpanda 外置数据库的访数据源信息，用于连接数据库，可参考 [Gorm 官网连接到数据库文档](https://gorm.io/docs/connecting_to_the_database.html) | - |
| externalMiddlewares.database.kpanda[0].maxOpenConnections | kpanda 外置数据库的最大连接数 | 10 |
| externalMiddlewares.database.kpanda[0].maxIdleConnections | kpanda 外置数据库的最大空闲连接数 | 10 |
| externalMiddlewares.database.kpanda[0].connectionMaxLifetimeSeconds | kpanda 外置数据库的最大连接生命周期 | 0 |
| externalMiddlewares.database.kpanda[0].connectionMaxIdleTimeSeconds | kpanda 外置数据库的最大空闲连接生命周期 | 0 |
| externalMiddleware.elasticsearch | 外置 Elasticsearch | - |
| externalMiddleware.elasticsearch.insight | insight 所使用的外置 Elasticsearch 配置 | - |
| externalMiddleware.elasticsearch.insight.endpoint | insight 所使用的外置 Elasticsearch 的访问地址 | - |
| externalMiddleware.elasticsearch.insight.anonymous | insight 所使用的外置 Elasticsearch 的匿名访问，取值 true，false，配置为 true 时不应再填访问凭证 | false |
| externalMiddleware.elasticsearch.insight.username | insight 所使用的外置 Elasticsearch 的访问用户名 | - |
| externalMiddleware.elasticsearch.insight.password | insight 所使用的外置 Elasticsearch 的访问密码 | - |
| externalMiddleware.kafka | 外置 kafka | - |
| externalMiddleware.kafka.insight | insight 所使用的外置 kafka 配置 | - |
| externalMiddleware.kafka.insight.brokers | brokers 地址 | - |
| externalMiddleware.kafka.insight.username | insight 所使用的外置 kafka 的访问用户名 | 可选 |
| externalMiddleware.kafka.insight.password | insight 所使用的外置 kafka 的访问密码 | 可选 |
| renewCerts | 集群证书续期 | - |
| renewCerts.mode | 证书续期的两种模式，支持 cyclical、onetime | - |

## 精简配置说明

**离线模式下采用 builtin 方式安装**

builtin 模式意味着所需的第三方软件（如 chartMusem 、Minio、Docker registry）将由安装器进行部署并提供 DCE 5.0 平台使用。

```yaml
apiVersion: provision.daocloud.io/v1alpha3
kind: ClusterConfig
metadata:
  creationTimestamp: null
spec:
  clusterName: my-cluster
  masterNodes:
    - nodeName: "g-master1" # (1)!
      ip: xx.xx.xx.xx
      ansibleUser: "root"
      ansiblePass: "dangerous"
  workerNodes:
  fullPackagePath: "/root/offline"
  osRepos:
    type: builtin # (2)!
    isoPath: "/root/CentOS-7-x86_64-DVD-2009.iso"
    osPackagePath: "/root/os-pkgs-centos7-v0.4.4.tar.gz"
  imagesAndCharts:
    type: builtin # (3)!
  addonPackage:
    #path:
    #  - "/root/standard-addon-offline-package-v0.18.0-amd64.tar.gz"
    #  - "/root/gpu-addon-offline-package-v0.18.0-amd64.tar.gz"
  binaries:
    type: builtin # (4)!
```

1. nodeName 将覆盖 hostName，应符合 RFC1123 标准
2. official-service(if omit or empty), builtin or external
3. official-service(if omit or empty), builtin or external，
   目前还不支持 External S3 ...... FIXME
4. official-service(if omit or empty), builtin or external

**离线模式下采用 external 方式安装**

external 模式意味着所需的第三方软件（如 chartMusem 、Minio、Docker registry 等等）无需安装器安装，由使用者提供地址供 DCE 5.0 平台使用。

```yaml
apiVersion: provision.daocloud.io/v1alpha3
kind: ClusterConfig
metadata:
  creationTimestamp: null
spec:
  clusterName: my-cluster
  masterNodes:
    - nodeName: "g-master1" # (1)!
      ip: xx.xx.xx.xx
      ansibleUser: "root"
      ansiblePass: "dangerous"
  workerNodes:
    
  fullPackagePath: "/root/offline"
  osRepos:
    type: external # (2)!
    isoPath: "/root/CentOS-7-x86_64-DVD-2009.iso" # (3)!
    osPackagePath: "/root/os-pkgs-centos7-v0.4.4.tar.gz" # (3)!
    externalRepoType: centos # (4)!
    externalRepoURLs: ["https://extertal-repo.daocloud.io/centos/\$releasever/os/\$basearch/"]
  imagesAndCharts:
    type: external # (5)!
    externalImageRepo: https://external-registry.daocloud.io # (6)!
    externalImageRepoUsername: admin
    externalImageRepoPassword: Harbor12345
    externalChartRepoType: chartmuseum # (7)!
    externalChartRepo: https://external-charts.daocloud.io:8081 # (8)!
    externalChartUsername: rootuser
    externalChartMuseumPassword: rootpass123
  addonPackage:
    path: "/root/addon-offline-full-package-v0.4.8-amd64.tar.gz"
  binaries:
    type: external # (2)!
    externalRepository: https://external-binaries.daocloud.io:9000/kubean # (6)!
```

1. nodeName 将覆盖 hostName，应符合 RFC1123 标准
2. official-service(if omit or empty), builtin or external
3. Optional only if external repo already have full required resources
4. `centos` as CentOS, RedHat,kylin AlmaLinux or Fedora; `debian` as Debian; `ubuntu` as Ubuntu
5. official-service(if omit or empty), builtin or external. Not Support External S3 so far...... FIXME
6. Optional only if external repo already have full required resources IP or domain name
7. chartmuseum or harbor
8. IP or domain name

**在线模式采用 official-service 方式安装**

official-service 模式，当使用者采用在线安装 DCE 5.0 时，DCE 5.0 平台使用的资源将从 DaoCloud 的官方仓库进行获取。

```yaml
apiVersion: provision.daocloud.io/v1alpha3
kind: ClusterConfig
metadata:
  creationTimestamp: null
spec:
  clusterName: my-cluster
  masterNodes:
    - nodeName: "g-master1" # (1)!
      ip: xx.xx.xx.xx
      ansibleUser: "root"
      ansiblePass: "dangerous"
  workerNodes:
```

1. nodeName 将覆盖 hostName，应符合 RFC1123 标准

## 通过命令行生成 clusterConfig 配置文件模板

### 全模式 1 节点模式

``` bash
# 官方在线
./dce5-installer generate-config --install-mode=cluster-create --master=1 --access-type=official-service
# 官方在线简化版
./dce5-installer generate-config --master=1

# 内建离线
./dce5-installer generate-config --install-mode=cluster-create --master=1 --access-type=builtin
# 内建离线简化版
./dce5-installer generate-config --master=1 --access-type=builtin

# 扩展离线
./dce5-installer generate-config --install-mode=cluster-create --master=1 --access-type=external
# 扩展离线简化版
./dce5-installer generate-config --master=1 --access-type=external
```

### 全模式 4 节点模式

``` bash
# 官方在线
./dce5-installer generate-config --install-mode=cluster-create --master=3 --access-type=official-service
# 官方在线简化版
./dce5-installer generate-config --master=3

# 内建离线
./dce5-installer generate-config --install-mode=cluster-create --master=3 --access-type=builtin
# 内建离线简化版
./dce5-installer generate-config --master=3 --access-type=builtin

# 扩展离线
./dce5-installer generate-config --install-mode=cluster-create --master=3 --access-type=external
# 扩展离线简化版
./dce5-installer generate-config --master=3 --access-type=external
```

### 全模式 7节点模式

``` bash
# 官方在线
./dce5-installer generate-config --install-mode=cluster-create --master=3 --worker=3 --access-type=official-service
# 官方在线简化版
./dce5-installer generate-config --master=3 --worker=3

# 内建离线
./dce5-installer generate-config --install-mode=cluster-create --master=3 --worker=3 --access-type=builtin
# 内建离线简化版
./dce5-installer generate-config --master=3 --worker=3 --access-type=builtin

# 扩展离线
./dce5-installer generate-config --install-mode=cluster-create --master=3 --worker=3 --access-type=external
# 扩展离线简化版
./dce5-installer generate-config --master=3 --worker=3 --access-type=external
```

### 社区版

``` bash
# 官方在线
./dce5-installer generate-config --install-mode=install-app --access-type=official-service
# 官方在线简化版
./dce5-installer generate-config --install-mode=install-app

# 内建离线
./dce5-installer generate-config --install-mode=install-app --access-type=builtin

# 扩展离线
./dce5-installer generate-config --install-mode=install-app --access-type=external
```
