# RabbitMQ Release Notes

This page lists the Release Notes of the RabbitMQ message queue, so that you can understand the evolution path and feature changes of each version.

## 2023-04-27

### v0.10.1

#### new function

- **Add** `mcamel-rabbitmq` details page displays related events
- **NEW** `mcamel-rabbitmq` supports custom roles
- **NEW** `mcamel-rabbitmq` supports access link tracking

#### Optimization

- **Optimize** `mcamel-rabbitmq` scheduling strategy adds a sliding button

## 2023-03-30

### v0.9.1

#### Optimization

- **Optimize** `mcamel-rabbitmq` improves Operator image to speed up addresses.

## 2023-03-28

### v0.9.0

#### new function

- **NEW** `mcamel-rabbitmq` supports middleware link tracking adaptation.
- **New** Enable link tracking according to parameter configuration when installing `mcamel-rabbitmq`.

## 2023-02-23

### v0.8.0

#### new function

- **Added** `mcamel-rabbitmq` helm-docs template file.
- **NEW** The Operator in the `mcamel-rabbitmq` app store can only be installed in mcamel-system.
- **NEW** `mcamel-rabbitmq` supports cloud shell.
- **NEW** `mcamel-rabbitmq` supports separate registration of navigation bar.

- **Add** log view operation instructions, support custom query, export and other functions.

#### upgrade

- **Upgrade** `mcamel-rabbitmq` upgrade offline mirror detection script.

#### fix

- **NEW** `mcamel-rabbitmq` supports viewing logs.
- **Fix** the problem that `mcamel-rabbitmq` instance name is too long and the custom resource cannot be created.
- **Fix** `mcamel-rabbitmq` workspace Editor user cannot view instance password.

## 2022-12-25

### v0.7.0

#### new function

- **NEW** `mcamel-rabbitmq` NodePort port conflict detection in advance.
- **NEW** `mcamel-rabbitmq` node affinity configuration.

#### Optimization

- **Optimize** `mcamel-rabbitmq-ui` middleware style walkthrough optimization.

## 2022-11-28

### v0.6.4

#### new function

- **NEW** Add interface to get user list
- **New** supports multi-architecture images, the configuration method is `depend.arm64-img.rabbitClusterImageFormat: xxxx`
- **New** supports sc expansion interception, when sc does not support expansion, directly intercept it
- **Add** public field when returning list or details
- **Added** return alerts
- **Add** Validation Service annotation

#### Optimization

- **Optimized** Password verification is adjusted to MCamel medium password strength

#### fix

- **FIXED** page console may access wrong port

## 2022-10-27

### v0.6.1

#### new function

- **NEW** Added to increase coverage
- **Add** front-end UI registration function
- **NEW** Performance enhancements
- **NEW** Added pagination function to the list page
- **NEW** Added the function of modifying the configuration
- **NEW** Added the ability to return modifiable configuration items
- **NEW** Change the limitation of creating instances to the cluster level instead of the namespace level
- **NEW** Added splicing function of monitoring address
- **NEW** Added the ability to modify the version number
- **NEW** Modify the underlying update logic to patch logic
- **NEW** RabbitMQ e2e test coverage is about 17.24%
- **NEW** Added RabbitMQ performance pressure test report
- **NEW** Added RabbitMQ bug spot check
- **NEW** Docking ghippo adds workspace interface
- **NEW** Docking insight injected into dashboard through crd
- **Add** uniformly adjust the timestamp api field to int64
- **NEW** Increased single-test coverage to 53%
- **Optimize** Update the release note script and run the release-process specification
- **NEW** New function description
- **NEW** Create RabbitMQ
- **NEW** RabbitMQ data migration
- **New** instance monitoring
- **NEW** Enter RabbitMQ for the first time
- **Added** Use cases