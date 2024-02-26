# MySQL Master-Slave Relationship

The master-slave relationship in MySQL can be complex when it comes to troubleshooting, as different symptoms may require different solutions.

1. Run the following command to confirm the MySQL status:

    ```bash
    kubectl get mysql -A
    ```

    The output will be similar to:

    ```
    NAMESPACE       NAME                          READY   REPLICAS   AGE
    ghippo-system   test                          True    1          3d
    mcamel-system   mcamel-common-mysql-cluster   False   2          62d
    ```

2. Pay attention to the databases with a __Ready__ field value of __False__ (here, the judgement of __True__ is that the delay is less than 30 seconds), and check the logs of the MySQL slave:

    ```bash
    [root@master-01 ~]$ kubectl get pod -n mcamel-system -Lhealthy,role | grep cluster-mysql | grep replica | awk '{print $1}' | xargs -I {} kubectl logs {} -n mcamel-system -c mysql | grep ERROR
    ```

When the instance status is __False__ , there may be several types of failures. You can troubleshoot and fix them based on the information in the database logs.

## Instance Status is __False__ but No Error Messages in Logs

If there are no __ERROR__ messages in the logs of the slave, it means that the __False__ status is due to a large delay in master-slave synchronization. You can further investigate the slave by performing the following steps:

1. Find the Pod of the slave node:

    ```bash
    kubectl get pod -n mcamel-system -Lhealthy,role | grep cluster-mysql | grep replica | awk '{print $1}'
    ```

    The output will be similar to:

    ```
    mcamel-common-mysql-cluster-mysql-1
    ```

2. Set the __binlog__ parameter:

    ```bash
    kubectl exec mcamel-common-mysql-cluster-mysql-1 -n mcamel-system -c mysql -- mysql --defaults-file=/etc/mysql/client.conf -NB -e 'set global sync_binlog=10086;'
    ```

3. Enter the MySQL container:

    ```bash
    kubectl exec -it mcamel-common-mysql-cluster-mysql-1 -n mcamel-system -c mysql -- mysql --defaults-file=/etc/mysql/client.conf
    ```

4. Run the following command inside the MySQL container to check the slave status.

    The __Seconds_Behind_Master__ field indicates the delay between the master and slave. If the value is between 0 and 30, it can be considered as no delay, indicating that the master and slave are in sync.

    ??? note "SQL statements"

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

5. After the master-slave synchronization, if __Seconds_Behind_Master__ is less than 30s, set __sync_binlog=1__ :

    ```bash
    kubectl exec mcamel-common-mysql-cluster-mysql-1 -n mcamel-system -c mysql -- mysql --defaults-file=/etc/mysql/client.conf -NB -e 'set global sync_binlog=1';
    ```

6. If the issue persists, you can check the host load or IO of the slave node by running the following command:

    ```bash
    [root@master-01 ~]$ uptime
    11:18  up 1 day, 17:49, 2 users, load averages: 9.33 7.08 6.28
    ```

    In normal circumstances, the __load averages__ should not exceed 10 for a prolonged period. If it exceeds 30 or above, consider adjusting the Pod and disk allocation for that node.

## Replication Error in Slave Logs

If there are replication errors in the logs of the slave Pod, it may be caused by various reasons. The following sections will provide different scenarios along with their corresponding diagnosis and repair methods.

### Purged Binlog Error

In case you encounter the keyword __purged binlog__ in the logs, it typically indicates the need to rebuild the slave.

??? note "Erros"

    ```bash
    [root@demo-alpha-master-01 /]$ kubectl get pod -n mcamel-system -Lhealthy,role | grep cluster-mysql | grep replica | awk '{print $1}' | xargs -I {} kubectl logs {} -n mcamel-system -c mysql | grep ERROR
    2023-02-08T18:43:21.991730Z 116 [ERROR] [MY-010557] [Repl] Error reading packet from server for channel '': Cannot replicate because the master purged required binary logs. Replicate the missing transactions from elsewhere, or provision a new slave from backup. Consider increasing the master's binary log expiration period. The GTID sets and the missing purged transactions are too long to print in this message. For more information, please see the master's error log or the manual for GTID_SUBTRACT (server_errno=1236)
    2023-02-08T18:43:21.991777Z 116 [ERROR] [MY-013114] [Repl] Slave I/O for channel '': Got fatal error 1236 from master when reading data from binary log: 'Cannot replicate because the master purged required binary logs. Replicate the missing transactions from elsewhere, or provision a new slave from backup. Consider increasing the master's binary log expiration period. The GTID sets and the missing purged transactions are too long to print in this message. For more information, please see the master's error log or the manual for GTID_SUBTRACT', Error_code: MY-013114
    ```

