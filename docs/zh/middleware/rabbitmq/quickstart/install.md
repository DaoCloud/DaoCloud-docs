# 安装 RabbitMQ

按照以下步骤安装 RabbitMQ。

## 添加源

```shell
helm repo add mcamel-release https://release.daocloud.io/chartrepo/mcamel
```

## 更新源

```shell
helm repo update
```

## 安装 RabbitMQ Cluster Operator

```shell
helm upgrade --install rabbitmq-cluster-operator --create-namespace -n mcamel-system --cleanup-on-fail mcamel-release/rabbitmq-cluster-operator --version 0.1.0-321531a
```

## 安装 RabbitMQ集群

```shell
helm upgrade --install rabbitmq --create-namespace -n mcamel-system --cleanup-on-fail --set rabbitmq.persistence.storageClassName=local-path mcamel-relea
```

!!! note

    1. 需要指定持久化存储数据参数，否则安装会失败。

    2. 安装 RabbitMQ 集群前，先确保 RabbitMQ Cluster Operator 已部署。
