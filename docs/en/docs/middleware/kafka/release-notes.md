# Kafka message queue Release Notes

This page lists the Release Notes of Kafka message queue, so that you can understand the evolution path and feature changes of each version.

### 2023-10-31

#### v0.9.0

##### Enhancements

- **New Feature:** Added offline upgrade functionality.
- **New Feature:** Added restart functionality for instances.
- **Bug Fix:** Fixed cloudshell permissions issue.

## 2023-08-31

### v0.8.0

#### New Features

- **Added** Whitelist access control.

#### Improvements

- **Improved** Syntax compatibility for KindBase.
- **Improved** Page display during operator creation process.

## 2023-07-31

### v0.7.3

#### New Features

- **Added** Access restrictions for UI interface.

## 2023-06-30

### v0.7.0

#### New Features

- **Added**: Integrated with the global management audit log module.
- **Added**: Added support for `LoadBalancer` service type.

#### Improvements

- **Improved**: Removed interfering elements and added time range selection to monitoring charts.
- **Improved**: Closed-loop installation of `ServiceMonitor`.

## 2023-04-27

### v0.5.1

#### New features

- **Added** `mcamel-kafka` details page displays related events
- **Added** `mcamel-kafka` supports custom roles

#### Optimization

- **Optimized** `mcamel-kafka` scheduling strategy adds a sliding button

## 2023-03-28

### v0.4.0

#### New features

- **Added** `mcamel-kafka` supports middleware traces adaptation.
- **Added** Install `mcamel-kafka` to enable traces according to parameter configuration.

#### Optimization

- **Optimized** `mcamel-kafka` optimizes Kafka's default configuration.
- **upgrade** golang.org/x/net to v0.7.0
- **Upgrade** GHippo SDK to v0.14.0

## 2023-02-23

### v0.3.0

#### New features

- **Added** `mcamel-kafka` helm-docs template file.
- **Added** The Operator in the `mcamel-kafka` app store can only be installed in mcamel-system.
- **Added** `mcamel-kafka` supports cloud shell.
- **Added** `mcamel-kafka` supports separate registration of navigation bar.
- **Added** `mcamel-kafka` supports viewing logs.
- **Added** `mcamel-kafka` Operator docking with chart-syncer.

#### Optimization

- **Optimized** `mcamel-kafka` upgrade offline mirror detection script.

#### fix

- **Fixed** the problem that `mcamel-kafka` instance name is too long and the custom resource cannot be created.
- **Fixed** `mcamel-kafka` workspace Editor user cannot view instance password.
- **Added** log view operation instructions, support custom query, export and other features.

## 2022-12-25

### v0.2.0

#### New features

- **Added** `mcamel-kafka` NodePort port conflict early detection.
- **Added** `mcamel-kafka` node affinity configuration.

#### Optimization

- **Optimized** `mcamel-kafka` manager removes the probe to prevent kafka from being unable to open the manager when it is not ready.
- **Optimized** `mcamel-kafka` zooEntrance repackage mirror address to 1.0.0.

## 2022-11-28

### v0.1.6

#### New features

- **Optimized** Improve and optimize the copy function
- **Optimized** instance details - access settings, remove cluster IPv4
- **Optimized** Middleware password verification difficulty adjustment
- **Added** Docking alert capability
- **Added** Added the feature of judging whether sc supports capacity expansion and prompting in advance
- **Optimized** Optimize the prompt logic of installation environment check & adjust its style
- **Optimized** middleware style walkthrough optimization
- **Fixed** The offline image has numbers and capital letters that cannot be scanned

## 2022-11-08

### v0.1.4

#### New features

- **Fixed** The correct field cannot be verified when updating, such as managerPass
- **Optimized** Password validation adjusted to MCamel low password strength
- **Added** Returns whether the sc capacity can be updated
- **Added** public field when returning list or details
- **Added** Added return alert
- **Added** Validation Service annotation
- **Fixed** operator select by name
- **Fixed** service address display error
- **Fixed** When Kafka uses NodePort, the creation fails

## 2022-10-28

### v0.1.2

#### New features

- **Added** Sync Pod status to instance details page
- **Optimized** workspace interface logic adjustment
- **Optimized** Style adjustments that do not conform to design specifications
- **Optimized** password acquisition logic adjustment
- **Optimized** cpu&memory request amount should be less than limit logic adjustment

## 2022-9-25

### v0.1.1

#### New features

- **Added** supports kafka list query, status query, creation, deletion and modification
- **Added** Support kafka-manager to manage kafka
- **Added** Support kafka metric monitoring, check the monitoring chart
- **Added** support for ghippo permission linkage
- **Added** `mcamel-elasticsearch` interface to get user list
- **Optimized** Update the release note script and run the release-process specification