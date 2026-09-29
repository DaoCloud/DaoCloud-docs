---
hide:
  - toc
---

# Unifabric Overview

## Introduction

Unifabric is a full-lifecycle monitoring and management platform for RDMA networks in
high-performance computing (HPC) and large-scale cloud environments.
Its core goal is to address the **observability** and **operability** challenges in complex RDMA
network environments, helping O&M personnel and developers to:

- Keep real-time track of the health status and performance metrics of the entire network
  (switches, hosts, and links).
- Quickly locate key problems such as network congestion and packet loss that degrade
  application performance.
- Obtain data support for network capacity planning and performance tuning.

## Quick Start and Deployment

The software is deployed on the Kubernetes platform through a Helm chart.
It consists of two main components: Controller and Agent.

1. The Controller is responsible for switch collection and data integration.
2. The Agent is deployed on every host in the cluster to collect host information.

## Core Features

### RDMA Topology

The RDMA topology view is one of the core interfaces of Unifabric, providing a hierarchical
display and device monitoring for the entire network.
This view supports a hierarchical topology display that clearly shows the hierarchy of devices
such as Spine switches, Leaf switches, and super nodes, and indicates the connection status
between devices in real time. With this interface, O&M personnel can perform centralized
monitoring of Spine/Leaf switches, compute nodes, and storage devices in the network and check
their runtime data and health information. In addition, it provides convenient topology
navigation: users can click a super node area to drill down into details, and quickly query and
manage the basic information (such as IP and configuration) of all key network components through
detailed lists such as the node list, compute switch list, and storage switch list.

### Super Node Topology

The super node group topology view focuses on **local in-depth analysis** in high-performance
computing environments. By providing cluster switching and super node switching, it enables users
to quickly locate and enter a specific high-performance computing group for analysis. The view
presents the internal interconnection structure of the selected group as a super node group
view, and, together with the node status feature, intuitively shows the health of the compute
nodes in the group. It also provides strong diagnostic capabilities: users can click any link to
enter link performance analysis and view a detailed report, and quickly obtain detailed
information about all connections through the link list, thereby effectively diagnosing and
resolving network performance bottlenecks and congestion problems within the group.

### Unifabric Feature Details

| Feature | Description |
| ------ | -------- |
| Hierarchical topology display | Supports displaying the connection architecture of Spine switches, Leaf switches, super node groups, and storage devices. |
| Connection status indication | Supports displaying the connection status between devices in real time. When a connection is interrupted, the connection line automatically disappears. |
| Spine/Leaf monitoring | Supports displaying the runtime data and monitoring metrics of switches. |
| Compute node monitoring | Supports displaying the status and performance information of compute nodes. |
| Storage device display | Supports displaying the connection status of storage devices. |
| Compute switch list | Supports displaying details of Spine/Leaf switches, including role, management IP, port status, TX/RX bandwidth, utilization, and uptime. |
| Storage switch list | Supports displaying details of storage switches, including management IP, port status, and TX/RX bandwidth and utilization. |
| Node list | Supports displaying details of compute nodes, including basic information, number of RDMA devices, number of Pods, and bandwidth utilization. |
| Topology navigation | Supports clicking a super node area to view the detailed super node group topology view. |
| Cluster switching | Supports cluster selection. |
| Super node switching | Supports super node group selection. |
| Super node group view | Supports displaying the internal interconnection structure of the selected super node group. |
| Node status | Supports displaying node health status. |
| GPU interconnection details | Supports displaying the link connections between each super node. |
| Link performance analysis | Supports clicking any link connection path to display the real-time data and performance metrics of that link. |
| Link list | Supports displaying link details, including node name, GPU device ID, link ID, RX/TX rate, network errors (UE), and congestion (CE) metrics. |
