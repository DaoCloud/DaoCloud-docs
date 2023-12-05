# Redis Cache Service Release Notes

This page lists the release notes for the Redis Cache service, providing you with information about the evolution and feature changes in each version.

## 2023-11-30

### v0.13.0

#### Improvements

- **Added** support for recording operation audit logs
- **Improved** prompt when instance list information is not obtained
- **Improved** display of Mcamel-Redis monitoring dashboard in both Chinese and English

### 2023-10-31

#### v0.12.0

##### Improvements

- **New** Added offline upgrade functionality.
- **New** Added restart functionality for instances.
- **New** Added parameter template functionality.
- **New** Added cross-cluster recovery for instances.
- **Improved** Optimized the calculation method for master-slave delay.
- **Bug Fix** Fixed cloudshell permissions issue.

## 2023-08-31

### v0.11.0

#### Improvements

- **Improved** Syntax compatibility for KindBase.
- **Improved** Page display during operator creation process.

## 2023-07-31

### v0.10.0

#### New Features

- **Added** access whitelist configuration for `mcamel-redis`.

#### Optimizations

- **Optimized** the creation dialog of `mcamel-redis` instance by adding default anti-affinity label values, simplifying the configuration process.
- **Optimized** the data recovery interface of `mcamel-redis`.
- **Optimized** the display of frontend interface permissions for `mcamel-redis`.

#### Bug Fixes

- **Fixed** failure to close node affinity for `mcamel-redis`.

## 2023-06-30

### v0.9.0

#### New Features

- **Added** the ability to prevent creating Redis instances with the same name under different namespaces for `mcamel-redis`.
- **Added** handling of non-MCamel managed Redis instances to avoid potential misoperations for `mcamel-redis`.
- **Optimized** the structure and style display of the backup management page for `mcamel-redis`.
- **Optimized** the password display in backup jobs for `mcamel-redis`.
- **Optimized** the monitoring charts by removing distracting elements and adding a time range selection for `mcamel-redis`.
- **Optimized** the installation process of `mcamel-redis` ServiceMonitor.

## 2023-05-30

### v0.8.0

#### New Features

- **Added** the ability to configure instance anti-affinity for `mcamel-redis`.
- **Added** integration with the global management audit log module for `mcamel-redis`.
- **Fixed** an issue where backup-related content remained after deleting Redis instances for `mcamel-redis`.
- **Fixed** the incorrect display of Service addresses for sentinel clusters in `mcamel-redis`.

## 2023-04-27

### v0.7.1

#### New Features

- **Added** event display on the details page for `mcamel-redis`.
- **Added** support for filtering by Cluster and Namespace fields in the list API for `mcamel-redis`.
- **Added** custom roles for `mcamel-redis`.

#### Fixes

- **Fixed** sliding button in scheduling strategy optimization for `mcamel-redis`.

## 2023-03-29

### v0.6.2

#### New Features

- **Added** support for automated backup and recovery for `mcamel-redis`.

#### Fixes

- **Fixed** missing export of backup recovery offline images.
- **Fixed** several known issues to improve system stability and security for `mcamel-redis`.

#### Documentation

- **Added** documentation on backup functionality.

## 2023-02-23

### v0.5.0

#### API

- **Added** helm-docs template files for `mcamel-redis`.
- **Added** restriction to install Operator from the application store only in mcamel-system namespace for `mcamel-redis`.
- **Added** support for cloud shell for `mcamel-redis`.
- **Added** separate registration for navigation bar for `mcamel-redis`.
- **Added** support for log viewing for `mcamel-redis`.
- **Added** version updates for singleton/cluster mode Operator for `mcamel-redis`.
- **Added** display of common Redis clusters for `mcamel-redis`.
- **Added** Operator integration with chart-syncer for `mcamel-redis`.
- **Fixed** issue where custom resources couldn't be created due to long instance names for `mcamel-redis`.
- **Fixed** issue where workspace editor users couldn't view instance passwords for `mcamel-redis`.
- **Fixed** issue where the correct Redis version number couldn't be parsed for `mcamel-redis`.
- **Fixed** issue where Port couldn't be modified for `mcamel-redis`.
- **Upgraded** offline image detection script for `mcamel-redis`.

#### Documentation

- **Added** instructions for log viewing, including custom querying and exporting capabilities.

## 2022-12-25

### v0.4.0

#### API

- **Added** early detection of NodePort port conflicts for `mcamel-redis`.
- **Added** configuration for node affinity for `mcamel-redis`.
- **Fixed** issue where setting nodeport for singleton and cluster mode was not effective for `mcamel-redis`.
- **Fixed** issue where setting slave nodes to 0 in cluster mode was not allowed for `mcamel-redis`.

## 2022-11-28

### v0.2.6

#### API

- **Fixed** validation error for certain fields when updating Redis.
- **Improved** password strength to meet MCamel's low-strength password requirement.
- **Improved** the version dependency for sentinel mode, v1.1.1 => v1.2.2, with important change to support k8s 1.25+.
- **Added** support for installing master-slave mode Redis clusters in ARM environments.
- **Added** scaling prompt for sc command.
- **Added** common fields for returning lists or details.
- **Added** return of alarm lists.
- **Added** validation for Service annotations.
- **Fixed** issue with service address display for `mcamel-redis`.

## 2022-10-26

### v0.2.2

#### API

- **Added** the ability to retrieve a list of users.
- **Added** support for ARM architecture.
- **Added** full lifecycle management for Redis instances.
- **Added** deployment of monitoring for Redis instances.
- **Added** support for Redis sentinel, including one-click deployment of singleton and cluster modes.
- **Added** support for WS permission isolation.
- **Added** support for online dynamic scaling.
- **Upgraded** release notes script.
