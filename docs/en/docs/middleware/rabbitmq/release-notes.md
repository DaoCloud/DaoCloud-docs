# RabbitMQ Release Notes

This page lists the Release Notes of the RabbitMQ message queue, so that you can understand the evolution path and feature changes of each version.

## 2023-03-30

### v0.9.1

#### Optimization

- **Optimize** `mcamel-rabbitmq` improves Operator image to speed up addresses.

## 2023-03-28

### v0.9.0

#### Features

- **Added** `mcamel-rabbitmq` supports middleware link tracking adaptation.
- **Added** Enable link tracking according to parameter configuration when installing `mcamel-rabbitmq`.

## 2023-02-23

### v0.8.0

#### Features

- **Added** `mcamel-rabbitmq` helm-docs template file.
- **Added** The Operator in the `mcamel-rabbitmq` app store can only be installed in mcamel-system.
- **Added** `mcamel-rabbitmq` supports cloud shell.
- **Added** `mcamel-rabbitmq` supports separate registration of navigation bar.

- **Added** log view operation instructions, support custom query, export and other functions.

#### upgrade

- **Upgrade** `mcamel-rabbitmq` upgrade offline mirror detection script.

#### Fix

- **Added** `mcamel-rabbitmq` supports viewing logs.
- **Fixed** the problem that `mcamel-rabbitmq` instance name is too long and the custom resource cannot be created.
- **Fixed** `mcamel-rabbitmq` workspace Editor user cannot view instance password.

## 2022-12-25

### v0.7.0

#### Features

- **Added** `mcamel-rabbitmq` NodePort port conflict detection in advance.
- **Added** `mcamel-rabbitmq` node affinity configuration.

#### Optimization

- **Optimize** `mcamel-rabbitmq-ui` middleware style walkthrough optimization.

## 2022-11-28

### v0.6.4

#### Features

- **Added** Add interface to get user list
- **Added** supports multi-architecture images, the configuration method is `depend.arm64-img.rabbitClusterImageFormat: xxxx`
- **Added** supports sc expansion interception, when sc does not support expansion, directly intercept it
- **Added** public field when returning list or details
- **Added** return alerts
- **Added** Validation Service annotation

#### Optimization

- **Optimized** Password verification is adjusted to MCamel medium password strength

#### Fix

- **Fixed** page console may access wrong port

## 2022-10-27

### v0.6.1

#### Features

- **Added** Added to increase coverage
- **Added** front-end UI registration function
- **Added** Performance enhancements
- **Added** Added pagination function to the list page
- **Added** Added the function of modifying the configuration
- **Added** Added the ability to return modifiable configuration items
- **Added** Change the limitation of creating instances to the cluster level instead of the namespace level
- **Added** Added splicing function of monitoring address
- **Added** Added the ability to modify the version number
- **Added** Modify the underlying update logic to patch logic
- **Added** RabbitMQ e2e test coverage is about 17.24%
- **Added** Added RabbitMQ performance pressure test report
- **Added** Added RabbitMQ bug spot check
- **Added** Docking ghippo adds workspace interface
- **Added** Docking insight injected into dashboard through crd
- **Added** uniformly adjust the timestamp api field to int64
- **Added** Increased single-test coverage to 53%
- **Optimize** Update the release note script and execute the release-process specification
- **Added** New function description
- **Added** Create RabbitMQ
- **Added** RabbitMQ data migration
- **Added** instance monitoring
- **Added** Enter RabbitMQ for the first time
- **Added** Applicable scenarios