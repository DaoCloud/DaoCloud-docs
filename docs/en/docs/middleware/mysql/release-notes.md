---
MTPE: windsonsea
date: 2024-01-05
---

# MySQL Release Notes

This page lists the Release Notes of the MySQL database, so that you can understand the evolution path and feature changes of each version.

*[mcamel-mysql]: "mcamel" is the dev name for DaoCloud's middlewares, and "mysql" is a popular relational database

## 2023-12-31

### v0.14.0

- **Added** support for creating instances in group replication mode
- **Fixed** an issue where validation for special characters in input fields was not working when creating instances.

## 2023-11-30

### v0.13.0

- **Added** support for recording operation audit logs
- **Improved** prompt when instance list information is not obtained
- **Improved** display of Mcamel-MySQL monitoring dashboard in both Chinese and English

## 2023-10-31

### v0.12.0

- **Added** offline upgrade functionality
- **Added** restart functionality for instances
- **Added** workload anti-affinity configuration
- **Added** cross-cluster recovery for instances
- **Fixed** Pod list display to show Host IP
- **Fixed** cloudshell permissions issue

## 2023-08-31

### v0.11.0

- **Added** Parameter template functionality
- **Improved** syntax compatibility for KindBase
- **Improved** page display during operator creation process

## 2023-07-31

### v0.10.3

- **Added** access restrictions for UI interface

## 2023-06-30

### v0.10.0

- **Improved** the structure and style display of the backup management page for __mcamel-mysql__ 
- **Improved** the monitoring charts for __mcamel-mysql__ by removing distracting elements and adding a time range selection
- **Improved** the source of storage capacity metrics for __mcamel-mysql__ by using neutral metrics
- **Improved** the installation process of __mcamel-mysql__ ServiceMonitor

## 2023-05-30

### v0.9.0

- **Added** integration with the global management audit log module for __mcamel-mysql__ 
- **Added** the ability to configure the interval for collecting monitoring data for __mcamel-mysql__ instances
- **Fixed** an issue where Raft cluster couldn't be established properly when installing MySQL Operator with multiple replicas for __mcamel-mysql__ 
- **Fixed** the PodDisruptionBudget version to v1 when upgrading MySQL Operator with multiple replicas for __mcamel-mysql__ 

## 2023-04-27

### v0.8.1

- **Added** __mcamel-mysql__ details page displays related events
- **Added** __mcamel-mysql__ openapi list interface supports Cluster and Namespace field filtering
- **Added** __mcamel-mysql__ custom role
- **Added** __mcamel-mysql__ is connected to HwameiStor and supports storage capacity display (you need to manually create HwameiStor exporter ServiceMonitor)
- **Upgraded** Optimize the scheduling strategy to add a sliding button

## 2023-03-28

### v0.7.0

#### New features

- **Added** __mcamel-mysql__ supports middleware traces adaptation
- **Added** Install __mcamel-mysql__ to enable traces according to parameter configuration.
- **Added** __mcamel-mysql__ PhpMyAdmin supports LoadBalancer type

#### Improvements

- **Upgraded** golang.org/x/net to v0.7.0
- **Upgraded** GHippo SDK to v0.14.0
- **Improved** __mcamel-mysql__ common-mysql supports multiple instance optimization
- **Improved** __mcamel-mysql__ troubleshooting manual adds more processing methods

## 2023-02-23

### v0.6.0

### New features

- **Added** __mcamel-mysql__ helm-docs template file
- **Added** The Operator in the __mcamel-mysql__ app store can only be installed in mcamel-system
- **Added** __mcamel-mysql__ supports cloud shell
- **Added** __mcamel-mysql__ supports separate registration of navigation bar
- **Added** __mcamel-mysql__ supports viewing logs
- **Added** __mcamel-mysql__ updated Operator version
- **Added** __mcamel-mysql__ shows common MySQL in the instance list
- **Added** __mcamel-mysql__ supports MySQL 8.0.29
- **Added** __mcamel-mysql__ supports LB
- **Added** __mcamel-mysql__ supports Operator docking with chart-syncer
- **Added** __mcamel-mysql__ Operator finalizers permission to support openshift
- **Added** __UI__ adds MySQL master-slave replication delay display
- **Added** __Documentation__ adds log viewing operation instructions, supports custom query, export and other features
- **Upgraded** __mcamel-mysql__ upgrade offline mirror detection script

#### Fixes

- **Fixed** an issue that __mcamel-mysql__ instance name is too long and the custom resource cannot be created
- **Fixed** __mcamel-mysql__ workspace Editor user cannot view instance password
- **Fixed** Duplicate definition of __expire-logs-days__ parameter in __mcamel-mysql__ configuration file
- **Fixed** The binlog expiration time in __mcamel-mysql__ 8.0 environment is not as expected
- **Fixed** __mcamel-mysql__ backup set listing would show older backup sets for clusters with the same name

## 2022-12-25

### v0.5.0

- **Added** early detection of NodePort port conflicts
- **Added** node affinity configuration
- **Added** Bucket can be verified when creating a backup configuration
- **Fixed** The default configuration cannot be displayed in the arm environment
- **Fixed** The name verification is inconsistent with the front end when creating an instance
- **Fixed** After reconnecting to the cluster with changed name, the configuration management address display error
- **Fixed** an issue of failed to save auto backup configuration
- **Fixed** an issue that the automatic backup set cannot be displayed

## 2022-11-08

### v0.4.0

### New features

- **Added** MySQL lifecycle management interface function
- **Added** MySQL details interface function
- **Added** docking insight based on grafana crd
- **Added** interface with ghippo service
- **Added** an interface with kpanda
- **Added** Increased single-test coverage to 30%
- **Added** backup and restore function
- **Added** backup configuration interface
- **Added** backup and restore source field in instance list interface
- **Added** interface to get user list
- **Added** __mysql-operator__ chart parameter to specify the metric exporter image
- **Added** support arm64 architecture
- **Added** arm64 operator image packaging
- **Added** support for password desensitization
- **Added** support for service exposure as nodeport
- **Added** support for mtls
- **Added** __documentation__ first release of documentation website
- **Added** __documentation__ basic concept
- **Added** __Documentation__ Concepts
- **Added** __documentation__ for first time use of MySQL
- **Added** __documentation__ delete MySQL instance

#### Improvements

- **Improved** uniformly adjust the timestamp api field to int64
- **Fixed** fuzzy search of backup list interface invalid
- **Fixed** dependency bug
- **Fixed** After the backup job is deleted, the backup task list cannot be displayed
- **Fixed** an issue that the image cannot be grabbed when it has uppercase and numbers

## 2022-10-18

### v0.3

- **Added** MySQL lifecycle management interface function
- **Added** MySQL details interface function
- **Added** docking insight based on grafana crd
- **Added** interface with ghippo service
- **Added** an interface with kpanda
- **Added** Increased single-test coverage to 30%
- **Added** backup and restore function
- **Added** backup configuration interface
- **Added** backup and restore source field in instance list interface
- **Fixed** fuzzy search of backup list interface invalid
- **Improved** uniformly adjust the timestamp api field to int64
