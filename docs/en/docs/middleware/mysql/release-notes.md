# MySQL Release Notes

This page lists the Release Notes of the MySQL database, so that you can understand the evolution path and feature changes of each version.

## 2023-03-28

### v0.7.0

#### Features

- **Added** `mcamel-mysql` supports middleware link tracking adaptation.
- **Added** Install `mcamel-mysql` to enable link tracking according to parameter configuration.
- **Added** `mcamel-mysql` PhpMyAdmin supports LoadBalancer type.

#### upgrade

- **upgrade** golang.org/x/net to v0.7.0
- **Upgrade** GHippo SDK to v0.14.0
- **optimization** `mcamel-mysql` common-mysql supports multiple instance optimization.
- **Optimize** `mcamel-mysql` troubleshooting manual adds more processing methods.

## 2023-02-23

### v0.6.0

### new function

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
- **Added** `Documentation` adds log viewing operation instructions, supports custom query, export and other functions.

#### Optimization

- **Upgrade** `mcamel-mysql` upgrade offline mirror detection script.

#### Fix

- **Fixed** the problem that `mcamel-mysql` instance name is too long and the custom resource cannot be created.
- **Fixed** `mcamel-mysql` workspace Editor user cannot view instance password.
- **Fixed** Duplicate definition of `expire-logs-days` parameter in `mcamel-mysql` configuration file.
- **Fixed** The binlog expiration time in `mcamel-mysql` 8.0 environment is not as expected.
- **Fixed** `mcamel-mysql` backup set listing would show older backup sets for clusters with the same name.

## 2022-12-25

### v0.5.0

#### Features

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

### new function

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

- **Optimize** uniformly adjust the timestamp api field to int64

#### Fix

- **Fixed** Fix fuzzy search of backup list interface invalid
- **Fixed** Fix dependency bug
- **Fixed** After the backup job is deleted, the backup task list cannot be displayed
- **Fixed** The problem that the image cannot be grabbed when it has uppercase and numbers

## 2022-10-18

### v0.3

#### Features

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
- **Optimize** uniformly adjust the timestamp api field to int64