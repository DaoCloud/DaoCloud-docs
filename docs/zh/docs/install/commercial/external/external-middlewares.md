# 使用外接中间件服务

本文描述如何使用第三方中间服务，包含：mysql、redis、elasticsearch、S3Storage。

## 使用外接数据库（MySQL）

### 前置说明

- DCE 5.0 产品模块中使用了 MySQL 数据库来存储数据，所以仅支持 MySQL 数据库外接

- 下述示例脚本仅用于演示目的，实际应用中应该根据具体的需求进行修改，例如数据库名称、用户名、密码等，
  并且可以将以下语句拆分至不同的 DBMS 执行

### 操作步骤

1. 准备一个 MySQL 数据库，并且具有创建数据库、创建用户、授予权限的权限。

2. 连接到 MySQL 数据库，执行如下 SQL，完成 database、用户的创建并授予对应权限。

    ```sql
    # ghippo apiserver
    CREATE DATABASE ghippo CHARACTER SET utf8 COLLATE utf8_general_ci;
    CREATE USER 'ghippo' IDENTIFIED BY 'password';
    GRANT ALL PRIVILEGES ON ghippo.* TO 'ghippo';
   
    # ghippo keycloak
    CREATE DATABASE keycloak CHARACTER SET utf8 COLLATE utf8_general_ci;
    CREATE USER 'keycloak' IDENTIFIED BY 'password';
    GRANT ALL PRIVILEGES ON keycloak.* TO 'keycloak';
   
    # ghippo audit
    CREATE DATABASE audit CHARACTER SET utf8 COLLATE utf8_general_ci;
    CREATE USER 'audit' IDENTIFIED BY 'password';
    GRANT ALL PRIVILEGES ON audit.* TO 'audit';
   
    # kpanda
    CREATE DATABASE kpanda CHARACTER SET utf8 COLLATE utf8_general_ci;
    CREATE USER 'kpanda' IDENTIFIED BY 'password';
    GRANT ALL PRIVILEGES ON kpanda.* TO 'kpanda';

    # set sort_buffer_size (used for clusterpedia)
    SET GLOBAL sort_buffer_size=8*1024*1024;
    SET SESSION sort_buffer_size=8*1024*1024;

    # skoala
    CREATE DATABASE skoala CHARACTER SET utf8 COLLATE utf8_general_ci;
    CREATE USER 'skoala' IDENTIFIED BY 'password';
    GRANT ALL PRIVILEGES ON skoala.* TO 'skoala';

    # amamba
    CREATE DATABASE amamba CHARACTER SET utf8 COLLATE utf8_general_ci;
    CREATE USER 'amamba' IDENTIFIED BY 'password';
    GRANT ALL PRIVILEGES ON amamba.* TO 'amamba';

    # insight
    CREATE DATABASE insight CHARACTER SET utf8 COLLATE utf8_general_ci;
    CREATE USER 'insight' IDENTIFIED BY 'password';
    GRANT ALL PRIVILEGES ON insight.* TO 'insight';

    # ipavo
    CREATE DATABASE ipavo CHARACTER SET utf8 COLLATE utf8_general_ci;
    CREATE USER 'ipavo' IDENTIFIED BY 'password';
    GRANT ALL PRIVILEGES ON ipavo.* TO 'ipavo';

    # kcollie
    CREATE DATABASE kcollie CHARACTER SET utf8 COLLATE utf8_general_ci;
    CREATE USER 'kcollie' IDENTIFIED BY 'password';
    GRANT ALL PRIVILEGES ON kcollie.* TO 'kcollie';

    # gmagpie
    CREATE DATABASE gmagpie CHARACTER SET utf8 COLLATE utf8_general_ci;
    CREATE USER 'gmagpie' IDENTIFIED BY 'password';
    GRANT ALL PRIVILEGES ON gmagpie.* TO 'gmagpie';

    # dowl
    CREATE DATABASE dowl CHARACTER SET utf8 COLLATE utf8_general_ci;
    CREATE USER 'dowl' IDENTIFIED BY 'password';
    GRANT ALL PRIVILEGES ON dowl.* TO 'dowl';
    ```

