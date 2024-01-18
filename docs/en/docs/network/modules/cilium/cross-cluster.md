# Cilium Network Communication Acceleration

## Introduction

This page describes how to configure Cilium's communication acceleration capability. There are two optional configuration methods.

## Prerequisites

Please make sure the Linux Kernel version >= 4.9.17 with 5.10+ recommended. To view and install the latest version, you can do the following:

1. To view the current kernel version:

    ```bash
    uname -r
    ```

2. Install the ELRepo repository, which provides the latest Linux kernel version:

    ```bash
    rpm --import https://www.elrepo.org/RPM-GPG-KEY-elrepo.org
    rpm -Uvh https://www.elrepo.org/elrepo-release-7.el7.elrepo.noarch.rpm
    ```

3. Install the latest Linux kernel version:

    ```bash
    yum --enablerepo=elrepo-kernel install kernel-ml
    ```

    > `kernel-ml` is the latest documented version of the kernel. You can also choose another version.

4. Update the GRUB configuration to use the new kernel version at boot time:

    ```bash
    grub2-mkconfig -o /boot/grub2/grub.cfg
    ```

## First method：configure when creating the cluster

1. Click `Container Management` --> `Clusters`. On the page of `Create Cluster`, enter the cluster's `basic information` and `node configuration`, then go to `Network Configuration` to configure as follows:
![cilium-speedup01](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/network/images/cilium-speedup1.png)

    - Select `cilium` for the cluster's CNI plugin

    - Add `other parameters` as follows:

        ```yaml
        # Auto direct node routes must be set to be true, otherwise cross-node traffic cannot be routed
        auto-direct-node-routes: "true" 
        # If masquerading is used, it will replace the iptables implementation based on eBPF.
        # Require kernel 5.10 and later.
        # Otherwise it will be downgraded to the iptables implementation even if enabled
        enable-bpf-masquerade: "true" 
        # When doing source address translation for Pod access to outside traffic, enable it if using tunnel mode.
        # Disable it if BGP is used to connect to the physical network.
        enable-ipv6-masquerade: "false" 
        # Distribute no-ct iptables rules for the pod to improve performance.
        install-no-conntrack-iptables-rules: "true" 
        # Disable the ability for hosts to bypass their kernel stack when processing packets to speed up data forwarding. 
        # Enable it by default, but fallback to legacy behavior if the host kernel does not support it.
        enable-host-legacy-routing: "false"
        # Turn on bandwidth-manager to improve the performance of tcp, udp
        enable-bandwidth-manager: "true"
        # Kube-proxy replacement feature can be enabled after removing kube-proxy component
        kube-proxy-replacement: strict 
        # Disable tunnel mode
        tunnel: disabled
        # (optional) bbr network blocking control, with the requirement of kernel > 5.18
        enable-bbr: "true"
        ```

    - Use the default configuration items for everything else

1. Click `Create Cluster` to complete the creation.

## Second method: modify Cilium ConfigMaps

If the cluster has been created and you need to enable acceleration parameters, you can modify the `Cilium-Config` file.

Click `Container Management`--> `Clusters`. Go to the created cluster and click `ConfigMaps & Secrets`. Select `Config Items`, find `Cilium-config`, and then click Edit to enter the following acceleration parameters:

![cilium-sppedup02](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/network/images/cilium-speedup2.png)

![speed-up03](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/network/images/cilium-speedup3.png)

Once the parameters are written, click `OK` to achieve Pod communication acceleration.
