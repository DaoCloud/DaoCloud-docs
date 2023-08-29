# Local storage

Local Storage (LS) is a module of HwameiStor, which aims to provide high-performance local persistent LVM storage volumes for applications.

![architecture](../img/architecture.png)

Currently supported local persistent data volume type: `LVM`.

Currently supported local disk types: `HDD`, `SSD`, `NVMe`.

## Use cases

HwameiStor provides two kinds of local data volumes: LVM and Disk.
As a part of HwameiStor, local storage is responsible for providing LVM local data volumes, including highly available LVM data volumes and non-highly available LVM data volumes.

Non-highly available LVM local data volumes are suitable for the following cases and applications:

- A **database** with high availability features, such as MongoDB, etc.
- **Message middleware** with high availability features, such as Kafka, RabbitMQ, etc.
- A **key-value storage system** with high availability features, such as Redis, etc.
- Other applications with high availability features

Highly available LVM local data volume, suitable for the following cases and applications:

- **Database**, such as MySQL, PostgreSQL, etc.
- Other applications that require high data availability

## Install and deploy using Helm Chart

Local storage is part of HwameiStor and must work with local disk manager. Users are advised to [deploy via helm-charts](../install/deploy-helm.md).

## Independent installation and deployment method

Developers can install [independent installation](../install/deploy-helm.md) local-storage from source code, mainly for development and testing use cases. For this installation method, you need to install [Local Disk Manager](./ldm.md) in advance.
