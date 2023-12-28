---
hide:
  - toc
---

# First-time Use of Data Services

When using DCE 5.0 for the first time, [Elasticsearch Search Service](../elasticsearch/intro/index.md), [Kafka Message Queue](../kafka/intro/index.md), [MinIO Object Storage](../minio/intro/index.md), [MySQL Data](../mysql/intro/index.md), [RabbitMQ Messages](../rabbitmq/intro/index.md), [PostgreSQL Database](../postgresql/intro/index.md), [Redis Database](../redis/intro/index.md), [MongoDB Database](../mongodb/intro/index.md), [RocketMQ Message Queue](../rocketmq/intro/index.md), and other middleware, you need to select a workspace.

For a detailed introduction to workspaces, you can refer to [Workspace and Hierarchy](../../ghippo/user-guide/workspace/ws-folder.md).

The following describes how to select a workspace using MinIO as an example, and the same applies to other data service components.

## Prerequisites

1. Create a [workspace](../../ghippo/user-guide/workspace/workspace.md) in the DCE 5.0 platform
2. If you need to create a middleware instance directly, you also need to [create](../../kpanda/user-guide/clusters/create-cluster.md) or [integrate](../../kpanda/user-guide/clusters/integrate-cluster.md) a cluster in the DCE 5.0 container management module.

## Procedure

1. In the left navigation bar, select `Middleware` -> `MinIO Storage`.



2. In the pop-up window, select a workspace, and then click `Confirm`.


    !!! note

        If the pop-up window does not appear or you want to change workspaces, you can manually click the switch icon in the red box to select a new workspace.

3. For the first use, you can click [`Deploy Now`](../minio/user-guide/create.md) to create a MinIO instance.