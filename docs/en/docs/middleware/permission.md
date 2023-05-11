---
hide:
   - toc
---

# Data service (middleware) permission design description

The data service module is built on [workspace](../ghippo/user-guide/workspace/ws-permission.md). Each middleware module of the data service corresponds to the permission mapping of each module in the workspace as follows:

| | | | | | |
| ------------- | ---------------------- | ------------ -------- | --------------- | ---------------- | -------- -------- |
| Middleware Modules | Menu Objects | Actions | Workspace Admin | Workspace Editor | Workspace Viewer |
| MySQL | MySQL Instance List | View List | ✅ | ✅ | ✅ |
| | | Instance Name Search | ✅ | ✅ | ✅ |
| | | Create instance | ✅ | ✅ | ❌ |
| | | Update Instance Configuration | ✅ | ✅ | ❌ |
| | | Delete instance | ✅ | ❌ | ❌ |
| | MySQL Instance Details | Instance Overview | ✅ | ✅ | ✅ |
| | | Instance Monitoring | ✅ | ✅ | ✅ |
| | | View instance configuration parameters | ✅ | ✅ | ✅ |
| | | Modify instance configuration parameters | ✅ | ✅ | ❌ |
| | | View Instance Access Password | ✅ | ✅ | ❌ |
| | | View instance backup list | ✅ | ✅ | ✅ |
| | | Instance creation backup | ✅ | ✅ | ❌ |
| | | Instance modification automatic backup task | ✅ | ✅ | ❌ |
| | | Create new instance with backup | ✅ | ✅ | ❌ |
| | Backup configuration management | Backup configuration list | ✅ | ❌ | ❌ |
| | | Create Backup Configuration | ✅ | ❌ | ❌ |
| | | Modify backup configuration | ✅ | ❌ | ❌ |
| | | Delete backup configuration | ✅ | ❌ | ❌ |
| RabbitMQ | List of RabbitMQ Instances | View List | ✅ | ✅ | ✅ |
| | | Instance Name Search | ✅ | ✅ | ✅ |
| | | Create instance | ✅ | ✅ | ❌ |
| | | Update Instance Configuration | ✅ | ✅ | ❌ |
| | | Delete instance | ✅ | ❌ | ❌ |
| | RabbitMQ Instance Details | Instance Overview | ✅ | ✅ | ✅ |
| | | Instance Monitoring | ✅ | ✅ | ✅ |
| | | View instance configuration parameters | ✅ | ✅ | ✅ |
| | | Modify instance configuration parameters | ✅ | ✅ | ❌ |
| | | View Instance Access Password | ✅ | ✅ | ❌ |
| Elasticsearch | Elasticsearch Instance List | View List | ✅ | ✅ | ✅ |
| | | Instance Name Search | ✅ | ✅ | ✅ |
| | | Create instance | ✅ | ✅ | ❌ |
| | | Update Instance Configuration | ✅ | ✅ | ❌ |
| | | Delete instance | ✅ | ❌ | ❌ |
| | Elasticsearch Instance Details | Instance Overview | ✅ | ✅ | ✅ |
| | | Instance Monitoring | ✅ | ✅ | ✅ |
| | | View instance configuration parameters | ✅ | ✅ | ✅ |
| | | Modify instance configuration parameters | ✅ | ✅ | ❌ |
| | | View Instance Access Password | ✅ | ✅ | ❌ |
| Redis | List of Redis Instances | View List | ✅ | ✅ | ✅ |
| | | Instance Name Search | ✅ | ✅ | ✅ |
|| | Create instance | ✅ | ✅ | ❌ |
| | | Update Instance Configuration | ✅ | ✅ | ❌ |
| | | Delete instance | ✅ | ❌ | ❌ |
| | Redis Instance Details | Instance Overview | ✅ | ✅ | ✅ |
| | | Instance Monitoring | ✅ | ✅ | ✅ |
| | | View instance configuration parameters | ✅ | ✅ | ✅ |
| | | Modify instance configuration parameters | ✅ | ✅ | ❌ |
| | | View Instance Access Password | ✅ | ✅ | ❌ |
| Kafka | Kafka Instance List | View List | ✅ | ✅ | ✅ |
| | | Instance Name Search | ✅ | ✅ | ✅ |
| | | Create instance | ✅ | ✅ | ❌ |
| | | Update Instance Configuration | ✅ | ✅ | ❌ |
| | | Delete instance | ✅ | ❌ | ❌ |
| | Kafka Instance Details | Instance Overview | ✅ | ✅ | ✅ |
| | | Instance Monitoring | ✅ | ✅ | ✅ |
| | | View instance configuration parameters | ✅ | ✅ | ✅ |
| | | Modify instance configuration parameters | ✅ | ✅ | ❌ |
| | | View Instance Access Password | ✅ | ✅ | ❌ |
| MinIO | List of MinIO Instances | View List | ✅ | ✅ | ✅ |
| | | Instance Name Search | ✅ | ✅ | ✅ |
| | | Create instance | ✅ | ✅ | ❌ |
| | | Update Instance Configuration | ✅ | ✅ | ❌ |
| | | Delete instance | ✅ | ❌ | ❌ |
| | MinIO Instance Details | Instance Overview | ✅ | ✅ | ✅ |
| | | Instance Monitoring | ✅ | ✅ | ✅ |
| | | View instance configuration parameters | ✅ | ✅ | ✅ |
| | | Modify instance configuration parameters | ✅ | ✅ | ❌ |
| | | View Instance Access Password | ✅ | ✅ | ❌ |
| PostgreSQL | PostgreSQL Instance List | View List | ✅ | ✅ | ✅ |
| | | Instance Name Search | ✅ | ✅ | ✅ |
| | | Create instance | ✅ | ✅ | ❌ |
| | | Update Instance Configuration | ✅ | ✅ | ❌ |
| | | Delete instance | ✅ | ❌ | ❌ |
| | PostgreSQL Instance Details | Instance Overview | ✅ | ✅ | ✅ |
| | | Instance Monitoring | ✅ | ✅ | ✅ |
| | | View instance configuration parameters | ✅ | ✅ | ✅ |
| | | Modify instance configuration parameters | ✅ | ✅ | ❌ |
| | | View Instance Access Password | ✅ | ✅ | ❌ |
