# MySQL Troubleshooting Manual

This page will continue to count and sort out common MySQL abnormal faults and repair methods. If you encounter problems in use, please read this troubleshooting manual first.

> If you find a problem that is not included in this manual, you can quickly jump to the bottom of the page and submit your problem.

## MySQL health check

You can view the MySQL health status with a single command:

```none
kubectl get pod -n mcamel-system -Lhealthy,role | grep mysql
```

The output is similar to:

```
mcamel-common-mysql-cluster-auto-2023-03-28t00-00-00-backujgg9m 0/1 Completed 0 27h
mcamel-common-mysql-cluster-auto-2023-03-29t00-00-00-backusgf59 0/1 Completed 0 3h43m
mcamel-common-mysql-cluster-mysql-0 4/4 Running 6 (11h ago) 25h yes master
mcamel-common-mysql-cluster-mysql-1 4/4 Running 690 (11h ago) 4d20h yes replica
mcamel-mysql-apiserver-9797c7f76-bvf5n 2/2 Running 0 22h
mcamel-mysql-ui-7ffd9dd8db-d5jfm 2/2 Running 0 25m
mysql-operator-0 2/2 Running 109 (47m ago) 2d21h
```

As shown above, if the status of the active and standby nodes (`master` `replica`) is `yes`, it means that MySQL is in a normal state.

## MySQL Pods

You can quickly view the health status of all `MySQL` instances on the current cluster with the following command:

```bash
kubectl get mysql -A
```

The output is similar to:

```bash
NAMESPACE NAME READY REPLICAS AGE
ghippo-system test True 1 3d
mcamel-system mcamel-common-mysql-cluster False 2 62d
```

### Pod running = 0/4 with status `Init:Error`

When encountering such problems, the first thing you should look at is the (sidecar) log information of the `master` node.

```bash
kubectl get pod -n mcamel-system -Lhealthy,role | grep cluster-mysql | grep master | awk '{print $1}' | xargs -I {} kubectl logs -f {} -n mcamel-system -c sidecar
```

??? note "Example output content"

     ```none
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
     E0209 05:38:56.223635 1 deleg.go:144] sidecar "msg"="failed waiting for xtrabackup to finish" "error"="exit status 1"
     ```

Log in to `MySQL` of the `master` node, and run `alter` table structure:

```bash
[root@master-01 ~]$ kubectl get pod -n mcamel-system -Lhealthy,role | grep cluster-mysql | grep master
mcamel-common-mysql-cluster-mysql-0

# get password
[root@master-01 ~]$ kubectl get secret -n mcamel-system mcamel-common-mysql-cluster-secret -o=jsonpath='{.data.ROOT_PASSWORD}' | base64 -d

[root@master-01 ~]$ kubectl exec -it mcamel-common-mysql-cluster-mysql-0 -n mcamel-system -c mysql -- /bin/bash

# Note: Modifying the table structure requires root privileges to log in
~bash:mysql -uroot -p
```

??? note "The SQL statement is as follows"

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

### Pod running = 2/4

This kind of problem is probably because the disk usage used by the MySQL instance has reached 100%, you can run the following command on the `master` node to check the disk usage.

```bash
kubectl get pod -n mcamel-system | grep cluster-mysql | awk '{print $1}' | xargs -I {} kubectl exec {} -n mcamel-system -c sidecar -- df -h | grep /var/lib /mysql
```

The output is similar to:

```console
/dev/drbd43001 50G 30G 21G 60% /var/lib/mysql
/dev/drbd43005 80G 29G 52G 36% /var/lib/mysql
```

If a PVC is found to be full, the PVC needs to be expanded.

```bash
kubectl edit pvc data-mcamel-common-mysql-cluster-mysql-0 -n mcamel-system # just modify the request size
```

### Pod running = 3/4

<!--screenshot-->

Use `kubectl describe` to frame the Pod in the above picture, and find an abnormal prompt: `Warning Unhealthy 4m50s (x7194 over 3h58m) kubelet Readiness probe failed: `

