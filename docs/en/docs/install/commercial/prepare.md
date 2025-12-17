---
MTPE: windsonsea
date: 2024-05-11
---

# Prerequisites Check

This page describes the preparation work required for deploying DCE 5.0.

!!! note

    Currently, the installer script only performs prerequisite checks on the bootstrap machine,
    mainly including whether prerequisite dependency tools have been installed, and whether
    the current bootstrap has CPU > 10 Core, Memory > 12G, disk > 100GB

## Machine Check

| **Check Item** | **Specific Requirements** | **Description** |
| -------------- | ------------------------- | --------------- |
| User Permissions | root | Must use root user for deployment, and all servers must allow root user SSH login |
| swap | Disabled | If not satisfied, the system has a certain probability of io spikes, causing container runtime to freeze |
| Firewall | Disabled (not mandatory) | - |
| selinux | Disabled (not mandatory) | - |
| Time Synchronization | All cluster nodes must have synchronized time | This is an official requirement of Docker and Kubernetes. Otherwise kube.conf will report error `Unable to connect to the server: x509: certificate has expired or is not yet` |
| Timezone | All servers must have unified timezone | Recommended to set to Asia/Shanghai. <br />Reference command: timedatectl set-timezone Asia/Shanghai |
| Nameserver | /etc/resolv.conf must have at least one Nameserver | CoreDNS requirement, otherwise there will be errors. This nameserver can be a non-existent IP address in a pure offline environment. Centos8minimal has no /etc/resolv file by default and needs to be created manually |
| Network Config | IPv6 support | Bootstrap node must enable ipv6 when using podman to access K8S inside kind. Verify this by ensuring `sysctl net.ipv6.conf.all.disable_ipv6` returns `0`. |
| Network Forwarding | Enable ip_forward | Bootstrap node must enable ipv4.ip_forward, verify `sysctl net.ipv4.ip_forward` returns `1` and ensure its persistence. |

## Bootstrap Machine Dependency Component Check

| **Check Item** | **Version Requirements** | **Description** |
| -------------- | ----------------------- | --------------- |
| podman | v4.4.4 | - |
| helm | ≥ 3.11.1 | - |
| skopeo | ≥ 1.11.1 | - |
| kind | v0.19.0 | - |
| kubectl | ≥ 1.25.6 | - |
| yq | ≥ 4.31.1 | - |
| minio client | `mc.RELEASE.2023-02-16T19-20-11Z` | |

If dependency components do not exist, install them through scripts. Refer to [Install Prerequisites](../install-tools.md).

```bash
export VERSION=v0.16.0
# Download script
curl -LO https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/install_prerequisite_${VERSION}.sh

# Add executable permissions
chmod +x install_prerequisite_${VERSION}.sh

# Start installation
bash install_prerequisite_${VERSION}.sh online full
```
