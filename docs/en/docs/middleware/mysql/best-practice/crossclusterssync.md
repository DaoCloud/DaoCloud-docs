# MySQL Cross-Cluster Synchronization

MySQL's built-in replication capability provides various replication methods such as master-slave, multi-slave, multi-master, and cascading, and supports data synchronization across versions (5.x, 8.x).

In this example, we will use a 1-to-1 master-slave configuration to achieve data synchronization between MySQL instances across clusters. Both the source and target instances have 3 replica instances. During the synchronization period, the target instance only provides read-only services and can run as an independent instance after the synchronization relationship is released.

!!! caution

    The replication function only performs incremental synchronization, and data differences that have occurred before the task starts will not be synchronized. Therefore, it is necessary to create the same database structure in the target database or use the mysqldump command to perform a full data synchronization. The following example uses mysqldump.

## Full Data Dump (Optional)

When the user's business database has a certain amount of existing data, it is recommended to perform a dump operation first to complete a full backup to ensure that the database structure and content between the master and slave are consistent.

1. Log in to the source node and perform the backup operation:

    ````shell
    # Enter the source Pod
    kubectl exec -it [Pod Name] -- /bin/bash
    # Lock the tables to prevent data inconsistency
    mysql> FLUSH TABLES WITH READ LOCK;
    # Perform dump on the target database
    shell> mysqldump -u [Username] --set-gtid-purged=off -p [Database Name] > backup.sql
    # Unlock the tables
    mysql> UNLOCK TABLES;
    # Exit the source Pod terminal and return to the node console
    shell> exit
    # Copy the backup file from the source Pod to the node it is on
    kubectl cp [Source Pod Name]:/path/to/backup.sql /path/on/local/computer/backup.sql
    # Copy the backup file to the target node
    scp backup.sql [Username]@[Target Node Address]:[Storage Path]
    ````

2. Log in to the target node and perform the restore operation:

    ````shell
    # Copy the backup file from the node to the target Pod
    kubectl cp backup.sql [Target Pod Name]:[Storage Path] -n [Namespace]
    # Enter the target Pod
    kubectl exec -it [Target Pod Name] -n [Namespace] -- /bin/bash
    # Enter the target Pod and execute the data restore command
    shell> mysql -u [Username] -p [Database Name] < backup.sql
    ````

## Incremental Data Synchronization

With the consistent database structure between the master and slave, you can use MySQL's built-in replication function for continuous synchronization. The operations are as follows:

### Source

1. Go to the parameter configuration page of the middleware and determine the following configuration parameters:

    ````configuration
    server-id = <Instance Unique Identifier> # The ID of the source instance and target instance must be different
    log-bin = <Path and Name of Binary Log File>
    binlog-format = Mixed
    ````

    The `server-id` parameter is not provided on the parameter configuration page. The modification method is as follows:

    1. Go to the CR file of the instance: Container Management - Cluster Where the Instance Resides - Custom Resources - mysqlclusters.mysql.presslabs.org - Instance CR
    2. Add the field: spec.serverIDOffset: 200


2. Create a replication account

    Enter the mysql service console and execute the following creation command. This user is dedicated to data synchronization between clusters. For security reasons, it is recommended to create this user.

    ````mysql
    mysql> grant replication slave, replication client on *.* to 'rep'@'%' identified by '123456ab';
    ````

    Parameter explanation:

    - `grant`: Grant
    - `replication`: Grant replication permission
    - `*.*`: All databases and tables
    - `rep`: Authorized user
    - `%`: All machines can access
    - `by '123456ab'`: Password for this user


3. Service configuration

    Go to the "Container Management" module and configure a NodePort service for the instance to enable synchronization access to the target instance:


    - Service port and container port: 3306
    - Add label: role/master

### Target

1. Ensure that the server-id of the target end is different from that of the source end. If configuration is required, refer to the method for configuring the source end.

    ````mysql
    server-id = <Unique Identifier of the Target Cluster>
    ````

2. Configure the source end information in the MySQL command line on the target end:

    ````mysql
    mysql> CHANGE MASTER TO
             MASTER_HOST = '<Source Cluster's NodePort Service IP Address>',
             MASTER_PORT = <Source Cluster's NodePort Service Port Number>,
             MASTER_USER = '<Username>',
             MASTER_PASSWORD = '<Password>',
             MASTER_LOG_FILE = '<File Value of the Source Cluster>', # File value recorded in the source end operation
             MASTER_LOG_POS = <Position Value of the Source Cluster>, # Position value recorded in the source end operation
             MASTER_RETRY_COUNT = <Number of Connection Retry Attempts>;  # 0 means unlimited
    ````

    The File and Position fields can be viewed in the console of the source end. The command to view is as follows:

    ````mysql
    mysql> SHOW MASTER STATUS;
    ````

    Example:

    ````mysql
    mysql> CHANGE MASTER TO
             MASTER_HOST = '172.30.120.202',
             MASTER_PORT = 32470,
             MASTER_USER = 'rep',
             MASTER_PASSWORD = '123456ab',
             MASTER_LOG_FILE = 'mysql-bin.000003',
             MASTER_LOG_POS = 2595935,
             MASTER_RETRY_COUNT = 0;
    ````

3. Start the synchronization. After starting, the data synchronization between the two instances will be automatically performed continuously.

    ````mysql
    mysql> start slave;
    ````

4. Check the status, pay special attention to the following two items. If the status is `Yes`, it means that the replication function has started running.

    ````mysql
    mysql> SHOW SLAVE STATUS\G
    ````


    !!! note

        At this time, the target end is in the slave state and will be displayed as "Not Ready" in the middleware list. This is normal and will return to normal after the master-slave relationship is released.


## Target Provides Services

When the source end fails, the target end switches roles to provide services externally. To do this, you need to release the master-slave synchronization relationship first. The operations are as follows:

````mysql
# To release the master-slave relationship, you need to stop the slave node first
mysql> stop slave;
mysql> reset slave all;
# Restart the database service on the target end
mysql> service mysql restart
````

After restarting, the target instance will resume independent operation.

## Data Recovery

If data recovery is required, it can be achieved through the dump method. Please refer to the "Full Data Dump" section for details.
