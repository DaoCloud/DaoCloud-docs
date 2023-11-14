# Nacos Version Downgrade

If you are using a version higher than Nacos 2.1.x and want to downgrade to a version lower than 2.1.x while using an external database, you can follow the steps below to downgrade the version:

1. Identify the Nacos CR (Custom Resource) resource that needs to be downgraded.

    ```bash
    kubectl get nacos -A
    ```

2. Modify the `image` field and replace it with the desired version for downgrade.

3. Modify the database using the following SQL statements:

    ```sql
    alter table config_info drop column encrypted_data_key;
    alter table config_info_beta drop column encrypted_data_key;
    alter table his_config_info drop column encrypted_data_key;
    ```

4. Restart the StatefulSet of this Nacos deployment.
