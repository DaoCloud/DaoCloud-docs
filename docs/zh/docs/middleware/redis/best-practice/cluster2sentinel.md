# 集群模式 to 哨兵模式

RedisShake 支持不同部署模式实例间的数据同步与迁移能力，现以 3 主 3 从集群模式实例与 3 副本哨兵模式实例的场景为例，演示不同模式之间的同步配置方法。

假设 Redis __实例 redis-a__  为 3 主 3 从集群模式， __实例 redis-b__  为 3 副本哨兵模式，两实例处于不同集群。现将 __实例 redis-a__  作为主实例， __实例 redis-b__  作为从实例搭建同步结构，提供以下灾备支持：

- 正常状态下，由 __实例 redis-a__  对外提供服务，并持续同步数据 __实例 redis-a__  -> __实例 redis-b__  ；
- 当主 __实例 redis-a__  故障离线后，由 __实例 redis-b__  对外提供服务；
- 待 __实例 redis-a__  恢复上线后， __实例 redis-b__  -> __实例 redis-a__  回写增量数据；
- __实例 redis-a__  数据恢复完成后，切换为初始状态，即由 __实例 redis-a__  提供服务，并向 __实例 redis-b__  持续数据同步。

!!! note

    数据传输的方式与传输源端实例有关，在 __数据同步__ 中源端 __实例 redis-a__  为集群模式，需要为 3 个 leader 副本分别部署一个 RedisShake（Redis-shake-sync）；在 __数据恢复__ 中源端 __实例 redis-b__  为哨兵模式，则仅需部署一个 RedisShake（Redis-shake-recovery）。

## 数据同步部署

图例：数据同步 __实例 redis-a__  -> __实例 redis-b__ 

![sync](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/middleware/redis/images/sync17.jpg)

### 为 __实例 redis-a__  配置服务

为 Redis 实例的每一个 Leader Pod 创建一个 __Nodeport__  服务，用于 RedisShake 的数据同步访问。本例中需要为 __实例 redis-a__  的 3 个 Leader Pod 分别创建服务，下面以 Pod __redis-a-leader-0__  为例，为其创建服务：

1. 进入 __容器管理__  -> __源端实例所在集群__  -> __有状态工作负载__ ：选择工作负载 __redis-a-leader__ ，为其创建一个服务，命名为 __redis-a-leader-svc-0__ ，访问类型为 __Nodeport__ ，容器端口和服务端口均为 6379。

    ![svc](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/middleware/redis/images/sync03.png)

2. 查看该服务。并确定工作负载选择器包含以下标签
   
    ```yaml
    app.kubernetes.io/component: redis
    app.kubernetes.io/managed-by: redis-operator
    app.kubernetes.io/name: redis-a
    role: leader
     # 注意 pod-name 一定要选择正确的 leader pod 名称
    statefulset.kubernetes.io/pod-name: redis-a-leader-0
    ```

    ![svc](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/middleware/redis/images/sync04.png)

重复执行以上操作，为 __redis-a-leader-1__  __redis-a-leader-2__  分别创建服务。

### 为 __实例 redis-b__  配置服务

参考 __图例：数据同步 实例 redis-a -> 实例 redis-b__  可见， __实例 redis-b__  与 __RedisShake__  处于同一集群，
因此为 __实例 redis-b__  创建一个 ClusterIP 服务即可,端口指向 6379，如下图所示：

![svc](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/middleware/redis/images/sync23.png)

![svc](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/middleware/redis/images/sync24.png)

### RedisShake 部署

RedisShake 通常与数据传输的目标 Redis 实例运行于同一集群及命名空间上，因此，本例中为了实现数据同步，需要在 __实例 redis-b__  所在集群部署 RedisShake，配置方式如下。

注意，在集群模式下，RedisShake 要求与源端 Redis 实例的 Leader Pod 形成一对一关系（请参考图例：数据同步 __实例 redis-a__  -> __实例 redis-b__ ），因此这里需要部署 3 个独立的 RedisShake。以 __redis-a-leader-0__  为例，创建 __Redis-shake-sync-0__ ：

#### 1. 创建配置项

在 __容器管理__  -> __目标端实例所在集群__  -> __配置与存储__  -> __配置项__ 为 RedisShake 实例创建配置项 __redis-sync-0__ 。导入文件 __sync.toml__ （文件内容见附录），并注意需要修改以下内容：

![conf](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/middleware/redis/images/sync05.png)

- source.address：源端 __实例 redis-a__  的 __redis-a-leader-svc-0__  服务地址：

    ```toml
    address = "10.233.109.145:32283"
    ```
    
