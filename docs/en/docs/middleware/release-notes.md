# Middleware Release Notes

This page summarizes all middleware module release notes.

*[Elasticsearch]: A distributed full-text search and analytics engine, suitable for log search, monitoring, and complex query analysis.  
*[Kafka]: A high-throughput, distributed streaming platform for real-time data processing and log collection.  
*[MinIO]: A high-performance object storage system compatible with the S3 interface, ideal for storing unstructured data such as images, videos, and backups.  
*[MongoDB]: A document-oriented NoSQL database.  
*[MySQL]: A widely used relational database.  
*[PostgreSQL]: An open-source object-relational database with support for complex queries, transactions, and scalable data modeling.  
*[RabbitMQ]: A message broker supporting multiple protocols, ideal for building reliable asynchronous communication systems.  
*[Redis]: A high-performance key-value store, widely used for caching, session management, and distributed locks.  
*[RocketMQ]: A highly reliable and scalable distributed messaging middleware, suitable for transactional and ordered message scenarios.  

## 2025-11-30

### Elasticsearch v0.26.0

- **Added** support for displaying cluster resources bound to the workspace when creating an instance

### Kafka v0.27.0

- **Added** support for displaying cluster resources bound to the workspace when creating an instance

### MinIO v0.23.0

- **Added** support for displaying cluster resources bound to the workspace when creating an instance

### MongoDB v0.18.0

- **Added** support for displaying cluster resources bound to the workspace when creating an instance

### MySQL v0.28.0

- **Added** support for displaying cluster resources bound to the workspace when creating an instance
- **Added** alerts for failover events in primary–replica mode
- **Fixed** an issue where the `mysql_router` account was occasionally not created in MGR mode
- **Upgraded** phpMyAdmin to 5.2.3

### PostgreSQL v0.20.0

- **Added** support for displaying cluster resources bound to the workspace when creating an instance

### RabbitMQ v0.29.0

- **Added** support for displaying cluster resources bound to the workspace when creating an instance

### Redis v0.29.0

- **Added** support for displaying cluster resources bound to the workspace when creating an instance
- **Upgraded** the Opstree Operator to 0.22.2

### RocketMQ v0.17.0

- **Added** support for displaying cluster resources bound to the workspace when creating an instance
- **Added** affinity and toleration configurations for Controller and NameServer

## 2025-10-31

### Elasticsearch v0.25.2

- **Added** support for toleration configuration
- **Fixed** relok8s parsing issues
- **Fixed** incorrect ghippo upgrade logs
- **Upgraded** Elasticsearch and Kibana from 8.17.1 to 8.17.10
- **Upgraded** the operator to 2.16.1

### Kafka v0.26.0

- **Added** support for password configuration
- **Added** support for configuring complex listener access
- **Added** support for toleration configuration
- **Added** support for Kafka 4.0
- **Added** support for retrieving CPU, memory, storage capacity, and replica count from CRs
- **Added** support for configuring ghippo SDK cache expiration time in chart values
- **Fixed** dashboard display issues
- **Fixed** errors when creating Kafka configuration templates

### MinIO v0.22.0

- **Added** early detection for NodePort port conflicts
- **Added** support for node affinity configuration
- **Added** support for toleration configuration
- **Added** support for configuring ghippo SDK cache expiration time in chart values
- **Optimized** by removing the authentication information input field
- **Fixed** abnormal status display for single-instance deployments
- **Fixed** missing name validation when creating instances
- **Fixed** an issue where MinIO could not be restarted
- **Upgraded** the MinIO Operator to 6.0.4
- **Upgraded** the offline image validation script

### MongoDB v0.17.0

- **Added** support for toleration configuration
- **Added** support for configuring ghippo SDK cache expiration time in chart values
- **Fixed** an issue where audit logs were lost in certain scenarios
- **Fixed** potential permission leakage by adding the v1alpha2 API and including `workspace_id` in URLs
- **Fixed** an issue where restored instances used NodePort as the Express service type
- **Fixed** failures during MongoDB restore operations

### MySQL v0.27.1

- **Added** support for toleration configuration
- **Added** timeout configuration for the ghippo workspace SDK
- **Fixed** dashboard syntax issues
- **Fixed** errors when updating parameters while enabling automatic backups
- **Upgraded** MySQL from 5.7.31 to 5.7.44

### PostgreSQL v0.19.0

- **Added** support for toleration configuration
- **Upgraded** pgAdmin to 9.6.0
- **Upgraded** the exporter to v0.17.1
- **Upgraded** the operator to 0.14.0

### RabbitMQ v0.28.0

- **Added** enhanced default parameter templates
- **Added** support for page display of RabbitMQ installed via installer
- **Added** support for version 4.1.0
- **Fixed** removal of Istio injection labels from `matchLabels` in deployments
- **Fixed** an issue where configuration templates could not be created
- **Fixed** an issue where the NodePort management service type did not take effect
- **Upgraded** the RabbitMQ Operator to 4.4.1 to support RabbitMQ 4.0.5

### Redis v0.28.0

- **Added** support for toleration configuration
- **Fixed** audit log issues during ghippo upgrades
- **Upgraded** Redis to 7.2.9 and removed versions 7.2.6 and 7.2.7
- **Upgraded** RedisInsight to 2.70.0

### RocketMQ v0.16.0

