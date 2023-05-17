---
MTPE: Jeanine-tw
Revised: Jeanine-tw
Pics: Jeanine-tw
Date: 2022-12-29
---

# Install Metallb

This page describes how to install Metallb.

> To install ARP Pool, enable Helm and make it ready to wait.

Please confirm that your cluster has successfully connected to the `Container Management` platform, and then perform the following steps to install Metallb.

1. Click `Container Management`->`Clusters` in the left navigation bar, and then find the cluster name where you want to install Metallb.

    

2. In the left navigation bar, select `Helm Releases` -> `Helm Charts`, and then find and click `metallb`.

    

3. Select the version you want to install in `Version` and click `Install`.

    ! [metallb_version](./../images/metallb-helm-version.png)

4. In the installation screen, initialize Metallb ARP mode.

    !!! note

        - If ARP mode is enabled during installation, please turn on Ready Wait.

        - When installing Metallb, you can choose to initialize Metallb ARP mode.

        - LoadBalancer Service assigns IP addresses from this pool by default and declares all IP addresses in this pool via APR.

        - The address pool list can be configured for IPv4 and IPv6 addresses.

        - Each address segment can be entered either as a legal CIDR (e.g. 192.168.1.0/24) or as an IP range (e.g. 1.1.1.1-1.1.1.20).

        - Each address segment entered should belong to a real "physical" segment of the cluster node, but should not conflict with an existing IP address.

    

5. Configure `L2Advertisement Setting` -> `NodeSelectors`.

    By default, all nodes will be the next hop for the LoadBalancer IP, but you can restrict only certain nodes to be the next hop for the LoadBalancer IP via NodeSelector:

    

    As shown above, only the node matching Label "kubernetes.io/os: linux" will be the next hop for the LoadBalancer IP.

6. Specify an interface to declare the LB IP.

    By default, Metallb declares LB IPs from all NICs of the node, but we can configure specific network interfaces to declare them.

    

7. Metallb is installed.

    

!!! note

    - Metallb installation only provides initialization of ARP mode; BGP mode configuration is more complicated and requires hardware support. So initialization of Metallb BGP mode is not provided here. To configure BGP mode, please refer to [advanced_bgp_configuration](https://metallb.universe.tf/configuration/_advanced_bgp_configuration).

    - If ARP mode is not initialized during installation, you cannot use Helm update to reinitialize ARP mode, please refer to [Metallb usage](usage.md).
