---
MTPE: windsonsea
date: 2024-05-11
---

# Use External Middleware Services

This document describes how to use third-party middleware services, including MySQL, Redis, Elasticsearch, and S3Storage.

## Use External Database

### Prerequisites

- DCE product modules have a built-in MySQL database for data storage, but the installer also supports using external MySQL, Kingbase, and PostgreSQL databases.

- The example scripts provided below are for demonstration purposes only. In actual applications, you should modify them according to specific requirements, such as database name, username, and password, and you can split the statements to be executed on different DBMS.

### Steps for External MySQL

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
    apiVersion: provision.daocloud.io/v1alpha4
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

4. After completing the above configuration, you can proceed with [deploying DCE Enterprise](../start-install.md).

### Steps for External Kingbase Database

1. Prepare a Kingbase database with permissions to create databases, users, and grant access.

2. Connect to the Kingbase database and run the following SQL statements to create databases, users, and grant corresponding permissions:

    ```sql
    CREATE DATABASE ghippo;
    CREATE USER ghippo WITH encrypted password 'password';
    GRANT ALL PRIVILEGES ON DATABASE ghippo TO ghippo;
 
    CREATE DATABASE keycloak;
    CREATE USER keycloak WITH encrypted password 'password';
    GRANT ALL PRIVILEGES ON DATABASE keycloak TO keycloak;
 
    CREATE DATABASE audit;
    CREATE USER audit WITH encrypted password 'password';
    GRANT ALL PRIVILEGES ON DATABASE audit TO audit;
 
    CREATE DATABASE kpanda;
    CREATE USER kpanda WITH encrypted password 'password';
    GRANT ALL PRIVILEGES ON DATABASE kpanda TO kpanda;
 
    CREATE DATABASE skoala;
    CREATE USER skoala WITH encrypted password 'password';
    GRANT ALL PRIVILEGES ON DATABASE skoala TO skoala;
 
    CREATE DATABASE amamba;
    CREATE USER amamba WITH encrypted password 'password';
    GRANT ALL PRIVILEGES ON DATABASE amamba TO amamba;
 
    CREATE DATABASE insight;
    CREATE USER insight WITH encrypted password 'password';
    GRANT ALL PRIVILEGES ON DATABASE insight TO insight;
 
    CREATE DATABASE ipavo;
    CREATE USER ipavo WITH encrypted password 'password';
    GRANT ALL PRIVILEGES ON DATABASE ipavo TO ipavo;
 
    CREATE DATABASE kcollie;
    CREATE USER kcollie WITH encrypted password 'password';
    GRANT ALL PRIVILEGES ON DATABASE kcollie TO kcollie;
 
    CREATE DATABASE gmagpie;
    CREATE USER gmagpie WITH encrypted password 'password';
    GRANT ALL PRIVILEGES ON DATABASE gmagpie TO gmagpie;
 
    CREATE DATABASE dowl;
    CREATE USER dowl WITH encrypted password 'password';
    GRANT ALL PRIVILEGES ON DATABASE dowl TO dowl;
    ```

