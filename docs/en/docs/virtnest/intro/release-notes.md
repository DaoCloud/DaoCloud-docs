---
MTPE: windsonsea
Date: 2024-10-10
---

# VirtNest Release Notes

This page provides the release notes for VirtNest (Virtual Machine),
allowing you to understand the evolution path and feature changes of each version.

## 2025-07-30

### v0.18.1

* **Added** IP search support for the virtual machine list API.
* **Optimized** VirtNest integration with Insight (`metrics`, `log`, `otel tracing`) to meet development best practices.
* **Optimized** support for scheduled snapshots and snapshot backup restoration of virtual machines using scripts and documentation.
* **Fixed** error occurring during batch creation of virtual machines.

## 2025-04-30

### v0.17.0

- **Upgraded** user experience for GPU selection.

## 2025-02-28

### v0.16.0

- **Added** status prompts for real-time VM migration.  
- **Added** UI prompts indicating whether storage supports hot-plugging.  
- **Fixed** an issue where the image address was empty during cold migration within the VM cluster.  
- **Fixed** an incorrect disk count in the VM overview.

## 2024-11-30

### v0.15.0

- **Added** support for semi-automated Muxi GPU configuration.  
- **Added** snapshot management.  
- **Added** a VM monitoring overview.  
- **Fixed** an issue where VM network interfaces went down after reboot.  
- **Fixed** VM creation failures when using GPU.

## 2024-10-31

### v0.14.0

- **Upgraded** VirtNest Agent to v0.8.0.  
- **Fixed** an error when creating VMs with GPUs.  
- **Fixed** an issue where VM disks could not be expanded.

## 2024-09-30

### v0.13.0

#### Features

- **Added** support for updating virtual machine networks.
- **Added** support for cold migration of virtual machines within the cluster.

#### Fixes

- **Fixed** an issue where the system disk was empty when creating a virtual machine from a template.
- **Fixed** a display issue when the image source for a virtual machine created from a template was set to HTTP.
- **Fixed** an issue where CPU monitoring for virtual machines did not display.
- **Fixed** an issue where the VNC interface could not be opened when the kpanda version was above v0.29.

## 2024-8-31

### v0.12.0

- **Added** the hot resizing feature of virtual machine disks.
- **Added** backend support for cold migration of virtual machines.
- **Fixed** an issue of no data for CPU monitoring.
- **Fixed** an issue when hot migrating a virtual machine without specifying a node.

## 2024-07-31

### v0.11.0

- **Added** a feature of hot-adding disks to virtual machines.
- **Fixed** a bug when creating virtual machines from templates.
- **Fixed** an issue of snapshot restoration failure.
- **Fixed** display issues with snapshot and clone menus.

## 2024-06-30

### v0.10.0

- **Added** a feature of real-time updates of virtual machine memory and CPU.
- **Added** a feature of real-time migration of virtual machines to specified nodes.
- **Added** a feature of updating GPU information of virtual machines.
- **Upgraded** KubeVirt component to version 1.2.2.
- **Fixed** issues with errors when starting virtual machines created through built-in templates.

## 2024-05-30

### v0.9.0

- **Added** support for directly updating versions in the Helm application interface
  for the virtual machine module.
- **Fixed** an issue where creating a virtual machine via YAML configuration would fail
  due to user information parsing errors.
- **Fixed** abnormal calculations in virtual machine resource monitoring.

## 2024-04-30

### v0.8.1

- **Added** GPU information in the details of virtual machines and virtual machine templates.
- **Improved** the performance of the virtual machine list.
- **Fixed** issues with using the bridge network mode for virtual machines.

## 2024-3-26

### v0.7.0

- **Added** GPU configuration support for virtual machines
- **Added** OpenAPI documentation to the documentation site
- **Added** integration with audit logs
- **Improved** inheritance of network and storage information from the template
  when creating virtual machines through a VM template
- **Fixed** inaccurate memory usage rate in virtual machine monitoring

## 2024-01-26

### v0.6.0

#### Features

- **Added** support for importing virtual machines from VMware into the virtual machine module of DCE 5.0
- **Added** IPv6 pool for virtual machine networks
- **Added** support for configuring network information when creating virtual machines from templates

#### Improvements

- **Improved** monitoring information in virtual machine details
- **Improved** prompt message for configuring storage when creating virtual machines

#### Fixes

- **Fixed** an issue where network configuration information was displayed incorrectly when virtual machine was powered off
- **Fixed** incorrect position for creating Multus CR in network configuration prompt message
  when creating virtual machines
- **Fixed** an issue where powered-off virtual machines could not be updated

## 2023-12-26

### v0.5.0

- **Added** support for richer network configurations for virtual machines, such as multi-NIC capability
- **Added** monitoring information to virtual machine details
- **Improved** response speed for virtual machine list
- **Improved** the sorting of the virtual machine template list
- **Fixed** an issue of possible failure to retrieve kubevirt client

## 2023-11-30

### v0.4.0

- **Upgraded** KubeVirt to 1.0.0
- **Improved** virtual machine details with additional information such as username, password, CPU, and memory
- **Fixed** occasional issue with not seeing virtual machine monitoring data on the dashboard

## 2023-10-31

### v0.3.0

- **Added** support for live migration
- **Added** support for accessing virtual machines via terminal
- **Added** support for editing virtual machines with YAML
- **Added** support for adding data disks to virtual machines
- **Added** support for selecting images from container registries to create virtual machines
- **Added** support for creating virtual machines from templates
- **Added** support for converting virtual machine configurations into templates
- **Added** support for deleting custom templates
- **Added** support for custom operating systems
- **Improved** sorting of virtual machine list
- **Fixed** an issue with VNC access not working

## 2023-8-31

### v0.2.0

- **Added** support for restarting virtual machines.
- **Added** support for editing virtual machines using forms.
- **Added** support for creating virtual machines using YAML.
- **Added** support for cloning virtual machines.
- **Added** support for creating snapshots of virtual machines.
- **Added** support for restoring virtual machines from snapshots and displaying restore records.

## 2023-07-31

### v0.1.0

- **Added** support for displaying a list of virtual machines through the cluster
- **Added** support for creating virtual machines using container images
- **Added** support for powering off/starting virtual machines
- **Added** support for deleting virtual machines
- **Added** support for accessing virtual machines via the console (VNC)
- **Added** support for viewing virtual machine details
