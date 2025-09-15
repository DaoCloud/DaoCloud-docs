---
MTPE: ModetaNiu
date: 2025-06-23
---

# Release Notes

This page lists the release notes for Cloud Edge Collaboration, providing an overview
of the evolution path and feature changes in each version.

## 2025-06-30

### v0.20.0

- **Improved** edge node onboarding process by using `keadm` and rebuilding the edge installation package.  
- **Improved** removal of `kant-workeragent` configuration in edge units, using default configuration
  for install/uninstall, with upgrades managed via Helm applications.  
- **Fixed** an issue where batch workloads temporarily filtered out resources other than Deployments.  

## 2025-03-31

### v0.19.1

* **Added** support for installing KubeEdge v1.20.0 on edge units.
* **Fixed** an issue where the user-agent in audit logs was incorrect.
* **Fixed** an issue where updating only the ConfigMap via Helm did not trigger a restart of the CloudCore Pod.
* **Fixed** an issue where the default image URLs for system components were incorrect when creating an edge unit.

## 2024-12-31

### v0.18.0

- **Added** support for reporting terminal device status.
- **Updated** the display of the time taken to retrieve status after edge unit installation.

## 2024-11-30

### v0.17.0

- **Updated** the unit display for terminal device collection and reporting intervals.
- **Updated** download prompts for edge installation packages.

## 2024-10-31

### v0.16.0

- **Updated** token validity period prompts in edge node installation commands.

## 2024-09-30

### v0.15.0

- **Updated** support for editing terminal devices while in a bound node state.
- **Updated** the batch workload management process for a more user-friendly experience.

## 2024-08-31

### v0.14.0

- **Added** support for allocating initial cloud resources to edge units based on edge node scale.
- **Added** support for uninstallation policy settings for edge units.
- **Updated** edge node access commands to allow setting the CloudCore component access address.

## 2024-07-31

### v0.13.0

- **Added** support for pre-pulling images on edge nodes when network conditions are good
- **Improved** by adding a beginner's guide to help users quickly get started with edge services.
- **Improved** the addition of a beginner's guide to help users quickly get started with edge business

## 2024-06-30

### v0.12.0

- **Added** support for creating and managing device models
- **Improved** device parameter configuration for more flexible device creation
- **Improved** support for edge installation packages to dynamically update download links based on offline environments

## 2024-05-30

### v0.11.0

- **Improved** the interaction for custom repositories in edge units, making creation more convenient
- **Improved** the edge node access which now suppports cloud-edge communication protocols, including WebSocket and QUIC
- **Improved** edge workloads which now support multi-instance configuration

## 2024-05-06

### v0.10.0

- **Added** support for user-defined installation of MQTT services
- **Added** a feature of confguring workload upgrade policy
- **Added** a feature of configuring workload affinity
- **Added** a feature of adding aliases for edge nodes
- **Improved** the edge node access process for a more user-friendly experience

## 2024-04-07

### v0.9.0

- **Added** support for users to customize installation of MQTT service
- **Improved** the edge node access process for a more user-friendly interaction
- **Fixed** an issue with client displaying time in different time zones

## 2024-02-06

### v0.8.1

- **Added** a feature of rolling back versions of workloads
- **Added** display of deployed workload versions
- **Added** monitoring of edge node status, node resource usage, read/write speeds, receive/send rates, and other metrics
- **Added** monitoring of workload status, resource usage, read/write speeds, receive/send rates, and other metrics
- **Added** scheduling of GPU resources such as NVIDIA, Huawei Ascend, and others

## 2024-01-09

### v0.7.1

- **Added** support for integrating with KubeEdge installed in the cluster
- **Improved** batch deletion interaction for edge resources
- **Improved** edge unit image authentication interaction
- **Improved** custom device parameter configuration

## 2023-12-06

### v0.6.1

#### New Features

- **Added** support for custom end device access, compatible with multiple device protocols
- **Added** service capabilities to support edge-to-edge communication
- **Added** a feature to view container log information

#### Improvements

- **Improved** interaction for setting component Helm repository when creating edge units
- **Improved** interaction for setting edge component container registry address when creating batch tasks
- **Improved** a feature of editing and deleting edge units in the "In Progress" state

#### Fixes

- **Fixed** an issue where the default container registry for edge units created in the Cloud Edge Collaboration installed via the installer was set to "release"
- **Fixed** an issue with abnormal edge unit status determination due to the addition of edge components

## 2023-11-06

### v0.5.0

- **Added** a feature of batch registration and access of x86_64 and arm64 architecture edge computing machines as edge nodes
- **Added** features of pausing/resuming the scheduling of edge nodes
- **Added** a feature of removing edge nodes
- **Added** a feature to show node information, such as kubelet version, operating system, container runtime, and resource usage/allocation status.
- **Added** a feature to show the list of pods, labels and annotations, event list, and status on edge nodes
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
- **Added** a feature of updating workloads, including container specifications, access configurations, and deployment configurations.
- **Added** operations of restarting/stopping workloads
- **Added** a feature to view workload event information
- **Added** a feature of deploying applications to edge node groups as images in bulk
- **Added** a feature of creating message routes to allow messages to be forwarded to corresponding endpoints based on configured routing rules
- **Added** the access of Modbus protocol end device to the platform and realized the visual management
- **Added** features of binding and unbinding end devices with registered edge nodes
- **Added** twin properties of adding, modifying, and deleting device
- **Added** support for editing twin properties to change the expected values in the device twin information stored on edge nodes, allowing devices to synchronize and change their status accordingly
- **Added** a feature of adding tags to devices, allowing for querying devices based on multiple tag key-value pairs
- **Added** support for configuring device access settings to obtain device data
- **Added** support for deleting end devices
