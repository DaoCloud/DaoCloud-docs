# MySQL 主备关系

MySQL 的主备关系故障相对比较复杂，基于不同现象，会有不同的解决方案。

1. 执行以下命令确认 MySQL 状态:

    ```bash
    kubectl get mysql -A
    ```

    输出类似于：

    ```
    NAMESPACE       NAME                          READY   REPLICAS   AGE
    ghippo-system   test                          True    1          3d
    mcamel-system   mcamel-common-mysql-cluster   False   2          62d
    ```

2. 关注 `Ready` 字段值为 `False` 的库 (这里为 `True` 的判断是延迟小于 30s 同步)，查看 MySQL 从库的日志

    ```bash
    kubectl get pod -n mcamel-system -Lhealthy,role | grep cluster-mysql | grep replica | awk '{print $1}' | xargs -I {} kubectl logs {} -n mcamel-system -c mysql | grep ERROR
    ```

当实例状态为 `False` 时，可能存在以下几类故障，可以结合库日志信息排查修复。

## 实例状态为 `false` 但日志无报错信息

如果从库的日志中没有任何错误 `ERROR` 信息，说明 `False` 只是因为主从同步的延迟过大，可对从库执行以下命令进一步排查：

1. 寻找到从节点的 Pod

    ```bash
    kubectl get pod -n mcamel-system -Lhealthy,role | grep cluster-mysql | grep replica | awk '{print $1}'
    ```

    输出类似于：

    ```
    mcamel-common-mysql-cluster-mysql-1
    ```

2. 设置 `binlog` 参数

    ```bash
    kubectl exec mcamel-common-mysql-cluster-mysql-1 -n mcamel-system -c mysql -- mysql --defaults-file=/etc/mysql/client.conf -NB -e 'set global sync_binlog=10086;'
    ```

3. 进入 MySQL 的容器

    ```bash
    kubectl exec -it mcamel-common-mysql-cluster-mysql-1 -n mcamel-system -c mysql -- mysql --defaults-file=/etc/mysql/client.conf
    ```

4. 在 MySQL 容器中执行查看命令，获取从库状态。

    `Seconds_Behind_Master` 字段为主从延迟，如果取值在 0~30，可以认为没有延迟；表示主从可以保持同步。

    ??? note "SQL 语句如下"

        ```sql
        mysql> show slave status\G; 
        *************************** 1. row ***************************
                      Slave_IO_State: Waiting for source to send event
                          Master_Host: mcamel-common-mysql-cluster-mysql-0.mysql.mcamel-system
                          Master_User: sys_replication
                          Master_Port: 3306
                        Connect_Retry: 1
                      Master_Log_File: mysql-bin.000304
                  Read_Master_Log_Pos: 83592007
                      Relay_Log_File: mcamel-common-mysql-cluster-mysql-1-relay-bin.000002
                        Relay_Log_Pos: 83564355
                Relay_Master_Log_File: mysql-bin.000304
                    Slave_IO_Running: Yes
                    Slave_SQL_Running: Yes
                      Replicate_Do_DB:
                  Replicate_Ignore_DB:
                  Replicate_Do_Table:
              Replicate_Ignore_Table:
              Replicate_Wild_Do_Table:
          Replicate_Wild_Ignore_Table:
                          Last_Errno: 0
                          Last_Error:
                        Skip_Counter: 0
                  Exec_Master_Log_Pos: 83564299
                      Relay_Log_Space: 83592303
                      Until_Condition: None
                      Until_Log_File:
                        Until_Log_Pos: 0
                  Master_SSL_Allowed: No
                  Master_SSL_CA_File:
                  Master_SSL_CA_Path:
                      Master_SSL_Cert:
                    Master_SSL_Cipher:
                      Master_SSL_Key:
                Seconds_Behind_Master: 0
        Master_SSL_Verify_Server_Cert: No
                        Last_IO_Errno: 0
                        Last_IO_Error:
                      Last_SQL_Errno: 0
                      Last_SQL_Error:
          Replicate_Ignore_Server_Ids:
                    Master_Server_Id: 100
                          Master_UUID: e17dae09-8da0-11ed-9104-c2f9484728fd
                    Master_Info_File: mysql.slave_master_info
                            SQL_Delay: 0
                  SQL_Remaining_Delay: NULL
              Slave_SQL_Running_State: Replica has read all relay log; waiting for more updates
                  Master_Retry_Count: 86400
                          Master_Bind:
              Last_IO_Error_Timestamp:
            Last_SQL_Error_Timestamp:
                      Master_SSL_Crl:
                  Master_SSL_Crlpath:
                  Retrieved_Gtid_Set: e17dae09-8da0-11ed-9104-c2f9484728fd:21614244-21621569
                    Executed_Gtid_Set: 4bc2107c-819a-11ed-bf23-22be07e4eaff:1-342297,
        7cc717ea-7c1b-11ed-b59d-c2ba3f807d12:1-619197,
        a5ab763a-7c1b-11ed-b5ca-522707642ace:1-178069,
        a6045297-8743-11ed-8712-8e52c3ace534:1-4073131,
        a95cf9df-84d7-11ed-8362-5e8a1c335253:1-493942,
        b5175b1b-a2ac-11ed-b0c6-d6fbe05d7579:1-3754703,
        c4dc2b14-9ed9-11ed-ac61-36da81109699:1-945884,
        e17dae09-8da0-11ed-9104-c2f9484728fd:1-21621569
                        Auto_Position: 1
                Replicate_Rewrite_DB:
                        Channel_Name:
                  Master_TLS_Version:
              Master_public_key_path:
                Get_master_public_key: 0
                    Network_Namespace:
        1 row in set, 1 warning (0.00 sec)
        ```

