# MySQL MGR Troubleshooting Manual

## Common Commands

### Retrieve Root Password

To find the secret resource ending with "-mgr-secret" in the namespace of the MySQL MGR cluster, here is an example to retrieve the secret for the "kpanda-mgr" cluster:

```shell
kubectl get secrets/kpanda-mgr-mgr-secret -n mcamel-system --template={{.data.rootPassword}} | base64 -d
```

The command will output the root password, for example:

```
root123!
```

### Check Cluster Status

You can check the cluster status using the MySQL command line:

```shell
mysqlsh -uroot -pPassword -- cluster status
```

Replace `Password` with the actual root password retrieved in the previous step.

```sql
sh-4.4$ mysqlsh -uroot -pPassword  -- cluster status
{
    "clusterName": "kpanda_mgr", 
    "defaultReplicaSet": {
        "name": "default", 
        "primary": "kpanda-mgr-2.kpanda-mgr-instances.mcamel-system.svc.cluster.local:3306", 
        "ssl": "REQUIRED", 
        "status": "OK", 
        "statusText": "Cluster is ONLINE and can tolerate up to ONE failure.", 
        "topology": {
            "kpanda-mgr-0.kpanda-mgr-instances.mcamel-system.svc.cluster.local:3306": {
                "address": "kpanda-mgr-0.kpanda-mgr-instances.mcamel-system.svc.cluster.local:3306", 
                "memberRole": "SECONDARY", 
                "mode": "R/O", 
                "readReplicas": {}, 
                "replicationLag": "applier_queue_applied", 
                "role": "HA", 
                "status": "ONLINE", 
                "version": "8.0.31"
            }, 
            "kpanda-mgr-1.kpanda-mgr-instances.mcamel-system.svc.cluster.local:3306": {
                "address": "kpanda-mgr-1.kpanda-mgr-instances.mcamel-system.svc.cluster.local:3306", 
                "memberRole": "SECONDARY", 
                "mode": "R/O", 
                "readReplicas": {}, 
                "replicationLag": "applier_queue_applied", 
                "role": "HA", 
                "status": "ONLINE", 
                "version": "8.0.31"
            }, 
            "kpanda-mgr-2.kpanda-mgr-instances.mcamel-system.svc.cluster.local:3306": {
                "address": "kpanda-mgr-2.kpanda-mgr-instances.mcamel-system.svc.cluster.local:3306", 
                "memberRole": "PRIMARY", 
                "mode": "R/W", 
                "readReplicas": {}, 
                "replicationLag": "applier_queue_applied", 
                "role": "HA", 
                "status": "ONLINE", 
                "version": "8.0.31"
            }
        }, 
        "topologyMode": "Single-Primary"
    }, 
    "groupInformationSourceMember": "kpanda-mgr-2.kpanda-mgr-instances.mcamel-system.svc.cluster.local:3306"
}
```

!!! note

    Under normal circumstances in the cluster:

    - The status of all nodes should be ONLINE.
    - One node should have the memberRole of PRIMARY, while the other nodes should have the memberRole of SECONDARY.

To check using an SQL statement: `SELECT * FROM performance_schema.replication_group_members\G`

```sql
mysql> SELECT * FROM performance_schema.replication_group_members\G
*************************** 1. row ***************************
              CHANNEL_NAME: group_replication_applier
                 MEMBER_ID: 6f464f4e-ba96-11ee-a028-a225dc125542
               MEMBER_HOST: kpanda-mgr-2.kpanda-mgr-instances.mcamel-system.svc.cluster.local
               MEMBER_PORT: 3306
              MEMBER_STATE: ONLINE
               MEMBER_ROLE: PRIMARY
            MEMBER_VERSION: 8.0.31
MEMBER_COMMUNICATION_STACK: MySQL
*************************** 2. row ***************************
              CHANNEL_NAME: group_replication_applier
                 MEMBER_ID: b3a53102-bfec-11ee-a821-0a8fb9f7d1ce
               MEMBER_HOST: kpanda-mgr-0.kpanda-mgr-instances.mcamel-system.svc.cluster.local
               MEMBER_PORT: 3306
              MEMBER_STATE: ONLINE
               MEMBER_ROLE: SECONDARY
            MEMBER_VERSION: 8.0.31
MEMBER_COMMUNICATION_STACK: MySQL
*************************** 3. row ***************************
              CHANNEL_NAME: group_replication_applier
                 MEMBER_ID: bdddd16f-bfec-11ee-a7a4-324c8edaca40
               MEMBER_HOST: kpanda-mgr-1.kpanda-mgr-instances.mcamel-system.svc.cluster.local
               MEMBER_PORT: 3306
              MEMBER_STATE: ONLINE
               MEMBER_ROLE: SECONDARY
            MEMBER_VERSION: 8.0.31
MEMBER_COMMUNICATION_STACK: MySQL
3 rows in set (0.00 sec)
```

