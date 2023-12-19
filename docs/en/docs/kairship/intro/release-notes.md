# Release Notes

This page lists the release notes of Multicloud Management module,
so that you can understand the evolution path and feature changes of each version.

## 2023-11-30

### v0.14

- **Added** support for audit logs
- **Added** differentiated configuration result display for workloads
- **Added** support for creating workloads from YAML, allowing batch creation of multiple resources

#### Fixes

- **Fixed** pagination issue when querying service workloads
- **Fixed** improved validation for replica count in workload topology constraints

#### Upgrades

- **Upgraded** karmada version to v1.7.0

## 2023-10-31

### v0.13

#### Bug Fixes

- **Fixed** the issue where corresponding Pods cannot be viewed when viewing svc.
- **Fixed** the issue of being unable to delete member clusters after enabling metricAdaptor.

## 2023-08-31

### v0.12

#### New Features

- **Added** Support for [Cross-Cluster Horizontal Pod Autoscaling (FHPA)](../best-practice/fhpa.md).

#### Bug Fixes

- **Fixed** the issue of continuous restart of kairship-apiserver.

## 2023-08-31

### v0.12

#### New Features

- **Added** Support for cross-cluster horizontal pod autoscaling (FHPA)

#### Bug Fixes

- **Fixed** the issue of continuous restarts of kairship-apiserver

## 2023-07-31

### v0.11

#### New Features

- **Added** support for viewing event information in resource details.

#### Optimizations

- **Optimized** the Karmada Operator project for the community edition of the cluster.

## 2023-06-30

### v0.10.3

#### New Features

- **Added** support for LoadBalancer type in Service.
- **Added** distribution status display for resources.
- **Added** multi-cloud audit logs.

#### Fixes

- **Fixed** the issue of audit log out of range.
- **Fixed** the duplicate icon issue when adding a working cluster to the multi-cloud instance details page.
- **Fixed** the error that occurs when modifying the number of instances while creating a multi-cloud workload.
- **Fixed** the icon style issue with the distribution status of multi-cloud resources.

#### Improvements

- **Improved**: Optimized the data source for excluding clusters in deployment strategies.

## 2023-05-29

### v0.9.1

#### New Features

- Edit Service tags, annotations in Web UI.

#### Fixes

- Overview of expected scheduling clusters on the resource details page.
- Occasional failure of kairship-proxy.
- No arm64 vesions of __cffssl__ and __kubectl__ .

#### Improvements

- Add a cluster column to the Ingress list.
- Reduce the propagation policy when converting single-cluster deployments to multicloud ones.

#### Upgrades

- `@dao-style/extend` to v1.2.1.
- cloudtty API to v0.5.2.

## 2023-04-27

### v0.8.0

#### New Features

- Cluster scheduling group
- Image selector selection
- Scheduled rescheduling
- Threshold for defining cluster health status

#### Bug Fixes

- If the deployment policy is the CR resource type, __kind__ is not automatically filled

#### Others

- Remove Istio sidecar injection for controller-manager and proxy
- Enhance warning message for deleting a multicloud instance

## 2023-03-29

### v0.7.4

#### New Features

- Custom cluster management
- Data storage for workloads
- Convert Services into multicloud resources when converting a single-cluster application to multicloud application
- Differentiated configuration of multicloud IngressClass
- Cluster-level deployment policies and override policies
- Custom permissions of roles

#### Improvement

- Choice to hide annotations prefixed with 'kairship.io/'
- Guide users to select cluster when setting override policies

#### Bug Fixes

- Services cannot be converted to multicloud resources when converting the applications
- Wrong link to Service Mesh module
- Incorrect front-end version
- Filter LB Service in clusters added into a multicloud instance when converting applications to multicloud applications
- Upgrade karmada version to v1.5.0

## 2023-02-27

### v0.6.3

#### New Features

- Management of multicloud custom resources, supporting CRUD and deployment actions
- Management of multicloud Services, supporting CRUD and deployment actions

#### Improvement

- Auto-propagation fields when creating a multicloud workload
- Specify the deployment position of multicloud Services
- Display expected clusters for scheduling in Workload Overview page

#### Bug Fixes

- Clusters cannot be displayed when converting single-cluster applications into multicloud applications
- Counting error of total CronJobs and Active CronJobs
- Issues related to generating propagation policy names
- Cronjobs cannot be updated via YAML files
- Status error of propagation policies in the overview page of custom resource
- There is no mirror for kairship-ui in offline package

## 2022-12-25

### v0.5

#### New Features

- Add APIs for CronJob CRUD actions
- Add APIs for Job CRUD actions
- Convert single-cluster applications to multicloud clusters and related resources
- Add Job and CronJob types to ListPropagationPolicies and ListInstanceOverridePolicies interfaces
- ETCD high availability
- Added priority field to propagation policy
- imageOverride, CommandOverrider ArgsOverrider LabelsOverrider AnnotationsOverrider in override policies
- Delete protection: if a propagation policy has been used and associated with a workload, it cannot be deleted
- New types of multicloud workload: Job, CronJob
- Create and update override policies with graphical forms
- Create and update propagation policies with graphical forms
- Display eviction status of worker clusters

#### Improvement

- Add Enable/Disenable slider for propagation constraints when creating propagation policies
- Upgrade the version of karmada-operator to v0.1.9, solving the problem of pod anti-affinity of multiple instances of etcd

#### Bug Fixes

- A user who is not associated with any role can view all instance information
- When the scheduling algorithm is Duplicated, the total number of workload instances is incorrectly counted
- Data in ghippo was not deleted when instance was deleted
- When the instance is deleted, the labels of the working cluster are not removed
- When a cluster is removed, it can still be added into a multicloud instance
- Unable to update resources when removing a cluster
- Unhealthy clusters cannot be removed

## 2022-11-25

### v0.4

#### New Features

- Prometheus metrics and Opentelemetry traces
- Filter clusters if the users specified a region when creating a deployment
- Filter clusters if the users specified a label when creating a deployment
- Failover

#### Bug Fixes

- estimator is not suitable for offline installation
- Status error of deployments in overview page

## 2022-10-21

### v0.3

#### New Features

- Enable permission verification
- list instance API that can display data according to permissions
- Query cluster resource information based on user permissions
- Query labels of all member clusters
- One-click conversion of single-clsuter applications to multicluster applications
- Query the namespace and deployment resources of the member cluster
- Added prompts for creating multicloud resources

#### Improvement

- The protobuf data structure of karmada PropagationPolicy and OverridePolicy

#### Bug Fixes

- Sorting all PropagationPolicy resources under the instance does not take effect
- Issues related removing member clusters
- Other bugs

## 2022-9-25

### v0.2

#### New Features

- API to query scheduling time
- API to manage configmaps of multicloud services
- Batch creation of resources and policies
- Add workload labels for Services
- API to get Service under all namespaces
- Istio sidecar injection
- Deploy the karmada estimator when adding a cluster into a multicloud instance
- API for multicloud secrets
- Collect CPU/Memory usage info of instances
- API to query instance events

## 2022-8-21

### v0.1

#### New Features

- Cloudshell API to manage Karmada clusters through cloudshell
- API to manage multicloud namespaces
- API to manage multicloud Services
- API to manage multicloud workload details
- Cluster taints and tolerance
- API to download kubeconfig of for Karmada instances
- API to update instance's alias and labels

#### Improvement

- Enhance instance API and collect resource statistics of Karmada instances
