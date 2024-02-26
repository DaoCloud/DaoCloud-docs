# Cluster Mode to Cluster Mode

Redis-shake supports data synchronization and migration capabilities between instances in cluster mode. In this example, we demonstrate the configuration method for cross-cluster synchronization using a 3-master 3-slave cluster mode Redis setup.

Assuming that Redis **instance redis-a** and **instance redis-b** are in different clusters, both of them being in a 3-master 3-slave cluster mode, we will set up a synchronization structure where **instance redis-a** acts as the master instance and **instance redis-b** acts as the slave instance, providing the following disaster recovery support:

- Under normal circumstances, **instance redis-a** provides services externally and continuously synchronizes data to **instance redis-b**.
- When the master **instance redis-a** fails and goes offline, **instance redis-b** takes over and provides services.
- After the master **instance redis-a** recovers and comes back online, **instance redis-b** writes back incremental data to **instance redis-a**.
- Once data recovery is complete for **instance redis-a**, it switches back to the initial state, where **instance redis-a** provides services and continues data synchronization with **instance redis-b**.

!!! note

    Data synchronization and data recovery need to be completed through different Redis-shake groups. Therefore, in this example, two sets of Redis-shake instances (Redis-shake-sync/Redis-shake-recovery) containing a total of 6 Redis-shake instances are created.

## Data Synchronization Deployment

Diagram: Data Synchronization  **instance redis-a** >> **instance redis-b**

### Configuring Services for the Source Instance

If the source instance is part of a DCE 5.0 cluster, you can enable the solution under __Data Services__ - __Redis__ - __Solutions__ - __Cross-cluster Master-Slave Synchronization__ , which will automatically configure the services.

If the source instance is in a third-party cluster, manual service configuration is required. The configuration process is described below:

Create a __NodePort__ service for each leader pod of the Redis instance to allow access for Redis-Shake data synchronization. In this example, we need to create services for the 3 leader pods of **instance redis-a**.

Taking Pod __redis-a-leader-0__ as an example, create a service for it:

1. Go to __Container Management__ - __Source Redis Cluster__ - __Stateful Workloads__ : Select the workload __redis-a-leader__ and create a service named __redis-a-leader-svc-0__ , with access type set as __NodePort__ , and container port and service port both set to 6379.

2. View the service and make sure that the workload selector includes the following labels:

    ```yaml
    app.kubernetes.io/component: redis
    app.kubernetes.io/managed-by: redis-operator
    app.kubernetes.io/name: redis-a
    app.kubernetes.io/part-of: redis-failover
    role: leader
    # Make sure to select the correct leader pod name for pod-name
    statefulset.kubernetes.io/pod-name: redis-a-leader-0
    ```

Repeat the above steps to create services for __redis-a-leader-1__ and __redis-a-leader-2__ .

### Deploying Redis-shake

Redis-shake is typically deployed on the same cluster as the target Redis instance for data transfer. Therefore, in order to achieve data synchronization in this example, we need to deploy redis-shake on the target side and configure it as follows.

Note that in cluster mode, Redis-shake requires a one-to-one relationship with the leader pods of the source Redis instance (refer to the diagram: Data Synchronization  **instance redis-a** >> **instance b**). Therefore, we need to deploy 3 independent Redis-shake instances here.
Taking __redis-a-leader-0__ as an example, create Redis-shake-sync-0:

#### Create Configuration

In __Container Management__ - __Target Redis Cluster__ - __Configuration and Storage__ - __Configuration Options__ , create a configuration option named __redis-sync-0__ for the Redis-shake instance. Import the file __sync.toml__ (file content provided in the appendix), and make sure to modify the following content:

- source.address: The service address of the source __redis-a-leader-0__ 's __redis-a-leader-svc-0__ :

    ```toml
    address = "10.233.109.145:31278"
    ```

- Access password for the source instance: You can obtain the access password for the source instance through one of the following methods:
- If the source instance is a DCE 5.0 cluster, you can find the password in the deployment details page of the Redis service.
- If the source instance is a third-party cluster, you need to obtain the password from the corresponding configuration or contact the administrator.

Modify the following content accordingly:

```toml
auth = "your_source_instance_password"
```

Save the configuration.

#### Create Redis-shake-sync-0

In __Container Management__ - __Target Redis Cluster__ - __Stateful Workloads__ , create a stateful workload named __redis-a-leader-sync__ with a single ReplicaSet version and set the replica number to 1.

In the config section, select the previously created configuration option __redis-sync-0__ , and modify the following content:

```yaml
clusterName: redis-a-leader-sync
# Modify the image name to match the Redis-shake Docker image used in your environment
image: harbor.mycluster.com/edgegallery/redis-shake:v1.0.0
```

Make sure that the workload selector includes the following labels:

```yaml
app.kubernetes.io/component: redis-shake
app.kubernetes.io/managed-by: redis-operator
app.kubernetes.io/name: redis-a-leader-sync
app.kubernetes.io/part-of: redis-failover
role: sync
statefulset.kubernetes.io/pod-name: redis-a-leader-sync-0
```

Click __Deploy__ .

Repeat the above steps to create Redis-shake-sync-1 and Redis-shake-sync-2 for __redis-a-leader-1__ and __redis-a-leader-2__ respectively.

### Verify Data Synchronization

After completing the above steps, Redis-shake will start synchronizing data from the source Redis instance to the target Redis instance. You can verify the synchronization status by checking the logs of each Redis-shake instance:

