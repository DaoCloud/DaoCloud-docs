# VirtNest Release Notes

This page provides the release notes for VirtNest (Virtual Machine Containers),
allowing you to understand the evolution path and feature changes of each version.

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

- **Fixed** issue with VNC access not working

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
