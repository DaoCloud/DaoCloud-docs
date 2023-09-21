# Cluster Mode to Sentinel Mode

Redis-shake supports data synchronization and migration between instances deployed in different deployment modes. In this example, we will demonstrate the synchronization configuration methods between a 3-master 3-slave cluster mode instance and a 3-replica sentinel mode instance.

Let's assume that Redis **instance redis-a** is configured in a 3-master 3-slave cluster mode, while **instance redis-b** is set up as a 3-replica sentinel mode instance. These two instances are part of separate clusters. We will now build a synchronization structure where **instance redis-a** acts as the master instance and **instance redis-b** serves as the slave instance, providing the following disaster recovery support:

- Under normal conditions, **instance redis-a** serves external requests and continuously synchronizes data from **instance redis-a** to **instance redis-b**.
- In the event of a failure or offline state of the master **instance redis-a**, **instance redis-b** takes over and serves external requests.
- Once the master **instance redis-a** is restored and comes back online, **instance redis-b** performs incremental data rewriting to **instance redis-a**.
- After the data recovery of **instance redis-a** is complete, it switches back to the initial state, with **instance redis-a** serving requests and maintaining continuous data synchronization with **instance redis-b**.

!!! note

    The method of data transfer depends on the source instance. In the `data synchronization` phase, the source instance **redis-a** is in cluster mode, so you need to deploy a Redis-shake (Redis-shake-sync) for each of the three leader replicas. In the `data recovery` phase, the source instance **redis-b** is in sentinel mode, so only one Redis-shake (Redis-shake-recovery) needs to be deployed.

## Data Synchronization Deployment

Diagram: Data synchronization from **instance redis-a** to **instance redis-b**

### Configuring Service for **Instance redis-a**

For each Leader Pod of the Redis instance, create a `NodePort` service for data synchronization access via Redis-Shake. In this example, we need to create services for the 3 Leader Pods of **instance redis-a**. Let's take the example of Pod `redis-a-leader-0` and create a service for it:

1. Go to `Container Management` - `Source Cluster` - `Stateful Workloads`: Select the workload `redis-a-leader` and create a service named `redis-a-leader-svc-0` with access type `NodePort`. Both the container port and service port should be set to 6379.

2. Verify the created service and ensure that the workload selector contains the following labels:

    ```yaml
    app.kubernetes.io/component: redis
    app.kubernetes.io/managed-by: redis-operator
    app.kubernetes.io/name: redis-a
    role: leader
    # Make sure to choose the correct leader pod name for pod-name
    statefulset.kubernetes.io/pod-name: redis-a-leader-0
    ```

Repeat the above steps to create services for `redis-a-leader-1` and `redis-a-leader-2`.

### Configuring Service for **Instance redis-b**

Referring to the diagram "Data synchronization from **instance redis-a** to **instance redis-b**," it can be seen that **instance redis-b** is in the same cluster as `redis-shake`. Therefore, you only need to create a ClusterIP service for **instance redis-b** that points to port 6379, as shown in the image below:


### Deploying Redis-Shake

Redis-Shake usually runs on the same cluster and namespace as the target Redis instance for data transfer. Therefore, in this example, to achieve data synchronization, you need to deploy Redis-Shake in the cluster where **instance redis-b** is located. Here's how to configure it:

Note: In cluster mode, Redis-Shake requires a one-to-one relationship with the leader pod of the source Redis instance (refer to the diagram "Data synchronization from **instance redis-a** to **instance redis-b**"). Hence, you need to deploy 3 independent instances of Redis-Shake. Let's take `redis-a-leader-0` as an example and create `Redis-shake-sync-0`:

#### 1. Create configuration items

In `Container Management` - `Target Cluster` - `Configuration & Storage` - `Configuration Items`, create a configuration item named `redis-sync-0` for the Redis-Shake instance. Import the file `sync.toml` (see appendix for file contents) and make sure to modify the following content:


- source.address: Service address of the source **instance redis-a**'s `redis-a-leader-svc-0`:

    ```toml
    address = "10.233.109.145:32283"
    ```
    
