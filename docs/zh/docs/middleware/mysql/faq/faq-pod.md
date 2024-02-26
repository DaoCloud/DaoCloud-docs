# MySQL Pod

可以通过以下命令快速的查看当前集群上所有 __MySQL__ 实例的健康状态：

```bash
kubectl get mysql -A
```

输出类似于：

```bash
NAMESPACE       NAME                          READY   REPLICAS   AGE
ghippo-system   test                          True    1          3d
mcamel-system   mcamel-common-mysql-cluster   False   2          62d
```
针对不同的副本状态，排障方案如下文所述。

## Pod running = 0/4，状态为 __Init:Error__ 

遇到此类问题时，首先应该查看 __master__ 节点的（sidecar）日志信息。

```bash
kubectl get pod -n mcamel-system -Lhealthy,role | grep cluster-mysql | grep master | awk '{print $1}' | xargs -I {} kubectl logs -f {} -n mcamel-system -c sidecar
```

??? note "输出内容示例"

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
    E0209 05:38:56.223635       1 deleg.go:144] sidecar "msg"="failed waiting for xtrabackup to finish" "error"="exit status 1"
    ```

登录 __master__ 节点的 __MySQL__ ，执行 __alter__ 表结构：

```bash
[root@master-01 ~]$ kubectl get pod -n mcamel-system -Lhealthy,role | grep cluster-mysql | grep master
mcamel-common-mysql-cluster-mysql-0

#获取密码
[root@master-01 ~]$ kubectl get secret -n mcamel-system mcamel-common-mysql-cluster-secret -o=jsonpath='{.data.ROOT_PASSWORD}' | base64 -d

[root@master-01 ~]$ kubectl exec -it mcamel-common-mysql-cluster-mysql-0 -n mcamel-system -c mysql -- /bin/bash

# 注意：修改表结构需要root权限登录
~bash:mysql -uroot -p
```

??? note "SQL 语句如下"

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

## Pod running = 2/4

此类问题很可能是因为 MySQL 实例使用的磁盘用量达到了 100%，可以在 __master__ 节点上运行以下命令检测磁盘用量。

```bash
kubectl get pod -n mcamel-system | grep cluster-mysql | awk '{print $1}' | xargs -I {} kubectl exec {} -n mcamel-system -c sidecar -- df -h | grep /var/lib/mysql
```

输出类似于：

```console
/dev/drbd43001            50G   30G   21G  60% /var/lib/mysql
/dev/drbd43005            80G   29G   52G  36% /var/lib/mysql
```

如果发现某个  PVC 满了，则需要为 PVC 扩容。

```bash
kubectl edit pvc data-mcamel-common-mysql-cluster-mysql-0 -n mcamel-system # 修改request大小即可
```

## Pod running = 3/4

![image](https://docs.daocloud.io/daocloud-docs-images/docs/middleware/mysql/images/faq-mysql-1.png)

使用 __kubectl describe__ 上图中框起来的 Pod，发现异常提示： __Warning Unhealthy 4m50s (x7194 over 3h58m) kubelet Readiness probe failed: __ 

此时需要手工进行修复，这是目前开源 __mysql-operator__ 版本的 [Bug](https://github.com/bitpoke/mysql-operator/pull/857)

修复方式有两种：

- 重启 __mysql-operator__ ，或者
- 手工更新 __sys_operator__ 的配置状态

```bash
kubectl exec mcamel-common-mysql-cluster-mysql-1 -n mcamel-system -c mysql -- mysql --defaults-file=/etc/mysql/client.conf -NB -e 'update sys_operator.status set value="1"  WHERE name="configured"'
```
