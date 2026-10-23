# Cross-Network Zone IP Allocation

This page describes how to use Spiderpool to implement IP allocation across network zones in
multi-availability-zone or multi-subnet scenarios.

## Scenarios

- Cluster nodes are located in different data centers or availability zones
- Each zone can use only a specific subnet
- The same application needs to be allocated an IP from the corresponding subnet on different nodes

## How It Works

SpiderIPPool supports `nodeName` and `nodeAffinity` to limit the range of nodes where an IPPool is
available. When a Pod is scheduled to a node, an IP is allocated from the IPPool that matches that node.

## Prerequisites

- Spiderpool is installed (refer to [Install Spiderpool](../../modules/spiderpool/install/install.md))
- The Multus configuration is ready (refer to [Manage Multus CR](../multus-cr.md))

## Configuration Steps

### 1. Create cross-zone IPPools

Create different IPPools for different nodes or zones:

```yaml
apiVersion: spiderpool.spidernet.io/v2beta1
kind: SpiderIPPool
metadata:
  name: ippool-zone-a
spec:
  subnet: 10.6.0.0/16
  ips:
    - 10.6.168.60-10.6.168.69
  gateway: 10.6.0.1
  nodeName:
  - node-a
---
apiVersion: spiderpool.spidernet.io/v2beta1
kind: SpiderIPPool
metadata:
  name: ippool-zone-b
spec:
  subnet: 10.7.0.0/16
  ips:
    - 10.7.168.60-10.7.168.69
  gateway: 10.7.0.1
  nodeName:
  - node-b
```

### 2. Specify the IPPool for the workload

Specify multiple IPPools through annotations, and Spiderpool tries to allocate from them in order:

```yaml
metadata:
  annotations:
    ipam.spidernet.io/ippool: |-
      {
        "ipv4": ["ippool-zone-a", "ippool-zone-b"]
      }
    v1.multus-cni.io/default-network: kube-system/macvlan-conf
```

## Verification

Check whether the Pod IP falls within the corresponding subnet:

```shell
kubectl get pod -o wide
```

!!! note

    - `nodeName` is suitable for small-scale clusters, while `nodeAffinity` is more suitable for
      large-scale scenarios or scenarios managed by labels
    - The IPPool subnet and gateway must be consistent with the network where the node resides
