---
MTPE: ModetaNiu
DATE: 2024-07-25
---

# Virtual Machine Details

The VM Detail page displays Basic Information, Settings, GPU Configuration, Overview, Storage, Network, Snapshot, 
and Event List.

Click __Container Management__ in the left navigation bar, then click __Clusters__ to enter the page of the cluster 
where the virtual machine is located. Click the VM Name to view the virtual machine details.

### Basic Information

- Status: The current running state of the virtual machine.
- Alias: The alias of the virtual machine.
- Cluster: The cluster where the virtual machine is located.
- Namespace: The namespace where the virtual machine is located.
- IP: The IP of the virtual machine. For virtual machines with multiple network interfaces, multiple IP will be assigned.
- Label & Annotation: Set the labels and annotations for the virtual machine.
- Node: The node running the virtual machine.
- Username & Password: The username/password for logging into the virtual machine.
- Create Time: The time when virtual machine was created.

### Configuration Information

- Operating System: The operating system installed on the virtual machine to execute programs.
- Image Address: A link to a virtual hard disk file or operating system installation media, which is used to 
  load and install the operating system in the virtual machine software.
- Network Mode: The network mode configured for the virtual machine.
- CPU & Memory: The resources allocated to the virtual machine.

### GPU Configuration

- GPU Type: The type of GPU configured for the virtual machine.
- GPU Model: The model of the GPU configured for the virtual machine.
- Number of Cards: The number of GPU cards configured for the virtual machine.

![VM Detail](../images/detail01.png)

### Overview

The virtual machine overview page allows you to view the monitoring content of the virtual machine. 
Please note that monitoring information cannot be obtained if insight-agent isn't installed.

### Storage

It displays the storage used by the virtual machine, including information on the system disk and data disks.

![Storage](../images/detail-sc.png)

### Network

It displays the network configuration of the virtual machine, including Multus CR, network interface names, IP addresses, and other information.

![Network](../images/detail-network.png)

### Snapshot

It displays the snapshot information of the virtual machine and supports restoring the virtual machine from snapshots.

![Snapshots](../images/detail-snapshot.png)

### Event List

The event list includes various state changes, operation records, and system messages that occur during 
the lifecycle of the virtual machine.

![Events](../images/detail-event.png)
