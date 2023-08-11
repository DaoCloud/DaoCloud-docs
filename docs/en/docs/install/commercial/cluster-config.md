# clusterConfig.yaml

This YAML file contains various configuration fields of the cluster, and this file must be configured before installation.
This file will define key parameters such as deployment mode and cluster node information. By default it is located in the `offline/sample/` directory.

The v0.6.0 version optimizes the structure of the configuration file, making it clearer and easier to read than before.

## ClusterConfig Example

The following is an example of ClusterConfig.yaml.

```yaml title="clusterConfig.yaml"
apiVersion: provision.daocloud.io/v1alpha3
kind: ClusterConfig
metadata:
spec:
  clusterName: my-cluster
   
  # The domain name or IP address of the TinderKind node, by default resolves to the IP of the default gateway on the TinderKind node's network interface. You can manually enter an IP or domain name. If it is a domain name and unable to be resolved, an automatic mapping will be created between this domain name and the default IP of the TinderKind node.
  # bootstrapNode: auto

  # Configuration for TinderKind clusters, with default values below
  #tinderKind:
  #  # Container name for the Kind cluster
  #  instanceName: my-cluster-installer
  #  # Host path where the Kind cluster will be mounted
  #  resourcesMountPath: /home/kind
  #  registryPort: 443
  #  minioServerPort: 9000
  #  minioConsolePort: 9001
  #  chartmuseumPort: 8081

  loadBalancer:

    # NodePort (default), metallb, cloudLB (Cloud Controller)
    type: metallb
    istioGatewayVip: xx.xx.xx.xx/32 # Required when loadBalancer.type is metallb, providing UI and OpenAPI access for DCE
    insightVip: xx.xx.xx.xx/32 # Do not discard /32, required when loadBalancer.type is metallb, used as the Insight data collection entry point for the global cluster, where the insight-agent of sub-clusters can report data to

  # Specify SSH private key, no need to define ansibleUser and ansiblePass for nodes after defining this
  # privateKeyPath: /root/.ssh/id_rsa_sample

  masterNodes:
    - nodeName: "g-master1" # nodeName overrides hostName, should comply with RFC1123 standard
      ip: xx.xx.xx.xx
      ansibleUser: "root"
      ansiblePass: "dangerous"
      #ansibleSSHPort: "22"
    - nodeName: "g-master2"
      ip: xx.xx.xx.xx
      ansibleUser: "root"
      ansiblePass: "dangerous"
      #ansibleSSHPort: "22"
    - nodeName: "g-master3"
      ip: xx.xx.xx.xx
      ansibleUser: "root"
      ansiblePass: "dangerous"
      #ansibleSSHPort: "22"
  workerNodes:
    - nodeName: "g-worker1"
      ip: xx.xx.xx.xx
      ansibleUser: "root"
      ansiblePass: "dangerous"
      #ansibleSSHPort: "22"
      nodeTaints:                       # For the 7-node mode: At least 3 worker nodes should have a taint applied (only for ES nodes). If an external ES is used, there is no need to add this taint.
       - "node.daocloud.io/es-only=true:NoSchedule"
      # nodeLabels:
      #   daocloud.io/hostname: g-worker1
    - nodeName: "g-worker2"
      ip: xx.xx.xx.xx
      ansibleUser: "root"
      ansiblePass: "dangerous"
      #ansibleSSHPort: "22"
      nodeTaints:
       - "node.daocloud.io/es-only=true:NoSchedule"
      # nodeLabels:
      #   daocloud.io/hostname: g-worker2
    - nodeName: "g-worker3"
      ip: xx.xx.xx.xx
      ansibleUser: "root"
      ansiblePass: "dangerous"
      #ansibleSSHPort: "22"
      nodeTaints:
       - "node.daocloud.io/es-only=true:NoSchedule"
      # nodeLabels:
      #   daocloud.io/hostname: g-worker3
 
  # ntpServer:
    # - 0.pool.ntp.org
    # - ntp1.aliyun.com
    # - ntp.ntsc.ac.cn
  
  fullPackagePath: "/root/offline" # The path to the extracted offline package, this field is required in offline mode.
  
  osRepos: # OS source
 
    # Support official-service(default), builtin
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
 
  imagesAndCharts: # Container registry and Chart repo source
 
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
 
  addonPackage: # offline package of app store addon, perform offline deployment for addon after this is defined
    # path: "/root/addon-offline-full-package-v0.4.8-amd64.tar.gz"
   
  binaries: # binary files
 
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
  #  this config will set the timezone of nodes , and it won't change timezone if this config is commented out.
  #  ntp_timezone: Asia/Shanghai
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

| Field             | Description                                                          | Default Value                                         |
| ----------------- | -------------------------------------------------------------------- | ----------------------------------------------------- |
| clusterName       | Name of the Global cluster within KuBean Cluster                      | -                                                     |
| tinderKind        | Configuration for the TinderKind cluster                              | -                                                     |
| tinderKind.instanceName | Container name for the TinderKind cluster                         | -                                                     |
| tinderKind.resourcesMountPath | Host path where the Kind cluster will be mounted                | /home/kind                                            |
| tinderKind.registryPort | Port of the container registry in the Kind cluster                     | 443                                                   |
| tinderKind.minioServerPort | Port of the MinIO Server in the Kind cluster                          | 9000                                                  |
| tinderKind.minioConsolePort | Port of the MinIO Console in the Kind cluster                         | 9001                                                  |
| tinderKind.chartmuseumPort | Port of the ChartMuseum in the Kind cluster                           | 8081                                                  |
| masterNodes       | List of Master nodes in the Global cluster, including nodeName/ip/ansibleUser/ansiblePass fields | -                                                     |
| masterNodes.nodeName | Node name that overrides hostName                                  | -                                                     |
| masterNodes.ip    | Node IP                                                             | -                                                     |
| masterNodes.ansibleUser | Node account                                                      | -                                                     |
| masterNodes.ansiblePass | Node password                                                     | -                                                     |
| masterNodes.ansibleSSHPort | ssh port, default is 22                                             | 22                                                    |
| workerNodes       | List of Worker nodes in the Global cluster, including nodeName/ip/ansibleUser/ansiblePass fields | -                                                     |
| privateKeyPath    | Path to the SSH private key file for deploying the cluster. If specified, ansibleUser and ansiblePass are not required | -                                                     |
| k8sVersion        | K8s version for installing the cluster, must match KuBean and offline package       | -                                                     |
| loadBalancer.insightVip | VIP used for Insight data collection in the Global cluster, required when loadBalancer.type is metallb   | -                                                     |
| loadBalancer.istioGatewayVip | VIP used for DCE UI and OpenAPI access when loadBalancer.type is metallb  | -                                                     |
| loadBalancer.type | Load balancer mode used, metallb for physical environments, NodePort for POC, cloudLB for public cloud and SDN CNI environments | NodePort (default), metallb, cloudLB (Cloud Controller) |
| fullPackagePath   | Path to the extracted offline package, required in offline mode      | -                                                     |
| addonPackage.path | Local file system path for the application store addon package       | -                                                     |
| imagesAndCharts   | Container registry and Chart repository sources                        | -                                                     |
| imagesAndCharts.externalChartRepo | IP or domain name of the external Chart repository              | -                                                     |
| imagesAndCharts.externalChartRepoPassword | Password for the external Chart repository, used for image push  | -                                                     |
| imagesAndCharts.externalChartRepoType | Type of the external Chart repository, either chartmuseum or harbor    | -                                                     |
| imagesAndCharts.externalChartRepoUsername | Username for the external Chart repository, used for image push | -                                                     |
| imagesAndCharts.externalImageRepo | IP or domain name of the external container registry with protocol header specified   | -                                                     |
| imagesAndCharts.externalImageRepoPassword | Password for the external container registry, used for image push  | -                                                     |
| imagesAndCharts.externalImageRepoUsername | Username for the external container registry, used for image push  | -                                                     |
| imagesAndCharts.type | Access mode for images and charts, official-service (online), buitin (TinderKind built-in registry and chartmuseum), external | official-service                                      |
| auditConfig       | Audit log configuration for the k8s api-server                        | Disabled by default                                   |
| binaries          | Executable binary files                                               | -                                                     |
| binaries.externalRepository | Access address of the external binary executable file repository in URL format | -                                                     |
| binaries.type     | Access mode for executable binary files, official-service (online), builtin (MinIO built-in in TinderKind nodes) | official-service                                      |
| network.clusterCIDR | Cluster CIDR                                                        | -                                                     |
| network.cni       | CNI selection, such as Calico, Cilium                                | calico                                                |
| network.serviceCIDR | Service CIDR                                                        | -                                                     |
| ntpServer         | Available NTP servers for time synchronization of new nodes           | -                                                     |
| osRepos           | Operating system software repositories                                | -                                                     |
| osRepos.externalRepoType | Operating system type of the external software repository, centos (all Red Hat series), debian, ubuntu | -                                                     |
| osRepos.externalRepoURLs | Access addresses of the external software repositories | - |
| osRepos.isoPath                    | Path to the operating system ISO file, required when type is builtin | -                                                     |
| osRepos.osPackagePath              | Path to the system package file, required when type is builtin        | -                                                     |
| osRepos.type                       | Access mode for the operating system software repository, either official-service (online) or builtin (MinIO built-in in TinderKind nodes) | official-service                                      |
| kubeanConfig.ntp_timezone          | Timezone setting for the nodes, if not configured, it will default to the timezone in the nodes | -                                                       |
| kubeanConfig.node_sysctl_tuning    | Enable to adjust the Systemctl kernel parameters for the Global cluster | false                                                   |
| kubeanConfig.extra_sysctl          | Set additional Systemctl kernel parameters                          | /usr/local/bin                                          |
| externalMiddlewares                | External middlewares                                                 | -                                                       |
| externalMiddlewares.database       | External database                                                   | -                                                       |
| externalMiddlewares.database.ghippoApiserver | Configuration for the external ghippoApiserver database         | -                                                       |
| externalMiddlewares.database.ghippoAuditserver | Configuration for the external ghippoAuditserver database     | -                                                       |
| externalMiddlewares.database.ghippoKeycloak | Configuration for the external ghippoKeycloak database          | -                                                       |
| externalMiddlewares.database.kpanda | Configuration for the external kpanda database                   | -                                                       |
| externalMiddlewares.database.kpanda[0].accessType | Access type for the external kpanda database, either readwrite or readonly | readwrite                                               |
| externalMiddlewares.database.kpanda[0].driver | Database type for the external kpanda database, currently only supports mysql | mysql                                                   |
| externalMiddlewares.database.kpanda[0].dataSourceName | Data source information for connecting to the external kpanda database, refer to https://gorm.io/docs/connecting_to_the_database.html | -                                                       |
| externalMiddlewares.database.kpanda[0].maxOpenConnections | Maximum number of open connections for the external kpanda database | 10                                                      |
| externalMiddlewares.database.kpanda[0].maxIdleConnections | Maximum number of idle connections for the external kpanda database | 10                                                      |
| externalMiddlewares.database.kpanda[0].connectionMaxLifetimeSeconds | Maximum connection lifetime in seconds for the external kpanda database | 0                                                       |
| externalMiddlewares.database.kpanda[0].connectionMaxIdleTimeSeconds | Maximum idle connection time in seconds for the external kpanda database | 0                                                       |
| externalMiddleware.elasticsearch | External Elasticsearch                                               | -                                                       |
| externalMiddleware.elasticsearch.insight | Configuration for the external Elasticsearch used by Insight       | -                                                       |
| externalMiddleware.elasticsearch.insight.endpoint | Access endpoint for the external Elasticsearch used by Insight | -                                                       |
| externalMiddleware.elasticsearch.insight.anonymous | Enable anonymous access to the external Elasticsearch used by Insight, either true or false. When set to true, credentials should not be provided | false                                                   |
| externalMiddleware.elasticsearch.insight.username | Username for accessing the external Elasticsearch used by Insight   | -                                                       |
| externalMiddleware.elasticsearch.insight.password | Password for accessing the external Elasticsearch used by Insight   | -                                                       |

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
