---
hide:
  - toc
---

# Backup and Restore

Backup and restore are essential aspects of system management. In practice, it is important to
first back up the data of the system at a specific point in time and securely store the backup.
In case of incidents such as data corruption, loss, or accidental deletion, the system can be
quickly restored based on the previous backup data, reducing downtime and minimizing losses.

- In real production environments, services may be deployed across different clouds, regions,
  or availability zones. If one infrastructure faces a failure, organizations need to quickly
  restore applications in other available environments. In such cases, cross-cloud or cross-cluster
  backup and restore become crucial.
- Large-scale systems often involve multiple roles and users with complex permission management systems.
  With many operators involved, accidents caused by human error can lead to system failures.
  In such scenarios, the ability to roll back the system quickly using previously backed-up data
  is necessary. Relying solely on manual troubleshooting, fault repair, and system recovery can
  be time-consuming, resulting in prolonged system unavailability and increased losses for organizations.
- Additionally, factors like network attacks, natural disasters, and equipment malfunctions can
  also cause data accidents.

Therefore, backup and restore are vital as the last line of defense for maintaining system stability
and ensuring data security.

Backups are typically classified into three types: full backups, incremental backups,
and differential backups. Currently, DCE 5.0 supports full backups and incremental backups.

The backup and restore provided by DCE 5.0 can be divided into two categories:
**Application Backup** and **ETCD Backup**. It supports both manual backups
and scheduled automatic backups using CronJobs.

- Application Backup

    Application backup refers to backing up data of a specific workload in the cluster and then
    restoring that data either within the same cluster or in another cluster. It supports backing up
    all resources under a namespace or filtering resources by specific labels.

    Application backup also supports cross-cluster backup of stateful applications.
    For detailed steps, refer to the [Backup and Restore MySQL Applications and Data Across Clusters](../../best-practice/backup-mysql-on-nfs.md) guide.

- etcd Backup

    etcd is the data storage component of Kubernetes. Kubernetes stores its own component's data
    and application data in etcd. Therefore, backing up etcd is equivalent to backing up the
    entire cluster's data, allowing quick restoration of the cluster to a previous state in case of failures.

    It's worth noting that currently, restoring etcd backup data is only supported within the same
    cluster (the original cluster). To learn more about related best practices, refer to the
    [ETCD Backup and Restore](../../best-practice/etcd-backup.md) guide.
