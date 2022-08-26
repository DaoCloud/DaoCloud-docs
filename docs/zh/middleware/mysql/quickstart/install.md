# 安装 MySQL

按照以下步骤安装 MySQL。

## 添加源

```shell
helm repo add mcamel-release https://release.daocloud.io/chartrepo/mcamel
```

## 更新源

```shell
helm repo update
```

## 安装 MySQL Cluster Operator

```shell
helm upgrade --install MySQL-cluster-operator --create-namespace -n mcamel-system --cleanup-on-fail mcamel-release/MySQL-cluster-operator --version 0.1.0-321531a
```

## 安装 MySQL集群

```shell
helm upgrade --install MySQL --create-namespace -n mcamel-system --cleanup-on-fail --set MySQL.persistence.storageClassName=local-path mcamel-relea
```

> 注意：
>
> 1. 需要指定持久化存储数据参数，否则安装会失败。
>
> 2. 安装 MySQL 集群前，先确保 MySQL Cluster Operator 已部署。
