---
MTPE: Jeanine-tw
Revised: Jeanine-tw
Pics: Jeanine-tw
Date: 2023-01-10
---

# Install Spiderpool

This page describes how to install Spiderpool.

## Prerequisites

1. To use SpiderPool in a DCE 5.0 cluster, you need a combination of [Calico](../calico/index.md)/[Cillium](../cilium/index.md).

2. It is recommended to use Spiderpool version v0.7.0 and above. The new version of Spiderpool supports auto-installation of [Multus](../multus-underlay/install.md) which can work with [Multus CR Management](../../../network/config/multus-cr.md) to use Underlay CNIs including  [Macvlan](../multus-underlay/macvlan.md) or [SR-IOV](../multus-underlay/sriov.md), and confirm the network interface and subnet to be used.

## How to install Spiderpool

Please confirm that your cluster has successfully connected to the `Container Management` platform, and then perform the following steps to install Spiderpool.

1. Click `Container Management` -> `Clusters` in the left navigation bar and find the cluster name where you want to install Spiderpool.

2. Select `Helm Releases` -> `Helm Charts` in the left navigation bar, and then find and click `spiderpool`.

    

3. Select the version you want to install in `Version`, and click `Install`.

    

4. In the installation page, fill in the required parameters.

    

    

    The parameters in the above screens are described as follows:

    - `namespace`: namespace where SpiderPool is deployed, and the default is `kube-system`. If you change to another Namespace, the interface might not be available.

    - `Global Setting` —> `global container registry`: set the registry address of all images. The available online registry has been filled in by defaul. If it is a private environment, it can be modified to a private registry address.

    - `Spiderpool Agent Setting` —> `Spiderpool Agent Image` —>  `repository`: set the image name and just keep the default.

    - `Spiderpool Agent Setting` —> `Spiderpool Agent Prometheus Setting` -> `Enable Metrics`: if turned on, the Spiderpool Agent will collect metrics for external collection.

    - `Spiderpool Agent Setting` —> `Spiderpool Agent ServiceMonitor` -> `Install`: install the ServiceMonitor object of Spiderpool Agent, which requires Prometheus to be installed in the cluster, otherwise the creation will fail.

    - `Spiderpool Agent Setting` —> `Spiderpool Agent PrometheusRule` -> `Install`: install the prometheusRule object of Spiderpool Agent, which requires Prometheus to be installed in the cluster, otherwise the creation will fail.

    

    The parameters in the above screen are described as follows:
  
    - `Spiderpool Controller Setting` -> `replicas number`: set the number of replicas of the Spiderpool Controller, which is mainly responsible for the controller logic of the Spiderpool.

        > The Pod is in hostnetwork mode, and anti-affinity is set between Pods, so at most one Pod can be deployed on a Node. If you want to deploy more than 1 replicas, please ensure that the number of nodes in the cluster is sufficient, otherwise some Pod scheduling will fail.

    - `Spiderpool Controller Setting` -> `Spiderpool Controller Image` -> `repository`: set the image name and just keep the default.

    - `Spiderpool Controller Setting` -> `Spiderpool Controller Prometheus Setting` -> `Enable Metrics`: if turned on, the Spiderpool Controller will collect metrics information for external collection.

    - `Spiderpool Controller Setting` -> `Spiderpool Controller ServiceMonitor` -> `Install`: install the ServiceMonitor object of Spiderpool Controller, which requires Prometheus to be installed in the cluster, otherwise the creation will fail.

    - `Spiderpool Controller Setting` -> `Spiderpool Controller PrometheusRule` -> `Install`: install the prometheusRule object of the Spiderpool Controller, which requires Prometheus to be installed in the cluster, otherwise the creation will fail.

    - `IP Family Setting -> enable IPv4`: enable IPv4 support. If enabled, when assigning an IP to a pod, it must try to assign an IPv4 address, otherwise it will cause the Pod to fail to start.
    Therefore, be sure to open the subsequent `Cluster Default Ippool Installation` -> `install IPv4 ippool` to create the default IPv4 pool for the cluster.

    - `IP Family Setting -> enable IPv6`: enable IPv6 support. If enabled, when assigning an IP to the pod, it must try to assign an IPv6 address, otherwise it will cause the Pod to fail to start.
    Therefore, be sure to open the subsequent `Cluster Default Ippool Installation` -> `install IPv6 ippool` to create the default IPv6 pool for the cluster.

    

    The parameters in the above figure are described as follows:

    - `Cluster Default Ippool Installation` -> `install IPv4 ippool`: install IPv4 IP pool.

    - `Cluster Default Ippool Installation` -> `install IPv6 ippool`: install IPv6 IP pool.

    - `Cluster Default Ippool Installation` -> `IPv4 ippool name`: the name of the IPv4 ippool. Ignore this option if `install IPv4 ippool` is not enabled.

    - `Cluster Default Ippool Installation` -> `IPv6 ippool name`: the name of the IPv6 ippool. Ignore this option if `install IPv6 ippool` is not enabled.

    - `Cluster Default Ippool Installation` -> `IPv4 ippool subnet`: set the IPv4 subnet number in the default pool, e.g. `192.168.0.0/16`. Please plan the available subnets and gateways in advance. Ignore this option if `install IPv4 ippool` is not enabled.

    - `Cluster Default Ippool Installation` -> `IPv6 ippool subnet`:set the IPv6 subnet number in the default pool, e.g. `fd00::/112`. Please plan the available subnets and gateways in advance. Ignore this option if `install IPv6 ippool` is not enabled.

    - `Cluster Default Ippool Installation` -> `IPv4 ippool gateway`: set the IPv4 gateway, such as `192.168.0.1`. This IP address must belong to `IPv4 ippool subnet`. Ignore this option if `install IPv4 ippool` is not enabled.

    - `Cluster Default Ippool Installation` -> `IPv6 ippool gateway`:set the IPv6 gateway, such as `fd00::1`. The IP address must belong to `IPv6 ippool subnet`. Ignore this option if `install IPv6 ippool` is not enabled.

    - `Cluster Default Ippool Installation` -> `IP Ranges for default IPv4 ippool`:set which IP addresses can be assigned to Pods. Multiple members can be set, and each member only supports strings in 2 input formats.

        1. A continuous IP segment, such as `192.168.0.10-192.168.0.100`.
        2. A single IP address, such as `192.168.0.200`. The CIDR format is not supported.

        These IP addresses MUST belong to the `IPv4 ippool subnet`. Ignore this option if `install IPv4 ippool` is not enabled.

    - `Cluster Default Ippool Installation` -> `IP Ranges for default IPv6 ippool`: Set which IP addresses can be assigned to Pods. Multiple members can be set, and each member only supports strings in 2 input formats.

        1. a continuous IP segment, such as `fd00::10-fd00::100`.
        2. a single IP address, such as `fd00::10-fd00::100`. The CIDR format is not supported.

        These IP addresses MUST belong to the `IPv6 ippool subnet`. Ignore this option if `install IPv6 ippool` is not enabled.

5. Click the `OK` button in the lower right corner to complete the installation. When finished, you can refer to the [Usage of SpiderPool](./usage.md) to use the IP Pool.

!!! note

    During the installation process, a single subnet and ippool can be created; after the installation is complete, more subnets and ippools can be created in the user interface.
