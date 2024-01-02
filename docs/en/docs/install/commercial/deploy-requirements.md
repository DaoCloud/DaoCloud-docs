# Deployment Requirements

When deploying DCE 5.0, it is necessary to first plan the software, hardware, and network.

## Operating System Requirements

| Architecture | Operating System | Recommended Kernel Version | Remarks (Installation Guide) |
| ------------ | ---------------- | ------------------------- | --------------------------- |
| AMD 64       | CentOS 7.X       | Kernel 3.10.0-1127.el7.x86_64 on an x86_64 | Recommended CentOS 7.9<br />[Offline Installation of DCE 5.0 Commercial Edition](start-install.md) |
|              | Redhat 8.X       | 4.18.0-305.el8.x86_64                     | Recommended Redhat 8.4<br />Refer to [Offline Installation of DCE 5.0 Commercial Edition](start-install.md) |
|              | Redhat 7.X       | 3.10.0-1160.e17.x86                       | Recommended Redhat 7.9<br />Refer to [Offline Installation of DCE 5.0 Commercial Edition](start-install.md) |
|              | Redhat 9.X       | 5.14.0-284.11.1.e9_2.x86_64              | Recommended Redhat 9.2<br />Refer to [Offline Installation of DCE 5.0 Commercial Edition](start-install.md)<br /> |
|              | Ubuntu 20.04     | 5.10.104                                  | Refer to [Offline Installation of DCE 5.0 Commercial Edition](start-install.md) |
|              | UOS V20 (1020a) | 5.4.0-125-generic                        | Refer to [Deploying DCE 5.0 Commercial Edition on UOS V20 (1020a)](../os-install/uos-v20-install-dce5.0.md) |
|              | openEuler 22.03  | 5.10.0-60.18.0.50.oe2203.x86_64          | Refer to [Offline Installation of DCE 5.0 Commercial Edition](start-install.md) |
|              | Oracle Linux R9/R8 U1 | 5.15.0-3.60.5.1.el9uek.x86_64        | Refer to [Deploying DCE 5.0 Commercial Edition on Oracle Linux R9 U1](../os-install/oracleLinux-install-dce5.0.md) |
|              | TencentOS Server 3.1 | 5.4.119-19.0009.14                   | Refer to [Deploying DCE 5.0 Commercial Edition on TencentOS Server 3.1](../os-install/TencentOS-install-dce5.0.md) |
| ARM 64       | Kylin OS V10 SP2 | 4.19.90-24.4.v2101.ky10.aarch64         | Refer to [Offline Installation of DCE 5.0 Commercial Edition](start-install.md) |

!!! note

    If the operating system is not listed in the table above, please refer to the document [Other Linux Offline Deployment of DCE 5.0 Commercial Edition](../os-install/otherlinux.md) for installation and deployment.

## Hardware Requirements

### CPU, Memory, and Disk

| Type   | Specific Requirements |
| ------ | -------------------- |
| CPU    | No overselling       |
| Memory | No overselling       |
| Disk   | IOPS > 500, Throughput > 200 MB/s |

### Requirements for CPU, Memory, and Disk in Beginner Mode

Refer to [Beginner Mode Description](./deploy-arch.md#_2).

| Quantity | Server Role | Server Usage                           | Number of CPUs | Memory Capacity | System Disk | Unpartitioned Disk |
| -------- | ----------- | -------------------------------------- | -------------- | --------------- | ----------- | ----------------- |
| 1        | all in one  | Image repository, chart museum, and global cluster itself | 16 cores       | 32G             | 200G        | 400G              |

### Requirements for CPU, Memory, and Disk in 4-node Mode

Refer to [4-node Mode Description](./deploy-arch.md#4).

| Quantity | Server Role | Server Usage                                               | Number of CPUs | Memory Capacity | System Disk | Unpartitioned Disk |
| -------- | ----------- | ---------------------------------------------------------- | -------------- | --------------- | ----------- | ----------------- |
| 1        | Seed Node   | 1. Execute installation and deployment program<br />2. Run the image repository and chart museum required by the platform | 2              | 4G              | 200G        | -                 |
| 3        | Control Plane | 1. Run DCE 5.0 components<br />2. Run kubernetes system components | 8              | 16G             | 100G        | 200G              |

### Requirements for CPU, Memory, and Disk in 7-node Mode (Recommended for Production Environment)

Refer to [7-node Mode Description](./deploy-arch.md#7-1-6).

| Quantity | Server Role | Server Usage                                               | Number of CPUs | Memory Capacity | System Disk | Unpartitioned Disk |
| -------- | ----------- | ---------------------------------------------------------- | -------------- | --------------- | ----------- | ----------------- |
| 1        | Seed Node   | 1. Execute installation and deployment program<br />2. Run the image repository and chart museum required by the platform | 2              | 4G              | 200G        | -                 |
| 3        | Master      | 1. Run DCE 5.0 components<br />2. Run kubernetes system components | 8              | 16G             | 100G        | 200G              |
| 3        | Worker      | Run log-related components separately                      | 8              | 16G             | 100G        | 200G              |

## Network Requirements

### Network Topology

Assuming VIP is used as the load balancing method for the global cluster:

![Network-Topology](https://docs.daocloud.io/daocloud-docs-images/docs/install/commercial/images/Network-Topology.png)

### Network Requirements

| Resource          | Requirements | Description |
| ----------------- | ------------ | ----------- |
| `istioGatewayVip` | 1            | If the load balancing mode is metallb, a VIP needs to be specified for the UI interface and OpenAPI access entry of DCE. |
| `insightVip`      | 1            | If the load balancing mode is metallb, a VIP needs to be specified for the insight data collection entry of the global cluster. The insight-agent of the sub-cluster can report data to this VIP. |
| Network Speed     | 1000 M/s     | Not less than 1 Gbps, 10 Gbps is recommended |
| Protocol          | -            | Supports IPv6 |
| Reserved IP Address Ranges | 2          | Used by Pods (default is 10.233.64.0/18) and Services (default is 10.233.0.0/18). If they are already in use, you can define other IP address ranges to avoid IP address conflicts. |
| Routing           | -            | Servers have default routes or routes pointing to the 0.0.0.0 address. |
| NTP Server Address | 1~4          | Make sure that there are accessible NTP server IP addresses in your data center. |
| DNS Server Address | 1~2          | If your applications require DNS services, prepare accessible DNS server IP addresses. |

## Client Browser Requirements

- Firefox **≥** v49
- Chrome **≥** v54
