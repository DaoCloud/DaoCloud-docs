---
hide:
  - toc
---

# edit clusterConfig.yaml

This YAML file contains various configuration fields of the cluster, and this file must be configured before installation.
This file will define key parameters such as the deployed load balancing type, deployment mode, and cluster node information. By default it is located in the `offline/sample/` directory.

## ClusterConfig Example

The following is an example ClusterConfig file( assuming the bootstrap node IP is 10.6.127.220)

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
      ansibleUser: "root"       # (6)
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

1. 3 options: `NodePort` (default), `metallb`, `cloudLB` (Cloud Controller)
2. Required when loadBalancer.type is `metallb`, provides UI and OpenAPI access for DCE
3. Do not discard /32, it is required when loadBalancer.type is metallb, it is used as the Insight data collection entry of the GLobal cluster, and the insight-agent of the sub-cluster can report data to this VIP
4. If you use SSH to access the node without password, you need to specify the address of the key file
5. `nodeName` will override hostName and should comply with RFC1123 standard
6. SSH username
7. SSH password
8. In the mode of 7 nodes and above, in order to ensure the stability of the cluster, ES will use a dedicated host. then at least 3 worker nodes need to have taints
9. Time synchronization server
10. There are several options: built-in, external, online
11. Simply replace all /etc/hosts. If blank, all mirrors will use tinder node IP as mirror repository
12. Configuration of kubean mirror warehouse and MinIO warehouse
13. kubean mirror warehouse
14. The minio repository for kubean binary sources
15. kubean rpm/deb source configuration, `centos` means CentOS, RedHat, AlmaLinux or Fedora; `debian` means Debian; `ubuntu` means Ubuntu
16. isoPath cannot be empty in offline mode
17. The k8sVersion field is only applicable to online mode, no need to set it in offline mode
18. Whether to enable k8s apisever audit log and related configuration
19. The criVersion field is only available in online mode, no need to set it in offline mode

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
| registry.type | The type of image pull registry for k8s components and DCE components, including online (online environment), built-in (use the built-in registry of bootstrapping node), external (use the existing external registry) | online |
| registry.builtinRegistryDomainName | If you use built-in (use the built-in registry of bootstrapping node), if you need to automatically implant the domain name of the registry into /etc/hosts of each node and the hosts of CoreDNS, you can specify the domain name | - |
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
