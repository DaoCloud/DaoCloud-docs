# Cluster configuration file clusterConfig.yaml

This YAML file contains various configuration fields of the cluster, and this file must be configured before installation.
This file will define key parameters such as deployment mode and cluster node information. By default it is located in the `offline/sample/` directory.

The v0.6.0 version optimizes the structure of the configuration file, making it clearer and easier to read than before.

## ClusterConfig Example

The following is an example ClusterConfig file.

```yaml title="clusterConfig.yaml"
apiVersion: provision.daocloud.io/v1alpha3
kind: ClusterConfig
metadata:
spec:
   clusterName: my-cluster
   
   # The domain name or IP of the bootstrapping node, by default, resolves to the IP of the network card where the default gateway of the bootstrapping node is located; you can manually fill in the IP or domain name, if it is a domain name, if it is detected that it cannot be resolved, a mapping between this domain name and the default IP of the bootstrapping node will be automatically established
   # bootstrapNode: auto
 
   loadBalancer:
 
     # NodePort(default), metallb, cloudLB (Cloud Controller)
     type: metallb
     istioGatewayVip: xx.xx.xx.xx/32 # Required when loadBalancer.type is metallb, provide UI and OpenAPI access for DCE
     insightVip: xx.xx.xx.xx/32 # Do not discard /32, it is required when loadBalancer.type is metallb, it is used as the Insight data collection entry of the global cluster, and the insight-agent of the sub-cluster can report data to this VIP
 
   # Specify the ssh private key, no need to define ansibleUser and ansiblePass of the node after definition
   # privateKeyPath: /root/.ssh/id_rsa_sample
 
   masterNodes:
     - nodeName: "g-master1" # nodeName will override hostName, should conform to RFC1123 standard
       ip: xx.xx.xx.xx
       ansibleUser: "root"
       ansiblePass: "dangerous"
     - nodeName: "g-master2"
       ip: xx.xx.xx.xx
       ansibleUser: "root"
       ansiblePass: "dangerous"
     - nodeName: "g-master3"
       ip: xx.xx.xx.xx
       ansibleUser: "root"
       ansiblePass: "dangerous"
   workerNodes:
     - nodeName: "g-worker1"
       ip: xx.xx.xx.xx
       ansibleUser: "root"
       ansiblePass: "dangerous"
       nodeTaints: # For 7-node mode: at least 3 worker nodes should be tainted (ES nodes only)
        - "node.daocloud.io/es-only=true:NoSchedule"
     - nodeName: "g-worker2"
       ip: xx.xx.xx.xx
       ansibleUser: "root"
       ansiblePass: "dangerous"
       nodeTaints:
        - "node.daocloud.io/es-only=true:NoSchedule"
     - nodeName: "g-worker3"
       ip: xx.xx.xx.xx
       ansibleUser: "root"
       ansiblePass: "dangerous"
       nodeTaints:
        - "node.daocloud.io/es-only=true:NoSchedule"
 
   # ntpServer:
     # - 0.pool.ntp.org
     # - ntp1.aliyun.com
     # - ntp.ntsc.ac.cn
  
   fullPackagePath: "/root/offline" # The path of the decompressed offline package, this field is required in offline mode
  
   osRepos: # Operating system software source
 
     # support official-service(default), builtin
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
 
   imagesAndCharts: # container registry and Chart registry source
 
     # official-service(default), builtin or external
 
     type: builtin
 
     # type: external
     # IP or domain name
     # externalImageRepo: https://external-registry.daocloud.io
     # Set user and password. Optional
     # externalImageRepoUsername: admin
     # externalImageRepoPassword: Harbor12345
     #chartmuseum or harbor
     # externalChartRepoType: chartmuseum
     # IP or domain name
     # externalChartRepo: https://external-charts.daocloud.io:8081
     # Set user and password. Optional
     # externalChartRepoUsername: rootuser
     # externalChartRepoPassword: rootpass123
 
   addonPackage: # App store addon offline package, after definition, addon will be deployed offline
     # path: "/root/addon-offline-full-package-v0.4.8-amd64.tar.gz"
   
   binaries: # Binary executables
 
     # official-service(default), builtin
     type: builtin
 
     # type: external
     # IP or domain name
     # externalRepository: https://external-binaries.daocloud.io:9000/kubean
 
  #externalMiddlewares:
   # database:
   #kpanda:
   # - dbDriverName: "mysql"
   # # Please refer https://gorm.io/docs/connecting_to_the_database.html
   # dataSourceName: "user:password@tcp(localhost:3306)/dbname"
   # # readwrite(default) or readonly
   # accessType: readwrite
   # # The maximum number of open connections to the database.
   # #maxOpenConnections: 100
   # # The maximum number of connections in the idle connection pool.
   # #maxIdleConnections: 10
   # # The maximum amount of time a connection may be reused.
   # #connectionMaxLifetimeSeconds: 3600
   # # The maximum amount of time a connection may be idle.
   # #connectionMaxIdleSeconds: 1800
   #ghippoApiserver:
   # - dbDriverName: "mysql"
   # dataSourceName: "user:password@tcp(localhost:3306)/dbname"
   #ghippoKeycloak:#      - dbDriverName: "mysql"
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
  #  S3Storage:
  #    default:
  #      endpoint: "xx.xx.xx.xx:9000"
  #      # Set if you dont want to verify the certificate.
  #      insecure: true
  #      bucket: "bucketname"
  #      accessKey: "YOUR-ACCESS-KEY-HERE"
  #      secretKey: "YOUR-SECRET-KEY-HERE"
  
  # Examples as below. More refer to kubespray options setting documentations.
  # kubeanConfig: |-
  #  # Enable recommended node sysctl settings
  #  node_sysctl_tuning: true
  #  # Extra node sysctl settings while node_sysctl_tuning is enabled
  #  extra_sysctl: [{ name: net.ipv4.tcp_keepalive_time, value: 700 }]
  # bin_dir: /usr/local/bin
  # http_proxy: ""
  # https_proxy: ""
  # upstream_dns_servers:
  #   - 8.8.8.8
  #   - 8.8.4.4
 
  # k8sVersion only take effect in online mode, don't set it in offline mode.
  # Unless to install a non-latest k8s version with offline pkg in place.
  # k8sVersion: v1.25.4
  # auditConfig:
  #  logPath: /var/log/audit/kube-apiserver-audit.log
  #  logHostPath: /var/log/kubernetes/audit
  #  policyFile: /etc/kubernetes/audit-policy/apiserver-audit-policy.yaml
  #  logMaxAge: 30
  #  logMaxBackups: 10
  #  logMaxSize: 100
  #  policyCustomRules: >
  #    - level: None
  #      users: []
  #      verbs: []
  #      resources: []
  # network:
  #  cni: calico
  #  clusterCIDR: 10.233.64.0/18
  #  serviceCIDR: 10.233.0.0/18
  # cri:
  #  criProvider: containerd
  #  criVersion only take effect in online mode, don't set it in offline mode
  #  criVersion: 1.6.8
```

