---
MTPE: windsonsea
date: 2024-01-05
---

# Elasticsearch Indexing Service Release Notes

This page lists the Release Notes of Elasticsearch indexing service, so that you can understand the evolution path and feature changes of each version.

*[mcamel-elasticsearch]: "mcamel" is the dev name for DaoCloud's middlewares, and "elasticsearch" is the middleware for distributed search and analytics services

## 2023-12-31

### v0.13.0

#### Improvements

- **Fixed** an issue where validation for special characters in input fields was not working when creating instances.

## 2023-11-30

### v0.12.0

#### Improvements

- **Added** support for recording operation audit logs
- **Improved** prompt when instance list information is not obtained

### 2023-10-31

#### v0.11.0

##### Improvements

- **Added** offline upgrade functionality
- **Added** restart functionality for instances
- **Fixed** cloudshell permissions issue

## 2023-08-31

### v0.10.0

#### Improvements

- **Improved** syntax compatibility for KindBase
- **Improved** default anti-affinity configuration on the creation page
- **Improved** page display during operator creation process

## 2023-07-31

### v0.9.3

#### New features

- **Added** access restrictions for UI interface

## 2023-06-30

### v0.9.0

#### New features

- **Added** anti-affinity configuration for `mcamel-elasticsearch` nodes
- **Added** monitoring charts for `mcamel-elasticsearch`, removing interfering elements and adding time range selection

#### Improvements

- **Improved** closed-loop installation of `mcamel-elasticsearch` ServiceMonitor
- **Fixed** the monitoring charts for `mcamel-elasticsearch`, removing interfering elements and adding time range selection

## 2023-05-30

### v0.8.0

#### New features

- **Added** integrationg with the global management audit log module for `mcamel-elasticsearch`
- **Added** configurable instance monitoring data collection interval for `mcamel-elasticsearch`
- **Fixed** incorrect pagination display in the Pod list for `mcamel-elasticsearch`

## 2023-04-27

### v0.5.1

#### New features

- **Added** `mcamel-elasticsearch` details page displays related events
- **Added** `mcamel-elasticsearch` supports custom roles

#### Improvements

- **Improved** `mcamel-elasticsearch` scheduling strategy adds a sliding button
- **Fixed** `mcamel-elasticsearch` may interrupt the retry problem when managing clusters

## 2023-03-28

### v0.6.0

#### New features

- **Added** `mcamel-elasticsearch` supports middleware traces adaptation
- **Added** Enable traces according to parameter configuration when installing `mcamel-elasticsearch`
- **Added** `mcamel-elasticsearch` Kibana supports LoadBalancer type

#### Upgrade

- **Upgraded** golang.org/x/net to v0.7.0
- **Upgraded** GHippo SDK to v0.14.0

## 2023-02-23

### v0.5.0

#### New features

- **Added** `mcamel-elasticsearch` helm-docs template file
- **Added** The Operator in the `mcamel-elasticsearch` app store can only be installed on mcamel-system
- **Added** `mcamel-elasticsearch` supports cloud shell
- **Added** `mcamel-elasticsearch` supports separate registration of navigation bar
- **Added** `mcamel-elasticsearch` supports viewing logs
- **Added** `mcamel-elasticsearch` Operator docking with chart-syncer
- **Added** `mcamel-elasticsearch` supports LB

- **Added** log view operation instructions, support custom query, export and other features

#### Upgrade

- **Upgraded** `mcamel-elasticsearch` upgrade offline mirror detection script

#### Fixes

- **Fixed** an issue that `mcamel-elasticsearch` instance name is too long and the custom resource cannot be created.
- **Fixed** `mcamel-elasticsearch` workspace Editor users cannot see instance password
- **Fixed** `mcamel-elasticsearch` password cannot use special characters
- **Fixed** `mcamel-elasticsearch` out of index causing panic issue

## 2022-12-25

### v0.4.0

#### New features

- **Added** `mcamel-elasticsearch` gets the list of NodePorts allocated by the cluster
- **Added** `mcamel-elasticsearch` adds status details
- **Added** `mcamel-elasticsearch` node affinity configuration

#### Improvements

- **Improved** `mcamel-elasticsearch` can display public es, which cannot be deleted before being managed
- **Improved** `mcamel-elasticsearch` increases health status return

#### Fixes

- **Fixed** `mcamel-elasticsearch` fixes the bug that deletion will fail when kb does not exist
- **Fixed** `mcamel-elasticsearch` fixes exporter offline failure
- **Fixed** `mcamel-elasticsearch` fixes the bug that port information is not returned after the es is successfully created
- **Fixed** Kibana's service type does not meet expectations when `mcamel-elasticsearch` queries instance list and details

## 2022-11-28

### v0.3.6

- **Improved** Password validation adjusted to MCamel medium password strength
- **Improved** Characters can be upgraded
- **Added** sc expansion prompt
- **Added** public field when returning list or details
- **Added** return alert
- **Added** Validation Service annotation
- **Fixed** After updating the instance, the cluster uses the wrong image, resulting in abnormal cluster status
- **Fixed** When using NodePort, the update instance reported an error
- **Upgraded** depends on eck operator version 2.3.0
- **Improved** In some versions of K8s clusters, the default FD is insufficient and cannot be started
- **Improved** Reduce the running permissions of the elasticsearch container

## 2022-10-28

### v0.3.4

#### New features

- **Added** sync pod status to instance details page
- **Added** interface to get user list
- **Added** support arm architecture

#### Improvements

- **Improved** workspace interface logic adjustment
- **Improved** Style adjustments that do not conform to design specifications
- **Improved** password acquisition logic adjustment
- **Improved** cpu&memory request amount should be less than limit logic adjustment
- **Improved** The instance version does not allow modification, the drop-down box should be text

#### Fixes

- **Fixed** Update the instance service settings, confirm that there is no response, and cannot be submitted

## 2022-9-25

### v0.3.2

#### New features

- **Added** pagination feature to the list page
- **Added** the feature of modifying the configuration
- **Added** the ability to return modifiable configuration items
- **Added** Change the limitation of creating instances to the cluster level instead of the namespace level
- **Added** splicing feature of monitoring address
- **Added** the ability to modify the version number
- **Added** Modify the underlying update logic to patch logic
- **Added** uniformly adjust the timestamp api field to int64
- **Added** The single-test coverage rate has been increased to 43%
- **Added** workspace interface for docking with global management
- **Added** Docking insight injected into dashboard through crd
- **Added** Update the release note script to implement the release-process specification
- **Added** Support helm deploy eck-operator
- **Added** Support helm to deploy mcamel-elasticsearch service
- **Added** First release of documentation website
- **Added** feature description
- **Added** Product Advantages
- **Added** What is Elasticsearch
- **Added** Basic concept
- **Added** Cluster Capacity Planning
