# MySQL Archiving Solution

pt-archiver is a tool used to archive tables. It can achieve low-impact, high-performance archiving by deleting old data from the table without causing significant impact on OLTP queries. It can insert the data into another table, which does not need to be on the same server. It can also write the data to a file in a format suitable for LOAD DATA INFILE. Alternatively, it can simply delete the data. During archiving, you can also specify the columns and rows to archive.

## Installation

The `pt-heartbeat` tool is already installed by default when deploying MySQL. You can check it using the following command:

```shell
[root@mysql1012-mysql-2 /]# pt-archiver --version
pt-archiver 3.4.0
```

`pt-heartbeat` requires at least one of the `--dest`, `--file`, or `--purge` options to be specified, and some options are mutually exclusive.

```console
Specify at least one of --dest, --file, or --purge.
  --ignore and --replace are mutually exclusive.
  --txn-size and --commit-each are mutually exclusive.
  --low-priority-insert and --delayed-insert are mutually exclusive.
  --share-lock and --for-update are mutually exclusive.
  --analyze and --optimize are mutually exclusive.
  --no-ascend and --no-delete are mutually exclusive.
  DSN values in --dest default to values from --source if COPY is yes
```

## Archiving Methods

### Delete Data Without Archiving

```shell
pt-archiver \
--source h=172.30.47.0,u=root,p='ZoO1l1K%YbG!zlh',P=31898,D=test,t=myTableSimple \
--purge \
--where "1=1" \
--nosafe-auto-incremen
```

### Archive to File

File Format: Specify the file format using the `--output-format` option. If you want to include a header in the archived file, use the `--header` option.

- dump: MySQL dump format using tabs as field separator (default)
- csv: Dump rows using ‘,’ as separator and optionally enclosing fields by ‘”’.
  This format is equivalent to FIELDS TERMINATED BY ‘,’ OPTIONALLY ENCLOSED BY ‘”’.

Recovery: You can use the `LOAD DATA LOCAL INFILE` syntax to restore the archived data.

```shell
pt-archiver \
--source h=172.30.47.0,u=root,p='ZoO1l1K%YbG!zlh',P=31898,D=test,t=one_column \
--file=/var/log/one_column.txt \
--progress 5000 \
--where "1=1" \
--no-delete \
--statistics --limit=10000 --txn-size 1000 --nosafe-auto-incremen
 
cat /var/log/one_column.txt
1   zhangsan
 
pt-archiver \
--source h=172.30.47.0,u=root,p='ZoO1l1K%YbG!zlh',P=31898,D=test,t=one_column \
--file=/var/log/one_column_csv.txt \
--output-format=csv \ --progress 5000 \
--where "1=1" \
--no-delete \
--statistics --limit=10000 --txn-size 1000 --nosafe-auto-incremen
 
cat /var/log/one_column_csv.txt
1, "zhangsan"
 
# Using the `--header` option, the header will only be added if the file specified by `--file` does not exist.
pt-archiver \
--source h=172.30.47.0,u=root,p='ZoO1l1K%YbG!zlh',P=31898,D=test,t=one_column \
--file=/var/log/one_column_csv.txt \
--output-format=csv \
--header \
--progress 5000 \
--where "1=1" \
--no-delete \
--statistics --limit=10000 --txn-size 1000 --nosafe-auto-incremen
 
cat /var/log/one_column_csv.txt
id  name
1   zhangsan
 
# Restore
mysql -uroot -p'ZoO1l1K%YbG!zlh' -h172.30.47.0 -P31898 --local-infile=1
LOAD DATA local INFILE '/var/log/one_column_csv.txt' INTO TABLE one_column;
```

### No Operation, Only Print the Executed Queries, using the `--dry-run` option

```shell
pt-archiver \
--source h=172.30.47.0,u=root,p='ZoO1l1K%YbG!zlh',P=31898,D=test,t=myTableSimple \
--purge \
--where "1=1" \
--dry-run
```