The steps to perform the rebuild operation are as follows:

1. Find the Pod of the slave node:

    ```bash
    [root@master-01 ~]$ kubectl get pod -n mcamel-system -Lhealthy,role | grep cluster-mysql | grep replica | awk '{print $1}'
    mcamel-common-mysql-cluster-mysql-1
    ```

2. Find the PVC (PersistentVolumeClaim) of the slave node:

    ```bash
    [root@master-01 /]$ kubectl get pvc -n mcamel-system | grep mcamel-common-mysql-cluster-mysql-1
    data-mcamel-common-mysql-cluster-mysql-1                                        Bound    pvc-5840569e-834f-4236-a5c6-878e41c55c85   50Gi       RWO            local-path                   33d
    ```

3. Delete the PVC of the slave node:

    ```bash
    [root@master-01 /]$ kubectl delete pvc data-mcamel-common-mysql-cluster-mysql-1 -n mcamel-system
    persistentvolumeclaim "data-mcamel-common-mysql-cluster-mysql-1" deleted
    ```

4. Delete the Pod of the slave:

    ```bash
    [root@master-01 /]$ kubectl delete pod mcamel-common-mysql-cluster-mysql-1 -n mcamel-system
    pod "mcamel-common-mysql-cluster-mysql-1" deleted
    ```

### Primary Key Conflict Error

??? note "Errors"

    ```bash
    [root@demo-alpha-master-01 /]$ kubectl get pod -n mcamel-system -Lhealthy,role | grep cluster-mysql | grep replica | awk '{print $1}' | xargs -I {} kubectl logs {} -n mcamel-system -c mysql | grep ERROR
    2023-02-08T18:43:21.991730Z 116 [ERROR] [MY-010557] [Repl] Could notexecute Write_rows event on table dr_brower_db.dr_user_info; Duplicate entry '24' for key 'PRIMARY', Error_code:1062; handler error HA_ERR_FOUND_DUPP_KEY; the event's master logmysql-bin.000010, end_log_pos 5295916
    ```

If you see the following error in the error log: __Duplicate entry '24' for key 'PRIMARY', Error_code:1062; handler error HA_ERR_FOUND_DUPP_KEY;__ , it indicates a primary key conflict or an error where the primary key does not exist. In such cases, you can recover using an idempotent mode or skip the error by inserting an empty transaction:

**Method 1**: Idempotent Recovery

1. Find the Pod of the slave node:

    ```bash
    [root@master-01 ~]$ kubectl get pod -n mcamel-system -Lhealthy,role | grep cluster-mysql | grep replica | awk '{print $1}'
    mcamel-common-mysql-cluster-mysql-1
    ```

2. Set MySQL to idempotent mode:

    ```bash
    [root@master-01 ~]$ kubectl exec mcamel-common-mysql-cluster-mysql-1 -n mcamel-system -c mysql -- mysql --defaults-file=/etc/mysql/client.conf -NB -e 'stop slave;set global slave_exec_mode="IDEMPOTENT";set global sync_binlog=10086;start slave;'
    ```

**Method 2**: Insert Empty Transaction to Skip Error

```sql
mysql> stop slave;
mysql> SET @@SESSION.GTID_NEXT= 'xxxxx:105220'; /* Specific value mentioned in the logs */
mysql> BEGIN;
mysql> COMMIT;
mysql> SET SESSION GTID_NEXT = AUTOMATIC;
mysql> START SLAVE;
```

After completing the above steps, observe the progress of the slave rebuild:

```bash
# Enter the MySQL container
[root@master-01 ~]$ kubectl exec -it mcamel-common-mysql-cluster-mysql-1 -n mcamel-system -c mysql -- mysql --defaults-file=/etc/mysql/client.conf
```

Run the following command to check the slave's replication delay status in the field __Seconds_Behind_Master__ . If the value is between 0 and 30, it indicates that there is no significant delay, and the master and slave databases are essentially synchronized.

```sql
mysql> show slave status\G;
```

After confirming the master-slave synchronization (when __Seconds_Behind_Master__ is less than 30s), run the following command to set MySQL strict mode:

```bash
[root@master-01 ~]$ kubectl exec mcamel-common-mysql-cluster-mysql-1 -n mcamel-system -c mysql -- mysql --defaults-file=/etc/mysql/client.conf -NB -e 'stop slave;set global slave_exec_mode="STRICT";set global sync_binlog=10086;start slave;
```

