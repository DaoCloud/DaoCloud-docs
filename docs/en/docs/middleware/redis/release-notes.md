---
MTPE: windsonsea
date: 2024-01-05
---

# Redis Cache Service Release Notes

This page lists the release notes for the Redis Cache service, providing you with information about the evolution and feature changes in each version.

*[mcamel-redis]: "mcamel" is the dev name for DaoCloud's middlewares, and "redis" is the middleware that provides memory cache services

## 2024-03-31

### v0.16.0

- **Added** Redis slow query analysis
- **Improved** support for enabling hostnetwork in Redis Sentinel mode
- **Improved** prevention of reading Redis password when user permissions are insufficient
- **Improved** Redis Sentinel mode Operator upgrade
- **Fixed** issue with creating more than 3 replicas in Redis Sentinel mode (requires Operator upgrade)
- **Fixed** potential unavailability issues after a Redis Sentinel mode master crash (requires Operator upgrade)
- **Fixed** default backup path set to `name.rdb`
- **Fixed** incorrect memory usage rate in Redis Sentinel mode monitoring dashboard

## 2024-01-31

### v0.15.0

#### Improvements

- **Improved** Redis Operator version upgrade to 6.2.12
- **Improved** addition of Redis version display in global management
- **Fixed** Redis cluster mode scaling not taking effect (requires Operator upgrade)
- **Fixed** support for NodePort access in Redis cluster mode (requires Operator upgrade)

## 2023-12-31

### v0.14.0

- **Added** Built-in alarm rules for Redis
- **Improved** Redis Sentinel mode to return multiple NodePort addresses for sentinels when using NodePort mode
- **Fixed** an issue where validation for input fields with special characters was not effective when creating an instance

## 2023-11-30

### v0.13.0

- **Added** support for recording operation audit logs
- **Improved** prompt when instance list information is not obtained
- **Improved** display of Mcamel-Redis monitoring dashboard in both Chinese and English

### 2023-10-31

#### v0.12.0

- **Added** offline upgrade functionality
- **Added** restart functionality for instances
- **Added** parameter template functionality
- **Added** cross-cluster recovery for instances
- **Improved** Optimized the calculation method for master-slave delay
- **Fixed** cloudshell permissions issue

## 2023-08-31

### v0.11.0

- **Improved** syntax compatibility for KindBase
- **Improved** page display during operator creation process

## 2023-07-31

### v0.10.0

- **Added** access whitelist configuration for __mcamel-redis__ 
- **Improved** the creation dialog of __mcamel-redis__ instance by adding default anti-affinity label values, simplifying the configuration process
- **Improved** the data recovery interface of __mcamel-redis__ 
- **Improved** the display of frontend interface permissions for __mcamel-redis__ 
- **Fixed** failure to close node affinity for __mcamel-redis__ 

## 2023-06-30

### v0.9.0

#### New features

- **Added** the ability to prevent creating Redis instances with the same name under different namespaces for __mcamel-redis__ 
- **Added** handling of non-MCamel managed Redis instances to avoid potential misoperations for __mcamel-redis__ 
- **Improved** the structure and style display of the backup management page for __mcamel-redis__ 
- **Improved** the password display in backup jobs for __mcamel-redis__ 
- **Improved** the monitoring charts by removing distracting elements and adding a time range selection for __mcamel-redis__ 
- **Improved** the installation process of __mcamel-redis__ ServiceMonitor

## 2023-05-30

### v0.8.0

- **Added** the ability to configure instance anti-affinity for __mcamel-redis__ 
- **Added** integration with the global management audit log module for __mcamel-redis__ 
- **Fixed** an issue where backup-related content remained after deleting Redis instances for __mcamel-redis__ 
- **Fixed** the incorrect display of Service addresses for sentinel clusters in __mcamel-redis__ 

## 2023-04-27

### v0.7.1

- **Added** event display on the details page for __mcamel-redis__ 
- **Added** support for filtering by Cluster and Namespace fields in the list API for __mcamel-redis__ 
- **Added** custom roles for __mcamel-redis__ 
- **Fixed** sliding button in scheduling strategy optimization for __mcamel-redis__ 

## 2023-03-29

### v0.6.2

- **Added** support for automated backup and recovery for __mcamel-redis__ 
- **Fixed** missing export of backup recovery offline images
- **Fixed** several known issues to improve system stability and security for __mcamel-redis__ 
- **Added** documentation on backup functionality

## 2023-02-23

### v0.5.0

- **Added** helm-docs template files for __mcamel-redis__ 
- **Added** restriction to install Operator from the application store only in mcamel-system namespace for __mcamel-redis__ 
- **Added** support for cloud shell for __mcamel-redis__ 
- **Added** separate registration for navigation bar for __mcamel-redis__ 
- **Added** support for log viewing for __mcamel-redis__ 
- **Added** version updates for singleton/cluster mode Operator for __mcamel-redis__ 
- **Added** display of common Redis clusters for __mcamel-redis__ 
- **Added** Operator integration with chart-syncer for __mcamel-redis__ 
- **Fixed** issue where custom resources couldn't be created due to long instance names for __mcamel-redis__ 
- **Fixed** issue where workspace editor users couldn't view instance passwords for __mcamel-redis__ 
- **Fixed** issue where the correct Redis version number couldn't be parsed for __mcamel-redis__ 
- **Fixed** issue where Port couldn't be modified for __mcamel-redis__ 
- **Upgraded** offline image detection script for __mcamel-redis__ 
- **Added** instructions for log viewing, including custom querying and exporting capabilities

## 2022-12-25

### v0.4.0

- **Added** early detection of NodePort port conflicts for __mcamel-redis__ 
- **Added** configuration for node affinity for __mcamel-redis__ 
- **Fixed** issue where setting nodeport for singleton and cluster mode was not effective for __mcamel-redis__ 
- **Fixed** issue where setting slave nodes to 0 in cluster mode was not allowed for __mcamel-redis__ 

## 2022-11-28

### v0.2.6

- **Fixed** validation error for certain fields when updating Redis
- **Improved** password strength to meet MCamel's low-strength password requirement
- **Improved** the version dependency for sentinel mode, v1.1.1 => v1.2.2, with important change to support k8s 1.25+
- **Added** support for installing master-slave mode Redis clusters in ARM environments
- **Added** scaling prompt for sc command
- **Added** common fields for returning lists or details
- **Added** return of alarm lists
- **Added** validation for Service annotations
- **Fixed** issue with service address display for __mcamel-redis__ 

## 2022-10-26

### v0.2.2

- **Added** the ability to retrieve a list of users
- **Added** support for ARM architecture
- **Added** full lifecycle management for Redis instances
- **Added** deployment of monitoring for Redis instances
- **Added** support for Redis sentinel, including one-click deployment of singleton and cluster modes
- **Added** support for WS permission isolation
- **Added** support for online dynamic scaling
- **Upgraded** release notes script
