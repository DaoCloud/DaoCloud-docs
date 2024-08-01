# Backup Configuration

DCE Data Services provides MySQL with backup and restore capabilities to ensure data safety. In the workspace, the workspace administrator can centrally manage the storage configurations for MySQL data backups.

## Create a Backup Configuration

1. Click the **MySQL Database** in the navigation bar.
2. In the MySQL Database navigation bar, click **Backup Configuration**, and then click the **Create** button in the list.

    <!-- ![mysql-backup-config](../../images/mysql-backup-config.png) -->

3. Select the type of backup configuration.

    - When using the MinIO instance provided by DCE 5.0 Data Services, select the MinIO instance where you want to backup data. The system will automatically fetch the address of the selected MinIO. You need to fill in the Access_Key, Secret_Key, and Bucket name of the selected MinIO instance. Ensure that the specified Bucket already exists in MinIO.

    - When using other S3 object storage: Fill in the access address, Access_Key, Secret_Key, and Bucket name of the S3 you want to use.

    <!-- ![mysql-backup-config](../../images/mysql-backup-config-1.png) -->

    <!-- ![mysql-backup-config](../../images/mysql-backup-config-2.png) -->

4. After filling in and verifying the information, click **OK** to return to the backup configuration list, where you can view the successfully created storage information.

## Edit a Backup Configuration

Go to the backup configuration list, click the **...** -> **Update** in the last column of the object storage you want to edit, and make the desired changes.

## Delete a Backup Configuration

Go to the backup configuration list, click the **...** -> **Delete** in the last column of the object storage you want to delete.

If the middleware instance in the workspace is using the selected object storage instance, it cannot be deleted.

<!-- ![mysql-backup-config](../../images/mysql-backup-config-3.png) -->
