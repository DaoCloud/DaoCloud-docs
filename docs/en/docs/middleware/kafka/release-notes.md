# Kafka message queue Release Notes

This page lists the Release Notes of Kafka message queue, so that you can understand the evolution path and feature changes of each version.

## 2023-03-28

### v0.4.0

#### Features

- **Added** `mcamel-kafka` supports middleware link tracking adaptation.
- **Added** Install `mcamel-kafka` to enable link tracking according to parameter configuration.

#### Optimization

- **Optimize** `mcamel-kafka` optimizes Kafka's default configuration.
- **upgrade** golang.org/x/net to v0.7.0
- **Upgrade** GHippo SDK to v0.14.0

## 2023-02-23

### v0.3.0

#### Features

- **Added** `mcamel-kafka` helm-docs template file.
- **Added** The Operator in the `mcamel-kafka` app store can only be installed in mcamel-system.
- **Added** `mcamel-kafka` supports cloud shell.
- **Added** `mcamel-kafka` supports separate registration of navigation bar.
- **Added** `mcamel-kafka` supports viewing logs.
- **Added** `mcamel-kafka` Operator docking with chart-syncer.

#### Optimization

- **Optimize** `mcamel-kafka` upgrade offline mirror detection script.

#### Fix

- **Fixed** the problem that `mcamel-kafka` instance name is too long and the custom resource cannot be created.
- **Fixed** `mcamel-kafka` workspace Editor user cannot view instance password.
- **Added** log view operation instructions, support custom query, export and other functions.

## 2022-12-25

### v0.2.0

#### Features

- **Added** `mcamel-kafka` NodePort port conflict early detection.
- **Added** `mcamel-kafka` node affinity configuration.

#### Optimization

- **Optimize** `mcamel-kafka` manager removes the probe to prevent kafka from being unable to open the manager when it is not ready.
- **Optimize** `mcamel-kafka` zooEntrance repackage mirror address to 1.0.0.

## 2022-11-28

### v0.1.6

#### Features

- **Optimized** Improve and optimize the copy function
- **Optimized** instance details - access settings, remove cluster IPv4
- **Optimized** Middleware password verification difficulty adjustment
- **Added** Docking alarm capability
- **Added** Added the function of judging whether sc supports capacity expansion and prompting in advance
- **Optimization** Optimize the prompt logic of installation environment detection & adjust its style
- **Optimize** middleware style walkthrough optimization
- **Fixed** The offline image has numbers and capital letters that cannot be scanned

## 2022-11-08

### v0.1.4

#### Features

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

#### Features

- **Added** Sync Pod status to instance details page
- **Optimize** workspace interface logic adjustment
- **Optimization** Style adjustments that do not conform to design specifications
- **Optimized** password acquisition logic adjustment
- **Optimize** cpu&memory request amount should be less than limit logic adjustment

## 2022-9-25

### v0.1.1

#### Features

- **Added** supports kafka list query, status query, creation, deletion and modification
- **Added** Support kafka-manager to manage kafka
- **Added** Support kafka metric monitoring, check the monitoring chart
- **Added** support for ghippo permission linkage
- **Added** `mcamel-elasticsearch` interface to get user list
- **Optimize** Update the release note script and execute the release-process specification