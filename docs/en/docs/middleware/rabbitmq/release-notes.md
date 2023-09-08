# RabbitMQ Release Notes

This page lists the Release Notes of the RabbitMQ message queue, so that you can understand the evolution path and feature changes of each version.

## 2023-08-31

### v0.13.0

#### Improvements

- **Improved** Syntax compatibility for KindBase.
- **Improved** Page display during operator creation process.
- **Improved** Added default anti-affinity configuration on the creation page.

## 2023-07-31

### v0.12.3

#### New Features

- **Added** workload anti-affinity capability.
- **Added** access restrictions for UI interface permissions.

## 2023-06-30

### v0.11.0

#### New Features

- **Added** `LoadBalancer` service type.

#### Optimization

- **Optimized** the monitoring charts by removing distracting elements and adding a time range selection.

## 2023-04-27

### v0.10.1

#### New features

- **Added** `mcamel-rabbitmq` details page displays related events
- **Added** `mcamel-rabbitmq` supports custom roles
- **Added** `mcamel-rabbitmq` supports access traces

#### Optimization

- **Optimized** `mcamel-rabbitmq` scheduling strategy adds a sliding button

## 2023-03-30

### v0.9.1

#### Optimization

- **Optimized** `mcamel-rabbitmq` improves Operator image to speed up addresses.

## 2023-03-28

### v0.9.0

#### New features

- **Added** `mcamel-rabbitmq` supports middleware traces adaptation.
- **Added** Enable traces according to parameter configuration when installing `mcamel-rabbitmq`.

## 2023-02-23

### v0.8.0

#### New features

- **Added** `mcamel-rabbitmq` helm-docs template file.
- **Added** The Operator in the `mcamel-rabbitmq` app store can only be installed in mcamel-system.
- **Added** `mcamel-rabbitmq` supports cloud shell.
- **Added** `mcamel-rabbitmq` supports separate registration of navigation bar.

- **Added** log view operation instructions, support custom query, export and other features.

#### upgrade

- **Upgrade** `mcamel-rabbitmq` upgrade offline mirror detection script.

#### fix

- **Added** `mcamel-rabbitmq` supports viewing logs.
- **Fixed** the problem that `mcamel-rabbitmq` instance name is too long and the custom resource cannot be created.
- **Fixed** `mcamel-rabbitmq` workspace Editor user cannot view instance password.

## 2022-12-25

### v0.7.0

#### New features

- **Added** `mcamel-rabbitmq` NodePort port conflict detection in advance.
- **Added** `mcamel-rabbitmq` node affinity configuration.

#### Optimization

- **Optimized** `mcamel-rabbitmq-ui` middleware style walkthrough optimization.

## 2022-11-28

### v0.6.4

#### New features

- **Added** Add interface to get user list
- **Added** supports multi-architecture images, the configuration method is `depend.arm64-img.rabbitClusterImageFormat: xxxx`
- **Added** supports sc expansion interception, when sc does not support expansion, directly intercept it
- **Added** public field when returning list or details
- **Added** return alerts
- **Added** Validation Service annotation

#### Optimization

- **Optimized** Password verification is adjusted to MCamel medium password strength

#### fix

- **Fixed** page console may access wrong port

## 2022-10-27

### v0.6.1

#### New features

- **Added** Added to increase coverage
- **Added** front-end UI registration function
- **Added** Performance enhancements
- **Added** Added pagination feature to the list page
- **Added** Added the feature of modifying the configuration
- **Added** Added the ability to return modifiable configuration items
- **Added** Change the limitation of creating instances to the cluster level instead of the namespace level
- **Added** Added splicing feature of monitoring address
- **Added** Added the ability to modify the version number
- **Added** Modify the underlying update logic to patch logic
- **Added** RabbitMQ e2e test coverage is about 17.24%
- **Added** Added RabbitMQ performance pressure test report
- **Added** Added RabbitMQ bug spot check
- **Added** Docking ghippo adds workspace interface
- **Added** Docking insight injected into dashboard through crd
- **Added** uniformly adjust the timestamp api field to int64
- **Added** Increased single-test coverage to 53%
- **Optimized** Update the release note script and run the release-process specification
- **Added** New feature description
- **Added** Create RabbitMQ
- **Added** RabbitMQ data migration
- **Added** instance monitoring
- **Added** Enter RabbitMQ for the first time
- **Added** Use cases