### Replication Error in Master-Slave Setup

When the slave database encounters an error message similar to __[Note] Slave: MTS group recovery relay log info based on Worker-Id 0, group_r__ , you can perform the following steps:

1. Find the Pod of the slave node:

    ```shell
    [root@master-01 ~]# kubectl get pod -n mcamel-system -Lhealthy,role | grep cluster-mysql | grep replica | awk '{print $1}'
    mcamel-common-mysql-cluster-mysql-1
    ```

2. Set the slave to skip this particular log and continue replication:

    ```shell
    [root@master-01 ~]# kubectl exec mcamel-common-mysql-cluster-mysql-1 -n mcamel-system -c mysql -- mysql --defaults-file=/etc/mysql/client.conf -NB -e 'stop slave;reset slave;change master to MASTER_AUTO_POSITION = 1;start slave;'
    ```

!!! tip

    1. This situation can be handled using an idempotent mode.
    2. In such replication errors, redoing the setup on the slave database is also a viable option.

## Both Primary and Replica Pods are Labeled as __replica__ 

1. By executing the following command, you will discover that both MySQL Pods
   are labeled as __replica__ role. You need to correct one of them to __master__ .

    ```bash
    [root@aster-01 ~]$ kubectl get pod -n mcamel-system -Lhealthy,role|grep mysql
    mcamel-common-mysql-cluster-mysql-0                          4/4     Running   5 (16h ago)   16h   no       replica
    mcamel-common-mysql-cluster-mysql-1                          4/4     Running   6 (16h ago)   16h   no       replica
    mysql-operator-0                                             2/2     Running   1 (16h ago)   16h
    ```

2. Go to MySQL to check:

    ```bash
    kubectl exec -it mcamel-common-mysql-cluster-mysql-0 -n mcamel-system -c mysql -- mysql --defaults-file=/etc/mysql/client.conf
    ```

3. To check the status information of the __slave__ , look for the results where the query output is empty. These correspond to the original __master__ . In the example below, __mysql-0__ corresponds to the relevant content:

    ??? note "Status examples“

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

4. Perform a reset operation on the MySQL shell of the master:

    ```sql
    mysql> stop slave; reset slave;
    ```

5. Manually edit the Pod of the master: change its label from __role replica__ to __master__ and set __healthy no__ to __yes__ .

6. Run the following command on the MySQL shell of the slave:

    ```sql
    mysql> start slave;
    ```

7. If the master and slave are not establishing a connection, run the following command on the MySQL shell of the slave:

    ```sql
    -- Note to replace {master-host-pod-index}
    mysql > change master to master_host='mcamel-common-mysql-cluster-mysql-{master-host-pod-index}.mysql.mcamel-system',master_port=3306,master_user='root',master_password='{password}',master_auto_position=1,MASTER_HEARTBEAT_PERIOD=2,MASTER_CONNECT_RETRY=1, MASTER_RETRY_COUNT=86400;
    ```

## Inconsistent Primary and Standby Data

When there is inconsistency in data between the primary and standby instances, you can run the following commands to achieve primary-standby consistency synchronization:

```sql
pt-table-sync --execute --charset=utf8 --ignore-databases=mysql,sys,percona --databases=amamba,audit,ghippo,insight,ipavo,keycloak,kpanda,skoala dsn=u=root,p=xxx,h=mcamel-common-kpanda-mysql-cluster-mysql-0.mysql.mcamel-system,P=3306 dsn=u=root,p=xxx,h=mcamel-common-kpanda-mysql-cluster-mysql.mysql.mcamel-system,P=3306  --print

pt-table-sync --execute --charset=utf8 --ignore-databases=mysql,sys,percona --databases=kpanda dsn=u=root,p=xxx,h=mcamel-common-kpanda-mysql-cluster-mysql-0.mysql.mcamel-system,P=3306 dsn=u=root,p=xxx,h=mcamel-common-kpanda-mysql-cluster-mysql-1.mysql.mcamel-system,P=3306  --print
```

To address this issue and achieve data supplementation, you can use __pt-table-sync__ . The following example demonstrates how to supplement data from __mysql-0__ to __mysql-1__ .

This scenario is often applicable during master-slave switching, where the new slave has extra executed GTIDs that need to be synchronized before redoing the process.

Data supplementation ensures that data is not lost. However, there are potential risks involved. If the new master has deleted data, it will be re-supplemented. Additionally, if the new master has existing data, it will be replaced with older data.
