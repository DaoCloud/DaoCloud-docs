# MySQL 排障手册

本文将会持续统计和梳理常见的 MySQL 异常故障以及修复方式，若遇到使用问题，请优先查看此排障手册。

> 如果您发现遇到的问题，未包含在本手册，可以快速跳转到页面底部，提交您的问题。

## 故障问题汇总

- [MySQL 排障手册](#mysql-排障手册)
  - [故障问题汇总](#故障问题汇总)
  - [mysql pod 出现 (2/4) running 的情况](#mysql-pod-出现-24-running-的情况)
  - [mysql pod 一直有一个 pod 出现了 (0/4) Init:Error 的状态](#mysql-pod-一直有一个-pod-出现了-04-initerror-的状态)
  - [mysql 不健康](#mysql-不健康)
    - [从库没有错误日志](#从库没有错误日志)
    - [从库出现复制错误](#从库出现复制错误)
      - [出现了 purged binlog 错误](#出现了-purged-binlog-错误)
      - [主键冲突错误](#主键冲突错误)
    - [两个都是 replica (从库)](#两个都是-replica-从库)
  - [Mysql pod 节点是 (3/4) running 状态，describe 出 unhealthy 状态](#mysql-pod-节点是-34-running-状态describe-出-unhealthy-状态)
  - [数据库运行正常，使用 CR 创建数据库出现了报错](#数据库运行正常使用-cr-创建数据库出现了报错)

## mysql pod 出现 (2/4) running 的情况

一般出现此类问题，很可能是因为 MySQL 实例使用的磁盘用量达到了 100%，您可以使用以下命令进行检测磁盘用量。

```bash
[root@master-01 ~]# kubectl get pod -n mcamel-system | grep cluster-mysql | awk '{print $1}' | xargs -I {} kubectl exec {} -n mcamel-system -c sidecar -- df -h | grep /var/lib/mysql
/dev/drbd43001            50G   30G   21G  60% /var/lib/mysql
/dev/drbd43005            80G   29G   52G  36% /var/lib/mysql
```

如果发现某个 pvc 满了进行 pvc 扩容即可。

```bash
[root@master-01 ~]# kubectl edit pvc data-mcamel-common-mysql-cluster-mysql-0 -n mcamel-system # 修改request大小即可
```

## mysql pod 一直有一个 pod 出现了 (0/4) Init:Error 的状态

遇到此类问题时，我们优先查看 master 节点的（sidecar）日志信息

```bash
[root@master-01 ~]# kubectl get pod -n mcamel-system -Lhealthy,role | grep cluster-mysql | grep master | awk '{print $1}' | xargs -I {} kubectl logs -f {} -n mcamel-system -c sidecar
2023-02-09T05:38:56.208445-00:00 0 [Note] [MY-011825] [Xtrabackup] perl binary not found. Skipping the version check
2023-02-09T05:38:56.208521-00:00 0 [Note] [MY-011825] [Xtrabackup] Connecting to MySQL server host: 127.0.0.1, user: sys_replication, password: set, port: not set, socket: not set
2023-02-09T05:38:56.212595-00:00 0 [Note] [MY-011825] [Xtrabackup] Using server version 8.0.29
2023-02-09T05:38:56.217325-00:00 0 [Note] [MY-011825] [Xtrabackup] Executing LOCK INSTANCE FOR BACKUP ...
2023-02-09T05:38:56.219880-00:00 0 [ERROR] [MY-011825] [Xtrabackup] Found tables with row versions due to INSTANT ADD/DROP columns
2023-02-09T05:38:56.219931-00:00 0 [ERROR] [MY-011825] [Xtrabackup] This feature is not stable and will cause backup corruption.
2023-02-09T05:38:56.219940-00:00 0 [ERROR] [MY-011825] [Xtrabackup] Please check https://docs.percona.com/percona-xtrabackup/8.0/em/instant.html for more details.
2023-02-09T05:38:56.219945-00:00 0 [ERROR] [MY-011825] [Xtrabackup] Tables found:
2023-02-09T05:38:56.219951-00:00 0 [ERROR] [MY-011825] [Xtrabackup] keycloak/USER_SESSION
2023-02-09T05:38:56.219956-00:00 0 [ERROR] [MY-011825] [Xtrabackup] keycloak/AUTHENTICATION_EXECUTION
2023-02-09T05:38:56.219960-00:00 0 [ERROR] [MY-011825] [Xtrabackup] keycloak/AUTHENTICATION_FLOW
2023-02-09T05:38:56.219968-00:00 0 [ERROR] [MY-011825] [Xtrabackup] keycloak/AUTHENTICATOR_CONFIG
2023-02-09T05:38:56.219984-00:00 0 [ERROR] [MY-011825] [Xtrabackup] keycloak/CLIENT_SESSION
2023-02-09T05:38:56.219991-00:00 0 [ERROR] [MY-011825] [Xtrabackup] keycloak/IDENTITY_PROVIDER
2023-02-09T05:38:56.219998-00:00 0 [ERROR] [MY-011825] [Xtrabackup] keycloak/PROTOCOL_MAPPER
2023-02-09T05:38:56.220005-00:00 0 [ERROR] [MY-011825] [Xtrabackup] keycloak/RESOURCE_SERVER_SCOPE
2023-02-09T05:38:56.220012-00:00 0 [ERROR] [MY-011825] [Xtrabackup] keycloak/REQUIRED_ACTION_PROVIDER
2023-02-09T05:38:56.220018-00:00 0 [ERROR] [MY-011825] [Xtrabackup] keycloak/COMPONENT
2023-02-09T05:38:56.220027-00:00 0 [ERROR] [MY-011825] [Xtrabackup] keycloak/RESOURCE_SERVER
2023-02-09T05:38:56.220036-00:00 0 [ERROR] [MY-011825] [Xtrabackup] keycloak/CREDENTIAL
2023-02-09T05:38:56.220043-00:00 0 [ERROR] [MY-011825] [Xtrabackup] keycloak/FED_USER_CREDENTIAL
2023-02-09T05:38:56.220049-00:00 0 [ERROR] [MY-011825] [Xtrabackup] keycloak/MIGRATION_MODEL
2023-02-09T05:38:56.220054-00:00 0 [ERROR] [MY-011825] [Xtrabackup] keycloak/REALM
2023-02-09T05:38:56.220062-00:00 0 [ERROR] [MY-011825] [Xtrabackup] keycloak/CLIENT
2023-02-09T05:38:56.220069-00:00 0 [ERROR] [MY-011825] [Xtrabackup] keycloak/REALM_ATTRIBUTE
2023-02-09T05:38:56.220075-00:00 0 [ERROR] [MY-011825] [Xtrabackup] keycloak/OFFLINE_USER_SESSION
2023-02-09T05:38:56.220084-00:00 0 [ERROR] [MY-011825] [Xtrabackup] Please run OPTIMIZE TABLE or ALTER TABLE ALGORITHM=COPY on all listed tables to fix this issue.
E0209 05:38:56.223635       1 deleg.go:144] sidecar "msg"="failed waiting for xtrabackup to finish" "error"="exit status 1"
```

登陆 master 节点的 mysql，执行 alter 表结构：

```bash
[root@master-01 ~]# kubectl get pod -n mcamel-system -Lhealthy,role | grep cluster-mysql | grep master
mcamel-common-mysql-cluster-mysql-0

#获取密码
[root@master-01 ~]# kubectl get secret -n mcamel-system mcamel-common-mysql-cluster-secret -o=jsonpath='{.data.ROOT_PASSWORD}' | base64 -d

[root@master-01 ~]# kubectl exec -it mcamel-common-mysql-cluster-mysql-0 -n mcamel-system -c mysql -- /bin/bash

# 注意：修改表结构需要root权限登陆
~bash:mysql -uroot -p
```

> SQL 语句如下：

```sql
use keycloak;
ALTER TABLE USER_SESSION ALGORITHM=COPY;
ALTER TABLE AUTHENTICATION_EXECUTION ALGORITHM=COPY;
ALTER TABLE AUTHENTICATION_FLOW ALGORITHM=COPY;
ALTER TABLE AUTHENTICATOR_CONFIG ALGORITHM=COPY;
ALTER TABLE CLIENT_SESSION ALGORITHM=COPY;
ALTER TABLE IDENTITY_PROVIDER ALGORITHM=COPY;
ALTER TABLE PROTOCOL_MAPPER ALGORITHM=COPY;
ALTER TABLE RESOURCE_SERVER_SCOPE ALGORITHM=COPY;
ALTER TABLE REQUIRED_ACTION_PROVIDER ALGORITHM=COPY;
ALTER TABLE COMPONENT ALGORITHM=COPY;
ALTER TABLE RESOURCE_SERVER ALGORITHM=COPY;
ALTER TABLE CREDENTIAL ALGORITHM=COPY;
ALTER TABLE FED_USER_CREDENTIAL ALGORITHM=COPY;
ALTER TABLE MIGRATION_MODEL ALGORITHM=COPY;
ALTER TABLE REALM ALGORITHM=COPY;
ALTER TABLE CLIENT ALGORITHM=COPY;
ALTER TABLE REALM_ATTRIBUTE ALGORITHM=COPY;
ALTER TABLE OFFLINE_USER_SESSION ALGORITHM=COPY
```

## mysql 不健康

我们可以通过以下命令快速的查看 当前集群上所有 MySQL 的健康状态

```bash
[root@-master-01 /]# kubectl get mysql -A
NAMESPACE       NAME                          READY   REPLICAS   AGE
ghippo-system   test                          True    1          3d
mcamel-system   mcamel-common-mysql-cluster   False   2          62d
```

如果，发现某个 mysql 的 ready 为 False (这里为 True 的判断是 延迟小于 30s 同步)，然后我们快速查看 从库 MySQL 的日志

```bash
[root@master-01 ~]# kubectl get pod -n mcamel-system -Lhealthy,role | grep cluster-mysql | grep replica | awk '{print $1}' | xargs -I {} kubectl logs {} -n mcamel-system -c mysql | grep ERROR
```

### 从库没有错误日志

如果上面的命令执行后，没有任何错误 `ERROR` 信息，这说明只是因为主从同步的延迟过大，

```bash
# 寻找到从节点的pod
[root@master-01 ~]# kubectl get pod -n mcamel-system -Lhealthy,role | grep cluster-mysql | grep replica | awk '{print $1}'
mcamel-common-mysql-cluster-mysql-1

# 设置binlog参数
[root@master-01 ~]# kubectl exec mcamel-common-mysql-cluster-mysql-1 -n mcamel-system -c mysql -- mysql --defaults-file=/etc/mysql/client.conf -NB -e 'set global sync_binlog=10086;'

# 进入mysql的容器
[root@master-01 ~]# kubectl exec -it mcamel-common-mysql-cluster-mysql-1 -n mcamel-system -c mysql -- mysql --defaults-file=/etc/mysql/client.conf
```

获取从库状态 `Seconds_Behind_Master` 为主从延迟，如果是 0~30，表示没有主从延迟了；表示从库追上了（主库）

```sql
mysql> show slave status\G; #获取从库状态 Seconds_Behind_Master 为主从延迟,如果是 0~30，表示没有主从延迟了。表示从库追上了（主库）
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

等从库追上以后 (Seconds_Behind_Master 小于 30s)，再设置成 `sync_binlog=1`

```bash
[root@master-01 ~]# kubectl exec mcamel-common-mysql-cluster-mysql-1 -n mcamel-system -c mysql -- mysql --defaults-file=/etc/mysql/client.conf -NB -e 'set global sync_binlog=1';
```

如果此时依然不见缓解，可以看看是不是从库的 mysql 的宿主机的负载或者 IO 太高。把它降低。

```bash
[root@master-01 ~]# uptime
11:18  up 1 day, 17:49, 2 users, load averages: 9.33 7.08 6.28
```

关注下 `load averages` ，正常情况下，不应该超过 3 个数值都不应长期超过 10；如果 超过 >30 以上，请合理调配下该节点的 POD 和磁盘

### 从库出现复制错误

如果我们在查看 Pod 日志时，发现了从库复制错误，这可能有多种情况，注意根据出现的错误内容，需要分别进行修复

#### 出现了 purged binlog 错误

```bash
[root@demo-alpha-master-01 /]# kubectl get pod -n mcamel-system -Lhealthy,role | grep cluster-mysql | grep replica | awk '{print $1}' | xargs -I {} kubectl logs {} -n mcamel-system -c mysql | grep ERROR
2023-02-08T18:43:21.991730Z 116 [ERROR] [MY-010557] [Repl] Error reading packet from server for channel '': Cannot replicate because the master purged required binary logs. Replicate the missing transactions from elsewhere, or provision a new slave from backup. Consider increasing the master's binary log expiration period. The GTID sets and the missing purged transactions are too long to print in this message. For more information, please see the master's error log or the manual for GTID_SUBTRACT (server_errno=1236)
2023-02-08T18:43:21.991777Z 116 [ERROR] [MY-013114] [Repl] Slave I/O for channel '': Got fatal error 1236 from master when reading data from binary log: 'Cannot replicate because the master purged required binary logs. Replicate the missing transactions from elsewhere, or provision a new slave from backup. Consider increasing the master's binary log expiration period. The GTID sets and the missing purged transactions are too long to print in this message. For more information, please see the master's error log or the manual for GTID_SUBTRACT', Error_code: MY-013114
```

注意关键字 `purged binlog` ，如果发现了此类错误，基本上，我们需要进行 从库的重建处理

```bash
 #寻找到从节点的pod
[root@master-01 ~]# kubectl get pod -n mcamel-system -Lhealthy,role | grep cluster-mysql | grep replica | awk '{print $1}'
mcamel-common-mysql-cluster-mysql-1

 #寻找从节点的pvc
[root@master-01 /]# kubectl get pvc -n mcamel-system | grep mcamel-common-mysql-cluster-mysql-1
data-mcamel-common-mysql-cluster-mysql-1                                        Bound    pvc-5840569e-834f-4236-a5c6-878e41c55c85   50Gi       RWO            local-path                   33d

# 删除从节点的pvc
[root@master-01 /]# kubectl delete pvc data-mcamel-common-mysql-cluster-mysql-1 -n mcamel-system 
persistentvolumeclaim "data-mcamel-common-mysql-cluster-mysql-1" deleted

# 删除从库的pod
[root@master-01 /]# kubectl delete pod mcamel-common-mysql-cluster-mysql-1 -n mcamel-system 
pod "mcamel-common-mysql-cluster-mysql-1" deleted
```

#### 主键冲突错误

```bash
[root@demo-alpha-master-01 /]# kubectl get pod -n mcamel-system -Lhealthy,role | grep cluster-mysql | grep replica | awk '{print $1}' | xargs -I {} kubectl logs {} -n mcamel-system -c mysql | grep ERROR
2023-02-08T18:43:21.991730Z 116 [ERROR] [MY-010557] [Repl] Could notexecute Write_rows event on table dr_brower_db.dr_user_info; Duplicate entry '24' for key 'PRIMARY', Error_code:1062; handler error HA_ERR_FOUND_DUPP_KEY; the event's master logmysql-bin.000010, end_log_pos 5295916
```

我们通过错误日志看到了类型如下内容：

> `Duplicate entry '24' for key 'PRIMARY', Error_code:1062; handler error HA_ERR_FOUND_DUPP_KEY;`

这说明出现了主键冲突，或者主键不存在的错误；此时，我们可以以幂等模式恢复：

```bash
# 寻找到从节点的pod
[root@master-01 ~]# kubectl get pod -n mcamel-system -Lhealthy,role | grep cluster-mysql | grep replica | awk '{print $1}'
mcamel-common-mysql-cluster-mysql-1

# 设置mysql 幂等模式
[root@master-01 ~]# kubectl exec mcamel-common-mysql-cluster-mysql-1 -n mcamel-system -c mysql -- mysql --defaults-file=/etc/mysql/client.conf -NB -e 'stop slave;set global slave_exec_mode="IDEMPOTENT";set global sync_binlog=10086;start slave;'
```

也可以插入空事务的形式跳过错误：

```sql
mysql> stop slave;
mysql> SET @@SESSION.GTID_NEXT= 'xxxxx:105220'; /* 具体数值，在日志里面提到 */
mysql> BEGIN;
mysql> COMMIT;
mysql> SET SESSION GTID_NEXT = AUTOMATIC;
mysql> START SLAVE;
```

执行完成以上操作后，我们可以观察下从库重建的进度，当主从没有延迟了之后，

```bash
# 进入mysql的容器
[root@master-01 ~]# kubectl exec -it mcamel-common-mysql-cluster-mysql-1 -n mcamel-system -c mysql -- mysql --defaults-file=/etc/mysql/client.conf
```

查看从库的状态 `Seconds_Behind_Master` 为主从延迟，如果是 0~30，表示没有主从延迟了。表示从库追上了（主库）

```sql
mysql> show slave status\G;
```

等从库追上以后 (Seconds_Behind_Master 小于 30s)，执行下方指令，设定 MySQL 严格模式：

```bash
[root@master-01 ~]# kubectl exec mcamel-common-mysql-cluster-mysql-1 -n mcamel-system -c mysql -- mysql --defaults-file=/etc/mysql/client.conf -NB -e 'stop slave;set global slave_exec_mode="STRICT";set global sync_binlog=10086;start slave;
```

### 两个都是 replica (从库)

```bash
[root@aster-01 ~]# kubectl get pod -n mcamel-system -Lhealthy,role|grep mysql
mcamel-common-mysql-cluster-mysql-0                          4/4     Running   5 (16h ago)   16h   no       replica
mcamel-common-mysql-cluster-mysql-1                          4/4     Running   6 (16h ago)   16h   no       replica
mysql-operator-0                                             2/2     Running   1 (16h ago)   16h
```

通过上方的命令，我们发现这 2 个 MySQL 的 Pod，都是 `replica` 角色，此时我们修正其中一个为 `master`：

```bash
[root@master-01 ~]# kubectl exec -it mcamel-common-mysql-cluster-mysql-0 -n mcamel-system -c mysql -- mysql --defaults-file=/etc/mysql/client.conf
```

分别进入到 MySQL 的 Pod 内，查看 `slave` 的状态信息，为空的一个就是原来的 `master`:

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

针对 master 的 mysql shell 执行：

```sql
mysql > stop slave;reset slave;
```

此时再手动 edit master 的 pod：`role replica => master ,healthy no => yes`；针对 slave 的 mysql shell 执行：

```sql
mysql > start slave;
```

如果主从没有建立联系，在 slave 的 mysql shell 执行：

```sql
-- 注意替换下 {master-host-pod-index}
mysql > change master to master_host='mcamel-common-mysql-cluster-mysql-{master-host-pod-index}.mysql.mcamel-system',master_port=3306,master_user='root',master_password='{password}',master_auto_position=1,MASTER_HEARTBEAT_PERIOD=2,MASTER_CONNECT_RETRY=1, MASTER_RETRY_COUNT=86400;
```

## Mysql pod 节点是 (3/4) running 状态，describe 出 unhealthy 状态

![image](../images/faq-mysql-1.png)

使用 `kubectl describe` 上图中框起来的 pod，发现异常提示： `Warning  Unhealthy  4m50s (x7194 over 3h58m)  kubelet  Readiness probe failed:
`

此时需要手工进行修复，这是目前开源 `mysql-operator` 版本的 BUG，详情查看： [[bugfix]update node_controller.go](https://github.com/bitpoke/mysql-operator/pull/857)

修复方式有两种：

1. 可以 `重启mysql-operator`
2. 手工更新 `sys_operator` 的配置状态

```bash
[root@master-01 ~]# kubectl exec mcamel-common-mysql-cluster-mysql-1 -n mcamel-system -c mysql -- mysql --defaults-file=/etc/mysql/client.conf -NB -e 'update sys_operator.status set value="1"  WHERE name="configured"'
```

## 数据库运行正常，使用 CR 创建数据库出现了报错

此类问题的原因有：`mysql root 密码有特殊字符`

![image](../images/faq-mysql-2.png)

获取原密码，如果出现了 密码里面含有 `-` 特殊字符，请换一个密码重装。

```bash
[root@master-01 ~]# kubectl get secret -n mcamel-system mcamel-common-mysql-cluster-secret -o=jsonpath='{.data.ROOT_PASSWORD}' | base64 -d

# 如果密码是带有 `-` 时，进入 mysql 的 shell 会出现输入原密码出现以下错误
bash-4.4# mysql -uroot -p
Enter password:
ERROR 1045 (28000): Access denied for user 'root'@'localhost' (using password: YES)
```