- 源端实例的访问密码：可在 __数据服务__ 实例的概览页获取该信息：

    ```toml
    password = "3wPxzWffdn" # keep empty if no authentication is required
    ```

    ![svc](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/middleware/redis/images/sync06.png)

- 目标端实例访问地址，采用上一步为 __实例 redis-b__  创建的 ClusterIP 服务（端口 6379）作为目标端的访问地址：

    ```toml
    # 注意：由于 headless 服务可直接连接工作负载，因此可以通过该服务访问工作负载默认端口 6379。
    address = "10.233.16.241:6379"
    ```

- 目标端实例的访问密码，可在 __数据服务__ 模块下的 Redis 实例概览页获取该信息:

    ```toml
    password = "3wPxzasd" # keep empty if no authentication is required
    ```

- 目标端类型需设置为 __standalone__ ：

    ```toml
    [target]
    type = "standalone" # "standalone" or "cluster"
    ```

#### 2. 创建 RedisShake

1. 打开 __应用工作台__ ，选择 __向导__  -> __基于容器镜像__ ，创建一个应用 __Redis-shake-sync-0__ ：

    ![sync](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/middleware/redis/images/sync07.png)

2. 参考如下说明填写应用配置。
    
    - 应用所属集群、命名空间需与 Redis 实例一致；
    - 镜像地址：

        ```yaml
        release.daocloud.io/ndx-product/redis-shake@sha256:46652d7d8893fa4508c3c6725afc1e211fb9cb894c4dc85e94287395a32fc3dc
        ```

    - 默认服务的访问类型为 Nodeport ，容器端口和服务端口设置为 6379。

        ![sync](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/middleware/redis/images/sync08.png)

    - __高级设置__  -> __生命周期__  -> __启动命令__  -> __运行参数__  填入：

        ```yaml
        /etc/sync/sync.toml
        ```

        ![sync](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/middleware/redis/images/sync09.png)

    - __高级设置__  -> __数据存储__ ：添加配置项 __redis-sync-0__ ，路径必须设置为：

        ```yaml
        /etc/sync
        ```

    - __高级设置__  -> __数据存储__ ：添加一个临时路径，读写权限为 __读写__ ，容器路径必须为：

        ```yaml
        /data
        ```

       ![sync](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/middleware/redis/images/sync10.png)

3. 点击 __确定__ ，完成 RedisShake 创建。

重复执行以上操作，分别为其他两个 Leader Pod 创建 __Redis-shake-sync-1__ ， __Redis-shake-sync-2__ 。

完成 RedisShake 的创建后，实际就已经开始 Redis 实例间的同步，此时可通过 __redis-cli__  工具验证同步，这里就不做赘述。

## 数据恢复

图例：数据恢复 __实例 redis-b__  -> __实例 redis-a__ 

![recovery](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/middleware/redis/images/sync18.jpg)

当源端实例 __实例 redis-a__  发生故障离线后，将由目标端 __实例 redis-b__  提供服务，该过程必然产生新增数据。 __实例 redis-a__  恢复上线后，首先需要从 __实例 redis-b__  恢复增量数据，此时 __实例 redis-a__  与 __实例 redis-b__  角色互换， __实例 redis-b__  作为数据源向 __实例 redis-a__  同步数据。

参考 __图例：数据恢复实例 redis-b -> 实例 redis-a__ ，因 __实例 redis-a__  为集群模式，需要在其所在集群部署 1 个 RedisShake 实例，实现 __实例 redis-b__  -> __实例 redis-a__  的数据回传，配置方式如下。

!!! note

    __实例 redis-a__  上线前，请先关闭用于实例 __redis-a__  -> __实例 redis-b__  数据同步的 3 个 RedisShake 实例( __redis-shake-sync-0__ 、 __redis-shake-sync-1__ 、 __redis-shake-sync-2__ )，避免发生错误的数据同步覆盖掉新增数据。

### 为 __实例 redis-b__  配置服务

恢复流程中 __实例 redis-b__  为数据源，因此需要为该实例创建一个 Nodeport 服务，用于 RedisShake 的跨集群访问。

此时的数据源 __实例 redis-b__  为哨兵模式，因此仅需要创建 1 个服务，以下为创建过程 ：

1. 进入 __容器管理__  -> __源端实例所在集群__  -> __有状态工作负载__ ：选择工作负载 __redis-b__ ，创建一个 __Nodeport__  服务 __redis-b-recovery-svc__ ，容器端口和服务端口均为 6379

    ![svc](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/middleware/redis/images/sync25.png)

