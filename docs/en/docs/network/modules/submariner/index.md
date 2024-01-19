---
MTPE: Jeanine-tw
Revised: Jeanine-tw
Pics: N/A
Date: 2023-05-17
---

# What is Submariner

As Kubernetes continues to evolve, multicluster architectures are becoming increasingly popular. Multiclusters improve application redundancy, scalability, and fault isolation capabilities, but interconnectivity between clusters is a major issue. Submariner is an open-source multicluster networking solution that securely enables cross-cluster communication between Pods and Services, and leverages the Lighthouse component to enable [KMCS](https://github.com/kubernetes/enhancements/tree/master/keps/sig-multicluster/1645-multicluster-services-api) that provides cross-cluster service discovery capabilities.

The **architecture**:

![submariner](https://docs.daocloud.io/daocloud-docs-images/docs/network/images/submariner.png)

It includes the following **important components**:

- Broker: has no actual Pod and Service, but only provides credentials for subclusters to access the Broker cluster API-Server. Based on this, it enables the exchange of Metadata information between sub-clusters for discovering each other.
- Gateway Engine: establishes and maintains tunnels between clusters to establish network communication across clusters.
- Route Agent: establishes Vxlan tunnels between Gateway nodes and worker nodes so that cross-cluster traffic on worker nodes is first forwarded to Gateway nodes and then sent from Gateway nodes to the other side via cross-cluster tunnels.
- Service Discover: includes the Lighthouse-agent and Lighthouse-dns-server components that implement the KMCS API to provide cross-cluster service discovery.

**Optional components**:

- Globalnet Controller: supports cross-cluster interconnection of overlapping subnets.

**Important CRD** lists:

```shell
[root@master1]# kubectl get crd | grep -iE 'submariner|.multicluster'
brokers.submariner.io                                 2023-02-22T13:56:30Z
clusterglobalegressips.submariner.io                  2023-02-22T13:56:37Z
clusters.submariner.io                                2023-02-22T13:56:37Z
endpoints.submariner.io                               2023-02-22T13:56:37Z
gateways.submariner.io                                2023-02-22T13:56:37Z
globalegressips.submariner.io                         2023-02-22T13:56:37Z
globalingressips.submariner.io                        2023-02-22T13:56:37Z
servicediscoveries.submariner.io                      2023-02-22T13:56:30Z
serviceexports.multicluster.x-k8s.io                  2023-02-22T11:32:29Z
serviceimports.multicluster.x-k8s.io                  2023-02-22T11:32:29Z
submariners.submariner.io                             2023-02-22T13:56:30Z
```

- submariners.submariner.io: used by the submariner-operator component to create all Submariner components
- clusters.submariner.io: stores information about each subcluster, including the subnetting information of its Pods and Services
- endpoints.submariner.io: basic information about each subcluster gateway node, including private/public IP/tunnel mode/status, etc.
- serviceexports.multicluster.x-k8s.io: export each Service corresponding to a serviceexports object for service discovery
- serviceimports.multicluster.x-k8s.io: the Lighthouse-agent creates a corresponding serviceimports object for consumption by other clusters
- clusterglobalegressips.submariner.io: global CIDR to resolve overlapped subcluster subnets when globalnet is enabled

## What's Next

- [Submariner installation](install.md)
- [Submariner usage](usage.md)