### View Member Status

View member status: `SELECT * FROM performance_schema.replication_group_member_stats\G`

```sql
mysql> SELECT * FROM performance_schema.replication_group_member_stats\G
*************************** 1. row ***************************
                              CHANNEL_NAME: group_replication_applier
                                   VIEW_ID: 17066729271025607:9
                                 MEMBER_ID: 6f464f4e-ba96-11ee-a028-a225dc125542
               COUNT_TRANSACTIONS_IN_QUEUE: 0
                COUNT_TRANSACTIONS_CHECKED: 4748638
                  COUNT_CONFLICTS_DETECTED: 0
        COUNT_TRANSACTIONS_ROWS_VALIDATING: 1109
        TRANSACTIONS_COMMITTED_ALL_MEMBERS: 6f464f4e-ba96-11ee-a028-a225dc125542:1-10,
95201c7d-ba96-11ee-a018-bed74fb0bf8d:1-8,
b438e224-ba96-11ee-bc57-bed74fb0bf8d:1-12516339,
b439a7d3-ba96-11ee-bc57-bed74fb0bf8d:1-18
            LAST_CONFLICT_FREE_TRANSACTION: b438e224-ba96-11ee-bc57-bed74fb0bf8d:12519298
COUNT_TRANSACTIONS_REMOTE_IN_APPLIER_QUEUE: 0
         COUNT_TRANSACTIONS_REMOTE_APPLIED: 6
         COUNT_TRANSACTIONS_LOCAL_PROPOSED: 4748638
         COUNT_TRANSACTIONS_LOCAL_ROLLBACK: 0
*************************** 2. row ***************************
                              CHANNEL_NAME: group_replication_applier
                                   VIEW_ID: 17066729271025607:9
                                 MEMBER_ID: b3a53102-bfec-11ee-a821-0a8fb9f7d1ce
               COUNT_TRANSACTIONS_IN_QUEUE: 0
                COUNT_TRANSACTIONS_CHECKED: 4514132
                  COUNT_CONFLICTS_DETECTED: 0
        COUNT_TRANSACTIONS_ROWS_VALIDATING: 1110
        TRANSACTIONS_COMMITTED_ALL_MEMBERS: 6f464f4e-ba96-11ee-a028-a225dc125542:1-10,
95201c7d-ba96-11ee-a018-bed74fb0bf8d:1-8,
b438e224-ba96-11ee-bc57-bed74fb0bf8d:1-12519027,
b439a7d3-ba96-11ee-bc57-bed74fb0bf8d:1-18
            LAST_CONFLICT_FREE_TRANSACTION: b438e224-ba96-11ee-bc57-bed74fb0bf8d:12520590
COUNT_TRANSACTIONS_REMOTE_IN_APPLIER_QUEUE: 0
         COUNT_TRANSACTIONS_REMOTE_APPLIED: 4514129
         COUNT_TRANSACTIONS_LOCAL_PROPOSED: 0
         COUNT_TRANSACTIONS_LOCAL_ROLLBACK: 0
*************************** 3. row ***************************
                              CHANNEL_NAME: group_replication_applier
                                   VIEW_ID: 17066729271025607:9
                                 MEMBER_ID: bdddd16f-bfec-11ee-a7a4-324c8edaca40
               COUNT_TRANSACTIONS_IN_QUEUE: 0
                COUNT_TRANSACTIONS_CHECKED: 4658713
                  COUNT_CONFLICTS_DETECTED: 0
        COUNT_TRANSACTIONS_ROWS_VALIDATING: 1093
        TRANSACTIONS_COMMITTED_ALL_MEMBERS: 6f464f4e-ba96-11ee-a028-a225dc125542:1-10,
95201c7d-ba96-11ee-a018-bed74fb0bf8d:1-8,
b438e224-ba96-11ee-bc57-bed74fb0bf8d:1-12519027,
b439a7d3-ba96-11ee-bc57-bed74fb0bf8d:1-18
            LAST_CONFLICT_FREE_TRANSACTION: b438e224-ba96-11ee-bc57-bed74fb0bf8d:12520335
COUNT_TRANSACTIONS_REMOTE_IN_APPLIER_QUEUE: 0
         COUNT_TRANSACTIONS_REMOTE_APPLIED: 4658715
         COUNT_TRANSACTIONS_LOCAL_PROPOSED: 0
         COUNT_TRANSACTIONS_LOCAL_ROLLBACK: 0
3 rows in set (0.00 sec)
```