3. In the [clusterConfig.yaml](../cluster-config.md) file, configure the `externalMiddlewares.database` parameter.
   Assume the Kingbase database access address is 172.30.41.2:54321. Different database types have different
   `dataSourceName` configuration formats. For details, refer to
   <https://gorm.io/docs/connecting_to_the_database.html>

    ```yaml
    apiVersion: provision.daocloud.io/v1alpha4
    kind: ClusterConfig
    metadata:
      creationTimestamp: null
    spec:
      ..............
      externalMiddlewares:
        database:
          kpanda:
            - dbDriverName: "kingbase"
              # Please refer https://gorm.io/docs/connecting_to_the_database.html
              dataSourceName: "host=172.30.41.2 user=kpanda password=password dbname=kpanda port=54321"
              # readwrite(default) or readonly
              accessType: readwrite
              # The maximum number of open connections to the database.
              # maxOpenConnections: 100
              # The maximum number of connections in the idle connection pool.
              # maxIdleConnections: 10
              # The maximum amount of time a connection may be reused.
              #connectionMaxLifetimeSeconds: 3600
              # The maximum amount of time a connection may be idle.
              # connectionMaxIdleSeconds: 1800
          ghippoApiserver:
            - dbDriverName: "kingbase"
              dataSourceName: "host=172.30.41.2 user=ghippo password=password dbname=ghippo port=54321"
          ghippoKeycloak:
            - dbDriverName: "kingbase"
              dataSourceName: "host=172.30.41.2 user=keycloak password=password dbname=keycloak port=54321"
          ghippoAuditserver:
            - dbDriverName: "kingbase"
              dataSourceName: "host=172.30.41.2 user=audit password=password dbname=audit port=54321"
          skoala:
            - dbDriverName: "kingbase"
              dataSourceName: "host=172.30.41.2 user=skoala password=password dbname=skoala port=54321"
          amamba:
            - dbDriverName: "kingbase"
              dataSourceName: "host=172.30.41.2 user=amamba password=password dbname=amamba port=54321"
          insight:
            - dbDriverName: "kingbase"
              dataSourceName: "host=172.30.41.2 user=insight password=password dbname=insight port=54321"
          ipavo:
            - dbDriverName: "kingbase"
              dataSourceName: "host=172.30.41.2 user=ipavo password=password dbname=ipavo port=54321"
          kcollie:
            - dbDriverName: "kingbase"
              dataSourceName: "host=172.30.41.2 user=kcollie password=password dbname=kcollie port=54321"
          gmagpie:
            - dbDriverName: "kingbase"
              dataSourceName: "host=172.30.41.2 user=gmagpie password=password dbname=gmagpie port=54321"
          dowl:
            - dbDriverName: "kingbase"
              dataSourceName: "host=172.30.41.2 user=dowl password=password dbname=dowl port=54321"
    ```

4. After completing the above configuration, you can proceed with [deploying DCE Enterprise](../start-install.md).

### Steps for External PostgreSQL Database

1. Prepare a PostgreSQL database with permissions to create databases, users, and grant access.

2. Connect to the PostgreSQL database and run the following SQL statements to create databases, users, and grant corresponding permissions:

   ```sql
   CREATE USER ghippo WITH encrypted password 'password';
   CREATE DATABASE ghippo OWNER ghippo;
   GRANT ALL PRIVILEGES ON DATABASE ghippo TO ghippo;
   
   CREATE USER keycloak WITH encrypted password 'password';
   CREATE DATABASE keycloak OWNER keycloak;
   GRANT ALL PRIVILEGES ON DATABASE keycloak TO keycloak;
   
   CREATE USER audit WITH encrypted password 'password';
   CREATE DATABASE audit OWNER audit;
   GRANT ALL PRIVILEGES ON DATABASE audit TO audit;
   
   CREATE USER kpanda WITH encrypted password 'password';
   CREATE DATABASE kpanda OWNER kpanda;
   GRANT ALL PRIVILEGES ON DATABASE kpanda TO kpanda;
   
   CREATE USER skoala WITH encrypted password 'password';
   CREATE DATABASE skoala OWNER skoala;
   GRANT ALL PRIVILEGES ON DATABASE skoala TO skoala;
   
   CREATE USER amamba WITH encrypted password 'password';
   CREATE DATABASE amamba OWNER amamba;
   GRANT ALL PRIVILEGES ON DATABASE amamba TO amamba;
   
   CREATE USER insight WITH encrypted password 'password';
   CREATE DATABASE insight OWNER insight;
   GRANT ALL PRIVILEGES ON DATABASE insight TO insight;
   
   CREATE USER ipavo WITH encrypted password 'password';
   CREATE DATABASE ipavo OWNER ipavo;
   GRANT ALL PRIVILEGES ON DATABASE ipavo TO ipavo;
   
   CREATE USER kcollie WITH encrypted password 'password';
   CREATE DATABASE kcollie OWNER kcollie;
   GRANT ALL PRIVILEGES ON DATABASE kcollie TO kcollie;
   
   CREATE USER gmagpie WITH encrypted password 'password';
   CREATE DATABASE gmagpie OWNER gmagpie;
   GRANT ALL PRIVILEGES ON DATABASE gmagpie TO gmagpie;
   
   CREATE USER dowl WITH encrypted password 'password';
   CREATE DATABASE dowl OWNER dowl;
   GRANT ALL PRIVILEGES ON DATABASE dowl TO dowl;
   ```

