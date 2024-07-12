---
MTPE: windsonsea
Date: 2024-04-24
---

# VirtNest Release Notes

This page provides the release notes for VirtNest (Virtual Machine),
allowing you to understand the evolution path and feature changes of each version.

## 2024-06-30

### v0.10.0

#### Features

- **Added** a feature of real-time updates of virtual machine memory and CPU.
- **Added** a feature of real-time migration of virtual machines to specified nodes.
- **Added** a feature of updating GPU information of virtual machines.

#### Improvements

- **Upgraded** KubeVirt component to version 1.2.2.

#### Fixes

- **Fixed** issues with errors when starting virtual machines created through built-in templates.

## 2024-05-30

### v0.9.0

#### Features

- **Added** Support for directly updating versions in the Helm application interface
  for the virtual machine module.

#### Fixes

- **Fixed** an issue where creating a virtual machine via YAML configuration would fail
  due to user information parsing errors.
- **Fixed** abnormal calculations in virtual machine resource monitoring.

## 2024-04-30

### v0.8.1

#### Features

- **Added** GPU information in the details of virtual machines and virtual machine templates.

#### Improvements

- **Improved** the performance of the virtual machine list.

#### Fixes

- **Fixed** issues with using the bridge network mode for virtual machines.

## 2024-3-26

### v0.7.0

#### Features

- **Added** GPU configuration support for virtual machines
- **Added** OpenAPI documentation to the documentation site
- **Added** integration with audit logs

#### Improvements

- **Improved** inheritance of network and storage information from the template
  when creating virtual machines through a VM template

#### Fixes

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

#### Features

- **Added** support for richer network configurations for virtual machines, such as multi-NIC capability
- **Added** monitoring information to virtual machine details

#### Improvements

- **Improved** response speed for virtual machine list
- **Improved** the sorting of the virtual machine template list

#### Fixes

- **Fixed** an issue of possible failure to retrieve kubevirt client

## 2023-11-30

### v0.4.0

#### Upgrades

- **Upgraded** KubeVirt to 1.0.0

#### Improvements

- **Improved** virtual machine details with additional information such as username, password, CPU, and memory

#### Fixes

- **Fixed** occasional issue with not seeing virtual machine monitoring data on the dashboard

## 2023-10-31

### v0.3.0

#### New Features

- **Added** support for live migration
- **Added** support for accessing virtual machines via terminal
- **Added** support for editing virtual machines with YAML
- **Added** support for adding data disks to virtual machines
- **Added** support for selecting images from image repositories to create virtual machines
- **Added** support for creating virtual machines from templates
- **Added** support for converting virtual machine configurations into templates
- **Added** support for deleting custom templates
- **Added** support for custom operating systems

#### Improvements

- **Improved** sorting of virtual machine list

#### Fixes

- **Fixed** an issue with VNC access not working

## 2023-8-31

### v0.2.0

#### New Features

- **Added** support for restarting virtual machines.
- **Added** support for editing virtual machines using forms.
- **Added** support for creating virtual machines using YAML.
- **Added** support for cloning virtual machines.
- **Added** support for creating snapshots of virtual machines.
- **Added** support for restoring virtual machines from snapshots and displaying restore records.

## 2023-07-31

### v0.1.0

#### New Features

- **Added** support for displaying a list of virtual machines through the cluster
- **Added** support for creating virtual machines using container images
- **Added** support for powering off/starting virtual machines
- **Added** support for deleting virtual machines
- **Added** support for accessing virtual machines via the console (VNC)
- **Added** support for viewing virtual machine details
