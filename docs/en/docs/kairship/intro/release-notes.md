# Multi-cloud Orchestration Release Notes

This page lists the Release Notes of multi-cloud orchestration, so that you can understand the evolution path and feature changes of each version.

## 2023-03-29

### v0.7.4

#### Features

- **Added** support custom management cluster
- **Added** Load form supports data storage
- **Added** Added support for carrying Service when upgrading the load with one key
- **Added** Multi-cloud routing supports differentiated configuration of IngressClass
- **Added** supports cluster-level deployment strategies and differentiated strategies
- **Added** Added support for configuring LabelsOverrider and AnnotationsOverrider
- **Added** custom role permissions

#### Optimization

- **Optimize** instance form, support hiding annotations prefixed with 'kairship.io/'
- **Optimized** load form, differentiated configuration guides users to select clusters

#### Fix

- **Fixed** Fix the problem that one-click propagation service fails
- **Fixed** fix mesh jump link style
- **Fixed** Incorrect front-end version
- **Fixed** One-click upgrade workload automatically propagates dependent services
- **Fixed** filter subcluster LB type service for one-click upgrade
- **Fixed** Upgrade karmada version to v1.5.0

## 2023-02-27

### v0.6.3

#### Features

- **Added** Add multi-cloud custom resource module, support addition, deletion, modification, query, and distribution functions
- **Added** Add multi-cloud routing module, support addition, deletion, modification, query and distribution functions

#### Optimization

- **Optimized** Load form supports auto-propagation fields
- **Optimized** Multi-cloud Service supports specifying the deployment cluster function
- **Optimized** load details, support clusters showing expected scheduling

#### Fix

- **Fixed** Fix the problem that the one-click upgrade of multi-cloud resources cannot display the member cluster
- **Fixed** cronjob calculation of the total number of tasks and the number of current tasks is incorrect
- **Fixed** Generate pp resource name issue
- **Fixed** Cronjob not updating via yaml
- **Fixed** Custom resource details page, deployment policy usage status display problem
- **Fixed** no mirror for kairship-ui in offline package

## 2022-12-25

### v0.5

#### Features

- **Added** Add cronjob related interfaces such as adding, deleting, modifying and checking
- **Added** Add related interfaces such as adding, deleting, modifying and checking jobs
- **Added** Added one-click migration of multi-cluster applications for single-cluster applications, automatic upgrade of dependent resources
- **Added** Add job and cronjob types to ListPropagationPolicies and ListInstanceOverridePolicies interfaces
- **Added** ETCD high availability
- **Added** Added priority field to deployment strategy
- **Added** New support for differentiation strategy imageOverride, CommandOverrider ArgsOverrider LabelsOverrider AnnotationsOverrider
- **Added** If the deployment strategy has been used and associated with the workload, the deployment strategy does not support deletion
- **Added** multi-cloud workload, new support for Job, CronJob
- **Added** Differentiation strategy supports form-based creation and update
- **Added** Deployment strategy supports form-based creation and update
- **Added** Worker cluster supports displaying eviction status

#### Optimization

- **Optimized** Deployment policy form, new enable and disable switches for propagation constraints
- **Upgrade** the version of karmada-operator to v0.1.9, to solve the problem of pod anti-affinity of multiple instances of etcd

#### Fix

- **Fixed** A user who is not associated with any role can view all instance information
- **Fixed** When the scheduling algorithm is Duplicated, the total number of workload instances is incorrectly counted
- **Fixed** When the scheduling algorithm is Duplicated, the total number of workload instances is incorrectly counted
- **Fixed** Data in ghippo was not deleted when instance was deleted
- **Fixed** When the instance is deleted, the labels of the working cluster are not removed
- **Fixed** When removing a cluster, you can see the cluster being removed in the single-cluster application multi-cloud interface, and you can add the cluster being removed
- **Fixed** Fix that in the process of removing the member cluster, one-click upgrade of the resources of the member cluster cannot be performed
- **Fixed** unhealthy pair member cluster cannot be removed

## 2022-11-25

### v0.4

#### Features

- **Added** prometheus metrics, opentelemetry link trace
- **Added** Displays the corresponding cluster list after creating a workload in a specified region
- **Added** Displays the corresponding cluster list after creating a specified workload tag
- **Added** Productization of failover failover

#### Fix

- **Fixed** estimator is not suitable for offline installation
- **Fixed** the problem that the stateless load display on the instance details page is abnormal

## 2022-10-21

### v0.3

#### Features

- **Added** multi-cloud orchestration enable permission verification
- **Added** multi-cloud orchestration list instance interface, display data according to permissions
- **Added** Multi-cloud orchestration query cluster resource overview information based on user permissions
- **Added** multi-cloud orchestration to query the labels of all member clusters
- **Added** One-click conversion of multi-cloud orchestration stand-alone cluster applications to multi-cluster applications
- **Added** multi-cloud orchestration to query the namespace and deployment resources of the member cluster
- **Added** Added prompts for creating multi-cloud resources

#### Optimization

- **Optimize** multi-cloud orchestration optimizes the protobuf data structure of karmada PropagationPolicy and OverridePolicy

#### Fix

- **Fixed** Multi-cloud orchestration fixes the problem that the sorting of all PropagationPolicy resources under the instance does not take effect
- **Fixed** multi-cloud orchestration fixes the problem of removing member clusters
- **Fixed** Several bug fixes

## 2022-9-25

### v0.2

#### Features

- **Added** query interface for scheduling time
- **Added** multi-cloud service ConfigMap management interface
- **Added** Create multiple resources and policy resources in batches
- **Added** Service adds workload tags
- **Added** Get the interface of Service under all namespaces
- **Added** Added istio sidecar injection
- **Added** When accessing the cluster, deploy the karmada estimator
- **Added** multi-cloud secret interface
- **Added** Added resource data collection of instance cpu and memery
- **Added** Added event query API for instance

## 2022-8-21

### v0.1

#### Features

- **Added** Added cloudshell API to manage karmada cluster through cloudshell
- **Added** Added management interface for multi-cloud namespaces
- **Added** multi-cloud service management interface
- **Added** multi-cloud workload details related interface
- **Added** Added support for setting cluster taint and tolerance
- **Added** Download kubeconfig interface for karmada instance
- **Added** Provide instance update API to support modification of instance alias and label

#### Optimization

- **Optimize** Optimize instance API and collect resource statistics of karmada instance