## Key fields

For key field descriptions in this YAML file, see the table below.

| Field | Description | Default |
| :----------------------------------------------------------- | :----------------------------------------------------------- | :------------------------------------------------------ |
| auditConfig | k8s api-server audit log configuration | default off |
| binaries | binary executables | - |
| binaries.externalRepository | The access address of the external binary executable file repository, URL format | - |
| binaries.type | The access mode of the binary executable file, the value is official-service (online), builtin (minio built in bootstrapping node) | official-service |
| clusterName | Global cluster name in KuBean Cluster | - |
| fullPackagePath | The path of the decompressed offline package, this field is required in offline mode | - |
| addonPackage.path | App store addon package local file system path | - |
| imagesAndCharts | Container registry and Chart repository source | - |
| imagesAndCharts.externalChartRepo | IP or domain name of external Chart repository | - |
| imagesAndCharts.externalChartRepoPassword | The password of the external Chart repository, used to push the image | - |
| imagesAndCharts.externalChartRepoType | The type of external Chart repository, the value is chartmuseum, harbor | - |
| imagesAndCharts.externalChartRepoUsername | The username of the external Chart repository, used to push images | - |
| imagesAndCharts.externalImageRepo | Specify the IP or domain name of the external registry (need to specify the protocol header) | - |
| imagesAndCharts.externalImageRepoPassword | The password of the external image repository, used to push images | - |
| imagesAndCharts.externalImageRepoUsername | The username of the external image repository, used to push images | - |
| imagesAndCharts.type| Mirror and Chart access mode, the value is official-service (online), buitin (Tinder built-in registry and chartmuseum), external (external) | official-service |
| k8sVersion | The K8s version of the kuBean installation cluster must match the KuBean and offline packages | - |
| loadBalancer.insightVip | If the load balancing mode is metallb, you need to specify a VIP for the insight data collection portal of the GLobal cluster, and the insight-agent of the sub-cluster can report data to this VIP | - |
| loadBalancer.istioGatewayVip | If the load balancing mode is metallb, you need to specify a VIP to provide DCE UI interface and OpenAPI access entrance | - |
| loadBalancer.type | LoadBalancer mode used, metallb for physical environment, NodePort for POC, cloudLB for public cloud and SDN CNI environment | NodePort (default), metallb, cloudLB (Cloud Controller) |
| masterNodes | Global cluster: Master node list, including several key fields of nodeName/ip/ansibleUser/ansiblePass | - |
| network.clusterCIDR | Cluster CIDR | - |
| network.cni | CNI selection, such as Calico, Cilium | calico |
| network.serviceCIDR | Service CIDR | - |
| ntpServer | Available NTP server for new nodes to synchronize time | - |
| osRepos | Operating System Software Repositories | - |
| osRepos.externalRepoType | The operating system type of the external software source service, the value is centos (all Red Hat series), debian, ubuntu | - |
| osRepos.externalRepoURLs | Access URLs of external software sources | - |
| osRepos.isoPath | The path of the ISO file of the operating system, cannot be empty when type is builtin | - |
| osRepos.osPackagePath | The path of the system package file, it cannot be empty when type is builtin | - |
| osRepos.type | The access mode of the operating system software source, the value is official-service (online), builtin (minio built into the bootstrapping node) | official-service |
| privateKeyPath | The SSH private key file path of the kuBean deployment cluster, if filled in, no need to define ansibleUser, ansiblePass | - |
| workerNodes | Global cluster: Worker node list, including nodeName/ip/ansibleUser/ansiblePass several key fields | - |
| externalMiddlewares | External Middleware | - |
| externalMiddlewares.database | externalMiddlewares.database | - |
| externalMiddlewares.database.ghippoApiserver | ghippoApiserver external database configuration | - |
| externalMiddlewares.database.ghippoAuditserver | ghippoAuditserver external database configuration | - |
| externalMiddlewares.database.ghippoKeycloak | ghippoKeycloak external database configuration | - |
| externalMiddlewares.database.kpanda | kpanda external database configuration | - |
| externalMiddlewares.database.kpanda[0].accessType | kpanda external database access type, value: readwrite, readonly | readwrite |
| externalMiddlewares.database.kpanda[0].driver | kpanda external database type, value: mysql | mysql |
| externalMiddlewares.database.kpanda[0].dataSourceName | kpanda external database access data source information, used to connect to the database, please refer to https://gorm.io/docs/connecting_to_the_database.html | - |
| externalMiddlewares.database.kpanda[0].maxOpenConnections | kpanda Maximum number of connections to an external database | 10 |
| externalMiddlewares.database.kpanda[0].maxIdleConnections | The maximum number of idle connections of kpanda external database | 10 |
| externalMiddlewares.database.kpanda[0].connectionMaxLifetimeSeconds | The maximum connection lifetime of kpanda's external database | 0 |
| externalMiddlewares.database.kpanda[0].connectionMaxIdleTimeSeconds | The maximum idle connection lifetime of kpanda external database | 0 |
| externalMiddleware.elasticsearch | ExternalMiddleware.elasticsearch | - |
| externalMiddleware.elasticsearch.insight | External Elasticsearch configuration used by insight | - |
| externalMiddleware.elasticsearch.insight.endpoint | The access address of the external Elasticsearch used by insight | - |
| externalMiddleware.elasticsearch.insight.anonymous | Anonymous access of the external Elasticsearch used by insight, the value is true, false, and the access credentials should not be filled in when it is set to true | false |
| externalMiddleware.elasticsearch.insight.username | The access username of the external Elasticsearch used by insight | - |
| externalMiddleware.elasticsearch.insight.password | The access password of the external Elasticsearch used by insight | - |