- Access password for the source instance: You can obtain this information from the overview page of the source instance in `Data Services`:

    ```toml
    password = "3wPxzWffdn" # keep empty if no authentication is required
    ```

- Access address for the target instance, using the ClusterIP service created for **instance redis-b** (port 6379) as the target's address:

    ```toml
    # Note: Since the headless service can directly connect to the workload, you can access the default port 6379 through this service.
    address = "10.233.16.241:6379"
    ```

- Access password for the target instance: You can obtain this information from the Redis instance overview page in the `Data Services` module:

    ```toml
    password = "3wPxzasd" # keep empty if no authentication is required
    ```

- Set the target type to `standalone`:

    ```toml
    [target]
    type = "standalone" # "standalone" or "cluster"
    ```

### Deploying Redis-Shake

#### Create Redis-Shake

1. Open `Application Workbench`, select `Wizard` - `Based on Container Image`, and create an application named `Redis-shake-sync-0`.


2. Fill in the application configuration details as follows:

    - The cluster and namespace of the application should match the Redis instance.
    - Image address:

        ```yaml
        release.daocloud.io/ndx-product/redis-shake@sha256:46652d7d8893fa4508c3c6725afc1e211fb9cb894c4dc85e94287395a32fc3dc
        ```

    - Set the access type of the default service to NodePort, with container port and service port set to 6379.


    - In `Advanced Settings` - `Lifecycle` - `Startup Command` - `Run Arguments`, enter:

        ```yaml
        /etc/sync/sync.toml
        ```

    - In `Advanced Settings` - `Data Storage`, add a configuration item named `redis-sync-0`, and make sure the path is set to:

        ```yaml
        /etc/sync
        ```

    - In `Advanced Settings` - `Data Storage`, add a temporary path with read and write permissions set to "Read/Write", and the container path must be:

        ```yaml
        /data
        ```


3. Click `OK` to complete the creation of Redis-Shake.

Repeat the above steps to create `Redis-shake-sync-1` and `Redis-shake-sync-2` for the other two Leader Pods.

After creating Redis-Shake, the data synchronization between Redis instances has started. You can use the `redis-cli` tool to verify the synchronization. Here, we will not go into further details.

## Data Recovery

Diagram: Data recovery from **instance redis-b** to **instance redis-a**

When the source instance **instance redis-a** goes offline due to a failure, the target instance **instance redis-b** takes over and starts serving requests. During this time, new data will be generated on the target instance. When the source instance **instance redis-a** comes back online, it needs to recover the incremental data from **instance redis-b**. At this point, the roles of **instance redis-a** and **instance redis-b** are swapped, and **instance redis-b** becomes the data source that synchronizes data to **instance redis-a**.

Refer to the diagram "Data recovery from **instance redis-b** to **instance redis-a**." Since **instance redis-a** is in cluster mode, you need to deploy 3 Redis-Shake instances in its cluster to achieve data recovery from **instance redis-b** to **instance redis-a**. Configure them as follows:

!!! note

    Before bringing **instance redis-a** back online, make sure to shut down the 3 Redis-Shake instances (`Redis-shake-sync-0`, `Redis-shake-sync-1`, `Redis-shake-sync-2`) used for **instance redis-a** >> **instance redis-b** data synchronization to avoid incorrect data synchronization that may overwrite new data.

### Configuring Service for **Instance redis-b**

In the recovery process, **instance redis-b** acts as the data source. Therefore, you need to create a NodePort service for this instance to enable cross-cluster access for Redis-Shake.

Since the data source **instance redis-b** is in sentinel mode, you only need to create one service. Here's how to create it:

1. Go to `Container Management` - `Source Cluster` - `Stateful Workloads`: Select the workload `redis-b` and create a `NodePort` service named `redis-b-recovery-svc`. Both the container port and service port should be set to 6379.