5. 主从同步后 `Seconds_Behind_Master` 小于 30s，设置 `sync_binlog=1`

    ```bash
    kubectl exec mcamel-common-mysql-cluster-mysql-1 -n mcamel-system -c mysql -- mysql --defaults-file=/etc/mysql/client.conf -NB -e 'set global sync_binlog=1';
    ```

6. 如果此时依然不见缓解，可以查看从库的宿主机负载或者 IO 是否太高，执行以下命令：

    ```bash
    [root@master-01 ~]$ uptime
    11:18  up 1 day, 17:49, 2 users, load averages: 9.33 7.08 6.28
    ```

    `load averages` 在正常情况下 3 个数值都不应长期超过 10；如果超过 30 以上，请合理调配下该节点的 Pod 和磁盘。

## 从库日志出现`复制错误`

如果从库 Pod 日志中出现从库复制错误，可能由多种原因引起，下文将针对不同情况介绍判断及修复方法。

### purged binlog 错误

注意以下示例，如果出现关键字 `purged binlog`，通常需要对从库执行重建处理。

??? note "错误示例"

    ```bash
    [root@demo-alpha-master-01 /]$ kubectl get pod -n mcamel-system -Lhealthy,role | grep cluster-mysql | grep replica | awk '{print $1}' | xargs -I {} kubectl logs {} -n mcamel-system -c mysql | grep ERROR
    2023-02-08T18:43:21.991730Z 116 [ERROR] [MY-010557] [Repl] Error reading packet from server for channel '': Cannot replicate because the master purged required binary logs. Replicate the missing transactions from elsewhere, or provision a new slave from backup. Consider increasing the master's binary log expiration period. The GTID sets and the missing purged transactions are too long to print in this message. For more information, please see the master's error log or the manual for GTID_SUBTRACT (server_errno=1236)
    2023-02-08T18:43:21.991777Z 116 [ERROR] [MY-013114] [Repl] Slave I/O for channel '': Got fatal error 1236 from master when reading data from binary log: 'Cannot replicate because the master purged required binary logs. Replicate the missing transactions from elsewhere, or provision a new slave from backup. Consider increasing the master's binary log expiration period. The GTID sets and the missing purged transactions are too long to print in this message. For more information, please see the master's error log or the manual for GTID_SUBTRACT', Error_code: MY-013114
    ```

