---
hide:
  - toc
---

# Data Service

DCE 5.0 selected and integrated some classic data services for actual use cases, to provide a unified and comprehensive management platform for users.

You can install/enable the following data services on demand:

- [Elasticsearch](elasticsearch/intro/index.md): a quite popular full-text search engine
- [Kafka](./kafka/intro/index.md): data pipeline commonly used for message transmission
- [MinIO](./minio/intro/index.md): a very popular lightweight object storage solution
- [MySQL](mysql/intro/index.md): one of the most popular open-source relational databases
- [RabbitMQ](rabbitmq/intro/index.md): a transmission pipeline commonly used for data transaction
- [Redis](./redis/intro/index.md): an in-memory database
- [PostgreSQL](./postgresql/intro/index.md): one of the most popular open-source relational databases

## Learning Journey

This journey is based on RabbitMQ, but it also applies to other data services.a

!!! info

    Click words in the flow chart below, you will be directed to the corresponding guide page.

```mermaid
graph TD
    
    B(Select Workspace) --> C{Deploy/Create Instance}
    C -.-> D [Update/Delete Instance]
    C -.->E [Instance Overview]
    C -.->F [Instance Monitoring]
    C -.->G[Data Migration]
    C -.->H[Uninstall RabbitMQ]
    
    click B "https://docs.daocloud.io/en/middleware/rabbitmq/user-guide/login/"
    click C "https://docs.daocloud.io/en/middleware/rabbitmq/user-guide/create/"
    click D "https://docs.daocloud.io/en/middleware/rabbitmq/user-guide/update/"
    click E "https://docs.daocloud.io/en/middleware/rabbitmq/user-guide/view/"
    click F "https://docs.daocloud.io/en/middleware/rabbitmq/user-guide/insight/"
    click G "https://docs.daocloud.io/en/middleware/rabbitmq/user-guide/migrate/"
    click H "https://docs.daocloud.io/en/middleware/rabbitmq/quickstart/install/#_1"
```

[Elasticsearch](elasticsearch/intro/index.md){ .md-button .md-button--primary }
[Kafka](./kafka/intro/index.md){ .md-button .md-button--primary }
[MinIO](./minio/intro/index.md){ .md-button .md-button--primary }
[MySQL](mysql/intro/index.md){ .md-button .md-button--primary }
[RabbitMQ](rabbitmq/intro/index.md){ .md-button .md-button--primary }
[Redis](./redis/intro/index.md){ .md-button .md-button--primary }
[PostgreSQL](./postgresql/intro/index.md){ .md-button .md-button--primary }
