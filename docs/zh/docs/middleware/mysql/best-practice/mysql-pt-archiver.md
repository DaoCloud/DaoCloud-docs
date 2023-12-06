# MySQL 归档方案

pt-archiver 是用来归档表的工具，可以做到低影响、高性能的归档工具，从表中删除旧数据，而不会对 OLTP 查询产生太大影响。
可以将数据插入到另一个表中，该表不需要在同一台服务器上。可以将其写入适合 LOAD DATA INFILE 的格式的文件中。
或者两者都不做，只做删除。在归档的时候也可以指定归档的列和行。

## 安装

默认部署 MySQL 时已经安装了 `pt-heartbeat` 工具，通过以下命令检查：

```shell
[root@mysql1012-mysql-2 /]# pt-archiver --version
pt-archiver 3.4.0
```

`pt-heartbeat` 至少需要指定 `--dest`、`--file`、`--purge` 其中的一个，有一些选项是互斥的。

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

## 归档方法

### 仅删除数据，不归档

```shell
pt-archiver \
--source h=172.30.47.0,u=root,p='ZoO1l1K%YbG!zlh',P=31898,D=test,t=myTableSimple \
--purge \
--where "1=1" \
--nosafe-auto-incremen
```

### 归档到文件

文件格式：通过 `--output-format` 指定，归档出来的文件有 header：使用 `--header` 选项。

- dump: MySQL dump format using tabs as field separator (default)
- csv: Dump rows using ‘,’ as separator and optionally enclosing fields by ‘”’.
  This format is equivalent to FIELDS TERMINATED BY ‘,’ OPTIONALLY ENCLOSED BY ‘”’.

恢复：可以采用 LOAD DATA local INFILE 语法

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
 
# 使用--header选项，这里要保证--file指定的文件不存在才会添加header
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
 
# 恢复
mysql -uroot -p'ZoO1l1K%YbG!zlh' -h172.30.47.0 -P31898 --local-infile=1
LOAD DATA local INFILE '/var/log/one_column_csv.txt' INTO TABLE one_column;
```

### 不做任何操作，只打印要执行的查询语句，--dry-run 选项

```shell
pt-archiver \
--source h=172.30.47.0,u=root,p='ZoO1l1K%YbG!zlh',P=31898,D=test,t=myTableSimple \
--purge \
--where "1=1" \
--dry-run
```

### 归档到别的表（这个表可以在另一个数据库实例）

```shell
pt-archiver \
--source h=172.30.47.0,u=root,p='ZoO1l1K%YbG!zlh',P=31898,D=test,t=myTableSimple \
--dest h=172.30.47.0,u=root,p='12345678@',P=31507 \
--where "1=1" \
--no-delete
```

### 指定要归档的列，--cloumns 参数

```shell
pt-archiver \
--source h=172.30.47.0,u=root,p='ZoO1l1K%YbG!zlh',P=31898,D=test,t=myTableSimple \
--dest h=172.30.47.0,u=root,p='12345678@',P=31507 \
--where "1=1" \
--no-delete \
--columns=name,email
```

### 有从库的归档，从库延迟大于 1s 就暂停归档：--check-slave-lag

```shell
# 在replica里执行
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

## 常见问题

1. 归档出来的新数据总是少一行，可参考[故障分析 | pt-archiver 归档丢失一条记录](https://opensource.actionsky.com/20220926-mysql/)

    ```mysql
    # 加上--dry-run 查看生成的语句，注意 WHERE (1=1) AND (`id` < '3')
    
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

    **解决办法一： --nosafe-auto-incremen**

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

    **解决办法二：--no-ascend 和在--source 的 DSN 里通过 i=specified_index 指定索引**

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

1. 没有主键，采用默认参数会归档失败

    - 默认会去找 `ascendable index`，如果没有就会失败。
    - 可以在 `–source` 的 DSN 指定其他索引：`i=specified_index`

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
    
    # 没有主键，没有在--source 里指定索引，失败
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


    **解决办法：在–source 的 DSN 里通过 i=other_index 指定其他索引**

    ```shell
    pt-archiver \
    --source h=172.30.47.0,u=root,p='ZoO1l1K%YbG!zlh',P=31898,D=test,t=myTableNoPrimaryKey,i=name_index \
    --dest h=172.30.47.0,u=root,p='12345678@',P=31507 \
    --where "1=1"
    ```

1. 批量插入失败

    - 当使用了--bulk-insert 的时候，出现失败的情况。

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

    - 查看 MySQL 相关变量

        ```mysql
        mysql> show variables like 'local_infile';
        +---------------+-------+
        | Variable_name | Value |
        +---------------+-------+
        | local_infile  | OFF   |
        +---------------+-------+
        1 row in set (0.04 sec)
        ```

    - 需要在 client 和 server 两边都设置 local_infile=on, set global local_infile=on; 还需要在--source 和--dest 里设置 L=1

        ```mysql
        # 需要在 source 和 dest 两边的 MySQL 都设置
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
