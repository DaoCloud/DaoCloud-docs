---
MTPE: windsonsea
date: 2024-01-05
---

# RabbitMQ Release Notes

This page lists the Release Notes of the RabbitMQ message queue, so that you can understand the evolution path and feature changes of each version.

*[mcamel-rabbitmq]: "mcamel" is the dev name for DaoCloud's middlewares, and "rabbitmq" is a message agent implemented on the basis of AMQP

## 2024-04-30

### v0.19.0

- **Added** a prompt for namespace quota

## 2024-03-31

### v0.18.0

- **Improved** support for Chinese monitoring dashboard in Chinese mode

## 2024-01-31

### v0.17.0

#### Improvements

- **Improved** Added display of RabbitMQ version in global management

## 2023-12-31

### v0.16.0

- **Fixed** an issue where validation for special characters in input fields was not working when creating instances.

## 2023-11-30

### v0.15.0

- **Added** support for setting access whitelist for Mcamel-RabbitMQ
- **Added** support for recording operation audit logs
- **Improved** prompt when instance list information is not obtained

## 2023-10-31

### v0.14.0

- **Added** offline upgrade functionality
- **Added** restart functionality for instances
- **Fixed** cloudshell permissions issue

## 2023-08-31

### v0.13.0

- **Improved** syntax compatibility for KindBase
- **Improved** page display during operator creation process
- **Improved** default anti-affinity configuration on the creation page

## 2023-07-31

### v0.12.3

- **Added** workload anti-affinity capability
- **Added** access restrictions for UI interface permissions

## 2023-06-30

### v0.11.0

- **Added** __LoadBalancer__ service type
- **Improved** the monitoring charts by removing distracting elements and adding a time range selection

## 2023-04-27

### v0.10.1

- **Added** __mcamel-rabbitmq__ details page displays related events
- **Added** __mcamel-rabbitmq__ supports custom roles
- **Added** __mcamel-rabbitmq__ supports access traces
- **Improved** __mcamel-rabbitmq__ scheduling strategy adds a sliding button

## 2023-03-30

### v0.9.1

- **Improved** __mcamel-rabbitmq__ improves Operator image to speed up addresses.

## 2023-03-28

### v0.9.0

- **Added** __mcamel-rabbitmq__ supports middleware traces adaptation
- **Added** Enable traces according to parameter configuration when installing __mcamel-rabbitmq__ 

## 2023-02-23

### v0.8.0

- **Added** __mcamel-rabbitmq__ helm-docs template file
- **Added** The Operator in the __mcamel-rabbitmq__ app store can only be installed in mcamel-system
- **Added** __mcamel-rabbitmq__ supports cloud shell
- **Added** __mcamel-rabbitmq__ supports separate registration of navigation bar
- **Added** log view operation instructions, support custom query, export and other features
- **Upgraded** __mcamel-rabbitmq__ upgrade offline mirror detection script
- **Added** __mcamel-rabbitmq__ supports viewing logs
- **Fixed** an issue that __mcamel-rabbitmq__ instance name is too long and the custom resource cannot be created
- **Fixed** __mcamel-rabbitmq__ workspace Editor user cannot view instance password

## 2022-12-25

### v0.7.0

- **Added** __mcamel-rabbitmq__ NodePort port conflict detection in advance
- **Added** __mcamel-rabbitmq__ node affinity configuration
- **Improved** __mcamel-rabbitmq-ui__ middleware style walkthrough optimization

## 2022-11-28

### v0.6.4

- **Added** interface to get user list
- **Added** supports multi-architecture images, the configuration method is __depend.arm64-img.rabbitClusterImageFormat: xxxx__ 
- **Added** supports sc expansion interception, when sc does not support expansion, directly intercept it
- **Added** public field when returning list or details
- **Added** return alerts
- **Added** Validation Service annotation
- **Improved** Password verification is adjusted to MCamel medium password strength
- **Fixed** page console may access wrong port

## 2022-10-27

### v0.6.1

#### New features

- **Added** to increase coverage
- **Added** front-end UI registration function
- **Added** Performance enhancements
- **Added** pagination feature to the list page
- **Added** the feature of modifying the configuration
- **Added** the ability to return modifiable configuration items
- **Added** Change the limitation of creating instances to the cluster level instead of the namespace level
- **Added** splicing feature of monitoring address
- **Added** the ability to modify the version number
- **Added** Modify the underlying update logic to patch logic
- **Added** RabbitMQ e2e test coverage is about 17.24%
- **Added** RabbitMQ performance pressure test report
- **Added** RabbitMQ bug spot check
- **Added** Docking ghippo adds workspace interface
- **Added** Docking insight injected into dashboard through crd
- **Added** uniformly adjust the timestamp api field to int64
- **Added** Increased single-test coverage to 53%
- **Improved** Update the release note script and run the release-process specification
- **Added** New feature description
- **Added** Create RabbitMQ
- **Added** RabbitMQ data migration
- **Added** instance monitoring
- **Added** Enter RabbitMQ for the first time
- **Added** use cases
