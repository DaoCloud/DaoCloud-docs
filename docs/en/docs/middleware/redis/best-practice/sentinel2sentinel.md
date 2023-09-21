# Sentinel mode to Sentinel mode

Redis-shake supports data synchronization and migration capabilities between Sentinel mode instances. In this example, we will demonstrate the configuration method for cross-cluster synchronization using a 3-replica Sentinel mode Redis.

Let's assume that **instance redis-a** and **instance redis-b** are in different clusters. Both instances are running in a 3-replica Sentinel mode. We will set up a synchronization structure where **instance redis-a** acts as the master instance and **instance redis-b** acts as the slave instance, providing the following disaster recovery support:

- Under normal circumstances, **instance redis-a** serves external requests and continuously synchronizes data to **instance redis-b**.
- If the master **instance redis-a** goes offline due to a failure, **instance redis-b** takes over and serves external requests.
- Once the master **instance redis-a** recovers, the incremental data is written back from **instance redis-b** to **instance redis-a**.
- After the data recovery of **instance redis-a** is complete, it switches back to the initial state where **instance redis-a** serves external requests and continues data synchronization with **instance redis-b**.

!!! note

    Data synchronization and data recovery need to be performed by different Redis-shake instances. Therefore, in this example, we need to create two Redis-shake instances: `Redis-shake-sync` and `Redis-shake-recovery`.

## Data Synchronization Deployment

Diagram: Data synchronization **instance redis-a** >> **instance redis-b**

![sync](../images/sync12.png)

### Configuring Service for the Source Instance

If the source instance is in a DCE 5.0 cluster, you can enable the solution in `Data Services` - `Redis` - `Cross-Cluster Master-Slave Synchronization`, and the service configuration will be automatically completed.

![svc](../images/sync17.png)

If the source instance is in a third-party cluster, you need to manually configure the service. The configuration method is described below:

Create a `NodePort` service for the Redis instance to allow data synchronization access from Redis-Shake. In this example, we need to create one service for **instance redis-a**. Here's the process:

1. Go to `Container Management` - `Cluster where the source instance is located` - `Stateful Workloads`: Select the workload `redis-a` and create a `NodePort` service with the container port and service port set to 6379.

    ![svc](../images/sync03.png)

2. Verify the service and make sure that the workload selector includes the following labels.

    ```yaml
    app.kubernetes.io/component: redis
    app.kubernetes.io/managed-by: redis-operator
    app.kubernetes.io/name: redis-a
    app.kubernetes.io/part-of: redis-failover
    redis-failover: master
    redisfailovers.databases.spotahome.com/name: redis-a
    ```

#### Creating Configuration

In `Container Management` - `Cluster where the target instance is located` - `Configuration and Storage` - `Configurations`, create a configuration item `redis-sync` for the Redis-shake instance. Import the file `sync.toml` (file content can be found in the `Appendix`), and make sure to modify the following:

![conf](../images/sync15.jpg)

- source.address: The service address of the source instance `redis-a` created in the previous step:

    ```toml
    address = "10.233.109.145:31278"
    ```

- Access password for the source instance: This can be obtained from the Overview page of the Redis instance:

    ```toml
    password = "3wPxzWffdn" # keep empty if no authentication is required
    ```

    ![conf](../images/sync16.png)

- Address for accessing the target instance. This address can either be the newly created `ClusterIP` service address or the default `Headless` service address `rfr-redis-b` of the instance `redis-b`. In this example, we use the `Headless` service address:

    ```toml
    address = "rfr-redis-b:6379"
    ```

    You can find this service information in `Cluster Management` - `Cluster where the target instance is located` - `Workloads` - `Access Method`. Similar to the following screenshot:

    ![conf](../images/sync22.png)

- Access password for the target instance. This can be obtained from the Redis instance's Overview page under the Data Services module:

    ```toml
    password = "3wPxzWffdn" # keep empty if no authentication is required
    ```

    Similar to the following location:

    ![svc](../images/sync06.png)

- Set the target type to `standalone`:

    ```toml
    [target]
    type = "standalone" # "standalone" or "cluster"
    ```

#### Creating Redis-shake

1. Open the `App Workbench`, select `Wizard` - `Based on Container Image` and create an application `Redis-shake-sync`:

    ![sync](../images/sync07.png)