At this time, it needs to be repaired manually. This is the [Bug] of the current open source `mysql-operator` version (https://github.com/bitpoke/mysql-operator/pull/857)

There are two ways to fix it:

- restart `mysql-operator`, or
- Manually update configuration status of `sys_operator`

```bash
kubectl exec mcamel-common-mysql-cluster-mysql-1 -n mcamel-system -c mysql -- mysql --defaults-file=/etc/mysql/client.conf -NB -e 'update sys_operator.status set value= "1" WHERE name="configured"'
```

## MySQL Operator

### `storageClass` not specified

`mysql-operator` cannot obtain a PVC and is in `pending` state because `storageClass` is not specified.

If you use Helm to start, you can do the following settings:

1. Application to close PVC

     ```bash
     orchestrator.persistence.enabled=false
     ```

2. Specify storageClass to get PVC

     ```bash
     orchestrator.persistence.storageClass={storageClassName}
     ```

If you use other tools, you can modify the corresponding fields in `value.yaml` to achieve the same effect as Helm startup.

## MySQL master-slave relationship

1. Run the following command to confirm the MySQL status:

     ```bash
     kubectl get mysql -A
     ```

     The output is similar to:

     ```
     NAMESPACE NAME READY REPLICAS AGE
     ghippo-system test True 1 3d
     mcamel-system mcamel-common-mysql-cluster False 2 62d
     ```

2. Pay attention to the library whose `Ready` field value is `False` (the judgment of `True` here is that the delay is less than 30s for synchronization), and check the logs of the MySQL slave library

     ```bash
     [root@master-01 ~]$ kubectl get pod -n mcamel-system -Lhealthy,role | grep cluster-mysql | grep replica | awk '{print $1}' | xargs -I {} kubectl logs {} -n mcamel -system -c mysql | grep ERROR
     ```

### There is no error from the library, but the synchronization delay is large

If there is no error `ERROR` message in the log, it means `False` is only because the delay of master-slave synchronization is too large, you can run the following command on the slave library for further investigation:

1. Find the Pod of the slave node

     ```bash
     kubectl get pod -n mcamel-system -Lhealthy,role | grep cluster-mysql | grep replica | awk '{print $1}'
     ```

     The output is similar to:

     ```
     mcamel-common-mysql-cluster-mysql-1
     ```

2. Set the `binlog` parameter

     ```bash
     kubectl exec mcamel-common-mysql-cluster-mysql-1 -n mcamel-system -c mysql -- mysql --defaults-file=/etc/mysql/client.conf -NB -e 'set global sync_binlog=10086;'
     ```

3. Enter the MySQL container

     ```bash
     kubectl exec -it mcamel-common-mysql-cluster-mysql-1 -n mcamel-system -c mysql -- mysql --defaults-file=/etc/mysql/client.conf
     ```

4. Run the view command in the MySQL container to obtain the status of the slave library.

     The `Seconds_Behind_Master` field is the master-slave delay. If the value is 0~30, it can be considered that there is no delay; it means that the master-slave can maintain synchronization.

     ??? note "The SQL statement is as follows"

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

5. After master-slave synchronization, `Seconds_Behind_Master` is less than 30s, set `sync_binlog=1`

     ```bash
     kubectl exec mcamel-common-mysql-cluster-mysql-1 -n mcamel-system -c mysql -- mysql --defaults-file=/etc/mysql/client.conf -NB -e 'set global sync_binlog=1';
     ```

6. If there is still no relief at this time, you can check whether the host load or IO of the slave library is too high, and run the following command:

     ```bash
     [root@master-01 ~]$ uptime
     11:18 up 1 day, 17:49, 2 users, load averages: 9.33 7.08 6.28
     ```

     `load averages` under normal circumstances, none of the three values should exceed 10 for a long time; if it exceeds 30, please allocate the Pod and disk of this node reasonably.

### `Replication Error` from library log

If there is a slave library replication error in the Pod log of the slave library, there may be multiple reasons. You can confirm the repair method based on other error messages that appear at the same time.

#### purged binlog error

Note the following example, if the keyword `purged binlog` appears, it is usually necessary to perform rebuild processing on the slave library.

??? note "Error Example"

    ```bash
    [root@demo-alpha-master-01 /]$ kubectl get pod -n mcamel-system -Lhealthy,role | grep cluster-mysql | grep replica | awk '{print $1}' | xargs -I {} kubectl logs {} -n mcamel-system -c mysql | grep ERROR
    2023-02-08T18:43:21.991730Z 116 [ERROR] [MY-010557] [Repl] Error reading packet from server for channel '': Cannot replicate because the master purged required binary logs. Replicate the missing transactions from elsewhere, or provision a new slave from backup. Consider increasing the master's binary log expiration period. The GTID sets and the missing purged transactions are too long to print in this message. For more information, please see the master's error log or the manual for GTID_SUBTRACT (server_errno=1236)
    2023-02-08T18:43:21.991777Z 116 [ERROR] [MY-013114] [Repl] Slave I/O for channel '': Got fatal error 1236 from master when reading data from binary log: 'Cannot replicate because the master purged required binary logs. Replicate the missing transactions from elsewhere, or provision a new slave from backup. Consider increasing the master's binary log expiration period. The GTID sets and the missing purged transactions are too long to print in this message. For more information, please see the master's error log or the manual for GTID_SUBTRACT', Error_code: MY-013114
    ```

The reconstruction operation is as follows:

1. Find the Pod of the slave node

    ```bash
    [root@master-01 ~]$ kubectl get pod -n mcamel-system -Lhealthy,role | grep cluster-mysql | grep replica | awk '{print $1}'
    mcamel-common-mysql-cluster-mysql-1
    ```

1. Find the PVC of the slave node
    
    ```bash
    [root@master-01 /]$ kubectl get pvc -n mcamel-system | grep mcamel-common-mysql-cluster-mysql-1
    data-mcamel-common-mysql-cluster-mysql-1 Bound pvc-5840569e-834f-4236-a5c6-878e41c55c85 50Gi RWO local-path 33d
    ```

1. Delete the PVC of the slave node

    ```bash
    [root@master-01 /]$ kubectl delete pvc data-mcamel-common-mysql-cluster-mysql-1 -n mcamel-system
    persistentvolumeclaim "data-mcamel-common-mysql-cluster-mysql-1" deleted
    ```

1. Delete the Pod from the library

    ```bash
    [root@master-01 /]$ kubectl delete pod mcamel-common-mysql-cluster-mysql-1 -n mcamel-system
    pod "mcamel-common-mysql-cluster-mysql-1" deleted
    ```

#### primary key conflict error

??? note "Error instance"

     ```bash
     [root@demo-alpha-master-01 /]$ kubectl get pod -n mcamel-system -Lhealthy,role | grep cluster-mysql | grep replica | awk '{print $1}' | xargs -I {} kubectl logs { } -n mcamel-system -c mysql | grep ERROR
     2023-02-08T18:43:21.991730Z 116 [ERROR] [MY-010557] [Repl] Could notrun Write_rows event on table dr_brower_db.dr_user_info; Duplicate entry '24' for key 'PRIMARY', Error_code:1062 ; handler error HA_ERR_FOUND_DUPP_KEY ; the event's master logmysql-bin.000010, end_log_pos 5295916
     ```

If you see in the error log: `Duplicate entry '24' for key 'PRIMARY', Error_code:1062; handler error HA_ERR_FOUND_DUPP_KEY;`,

Indicates that there is a primary key conflict, or an error that the primary key does not exist. At this point, the error can be skipped in the form of idempotent recovery or inserting an empty transaction:

**Method 1**: Idempotent mode recovery

1. Find the Pod of the slave node

     ```bash
     [root@master-01 ~]$ kubectl get pod -n mcamel-system -Lhealthy,role | grep cluster-mysql | grep replica | awk '{print $1}'
     mcamel-common-mysql-cluster-mysql-1
     ```

2. Set mysql idempotent mode

     ```bash
     [root@master-01 ~]$ kubectl exec mcamel-common-mysql-cluster-mysql-1 -n mcamel-system -c mysql -- mysql --defaults-file=/etc/mysql/client.conf -NB - e 'stop slave;set global slave_exec_mode="IDEMPOTENT";set global sync_binlog=10086;start slave;'
     ```

**Method 2**: Insert empty transaction skip error

```sql
mysql> stop slave;
mysql> SET @@SESSION.GTID_NEXT= 'xxxxx:105220'; /* The specific value is mentioned in the log */
mysql> BEGIN;
mysql> COMMIT;
mysql> SET SESSION GTID_NEXT = AUTOMATIC;
mysql> START SLAVE;
```

After performing the above operations, observe the progress of rebuilding from the library:

```bash
# Enter the mysql container
[root@master-01 ~]$ kubectl exec -it mcamel-common-mysql-cluster-mysql-1 -n mcamel-system -c mysql -- mysql --defaults-file=/etc/mysql/client.conf
```

Run the following command to view the master-slave delay status field `Seconds_Behind_Master` of the slave library. If the value is 0~30, it means that there is no master-slave delay, and the master library and the slave library are basically in sync.

```sql
mysql> show slave status\G;
```

After confirming the master-slave synchronization (Seconds_Behind_Master is less than 30s), run the following command to set MySQL strict mode:

```bash
[root@master-01 ~]$ kubectl exec mcamel-common-mysql-cluster-mysql-1 -n mcamel-system -c mysql -- mysql --defaults-file=/etc/mysql/client.conf -NB - e 'stop slave;set global slave_exec_mode="STRICT";set global sync_binlog=10086;start slave;
```

#### Similar errors from `[Note] Slave: MTS group recovery relay log info based on Worker-Id 0, group_r` from the library

1. Find the Pod of the slave node

     ```shell
     [root@master-01 ~]# kubectl get pod -n mcamel-system -Lhealthy,role | grep cluster-mysql | grep replica | awk '{print $1}'
     mcamel-common-mysql-cluster-mysql-1
     ```

2. Set the slave library to skip this log and continue copying

     ```shell
     [root@master-01 ~]# kubectl exec mcamel-common-mysql-cluster-mysql-1 -n mcamel-system -c mysql -- mysql --defaults-file=/etc/mysql/client.conf -NB - e 'stop slave;reset slave;change master to MASTER_AUTO_POSITION = 1;start slave;';
     ```

>Tips:

> 1. This case can be executed in idempotent mode.

>2. This type of error can also be redone from the library.

### The active and standby Pods are both `replica`

1. Through the following command, it is found that the two MySQL Pods are both `replica` roles, and one of them needs to be changed to `master`.

     ```bash
     [root@aster-01 ~]$ kubectl get pod -n mcamel-system -Lhealthy,role|grep mysql
     mcamel-common-mysql-cluster-mysql-0 4/4 Running 5 (16h ago) 16h no replica
     mcamel-common-mysql-cluster-mysql-1 4/4 Running 6 (16h ago) 16h no replica
     mysql-operator-0 2/2 Running 1 (16h ago) 16h
     ```

2. Enter MySQL to view:

     ```bash
     kubectl exec -it mcamel-common-mysql-cluster-mysql-0 -n mcamel-system -c mysql -- mysql --defaults-file=/etc/mysql/client.conf
     ```

3. Check the status information of `slave`, if the query result is empty, it is the original `master`, as shown in the example below corresponding to `mysql-0`:

     ??? note "Status Information Example"

         ```sql
         --mysql-0
         mysql> show slave status\G;
         empty set, 1 warning (0.00 sec)

         --mysql-1
         mysql> show slave status\G;
         *************************** 1. row ********************* *****
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
                     Slave_SQL_Running: YesReplicate_Do_DB:
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

4. Perform a reset operation against the master's mysql shell:

     ```sql
     mysql > stop slave; reset slave;
     ```

5. At this point, manually edit the Pod of the master: `role replica => master , healthy no => yes`.

6. Execute for the mysql shell of the slave:

     ```sql
     mysql> start slave;
     ```

7. If the master-slave has not established a connection, run in the mysql shell of the slave:

     ```sql
     -- Pay attention to replace {master-host-pod-index}
     mysql > change master to master_host='mcamel-common-mysql-cluster-mysql-{master-host-pod-index}.mysql.mcamel-system', master_port=3306, master_user='root', master_password='{password }', master_auto_position=1, MASTER_HEARTBEAT_PERIOD=2, MASTER_CONNECT_RETRY=1, MASTER_RETRY_COUNT=86400;
     ```

### Inconsistent primary and secondary data - active data synchronization

When the master-slave instance data is inconsistent, you can run the following command to complete the master-slave consistency synchronization:

```sql
pt-table-sync --execute --charset=utf8 --ignore-databases=mysql,sys,percona --databases=amamba,audit,ghippo,insight,ipavo,keycloak,kpanda,skoala dsn=u=root,p =xxx,h=mcamel-common-kpanda-mysql-cluster-mysql-0.mysql.mcamel-system,P=3306 dsn=u=root,p=xxx,h=mcamel-common-kpanda-mysql-cluster- mysql.mysql.mcamel-system,P=3306 --print

pt-table-sync --execute --charset=utf8 --ignore-databases=mysql,sys,percona --databases=kpanda dsn=u=root,p=xxx,h=mcamel-common-kpanda-mysql-cluster -mysql-0.mysql.mcamel-system,P=3306 dsn=u=root,p=xxx,h=mcamel-common-kpanda-mysql-cluster-mysql-1.mysql.mcamel-system,P=3306 - -print
```

Use pt-table-sync to complete data supplementation, in the example it is `mysql-0=> mysql-1` supplementary data.

This scenario is often applicable to master-slave switching, and it is found that the new slave library has redundant executed gtids to supplement the data before redoing.

This kind of supplementary data can only ensure that the data will not be lost. If the deleted data in the new main database will be added back, it is a potential risk. If there is data in the new main database, it will be replaced with old data, which is also a risk.

## Other failures

### CR fails to create a database and reports an error

The database is running normally, but an error is reported when using CR to create the database. The reasons for this kind of problem are: `mysql root` password has special characters

<!--screenshot-->

1. Obtain and view the original password:

     ```bash
     [root@master-01 ~]$ kubectl get secret -n mcamel-system mcamel-common-mysql-cluster-secret -o=jsonpath='{.data.ROOT_PASSWORD}' | base64 -d
     ```

2. If the password contains special characters `-`, enter the MySQL shell and enter the original password, the following error occurs

     ```bash
     bash-4.4# mysql -uroot -p
     Enter password:
     ERROR 1045 (28000): Access denied for user 'root'@'localhost' (using password: YES)
     ```

3. Clean and rebuild:

     - Method 1: Clean up the data directory, delete the Pod and wait for the sidecar to run, delete the data directory again, and then delete the Pod to restore:

     ```bash
     [root@master-01 ~]# kubectl exec -it mcamel-common-mysql-cluster-mysql-1 -n mcamel-system -c sidecar -- /bin/sh
     sh-4.4# cd /var/lib/mysql
     sh-4.4# ls | xargs rm -rf
     ```

     - Method 2: Delete the PVC and then delete the Pod. It only needs to be processed once to recover:

     ```bash
     kubectl delete pvc data-mcamel-common-mysql-cluster-mysql-1 -n mcamel-system
     ```

     ```bash
     kubectl delete pod mcamel-common-mysql-cluster-mysql-1 -n mcamel-system
     ```