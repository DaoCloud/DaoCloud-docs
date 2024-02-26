# Custom Role Permissions for Middlewares

The Middlewares module allows users to customize role permissions. Users can create [custom roles](../../ghippo/user-guide/access-control/custom-role.md) in the __Global Management__ section and specify the permissions for each middleware.

When creating a custom role, you can assign one of three types of permissions: Create/Edit, View, and Delete.

!!! note

    Some permission options are automatically associated with related dependent permissions. For example, if you select the __Delete__ permission, the __View__ permission will be automatically selected as well. Please do not deselect dependent permissions to avoid issues with the intended functionality of the target permission.

The specific operations that these three permissions can perform within the Middlewares module are as follows:

| Data Middleware Service | Operation Object | Operation | Create/Edit | View | Delete |
| ------------- | ------------------ | ---------- | ----- | -- | -- |
| Configuration Management | Configuration List | View List | ✅ | ✅ | ✅ |
| | | Configuration Name Search | ✅ | ✅ | ✅ |
| | | Create Configuration | ✅ | ❌ | ❌ |
| | | Update Configuration | ✅ | ❌ | ❌ |
| | | Delete Configuration | ❌ | ❌ | ✅ |
| MySQL | MySQL Instance List | View List | ✅ | ✅ | ✅ |
| | | Instance Name Search | ✅ | ✅ | ✅ |
| | | Create Instance | ✅ | ❌ | ❌ |
| | | Update Instance Configuration | ✅ | ❌ | ❌ |
| | | Delete Instance | ❌ | ❌ | ✅ |
| | MySQL Instance Details | Instance Overview | ✅ | ✅ | ❌ |
| | | Instance Monitoring | ✅ | ✅ | ❌ |
| | | View Instance Configuration Parameters | ✅ | ✅ | ❌ |
| | | Modify Instance Configuration Parameters | ✅ | ❌ | ❌ |
| | | View Instance Access Password | ✅ | ✅ | ❌ |
| | | View Instance Backup List | ✅ | ✅ | ❌ |
| | | Create Instance Backup | ✅ | ❌ | ❌ |
| | | Modify Instance Automatic Backup Task | ✅ | ❌ | ❌ |
| | | Create New Instance from Backup | ✅ | ✅ | ❌ |
| | Backup Configuration Management | Backup Configuration List | ✅ | ✅ | ✅ |
| | | Create Backup Configuration | ✅ | ❌ | ❌ |
| | | Modify Backup Configuration | ✅ | ❌ | ❌ |
| | | Delete Backup Configuration | ❌ | ❌ | ✅ |
| | Configuration Parameters | View Configuration Parameters | ✅ | ✅ | ❌ |
| | | Modify Configuration Parameters | ✅ | ❌ | ❌ |
| RabbitMQ | RabbitMQ Instance List | View List | ✅ | ✅ | ✅ |
| | | Instance Name Search | ✅ | ✅ | ✅ |
| | | Create Instance | ✅ | ❌ | ❌ |
| | | Update Instance Configuration | ✅ | ❌ | ❌ |
| | | Delete Instance | ❌ | ❌ | ✅ |
| | RabbitMQ Instance Details | Instance Overview | ✅ | ✅ | ❌ |
| | | Instance Monitoring | ✅ | ✅ | ❌ |
| | | View Instance Configuration Parameters | ✅ | ✅ | ❌ |
| | | Modify Instance Configuration Parameters | ✅ | ❌ | ❌ |
| | | View Instance Access Password | ✅ | ✅ | ❌ |
| Elasticsearch | Elasticsearch Instance List | View List | ✅ | ✅ | ✅ |
| | | Instance Name Search | ✅ | ✅ | ✅ |
| | | Create Instance | ✅ | ❌ | ❌ |
| | | Update Instance Configuration | ✅ | ❌ | ❌ |
| | | Delete Instance | ❌ | ❌ | ✅ |
| | Elasticsearch Instance Details | Instance Overview | ✅ | ✅ | ❌ |
| | | Instance Monitoring | ✅ | ✅ | ❌ |
| | | View Instance Configuration Parameters | ✅ | ✅ | ❌ |
| | | Modify Instance Configuration Parameters | ✅ | ❌ | ❌ |
| | | View Instance Access Password | ❌ | ✅ | ❌ |
| Redis | Redis Instance List | View List | ✅ | ✅ | ✅ |
| | | Instance Name Search | ✅ | ✅ | ✅ |
| | | Create Instance | ✅ | ❌ | ❌ |
| | | Update Instance Configuration | ✅ | ❌ | ❌ |
| | | Delete Instance | ❌ | ❌ | ✅ |
| | Redis Instance Details | Instance Overview | ✅ | ✅ | ❌ |
| | | Instance Monitoring | ✅ | ✅ | ❌ |
| | | View Instance Configuration Parameters | ✅ | ✅ | ❌ |
| | | Modify Instance Configuration Parameters | ✅ | ❌ | ❌ |
| | | View Instance Access Password | ✅ | ✅ | ❌ |
| | | Create Instance Backup | ✅ | ❌ | ❌ |
| | | Modify Instance Automatic Backup Task | ✅ | ❌ | ❌ |
| | | Create New Instance from Backup | ✅ | ✅ | ❌ |
| | Backup Configuration Management | Backup Configuration List | ✅ | ✅ | ✅ |
| | | Create Backup Configuration | ✅ | ❌ | ❌ |
| | | Modify Backup Configuration | ✅ | ❌ | ❌ |
| | | Delete Backup Configuration | ❌ | ❌ | ✅ |
| | Configuration Parameters | View Configuration Parameters | ✅ | ✅ | ❌ |
| | | Modify Configuration Parameters | ✅ | ❌ | ❌ |
| Kafka | Kafka Instance List | View List | ✅ | ✅ | ✅ |
| | | Instance Name Search | ✅ | ✅ | ✅ |
| | | Create Instance | ✅ | ❌ | ❌ |
| | | Update Instance Configuration | ✅ | ❌ | ❌ |
| | | Delete Instance | ❌ | ❌ | ✅ |
| | Kafka Instance Details | Instance Overview | ✅ | ✅ | ❌ |
| | | Instance Monitoring | ✅ | ✅ | ❌ |
| | | View Instance Configuration Parameters | ✅ | ✅ | ❌ |
| | | Modify Instance Configuration Parameters | ✅ | ❌ | ❌ |
| | | View Instance Access Password | ✅ | ✅ | ❌ |
| | Configuration Parameters | View Configuration Parameters | ✅ | ✅ | ❌ |
| | | Modify Configuration Parameters | ✅ | ❌ | ❌ |
| MinIO | MinIO Instance List | View List | ✅ | ✅ | ✅ |
| | | Instance Name Search | ✅ | ✅ | ✅ |
| | | Create Instance | ✅ | ❌ | ❌ |
| | | Update Instance Configuration | ✅ | ❌ | ❌ |
| | | Delete Instance | ❌ | ❌ | ✅ |
| | MinIO Instance Details | Instance Overview | ✅ | ✅ | ❌ |
| | | Instance Monitoring | ✅ | ✅ | ❌ |
| | | View Instance Configuration Parameters | ✅ | ✅ | ❌ |
| | | Modify Instance Configuration Parameters | ✅ | ❌ | ❌ |
| | | View Instance Access Password | ✅ | ✅ | ❌ |
| | Configuration Parameters | View Configuration Parameters | ✅ | ✅ | ❌ |
| | | Modify Configuration Parameters | ✅ | ❌ | ❌ |
| PostgreSQL | PostgreSQL Instance List | View List | ✅ | ✅ | ✅ |
| | | Instance Name Search | ✅ | ✅ | ✅ |
| | | Create Instance | ✅ | ❌ | ❌ |
| | | Update Instance Configuration | ✅ | ❌ | ❌ |
| | | Delete Instance | ❌ | ❌ | ✅ |
| | PostgreSQL Instance Details | Instance Overview | ✅ | ✅ | ❌ |
| | | Instance Monitoring | ✅ | ✅ | ❌ |
| | | View Instance Configuration Parameters | ✅ | ✅ | ❌ |
| | | Modify Instance Configuration Parameters | ✅ | ❌ | ❌ |
| | | View Instance Access Password | ✅ | ✅ | ❌ |
| | Configuration Parameters | View Configuration Parameters | ✅ | ✅ | ❌ |
| | | Modify Configuration Parameters | ✅ | ❌ | ❌ |
| MongoDB | MongoDB Instance List | View List | ✅ | ✅ | ✅ |
| | | Instance Name Search | ✅ | ✅ | ✅ |
| | | Create Instance | ✅ | ❌ | ❌ |
| | | Update Instance Configuration | ✅ | ❌ | ❌ |
| | | Delete Instance | ❌ | ❌ | ✅ |
| | MongoDB Instance Details | Instance Overview | ✅ | ✅ | ❌ |
| | | Instance Monitoring | ✅ | ✅ | ❌ |
| | | View Instance Configuration Parameters | ✅ | ✅ | ❌ |
| | | Modify Instance Configuration Parameters | ✅ | ❌ | ❌ |
| | | View Instance Access Password | ✅ | ✅ | ❌ |
| RocketMQ | RocketMQ Instance List | View List | ✅ | ✅ | ✅ |
| | | Instance Name Search | ✅ | ✅ | ✅ |
| | | Create Instance | ✅ | ❌ | ❌ |
| | | Update Instance Configuration | ✅ | ❌ | ❌ |
| | | Delete Instance | ❌ | ❌ | ✅ |
| | RocketMQ Instance Details | Instance Overview | ✅ | ✅ | ❌ |
| | | Instance Monitoring | ✅ | ✅ | ❌ |
| | | View Instance Configuration Parameters | ✅ | ✅ | ❌ |
| | | Modify Instance Configuration Parameters | ✅ | ❌ | ❌ |
| | | View Instance Access Password | ✅ | ✅ | ❌ |
