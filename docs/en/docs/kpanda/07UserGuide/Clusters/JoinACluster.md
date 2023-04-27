# Access cluster

Through access to the cluster operation, it is possible to manage many cloud service platform clusters and local private physical clusters in a unified manner, forming a unified governance platform, effectively avoiding the risk of being locked in by manufacturers, and helping enterprises to safely migrate their business to the cloud.

The container management platform supports access to a variety of mainstream container clusters:

- DaoCloud KubeSpray
- DaoCloud ClusterAPI
- DaoCloud Enterprise 4.0
- Redhat Openshift
- SUSE Rancher
- VMware Tanzu
- Amazon EKS
- Aliyun ACK
- Huawei CCE
- Tencent TKE
- Standard Kubernetes cluster

## Prerequisites

- Prepare a cluster to be connected, and ensure that the network between the container management cluster and the cluster to be connected is smooth.
- The current operating user should have [`NS Edit`](../Permissions/PermissionBrief.md) or higher.

## Fill in the basic configuration

1. Enter the `Cluster List` page, and click the `Connect to Cluster` button in the upper right corner.

    

2. On the `Access Container Cluster` page, configure basic information.

    - Cluster name: The name should be unique and cannot be changed after setting. The name has a maximum length of 63 characters, can only contain lowercase letters, numbers, and a separator ("-"), and must start and end with a lowercase letter or number.
    - Cluster Alias: You can enter any characters, no more than 60 characters.
    - Release version: The issuer of the cluster, including mainstream cloud vendors in the market and local private physical clusters. For local private physical clusters or cluster vendors not displayed in the list, you can select other vendors and customize the vendor name.

        

## Fill in the access configuration

1. In the `Access Configuration` area, click `How to get kubeConfig` in the upper right corner.

    

2. Follow the on-screen prompts to get the KubeConfig for the target cluster.

    

3. After filling in the KubeConfig of the target cluster, click `Validate Config`.

    If the information is correct, a successful verification prompt will appear in the upper right corner of the screen.

    

4. Confirm that all parameters are filled in correctly, and click `OK` in the lower right corner of the page.

    The page will automatically jump to the cluster list. The status of the newly connected cluster is `Accessing`, and becomes `Running` after the access is successful.

    

!!! note

    If the cluster status is always `connecting`, please confirm whether the access script is successfully executed on the corresponding cluster. For more details about cluster status, please refer to [Cluster Status](ClusterStatus.md).