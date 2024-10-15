# Create a cluster node availability check

When creating a cluster or adding nodes to an existing cluster, refer to the table below to check the node configuration to avoid cluster creation or expansion failure due to wrong node configuration.

| Check Item | Description |
| ---------- | ----------- |
| OS | Refer to [Supported Architectures and Operating Systems](#supported-architectures-and-operating-systems) |
| SELinux | Off |
| Firewall | Off |
| Architecture Consistency | Consistent CPU architecture between nodes (such as ARM or x86) |
| Host Time | All hosts are out of sync within 10 seconds. |
| Network Connectivity | The node and its SSH port can be accessed normally by the platform. |
| CPU | Available CPU resources are greater than 4 Cores |
| Memory | Available memory resources are greater than 8 GB |

## Supported architectures and operating systems

| Architecture | Operating System | Remarks |
| ---- | ------------------------ | ---- |
| ARM | Kylin Linux Advanced Server release V10 (Sword) SP2 | Recommended |
| ARM | UOS Linux | |
| ARM | openEuler | |
| x86 | CentOS 7.x | Recommended |
| x86 | Redhat 7.x | Recommended |
| x86 | Redhat 8.x | Recommended |
| x86 | Flatcar Container Linux by Kinvolk | |
| x86 | Debian Bullseye, Buster, Jessie, Stretch | |
| x86 | Ubuntu 16.04, 18.04, 20.04, 22.04 | |
| x86 | Fedora 35, 36 | |
| x86 | Fedora CoreOS | |
| x86 | openSUSE Leap 15.x/Tumbleweed | |
| x86 | Oracle Linux 7, 8, 9 | |
| x86 | Alma Linux 8, 9 | |
| x86 | Rocky Linux 8, 9 | |
| x86 | Amazon Linux 2 | |
| x86 | Kylin Linux Advanced Server release V10 (Sword) - SP2 Haiguang | |
| x86 | UOS Linux | |
| x86 | openEuler | |
