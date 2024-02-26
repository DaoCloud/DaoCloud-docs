# 哨兵模式 to 哨兵模式

[RedisShake](https://tair-opensource.github.io/RedisShake/) 支持哨兵模式实例间的数据同步与迁移能力，现以 3 副本哨兵模式 Redis 为例，演示跨集群同步配置方法。

假设 __实例 redis-a__  与 __实例 redis-b__  处于不同集群，二者均为 3 副本哨兵模式，现将 __实例 redis-a__  作为主实例， __实例 redis-b__  作为从实例搭建同步结构，提供以下灾备支持：

- 正常状态下，由 __实例 redis-a__  对外提供服务，并持续同步数据 __实例 redis-a__  -> __实例 redis-b__ ；
- 当主 __实例 redis-a__  故障离线后，由 __实例 redis-b__  对外提供服务；
- 待 __实例 redis-a__  恢复上线后， __实例 redis-b__  -> __实例 redis-a__  回写增量数据；
- __实例 redis-a__  数据恢复完成后，切换为初始状态，即由 __实例 redis-a__  提供服务，并向 __实例 redis-b__  持续数据同步。

!!! note

    数据同步与数据恢复需要通过不同的 RedisShake 组完成，因此在本例中需要分别创建 __Redis-shake-sync__ 、 __Redis-shake-recovery__  两个 RedisShake 实例。

## 数据同步部署

图例：数据同步 __实例 redis-a__  -> __实例 redis-b__  

![sync](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/middleware/redis/images/sync12.png)

### 为源端实例配置服务

如果源端实例处于 DCE 5.0 的集群中，可在 __数据服务__  -> __Redis__  -> __解决方案__  -> __跨集群主从同步__ 中开启方案，将自动完成服务配置工作。

![svc](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/middleware/redis/images/sync17.png)

如果源端实例处于第三方集群上，则需要手工完成服务配置，配置方法如下文：

为 Redis 实例创建一个 __Nodeport__  服务，用于 RedisShake 的数据同步访问。本例中需要为 __实例 redis-a__  创建 1 个服务，以下为创建过程 ：

1. 进入 __容器管理__  -> __源端实例所在集群__  -> __有状态工作负载__ ：选择工作负载 __redis-a__ ，创建一个 __Nodeport__  服务，容器端口和服务端口均为 6379

    ![svc](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/middleware/redis/images/sync03.png)

2. 查看该服务。并确定工作负载选择器包含以下标签
   
    ```yaml
    app.kubernetes.io/component: redis
    app.kubernetes.io/managed-by: redis-operator
    app.kubernetes.io/name: redis-a
    app.kubernetes.io/part-of: redis-failover
    redis-failover: master
    redisfailovers.databases.spotahome.com/name: redis-a
    ```

    ![svc](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/middleware/redis/images/sync14.png)

### RedisShake 部署

RedisShake 通常与数据传输的目标 Redis 实例运行于同一集群上，因此，本例中为了实现数据同步，需要在 __实例 redis-b__  所在集群部署 RedisShake，配置方式如下。

#### 创建配置项

在 __容器管理__  -> __目标端实例所在集群__  -> __配置与存储__  -> __配置项__ 为 RedisShake 实例创建配置项 __redis-sync__ 。导入文件 __sync.toml__  （文件内容见 __附录__ ），并注意需要修改以下内容：

![conf](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/middleware/redis/images/sync15.jpg)

- source.address：上一步骤创建的源端 __redis-a__  的服务地址：

    ```toml
    address = "10.233.109.145:31278"
    ```
    
- 源端实例的访问密码：可在 Redis 实例的概览页获取该信息：

    ```toml
    password = "3wPxzWffdn" # keep empty if no authentication is required
    ```
    ![conf](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/middleware/redis/images/sync16.png)

- 目标端实例访问地址，该地址可以采用新建的 __ClusterIP__  服务地址，也可以采用实例 __redis-b__  的默认 __Headless__  服务 __rfr-redis-b__  的地址，本例中采用 __Headless__  服务地址：

    ```toml
    address = "rfr-redis-b:6379"
    ```
 
    该服务信息可在 __集群管理__  -> __目标端所在集群__  -> __工作负载__  -> __访问方式__ 中查看。类似下图所示页面

    ![conf](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/middleware/redis/images/sync22.png)

- 目标端实例的访问密码，可在 __数据服务__ 模块下的 Redis 实例概览页获取该信息:

    ```toml
    password = "3wPxzWffdn" # keep empty if no authentication is required
    ```

    类似下图位置：

    ![svc](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/middleware/redis/images/sync06.png)

- 目标端类型需设置为 __standalone__ ：

    ```toml
    [target]
    type = "standalone" # "standalone" or "cluster"
    ```

#### 创建 RedisShake

1. 打开 __应用工作台__ ，选择 __向导__  -> __基于容器镜像__ ，创建一个应用 __Redis-shake-sync__ ：

    ![sync](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/middleware/redis/images/sync07.png)

2. 参考如下说明填写应用配置。
    
    - 应用所属集群、命名空间需与 Redis 实例一致；
    - 镜像地址：

        ```yaml
        release.daocloud.io/ndx-product/redis-shake@sha256:46652d7d8893fa4508c3c6725afc1e211fb9cb894c4dc85e94287395a32fc3dc
        ```

    - 默认服务的访问类型为 Nodeport，容器端口和服务端口设置为 6379。

        ![sync](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/middleware/redis/images/sync08.png)

    - __高级设置__  -> __生命周期__  -> __启动命令__  -> __运行参数__ 填入：

        ```yaml
        /etc/sync/sync.toml
        ```

        ![sync](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/middleware/redis/images/sync09.png)

    - __高级设置__  -> __数据存储__ ：添加配置项 __redis-sync__ ，路径必须设置为：

        ```yaml
        /etc/sync
        ```

    - __高级设置__  -> __数据存储__ ：添加一个临时路径，容器路径必须为：

        ```yaml
        /data
        ```

       ![sync](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/middleware/redis/images/sync20.png)

3. 点击 __确定__ ，完成 RedisShake 创建。

完成 RedisShake 的创建后，实际就已经开始 Redis 实例间的同步，此时可通过 __redis-cli__  工具验证同步，这里就不做赘述。

## 数据恢复

图例：数据恢复 __实例 redis-b__  -> __实例 redis-a__ 

![recovery](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/middleware/redis/images/sync13.png)

当源端 __实例 redis-a__  恢复上线后，首先需要从目标端 __实例 redis-b__  恢复增量数据，因此需要在 __实例 redis-a__  再次部署 1 个 RedisShake 实例，实现 __实例 redis-b__  -> __实例 redis-a__  的数据回传，此处配置方法与数据同步过程类似，执行 **反方向** 配置部署即可，完成 RedisShake 创建后，即自动开始数据恢复。

!!! note

    源端实例上线前，请先关闭用于正常同步的 __Redis-shake-sync__ ，避免发生错误的数据同步覆盖掉新增数据。

## 复原主从关系

如需复原初始的主从同步关系 __实例 redis-a__  -> __实例 redis-b__ ，需在 __容器管理__ 中停止 __实例 redis-a__  所在集群中正在运行的 __Redis-shake-recovery__  实例，重新启动目标端集群中的 __Redis-shake-sync__  实例，即可重建初始主从关系。

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
type = "standalone" # "standalone" or "cluster"
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
