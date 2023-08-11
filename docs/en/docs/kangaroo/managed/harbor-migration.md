# Harbor Migration Guide

This document will guide you through the process of migrating your existing Harbor environment to a new cluster environment. This migration scenario simulates a complex situation where the original Harbor uses Localpath storage,
and the new environment uses Minio object storage. The migration process involves the migration of Harbor, PostgreSQL,
and Minio.

## Environment Preparation

1. Original Harbor Environment: Harbor container environment using Localpath as the storage backend.
2. New Cluster Environment: Includes new PostgreSQL and Minio storage environments.
3. Plan storage and other resources appropriately.
4. Set the original Harbor to read-only mode during the migration process to ensure data consistency and integrity.

## Step 1: Migrate PostgreSQL

In this step, we will migrate the PostgreSQL database used by the original Harbor to the new cluster environment.

Tool Installation: [PostgreSQL Official Website](https://www.postgresql.org/download/)

1. Backup the PostgreSQL database used by Harbor using the `pg_dump` tool:

    ```sh
    pg_dump --username=<original_database_username> --host=<original_database_host> --port=<original_database_port> --format=plain --file=harbor_backup.sql <database_name>
    ```

    Replace the parameters in angle brackets with the actual values. For example, if the original database username is `postgres`, the original database host is `localhost`, the port is `32332`, and the database name is `core`, the command would be:

    ```sh
    pg_dump --username=postgres --host=localhost --port=32332 --format=plain --file=harbor_backup.sql core
    ```

2. Transfer the database backup file `harbor_backup.sql` from the original Harbor environment to the new PostgreSQL environment.

3. Restore the database in the new PostgreSQL environment:

    ```sh
    psql --host=<new_database_host> --port=<new_database_port> --username=<new_database_username> --dbname=<database_name> --file=harbor_backup.sql
    ```

    Replace the parameters in angle brackets with the actual values. For example, if the new database host is `localhost`, the port is `32209`, the new database username is `postgres`, and the database name is `core`, the command would be:

    ```sh
    psql --host=localhost --port=32209 --username=postgres --dbname=core --file=harbor_backup.sql
    ```

After completing these steps, you have successfully migrated the PostgreSQL database of Harbor to the new cluster environment. Make sure to back up your data throughout the migration process and perform thorough testing before the migration to ensure data security and business continuity.

## Step 2: Migrate Image Data to Minio

In this step, we will migrate the image data stored in the original Harbor to the Minio storage system. Follow these steps:

1. Download and install the `rclone` tool in the new cluster environment. `rclone` is a powerful command-line tool used for syncing and copying data between different object storages. You can find installation instructions on the [rclone official website](https://rclone.org/).

2. Configure `rclone` by setting the connection information to connect to the Minio storage. Open a terminal or command prompt and execute the command `rclone config`, which will guide you through the configuration process. Enter the configuration name, Minio storage type, access keys, and other required information as prompted. Ensure that you set the connection information correctly and can successfully connect to the Minio storage bucket.

3. Determine the specific directory where the registry service of the original Harbor is mounted. This directory contains the image files.

4. Use `rclone` to migrate the data. Run the following command in the terminal or command prompt:

    ```sh
    rclone copy <original_Harbor_image_storage_directory> <rclone_config_name>:<Minio_bucket_name>/harbor/images/
    ```

5. Replace the parameters in angle brackets with the actual values. For example, if the rclone configuration name is `minio`, the Minio bucket name is `harbor-images`, and the original Harbor image storage directory is `/data/docker/registry/`, the command would be:

    ```sh
    rclone copy /data/docker/registry/ minio:harbor-images/harbor/images/
    ```

!!! note

    The data migration process may take a long time, depending on the size of the image files and the network speed. Please be patient and wait for the data migration to complete.

## Step 3: Create a New Harbor Instance

In this step, we will create a new Harbor instance based on the new PostgreSQL and Minio environment. Ensure that Harbor is running smoothly in the new cluster environment.

1. In the new cluster environment, create a new Harbor instance using the connection information of the new PostgreSQL
   and Minio. You can use the container registry component to create a new instance. Please note that when creating a
   new instance, the account password should be consistent with the original environment, and you also need to select
   the database instance and minio storage in the new environment.
1. Ensure that the new Harbor instance has been successfully installed and configured.
1. Verify that the image data has been successfully migrated to Minio storage in the new Harbor instance.
1. Ensure that the new Harbor instance is running smoothly in the new cluster environment and can access and provide image services.
1. Test the new Harbor instance to verify the integrity and correctness of the migration. You can try uploading and
   downloading images and checking information such as logs and events to ensure that Harbor works normally.
1. If everything runs smoothly, congratulations! You have successfully completed the migration of Harbor to the
   new cluster environment, and the current Harbor instance is running smoothly in the Minio storage system.

Note that before performing the actual migration and creating a new Harbor instance, please ensure that you have made
sufficient backups and tested the migration process in a test environment to ensure data security and business continuity.
