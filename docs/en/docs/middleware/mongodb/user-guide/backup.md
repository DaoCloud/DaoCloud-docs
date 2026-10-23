# Backup Management

MongoDB supports automatic or manual backup of data in running instances.

## Backup Configuration

You can create multiple backup configurations for different instances. For example, one backup configuration per instance.

1. On the homepage of the MongoDB database, click **Configuration Management**.

    ![Configuration Management](../images/backup03.png)

2. On the **Storage Configuration** tab, click the **Create** button.

    ![Backup Configuration](../images/backup02.png)

    - Backup Type: Managed MinIO or S3
    - Backup Instance: Select an instance
    - Enter the Access_Key, Secret_Key, and Bucket name used to access the instance

    !!! note

        On the **Parameter Template** tab, you can create various templates for subsequent configuration.

3. After confirming that the information is correct, click **OK**.

## Backup Settings

Before backing up, you need to configure the backup settings first.

Enter a MongoDB instance and click **Backup Management** -> **Backup Settings** in the left navigation bar.

![Backup Settings](../images/backup01.png)

- Backup Configuration: You can create multiple [backup configurations](#backup-configuration) in advance.
- Path: The path of the data to be backed up, for example, /data123
- Automatic Backup: Once automatic backup is enabled, running instances will be fully backed up automatically.

    By default, automatic backups retain 30 copies.

## Create a Backup

1. Enter a MongoDB instance and click **Backup Management** -> **Backup Data** -> **Create Backup** in the left navigation bar.

    ![Create Backup](../images/backup04.png)

2. In the dialog box, enter a backup name and click **OK**.

    ![Enter a Name](../images/backup05.png)

3. The screen displays a success message. Click the **┇** button on the right to perform more operations.

## Recover Data

If you want to recover data, click the **┇** button on the right in the backup data list and select **Recover** in the pop-up menu.

![Recover](../images/backup06.png)

Select the recovery location, enter the name of the target instance, and click **Recovery Settings**.

![Recover](../images/backup07.png)
