# System Requirements for Installing Spiderpool

This page describes the system requirements for installing Spiderpool.

## Host Requirements

- x86-64 or arm64 architecture
- When ipvlan is used as the cluster CNI, the Linux kernel version must be greater than 4.2

## Kubernetes Requirements

Using the [SpiderSubnet](https://github.com/spidernet-io/spiderpool/blob/main/docs/usage/spider-subnet-zh_CN.md)
feature requires Kubernetes `v1.21` or later

## Host Network Ports Occupied by the Spiderpool Components

| Component | Port/Protocol | Description | Configuration Environment Variable |
|---|---|---|---|
| daemonset spiderpool-agent | 5710/tcp | Pod health check port | SPIDERPOOL_HEALTH_PORT |
| daemonset spiderpool-agent | 5711/tcp | Metrics port (if the metrics feature is enabled) | SPIDERPOOL_METRIC_HTTP_PORT |
| daemonset spiderpool-agent | 5712/tcp | gops port (if debug is enabled) | SPIDERPOOL_GOPS_LISTEN_PORT |
| deployment spiderpool-controller | 5720/tcp | Pod health check port | SPIDERPOOL_HEALTH_PORT |
| deployment spiderpool-controller | 5711/tcp | Metrics port (if the metrics feature is enabled) | SPIDERPOOL_METRIC_HTTP_PORT |
| deployment spiderpool-controller | 5722/tcp | webhook port | SPIDERPOOL_WEBHOOK_PORT |
| deployment spiderpool-controller | 5724/tcp | gops port (if debug is enabled) | SPIDERPOOL_GOPS_LISTEN_PORT |

## (Optional Installation) Host Network Ports Occupied by the SR-IOV Components

| Component | Port/Protocol | Description | Configuration Environment Variable |
|---|---|---|---|
| daemonset network-resources-injector | 5731/tcp | webhook port. This port is occupied only because this component is optionally installed | NA |
| deployment operator-webhook | 5732/tcp | webhook port. This component is optionally installed | NA |
