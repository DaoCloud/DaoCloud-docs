---
MTPE: Jeanine-tw
Revised: Jeanine-tw
Pics: Jeanine-tw
Date: 2022-12-29
---

# Install MetalLB

This page describes how to install MetalLB.

## Prerequisites

1. A `real physical IP` needs to be prepared for IP pool creation.

> To install ARP Pool, enable Helm and make it ready to wait.

## How to install MetalLB

Please confirm that your cluster has successfully connected to the `Container Management` platform, and then perform the following steps to install MetalLB.

1. Click `Container Management`->`Clusters` in the left navigation bar, and then find the cluster name where you want to install MetalLB.

    ![metallb_cluster](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/network/images/metallb-install-1.png)

2. In the left navigation bar, select `Helm Apps` -> `Helm Charts`, and then find and click `metallb`.

    ![metallb_repo](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/network/images/metallb-install-2.png)

3. Select the version you want to install in `Version` and click `Install`.


4. In the installation screen, initialize MetalLB ARP mode.

    !!! note

        - If ARP mode is enabled during installation, please turn on Ready Wait.

        - When installing MetalLB, you can choose to initialize MetalLB ARP mode.

        - LoadBalancer Service and declares all IP addresses in this pool via APR.

        - The address pool list can be configured for IPv4 and IPv6 addresses.

        - Each address segment can be entered either as a legal CIDR (e.g. 192.168.1.0/24) or as an IP range (e.g. 1.1.1.1-1.1.1.20).

        - Each address segment entered should belong to a real "physical" segment of the cluster node, but should not conflict with an existing IP address.
        
        - The IP pool is created with enabling address pool parameter `autoAssign: true` by default. For parameter details, refer to [Instructions for IPPool use](usage.md)

    ![metallb_ippool](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/network/images/metallb-install-3.png)

5. Configure `L2Advertisement Setting` -> `NodeSelectors`.

    By default, all nodes will be the next hop for the LoadBalancer IP, but you can restrict only certain nodes to be the next hop for the LoadBalancer IP via NodeSelector:

    ![node_list](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/network/images/metallb-install-4.png)

    As shown above, only the node matching Label "kubernetes.io/os: linux" will be the next hop for the LoadBalancer IP.

6. Specify an interface to declare the LB IP.

    By default, MetalLB declares LB IPs from all NICs of the node, but we can configure specific network interfaces to declare them.

    ![metallb-interface](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/network/images/metallb-install-5.png)

7. MetalLB is installed.

!!! note

    - MetalLB installation only provides initialization of ARP mode; BGP mode configuration is more complicated and requires hardware support. So initialization of MetalLB BGP mode is not provided here. To configure BGP mode, please refer to [advanced_bgp_configuration](https://metallb.universe.tf/configuration/_advanced_bgp_configuration).

    - If ARP mode is not initialized during installation, you cannot use Helm update to reinitialize ARP mode, please refer to [MetalLB usage](usage.md).
