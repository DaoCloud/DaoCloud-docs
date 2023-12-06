# Release Notes

This page lists the release notes for Cloud Edge Collaboration, providing an overview of the evolution path and feature changes in each version.

## 2023-12-06

### v0.6.1

#### New Features

- Added support for custom terminal device access, compatible with multiple device protocols
- Provided service capabilities to support edge-to-edge communication
- Added support for viewing container log information

#### Improvements

- Optimized interaction for setting component Helm repository when creating edge units
- Optimized interaction for setting edge component image repository address when creating batch tasks
- Supported editing and deleting edge units in the "In Progress" state

#### Fixes

- Fixed issue where the default image repository for edge units created in the cloud-edge collaboration installed via the installer was set to "release"
- Fixed issue with abnormal edge unit status determination due to the addition of edge components

## 2023-11-06

### v0.5.0

#### New Features

- Support for creating multiple edge units, allowing expansion of a workspace cluster with additional edge units.
- Customizable settings for KubeEdge image repository, KubeEdge Helm repository, and system component image repository.
- Ability to modify the NodePort port exposed by CloudCore for edge access.
- Editing capabilities for edge units, including modifying basic information, component repository settings, and access settings.
- Support for deleting edge units.
- Overview of edge units, including basic information, component repository settings, access settings, and resource status information.
- Bulk registration of x86_64 and arm64 architecture edge computing machines as edge nodes.
- Configuration options for node driver mode, CRI service address, and KubeEdge image repository.
- Support for edge node labeling, allowing quick filtering of nodes that edge applications want to schedule based on labels.
- Installation and management of nodes using token (valid for 24 hours) or certificate (long-term validity).
- Display of registered edge nodes, including node name, status, labels, CPU/memory (allocation/utilization), IP address, etc.
- Search functionality for edge node names.
- Pause/resume scheduling of edge nodes.
- Removal of edge nodes.
- Overview of edge node details, including Kubelet version, operating system, container runtime, resource usage/allocation status, etc.
- List of container groups, labels and annotations, events, and status on edge nodes.
- Display of registered edge node groups and support for searching by group name.
- Editing and deletion of edge node groups.
- Adding specific edge nodes to edge node groups.
- Filtering edge nodes to edge node groups based on labels.
- Deployment of applications to edge nodes using image-based deployment.
- Creation of workloads using YAML.
- Support for multiple image pulling strategies to meet different operational requirements during application restarts.
- Configuration of CPU/memory quotas, including request and limit values.
- Configuration of workload lifecycle, health checks, environment variables, data storage, and security settings.
- Addition of labels and annotations to workloads.
- Support for multiple network access methods for workloads, including port mapping, host network, and non-accessible modes.
- Container console support.
- Viewing container logs.
- Editing YAML configurations.
- Updating workloads, including container specifications, access configurations, and deployment configurations.
- Restarting/stopping workloads.
- Modifying workload labels and annotations.
- Deleting workloads.
- Display of basic information for deployed workloads, such as workload name, alias, status, namespace, etc.
- Listing of container groups for deployed workloads.
- Display and editing of container configuration information for deployed workloads, including container specifications, health checks, environment variables, and storage settings.
- Display and editing of node scheduling information for deployed workloads.
- Display and editing of labels and annotations for deployed workloads.
- Display and editing of access configuration information for deployed workloads, such as network type.
- Display of event lists for deployed workloads.
- Bulk deployment of applications to edge node groups using image-based deployment.
- Creation of batch deployments using YAML.
- Differentiated configuration of workload instances and container images for different node groups.
- Display and editing of batch deployment definitions.
- Deletion of deployed workload instances.
- Creation and deletion of configuration items and keys using forms and YAML, decoupling configuration items and encrypted files from container images to enhance portability of container workloads.
- Updating, exporting, and deleting configuration items and keys for easy management of configuration files.
- Creation and deletion of message endpoints.
- Creation of message routes, allowing messages to be forwarded to corresponding endpoints based on configured routing rules.
- Deletion of message routes.
- Support for Modbus protocol end device integration and visualization management.
- Binding and unbinding of end device with registered edge nodes.
- Addition, modification, and deletion of device twin properties.
- Editing of device twin properties to change expected values stored in device twin information on edge nodes, allowing device to synchronize changes with twin information.
- Adding tags to device for querying device based on multiple tag key-value pairs.
- Setting device access configurations for retrieving device data.
- Deletion of end device.
- Display of basic information for registered device, such as device name, access protocol, namespace, etc.
- Display and editing of end device twin properties, tags, and access configuration information.