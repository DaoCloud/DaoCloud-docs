# Middleware data service permission description

[Middleware Data Service](../../middleware/index.md) includes selected middleware:
MySQL, Redis, MongoDB, PostgreSQL, Elasticsearch, Kafka, RabbitMQ, RocketMQ, MinIO.
Middleware Data Services supports three user roles:

- Workspace Admin
- Workspace Editor
- Workspace Viewer

Each role has different permissions, which are described below.

<!--
You have permission to use `&check;`, but you don't have permission to use `&cross;`
-->

## Middleware Data Service Permission Description

| Middleware Modules | Menu Objects | Actions | Workspace Admin | Workspace Editor | Workspace Viewer |
| ------------- | ---------------------- | ------------ -------- | --------------- | ---------------- | -------- -------- |
| MySQL | MySQL Instance List | View List | &check; | &check; | &check; |
| | | instance name search | &check; | &check; | &check; |
| | | Create instance | &check; | &check; | &cross; |
| | | Update Instance Configuration | &check; | &check; | &cross; |
| | | delete instance | &check; | &cross; | &cross; |
| | MySQL Instance Details | Instance Overview | &check; | &check; | &check; |
| | | Instance Monitoring | &check; | &check; | &check; |
| | | View Instance Configuration Parameters | &check; | &check; | &check; |
| | | Modify instance configuration parameters | &check; | &check; | &cross; |
| | | View Instance Access Password | &check; | &check; | &cross; |
| | | View instance backup list | &check; | &check; | &check; |
| | | instance creation backup | &check; | &check; | &cross; |
| | | Instance modification automatic backup task | &check; | &check; | &cross; |
| | | Create new instance with backup | &check; | &check; | &cross; |
| | Backup configuration management | Backup configuration list | &check; | &cross; | &cross; |
| | | Create Backup Configuration | &check; | &cross; | &cross; |
| | | Modify backup configuration | &check; | &cross; | &cross; |
| | | delete backup configuration | &check; | &cross; | &cross; |
| RabbitMQ | RabbitMQ Instance List | View List | &check; | &check; | &check; |
| | | instance name search | &check; | &check; | &check; |
| | | Create instance | &check; | &check; | &cross; |
| | | Update Instance Configuration | &check; | &check; | &cross; |
| | | delete instance | &check; | &cross; | &cross; |
| | RabbitMQ Instance Details | Instance Overview | &check; | &check; | &check; |
| | | Instance Monitoring | &check; | &check; | &check; |
| | | View Instance Configuration Parameters | &check; | &check; | &check; |
| | | Modify instance configuration parameters | &check; | &check; | &cross; |
| | | View Instance Access Password | &check; | &check; | &cross; |
| Elasticsearch | Elasticsearch Instance List | View List | &check; | &check; | &check; |
| | | instance name search | &check; | &check; | &check; |
| | | Create instance | &check; | &check; | &cross; |
| | | Update Instance Configuration | &check; | &check; | &cross; |
| | | delete instance | &check; | &cross; | &cross; |
| | Elasticsearch Instance Details | Instance Overview | &check; | &check; | &check; |
| | | Instance Monitoring | &check; | &check; | &check; |
| | | View Instance Configuration Parameters | &check; | &check; | &check; |
| | | Modify instance configuration parameters | &check; | &check; | &cross; |
| | | View Instance Access Password | &check; | &check; | &cross; |
| Redis | Redis Instance List | View List | &check; | &check; | &check; |
| | | instance name search | &check; | &check; | &check; |
| | | Create instance | &check; | &check; | &cross; |
| | | Update Instance Configuration | &check; | &check; | &cross; |
| | | delete instance | &check; | &cross; | &cross; |
| | Redis Instance Details | Instance Overview | &check; | &check; | &check; |
| | | Instance Monitoring | &check; | &check; | &check; |
| | | View Instance Configuration Parameters | &check; | &check; | &check; |
| | | Modify instance configuration parameters | &check; | &check; | &cross; |
| | | View Instance Access Password | &check; | &check; | &cross; |
| Kafka | Kafka instance list | View list | &check; | &check; | &check; |
| | | instance name search | &check; | &check; | &check; |
| | | Create instance | &check; | &check; | &cross; |
| | | Update Instance Configuration | &check; | &check; | &cross; |
| | | delete instance | &check; | &cross; | &cross; |
| | Kafka Instance Details | Instance Overview | &check; | &check; | &check; |
| | | Instance Monitoring | &check; | &check; | &check; |
| | | View Instance Configuration Parameters | &check; | &check; | &check; |
| | | Modify instance configuration parameters | &check; | &check; | &cross; |
| | | View Instance Access Password | &check; | &check; | &cross; |
| MinIO | MinIO Instance List | View List | &check; | &check; | &check; |
| | | instance name search | &check; | &check; | &check; |
| | | Create instance | &check; | &check; | &cross; |
| | | Update Instance Configuration | &check; | &check; | &cross; |
| | | delete instance | &check; | &cross; | &cross; |
| | MinIO Instance Details | Instance Overview | &check; | &check; | &check; |
| | | Instance Monitoring | &check; | &check; | &check; |
| | | View Instance Configuration Parameters | &check; | &check; | &check; |
| | | Modify instance configuration parameters | &check; | &check; | &cross; |
| | | View Instance Access Password | &check; | &check; | &cross; |