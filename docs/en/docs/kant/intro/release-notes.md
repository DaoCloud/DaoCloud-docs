---
MTPE: ModetaNiu
date: 2024-06-28
---

# Release Notes

This page lists the release notes for Cloud Edge Collaboration, providing an overview
of the evolution path and feature changes in each version.

## 2024-05-30

### v0.11.0

#### Improvements

- **Improved** the interaction for custom repositories in edge units, making creation more convenient
- **Improved** the edge node access which now suppports cloud-edge communication protocols, including WebSocket and QUIC
- **Improved** edge workloads which now support multi-instance configuration

## 2024-05-06

### v0.10.0

#### New Features

- **Added** support for user-defined installation of MQTT services
- **Added** a feature of confguring workload upgrade strategy 
- **Added** a feature of configuring workload affinity 
- **Added** a feature of adding aliases for edge nodes

#### Improvements

- **Improved** the edge node access process for a more user-friendly experience

## 2024-04-07

### v0.9.0

#### New Features

- **Added** support for users to customize installation of MQTT service

#### Improvements

- **Improved** the edge node access process for a more user-friendly interaction

#### Fixes

- **Fixed** an issue with client displaying time in different time zones

## 2024-02-06

### v0.8.1

#### New Features

- **Added** a feature of rolling back versions of workloads
- **Added** display of deployed workload versions
- **Added** monitoring of edge node status, node resource usage, read/write speeds, receive/send rates, and other metrics
- **Added** monitoring of workload status, resource usage, read/write speeds, receive/send rates, and other metrics
- **Added** scheduling of GPU resources such as NVIDIA, Huawei Ascend, and others

## 2024-01-09

### v0.7.1

#### New Features

- **Added** support for integrating with KubeEdge installed in the cluster

#### Improvements

- **Improved** batch deletion interaction for edge resources
- **Improved** edge unit image authentication interaction
- **Improved** custom device parameter configuration

## 2023-12-06

### v0.6.1

#### New Features

- **Added** support for custom terminal device access, compatible with multiple device protocols
- **Added** service capabilities to support edge-to-edge communication
- **Added** a feature to view container log information

#### Improvements

- **Improved** interaction for setting component Helm repository when creating edge units
- **Improved** interaction for setting edge component image repository address when creating batch tasks
- **Improved** a feature of editing and deleting edge units in the "In Progress" state

#### Fixes

- **Fixed** an issue where the default image repository for edge units created in the Cloud Edge Collaboration installed via the installer was set to "release"
- **Fixed** an issue with abnormal edge unit status determination due to the addition of edge components

## 2023-11-06

### v0.5.0

#### New Features

- **Added** a feature of batch registration and access of x86_64 and arm64 architecture edge computing machines as edge nodes
- **Added** features of pausing/resuming the scheduling of edge nodes
- **Added** a feature of removing edge nodes
- **Added** a feature to show node information, such as Kubelet version, operating system, container runtime, resource usage/allocation status, etc.
- **Added** a feature to show the list of container groups, labels and annotations, event list, and status on edge nodes
- **Added** a feature of creating edge node groups through specified nodes or tag filtering
- **Added** a feature of editing and deleting edge node groups
- **Added** a feature of deploying applications to edge nodes as images
- **Added** a feature of creating workloads via YAML
- **Added** support for various image pull policies to meet different operational needs during application restarts
- **Added** a feature of configuring CPU/memory quotas, such as request and limit values
- **Added** a feature of configuring workload lifecycle, health checks, environment variables, data storage, and security settings
- **Added** a feature of adding workload labels and annotations
- **Added** support for multiple network access methods for workloads, including port mapping, host network, and no access
- **Added** a feature of editing workload YAML
- **Added** a feature of updating workloads, including container specifications, access configurations, deployment configurations, etc.
- **Added** operations of restarting/stopping workloads
- **Added** a feature to view workload event information
- **Added** a feature of deploying applications to edge node groups as images in bulk
- **Added** a feature of creating message routes to allow messages to be forwarded to corresponding endpoints based on configured routing rules
- **Added** the access of Modbus protocol terminal device to the platform and realized the visual management
- **Added** features of binding and unbinding terminal devices with registered edge nodes
- **Added** twin properties of adding, modifying, and deleting device
- **Added** support for editing twin properties to change the expected values in the device twin information stored on edge nodes, allowing devices to synchronize and change their status accordingly
- **Added** a feature of adding tags to devices, allowing for querying devices based on multiple tag key-value pairs
- **Added** support for configuring device access settings to obtain device data
- **Added** support for deleting terminal devices
