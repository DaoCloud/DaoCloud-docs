# Middleware Features

|      | **Kafka**   | **Elasticsearch** | **MySQL** | **Redis**                 | **postgreSQL** | **mongoDB** | **RabbitMQ** | **RocketMQ** | **MinIO** |
|-------------|-------------|-------------------|-----------|---------------------------|----------------|-------------|--------------|--------------|-----------|
| **Support Version**    | 3.1.0             | 7.16.3    | 5.7.31 / 8.0.29 / 8.0.31  | 6.2.5          | 15.1.0      | 4.2.24       | 3.9.25       | v4.5.0    | RELEASE.2023-10-07T15-07-38Z |
| **Single Node Deployment**    | ✓                 | N/A       | ✓                         | ✓              | ✓           | N/A          | ✓            | ✓         | ✓                            |
| **High Availability Deployment**   | ✓                 | ✓         | ✓                         | ✓              | ✓           | ✓            | ✓            | ✓         | ✓                            |
| **Vertical Scaling**    | ✓                 | ✓         | ✓                         | ✓              | ✓           | ✓            | ✓            | ✓         | N/A                          |
| **Vertical Shrink**    | N/A               | N/A       | N/A                       | N/A            | N/A         | N/A          | N/A          | N/A       | N/A                          |
| **Horizontal Scaling**    | ✓                 | ✓         | ✓                         | ✓              | ✓           | ✓            | ✓            | ✓         | ✓                            |
| **Horizontal Shrink**    | ✓                 | ✓         | ✓                         | ✓              | ✓           | ✓            | ✓            | ✓         | ✓                            |
| **Storage Expansion**    | ✓                 | ✓         | ✓                         | ✓              | ✓           | N/A          | ✓            | ✓         | N/A                          |
| **Restart**      | ✓                 | ✓         | ✓                         | ✓              | ✓           | ✓            | ✓            | ✓         | ✓                            |
| **Access Whitelist**   | ✓                 | N/A       | ✓                         | ✓              | ✓           | N/A          | N/A          | N/A       | N/A                          |
| **Monitoring**      | ✓                 | ✓         | ✓                         | ✓              | ✓           | ✓            | ✓            | ✓         | ✓                            |
| **Logging**      | ✓                 | ✓         | ✓                         | ✓              | ✓           | ✓            | ✓            | ✓         | ✓                            |
| **Parameter Configuration**    | ✓                 | N/A       | ✓                         | ✓              | ✓           | ✓            | N/A          | ✓         | ✓                            |
| **Built-in Parameter Template**  | ✓                 | N/A       | ✓                         | ✓              | N/A         | N/A          | N/A          | N/A       | N/A                          |
| **Backup**      | N/A               | N/A       | ✓                         | ✓              | ✓           | N/A          | N/A          | N/A       | N/A                          |
| **Restore from Backup**   | N/A               | N/A       | ✓                         | ✓              | N/A         | N/A          | N/A          | N/A       | N/A                          |
| **Console**     | ✓                 | ✓         | ✓                         | ✓              | ✓           | ✓            | ✓            | ✓         | ✓                            |
| **Node Affinity**   | ✓                 | ✓         | ✓                         | ✓              | ✓           | ✓            | ✓            | ✓         | ✓                            |
| **Workload Anti-affinity** | ✓                 | ✓         | ✓                         | ✓              | N/A         | ✓            | ✓            | ✓         | N/A                          |

!!! note

    The Redis backup and recovery function depends on the deployment version. Single mode does not support backup/recovery; cluster mode supports backup but not recovery; master-slave mode supports backup/recovery.