重建操作如下：

1. 寻找从节点的 Pod

    ```bash
    [root@master-01 ~]$ kubectl get pod -n mcamel-system -Lhealthy,role | grep cluster-mysql | grep replica | awk '{print $1}'
    mcamel-common-mysql-cluster-mysql-1
    ```

2. 寻找从节点的  PVC

    ```bash
    [root@master-01 /]$ kubectl get pvc -n mcamel-system | grep mcamel-common-mysql-cluster-mysql-1
    data-mcamel-common-mysql-cluster-mysql-1                                        Bound    pvc-5840569e-834f-4236-a5c6-878e41c55c85   50Gi       RWO            local-path                   33d
    ```

3. 删除从节点的 PVC

    ```bash
    [root@master-01 /]$ kubectl delete pvc data-mcamel-common-mysql-cluster-mysql-1 -n mcamel-system
    persistentvolumeclaim "data-mcamel-common-mysql-cluster-mysql-1" deleted
    ```

4. 删除从库的 Pod

    ```bash
    [root@master-01 /]$ kubectl delete pod mcamel-common-mysql-cluster-mysql-1 -n mcamel-system
    pod "mcamel-common-mysql-cluster-mysql-1" deleted
    ```

### 主键冲突错误

??? note "错误实例"

    ```bash
    [root@demo-alpha-master-01 /]$ kubectl get pod -n mcamel-system -Lhealthy,role | grep cluster-mysql | grep replica | awk '{print $1}' | xargs -I {} kubectl logs {} -n mcamel-system -c mysql | grep ERROR
    2023-02-08T18:43:21.991730Z 116 [ERROR] [MY-010557] [Repl] Could notexecute Write_rows event on table dr_brower_db.dr_user_info; Duplicate entry '24' for key 'PRIMARY', Error_code:1062; handler error HA_ERR_FOUND_DUPP_KEY; the event's master logmysql-bin.000010, end_log_pos 5295916
    ```

如果在错误日志中看到：`Duplicate entry '24' for key 'PRIMARY', Error_code:1062; handler error HA_ERR_FOUND_DUPP_KEY;`，

说明出现了主键冲突，或者主键不存在的错误。此时，可以以幂等模式恢复或插入空事务的形式跳过错误：

**方法1**：幂等模式恢复

1. 寻找到从节点的 Pod

    ```bash
    [root@master-01 ~]$ kubectl get pod -n mcamel-system -Lhealthy,role | grep cluster-mysql | grep replica | awk '{print $1}'
    mcamel-common-mysql-cluster-mysql-1
    ```

2. 设置 mysql 幂等模式

    ```bash
    [root@master-01 ~]$ kubectl exec mcamel-common-mysql-cluster-mysql-1 -n mcamel-system -c mysql -- mysql --defaults-file=/etc/mysql/client.conf -NB -e 'stop slave;set global slave_exec_mode="IDEMPOTENT";set global sync_binlog=10086;start slave;'
    ```

**方法 2** ：插入空事务跳过错误

```sql
mysql> stop slave;
mysql> SET @@SESSION.GTID_NEXT= 'xxxxx:105220'; /* 具体数值，在日志里面提到 */
mysql> BEGIN;
mysql> COMMIT;
mysql> SET SESSION GTID_NEXT = AUTOMATIC;
mysql> START SLAVE;
```

执行完成以上操作后，观察从库重建的进度：

```bash
# 进入 mysql 的容器
[root@master-01 ~]$ kubectl exec -it mcamel-common-mysql-cluster-mysql-1 -n mcamel-system -c mysql -- mysql --defaults-file=/etc/mysql/client.conf
```

