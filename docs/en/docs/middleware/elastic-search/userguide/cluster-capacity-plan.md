# Elasticsearch cluster specifications and capacity planning

## Storage Capacity Planning

The main factors affecting the storage capacity of the `Elasticsearch` service:

- Number of replicas: Replicas are beneficial to increase data reliability, but at the same time increase storage costs. The default and recommended number of replicas is 1.
- Internal task overhead: `Elasticsearch` is used for `segment` merges, `ES Translog`, logs, and reserves about 20% of disk space.
- Index overhead: typically 10% larger than source data, exact overhead can be calculated using `_cat/indices?v` API and `pri.store.size` value.
- OS reservation: By default, Linux will reserve 5% of the disk space for the `root` user to handle critical processes, system recovery, and prevent disk fragmentation issues.

### Formula

Full formula | Simplified version
---|---
Source data * (1 + number of replicas) * (1 + index overhead) / (1 - Linux reserved space) / (1 - internal overhead) = minimum storage requirement | source data * (1 + number of replicas) * 1.45 = minimum storage requirements

If you have `500G` of data storage and need a replica, the minimum storage requirement is closer to `500 * 2 * 1.1 / 0.95 / 0.8 = 1.5T`.

## Cluster configuration

Deploy the recommended configuration in a production environment: try to have one node take on only one role. Different nodes require different computing resources. After different roles are separated, they can be expanded on demand without affecting each other.

- The maximum number of nodes in the cluster = single node CPU * 5
- The maximum capacity of a single-node disk

     - Search scenarios: Maximum disk capacity of a single node = memory size of a single node (GB) * 10.
     - Scenarios such as logs: Maximum capacity of a single-node disk = single-node memory size (GB) * 50.

Configuration | Maximum number of nodes | Maximum single-node disk capacity (query) | Maximum single-node disk capacity (log)
---|---|--|--
4 cores 16G | 20 | 160 GB | 800 GB
8 cores 32G | 40 | 320 GB | 1.5 TB
16 cores 64G | 80 | 640 GB | 2 TB

## Planning the number of slices

Applicable scene:

- Log type, frequent writing, less query, about 30G for a single shard
- Search class, less writing, frequent query, no more than 20G for a single shard

Each `Elasticsearch` index is divided into multiple shards, and the data is scattered into different shards according to the hash algorithm. Since the number of index shards affects read and write performance and fault recovery speed, it is recommended to plan ahead.

### Shard usage overview

- `Elasticsearch` in version 7.x defaults to `1 primary shard` and `1 replica shard` per index
- On a single node, the maximum number of shards in version 7.x is 1000
- Try to keep the size of a single fragment between `10-50G` for the best experience, and it is generally recommended to be around `30G`

     - Large shards can slow down recovery from failures in `Elasticsearch`
     - A shard that is too small may lead to a lot of shards, because each shard will take up some CPU and memory, resulting in read and write performance and insufficient memory.
  
- When the number of shards exceeds the number of data nodes, it is recommended that the number of shards be close to an integer multiple of the data nodes, so that the shards can be evenly distributed to the data nodes.
- For log scenarios, it is recommended to enable the ILM function. When the fragment size is found to be unreasonable, use this function to adjust the number of fragments in time.

### Index shard resource occupation

Each index and each shard requires some memory and CPU resources. In most cases, a small set of large shards uses fewer resources than many small shards.

Segments play an important role in the resource usage of shards. Most shards contain several segments, which store their index data.
`Elasticsearch` keeps segment metadata in JVM heap memory so that it can be quickly retrieved for searching.
As a shard grows, its segments are merged into fewer, larger segments. This reduces the number of segments, which means less metadata is kept in heap memory.

In order to reduce the number of indexes and avoid excessively large and unordered mappings, consider storing similarly structured data in the same index instead of dividing data into different indexes based on the data source.
It is important to strike a good balance between the number of indexes/shards and the map size for each individual index.
Since the cluster state will be loaded into the heap memory on each node (including the master node), and the size of the heap memory is proportional to the number of indexes and the number of fields in a single index and fragment, it is also necessary to monitor the heap memory on the master node at the same time. It is important to monitor the heap memory usage and make sure it is sized appropriately.

Shards that are too small result in too small segments, which in turn increases overhead. You want to try to keep the average size of your shards from at least a few gigabytes to a few tens of gigabytes.
For time-series data use cases, shard sizes are typically between 20GB and 40GB.

Since the overhead of a single shard depends on the number of segments and the size of the segments, forcing smaller segments to be merged into larger segments via the forcemerge operation can reduce overhead and improve query performance.
Ideally, this should be done when no more data is being written in the index. Please note: This is an extremely resource-intensive operation, so it should be done during off-peak hours.

The number of shards that can be stored on each node is proportional to the available heap size, but Elasticsearch does not enforce a fixed limit.
Here's a good rule of thumb: Make sure to keep the number of shards below 20 for each configured GB on your node.
A node with 30GB of heap memory can have up to 600 shards, but within this limit, the fewer shards you have, the better.
In general, this helps the cluster stay healthy.

For more information, please refer to:

- [Reduce the number of cluster shards](https://www.elastic.co/guide/en/elasticsearch/reference/7.17/size-your-shards.html#reduce-cluster-shard-count)

- [How many shards should I have in my Elasticsearch cluster? ](https://www.elastic.co/cn/blog/how-many-shards-should-i-have-in-my-elasticsearch-cluster)

### Shard calculation formula

(metadata + growth space) * (1 + index overhead) / required shard size = approximate number of primary shards

Assume there is `80GiB` of data. Expect to keep each shard around `30GiB`. So your number of shards should be approximately 80 * 1.1 / 30 = 3

### How to manage shards

Use index lifecycle management (ILM) to automatically manage indexes, and the management strategy is as follows:

- According to the index size, automatic rollover
- Automatic rollover based on index creation time
- Automatic rollover according to the number of documents

The index lifecycle execution policy is executed every 10 minutes by default, and the inspection frequency can be controlled by modifying the `indices.lifecycle.poll_interval` parameter.