2. Verify the created service and ensure that the workload selector contains the following labels:

    ```yaml
    app.kubernetes.io/component: redis
    app.kubernetes.io/managed-by: redis-operator
    app.kubernetes.io/name: redis-b
    app.kubernetes.io/part-of: redis-failover
    redis-failover: master
    redisfailovers.databases.spotahome.com/name: redis-b
    ```

### Deploying Redis-Shake

Redis-shake is usually run on the same cluster as the target Redis instance for data transfer. Therefore, in this example, to achieve data synchronization, Redis-shake needs to be deployed on the target side and configured as follows.

#### Create Configuration Item

In `Container Management` - `Source Cluster` - `Configuration & Storage` - `Configuration Items`, create a configuration item named `redis-sync` for the Redis-shake instance. Import the `sync.toml` file (see `Appendix` for file content), and make sure to modify the following:


- source.address: The source is now **instance redis-b**, so enter the service address created for that instance in the previous step:

    ```toml
    address = "10.233.109.145:32283"
    ```
    
- Access password for the source instance: You can obtain this information from the overview page of **instance redis-b**:

    ```toml
    password = "3wPxzWffdn" # keep empty if no authentication is required
    ```

- Target instance access address: The target instance is now **instance redis-a**, and you can use the default service `redis-a-leader` (port: 6379) created by the system, so no need to create it:

    ```toml
    address = "172.30.120.202:6379"
    ```

    This configuration can be found in `Cluster Management` - `Cluster where redis-a is located` - `Workloads` - `Access Method`. As shown in the following figure:


    Click on the service name to enter the service details and you can see the ClusterIP address:


- Access password for the target instance: You can obtain this information from the overview page of **instance redis-a**:

    ```toml
    password = "3wPxzWffss" # keep empty if no authentication is required
    ```

- Since the data receiver is now **instance redis-b**, the target type needs to be set to `cluster`:

    ```toml
    [target]
    type = "cluster" # "standalone" or "cluster"
    ```

#### Create Redis-Shake

1. Open `Application Workbench`, select `Wizard` - `Based on Container Image`, and create an application named `Redis-shake-recovery`.


2. Fill in the application configuration details as follows:

    - The cluster and namespace of the application should match the Redis instance.
    - Image address:

        ```yaml
        release.daocloud.io/ndx-product/redis-shake@sha256:46652d7d8893fa4508c3c6725afc1e211fb9cb894c4dc85e94287395a32fc3dc
        ```

    - Set the access type of the default service to NodePort, with container port and service port set to 6379.


    - In `Advanced Settings` - `Lifecycle` - `Startup Command` - `Run Arguments`, enter:

        ```yaml
        /etc/sync/sync.toml
        ```


    - In `Advanced Settings` - `Data Storage`, add a configuration item named `redis-sync`, and make sure the path is set to:

        ```yaml
        /etc/sync
        ```

    - In `Advanced Settings` - `Data Storage`, add a temporary path with read and write permissions set to "Read/Write", and the container path must be:

        ```yaml
        /data
        ```

3. Click `OK` to complete the creation of Redis-Shake.


After creating Redis-Shake, the data synchronization between Redis instances has started. You can use the `redis-cli` tool to verify the synchronization. Here, we will not go into further details.

## Restoring Master-Slave Relationship

To restore the initial master-slave synchronization relationship **instance redis-a** >> **instance redis-b**, you need to stop the currently running `Redis-shake-sync` instances in the cluster where **instance redis-a** is located in `Container Management`. Then, restart the 3 `Redis-shake` instances in the cluster where the target instance is located to rebuild the initial master-slave relationship.


## Appendix

??? note “Click to see the full code” title="sync.toml"

    ```toml
    type = "sync"
     
    [source]
    version = 6.0 # redis version, such as 2.8, 4.0, 5.0, 6.0, 6.2, 7.0, ...
    address = "10.233.109.145:6379"
    username = "" # keep empty if not using ACL
    password = "3wPxzWffdn" # keep empty if no authentication is required
    tls = false
    elasticache_psync = "" # using when source is ElastiCache. ref: https://github.com/alibaba/RedisShake/issues/373
     
    [target]
    type = "cluster" # "standalone" or "cluster"
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