执行以下命令，查看从库的主从延迟状态字段 `Seconds_Behind_Master`，如果取值在 0~30，表示已没有主从延迟，主库和从库基本保持同步。

```sql
mysql> show slave status\G;
```

确认主从同步后 (Seconds_Behind_Master 小于 30s)，执行以下命令，设定 MySQL 严格模式：

```bash
[root@master-01 ~]$ kubectl exec mcamel-common-mysql-cluster-mysql-1 -n mcamel-system -c mysql -- mysql --defaults-file=/etc/mysql/client.conf -NB -e 'stop slave;set global slave_exec_mode="STRICT";set global sync_binlog=10086;start slave;
```

### 主从库复制错误

当从库出现类似 `[Note] Slave: MTS group recovery relay log info based on Worker-Id 0, group_r` 的错误信息，可以执行如下操作：

1. 寻找到从节点的 Pod

    ```shell
    [root@master-01 ~]# kubectl get pod -n mcamel-system -Lhealthy,role | grep cluster-mysql | grep replica | awk '{print $1}' 
    mcamel-common-mysql-cluster-mysql-1
    ```

2. 设置让从库跳过这个日志继续复制

    ```shell
    [root@master-01 ~]# kubectl exec mcamel-common-mysql-cluster-mysql-1 -n mcamel-system -c mysql -- mysql --defaults-file=/etc/mysql/client.conf -NB -e 'stop slave;reset slave;change master to MASTER_AUTO_POSITION = 1;start slave;'; 
    ```

!!! tip

    1. 这种情况可以以幂等模式执行
    2. 此种类型错误也可以重做从库

## 主备 Pod 均为 `replica`

1. 通过以下命令，发现两个 MySQL 的 Pod均为 `replica` 角色，需修正其中一个为 `master`。

    ```bash
    [root@aster-01 ~]$ kubectl get pod -n mcamel-system -Lhealthy,role|grep mysql
    mcamel-common-mysql-cluster-mysql-0                          4/4     Running   5 (16h ago)   16h   no       replica
    mcamel-common-mysql-cluster-mysql-1                          4/4     Running   6 (16h ago)   16h   no       replica
    mysql-operator-0                                             2/2     Running   1 (16h ago)   16h
    ```

2. 进入 MySQL 查看：

    ```bash
    kubectl exec -it mcamel-common-mysql-cluster-mysql-0 -n mcamel-system -c mysql -- mysql --defaults-file=/etc/mysql/client.conf
    ```

