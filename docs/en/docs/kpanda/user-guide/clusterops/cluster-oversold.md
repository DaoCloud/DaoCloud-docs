# Cluster Dynamic Resource Oversubscription

At present, many services have peak and off-peak periods. To ensure the performance and stability of a service, resources are usually requested based on peak demand when the service is deployed.
However, the peak period may be very short, causing resources to be wasted during off-peak periods.
**Cluster resource oversubscription** makes use of these requested-but-unused resources (that is, the difference between the requested amount and the used amount), thereby improving cluster resource utilization and reducing resource waste.

This document mainly describes how to use the cluster dynamic resource oversubscription feature.

## Prerequisites

- The container management module has [integrated a Kubernetes cluster](../clusters/integrate-cluster.md) or [created a Kubernetes cluster](../clusters/create-cluster.md), and the cluster UI can be accessed.
- A [namespace has been created](../namespaces/createns.md), and the user has been granted [Cluster Admin](../permissions/permission-brief.md) permissions.
  For details, refer to [Cluster Authorization](../permissions/cluster-ns-auth.md).
- If you are in an offline environment, you need to import the [Addon offline package](../../../download/addon/history.md), and the cro-operator chart must be available on the Helm Chart page.

## Enable Cluster Oversubscription

1. Click __Cluster List__ in the left navigation bar, and then click the name of the target cluster to enter the __Cluster Details__ page.

    ![Cluster List](../../images/cluster-oversold-01.png)

2. On the cluster details page, click __Operations and Maintenance__ -> __Cluster Settings__ in the left navigation bar, and then select the __Advanced Settings__ tab.

    ![Advanced Settings](../../images/cluster-oversold-02.png)

3. Turn on cluster oversubscription and set the oversubscription ratio.

    - If the cro-operator plugin is not installed, click the __Install Now__ button. For the installation procedure, refer to [Manage Helm Apps](../helm/helm-app.md).
    - If the cro-operator plugin is installed, turn on the cluster oversubscription switch and you can start using the cluster oversubscription feature.

    !!! note

        You need to add the following label to the corresponding namespace under the cluster for the cluster oversubscription policy to take effect.

    ```shell
    clusterresourceoverrides.admission.autoscaling.openshift.io/enabled: "true"
    ```

    ![Cluster Oversubscription](../../images/cluster-oversold-03.png)

## Use Cluster Oversubscription

After the cluster dynamic resource oversubscription ratio is set, it takes effect when workloads are running. The following uses nginx as an example to verify the resource oversubscription capability.

1. Create a workload named nginx and set the corresponding resource limits. For the creation procedure, refer to [Create a Stateless Workload (Deployment)](../workloads/create-deployment.md).

    ![Create a Workload](../../images/cluster-oversold-04.png)

2. Check whether the ratio of the Pod resource request value to the limit value of the workload matches the oversubscription ratio.

    ![Check Pod Resources](../../images/cluster-oversold-05.png)
