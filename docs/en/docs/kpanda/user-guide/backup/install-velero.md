# Install the velero plugin

velero is an open source tool for backing up and restoring Kubernetes cluster resources. It can back up resources in a Kubernetes cluster to cloud storage services, local storage, or other locations, and restore those resources to the same or a different cluster when needed.

This section describes how to install the velero plugin.

## Prerequisites

Before installing the `velero` plugin, the following prerequisites need to be met:

- The container management module [connected to the Kubernetes cluster](../clusters/integrate-cluster.md) or [created the Kubernetes cluster](../clusters/create-cluster.md), and can access the UI interface of the cluster.

- Completed a `velero` [namespace creation](../namespaces/createns.md).

- The current operating user should have [`NS Edit`](../permissions/permission-brief.md#ns-edit) or higher permissions, for details, please refer to [Namespace Authorization](../namespaces/createns.md).

## Steps

Please perform the following steps to install the `velero` plugin for your cluster.

1. On the cluster list page, find the target cluster that needs to install the `velero` plugin, click the name of the cluster, click `Helm Apps` -> `Helm chart` in the left navigation bar, and enter `velero` in the search bar to search .

     

2. Read the introduction of the `velero` plugin, select the version and click the `Install` button. This page will take `3.0.0` version as an example to install, and it is recommended that you install `3.0.0` and later versions.

     

3. Configure basic parameters on the installation configuration interface.

     

     - Name: Enter the plugin name, please note that the name can be up to 63 characters, can only contain lowercase letters, numbers and separators ("-"), and must start and end with lowercase letters or numbers, such as metrics-server-01.
     - Namespace: Select the namespace for plugin installation, it must be `velero` namespace.
     - Version: The version of the plugin, here we take `3.0.0` version as an example.
     - Ready Wait: When enabled, it will wait for all associated resources under the application to be ready before marking the application installation as successful.
     - Failed to delete: After it is enabled, the synchronization will be enabled by default and ready to wait. If the installation fails, the installation-related resources will be removed.
     - Verbose log: Turn on the verbose output of the installation process log.

     !!! note

         After enabling `Ready Wait` and/or `Failed Delete`, it takes a long time for the app to be marked as `Running`.

4. Installation parameter configuration

     - Required parameters

         - `S3url`: object storage access address (currently only Minio has been verified for compatibility).
         - `Use existing secret`: The name of the secret used to record the username and password of the object storage.
         After enabling `Ready Wait` and/or `Failed Delete`, it takes a long time for the app to be marked as `Running`.
         - `Features`: Enabled kubernetes features plugin modules.

     - optional parameter

         - `Backupstoragelocation`: location of velero backup data storage.
         - `Name`: The name of the BackupStorageLocation object that has been created.
         - `Bucket`: Bucket name for saving backup data.
         - `Accessmode`: velero’s access mode to data, you can choose `ReadWrite`: allow velero to read and write backup data; `ReadOnly`: allow velero to read backup data, but cannot modify backup data; `WriteOnly`: only allow velero to write Backup data, backup data cannot be read.
         - `Region`: The geographical region of the cloud storage. The `us-east-1` parameter is used by default, provided by the system administrator
         - `S3forcepathstyle`: Turn on or off to use S3 forcepath style access, that is, use the bucket name as part of the URL path.
         - `Use secret`: Turn on or off to use secret to access object storage.

     

     !!! note "The main content of the secret in the `Use existing secret` parameter includes key and vaule. The key is a fixed `cloud` parameter, and the vaule value is as follows:"

         ```yaml
         [default]
         aws_access_key_id = minio
         aws_secret_access_key = minio123
         ```

     

5. Click the `OK` button to complete the installation of the `velero` plug-in, and then the system will automatically jump to the `Helm Apps` list page. After a few minutes, refresh the page to see the application just installed.