### Archive to Another Table (which can be in another database instance)

```shell
pt-archiver \
--source h=172.30.47.0,u=root,p='ZoO1l1K%YbG!zlh',P=31898,D=test,t=myTableSimple \
--dest h=172.30.47.0,u=root,p='12345678@',P=31507 \
--where "1=1" \
--no-delete
```

### Specify Columns to Archive, using the `--columns` parameter

```shell
pt-archiver \
--source h=172.30.47.0,u=root,p='ZoO1l1K%YbG!zlh',P=31898,D=test,t=myTableSimple \
--dest h=172.30.47.0,u=root,p='12345678@',P=31507 \
--where "1=1" \
--no-delete \
--columns=name,email
```

### Archiving with a Replica, Pause Archiving if Replica Lag is Greater than 1s: `--check-slave-lag`

```shell
# Run in replica
mysql>stop slave;
mysql>CHANGE MASTER TO MASTER_DELAY = 10;
mysql>start slave;
mysql>show slave status \G;

pt-archiver \
--source h=127.0.0.1,u=root,p='ZoO1l1K%YbG!zlh',P=3306,D=test,t=myTableSimple \
--dest h=172.30.47.0,u=root,p='12345678@',P=31507 \
--where="1=1" \
--max-lag=1 \
--check-slave-lag h=10.244.2.30,u=root,p='ZoO1l1K%YbG!zlh',P=3306,D=test \
--check-interval 1s \
--progress=1 \
--statistics
```

## FAQs

