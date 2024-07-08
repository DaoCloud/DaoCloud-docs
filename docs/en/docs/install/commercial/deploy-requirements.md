---
MTPE: ModetaNiu
date: 2024-06-28
---

# Deployment Requirements

When deploying DCE 5.0, it is necessary to first plan the software, hardware, and network.

## OS Requirements

| **Architecture** | **OS** | **Tested OS and Kernel** | Remarks (Reference) |
| ------------- | --------- | --------------------------------- | ---------------------------- |
| AMD 64 | CentOS 7.X | CentOS 7.9<br />3.10.0-1127.el7.x86_64 on an x86_64 | [Offline Installation of DCE 5.0 Enterprise](start-install.md)<br />Note: CentOS 7 support ends on June 30, 2024 |
| | Redhat 8.X | Redhat 8.4<br />4.18.0-305.el8.x86_64 | [Offline Installation of DCE 5.0 Enterprise](start-install.md) |
| | Redhat 7.X | Redhat 7.9<br />3.10.0-1160.el7.x86 | [Offline Installation of DCE 5.0 Enterprise](start-install.md) |
| | Redhat 9.X | Redhat 9.2<br />5.14.0-284.11.1.el9_2.x86_64 | [Offline Installation of DCE 5.0 Enterprise](start-install.md) |
| | Ubuntu 20.04 | 5.10.104 | [Offline Installation of DCE 5.0 Enterprise](start-install.md) |
| | Ubuntu 22.04 | 5.15.0-78-generic | [Offline Installation of DCE 5.0 Enterprise](start-install.md) |
| | UnionTech OS V20 (1020a) | 5.4.0-125-generic | [Deploying DCE 5.0 Enterprise on UOS V20 (1020a)](../os-install/uos-v20-install-dce5.0.md) |
| | openEuler 22.03 | 5.10.0-60.18.0.50.oe2203.x86_64 | [Offline Installation of DCE 5.0 Enterprise](start-install.md) |
| | Oracle Linux R9/R8 U1 | 5.15.0-3.60.5.1.el9uek.x86_64 | [Deploying DCE 5.0 Enterprise on Oracle Linux R9 U1](../os-install/oracleLinux-install-dce5.0.md) |
| | TencentOS Server 3.1 | 5.4.119-19.0009.14 | [Deploying DCE 5.0 Enterprise on TencentOS Server 3.1](../os-install/TencentOS-install-dce5.0.md) |
| ARM 64 | Kylin OS V10 SP2 | 4.19.90-24.4.v2101.ky10.aarch64 | [Offline Installation of DCE 5.0 Enterprise](start-install.md) |

!!! note

    - CentOS 7 will reach the end of support on June 30, 2024. Enterprises should
      plan to replace the operating system based on their specific circumstances.
    - The operating systems and kernels mentioned above are the versions used by the testers.
    - If you are using an operating system not listed in the table above, refer to the document
      [Other Linux Offline Deployment DCE 5.0 Commercial Version](../os-install/otherlinux.md)
      for installation and deployment instructions.

## Kernel Requirements

Due to certain components or functionalities having requirements for the operating system's kernel version, please refer to the table below to choose the appropriate kernel version for deployment:

| Components/Features | Kernel Version |
| -------------------- | -------------- |
| GPU Capability in Container Management | ≥ 5.15|
| Cilium | ≥ 5.12 |
| Hwameistor DRDB Capability | [Kernels compatible with DRBD](../../storage/hwameistor/intro/drbd-support.md) |
| Kubevirt | > 3.15 |
| Merbridge | ≥ 5.7 |

### ⚠️ Kernel Considerations

