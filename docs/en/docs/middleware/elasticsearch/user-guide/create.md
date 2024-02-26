---
hide:
  - toc
---

# Create an Elasticsearch Instance

In the list of Elasticsearch instances, do the following to create a new instance.

1. Click __New Instance__ in the upper right corner.

    ![New Instance](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/middleware/elasticsearch/images/create01.png)

2. Fill in the __Basic Information__ of the instance. After passing the __Install Environment Check__ , click __Next__ .

    > If the installation environment check is not passed, the page will give the reason for failure and operation suggestions. The common reason is the lack of related components, you can install the corresponding components according to the page prompts.

    ![Basic Information](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/middleware/elasticsearch/images/create02.png)

3. Choose the version: Choose which Elasticsearch version to create the instance based on, currently only supports __7.16.3__ 

    ![Specification Settings](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/middleware/elasticsearch/images/create03.png)

4. Refer to the following information to fill in the __Spec Settings__ of the instance.

    === "Data Node (enabled by default)"

        - Used for storing data, performing data-related operations such as adding, deleting, modifying, searching, aggregating, etc. Data nodes require high resources and need to configure sufficient resources.
        - **If the __Dedicated Master Node__ is not enabled, the __Data Node__ will act as the `Dedicated Master Node**.
        - At least 1 replica, up to 50 replicas, default 3 replicas.
        - It is recommended that the number of replicas is an odd number, otherwise there is a risk of brain split.

        ![Hot Data Node](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/middleware/elasticsearch/images/create03-1.png)

    === "Kibana Node (enabled by default)"

        - Kibana is a visualization analysis platform for Elasticsearch, which can search, view data stored in indexes and interact with it.
        - The __Kibana Node__ is enabled by default, which is used to store Elasticsearch visualization data nodes.
        - Default to 1 replica, cannot be modified.

        ![Kibana Node](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/middleware/elasticsearch/images/create03-2.png)

    === "Master Node"

        - The master node is responsible for lightweight operations within the cluster, such as creating/deleting indexes, monitoring the status of other types of nodes, deciding how to allocate data shards, etc.
        - **If the __Dedicated Master Node__ is not enabled, the data node will act as the master node**. This may result in a situation where the data node and the master node compete for resources, affecting system stability.
        - After enabling the __Dedicated Master Node__ , the master node is separated from the __Data Node__ , which is beneficial to ensure the stability of the service.
        - Default 3 replicas, cannot be modified.

        ![Master Node](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/middleware/elasticsearch/images/create03-3.png)

    === "Cold Node"

        - Stores historical data and other data with low query frequency and basically no need for writing.
        - At least 2 replicas, up to 50 replicas, default 3 replicas.
        - If there are both "high query frequency/high write pressure" and "low query frequency/basic no write" data in the business, it is recommended to enable the __Cold Data Node__ to achieve cold and hot data separation.
        - After enabling the __Cold Data Node__ , the __Dedicated Master Node__ will be automatically enabled.

        ![Cold Node](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/middleware/elasticsearch/images/create03-4.png)

5. Refer to the following instructions to fill in __Service Settings__ 

    - Access Mode: The type of Service corresponding to the Elasticsearch instance. For detailed explanations of various types, you can refer to [Service type](https://kubernetes.io/docs/concepts/services-networking/service/#publishing-services-service-types)
    - Access Settings: The username and password for accessing the Elasticsearch instance, and the access type of Kibana.

    ![Service Settings](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/middleware/elasticsearch/images/create04.png)

    - Node Affinity: After enabling, the Elasticsearch instance can only be scheduled to nodes with specific labels.
    - Workload Anti-Affinity: Distribute the Pods under the workload to multiple nodes within the topological domain (the scope of the anti-affinity effect) according to the anti-affinity, to avoid multiple Pods being centrally scheduled to a certain node, causing node overload. Related video tutorials can refer to [Workload Anti-affinity](../../../videos/mcamel.md#_1)
    - Collection Interval for Monitoring: The data collection interval for instance monitoring. If not set, the global setting will be used. The default is 30s.

    ![Service Settings](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/middleware/elasticsearch/images/create04-1.png)

6. Check the information filled in, confirm that it is correct and click __OK__ . If you need to modify, you can click __Previous__ to return to modify the configuration.

    ![Confirmation](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/middleware/elasticsearch/images/create05.png)

After the instance is successfully created, the page will automatically jump to the Elasticsearch instance list, where you can view the basic information and status of all instances.

![Successfully Created](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/middleware/elasticsearch/images/create06.png)