### Assign Member Role

1. Assign a node as PRIMARY.

    ```shell
    select group_replication_set_as_primary('4697c302-3e52-11ed-8e61-0050568a658a');
    ```

2. `mysqlsh` syntax

    ```shell
    JS > var c=dba.getCluster()
    JS > c.status()
    JS > c.setPrimaryInstance('172.30.71.128:3306')
    ```

## Common Failure Scenarios

### A SECONDARY node is not in ONLINE status

```json
{
    "clusterName": "mgr0117",
    "defaultReplicaSet": {
        "name": "default",
        "primary": "mgr0117-2.mgr0117-instances.m0103.svc.cluster.local:3306",
        "ssl": "REQUIRED",
        "status": "OK_NO_TOLERANCE_PARTIAL",
        "statusText": "Cluster is NOT tolerant to any failures. 1 member is not active.",
        "topology": {
            "mgr0117-0.mgr0117-instances.m0103.svc.cluster.local:3306": {
                "address": "mgr0117-0.mgr0117-instances.m0103.svc.cluster.local:3306",
                "instanceErrors": [
                    "NOTE: group_replication is stopped."
                ],
                "memberRole": "SECONDARY",
                "memberState": "OFFLINE",
                "mode": "R/O",
                "readReplicas": {},
                "role": "HA",
                "status": "(MISSING)",
                "version": "8.0.31"
            },
            "mgr0117-1.mgr0117-instances.m0103.svc.cluster.local:3306": {
                "address": "mgr0117-1.mgr0117-instances.m0103.svc.cluster.local:3306",
                "memberRole": "SECONDARY",
                "mode": "R/O",
                "readReplicas": {},
                "replicationLag": "applier_queue_applied",
                "role": "HA",
                "status": "ONLINE",
                "version": "8.0.31"
            },
            "mgr0117-2.mgr0117-instances.m0103.svc.cluster.local:3306": {
                "address": "mgr0117-2.mgr0117-instances.m0103.svc.cluster.local:3306",
                "memberRole": "PRIMARY",
                "mode": "R/W",
                "readReplicas": {},
                "replicationLag": "applier_queue_applied",
                "role": "HA",
                "status": "ONLINE",
                "version": "8.0.31"
            }
        },
        "topologyMode": "Single-Primary"
    },
    "groupInformationSourceMember": "mgr0117-2.mgr0117-instances.m0103.svc.cluster.local:3306"
}
```

Here, we see the proper address field is mgr0117-0.mgr0117-instances.m0103.svc.cluster.local:3306. Enter the mgr0117-0 pod and execute:

```sql
mysql> start group_replication;
Query OK, 0 rows affected (5.82 sec)
```

If the data volume is large, this node will remain in the RECOVERING state for a relatively long time.

### No PRIMARY Node

### All Nodes Show OFFLINE

```mysql
mysql> SELECT * FROM performance_schema.replication_group_members;
+---------------------------+-----------+-------------+-------------+--------------+-------------+----------------+----------------------------+
| CHANNEL_NAME              | MEMBER_ID | MEMBER_HOST | MEMBER_PORT | MEMBER_STATE | MEMBER_ROLE | MEMBER_VERSION | MEMBER_COMMUNICATION_STACK |
+---------------------------+-----------+-------------+-------------+--------------+-------------+----------------+----------------------------+
| group_replication_applier |           |             |        NULL | OFFLINE      |             |                |                            |
+---------------------------+-----------+-------------+-------------+--------------+-------------+----------------+----------------------------+
1 row in set (0.00 sec)
```

At this point, you can attempt to restart the cluster from the MySQL shell:

```shell
dba.rebootClusterFromCompleteOutage();
```

If the issue persists, log in to the previous PRIMARY node using the command line and start the group replication on that node:

```shell
set global group_replication_bootstrap_group=on;
start group_replication;
set global group_replication_bootstrap_group=off;
```

!!! warning

    For the other nodes, run the above commands sequentially.