## Simplified configuration instructions

**In the offline mode, use the builtin method to install**

```yaml
apiVersion: provision.daocloud.io/v1alpha3
kind: ClusterConfig
metadata:
   creationTimestamp: null
spec:
   clusterName: my-cluster
   masterNodes:
     # nodeName will override hostName, should conform to RFC1123 standard
     - nodeName: "g-master1"
       ip: xx.xx.xx.xx
       ansibleUser: "root"
       ansiblePass: "dangerous"
   workerNodes:
   fullPackagePath: "/root/offline"
   osRepos:
     # official-service(if omit or empty), builtin or external
     type: builtin
     isoPath: "/root/CentOS-7-x86_64-DVD-2009.iso"
     osPackagePath: "/root/os-pkgs-centos7-v0.4.4.tar.gz"
   imagesAndCharts:
     # official-service(if omit or empty), builtin or external
     # External S3 is not yet supported  … FIXME
     type: builtin
   addonPackage:
     path: "/root/addon-offline-full-package-v0.4.8-amd64.tar.gz"
   binaries:
     # official-service(if omit or empty), builtin or external
     type: builtin
```

**Installation in external mode in offline mode**

```yaml
apiVersion: provision.daocloud.io/v1alpha3
kind: ClusterConfig
metadata:
   creationTimestamp: null
spec:
   clusterName: my-cluster
   masterNodes:
     # nodeName will override hostName, should conform to RFC1123 standard
     - nodeName: "g-master1"
       ip: xx.xx.xx.xx
       ansibleUser: "root"
       ansiblePass: "dangerous"
   workerNodes:
    
   fullPackagePath: "/root/offline"
   osRepos:
     # official-service(if omit or empty), builtin or external
     type: external
     # Optional only if external repo already have full required resources
     isoPath: "/root/CentOS-7-x86_64-DVD-2009.iso"
     # Optional only if external repo already have full required resources
     osPackagePath: "/root/os-pkgs-centos7-v0.4.4.tar.gz"
     # `centos` as CentOS, RedHat, kylin AlmaLinux or Fedora
     # `debian` as Debian
     # `ubuntu` as Ubuntu
     externalRepoType: centos
     externalRepoURLs: ["https://extertal-repo.daocloud.io/centos/\$releasever/os/\$basearch/"]
   imagesAndCharts:
     # official-service(if omit or empty), builtin or external
     # Not Support External S3 so far... FIXME
     type: external
     # Optional only if external repo already have full required resources
     # IP or domain name
     externalImageRepo: https://external-registry.daocloud.io
     externalImageRepoUsername: admin
     externalImageRepoPassword: Harbor12345
     #chartmuseum or harbor
     externalChartRepoType: chartmuseum
     # IP or domain name
     externalChartRepo: https://external-charts.daocloud.io:8081
     externalChartUsername: rootuser
     externalChartMuseumPassword: rootpass123
   addonPackage:
     path: "/root/addon-offline-full-package-v0.4.8-amd64.tar.gz"
   binaries:
     # official-service(if omit or empty), builtin or external
     type: external
     # Optional only if external repo already have full required resources
     # IP or domain name
     externalRepository: https://external-binaries.daocloud.io:9000/kubean
```

