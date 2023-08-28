---
hide:
  - toc
---

# Create Multicloud Workload from Image

Follow the steps below to create a stateless load (Deployment).

1. In the left navigation bar, click `multicloud Workload` to enter the multicloud stateless workload page, and click the `Image Creation` button in the upper right corner.

    <!--screenshot-->

2. On the `Create Stateless Payload` page, after configuring the basic information of the payload, click `Next`.

    Among the basic information, we need to specify the corresponding deployment work cluster. Multicloud Management provides very detailed cluster deployment capabilities, which can fully match all the capabilities of Karmada.

    There are three ways to select a deployment cluster:

    - Specify cluster: Specify the working cluster you want to deploy from the current multicloud instance

        <!--screenshot-->

    - Designated area: You can choose three types: manufacturer, region, and availability zone, and multiple selections are supported. If the current selection cannot meet the requirements, you can expand the advanced deployment strategy and choose whether to exclude clusters, configure cluster taint tolerance, and dynamic region selection. Since the above conditions are not intuitive, we will also show the expected scheduled cluster for you to review.

        <!--screenshot-->

    - Specify tags: Support adding one or more tag information, the tag information is related to the tags of the working cluster, you can select the target cluster by filling in the tags and selecting different operators `exists` or `equal`. If the current selection cannot meet the requirements, you can expand the advanced deployment strategy and choose whether to exclude clusters, configure cluster taint tolerance, and dynamic region selection. Since the above conditions are not intuitive, we will also show the expected scheduled cluster for you to review.

        <!--screenshot-->

        Note that when selecting the scheduling strategy for the number of deployment replicas, you need to pay attention to the following instructions:
    
    - When the deployment type is `repeated`, it means that in each working cluster covered by all, an instance corresponding to the number of replicas is started
    - When the deployment type is `Aggregation` or `Dynamic Weight`, it refers to the total number of replicas that are set to be started in all covered working clusters
    
3. On the `Container Configuration` page, configure the basic information of the container where the load resides, support the selection of images (including public and private images), and choose to configure information such as life cycle and health check, and then click `Next`.

    <!--screenshot-->

4. On the `Advanced Configuration` page, assign the configuration upgrade policy, scheduling policy, label and comment, and DNS, and click `Next`.

    <!--screenshot-->

    If you do not need to configure differentiation after the creation is complete, you can directly use `Confirm` to complete the creation of the multicloud workload

5. On the `Differential Configuration` page, after selecting the personalized container configuration, labels and annotations, click `OK`.

    <!--screenshot-->

    You can add the corresponding differentiated configuration item in the list area on the left. After you add a differentiated configuration item, you need to specify the corresponding cluster.
    The selectable range of the cluster is only the cluster selected at the beginning, and the selected cluster will use the specified differential configuration; the unspecified cluster will still use the default configuration

6. A successful creation prompt will appear on the screen, you can now [create multicloud service](../resource/service.md)!

    <!--screenshot-->

!!! note

    - When creating a multicloud workload through mirroring, if you need to use the advanced capabilities of specifying a location and specifying a label to create, you need to ensure that the corresponding location or label has been set for the working cluster;
    Adding tags needs to be added within a single cluster, and can be jumped to the corresponding cluster maintenance from the working cluster management list.
    - When configuring the number of replicas, you need to pay attention to the corresponding scheduling strategy. Only when it is repeated, will all the configured replicas be started in multiple clusters.
    - Automatic Propagation: By default, resources such as ConfigMap and Secret depended on in the multicloud workload configuration are automatically detected. When the button is turned on, it means that these resources will be automatically propagated together with the multicloud workload.