2. 查看该服务。并确定工作负载选择器包含以下标签
   
    ```yaml
    app.kubernetes.io/component: redis
    app.kubernetes.io/managed-by: redis-operator
    app.kubernetes.io/name: redis-b
    app.kubernetes.io/part-of: redis-failover
    redis-failover: master
    redisfailovers.databases.spotahome.com/name: redis-b
    ```

    ![svc](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/middleware/redis/images/sync14.png)

### RedisShake 部署

RedisShake 通常与数据传输的目标 Redis 实例运行于同一集群上，因此，本例中为了实现数据同步，需要在目标端部署 RedisShake，配置方式如下。

#### 1. 创建配置项

在 __容器管理__  -> __目标端实例所在集群__  -> __配置与存储__  -> __配置项__ 为 RedisShake 实例创建配置项 __redis-sync__ 。导入文件 __sync.toml__  （文件内容见 __附录__ ），并注意需要修改以下内容：

![conf](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/middleware/redis/images/sync15.png)

- source.address：此时的源端为 __实例 redis-b__ ，填写上一步骤为该实例创建的服务地址：

    ```toml
    address = "10.233.109.145:32283"
    ```
    
- 源端实例的访问密码：可在 __实例 redis-b__  的概览页获取该信息：

    ```toml
    password = "3wPxzWffdn" # keep empty if no authentication is required
    ```
    ![conf](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/middleware/redis/images/sync16.png)

- 目标端实例访问地址，此时的目标端为 __实例 redis-a__ ，这里可以采用系统默认创建的服务 __redis-a-leader__ （端口：6379），无需创建：

    ```toml
    address = "172.30.120.202:6379"
    ```

    该配置可在 __集群管理__  -> __redis-a 所在集群__  -> __工作负载__  -> __访问方式__ 中查看。如下图所示：

    ![conf](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/middleware/redis/images/sync18.png)

    点击服务名称，进入服务详情，可见 ClusterIP 地址：

    ![conf](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/middleware/redis/images/sync19.png)

- 目标端实例的访问密码，可在 __实例 redis-a__  的概览页获取该信息:

    ```toml
    password = "3wPxzWffss" # keep empty if no authentication is required
    ```

- 此时数据接收端为 __实例 redis-b__ ，因此目标端类型需设置为 __cluster__ ：

    ```toml
    [target]
    type = "cluster" # "standalone" or "cluster"
    ```

#### 2. 创建 RedisShake

1. 打开 __应用工作台__ ，选择 __向导__  -> __基于容器镜像__ ，创建一个应用 __Redis-shake-recovery__ ：

    ![sync](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/middleware/redis/images/sync07.png)

2. 参考如下说明填写应用配置。
    
    - 应用所属集群、命名空间需与 Redis 实例一致；
    - 镜像地址：

        ```toml
        release.daocloud.io/ndx-product/redis-shake@sha256:46652d7d8893fa4508c3c6725afc1e211fb9cb894c4dc85e94287395a32fc3dc
        ```

    - 默认服务的访问类型为 Nodeport，容器端口和服务端口设置为 6379。

        ![sync](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/middleware/redis/images/sync08.png)

    - __高级设置__  -> __生命周期__  -> __启动命令__  -> __运行参数__ 填入：

        ```toml
        /etc/sync/sync.toml
        ```

        ![sync](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/middleware/redis/images/sync09.png)

    - __高级设置__  -> __数据存储__ ：添加配置项 __redis-sync__ ，路径必须设置为：

        ```toml
        /etc/sync
        ```

    - __高级设置__  -> __数据存储__ ：添加一个临时路径，容器路径必须为：

        ```toml
        /data
        ```

       ![sync](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/middleware/redis/images/sync20.png)

3. 点击 __确定__ ，完成 RedisShake 创建。

完成 RedisShake 的创建后，实际就已经开始 Redis 实例间的同步，此时可通过 __redis-cli__  工具验证同步，这里就不做赘述。

## 复原主从关系

如需复原初始的主从同步关系 __实例 redis-a__  -> __实例 redis-b__ ，需在 __容器管理__ 中停止当前运行在 __实例 redis-a__  所在集群的 __redis-shake-recovery__  实例，重新启动目标端实例所在集群中的 3 个 __redis-shake-sync__  实例，即可重建初始主从关系。

![sync](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/middleware/redis/images/sync11.png)

## 附录

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
# RedisShake will obtain other nodes through the __cluster nodes__  command.
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