1. If the archived data is always missing one row, you can refer to
   [Troubleshooting | Missing One Record in pt-archiver Archive](https://opensource.actionsky.com/20220926-mysql/).

    ```mysql
    # Add --dry-run to view the generated query, pay attention to WHERE (1=1) AND (`id` < '3')
    ```
    
    pt-archiver \
    --source h=172.30.47.0,u=root,p='ZoO1l1K%YbG!zlh',P=31898,D=test,t=myTableSimple \
    --dest h=172.30.47.0,u=root,p='12345678@',P=31507 \
    --where "1=1" \
    --no-delete \
    --dry-run
    
    SELECT /*!40001 SQL_NO_CACHE */ `id`,`name`,`phone`,`email`,`address`,`list`,`country`,`region`,`postalzip`,`text`,`numberrange`,`currency`,`alphanumeric` FROM `test`.`myTableSimple` FORCE INDEX(`PRIMARY`) WHERE (1=1) AND (`id` < '3') ORDER BY `id` LIMIT 1
    SELECT /*!40001 SQL_NO_CACHE */ `id`,`name`,`phone`,`email`,`address`,`list`,`country`,`region`,`postalzip`,`text`,`numberrange`,`currency`,`alphanumeric` FROM `test`.`myTableSimple` FORCE INDEX(`PRIMARY`) WHERE (1=1) AND (`id` < '3') AND ((`id` > ?)) ORDER BY `id` LIMIT 1
    INSERT INTO `test`.`myTableSimple`(`id`,`name`,`phone`,`email`,`address`,`list`,`country`,`region`,`postalzip`,`text`,`numberrange`,`currency`,`alphanumeric`) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)
    
    
    SELECT MAX(id) from myTableSimple;
    +---------+
    | MAX(id) |
    +---------+
    |   3|
    +---------+
    ```

    **Solution 1: --nosafe-auto-incremen**

    ```shell
    pt-archiver \
    --source h=172.30.47.0,u=root,p='ZoO1l1K%YbG!zlh',P=31898,D=test,t=myTableSimple \
    --dest h=172.30.47.0,u=root,p='12345678@',P=31507 \
    --where "1=1" \
    --no-delete \
    --nosafe-auto-incremen \
    --dry-run
    
    SELECT /*!40001 SQL_NO_CACHE */ `id`,`name`,`phone`,`email`,`address`,`list`,`country`,`region`,`postalzip`,`text`,`numberrange`,`currency`,`alphanumeric` FROM `test`.`myTableSimple` FORCE INDEX(`PRIMARY`) WHERE (1=1) ORDER BY `id` LIMIT 1
    SELECT /*!40001 SQL_NO_CACHE */ `id`,`name`,`phone`,`email`,`address`,`list`,`country`,`region`,`postalzip`,`text`,`numberrange`,`currency`,`alphanumeric` FROM `test`.`myTableSimple` FORCE INDEX(`PRIMARY`) WHERE (1=1) AND ((`id` > ?)) ORDER BY `id` LIMIT 1
    INSERT INTO `test`.`myTableSimple`(`id`,`name`,`phone`,`email`,`address`,`list`,`country`,`region`,`postalzip`,`text`,`numberrange`,`currency`,`alphanumeric`) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)
    ```

    **Solution 2: Use `--no-ascend` and specify the index using `i=specified_index` in the `--source` DSN**

    ```shell
    pt-archiver \
    --source h=172.30.47.0,u=root,p='ZoO1l1K%YbG!zlh',P=31898,D=test,t=myTableSimple,i=name_index \
    --dest h=172.30.47.0,u=root,p='12345678@',P=31507 \
    --where "1=1" \
    --no-delete \
    --dry-run
    
    SELECT /*!40001 SQL_NO_CACHE */ `id`,`name`,`phone`,`email`,`address`,`list`,`country`,`region`,`postalzip`,`text`,`numberrange`,`currency`,`alphanumeric` FROM `test`.`myTableSimple` FORCE INDEX(`name_index`) WHERE (1=1) ORDER BY `name` LIMIT 1
    SELECT /*!40001 SQL_NO_CACHE */ `id`,`name`,`phone`,`email`,`address`,`list`,`country`,`region`,`postalzip`,`text`,`numberrange`,`currency`,`alphanumeric` FROM `test`.`myTableSimple` FORCE INDEX(`name_index`) WHERE (1=1) AND (((? IS NULL AND `name` IS NOT NULL) OR (`name` > ?))) ORDER BY `name` LIMIT 1
    INSERT INTO `test`.`myTableSimple`(`id`,`name`,`phone`,`email`,`address`,`list`,`country`,`region`,`postalzip`,`text`,`numberrange`,`currency`,`alphanumeric`) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)
    ```

1. If there is no primary key defined on the table, the default parameters may cause the archiving process to fail.

    - By default, `pt-archiver` looks for an "ascendable index". If no such index is found, the archiving process fails.
    - To resolve this issue, you can specify an alternative index in the `--source` DSN by adding `i=specified_index`. This allows `pt-archiver` to use the specified index for archiving, even if there is no primary key defined on the table.

    ```shell
    show create table myTableNoPrimaryKey\G
    *************************** 1. row ***************************
          Table: myTableNoPrimaryKey
    Create Table: CREATE TABLE `myTableNoPrimaryKey` (
      `id` mediumint NOT NULL,
      `name` varchar(255) DEFAULT NULL,
      `phone` varchar(100) DEFAULT NULL,
      `email` varchar(255) DEFAULT NULL,
      `address` varchar(255) DEFAULT NULL,
      `list` varchar(255) DEFAULT NULL,
      `country` varchar(100) DEFAULT NULL,
      `region` varchar(50) DEFAULT NULL,
      `postalZip` varchar(10) DEFAULT NULL,
      `text` text,
      `numberrange` mediumint DEFAULT NULL,
      `currency` varchar(100) DEFAULT NULL,
      `alphanumeric` varchar(255) DEFAULT NULL,
      KEY `name_index` (`name`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci
    1 row in set (0.03 sec)
    
    # No primary key specified, no index specified in --source, failed.
    pt-archiver \
    --source h=172.30.47.0,u=root,p='ZoO1l1K%YbG!zlh',P=31898,D=test,t=myTableNoPrimaryKey \
    --dest h=172.30.47.0,u=root,p='12345678@',P=31507 \
    --where "1=1"
    Cannot find an ascendable index in table at /usr/bin/pt-archiver line 3261.
    解决办法：在–source 的 DSN 里通过 i=other_index 指定其他索引

    pt-archiver \
    --source h=172.30.47.0,u=root,p='ZoO1l1K%YbG!zlh',P=31898,D=test,t=myTableNoPrimaryKey,i=name_index \
    --dest h=172.30.47.0,u=root,p='12345678@',P=31507 \
    --where "1=1"
    ```

    **Solution: Specify another index in the `--source` DSN using `i=other_index`**

    ```shell
    pt-archiver \
    --source h=172.30.47.0,u=root,p='ZoO1l1K%YbG!zlh',P=31898,D=test,t=myTableNoPrimaryKey,i=name_index \
    --dest h=172.30.47.0,u=root,p='12345678@',P=31507 \
    --where "1=1"
    ```

1. Bulk insert failure

   - When using the `--bulk-insert` option, failures may occur during bulk insertion.

        ```mysql
        pt-archiver \
        --source h=172.30.47.0,u=root,p='ZoO1l1K%YbG!zlh',P=31898,D=test,t=myTableSimple \
        --dest h=172.30.47.0,u=root,p='12345678@',P=31507,D=test,t=myTableSimple \
        --where "1=1" \
        --bulk-insert \
        --limit=1000 --no-delete --progress 10 --statistics
        TIME                ELAPSED   COUNT
        2023-10-16T10:37:32       0       0
        DBD::mysql::st execute failed: Loading local data is disabled; this must be enabled on both the client and server sides [for Statement "LOAD DATA LOCAL INFILE ? INTO TABLE `test`.`myTableSimple`(`id`,`name`,`phone`,`email`,`address`,`list`,`country`,`region`,`postalzip`,`text`,`numberrange`,`currency`,`alphanumeric`)" with ParamValues: 0='/tmp/GPJHnHSRUspt-archiver'] at /usr/bin/pt-archiver line 6876.
        ```

    - Check relevant variables of MySQL

        ```mysql
        mysql> show variables like 'local_infile';
        +---------------+-------+
        | Variable_name | Value |
        +---------------+-------+
        | local_infile  | OFF   |
        +---------------+-------+
        1 row in set (0.04 sec)
        ```

    - Ensure that the `local_infile` option is enabled on both the client and server sides. You can do this by setting `local_infile=on` in both the source and destination MySQL instances.

        ```mysql
        # Set local_infile=on on both the source and destination MySQL instances
        mysql> set global local_infile=on;
        Query OK, 0 rows affected (0.04 sec)
        
        
        pt-archiver \
        --source h=172.30.47.0,u=root,p='ZoO1l1K%YbG!zlh',P=31898,D=test,t=myTableSimple,L=1 \
        --dest h=172.30.47.0,u=root,p='12345678@',P=31507,D=test,t=myTableSimple \
        --where "1=1" \
        --bulk-insert \
        --limit=1000 --no-delete --progress 10 --statistics
        
        TIME                ELAPSED   COUNT
        2023-10-16T10:46:28       0       0
        2023-10-16T10:46:28       0       2
        Started at 2023-10-16T10:46:28, ended at 2023-10-16T10:46:29
        Source: D=test,L=1,P=31898,h=172.30.47.0,p=...,t=myTableSimple,u=root
        Dest:   D=test,L=1,P=31507,h=172.30.47.0,p=...,t=myTableSimple,u=root
        SELECT 2
        INSERT 2
        DELETE 0
        Action              Count       Time        Pct
        commit                  6     0.2151      45.16
        bulk_inserting          1     0.1418      29.77
        select                  2     0.0763      16.02
        print_bulkfile          2     0.0000       0.00
        other                   0     0.0431       9.04
        ```
