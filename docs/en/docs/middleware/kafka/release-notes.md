---
MTPE: windsonsea
date: 2024-01-05
---

# Kafka message queue Release Notes

This page lists the Release Notes of Kafka message queue, so that you can understand the evolution path and feature changes of each version.

*[mcamel-kafka]: "mcamel" is the dev name for DaoCloud's middlewares, and "kafka" is the middleware that provides distributed messaging queue services

## 2024-04-30

### v0.14.0

- **Added** a prompt for namespace quota
- **Fixed** the issue of incorrect default values for parameter templates

## 2024-03-31

### v0.13.0

- **Added** support for parameter template management
- **Added** capability to create Kafka instances via templates
- **Improved** support for configuring storage for Zookeeper
- **Improved** Prevent reading Kafka password when user permissions are insufficient

## 2024-01-31

### v0.12.0

#### Improvements

- **Improved** Added display of Kafka version in global management

## 2023-12-31

### v0.11.0

#### Improvements

- **Improved** support for Chinese language in the monitoring dashboard
- **Improved** returning multiple NodePorts for Kafka when accessed in NodePort mode
- **Fixed** an issue of duplicate data in the Kafka repair list display
- **Fixed** an issue where validation for special characters in input fields was not working when creating instances.

## 2023-11-30

### v0.10.0

#### Improvements

- **Added** support for recording operation audit logs
- **Improved** prompt when instance list information is not obtained

## 2023-10-31

### v0.9.0

#### Improvements

- **Added** offline upgrade functionality
- **Added** restart functionality for instances
- **Fixed** cloudshell permissions issue

## 2023-08-31

### v0.8.0

#### New features

- **Added** whitelist access control

#### Improvements

- **Improved** syntax compatibility for KindBase
- **Improved** page display during operator creation process

## 2023-07-31

### v0.7.3

#### New features

- **Added** access restrictions for UI interface

## 2023-06-30

### v0.7.0

#### New features

- **Added** integration with the global management audit log module
- **Added** support for __LoadBalancer__ service type

#### Improvements

- **Improved** interfering elements and added time range selection to monitoring charts
- **Improved** closed-loop installation of __ServiceMonitor__ 

## 2023-04-27

### v0.5.1

#### New features

- **Added** __mcamel-kafka__ details page displays related events
- **Added** __mcamel-kafka__ supports custom roles

#### Improvements

- **Improved** __mcamel-kafka__ scheduling strategy adds a sliding button

## 2023-03-28

### v0.4.0

#### New features

- **Added** __mcamel-kafka__ supports middleware traces adaptation
- **Added** Install __mcamel-kafka__ to enable traces according to parameter configuration

#### Improvements

- **Improved** __mcamel-kafka__ optimizes Kafka's default configuration.
- **Upgraded** golang.org/x/net to v0.7.0
- **Upgraded** GHippo SDK to v0.14.0

## 2023-02-23

### v0.3.0

#### New features

- **Added** __mcamel-kafka__ helm-docs template file
- **Added** The Operator in the __mcamel-kafka__ app store can only be installed in mcamel-system
- **Added** __mcamel-kafka__ supports cloud shell
- **Added** __mcamel-kafka__ supports separate registration of navigation bar
- **Added** __mcamel-kafka__ supports viewing logs
- **Added** __mcamel-kafka__ Operator docking with chart-syncer

#### Improvements

- **Improved** __mcamel-kafka__ upgrade offline mirror detection script

#### fix

- **Fixed** an issue that __mcamel-kafka__ instance name is too long and the custom resource cannot be created
- **Fixed** __mcamel-kafka__ workspace Editor user cannot view instance password
- **Added** log view operation instructions, support custom query, export and other features

## 2022-12-25

### v0.2.0

#### New features

- **Added** __mcamel-kafka__ NodePort port conflict early detection
- **Added** __mcamel-kafka__ node affinity configuration

#### Improvements

- **Improved** __mcamel-kafka__ manager removes the probe to prevent kafka from being unable to open the manager when it is not ready
- **Improved** __mcamel-kafka__ zooEntrance repackage mirror address to 1.0.0

## 2022-11-28

### v0.1.6

#### New features

- **Improved** Improve and optimize the copy function
- **Improved** instance details - access settings, remove cluster IPv4
- **Improved** Middleware password verification difficulty adjustment
- **Added** Docking alert capability
- **Added** the feature of judging whether sc supports capacity expansion and prompting in advance
- **Improved** Optimize the prompt logic of installation environment check & adjust its style
- **Improved** middleware style walkthrough optimization
- **Fixed** The offline image has numbers and capital letters that cannot be scanned

## 2022-11-08

### v0.1.4

#### New features

- **Fixed** The correct field cannot be verified when updating, such as managerPass
- **Improved** Password validation adjusted to MCamel low password strength
- **Added** Returns whether the sc capacity can be updated
- **Added** public field when returning list or details
- **Added** return alert
- **Added** Validation Service annotation
- **Fixed** operator select by name
- **Fixed** service address display error
- **Fixed** When Kafka uses NodePort, the creation fails

## 2022-10-28

### v0.1.2

#### New features

- **Added** Sync Pod status to instance details page
- **Improved** workspace interface logic adjustment
- **Improved** Style adjustments that do not conform to design specifications
- **Improved** password acquisition logic adjustment
- **Improved** cpu&memory request amount should be less than limit logic adjustment

## 2022-9-25

### v0.1.1

#### New features

- **Added** supports kafka list query, status query, creation, deletion and modification
- **Added** Support kafka-manager to manage kafka
- **Added** Support kafka metric monitoring, check the monitoring chart
- **Added** support for ghippo permission linkage
- **Added** __mcamel-elasticsearch__ interface to get user list
- **Improved** Update the release note script and run the release-process specification