In __Container Management__ - __Target Redis Cluster__ - __Stateful Workloads__ , select the Redis-shake workloads ( __redis-a-leader-sync-0__ , __redis-a-leader-sync-1__ , and __redis-a-leader-sync-2__ ) one by one, go to __Pods__ , click the pod name, and then click the __Logs__ tab.

Check the logs to ensure that the data synchronization is successful and there are no errors.

## Data Recovery Deployment

Diagram: Data Recovery **instance redis-b** >> **instance redis-a**

### Configuring Services for the Source Instance (Redis-b)

Create NodePort services for the leader pods of Redis-b, similar to the steps mentioned in the Data Synchronization Deployment section. Create services for the 3 leader pods of Redis-b and make sure to follow the naming convention mentioned earlier.

### Deploying Redis-shake for Data Recovery

Redis-shake needs to be deployed on the same cluster as the source Redis instance to perform data recovery. Therefore, in order to achieve data recovery in this example, we need to deploy Redis-shake on the source side and configure it accordingly.

Similar to the data synchronization configuration, we need to create Redis-shake instances corresponding to the leader pods of the target Redis instance.
Taking __redis-b-leader-0__ as an example, create Redis-shake-recovery-0:

#### Create ConfigMap

In __Container Management__ - __Source Redis Cluster__ - __ConfigMap and Storage__ - __ConfigMap__ , create a configuration option named __redis-recovery-0__ for the Redis-shake instance. Import the file __recovery.toml__ (file content provided in the appendix), and make sure to modify the following content:

- target.address: The service address of __redis-b-leader-0__ 's __redis-b-leader-svc-0__ :

    ```toml
    address = "10.233.109.146:31278"
    ```

- Access password for the source instance: You can obtain this information from the overview page of the Redis service in the Data Service module:

    ```toml
    password = "3wPxzWffdn" # keep empty if no authentication is required
    ```

- Target instance access address: Here, you need to fill in the clusterIP service of the target instance redis-b, which points to port 6379. Use the address of redis-b-leader:

    ```toml
    address = "10.233.43.13:6379"
    ```

    You can find this configuration in __Container Management__ - __Target Redis Cluster__ - __Workloads__ - __Access Method__ . Refer to the following screenshot:


    Click the service name, go to the service details page, and you will see the ClusterIP address:


- Access password for the target instance: You can obtain this information from the Redis instance overview page in the Data Service module:

    ```toml
    password = "3wPxzWffdn" # keep empty if no authentication is required
    ```

- Set the target type to __cluster__ :

    ```toml
    [target]
    type = "cluster" # "standalone" or "cluster"
    ```

#### Create Redis-shake

1. In the __Workbench__ , select __Wizard__ - __Based on Container Image__ to create an application named __redis-shake-sync-0__ :

2. Fill in the application configuration as described below:
    
    - The cluster and namespace of the application should match the Redis instance.
    - Image address:

        ```yaml
        release.daocloud.io/ndx-product/redis-shake@sha256:46652d7d8893fa4508c3c6725afc1e211fb9cb894c4dc85e94287395a32fc3dc
        ```

    - The access type of the default service should be NodePort, and set the container port and service port to 6379.

    - In __Advanced Settings__ - __Lifecycle__ - __Start Command__ - __Run Parameters__ , enter:

        ```yaml
        /etc/sync/sync.toml
        ```

    - In __Advanced Settings__ - __Data Storage__ : Add configuration item __redis-sync-0__ , and set the path to:

        ```yaml
        /etc/sync
        ```

    - In __Advanced Settings__ - __Data Storage__ : Add a temporary path, and the container path should be:

        ```yaml
        /data
        ```

3. Click __OK__ to complete the creation of Redis-shake.

Repeat the above steps to create __redis-shake-sync-1__ and __redis-shake-sync-2__ for the other two Leader Pods.

Once the Redis-shake instances are created, data synchronization will start between the Redis instances. You can use the __redis-cli__ tool to verify the synchronization, but that will not be covered here.

## Data Recovery

Diagram: Data Recovery **instance redis-b** >> **instance redis-a** 


When the source instance **instance redis-a** comes back online, you need to recover incremental data from the target instance **instance redis-b**. To achieve this, you need to deploy three Redis-shake instances in the cluster where **instance redis-a** resides. These instances will perform data replication from **instance redis-b** to **instance redis-a**. The configuration and deployment process is similar to the data synchronization. Configure and deploy the Redis-shake instances in the opposite direction for data recovery, and the recovery process will start automatically.

!!! note

    Before bringing the source instance back online, make sure to stop the running Redis-shake instances __Redis-shake-sync-0__ , __Redis-shake-sync-1__ , and __Redis-shake-sync-2__ in the cluster where **instance redis-b** resides, to avoid mistakenly synchronizing data that could overwrite the newly added data.

## Restoring Master-Slave Relationship

If you want to restore the initial master-slave synchronization relationship of **instance redis-a** >> **instance redis-b**, you need to stop the 3 Redis-shake-recovery instances used for data recovery in the target cluster through __Container Management__ , and then restart the 3 Redis-shake-sync instances in the target cluster. This will rebuild the initial master-slave relationship.

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
type = "cluster" # "standalone" or "cluster"
version = 6.0 # redis version, such as 2.8, 4.0, 5.0, 6.0, 6.2, 7.0, ...
# When the target is a cluster, write the address of one of the nodes.
# redis-shake will obtain other nodes through the __cluster nodes__ command.
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
