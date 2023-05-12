---
hide:
  - toc
---

# Data service introduction

DCE 5.0 selects some classic data service middleware for actual application scenarios, and through front-end and back-end development, it can meet the development and maintenance of various application scenarios.

Users can install/enable the following data service middleware on demand, plug and play:

- [Elasticsearch Search Service](elasticsearch/intro/what.md): Currently the preferred full-text search engine
- [Kafka message queue](./kafka/intro/what.md): data pipeline commonly used for message transmission
- [MinIO Object Storage](./minio/intro/what.md): A very popular lightweight object storage solution
- [MySQL Database](mysql/intro/what.md): One of the most popular open source relational databases
- [RabbitMQ message queue](rabbitmq/intro/what.md): a transmission pipeline commonly used for transaction data
- [Redis Cache Service](./redis/intro/what.md): an in-memory database
- [PostgreSQL database](./postgresql/intro/what.md): One of the most popular open source relational databases

## Data service learning path

The learning paths of the above data service middleware are roughly the same. Here we take RabbitMQ as an example to briefly explain the learning paths.

!!! info

    Click the corresponding text in the flow chart below to jump directly to the corresponding operation guide page.

```mermaid
graph TD
    
    B(select workspace) --> C{deploy/create instance}
    C -.-> D [update/delete instance]
    C -.->E [instance overview]
    C -.->F [instance monitoring]
    C -.->G[data migration]
    C -.->H[uninstall middleware]
    
    click B "https://docs.daocloud.io/middleware/rabbitmq/user-guide/login/"
    click C "https://docs.daocloud.io/middleware/rabbitmq/user-guide/create/"
    click D "https://docs.daocloud.io/middleware/rabbitmq/user-guide/update/"
    click E "https://docs.daocloud.io/middleware/rabbitmq/user-guide/view/"
    click F "https://docs.daocloud.io/middleware/rabbitmq/user-guide/insight/"
    click G "https://docs.daocloud.io/middleware/rabbitmq/user-guide/migrate/"
    click H "https://docs.daocloud.io/middleware/rabbitmq/quickstart/install/#_1"
```

[Elasticsearch](elasticsearch/intro/what.md){ .md-button .md-button--primary }
[Kafka](./kafka/intro/what.md){ .md-button .md-button--primary }
[MinIO](./minio/intro/what.md){ .md-button .md-button--primary }
[MySQL](mysql/intro/what.md){ .md-button .md-button--primary }
[RabbitMQ](rabbitmq/intro/what.md){ .md-button .md-button--primary }
[Redis](./redis/intro/what.md){ .md-button .md-button--primary }
[PostgreSQL](./postgresql/intro/what.md){ .md-button .md-button--primary }