3. 在 [集群配置文件 clusterConfig.yaml](../cluster-config.md) 中，配置 `externalMiddlewares.database` 参数，
   假设数据库访问地址为 localhost:3306；不同的数据库类型有不同的 dataSourceName 配置格式，
   详见文档 https://gorm.io/docs/connecting_to_the_database.html

    ```yaml
    apiVersion: provision.daocloud.io/v1alpha3
    kind: ClusterConfig
    metadata:
      creationTimestamp: null
    spec:
      ..............
      externalMiddlewares:
        database:
          kpanda:
            - dbDriverName: "mysql"
              # Please refer https://gorm.io/docs/connecting_to_the_database.html
              dataSourceName: "kpanda:password@tcp(localhost:3306)/dbname"
              # readwrite(default) or readonly
              accessType: readwrite
              # The maximum number of open connections to the database.
              #maxOpenConnections: 100
              # The maximum number of connections in the idle connection pool.
              #maxIdleConnections: 10
              # The maximum amount of time a connection may be reused.
              #connectionMaxLifetimeSeconds: 3600
              # The maximum amount of time a connection may be idle.
              #connectionMaxIdleSeconds: 1800
          ghippoApiserver:
            - dbDriverName: "mysql"
              dataSourceName: "ghippo:password@tcp(localhost:3306)/ghippo"
          ghippoKeycloak:
            - dbDriverName: "mysql"
              dataSourceName: "keycloak:password@tcp(localhost:3306)/keycloak"
          ghippoAuditserver:
            - dbDriverName: "mysql"
              dataSourceName: "audit:password@tcp(localhost:3306)/audit"
          skoala:
            - dbDriverName: "mysql"
              dataSourceName: "skoala:password@tcp(172.30.41.0:3308)/skoala"
          amamba:
            - dbDriverName: "mysql"
              dataSourceName: "amamba:password@tcp(172.30.41.0:3308)/amamba"
          insight:
            - dbDriverName: "mysql"
              dataSourceName: "insight:password@tcp(172.30.41.0:3308)/insight"
          ipavo:
            - dbDriverName: "mysql"
              dataSourceName: "ipavo:password@tcp(172.30.41.0:3308)/ipavo"
          kcollie:
            - dbDriverName: "mysql"
              dataSourceName: "kcollie:password@tcp(172.30.41.0:3308)/kcollie"
          gmagpie:
            - dbDriverName: "mysql"
              dataSourceName: "gmagpie:password@tcp(172.30.41.0:3308)/gmagpie"
          dowl:
            - dbDriverName: "mysql"
              dataSourceName: "dowl:password@tcp(172.30.41.0:3308)/dowl"
    ```

4. 完成上述配置后，可以继续执行[部署 DCE 5.0 商业版](../start-install.md)。

## 使用外接 Redis

操作步骤如下：

1. 在 [集群配置文件 clusterConfig.yaml](../cluster-config.md) 中，配置 `externalMiddlewares.redis` 参数：

    ```yaml
    apiVersion: provision.daocloud.io/v1alpha3
    kind: ClusterConfig
    metadata:
    spec:
      ..........
      externalMiddlewares:
        redis:
          kpanda: "redis://:password@localhost:6379"
      ..........
    ```

    !!! note

        - 支持 Redis Standalone、Redis Sentinel、Redis Cluster 三种模式

        - Standalone URL 格式为：`redis://[[user]:password@]host[:port][/db-number][?option=value]`

        - Sentinel URL 格式为：`redis+sentinel://[[user]:password@]host1[:port1][,host2[:port2]]/master-name[/db-number][?option=value]`

        - Cluster URL 格式为：`redis://[[user]:password@]host1[:port1]?addr=host2[:port2][&addr=host3:[port3][&option=value]] 或 rediss://[[user]:password@]host1[:port1]?addr=host2[:port2][&addr=host3:[port3][&option=value]]`

        - 目前仅有容器管理产品模块使用到了 Redis 组件

2. 完成上述配置后，可以继续执行[部署 DCE 5.0 商业版](../start-install.md)。

## 使用外接 Elasticsearch

操作步骤如下：

1. 在 [集群配置文件 clusterConfig.yaml](../cluster-config.md) 中，配置 `externalMiddlewares.elasticsearch` 参数：

    ```yaml
    apiVersion: provision.daocloud.io/v1alpha3
    kind: ClusterConfig
    metadata:
    spec:
      ..........
      externalMiddlewares:
        elasticsearch:
          insight:
            endpoint: "https://xx.xx.xx.xx:9200"
            # basic auth
            username: "username"
            password: "password"
      ..........
    ```

    !!! note

        目前仅有可观测产品模块使用到了 Elasticsearch 组件。
        如果使用外接中间件后，不建议使用 7 节点模式下的 worker 节点，不然占用资源。

2. 完成上述配置后，可以继续执行[部署 DCE 5.0 商业版](../start-install.md)。

## 使用外接 S3Storage

操作步骤如下：

1. 在 [集群配置文件 clusterConfig.yaml](../cluster-config.md) 中，配置 `externalMiddlewares.S3Storage` 参数：

    ```yaml
    apiVersion: provision.daocloud.io/v1alpha3
    kind: ClusterConfig
    metadata:
    spec:
      ..........
      externalMiddlewares:
        S3Storage:
          default:
            endpoint: "https://xx.xx.xx.xx:9200"
            # Set if you dont want to verify the certificate.
            insecure: true
            bucket: "bucketname"
            accessKey: "YOUR-ACCESS-KEY-HERE"
            secretKey: "YOUR-SECRET-KEY-HERE"
      ..........
    ```

2. 完成上述配置后，可以继续执行[部署 DCE 5.0 商业版](../start-install.md)。
