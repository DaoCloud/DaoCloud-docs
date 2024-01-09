---
MTPE: windsonsea
date: 2024-01-09
---

# Release Notes

This page lists the release notes for Cloud Edge Collaboration, providing an overview
of the evolution path and feature changes in each version.

## 2023-12-06

### v0.6.1

#### New Features

- **Added** support for custom terminal device access, compatible with multiple device protocols
- **Added** service capabilities to support edge-to-edge communication
- **Added** support for viewing container log information

#### Improvements

- **Improved** interaction for setting component Helm repository when creating edge units
- **Improved** interaction for setting edge component image repository address when creating batch tasks
- **Added** support for editing and deleting edge units in the "In Progress" state

#### Fixes

- **Fixed** an issue where the default image repository for edge units created in the cloud-edge collaboration installed via the installer was set to "release"
- **Fixed** an issue with abnormal edge unit status determination due to the addition of edge components

## 2023-11-06

### v0.5.0

- **Added** support for creating multiple edge units, allowing expansion of a workspace cluster with additional edge units.
- **Added** customizable settings for KubeEdge image repository, KubeEdge Helm repository, and system component image repository.
- **Added** ability to modify the NodePort port exposed by CloudCore for edge access.
- **Added** editing capabilities for edge units, including modifying basic information, component repository settings, and access settings.
- **Added** support for deleting edge units.
- **Added** overview of edge units, including basic information, component repository settings, access settings, and resource status information.
- **Added** bulk registration of x86_64 and arm64 architecture edge computing machines as edge nodes.
- **Added** configuration options for node driver mode, CRI service address, and KubeEdge image repository.
- **Added** support for edge node labeling, allowing quick filtering of nodes that edge applications want to schedule based on labels.
- **Added** installation and management of nodes using token (valid for 24 hours) or certificate (long-term validity).
- **Added** display registered edge nodes, including node name, status, labels, CPU/memory (allocation/utilization), IP address, etc.
- **Added** search functionality for edge node names.
- **Added** pause/resume scheduling of edge nodes.
- **Added** Removal of edge nodes.
- **Added** overview of edge node details, including Kubelet version, operating system, container runtime, resource usage/allocation status, etc.
- **Added** list of pods, labels and annotations, events, and status on edge nodes.
- **Added** display registered edge node groups and support for searching by group name.
- **Added** editing and deletion of edge node groups.
- **Added** specific edge nodes to edge node groups.
- **Added** filtering edge nodes to edge node groups based on labels.
- **Added** applications deployment to edge nodes using image-based deployment.
- **Added** workload creation using YAML.
- **Added** support for multiple image pulling strategies to meet different operational requirements
  during application restarts.
- **Added** configuration of CPU/memory quotas, including request and limit values.
- **Added** configuration of workload lifecycle, health checks, environment variables, data storage,
  and security settings.
- **Added** labels and annotations to workloads.
- **Added** support for multiple network access methods for workloads, including port mapping, host network,
  and non-accessible modes.
- **Added** container console support.
- **Added** container logs.
- **Added** YAML configurations.
- **Added** the capability of update workloads, including container specifications, access configurations,
  and deployment configurations.
- **Added** support for restarting/stopping workloads.
- Modify workload labels and annotations.
- **Added** support for deleting workloads.
- **Added**  basic information for deployed workloads, such as workload name, alias, status, namespace, etc.
- **Added** pods list for deployed workloads.
- **Added** displaying and editing container configuration information for deployed workloads,
  including container specifications, health checks, environment variables, and storage settings.
- **Added** displaying and editing node scheduling information for deployed workloads.
- **Added** displaying and editing labels and annotations for deployed workloads.
- **Added** displaying and editing access configuration information for deployed workloads, such as network type.
- **Added** displaying event lists for deployed workloads.
- **Added** bulk deployment of applications to edge node groups using image-based deployment.
- **Added** batch deployments using YAML.
- **Added** differentiated configuration of workload instances and container images for different node groups.
- **Added** displaying and editing batch deployment definitions.
- **Added** deletion of deployed workload instances.
- **Added** creating and deleting configmaps and keys using forms and YAML, decoupling configmaps and
  encrypted files from container images to enhance portability of container workloads.
- **Added** Updating, exporting, and deleting configmaps and keys for easy management of configuration files.
- **Added** creating and deletingmessage endpoints.
- **Added** creating message routes, allowing messages to be forwarded to corresponding endpoints
  based on configured routing rules.
- **Added** deleting message routes.
- **Added** support for Modbus protocol end device integration and visualization management.
- **Added** binding and unbinding end device with registered edge nodes.
- **Added** features of adding, modifying, and deleting device twin properties.
- **Added** editing device twin properties to change expected values stored in device twin information
  on edge nodes, allowing device to synchronize changes with twin information.
- **Added** tags to device for querying device based on multiple tag key-value pairs.
- **Added** device access configurations for retrieving device data.
- **Added** support for deleting end device.
- **Added** display of basic information for registered device, such as device name, access protocol, namespace, etc.
- **Added** support for displaying and editing end device twin properties, tags, and access configuration information.
