---
hide:
  - toc
---

# access cluster

Through access to the cluster operation, it is possible to manage many cloud service platform clusters and local private physical clusters in a unified manner, forming a unified governance platform, effectively avoiding the risk of being locked in by manufacturers, and helping enterprises to safely migrate their business to the cloud.

The container management module supports access to a variety of mainstream container clusters, such as DaoCloud KubeSpray, DaoCloud ClusterAPI, DaoCloud Enterprise 4.0, Redhat Openshift, SUSE Rancher, VMware Tanzu, Amazon EKS, Aliyun ACK, Huawei CCE, Tencent TKE, and standard Kubernetes clusters.

## Prerequisites

- Prepare a cluster to be connected, ensure that the network between the container management cluster and the cluster to be connected is smooth, and the Kubernetes version of the cluster is 1.22+.
- The current operating user should have [`NS Edit`](../permissions/permission-brief.md) or higher permissions.

## Steps

1. Enter the `Cluster List` page, and click the `Connect to Cluster` button in the upper right corner.

    

2. Fill in the basic information.

    - Cluster name: The name should be unique and cannot be changed after setting. Maximum 63 characters, can only contain lowercase letters, numbers, and a separator ("-"), and must start and end with a lowercase letter or number.
    - Cluster Alias: You can enter any characters, no more than 60 characters.
    - Release version: The issuer of the cluster, including mainstream cloud vendors in the market and local private physical clusters.

3. Fill in the KubeConfig of the target cluster, click `Verify Config`, and the cluster can be successfully connected only after the verification is passed.

    > If you do not know how to obtain the KubeConfig file of the cluster, you can click `How to obtain kubeConfig` in the upper right corner of the input box to view the corresponding steps.
    

4. Confirm that all parameters are filled in correctly, and click `OK` in the lower right corner of the page.

    

!!! note

    - The status of the newly connected cluster is `Accessing`, and becomes `Running` after the access is successful.
    - If the cluster status is always `connecting`, please confirm whether the access script is successfully executed on the corresponding cluster. For more details about cluster status, please refer to [cluster status](cluster-status.md).