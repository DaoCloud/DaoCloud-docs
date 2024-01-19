---
MTPE: FanLin
Date: 2024-01-19
---

# First Time Use of Middleware

When using DCE 5.0 for the first time, [Elasticsearch Search Service](../elasticsearch/intro/index.md), [Kafka Message Queue](../kafka/intro/index.md), [MinIO Object Storage](../minio/intro/index.md), [MySQL Data](../mysql/intro/index.md), [RabbitMQ Messages](../rabbitmq/intro/index.md), [PostgreSQL Database](../postgresql/intro/index.md), [Redis Database](../redis/intro/index.md), [MongoDB Database](../mongodb/intro/index.md), [RocketMQ Message Queue](../rocketmq/intro/index.md), and other middleware, you need to select a workspace.

For a detailed introduction to workspaces, you can refer to [Workspace and Folder](../../ghippo/user-guide/workspace/ws-folder.md).

The following describes how to select a workspace using MinIO as an example, and the same applies to other data service components.

## Prerequisites

1. Create a [workspace](../../ghippo/user-guide/workspace/workspace.md) in the DCE 5.0 platform
2. If you need to create a middleware instance directly, you also need to [create](../../kpanda/user-guide/clusters/create-cluster.md) or [integrate](../../kpanda/user-guide/clusters/integrate-cluster.md) a cluster in the DCE 5.0 container management module.

## Procedure

1. In the left navigation bar, select __Middleware__ -> __MinIO Object Storage__ .

    ![MinIO Object Storage](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/middleware/common/images/middleware01.png)

2. In the pop-up window, select a workspace, and then click __OK__ .

    ![Choose Workspace](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/middleware/common/images/middleware02.png)

    !!! note

        If the pop-up window does not appear or you want to change workspaces, you can manually click the switch icon in the red box to select a new workspace.

3. For the first use, you can click [__Create Now__](../minio/user-guide/create.md) to create a MinIO instance.

    ![Create Now](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/middleware/common/images/middleware03.png)