3. Modify the database configuration in clusterConfig.yaml. Assume the database access address is 172.30.41.2:5432. Different database types have different `dataSourceName` configuration formats. For details, refer to <https://gorm.io/docs/connecting_to_the_database.html>

    ```yaml
    apiVersion: provision.daocloud.io/v1alpha4
    kind: ClusterConfig
    metadata:
      creationTimestamp: null
    spec:
      ..............
      externalMiddlewares:
        database:
          kpanda:
            - dbDriverName: "postgres"
              # Please refer https://gorm.io/docs/connecting_to_the_database.html
              dataSourceName: "host=172.30.41.2 user=kpanda password=password dbname=kpanda port=5432"
              # readwrite(default) or readonly
              accessType: readwrite
              # The maximum number of open connections to the database.
              # maxOpenConnections: 100
              # The maximum number of connections in the idle connection pool.
              # maxIdleConnections: 10
              # The maximum amount of time a connection may be reused.
              # connectionMaxLifetimeSeconds: 3600
              # The maximum amount of time a connection may be idle.
              # connectionMaxIdleSeconds: 1800
          ghippoApiserver:
            - dbDriverName: "postgres"
              dataSourceName: "host=172.30.41.2 user=ghippo password=password dbname=ghippo port=5432"
          ghippoKeycloak:
            - dbDriverName: "postgres"
              dataSourceName: "host=172.30.41.2 user=keycloak password=password dbname=keycloak port=5432"
          ghippoAuditserver:
            - dbDriverName: "postgres"
              dataSourceName: "host=172.30.41.2 user=audit password=password dbname=audit port=5432"
          skoala:
            - dbDriverName: "postgres"
              dataSourceName: "host=172.30.41.2 user=skoala password=password dbname=skoala port=5432"
          amamba:
            - dbDriverName: "postgres"
              dataSourceName: "host=172.30.41.2 user=amamba password=password dbname=amamba port=5432"
          insight:
            - dbDriverName: "postgres"
              dataSourceName: "host=172.30.41.2 user=insight password=password dbname=insight port=5432"
          ipavo:
            - dbDriverName: "postgres"
              dataSourceName: "host=172.30.41.2 user=ipavo password=password dbname=ipavo port=5432"
          kcollie:
            - dbDriverName: "postgres"
              dataSourceName: "host=172.30.41.2 user=kcollie password=password dbname=kcollie port=5432"
          gmagpie:
            - dbDriverName: "postgres"
              dataSourceName: "host=172.30.41.2 user=gmagpie password=password dbname=gmagpie port=5432"
          dowl:
            - dbDriverName: "postgres"
              dataSourceName: "host=172.30.41.2 user=dowl password=password dbname=dowl port=5432"
    ```

4. After completing the above configuration, you can proceed with [deploying DCE Enterprise](../start-install.md).

## Use External Redis

The steps to configure external Redis are as follows:

1. In the [clusterConfig.yaml](../cluster-config.md), configure the `externalMiddlewares.redis` parameter:

    ```yaml
    apiVersion: provision.daocloud.io/v1alpha4
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

2. After completing the above configuration, you can proceed with [deploying DCE Enterprise](../start-install.md).

## Use External Elasticsearch

!!! note

    When using an external Elasticsearch, please be aware that if the external Elasticsearch does not
    have TLS enabled, you must set TLS to `off` in the `logging:output` Helm parameter of Insight.

The steps to configure external Elasticsearch are as follows:

1. In the [clusterConfig.yaml](../cluster-config.md), configure the `externalMiddlewares.elasticsearch` parameter:

    ```yaml
    apiVersion: provision.daocloud.io/v1alpha4
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

2. After completing the above configuration, you can proceed with [deploying DCE Enterprise](../start-install.md).

## Use External S3Storage

The steps to configure external S3Storage are as follows:

1. In the [clusterConfig.yaml](../cluster-config.md), configure the `externalMiddlewares.S3Storage` parameter:

    ```yaml
    apiVersion: provision.daocloud.io/v1alpha4
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

2. After completing the above configuration, you can proceed with [deploying DCE Enterprise](../start-install.md).

## Use External Kafka

Follow the steps below:

1. In the [clusterConfig.yaml](../cluster-config.md), configure the `externalMiddlewares.kafka` parameter:

    ```yaml
    apiVersion: provision.daocloud.io/v1alpha4
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

2. After completing the above configuration, you can proceed with [deploying DCE Business Edition](../start-install.md).