3. 查看 `slave` 的状态信息，查询结果为空的就是原来的 `master`，如下方示例中 `mysql-0` 对应的内容:

    ??? note "状态信息示例“

        ```sql
        -- mysql-0
        mysql> show slave status\G;
        empty set, 1 warning (0.00 sec)

        -- mysql-1
        mysql> show slave status\G;
        *************************** 1. row ***************************
                      Slave_IO_State: Waiting for source to send event
                          Master_Host: mcamel-common-mysql-cluster-mysql-0.mysql.mcamel-system
                          Master_User: sys_replication
                          Master_Port: 3306
                        Connect_Retry: 1
                      Master_Log_File: mysql-bin.000004
                  Read_Master_Log_Pos: 38164242
                      Relay_Log_File: mcamel-common-mysql-cluster-mysql-1-relay-bin.000002
                        Relay_Log_Pos: 38164418
                Relay_Master_Log_File: mysql-bin.000004
                    Slave_IO_Running: Yes
                    Slave_SQL_Running: Yes
                      Replicate_Do_DB:
                  Replicate_Ignore_DB:
                  Replicate_Do_Table:
              Replicate_Ignore_Table:
              Replicate_Wild_Do_Table:
          Replicate_Wild_Ignore_Table:
                          Last_Errno: 0
                          Last_Error:
                        Skip_Counter: 0
                  Exec_Master_Log_Pos: 38164242
                      Relay_Log_Space: 38164658
                      Until_Condition: None
                      Until_Log_File:
                        Until_Log_Pos: 0
                  Master_SSL_Allowed: No
                  Master_SSL_CA_File:
                  Master_SSL_CA_Path:
                      Master_SSL_Cert:
                    Master_SSL_Cipher:
                      Master_SSL_Key:
                Seconds_Behind_Master: 0
        Master_SSL_Verify_Server_Cert: No
                        Last_IO_Errno: 0
                        Last_IO_Error:
                      Last_SQL_Errno: 0
                      Last_SQL_Error:
          Replicate_Ignore_Server_Ids:
                    Master_Server_Id: 100
                          Master_UUID: c16da70b-ad12-11ed-8084-0a580a810256
                    Master_Info_File: mysql.slave_master_info
                            SQL_Delay: 0
                  SQL_Remaining_Delay: NULL
              Slave_SQL_Running_State: Replica has read all relay log; waiting for more updates
                  Master_Retry_Count: 86400
                          Master_Bind:
              Last_IO_Error_Timestamp:
            Last_SQL_Error_Timestamp:
                      Master_SSL_Crl:
                  Master_SSL_Crlpath:
                  Retrieved_Gtid_Set: c16da70b-ad12-11ed-8084-0a580a810256:537-59096
                    Executed_Gtid_Set: c16da70b-ad12-11ed-8084-0a580a810256:1-59096
                        Auto_Position: 1
                Replicate_Rewrite_DB:
                        Channel_Name:
                  Master_TLS_Version:
              Master_public_key_path:
                Get_master_public_key: 0
                    Network_Namespace:
        1 row in set, 1 warning (0.01 sec)
        ```

4. 针对 master 的 mysql shell 执行重置操作：

    ```sql
    mysql > stop slave;reset slave;
    ```

5. 此时再手动编辑 master 的 Pod：`role replica => master ,healthy no => yes`。

6. 针对 slave 的 mysql shell 执行：

    ```sql
    mysql > start slave;
    ```

7. 如果主从没有建立联系，在 slave 的 mysql shell 执行：

    ```sql
    -- 注意替换下 {master-host-pod-index}
    mysql > change master to master_host='mcamel-common-mysql-cluster-mysql-{master-host-pod-index}.mysql.mcamel-system',master_port=3306,master_user='root',master_password='{password}',master_auto_position=1,MASTER_HEARTBEAT_PERIOD=2,MASTER_CONNECT_RETRY=1, MASTER_RETRY_COUNT=86400;
    ```

## 主备数据不一致

当主从实例数据不一致时，可以执行以下命令完成主从一致性同步：

```sql
pt-table-sync --execute --charset=utf8 --ignore-databases=mysql,sys,percona --databases=amamba,audit,ghippo,insight,ipavo,keycloak,kpanda,skoala dsn=u=root,p=xxx,h=mcamel-common-kpanda-mysql-cluster-mysql-0.mysql.mcamel-system,P=3306 dsn=u=root,p=xxx,h=mcamel-common-kpanda-mysql-cluster-mysql.mysql.mcamel-system,P=3306  --print

pt-table-sync --execute --charset=utf8 --ignore-databases=mysql,sys,percona --databases=kpanda dsn=u=root,p=xxx,h=mcamel-common-kpanda-mysql-cluster-mysql-0.mysql.mcamel-system,P=3306 dsn=u=root,p=xxx,h=mcamel-common-kpanda-mysql-cluster-mysql-1.mysql.mcamel-system,P=3306  --print
```

使用 pt-table-sync 即可完成数据补充，示例中是 `mysql-0=> mysql-1` 补充数据。

这种场景往往适用于主从切换，发现新从库有多余的已执行的 gtid 在重做之前补充数据。

这种补充数据只能保证数据不丢失，如果新主库已经删除的数据会被重新补充回去，是一个潜在的风险，如果是新主库有数据，会被替换成老数据，也是一个风险。
