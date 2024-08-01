---
hide:
  - toc
---

# Manual Backup

MySQL databases support manual backups for instances in the `running` state, allowing you to back up your database data at any time to ensure data security.

## Steps

1. Access **MySQL Database**.
2. In the instance list, select the instance you want to enable automatic backup for, and click its name to enter the instance details.
3. Click **Backup Management** -> **Backup Data** in the left navigation bar.

    <!-- ![manual-backup](../../images/manual-backup.png) -->

4. Click the **Create Backup** button at the top right of the list, and fill in the name of the backup.

    - Ensure that the **Backup Management** -> **Backup Settings** section has the target backup object storage instance and storage path selected.
    - Confirm whether to enable automatic backup as needed.

    <!-- ![manual-backup](../../images/manual-backup-1.png) -->

5. Click **OK**, return to the backup list, and you can view the status of the backup in the list.