1. When the kernel version is below 5.9, using `ipvs` mode with `kube-proxy` can occasionally
   cause a 1-second delay when accessing internal services through Service or result in failures
   to access the Service after backend business upgrades. For more details, see the community
   [ISSUE](https://github.com/kubernetes/kubernetes/issues/81775). The following workarounds can be used:

    - Upgrade the kernel to version 5.9 or above
    - Switch the `kube-proxy` mode to `iptables`
    - Update kernel parameters: `net.ipv4.vs.conntrack=1` + `net.ipv4.vs.conn_reuse_mode=0` + `net.ipv4.vs.expire_nodest_conn=1`

2. Automatic kernel updates and upgrades on Ubuntu can cause the system to restart unexpectedly.
   If the software you are using depends on a specific kernel version, automatic updates to
   a new kernel version may lead to [compatibility issues](https://askubuntu.com/a/1176041).

## Hardware Requirements

### CPU, Memory, and Disk

| Type | Specific Requirements |
| ------ | -------------------- |
| CPU | No overselling |
| Memory | No overselling |
| Disk | IOPS > 500, Throughput > 200 MB/s |

### Requirements for CPU, Memory, and Disk in Beginner Mode

Refer to [Beginner Mode Description](./deploy-arch.md#_2).

| Quantity | Server Role | Server Usage | Number of CPUs | Memory Capacity | System Disk | Unpartitioned Disk |
| -------- | ---------- | ------------- | -------------- | --------------- | ----------- | ----------------- |
| 1 | all in one | Image repository, chart museum, and global cluster itself | 16 cores | 32 GB | 200 GB | 400 GB |

### Requirements for CPU, Memory, and Disk in 4-node Mode

Refer to [4-node Mode Description](./deploy-arch.md#4).

| Quantity | Server Role | Server Usage | Number of CPUs | Memory Capacity | System Disk | Unpartitioned Disk |
| -------- | ----------- | ------------ | -------------- | --------------- | ----------- | ----------------- |
| 1 | Bootstrap Node | 1. Run installation and deployment program<br />2. Run the image repository and chart museum required by the platform | 2 cores | 4 GB | 200 GB | - |
| 3 | Control Plane | 1. Run DCE 5.0 components<br />2. Run kubernetes system components | 8 cores | 16 GB | 100 GB | 200 GB |

### Requirements for CPU, Memory, and Disk in 7-node Mode (Recommended for Production Environment)

Refer to [7-node Mode Description](./deploy-arch.md#7-1-6).

| Quantity | Server Role | Server Usage | Number of CPUs | Memory Capacity | System Disk | Unpartitioned Disk |
| -------- | ----------- | ------------ | -------------- | --------------- | ----------- | ----------------- |
| 1 | Bootstrap Node | 1. Run installation and deployment program<br />2. Run the image repository and chart museum required by the platform | 2 cores | 4 GB | 200 GB | - |
| 3 | Master | 1. Run DCE 5.0 components<br />2. Run kubernetes system components | 8 cores | 16 GB | 100 GB | 200 GB |
| 3 | Worker | Run log-related components separately | 8 cores | 16 GB | 100 GB | 200 GB |

### etcd Disk Recommendations

Since etcd writes data to disk and persists it there, its performance is highly dependent on disk performance. Moreover, etcd is very sensitive to disk write latency, and latency issues can lead to etcd losing heartbeats.

**Recommendations:**

- Run etcd on machines supported by low-latency and high-throughput SSD or NVMe disks whenever possible.
- Use solid-state drives (SSDs) as the minimum choice. In production environments, NVMe drives are preferred.

## Network Requirements

### Network Topology

Assuming VIP is used as the load balancing method for the global cluster:

![Network-Topology](https://docs.daocloud.io/daocloud-docs-images/docs/install/commercial/images/Network-Topology.png)

### Network Requirements

| Resource | Requirements | Description |
| -------- | ------------ | ----------- |
| `istioGatewayVip` | 1 | If the load balancing mode is metallb, a VIP needs to be specified for the UI interface and OpenAPI access entry of DCE. |
| `insightVip` | 1 | If the load balancing mode is metallb, a VIP needs to be specified for the insight data collection entry of the global cluster. The insight-agent of the sub-cluster can report data to this VIP. |
| Network Speed | 1000 M/s | Not less than 1 Gbps, 10 Gbps is recommended |
| Protocol | - | Supports IPv6 |
| Reserved IP Address Ranges | 2 | Used by Pods (default is 10.233.64.0/18) and Services (default is 10.233.0.0/18). If they are already in use, you can define other IP address ranges to avoid IP address conflicts. |
| Routing | - | Servers have default routes or routes pointing to the 0.0.0.0 address. |
| NTP Server Address | 1~4 | Make sure that there are accessible NTP server IP addresses in your data center. |
| DNS Server Address | 1~2 | If your applications require DNS services, prepare accessible DNS server IP addresses. |

## Client Browser Requirements

- Firefox **≥** v49
- Chrome **≥** v54
