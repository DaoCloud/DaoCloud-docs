# MySQL Release Notes

This page lists the Release Notes of the MySQL database, so that you can understand the evolution path and feature changes of each version.

## 2023-04-27

### v0.8.1

#### new function

- **NEW** `mcamel-mysql` details page displays related events
- **NEW** `mcamel-mysql` openapi list interface supports Cluster and Namespace field filtering
- **Add** `mcamel-mysql` custom role
- **Added** `mcamel-mysql` is connected to HwameiStor and supports storage capacity display (you need to manually create HwameiStor exporter ServiceMonitor)

#### upgrade

- **Upgrade** Optimize the scheduling strategy to add a sliding button


## 2023-03-28

### v0.7.0

#### new function

- **NEW** `mcamel-mysql` supports middleware link tracking adaptation.
- **NEW** Install `mcamel-mysql` to enable link tracking according to parameter configuration.
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
- **NEW** `mcamel-mysql` supports cloud shell.
- **NEW** `mcamel-mysql` supports separate registration of navigation bar.
- **NEW** `mcamel-mysql` supports viewing logs.
- **Added** `mcamel-mysql` updated Operator version.
- **NEW** `mcamel-mysql` shows common MySQL in the instance list.
- **NEW** `mcamel-mysql` supports MySQL8.0.29.
- **NEW** `mcamel-mysql` supports LB.
- **NEW** `mcamel-mysql` supports Operator docking with chart-syncer.
- **Added** `mcamel-mysql` Operator finalizers permission to support openshift.
- **NEW** `UI` adds MySQL master-slave replication delay display
- **Added** `Documentation` adds log viewing operation instructions, supports custom query, export and other functions.

#### Optimization

- **Upgrade** `mcamel-mysql` upgrade offline mirror detection script.

#### fix

- **Fix** the problem that `mcamel-mysql` instance name is too long and the custom resource cannot be created.
- **FIXED** `mcamel-mysql` workspace Editor user cannot view instance password.
- **FIXED** Duplicate definition of `expire-logs-days` parameter in `mcamel-mysql` configuration file.
- **FIXED** The binlog expiration time in `mcamel-mysql` 8.0 environment is not as expected.
- **FIXED** `mcamel-mysql` backup set listing would show older backup sets for clusters with the same name.

## 2022-12-25

### v0.5.0

#### new function

- **NEW** Added early detection of NodePort port conflicts.
- **New** node affinity configuration.
- **Add** Bucket can be verified when creating a backup configuration.

- **FIX** The default configuration cannot be displayed in the arm environment.
- **Fix** The name verification is inconsistent with the front end when creating an instance.
- **Fix** After reconnecting to the cluster with changed name, the configuration management address display error.
- **FIX** Failed to save auto backup configuration.
- **FIXED** The problem that the automatic backup set cannot be displayed.

## 2022-11-08

### v0.4.0

### new function

- **NEW** Added MySQL lifecycle management interface function
- **NEW** Added MySQL details interface function
- **Add** docking insight based on grafana crd
- **NEW** Add interface with ghippo service
- **NEW** Add an interface with kpanda
- **NEW** Increased single-test coverage to 30%
- **NEW** Added backup and restore function
- **NEW** Added backup configuration interface
- **NEW** Added backup and restore source field in instance list interface
- **NEW** Add interface to get user list
- **Add** `mysql-operator` chart parameter to specify the metric exporter image
- **New** support arm64 architecture
- **NEW** Added arm64 operator image packaging
- **NEW** Added support for password desensitization
- **NEW** Added support for service exposure as nodeport
- **NEW** Added support for mtls
- **Added** `documentation` first release of documentation website
- **NEW** `documentation` basic concept
- **NEW** `Documentation` Concepts
- **Added** `documentation` for first time use of MySQL
- **NEW** `documentation` delete MySQL instance

#### Optimization

- **Optimize** uniformly adjust the timestamp api field to int64

#### fix

- **Fix** Fix fuzzy search of backup list interface invalid
- **FIX** Fix dependency bug
- **FIXED** After the backup job is deleted, the backup task list cannot be displayed
- **FIXED** The problem that the image cannot be grabbed when it has uppercase and numbers

## 2022-10-18

### v0.3

#### new function

- **NEW** Added MySQL lifecycle management interface function
- **NEW** Added MySQL details interface function
- **Add** docking insight based on grafana crd
- **NEW** Add interface with ghippo service
- **NEW** Add an interface with kpanda
- **NEW** Increased single-test coverage to 30%
- **NEW** Added backup and restore function
- **NEW** Added backup configuration interface
- **NEW** Added backup and restore source field in instance list interface
- **Fix** Fix fuzzy search of backup list interface invalid
- **Optimize** uniformly adjust the timestamp api field to int64