# MySQL Release Notes

This page lists the Release Notes of the MySQL database, so that you can understand the evolution path and feature changes of each version.

## 2023-11-30

### v0.13.0

#### Improvements

- **Added** support for recording operation audit logs
- **Improved** prompt when instance list information is not obtained
- **Improved** display of Mcamel-MySQL monitoring dashboard in both Chinese and English

## 2023-10-31

### v0.12.0

#### Improvements

- **New** Added offline upgrade functionality.
- **New** Added restart functionality for instances.
- **New** Added workload anti-affinity configuration.
- **New** Added cross-cluster recovery for instances.
- **Bug Fix** Fixed Pod list display to show Host IP.
- **Bug Fix** Fixed cloudshell permissions issue.

## 2023-08-31

### v0.11.0

#### New Features

- **Added** Parameter template functionality.

#### Improvements

- **Improved** Syntax compatibility for KindBase.
- **Improved** Page display during operator creation process.

## 2023-07-31

### v0.10.3

#### New Features

- **Added** Access restrictions for UI interface.

## 2023-06-30

### v0.10.0

#### New Features

- **Optimized** the structure and style display of the backup management page for `mcamel-mysql`.
- **Optimized** the monitoring charts for `mcamel-mysql` by removing distracting elements and adding a time range selection.
- **Optimized** the source of storage capacity metrics for `mcamel-mysql` by using neutral metrics.
- **Optimized** the installation process of `mcamel-mysql` ServiceMonitor.

## 2023-05-30

### v0.9.0

#### New Features

- **Added** integration with the global management audit log module for `mcamel-mysql`.
- **Added** the ability to configure the interval for collecting monitoring data for `mcamel-mysql` instances.
- **Fixed** an issue where Raft cluster couldn't be established properly when installing MySQL Operator with multiple replicas for `mcamel-mysql`.
- **Fixed** the PodDisruptionBudget version to v1 when upgrading MySQL Operator with multiple replicas for `mcamel-mysql`.

## 2023-04-27

### v0.8.1

#### New features

- **Added** `mcamel-mysql` details page displays related events
- **Added** `mcamel-mysql` openapi list interface supports Cluster and Namespace field filtering
- **Added** `mcamel-mysql` custom role
- **Added** `mcamel-mysql` is connected to HwameiStor and supports storage capacity display (you need to manually create HwameiStor exporter ServiceMonitor)

#### Upgrade

- **Upgraded** Optimize the scheduling strategy to add a sliding button

## 2023-03-28

### v0.7.0

#### New features

- **Added** `mcamel-mysql` supports middleware traces adaptation.
- **Added** Install `mcamel-mysql` to enable traces according to parameter configuration.
- **Added** `mcamel-mysql` PhpMyAdmin supports LoadBalancer type.

#### Upgrade

- **Upgraded** golang.org/x/net to v0.7.0
- **Upgraded** GHippo SDK to v0.14.0
- **optimized** `mcamel-mysql` common-mysql supports multiple instance optimization.
- **Optimized** `mcamel-mysql` troubleshooting manual adds more processing methods.

## 2023-02-23

### v0.6.0

### New features

- **Added** `mcamel-mysql` helm-docs template file.
- **Added** The Operator in the `mcamel-mysql` app store can only be installed in mcamel-system.
- **Added** `mcamel-mysql` supports cloud shell.
- **Added** `mcamel-mysql` supports separate registration of navigation bar.
- **Added** `mcamel-mysql` supports viewing logs.
- **Added** `mcamel-mysql` updated Operator version.
- **Added** `mcamel-mysql` shows common MySQL in the instance list.
- **Added** `mcamel-mysql` supports MySQL8.0.29.
- **Added** `mcamel-mysql` supports LB.
- **Added** `mcamel-mysql` supports Operator docking with chart-syncer.
- **Added** `mcamel-mysql` Operator finalizers permission to support openshift.
- **Added** `UI` adds MySQL master-slave replication delay display
- **Added** `Documentation` adds log viewing operation instructions, supports custom query, export and other features.

#### Optimization

- **Upgraded** `mcamel-mysql` upgrade offline mirror detection script.

#### fix

- **Fixed** the problem that `mcamel-mysql` instance name is too long and the custom resource cannot be created.
- **Fixed** `mcamel-mysql` workspace Editor user cannot view instance password.
- **Fixed** Duplicate definition of `expire-logs-days` parameter in `mcamel-mysql` configuration file.
- **Fixed** The binlog expiration time in `mcamel-mysql` 8.0 environment is not as expected.
- **Fixed** `mcamel-mysql` backup set listing would show older backup sets for clusters with the same name.

## 2022-12-25

### v0.5.0

#### New features

- **Added** Added early detection of NodePort port conflicts.
- **Added** node affinity configuration.
- **Added** Bucket can be verified when creating a backup configuration.

- **Fixed** The default configuration cannot be displayed in the arm environment.
- **Fixed** The name verification is inconsistent with the front end when creating an instance.
- **Fixed** After reconnecting to the cluster with changed name, the configuration management address display error.
- **Fixed** Failed to save auto backup configuration.
- **Fixed** The problem that the automatic backup set cannot be displayed.

## 2022-11-08

### v0.4.0

### New features

- **Added** Added MySQL lifecycle management interface function
- **Added** Added MySQL details interface function
- **Added** docking insight based on grafana crd
- **Added** Add interface with ghippo service
- **Added** Add an interface with kpanda
- **Added** Increased single-test coverage to 30%
- **Added** Added backup and restore function
- **Added** Added backup configuration interface
- **Added** Added backup and restore source field in instance list interface
- **Added** Add interface to get user list
- **Added** `mysql-operator` chart parameter to specify the metric exporter image
- **Added** support arm64 architecture
- **Added** Added arm64 operator image packaging
- **Added** Added support for password desensitization
- **Added** Added support for service exposure as nodeport
- **Added** Added support for mtls
- **Added** `documentation` first release of documentation website
- **Added** `documentation` basic concept
- **Added** `Documentation` Concepts
- **Added** `documentation` for first time use of MySQL
- **Added** `documentation` delete MySQL instance

#### Optimization

- **Optimized** uniformly adjust the timestamp api field to int64

#### fix

- **Fixed** Fix fuzzy search of backup list interface invalid
- **Fixed** Fix dependency bug
- **Fixed** After the backup job is deleted, the backup task list cannot be displayed
- **Fixed** The problem that the image cannot be grabbed when it has uppercase and numbers

## 2022-10-18

### v0.3

#### New features

- **Added** Added MySQL lifecycle management interface function
- **Added** Added MySQL details interface function
- **Added** docking insight based on grafana crd
- **Added** Add interface with ghippo service
- **Added** Add an interface with kpanda
- **Added** Increased single-test coverage to 30%
- **Added** Added backup and restore function
- **Added** Added backup configuration interface
- **Added** Added backup and restore source field in instance list interface
- **Fixed** Fix fuzzy search of backup list interface invalid
- **Optimized** uniformly adjust the timestamp api field to int64