---
hide:
   - toc
---

# Permissions

Data services are designed to be deployed in a [workspace](../ghippo/user-guide/workspace/ws-permission.md).
Users with different workspace permissions can perform different actions in data services.

| Service | Object | Action | Workspace Admin | Workspace Editor | Workspace Viewer |
| ------- | ------ | ---------- | --------------- | ---------------- | ---------------- |
| Configuration | Configuration List | View List  | ✅ | ✅  | ✅  |
| | | Search by Name | ✅ | ✅  | ✅  |
| | | Create Configuration | ✅ | ✅  | ❌  |
| | | Update Configuration | ✅ | ✅  | ❌  |
| | | Delete Configuration | ✅ | ❌  | ❌  |
| MySQL | MySQL Instance List  | View List  | ✅ | ✅  | ✅  |
| | | Search by Name | ✅ | ✅  | ✅  |
| | | Create Instance | ✅ | ✅  | ❌  |
| | | Update Instance Configuration | ✅ | ✅  | ❌  |
| | | Delete Instance | ✅ | ❌  | ❌  |
| | MySQL Instance Details | Instance Overview | ✅ | ✅  | ✅  |
| | | Instance Monitoring | ✅ | ✅  | ✅  |
| | | View Instance Parameters | ✅ | ✅  | ✅  |
| | | Modify Instance Parameters | ✅ | ✅  | ❌  |
| | | View Instance Access Password | ✅ | ✅  | ❌  |
| | | View Instance Backup List | ✅ | ✅  | ✅  |
| | | Create Instance Backup | ✅ | ✅  | ❌  |
| | | Modify Instance Auto-Backup Task | ✅ | ✅  | ❌  |
| | | Create New Instance from Backup | ✅ | ✅  | ❌  |
| | Backup Configuration Management | Backup Configuration List | ✅ | ✅  | ✅  |
| | | Create Backup Configuration | ✅ | ✅  | ❌  |
| | | Modify Backup Configuration | ✅ | ✅  | ❌  |
| | | Delete Backup Configuration | ✅ | ❌  | ❌  |
| | Parameters | View Parameters | ✅ | ✅  | ✅  |
| | | Modify Parameters | ✅ | ✅  | ❌  |
| RabbitMQ | RabbitMQ Instance List | View List  | ✅ | ✅  | ✅  |
| | | Search by Name | ✅ | ✅  | ✅  |
| | | Create Instance | ✅ | ✅  | ❌  |
| | | Update Instance Configuration | ✅ | ✅  | ❌  |
| | | Delete Instance | ✅ | ❌  | ❌  |
| | RabbitMQ Instance Details | Instance Overview | ✅ | ✅  | ✅  |
| | | Instance Monitoring | ✅ | ✅  | ✅  |
| | | View Instance Parameters | ✅ | ✅  | ✅  |
| | | Modify Instance Parameters | ✅ | ✅  | ❌  |
| | | View Instance Access Password | ✅ | ✅  | ❌  |
| Elasticsearch | Elasticsearch Instance List | View List  | ✅ | ✅  | ✅  |
| | | Search by Name | ✅ | ✅  | ✅  |
| | | Create Instance | ✅ | ✅  | ❌  |
| | | Update Instance Configuration | ✅ | ✅  | ❌  |
| | | Delete Instance | ✅ | ❌  | ❌  |
| | Elasticsearch Instance Details | Instance Overview | ✅ | ✅  | ✅  |
| | | Instance Monitoring | ✅ | ✅  | ✅  |
| | | View Instance Parameters | ✅ | ✅  | ✅  |
| | | Modify Instance Parameters | ✅ | ✅  | ❌  |
| | | View Instance Access Password | ✅ | ✅  | ❌  |
| Redis | Redis Instance List | View List  | ✅ | ✅  | ✅  |
| | | Search by Name | ✅ | ✅  | ✅  |
| | | Create Instance | ✅ | ✅  | ❌  |
| | | Update Instance Configuration | ✅ | ✅  | ❌  |
| | | Delete Instance | ✅ | ❌  | ❌  |
| | Redis Instance Details | Instance Overview | ✅ | ✅  | ✅  |
| | | Instance Monitoring | ✅ | ✅  | ✅  |
| | | View Instance Parameters | ✅ | ✅  | ✅  |
| | | Modify Instance Parameters | ✅ | ✅  | ❌  |
| | | View Instance Access Password | ✅ | ✅  | ❌  |
| | Backup Configuration Management | Backup Configuration List | ✅ | ✅  | ✅  |
| | | Create Backup Configuration | ✅ | ✅  | ❌  |
| | | Modify Backup Configuration | ✅ | ✅  | ❌  |
| | | Delete Backup Configuration | ✅ | ❌  | ❌  |
| | Parameters | View Parameters | ✅ | ✅  | ✅  |
| | | Modify Parameters | ✅ | ✅  | ❌  |
| Kafka | Kafka Instance List | View List  | ✅ | ✅  | ✅  |
| | | Search by Name | ✅ | ✅  | ✅  |
| | | Create Instance | ✅ | ✅  | ❌  |
| | | Update Instance Configuration | ✅ | ✅  | ❌  |
| | | Delete Instance | ✅ | ❌  | ❌  |
| | Kafka Instance Details | Instance Overview | ✅ | ✅  | ✅  |
| | | Instance Monitoring | ✅ | ✅  | ✅  |
| | | View Instance Parameters | ✅ | ✅  | ✅  |
| | | Modify Instance Parameters | ✅ | ✅  | ❌  |
| | | View Instance Access Password | ✅ | ✅  | ❌  |
| | Parameters | View Parameters | ✅ | ✅  | ✅  |
| | | Modify Parameters | ✅ | ✅  | ❌  |
| MinIO | MinIO Instance List | View List  | ✅ | ✅  | ✅  |
| | | Search by Name | ✅ | ✅  | ✅  |
| | | Create Instance | ✅ | ✅  | ❌  |
| | | Update Instance Configuration | ✅ | ✅  | ❌  |
| | | Delete Instance | ✅ | ❌  | ❌  |
| | MinIO Instance Details | Instance Overview | ✅ | ✅  | ✅  |
| | | Instance Monitoring | ✅ | ✅  | ✅  |
| | | View Instance Parameters | ✅ | ✅  | ✅  |
| | | Modify Instance Parameters | ✅ | ✅  | ❌  |
| | | View Instance Access Password | ✅ | ✅  | ❌  |
| | Parameters | View Parameters | ✅ | ✅  | ✅  |
| | | Modify Parameters | ✅ | ✅  | ❌  |
| PostgreSQL  | PostgreSQL Instance List | View List  | ✅ | ✅  | ✅  |
| | | Search by Name | ✅ | ✅  | ✅  |
| | | Create Instance | ✅ | ✅  | ❌  |
| | | Update Instance Configuration | ✅ | ✅  | ❌  |
| | | Delete Instance | ✅ | ❌  | ❌  |
| | PostgreSQL Instance Details | Instance Overview | ✅ | ✅  | ✅  |
| | | Instance Monitoring | ✅ | ✅  | ✅  |
| | | View Instance Parameters | ✅ | ✅  | ✅  |
| | | Modify Instance Parameters | ✅ | ✅  | ❌  |
| | | View Instance Access Password | ✅ | ✅  | ❌  |
| | Parameters | View Parameters | ✅ | ✅  | ✅  |
| | | Modify Parameters | ✅ | ✅  | ❌  |
