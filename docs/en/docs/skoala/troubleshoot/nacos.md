# Nacos Version Downgrade

If you are using a version later than Nacos 2.1.x and want to downgrade to a version earlier than 2.1.x,
and you are using an external database, you can refer to the following steps to downgrade the version:

1. Find the Nacos CR resource that needs to be downgraded.

    ```bash
    kubectl get nacos -A
    ```

2. Modify the `image` field and replace it with the version to be downgraded to.

3. Modify the database.

    ```sql
    alter table config_info drop column encrypted_data_key;
    alter table config_info_beta drop column encrypted_data_key;
    alter table his_config_info drop column encrypted_data_key;
    ```

4. Restart the StatefulSet of this Nacos.
