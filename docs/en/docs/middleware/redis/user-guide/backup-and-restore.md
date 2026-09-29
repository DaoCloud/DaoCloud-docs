# Redis Backup and Restore

Redis automatically generates data snapshots at specified intervals and saves them as `.rdb` files.
The backup and restore features of Redis ensure data persistence and security. This article describes how to back up and restore the data of the Redis cache service.

## Prerequisites

Before backing up a Redis instance, confirm that the `Backup Configuration` of the current workspace already contains a verified S3 storage.

![backup](../images/backup-restore.png)

## Backup Configuration

1. Select the target Redis instance from the instance list.
2. Click **Backup Management** -> **Backup Settings** in the left menu.
3. On the current page, select the S3 storage for backup and fill in the path address where the data is to be stored.

    !!! note

        Redis backup data is usually implemented through RDB files. When configuring the backup path, you only need to specify the storage folder name and the .rdb file extension.

4. To schedule daily or weekly backups, enable the automatic backup feature and select the backup period and time.

    ![backup](../images/backup-restore-1.png)

## Backup Data

1. Select the target Redis instance from the instance list.
2. Click **Backup Management** -> **Backup Data** in the left menu.
3. Click **Create Backup** at the top right of the list and fill in the backup name.

    ![backup](../images/backup-restore-2.png)

4. After clicking **OK**, you can view the backup status, backup time, path, and other information in the list.

    ![backup](../images/backup-restore-3.png)

## Restore Data

1. Select the data to be restored in the backup data list, click the operation button in the last column of the backup data list, and click **Restore**.

    You can choose to restore to the cluster and namespace where the current instance resides, or restore to another cluster and namespace.

    ![alt text](../images/backup-restore-4.png)

2. After clicking **OK**, you can view the status of data restoration.

    ![backup](../images/backup-restore-5.png)
