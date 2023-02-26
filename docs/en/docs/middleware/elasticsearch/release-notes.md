# Elasticsearch Indexing Service Release Notes

This page lists the Release Notes of Elasticsearch indexing service, so that you can understand the evolution path and feature changes of each version.

##v0.3.6

Release date: 2022-11-28

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

##v0.3.4

Release date: 2022-10-28

- **Add** sync pod status to instance details page
- **Optimize** workspace interface logic adjustment
- **Optimization** Style adjustments that do not conform to design specifications
- **Optimized** password acquisition logic adjustment
- **Optimize** cpu&memory request amount should be less than limit logic adjustment
- **Optimize** The instance version does not allow modification, the drop-down box should be text
- **Fix** Update the instance service settings, confirm that there is no response, and cannot be submitted
- **NEW** Add interface to get user list
- **New** support arm architecture

##v0.3.2

Release date: 2022-9-25

### APIs

- **NEW** Added pagination function to the list page
- **NEW** Added the function of modifying the configuration
- **NEW** Added the ability to return modifiable ConfigMaps
- **NEW** Change the limitation of creating instances to the cluster level instead of the namespace level
- **NEW** Added splicing function of monitoring address
- **NEW** Added the ability to modify the version number
- **NEW** Modify the underlying update logic to patch logic
- **Add** uniformly adjust the timestamp api field to int64
- **NEW** The single-test coverage rate has been increased to 43%
- **NEW** Add workspace interface for docking with global management
- **NEW** Docking insight injected into dashboard through crd
- **NEW** Update the release note script to implement the release-process specification

### Install

- **NEW** Support helm deploy eck-operator
- **NEW** Support helm to deploy mcamel-elasticsearch service

### Documentation

- **NEW** First release of documentation website
- **Add** function description
- **Add** Product Advantages
- **NEW** What is Elasticsearch
- **NEW** Basic concept
- **NEW** Cluster Capacity Planning