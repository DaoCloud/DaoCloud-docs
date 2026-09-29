# Backup Management

PostgreSQL supports automatic or manual backup of data in running instances.

## Backup Configuration

Only one shared configuration can be applied to each cluster, so modify it with caution.

![Backup Settings](../images/backup00.png)

## Backup Settings

Before backing up, you need to configure the backup settings first.

Enter a PostgreSQL instance and click **Backup Management** -> **Backup Settings** in the left navigation bar.

![Backup Settings](../images/backup01.png)

Automatic Backup: Once automatic backup is enabled, running instances will be fully backed up automatically.

## Create a Backup

1. Enter a PostgreSQL instance and click **Backup Management** -> **Backup Data** -> **Create Backup** in the left navigation bar.

    ![Create Backup](../images/backup04.png)

2. In the dialog box, enter a backup name and click **OK**.

    ![Enter a Name](../images/backup05.png)

3. The screen displays a success message. Click the **┇** button on the right to perform more operations.

## Delete Backup Data

If you want to delete backup data, click the **┇** button on the right in the backup data list and select **Delete** in the pop-up menu.

![Delete](../images/backup06.png)

After confirming that the information is correct in the dialog box, click **OK**.
