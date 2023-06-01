# keycloak 无法启动

## 故障表现

MySQL 已就绪，无报错。在安装全局管理后 keycloak 无法启动（> 10 次）。

![img](https://docs.daocloud.io/daocloud-docs-images/docs/reference/images/restart01.png)

## 检查项

- 如果数据库是 MySQL，检查 keycloak database 编码是否是 UTF8。

- 检查从 keycloak 到数据库的网络，检查数据库资源是否充足，包括但不限于资源限制、存储空间、物理机资源。

## 解决步骤

![img](https://docs.daocloud.io/daocloud-docs-images/docs/reference/images/restart02.png)

1. 检查 MySQL 资源占用是否到达 limit 限制
2. 检查 MySQL 中 database keycloak table 的数量是不是 92
3. 删除 keycloak database 并创建，提示 `CREATE DATABASE IF NOT EXISTS keycloak CHARACTER SET utf8`
4. 重启 keycloak Pod 解决问题
