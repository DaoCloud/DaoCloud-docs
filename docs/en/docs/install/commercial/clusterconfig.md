---
hide:
  - toc
---

# edit clusterConfig.yaml

This YAML file contains various configuration fields of the cluster, and this file must be configured before installation.
This file will define key parameters such as the deployed load balancing type, deployment mode, and cluster node information. By default it is located in the `offline/sample/` directory.

## ClusterConfig Example

The following is an example ClusterConfig file( assuming the bootstrap node IP is 10.6.127.220)

```yaml

apiVersion: provision.daocloud.io/v1alpha2
kind: ClusterConfig
metadata:
  creationTimestamp: null
spec:
  clusterName: my-cluster
  loadBalancer:
    type: metallb # NodePort(default), metallb, cloudLB (Cloud Controller)
    istioGatewayVip: 10.6.127.253/32 # Required when loadBalancer is metallb
                                     # Provide UI and OpenAPI access to DCE
    insightVip: 10.6.127.254/32      # Required when loadBalancer is metallb
                                     # Used as the Insight data collection entry for the GLobal cluster
                                     # The insight-agent of the subcluster can report data to this VIP 
  # privateKeyPath: /root/.ssh/id_rsa_sample
  masterNodes:
    - nodeName: "g-master1" # Node Name will override the hostName, should align with RFC1123 stsandard
      ip: 10.6.127.230
      ansibleUser: "root"       # SSH username
      ansiblePass: "dangerous"  # SSH password
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
      #nodeTaints:                       # for 7 node mode: at least 3 worker nodes should carry below taint(ES-Only nodes)
      #  - "node.daocloud.io/es-only=true:NoSchedule"
  ntpServer:
    - "172.30.120.197 iburst"
    - 0.pool.ntp.org
    - ntp1.aliyun.com
    - ntp.ntsc.ac.cn
  registry:
    type: built-in # options: built-in, external, online
    builtinRegistryDomainName: built-in-registry.daocloud.io # just to replace all /etc/hosts. if blank, all images use bootstrap node IP as registry
  imageConfig:                        # kubean rpm/deb source configuration as below
    imageRepository: built-in-registry.daocloud.io
    binaryRepository: http://10.6.127.220:9000/kubean
  repoConfig: # the kubean rpm/deb source configuration as below
    # `centos` using CentOS, RedHat,kylin AlmaLinux or Fedora
    # `debian` using Debian
    # `ubuntu` using Ubuntu
    repoType: centos
    # OS ISO file path, cannot be empty
    isoPath: "Please-replace-with-Your-Real-ISO-PATH-on-bootstrap-Node"
    dockerRepo: "http://10.6.127.220:9000/kubean/centos/$releasever/os/$basearch"
    extraRepos:
      - http://10.6.127.220:9000/kubean/centos-iso/\$releasever/os/\$basearch
      - http://10.6.127.220:9000/kubean/centos/\$releasever/os/\$basearch
  # k8sVersion only take effect in online mode, dont set it in offline mode. Unless to install a non-latest k8s version with offline pkg in place.
  k8sVersion: v1.24.7
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

## Key fields

For key fields in this YAML file, see the table below.

| Field | Description | Default |
| ----------------------- | -------------------------- ----------- | ------------------- |
| clusterName | Global cluster name in KuBean Cluster | - |
| loadBalancer.type | LoadBalancer mode used, metallb for physical environment, NodePort for POC, cloudLB for public cloud and SDN CNI environment | NodePort (default), metallb, cloudLB (Cloud Controller) |
| loadBalancer.istioGatewayVip | If the load balancing mode is metallb, you need to specify a VIP to provide DCE UI interface and OpenAPI access entrance | - |
| loadBalancer.insightVip | If the load balancing mode is metallb, you need to specify a VIP for the insight data collection portal of the GLobal cluster, and the insight-agent of the sub-cluster can report data to this VIP | - |
| privateKeyPath | The SSH private key file path of the kuBean deployment cluster, refer to the full-mode host list SSH connection settings | - |
| masterNodes | Global cluster: Master node list, including several key fields of nodeName/ip/ansibleUser/ansiblePass | - |
| workerNodes | Global cluster: Worker node list, including nodeName/ip/ansibleUser/ansiblePass several key fields | - |
| registry.type | The type of image pull registry for k8s components and DCE components, including online (online environment), built-in (use the built-in registry of Tinder node), external (use the existing external registry) | online |
| registry.builtinRegistryDomainName | If you use built-in (use the built-in registry of Tinder node), if you need to automatically implant the domain name of the registry into /etc/hosts of each node and the hosts of CoreDNS, you can specify the domain name | - |
| registry.externalRegistry | Specify the IP or domain name of the external registry (use the existing external registry), if you use Harbor, you need to create the corresponding Project in advance | - |
| registry.externalRegistryUsername | The username of the external repository, used to push images | - |
| registry.externalRegistryPassword | The password of the external repository, used to push images | - |
| imageConfig.imageRepository | If it is installed offline, the source of the local image repository when kuBean installs the cluster | - |
| imageConfig.binaryRepository | If it is installed offline, the source of the local binary repository when kuBean installs the cluster | https://files.m.daocloud.io |
| repoConfig | The source of RPM or DEB installation, if in offline mode, it is MinIO started by the installer | - |
| repoConfig.isoPath | The path of the operating system ISO file, cannot be empty in offline mode | - |
| k8sVersion | The K8s version of the kuBean installation cluster must match the KuBean and offline packages | - |
| ntpServer | Available NTP server for new nodes to synchronize time | - |
| network.cni | CNI selection, such as Calico, Cilium | calico |
| network.clusterCIDR | Cluster CIDR | - |
| network.serviceCIDR | Service CIDR | - |
| auditConfig | k8s api-server audit log configuration | default disabled |
