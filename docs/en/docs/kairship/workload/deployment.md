---
hide:
  - toc
---
# Create Multicloud Deployment from Image

After [added a worker cluster](../cluster.md#_2) into a multicloud instance, you can create multicloud workloads or [convert existing workloads into multicloud workloads](promote.md).

This page will introduce how to create a multicloud deployment from an image. For the YAML method, see [Create Multicloud Deployment from YAML](yaml.md)

## Prerequisites

- [Create a multicloud instance](../instance/add.md)
- [Add at least one worker cluster to the multicloud instance](../cluster.md#_2)
- If you want to deploy workloads to specific clusters based on region, availability zone, or labels, you need to add region, availability zone, and label information to the clusters beforehand.

## Steps

Follow the steps below to create a multicloud deployment from an image.

1. Click the name of the multicloud instance, then navigate to __MultiCloud Workloads__ in the left navigation pane, and click __Create from Image__ in the top right corner.

    ![Create from Image](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/kairship/images/deploy-create04.png)

2. Fill in the basic information as per the instructions provided.

    - Specify Clusters: Select the specific cluster to deploy the multicloud workload.
    - Specify Regions: Filter clusters based on the provider/region/availability zone. You can enable all three filters simultaneously.

        - __Exclude Clusters__ : Exclude a specific cluster from the filtering result. The workload will not be deployed to the excluded cluster. If you do not specify the target cluster, it will be deployed to all clusters by default.
        - __Cluster Taint Tolerance__ : After adding a taint to the cluster in the [Cluster](../cluster.md#_6) page, resources with that taint cannot be scheduled to that cluster. Enabling taint tolerance here allows resources with the corresponding taint to be scheduled to the selected cluster.
        - __Dynamic Regions__ : Dynamically deploy workloads to clusters in different regions to ensure cross-region high availability.

            ![Specify Region](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/kairship/images/deploy-create05.png)

    - Specify Labels: Deploy the workload to specific clusters based on labels.

        - You can add one or multiple cluster labels.
        - Operator - __In__ : The node must contain the selected labels, and the label value must belong to the value group you defined. Multiple values are separated by __;__ .
        - Operator - __Exists__ : The node only needs to have the label and its value doesn't matter.

            ![Specify Labels](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/kairship/images/deploy-create06.png)

    - Auto Propagation: When enabled, it automatically detects ConfigMaps, Secrets, and other resources that the multicloud workload depends on, and propagates these resources to each selected deployment cluster.
    - Pods: Set the number of replicas for the multicloud workload.
    - Deployment Policies

        - __Duplicated__ : Deploy the number of replicas set in the __Pods__ field to each selected cluster. __Total Replicas = Pod number ✖️ Cluster number__ 
        - __Aggregated__ : Distribute the number of replicas set in the __Pods__ field to as few clusters as possible. __Total Replicas = Pod number__ 
        - __Dynamic Weight__ : Dynamically distribute workloads subject to the available resources in each cluster. __Total Replicas = Pod number__ 

    !!! note

        - If cannot find your target cluster, you can either reduce filtering conditions or [add new worker clusters](../cluster.md#_2).
        - After setting the __Pods__ and __Deployment Policies__ , the total number of replicas to be deployed will be displayed below the selected policy.

3. Refer to the [container configuration](../../kpanda/user-guide/workloads/create-deployment.md#_4) to fill in the container settings.

4. Refer to the [advanced configuration](../../kpanda/user-guide/workloads/create-deployment.md#_6) to fill in the advanced settings.

    !!! note

        - If you don't need differentiated configurations, simply click __OK__ in the lower right corner to complete the creation.
        - If you need differentiated configurations, click __Next__ and refer to instructions below to add more settings.

5. Refer to the instructions below to fill in the differentiated configurations, and click __OK__ .

    - __Default__ : This refers to the general configuration filled in the previous steps and cannot be modified here.
    - If you need to modify the default configuration, you need to click __Previous__ at the bottom of the page to return to the corresponding configuration environment and re-enter the information.
    - Below the default configuration, click the __+__ button and select a cluster to set differentiated configurations for that specific cluster, different from other clusters.
    - Clusters that do not have differentiated configurations will use the default configuration.
    - Currently, you can configure different container images, environment variables, labels, and annotations for different clusters.

        ![Differentiated Configurations](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/kairship/images/deploy-create07.png)

You will be automatically redirected to the list of multicloud deployments. By clicking the "More Actions" button on the right side, you can edit the YAML of the workload, update/pause/restart/delete the workload.

![More Actions](../images/deploy-update01.png)
