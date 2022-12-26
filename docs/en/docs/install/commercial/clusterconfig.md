---
hide:
  - toc
---

# edit clusterConfig.yaml

This YAML file contains various configuration fields of the cluster, and this file must be configured before installation.
This file will define key parameters such as the deployed load balancing type, deployment mode, and cluster node information. By default it is located in the `offline/sample/` directory.

## ClusterConfig Example

The following is an example ClusterConfig file.

```yaml
apiVersion: provision.daocloud.io/v1alpha1
kind: ClusterConfig
metadata:
  creationTimestamp: null
spec:
  loadBalancer: NodePort # NodePort(default), metallb, cloudLB (Cloud Controller)
  istioGatewayVip: 10.6.127.254/32 # Required when loadBalancer is metallb
                                   # Provide UI and OpenAPI access to DCE
  registryVip: 10.6.127.253/32 # Required when loadBalancer is metallb
                                   # The container registry access entry of the Global cluster
  insightVip: 10.6.127.252/32 # Required when loadBalancer is metallb
                              # Used as the Insight data collection entry for the GLobal cluster
                              # The insight-agent of the subcluster can report data to this VIP
  compactClusterMode: false
  globalClusterName: my-global-cluster
  mgmtClusterName: my-mgmt-cluster
  mgmtMasterNodes:
    - nodeName: "rm-master1" # nodeName will override hostName, should conform to RFC1123 standard
      ip: 10.6.127.232
      ansibleUser: "root" # username
      ansiblePass: "123456" #password
  mgmtWorkerNodes:
    - nodeName: "rm-worker1" # nodeName will override hostName, should conform to RFC1123 standard
      ip: 10.6.127.230
      ansibleUser: "root" # username
      ansiblePass: "123456" #password
  globalMasterNodes: # This field does not work in simple mode
    - nodeName: "rg-master1"
      ip: 10.6.127.231
      ansibleUser: "root"
      ansiblePass: "123456"
  globalWorkerNodes: # This field does not work in simple mode
    - nodeName: "rg-worker1"
      ip: 10.6.127.234
      ansibleUser: "root"
      ansiblePass: "123456"
  ntpServer: # time synchronization server
    - "172.30.120.197 iburst"
    - 0.pool.ntp.org
    - ntp1.aliyun.com
    - ntp.ntsc.ac.cn
  persistentRegistryDomainName: temp-registry.daocloud.io # Local container registry
  imageConfig: # kubean image configuration
    imageRepository: temp-registry.daocloud.io
    binaryRepository: http://temp-registry.daocloud.io:9000/kubean
  repoConfig: # kubean rpm/deb source configuration
    # `centos` means CentOS, RedHat, AlmaLinux or Fedora
    # `debian` means Debian
    # `ubuntu` means Ubuntu
    repoType: centos
    dockerRepo: "http://temp-registry.daocloud.io:9000/kubean/centos/$releasever/os/$basearch"
    extraRepos:
    - http://temp-registry.daocloud.io:9000/kubean/centos-iso/\$releasever/os/\$basearch
    - http://temp-registry.daocloud.io:9000/kubean/centos/\$releasever/os/\$basearch
    # The k8sVersion field is only applicable to online mode, no need to set it in offline mode
    #k8sVersion: v1.24.6
  auditConfig:
    logPath: /var/log/audit/kube-apiserver-audit.log
    logHostPath: /var/log/kubernetes/audit
    # policyFile: /etc/kubernetes/audit-policy/apiserver-audit-policy.yaml
    # logMaxAge: 30
    # logMaxBackups: 10
    # logMaxSize: 100
    # policyCustomRules: >
    # - level: None
    # users: []
    # verbs: []
    # resources: []
  network:
    cni: calico
    clusterCIDR: 100.96.0.0/11
    serviceCIDR: 100.64.0.0/13
  cri:
    criProvider: containerd
    # The criVersion field is only available in online mode, no need to set it in offline mode
    # CriVersion: 1.6.8
  addons:
    ingress:
      version: 1.2.3
    dns:
      type: CoreDNS
      version: v1.8.4
```

## key fields

For key field descriptions in this YAML file, see the table below.

| Field | Description | Default |
| ---------------------------- | -------------------- ------------------------------------------- | --------- ------------------------------------------------ |
| compactClusterMode | Compact mode: If enabled, [Global Service Cluster](../../kpanda/07UserGuide/Clusters/ClusterRole.md) will be established on the management cluster, and the system will also ignore the setting of `globalXXXNode` field, Only need to set the parameter information of `mgmtXXXNode` field, this mode is also applicable to all-in-one machines. Minimalistic mode is the default option. <br />If set to `false`, it is classic mode. |true|
| loadBalancer | The mode of LoadBalancer used, metallb for physical environment, NodePort for POC, cloudLB for public cloud and SDN CNI environment | NodePort(default), metallb, cloudLB (Cloud Controller) |
| xxVIP | VIP with different functions (only for Metallb), note that the format is 10.6.229.58/32 or 1.2.3.4-1.2.3.5 | - |
| mgmtClusterName | Name of the management cluster in KuBean | - |
| globalClusterName | The name of the global service cluster in KuBean | - |
| istioGatewayVip | If the load balancing mode is metallb, you need to specify a VIP to be used as the DCE UI interface and OpenAPI access entry | - |
| registryVip | If the load balancing mode is metallb, you need to specify a VIP to be used as the access entry of the container registry of the Global cluster | - |
| insightVip | If the load balancing mode is metallb, you need to specify a VIP for the insight data collection entry of the GLobal cluster, and the insight-agent of the sub-cluster can report data to this VIP | - |
| persistentRegistryDomainName | If it is an offline installation, you need to specify this field to specify the temporary and future registry domain name | - |
| imageConfig.imageRepository | If it is installed offline, the source of the local container registry when kuBean installs the cluster | - |
| imageConfig.binaryRepository | If it is installed offline, the source of the local binary repository when kuBean installs the cluster | https://xxx.yy.zz |
| repoConfig | Source for RPM or DEB installations. In offline mode, the installer starts MinIO | - |
| k8sVersion | K8s version of kuBean installation cluster, must match KuBean and offline package | - |
| mgmtMasterNodes | Management cluster: Master node list, including several key fields of nodeName/ip/ansibleUser/ansiblePass | - |
| mgmtWorkerNodes | Management cluster: Worker node list, including several key fields of nodeName/ip/ansibleUser/ansiblePass | - |
| globalMasterNodes | Global service cluster: Master node list, including several key fields of nodeName/ip/ansibleUser/ansiblePass | - |
| globalWorkerNodes | Global service cluster: Worker node list, including several key fields of nodeName/ip/ansibleUser/ansiblePass | - |
| ntpServer | NTP server available to use for new nodes to synchronize time | - |
| network.cni | Choose a CNI, eg calico, cilium | calico |
| network.clusterCIDR | Cluster CIDR | - |
| network.serviceCIDR | Service CIDR | - |
| auditConfig | K8s api-server audit log configuration | default disabled |