2. Fill in the application configuration as per the instructions below.

    - The cluster and namespace of the application should match the Redis instance.
    - Image address:

        ```yaml
        release.daocloud.io/ndx-product/redis-shake@sha256:46652d7d8893fa4508c3c6725afc1e211fb9cb894c4dc85e94287395a32fc3dc
        ```

    - The access type for the default service is set to NodePort, with container port and service port both set to 6379.

        ![sync](../images/sync08.png)

    - `Advanced Settings` - `Lifecycle` - `Startup Command` - Enter the run parameter:

        ```yaml
        /etc/sync/sync.toml
        ```

        ![sync](../images/sync09.png)

    - `Advanced Settings` - `Data Storage`: Add configuration item `redis-sync` and set the path to:

        ```yaml
        /etc/sync
        ```

    - `Advanced Settings` - `Data Storage`: Add a temporary path with the container path set to:

        ```yaml
        /data
        ```

       ![sync](../images/sync20.png)

3. Click `OK` to complete the creation of Redis-shake.

Once Redis-shake is created, data synchronization between Redis instances will begin. You can verify the synchronization using the `redis-cli` tool, but we won't go into detail here.

## Data Recovery

Diagram: Data Recovery **instance redis-b** >> **instance redis-a**

![recovery](../images/sync13.png)

When the source instance **instance redis-a** comes back online, we need to recover the incremental data from the target instance **instance redis-b**. This requires deploying another Redis-shake instance on **instance redis-a** to achieve data recovery from **instance redis-b** to **instance redis-a**. The configuration process is similar to the data synchronization process, but in the opposite direction. Once the Redis-shake is created, data recovery will automatically begin.

!!! note

    Before bringing the source instance online, make sure to stop the `Redis-shake-sync` used for normal synchronization to avoid incorrect synchronization overwriting newly added data.

## Restoring the Master-Slave Relationship

To restore the initial master-slave synchronization relationship **instance redis-a** >> **instance redis-b**, stop the running `Redis-shake-recovery` instance in the cluster where **instance redis-a** is located in the `Container Management`. Then, restart the `Redis-shake-sync` instance in the target cluster, and the initial master-slave relationship will be reestablished.

![sync](../images/sync11.png)

## Appendix

```toml title="sync.toml"
type = "sync"
 
[source]
version = 6.0 # redis version, such as 2.8, 4.0, 5.0, 6.0, 6.2, 7.0, ...
address = "10.233.109.145:6379"
username = "" # keep empty if not using ACL
password = "3wPxzWffdn" # keep empty if no authentication is required
tls = false
elasticache_psync = "" # using when source is ElastiCache. ref: https://github.com/alibaba/RedisShake/issues/373
 
[target]
type = "standalone" # "standalone" or "cluster"
version = 6.0 # redis version, such as 2.8, 4.0, 5.0, 6.0, 6.2, 7.0, ...
# When the target is a cluster, write the address of one of the nodes.
# redis-shake will obtain other nodes through the `cluster nodes` command.
address = "10.233.103.2:6379"
username = "" # keep empty if not using ACL
password = "Aa123456" # keep empty if no authentication is required
tls = false
 
[advanced]
dir = "data"
 
# runtime.GOMAXPROCS, 0 means use runtime.NumCPU() cpu cores
ncpu = 4
 
# pprof port, 0 means disable
pprof_port = 0
 
# metric port, 0 means disable
metrics_port = 0
 
# log
log_file = "redis-shake.log"
log_level = "info" # debug, info or warn
log_interval = 5 # in seconds
 
# redis-shake gets key and value from rdb file, and uses RESTORE command to
# create the key in target redis. Redis RESTORE will return a "Target key name
# is busy" error when key already exists. You can use this configuration item
# to change the default behavior of restore:
# panic:   redis-shake will stop when meet "Target key name is busy" error.
# rewrite: redis-shake will replace the key with new value.
# ignore:  redis-shake will skip restore the key when meet "Target key name is busy" error.
rdb_restore_command_behavior = "rewrite" # panic, rewrite or skip
 
# pipeline
pipeline_count_limit = 1024
 
# Client query buffers accumulate new commands. They are limited to a fixed
# amount by default. This amount is normally 1gb.
target_redis_client_max_querybuf_len = 1024_000_000
 
# In the Redis protocol, bulk requests, that are, elements representing single
# strings, are normally limited to 512 mb.
target_redis_proto_max_bulk_len = 512_000_000
```
