---
hide:
  - toc
---

# Configure Automatic Backups

The MySQL database supports automatic backups of database instances. Since enabling backups can affect database read/write performance, it is recommended to schedule automatic backups during off-peak business hours. This ensures quick recovery and data safety in case of data loss.

## Steps

1. Navigate to **MySQL Database**.
2. In the instance list, select the instance for which you want to enable automatic backups and click its name to enter the instance details.
3. Click **Backup Management** -> **Backup Settings** in the left navigation bar.

    <!-- ![auto-backup](../../images/auto-backup.png) -->

    - Backup Configuration: Select the object storage instance configured in the workspace to store the backup data in the selected instance.
    - Path: Specify the address in the object storage. The complete S3 path format is `s3://bucket-name/object-key`. It should start with `/`.
    - Automatic Backup: Disabled by default. If enabled, the MySQL instance will be backed up periodically according to the set `Automatic Backup Cycle` and `Time`.
    - Automatic Backup Cycle: Selected by default.
        - Select All: Choose every day of the week. The system will perform automatic backups every day.
        - Select Cycle: Choose one or several days of the week. The system will perform automatic backups on the selected days.
    - Backup Time Period: Automatically perform backups within the selected time period.
    - Number of Backup Retentions: When the number of backups for the instance reaches the set value, the system will delete the earliest backup data that exceeds the set value.
