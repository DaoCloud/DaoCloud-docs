# Elasticsearch Indexing Service Release Notes

This page lists the Release Notes of Elasticsearch indexing service, so that you can understand the evolution path and feature changes of each version.

## 2023-04-27

### v0.5.1

#### new function

- **Add** `mcamel-elasticsearch` details page displays related events
- **NEW** `mcamel-elasticsearch` supports custom roles

#### Optimization

- **Optimize** `mcamel-elasticsearch` scheduling strategy adds a sliding button
- **Fix** `mcamel-elasticsearch` may interrupt the retry problem when managing clusters

## 2023-03-28

### v0.6.0

#### new function

- **NEW** `mcamel-elasticsearch` supports middleware link tracking adaptation.
- **NEW** Enable link tracking according to parameter configuration when installing `mcamel-elasticsearch`.
- **NEW** `mcamel-elasticsearch` Kibana supports LoadBalancer type.

#### upgrade

- **upgrade** golang.org/x/net to v0.7.0
- **Upgrade** GHippo SDK to v0.14.0

## 2023-02-23

### v0.5.0

#### new function

- **Added** `mcamel-elasticsearch` helm-docs template file.
- **NEW** The Operator in the `mcamel-elasticsearch` app store can only be installed on mcamel-system.
- **NEW** `mcamel-elasticsearch` supports cloud shell.
- **NEW** `mcamel-elasticsearch` supports separate registration of navigation bar.
- **New** `mcamel-elasticsearch` supports viewing logs.
- **New** `mcamel-elasticsearch` Operator docking with chart-syncer.
- **NEW** `mcamel-elasticsearch` supports LB.

- **Add** log view operation instructions, support custom query, export and other functions.

#### upgrade

- **Upgrade** `mcamel-elasticsearch` upgrade offline mirror detection script.

#### fix

- **Fix** the problem that `mcamel-elasticsearch` instance name is too long and the custom resource cannot be created.
- **FIXED** `mcamel-elasticsearch` workspace Editor users cannot see instance password.
- **Fix** `mcamel-elasticsearch` password cannot use special characters.
- **Fix** `mcamel-elasticsearch` out of index causing panic issue.

## 2022-12-25

### v0.4.0

#### new function

- **NEW** `mcamel-elasticsearch` gets the list of NodePorts allocated by the cluster.
- **New** `mcamel-elasticsearch` adds status details.
- **Added** `mcamel-elasticsearch` node affinity configuration.

#### Optimization

- **Optimization** `mcamel-elasticsearch` can display public es, which cannot be deleted before being managed.
- **Optimize** `mcamel-elasticsearch` increases health status return.

#### fix

- **Fix** `mcamel-elasticsearch` fixes the bug that deletion will fail when kb does not exist.
- **FIX** `mcamel-elasticsearch` fix es exporter offline failure.
- **Fix** `mcamel-elasticsearch` fixes the bug that the ports information is not returned after the es is successfully created.
- **Fix** Kibana's service type does not meet expectations when `mcamel-elasticsearch` queries instance list and details.

##v0.3.6

2022-11-28

- **IMPROVED** Password validation adjusted to MCamel medium password strength
- **IMPROVED** Characters can be upgraded
- **NEW** Added sc expansion prompt
- **Add** public field when returning list or details
- **NEW** Added return alert
- **Add** Validation Service annotation
- **Fix** After updating the instance, the cluster uses the wrong image, resulting in abnormal cluster status
- **FIXED** When using NodePort, the update instance reported an error
- **Upgrade** depends on eck operator version 2.3.0
- **Optimization** In some versions of K8s clusters, the default FD is insufficient and cannot be started
- **Optimize** Reduce the running permissions of the elasticsearch container

## 2022-10-28

### v0.3.4

#### new function

- **Add** sync pod status to instance details page
- **NEW** Add interface to get user list
- **New** support arm architecture

#### Optimization

- **Optimize** workspace interface logic adjustment
- **Optimization** Style adjustments that do not conform to design specifications
- **Optimized** password acquisition logic adjustment
- **Optimize** cpu&memory request amount should be less than limit logic adjustment
- **Optimize** The instance version does not allow modification, the drop-down box should be text

#### fix

- **Fix** Update the instance service settings, confirm that there is no response, and cannot be submitted

## 2022-9-25

### v0.3.2

#### new function

- **NEW** Added pagination function to the list page
- **NEW** Added the function of modifying the configuration
- **NEW** Added the ability to return modifiable configuration items
- **NEW** Change the limitation of creating instances to the cluster level instead of the namespace level
- **NEW** Added splicing function of monitoring address
- **NEW** Added the ability to modify the version number
- **NEW** Modify the underlying update logic to patch logic
- **Add** uniformly adjust the timestamp api field to int64
- **NEW** The single-test coverage rate has been increased to 43%
- **NEW** Add workspace interface for docking with global management
- **NEW** Docking insight injected into dashboard through crd
- **NEW** Update the release note script to implement the release-process specification
- **NEW** Support helm deploy eck-operator
- **NEW** Support helm to deploy mcamel-elasticsearch service
- **NEW** First release of documentation website
- **Add** function description
- **Add** Product Advantages
- **NEW** What is Elasticsearch
- **NEW** Basic concept
- **NEW** Cluster Capacity Planning