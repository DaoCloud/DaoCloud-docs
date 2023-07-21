# Custom Role Permissions for Data Services

The Data Services module allows users to customize role permissions. Users can create [custom roles](../../ghippo/user-guide/access-control/custom-role.md) in the `Global Management` section and specify the permissions for each middleware.

When creating a custom role, you can assign one of three types of permissions: Create/Edit, View, and Delete.

!!! note

    Some permission options are automatically associated with related dependent permissions. For example, if you select the `Delete` permission, the `View` permission will be automatically selected as well. Please do not deselect dependent permissions to avoid issues with the intended functionality of the target permission.

The specific operations that these three permissions can perform within the Data Services module are as follows:

| Data Service     | Object              | Operation         | Create/Edit | View | Delete |
| ---------------- | ------------------- | ----------------- | ----------- | ---- | ------ |
| Configuration Management | Configuration List | View List         | ✅           | ✅    | ✅      |
|                  |                     | Configuration Name Search | ✅ | ✅   | ✅      |
|                  |                     | Create Configuration | ✅           | ❌    | ❌      |
|                  |                     | Update Configuration | ✅           | ❌    | ❌      |
|                  |                     | Delete Configuration | ❌           | ❌    | ✅      |
| MySQL            | MySQL Instance List | View List         | ✅           | ✅    | ✅      |
|                  |                     | Instance Name Search | ✅           | ✅    | ✅      |
|                  |                     | Create Instance   | ✅           | ❌    | ❌      |
|                  |                     | Update Instance Configuration | ✅   | ❌    | ❌      |
|                  |                     | Delete Instance   | ❌           | ❌    | ✅      |
|                  | MySQL Instance Details | Instance Overview | ✅           | ✅    | ❌      |
|                  |                     | Instance Monitoring | ✅           | ✅    | ❌      |
|                  |                     | View Instance Configuration Parameters | ✅ | ✅   | ❌      |
|                  |                     | Modify Instance Configuration Parameters | ✅ | ❌   | ❌      |
|                  |                     | View Instance Access Password | ✅       | ✅    | ❌      |
|                  |                     | View Instance Backup List | ✅         | ✅    | ❌      |
|                  |                     | Create Instance Backup | ✅           | ❌    | ❌      |
|                  |                     | Modify Instance Auto Backup Task | ✅     | ❌    | ❌      |
|                  |                     | Create New Instance from Backup | ✅     | ✅    | ❌      |
|                  | Backup Configuration Management | Backup Configuration List | ✅       | ✅    | ✅      |
|                  |                     | Create Backup Configuration | ✅          | ❌    | ❌      |
|                  |                     | Modify Backup Configuration | ✅          | ❌    | ❌      |
|                  |                     | Delete Backup Configuration | ❌          | ❌    | ✅      |
|                  | Configuration Parameters | View Configuration Parameters | ✅       | ✅    | ❌      |
|                  |                     | Modify Configuration Parameters | ✅       | -    | ❌      |
| RabbitMQ         | RabbitMQ Instance List | View List        | ✅           | ✅    | ✅      |
|                  |                     | Instance Name Search | ✅           | ✅    | ✅      |
|                  |                     | Create Instance   | ✅           | ❌    | ❌      |
|                  |                     | Update Instance Configuration | ✅   | ❌    | ❌      |
|                  |                     | Delete Instance   | ❌           | ❌    | ✅      |
|                  | RabbitMQ Instance Details | Instance Overview | ✅       | ✅    | ❌      |
|                  |                     | Instance Monitoring | ✅           | ✅    | ❌      |
|                  |                     | View Instance Configuration Parameters | ✅ | ✅   | ❌      |
| Elasticsearch    | Elasticsearch Instance List | View List   | ✅       | ✅    | ✅      |
|                  |                     | Instance Name Search | ✅           | ✅    | ✅      |
|                  |                     | Create Instance   | ✅           | ❌    | ❌      |
|                  |                     | Update Instance Configuration | ✅   | ❌    | ❌      |
|                  |                     | Delete Instance   | ❌           | ❌    | ✅      |
|                  | Elasticsearch Instance Details | Instance Overview | ✅       | ✅    | ❌      |
|                  |                     | Instance Monitoring | ✅           | ✅    | ❌      |
|                  |                     | View Instance Configuration Parameters | ✅ | ✅   | ❌      |
|                  |                     | Modify Instance Configuration Parameters | ✅ | ❌   | ❌      |
|                  |                     | View Instance Access Token | ❌ | ✅   | ❌      |
| Service      | Object              | Operation                | Create/Edit | View | Delete |
| ------------ | ------------------- | ------------------------ | ----------- | ---- | ------ |
| Redis        | Redis Instance List | View List                | ✅           | ✅    | ✅      |
|              |                     | Instance Name Search     | ✅           | ✅    | ✅      |
|              |                     | Create Instance          | ✅           | ❌    | ❌      |
|              |                     | Update Instance Config   | ✅           | ❌    | ❌      |
|              |                     | Delete Instance          | ❌           | ❌    | ✅      |
|              | Redis Instance Details | Instance Overview       | ✅           | ✅    | ❌      |
|              |                     | Instance Monitoring      | ✅           | ✅    | ❌      |
|              |                     | View Instance Config     | ✅           | ✅    | ❌      |
|              |                     | Modify Instance Config   | ✅           | ❌    | ❌      |
|              |                     | View Instance Access PW  | ✅           | ✅    | ❌      |
|              |                     | Create Instance Backup   | ✅           | ❌    | ❌      |
|              |                     | Modify Auto Backup Task  | ✅           | ❌    | ❌      |
|              |                     | Create Instance from Backup | ✅        | ✅    | ❌      |
| Kafka        | Kafka Instance List | View List                | ✅           | ✅    | ✅      |
|              |                     | Instance Name Search     | ✅           | ✅    | ✅      |
|              |                     | Create Instance          | ✅           | ❌    | ❌      |
|              |                     | Update Instance Config   | ✅           | ❌    | ❌      |
|              |                     | Delete Instance          | ❌           | ❌    | ✅      |
|              | Kafka Instance Details | Instance Overview       | ✅           | ✅    | ❌      |
|              |                     | Instance Monitoring      | ✅           | ✅    | ❌      |
|              |                     | View Instance Config     | ✅           | ✅    | ❌      |
|              |                     | Modify Instance Config   | ✅           | ❌    | ❌      |
|              |                     | View Instance Access PW  | ✅           | ✅    | ❌      |
| MinIO        | MinIO Instance List | View List                | ✅           | ✅    | ✅      |
|              |                     | Instance Name Search     | ✅           | ✅    | ✅      |
|              |                     | Create Instance          | ✅           | ❌    | ❌      |
|              |                     | Update Instance Config   | ✅           | ❌    | ❌      |
|              |                     | Delete Instance          | ❌           | ❌    | ✅      |
|              | MinIO Instance Details | Instance Overview       | ✅           | ✅    | ❌      |
|              |                     | Instance Monitoring      | ✅           | ✅    | ❌      |
|              |                     | View Instance Config     | ✅           | ✅    | ❌      |
|              |                     | Modify Instance Config   | ✅           | ❌    | ❌      |
|              |                     | View Instance Access PW  | ✅           | ✅    | ❌      |
| PostgreSQL   | PostgreSQL Instance List | View List           | ✅           | ✅    | ✅      |
|              |                     | Instance Name Search     | ✅           | ✅    | ✅      |
|              |                     | Create Instance          | ✅           | ❌    | ❌      |
|              |                     | Update Instance Config   | ✅           | ❌    | ❌      |
|              |                     | Delete Instance          | ❌           | ❌    | ✅      |
|              | PostgreSQL Instance Details | Instance Overview    | ✅           | ✅    | ❌      |
|              |                     | Instance Monitoring      | ✅           | ✅    | ❌      |
|              |                     | View Instance Config     | ✅           | ✅    | ❌      |
|              |                     | Modify Instance Config   | ✅           | ❌    | ❌      |
|              |                     | View Instance Access PW  | ✅           | ✅    | ❌      |
|              |                     | View Config Parameters   | ✅           | ❌    | ❌      |
