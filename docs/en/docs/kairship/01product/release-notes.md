# Multicloud Orchestration Release Notes

This page lists the Release Notes of multicloud orchestration, so that you can understand the evolution path and feature changes of each version.

##v0.4

Release date: 2022-11-25

- **Add** prometheus metrics, opentelemetry link trace
- **NEW** Displays the corresponding cluster list after creating a workload in a specified region
- **NEW** Displays the corresponding cluster list after creating a specified workload tag
- **NEW** Productization of failover failover
- **Fix** estimator is not suitable for offline installation
- **Fixed** the problem that the stateless load display on the instance details page is abnormal

## v0.3

Release date: 2022-10-21

- **Add** multicloud orchestration enable permission verification
- **New** multicloud orchestration list instance interface, display data according to permissions
- **NEW** Multicloud orchestration query cluster resource overview information based on user permissions
- **NEW** multicloud orchestration to query the labels of all member clusters
- **NEW** One-click conversion of multicloud orchestration stand-alone cluster applications to multi-cluster applications
- **Add** multicloud orchestration to query the namespace and deployment resources of the member cluster
- **NEW** Added prompts for creating multicloud resources
- **Fix** Multicloud orchestration fixes the problem that the sorting of all PropagationPolicy resources under the instance does not take effect
- **Fix** multicloud orchestration fixes the problem of removing member clusters
- **Optimize** multicloud orchestration optimizes the protobuf data structure of karmada PropagationPolicy and OverridePolicy
- **FIX** Several bug fixes

## v0.2

Release date: 2022-9-25

- **Add** query interface for scheduling time
- **Add** multicloud service ConfigMap management interface
- **New** Create multiple resources and policy resources in batches
- **NEW** Service adds workload tags
- **NEW** Get the interface of Service under all namespaces
- **NEW** Added istio sidecar injection
- **New** When accessing the cluster, deploy the karmada estimator
- **New** multicloud secret interface
- **NEW** Added resource data collection of instance cpu and memery
- **NEW** Added event query API for instance

## v0.1

Release date: 2022-8-21

- **NEW** Added cloudshell API to manage karmada cluster through cloudshell
- **NEW** Added management interface for multicloud namespaces
- **Add** multicloud service management interface
- **Add** multicloud workload details related interface
- **NEW** Added support for setting cluster taint and tolerance
- **NEW** Download kubeconfig interface for karmada instance
- **NEW** Provide instance update API to support modification of instance alias and label
- **Optimize** Optimize instance API and collect resource statistics of karmada instance