- **Added** support for persistent storage of NameServer logs
- **Added** support for outputting Broker/Controller logs to the console
- **Added** support for RocketMQ 5.3.3
- **Added** support for toleration configuration
- **Added** support for configuring ghippo SDK cache expiration time in chart values
- **Fixed** an issue where using Operator version 0.15.0 could cause frequent Broker restarts
- **Fixed** an issue where page updates could overwrite map/slice fields in user-defined custom resources

## 2025-02-28

### Elasticsearch v0.24.0

- **Added** support for creating `Elasticsearch` instances with version v8.17.1.  

### Kafka v0.23.0

- **Improved** Kafka management tool by replacing `CMAK` with `kafka-ui`.  

### MySQL v0.26.0

- **Improved** upgraded `mysqld-exporter` image and added alerting rules for `MySQL-MGR`.  

### Redis v0.27.0

- **Added** support for creating `Redis` instances with version 7.2.7.  

### RocketMQ v0.14.0

- **Added** support for configuring static IPs for RocketMQ instances.  
- **Improved** support for setting timezone environment variables.  
- **Improved** upgraded operator image.  
- **Fixed** an issue where console connections failed after the name server restarted.  

## 2024-11-30

### Elasticsearch v0.23.0

- **Improved** disabled geoip database by default to avoid cluster health showing yellow.  

### Kafka v0.21.0

- **Improved** upgraded kafka-operator image to version 0.40.0 and added support for creating Kafka instances with version 3.7.0.  
- **Improved** added memory limits for kafka-operator.  

### Redis v0.24.0

- **Improved** support for deploying Redis instances with version 7.2.6.  
- **Improved** Redis Sentinel mode to support non-dynamic parameters.  
- **Fixed** an issue where Redis Sentinel mode could not start after restart.  

## 2024-09-30

### Elasticsearch v0.21.0

- **Added** support for choosing HTTPS/HTTP protocol when creating instances.  
- **Fixed** an issue where some operations lacked audit logs.  
- **Fixed** an issue where Elasticsearch instances created by the installer failed to be managed.  

### Kafka v0.19.0

- **Fixed** a permission leak when querying Kafka lists by workspace.  
- **Fixed** an issue where some operations lacked audit logs.  

### MinIO v0.19.0

- **Fixed** a permission leak when querying MinIO lists by workspace.  
- **Fixed** an issue where some operations lacked audit logs.  

### MongoDB v0.14.0

- **Improved** default service type for Express nodes in restored instances to NodePort.  
- **Fixed** a permission leak when querying MongoDB lists by workspace.  
- **Fixed** an issue where some operations lacked audit logs.  
- **Fixed** an issue where restoring MongoDB failed.  

### MySQL v0.22.0

- **Added** support for manual master-slave switch.  
- **Added** support for configuring Router nodes in MGR instances.  
- **Fixed** an issue where some operations lacked audit logs.  

### PostgreSQL v0.16.0

- **Fixed** a permission leak when querying PostgreSQL lists by workspace.  
- **Fixed** an issue where some operations lacked audit logs.  

### RabbitMQ v0.24.0

- **Fixed** an issue where some operations lacked audit logs.  
- **Fixed** an issue where monitoring data could not be queried after modifying the instance cluster name.  

### Redis v0.22.0

- **Fixed** a permission leak when querying Redis lists by workspace.  
- **Fixed** an issue where some operations lacked audit logs.  

### RocketMQ v0.11.0

- **Fixed** an issue where the pod list did not display all related pods in the instance.  
- **Fixed** a permission leak when querying Redis lists by workspace.  
- **Fixed** an issue where some operations lacked audit logs.  

## 2024-08-31

### MinIO v0.18.1

- **Improved** prevented abnormal clusters from being selected during instance creation.  
- **Fixed** a flaw in the multi-replica exit mechanism of `minio operator` by adjusting to single replica.  

### MongoDB v0.13.0

!!! warning

    Upgrading mongodb-operator to v0.10.0 will cause existing instances to restart.

- **Improved** prevented abnormal clusters from being selected during instance creation.  
- **Improved** default console access method for restored instances to NodePort.  
- **Improved** upgraded mongodb-operator to v0.10.0 with base images updated to ubi-minimal:8.6-994.  
- **Fixed** an issue where restoring MongoDB instances failed.  

### MySQL v0.21.0

- **Improved** prevented abnormal clusters from being selected during instance creation.  
- **Improved** fixed permission leakage issues in interfaces.  

### PostgreSQL v0.15.0

- **Improved** prevented abnormal clusters from being selected during instance creation.  
- **Fixed** an issue where PostgreSQL instance onboarding failed due to empty memory settings.  

### RabbitMQ v0.23.0

- **Improved** prevented abnormal clusters from being selected during instance creation.  

<span id="history"></span>

## Historical Release Notes

- [Elasticsearch Release Notes](./elasticsearch/release-notes.md)  
- [Kafka Release Notes](./kafka/release-notes.md)  
- [MinIO Release Notes](./minio/release-notes.md)  
- [MongoDB Release Notes](./mongodb/release-notes.md)  
- [MySQL Release Notes](./mysql/release-notes.md)  
- [PostgreSQL Release Notes](./postgresql/release-notes.md)  
- [RabbitMQ Release Notes](./rabbitmq/release-notes.md)  
- [Redis Release Notes](./redis/release-notes.md)  
- [RocketMQ Release Notes](./rocketmq/release-notes.md)  
