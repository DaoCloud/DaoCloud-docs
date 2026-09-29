# Deploy Elasticsearch Across Two Data Centers

## Background

Assume that ES is deployed according to the topology below. A potential problem exists: both replicas of an index shard may land in zone-1. If a disaster occurs in zone-1, all data of that shard will be lost. You need to use the ES configuration to distribute shard replicas across zone-1 and zone-2.

## Steps

1. Log in to the console and add labels to the nodes located in different data centers in the cluster. Assume that work1 and work2 are in one data center, and work3 is in another:

    ![00](../../elasticsearch/images/es2-01.png)

2. The ES configuration mainly consists of two parts: one is the scheduling configuration for ES nodes, and the other is the configuration of the ES configuration files.

### Node Scheduling Configuration

- In the ES YAML, we need to configure two nodeSets (one nodeSet corresponds to one StatefulSet).

    ![00](../../elasticsearch/images/es2-02.png)

- Using affinity and antiaffinity configurations, distribute two of the ES nodes in zone1 and the other ES node in zone2:

    ![00](../../elasticsearch/images/es2-03.png)

### Configuration File Settings

After dividing zone-1 and zone-2 into two nodeSets, you can configure their configuration files separately. The relevant configurations are:

- cluster.routing.allocation.awareness.attributes
- node.attr.zone
- cluster.routing.allocation.awareness.force.zone.values

1. The configuration for the nodes in zone-1 is:

    ```shell
    node.attr.zone: zone-1
    cluster.routing.allocation.awareness.attributes: zone
    cluster.routing.allocation.awareness.force.zone.values: zone-1,zone-2
    ```

2. The configuration for the nodes in zone-2 is:

    ```shell
    node.attr.zone: zone-2
    cluster.routing.allocation.awareness.attributes: zone
    cluster.routing.allocation.awareness.force.zone.values: zone-1,zone-2
    ```