**Online mode is installed by official-service**

```yaml
apiVersion: provision.daocloud.io/v1alpha3
kind: ClusterConfig
metadata:
   creationTimestamp: null
spec:
   clusterName: my-cluster
   masterNodes:
     # nodeName will override hostName, should conform to RFC1123 standard
     - nodeName: "g-master1"
       ip: xx.xx.xx.xx
       ansibleUser: "root"
       ansiblePass: "dangerous"
   workerNodes:
```

## Generate a clusterConfig configuration file template through the command line

### full mode 1 node mode

``` bash
# Official online:
./dce5-installergenerate-config --install-mode=cluster-create --master=1 --access-type=official-service
# Official online simplified version:
./dce5-installer generate-config --master=1

# Built-in offline:
./dce5-installer generate-config --install-mode=cluster-create --master=1 --access-type=builtin
# Built-in offline simplified version:
./dce5-installer generate-config --master=1 --access-type=builtin

# Extend offline:
./dce5-installer generate-config --install-mode=cluster-create --master=1 --access-type=external
# Extended offline simplified version:
./dce5-installer generate-config --master=1 --access-type=external
```

### Full Mode 4 Node Mode

``` bash
# Official online:
./dce5-installer generate-config --install-mode=cluster-create --master=3 --access-type=official-service
# Official online simplified version:
./dce5-installer generate-config --master=3

# Built-in offline:
./dce5-installer generate-config --install-mode=cluster-create --master=3 --access-type=builtin
# Built-in offline simplified version:
./dce5-installer generate-config --master=3 --access-type=builtin

# Extend offline:
./dce5-installer generate-config --install-mode=cluster-create --master=3 --access-type=external
# Extended offline simplified version:
./dce5-installer generate-config --master=3 --access-type=external
```

### full mode 7 node mode

``` bash
# Official online:
./dce5-installer generate-config --install-mode=cluster-create --master=3 --worker=3 --access-type=official-service
# Official online simplified version:
./dce5-installer generate-config --master=3 --worker=3

# Built-in offline:
./dce5-installer generate-config --install-mode=cluster-create --master=3 --worker=3 --access-type=builtin
# Built-in offline simplified version:
./dce5-installer generate-config --master=3 --worker=3 --access-type=builtin

# Extend offline:
./dce5-installer generate-config --install-mode=cluster-create --master=3 --worker=3 --access-type=external
# Extended offline simplified version:
./dce5-installer generate-config --master=3 --worker=3 --access-type=external
```

### Community Package

``` bash
# Official online
./dce5-installer generate-config --install-mode=install-app --access-type=official-service
# Official online simplified version:
./dce5-installer generate-config --install-mode=install-app

# Built-in offline:
./dce5-installer generate-config --install-mode=install-app --access-type=builtin

# Extend offline:
./dce5-installer generate-config --install-mode=install-app --access-type=external
```
