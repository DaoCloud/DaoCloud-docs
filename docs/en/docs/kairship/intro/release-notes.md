# Multi-cloud Orchestration Release Notes

This page lists the Release Notes of multi-cloud orchestration, so that you can understand the evolution path and feature changes of each version.

## 2023-04-27

### v0.8.0

#### new function

- **NEW** supports cluster scheduling group
- **NEW** Support mirror selector selection
- **NEW** advanced settings, new scheduled rescheduling
- **New** advanced settings, new cluster health status threshold setting

#### fix

- **Fix** When the deployment strategy selects the CR resource type, the kind is not automatically filled
- **Fix** Instance deletion pop-up window, whether to delete the Karmada instance synchronously to adjust the prompt information

#### remove

- **Remove** istio's sidecar injection for controller-manager and proxy

## 2023-03-29

### v0.7.4

#### new function

- **NEW** support custom management cluster
- **NEW** Load form supports data storage
- **NEW** Added support for carrying Service when upgrading the load with one key
- **NEW** Multi-cloud routing supports differentiated configuration of IngressClass
- **New** supports cluster-level deployment strategies and differentiated strategies
- **NEW** Added support for configuring LabelsOverrider and AnnotationsOverrider
- **Add** custom role permissions

#### Optimization

- **Optimize** instance form, support hiding annotations prefixed with 'kairship.io/'
- **Optimized** load form, differentiated configuration guides users to select clusters

#### fix

- **Fix** Fix the problem that one-click propagation service fails
- **FIX** fix grid jump link style
- **FIX** Incorrect front-end version
- **Fix** One-click upgrade workload automatically propagates dependent services
- **Fix** filter subcluster LB type service for one-click upgrade
- **FIX** Upgrade karmada version to v1.5.0

## 2023-02-27

### v0.6.3

#### new function

- **New** Add multi-cloud custom resource module, support addition, deletion, modification, query, and distribution functions
- **NEW** Add multi-cloud routing module, support addition, deletion, modification, query and distribution functions

#### Optimization

- **Optimized** Load form supports auto-propagation fields
- **Optimized** Multi-cloud Service supports specifying the deployment cluster function
- **Optimized** load details, support clusters showing expected scheduling

#### fix

- **Fix** Fix the problem that the one-click upgrade of multi-cloud resources cannot display the member cluster
- **Fix** cronjob calculation of the total number of tasks and the number of current tasks is incorrect
- **Fix** Generate pp resource name issue
- **FIX** Cronjob not updating via yaml
- **Fix** Custom resource details page, deployment policy usage status display problem
- **FIXED** no mirror for kairship-ui in offline package

## 2022-12-25

### v0.5

#### new function

- **NEW** Add cronjob related interfaces such as adding, deleting, modifying and checking
- **NEW** Add related interfaces such as adding, deleting, modifying and checking jobs
- **NEW** Added one-click migration of multi-cluster applications for single-cluster applications, automatic upgrade of dependent resources
- **NEW** Add job and cronjob types to ListPropagationPolicies and ListInstanceOverridePolicies interfaces
- **NEW** ETCD high availability
- **NEW** Added priority field to deployment policy
- **NEW** New support for differentiation strategy imageOverride, CommandOverrider ArgsOverrider LabelsOverrider AnnotationsOverrider
- **NEW** If the deployment strategy has been used and associated with the workload, the deployment strategy does not support deletion
- **NEW** multi-cloud workload, new support for Job, CronJob
- **NEW** Differentiation strategy supports form-based creation and update
- **NEW** Deployment strategy supports form-based creation and update
- **NEW** Worker cluster supports displaying eviction status

#### Optimization

- **Optimized** Deployment policy form, new enable and disable switches for propagation constraints
- **Upgrade** the version of karmada-operator to v0.1.9, to solve the problem of pod anti-affinity of multiple instances of etcd

#### fix

- **FIXED** A user who is not associated with any role can view all instance information
- **Fix** When the scheduling algorithm is Duplicated, the total number of workload instances is incorrectly counted
- **Fix** When the scheduling algorithm is Duplicated, the total number of workload instances is incorrectly counted
- **FIXED** Data in ghippo was not deleted when instance was deleted
- **FIXED** When the instance is deleted, the labels of the working cluster are not removed
- **Fix** When removing a cluster, you can see the cluster being removed in the single-cluster application multi-cloud interface, and you can add the cluster being removed
- **Fix** Fix that in the process of removing the member cluster, one-click upgrade of the resources of the member cluster cannot be performed
- **FIX** unhealthy pair member cluster cannot be removed

## 2022-11-25

### v0.4

#### new function

- **Add** prometheus metrics, opentelemetry link trace
- **NEW** Displays the corresponding cluster list after creating a workload in a specified region
- **NEW** Displays the corresponding cluster list after creating a specified workload tag
- **NEW** Productization of failover failover

#### fix

- **Fix** estimator is not suitable for offline installation
- **Fixed** the problem that the stateless load display on the instance details page is abnormal

## 2022-10-21

### v0.3

#### new function

- **Add** multi-cloud orchestration enable permission verification
- **New** multi-cloud orchestration list instance interface, display data according to permissions
- **NEW** Multi-cloud orchestration query cluster resource overview information based on user permissions
- **NEW** multi-cloud orchestration to query the labels of all member clusters
- **NEW** One-click conversion of multi-cloud orchestration stand-alone cluster applications to multi-cluster applications
- **Add** multi-cloud orchestration to query the namespace and deployment resources of the member cluster
- **NEW** Added prompts for creating multi-cloud resources

#### Optimization

- **Optimize** multi-cloud orchestration optimizes the protobuf data structure of karmada PropagationPolicy and OverridePolicy

#### fix

- **Fix** Multi-cloud orchestration fixes the problem that the sorting of all PropagationPolicy resources under the instance does not take effect
- **Fix** multi-cloud orchestration fixes the problem of removing member clusters
- **FIX** Several bug fixes

## 2022-9-25

### v0.2

#### new function

- **Add** query interface for scheduling time
- **Add** multi-cloud service ConfigMap management interface
- **New** Create multiple resources and policy resources in batches
- **NEW** Service adds workload tags
- **NEW** Get the interface of Service under all namespaces
- **NEW** Added istio sidecar injection
- **New** When accessing the cluster, deploy the karmada estimator
- **New** multi-cloud secret interface
- **NEW** Added resource data collection of instance cpu and memery
- **NEW** Added event query API for instance

## 2022-8-21

### v0.1

#### new function

- **NEW** Added cloudshell API to manage karmada cluster through cloudshell
- **NEW** Added management interface for multi-cloud namespaces
- **Add** multi-cloud service management interface
- **Add** multi-cloud workload details related interface
- **NEW** Added support for setting cluster taint and tolerance
- **NEW** Download kubeconfig interface for karmada instance
- **NEW** Provide instance update API to support modification of instance alias and label

#### Optimization

- **Optimize** Optimize instance API and collect resource statistics of karmada instance