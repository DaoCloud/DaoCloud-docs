---
hide:
  - toc
---

# Integrate Clusters

With the function of integrating clusters, DCE 5.0 allows you to manage on-premise and cloud clusters of various providers in a unified manner. This is quite important in avoiding the risk of being locked in by a certain providers, helping enterprises safely migrate their business to the cloud.

In DCE 5.0 Container Management module, you can integrate a cluster of the following providers: standard Kubernetes clusters, Redhat Openshift, SUSE Rancher, VMware Tanzu, Amazon EKS, Aliyun ACK, Huawei CCE, Tencent TKE, etc.

## Prerequisites

- Prepare a cluster of K8s v1.22+ and ensure its network connectivity.
- The operator should have the [NS Editor](../permissions/permission-brief.md) or higher permissions.

## Steps

1. Enter Container Management module, and click `Integrate Cluster` in the upper right corner.

    ![screen](../../images/cluster-integrate01.png)

2. Fill in the basic information by referring to the following instructions.

    - Cluster Name: It should be unique and cannot be changed after the integration. Maximum 63 characters, can only contain lowercase letters, numbers, and a separator ("-"), and must start and end with a lowercase letter or number.
    - Cluster Alias: Enter any characters, no more than 60 characters.
    - Release Distribution: the cluster provider, support mainstream vendors listed at the beginning.

3. Fill in the KubeConfig of the target cluster and click `Verify Config`. The cluster can be successfully connected only after the verification is passed.

    > Click `How do I get the KubeConfig?` to see the specific steps for getting this file.

    ![screen](../../images/cluster-integrate03.png)

4. Confirm that all parameters are filled in correctly and click `OK` in the lower right corner of the page.

!!! note

    The status of the newly integrated cluster is `Integrating`, which will become `Running` after the integration succeeds.
