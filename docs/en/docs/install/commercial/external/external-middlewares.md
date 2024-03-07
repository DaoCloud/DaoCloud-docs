# Use External Middleware Services

This document describes how to use third-party middleware services, including MySQL, Redis, Elasticsearch, and S3Storage.

## Use External Database (MySQL)

### Prerequisites

- DCE 5.0 uses MySQL database to store data, so only external MySQL database is supported.

- The example scripts provided below are for demonstration purposes only. In actual applications, you should modify them according to specific requirements, such as database name, username, password, etc., and you can split the statements to be executed on different DBMS.

### Steps

1. Prepare a MySQL database with permissions to create databases, users, and grant access.

2. Connect to the MySQL database and run the following SQL statements to create databases, users, and grant corresponding permissions:

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

3. In the [clusterConfig.yaml](../cluster-config.md), configure the
   `externalMiddlewares.database` parameter. Assuming the database access address is localhost:3306,
   different database types have different dataSourceName configuration formats.
   Refer to GORM documentation [Connecting to a Database](https://gorm.io/docs/connecting_to_the_database.html).

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

4. After completing the above configuration, you can proceed with [deploying DCE 5.0 Enterprise](../start-install.md).

## Use External Redis

The steps to configure external Redis are as follows:

1. In the [clusterConfig.yaml](../cluster-config.md), configure the `externalMiddlewares.redis` parameter:

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

        - Support for three modes: Redis Standalone, Redis Sentinel, and Redis Cluster.
        - Standalone URL format: `redis://[[user]:password@]host[:port][/db-number][?option=value]`
        - Sentinel URL format: `redis+sentinel://[[user]:password@]host1[:port1][,host2[:port2]]/master-name[/db-number][?option=value]`
        - Cluster URL format: `redis://[[user]:password@]host1[:port1]?addr=host2[:port2][&addr=host3:[port3][&option=value]]` or `rediss://[[user]:password@]host1[:port1]?addr=host2[:port2][&addr=host3:[port3][&option=value]]`
        - Currently, only the container management product module uses the Redis component.

2. After completing the above configuration, you can proceed with [deploying DCE 5.0 Enterprise](../start-install.md).

## Use External Elasticsearch

!!! note

    When using an external Elasticsearch, please be aware that if the external Elasticsearch does not
    have TLS enabled, you must set TLS to `off` in the `logging:output` Helm parameter of Insight.

The steps to configure external Elasticsearch are as follows:

1. In the [clusterConfig.yaml](../cluster-config.md), configure the `externalMiddlewares.elasticsearch` parameter:

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

        Currently, only the observability product module uses the Elasticsearch component.
        If an external middleware is used, it is not recommended to use worker nodes in 7-node mode,
        as it may consume too many resources.

2. After completing the above configuration, you can proceed with [deploying DCE 5.0 Enterprise](../start-install.md).

## Use External S3Storage

The steps to configure external S3Storage are as follows:

1. In the [clusterConfig.yaml](../cluster-config.md), configure the `externalMiddlewares.S3Storage` parameter:

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

2. After completing the above configuration, you can proceed with [deploying DCE 5.0 Enterprise](../start-install.md).

## Use External Kafka

Follow the steps below:

1. In the [clusterConfig.yaml](../cluster-config.md), configure the `externalMiddlewares.kafka` parameter:

    ```yaml
    apiVersion: provision.daocloud.io/v1alpha3
    kind: ClusterConfig
    metadata:
    spec:
      ..........
      externalMiddlewares:
        kafka:
          brokers:
            - host1:9092
            - host2:9092
          # the username and password of kafka is not necessary
          username: "username"
          password: "password"
      ..........
    ```

    !!! note

        Currently, only the observability module uses the Kafka component.

2. After completing the above configuration, you can proceed with [deploying DCE 5.0 Business Edition](../start-install.md).
