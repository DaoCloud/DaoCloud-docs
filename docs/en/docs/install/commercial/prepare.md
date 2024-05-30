---
MTPE: windsonsea
date: 2024-05-11
---

# Preparations

This page explains the preparations required for deploying DCE 5.0.

!!! note

    Currently, the installer script only performs pre-deployment checks on the bootstrap node,
    including whether the prerequisites have been installed and whether the CPU of the bootstrap node
    is greater than 10 cores, the memory is greater than 12GB, and the disk space is greater than 100GB.

## Machine Checks

| **Check Item** | **Specific Requirements** | **Description** |
| -------------- | ------------------------- | --------------- |
| User Privilege | root | Deployment must be done using the root user, and the root user must be allowed to SSH login to each server |
| Swap           | Disabled | If not satisfied, there is a chance that the system will experience IO spikes, causing the container runtime to freeze |
| Firewall       | Disabled (not mandatory) | -      |
| Selinux        | Disabled (not mandatory) | -      |
| Time Sync      | All cluster nodes must have synchronized time | This is a requirement from Docker and Kubernetes. Otherwise, the kube.conf will report an error `Unable to connect to the server: x509: certificate has expired or is not yet` |
| Timezone       | All servers must have the same timezone | It is recommended to set it to Asia/Shanghai.<br />Refer to the command: timedatectl set-timezone Asia/Shanghai |
| Nameserver     | /etc/resolv.conf must have at least one nameserver | Required by CoreDNS, otherwise there will be errors. In a pure offline environment, this nameserver can be a non-existent IP address. The default CentOS 8 minimal does not have the /etc/resolv file, so you need to create it manually. |
| Protocol | IPv6 Support | IPv6 must be enabled for bootstrap nodes using Podman |

## Dependency Component Checks on the Bootstrap Node

| **Check Item** | **Version Requirement** | **Description** |
| -------------- | ---------------------- | --------------- |
| podman         | v4.4.4                 | -               |
| helm           | ≥ 3.11.1               | -               |
| skopeo         | ≥ 1.11.1               | -               |
| kind           | v0.19.0                | -               |
| kubectl        | ≥ 1.25.6               | -               |
| yq             | ≥ 4.31.1               | -               |
| minio client   | `mc.RELEASE.2023-02-16T19-20-11Z` | - |

If the dependency components do not exist, install the dependency components using the script [Installing Prerequisites](../install-tools.md).

```bash
export VERSION=v0.16.0
# Download the script
curl -LO https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/install_prerequisite_${VERSION}.sh

# Add executable permissions
chmod +x install_prerequisite_${VERSION}.sh

# Start installation
bash install_prerequisite_${VERSION}.sh online full
```
