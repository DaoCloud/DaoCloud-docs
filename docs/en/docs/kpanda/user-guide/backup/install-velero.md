# Install the velero plugin

velero is an open source tool for backing up and restoring Kubernetes cluster resources. It can back up resources in a Kubernetes cluster to cloud storage services, local storage, or other locations, and restore those resources to the same or a different cluster when needed.

This section describes how to install the velero plugin.

## Prerequisites

Before installing the __velero__ plugin, the following prerequisites need to be met:

- The container management module [connected to the Kubernetes cluster](../clusters/integrate-cluster.md) or [created the Kubernetes cluster](../clusters/create-cluster.md), and can access the UI interface of the cluster.

- Completed a __velero__ [namespace creation](../namespaces/createns.md).

- The current operating user should have [`NS Edit`](../permissions/permission-brief.md#ns-edit) or higher permissions, for details, refer to [Namespace Authorization](../namespaces/createns.md).

## Steps

Please perform the following steps to install the __velero__ plugin for your cluster.

1. On the cluster list page, find the target cluster that needs to install the __velero__ plugin, click the name of the cluster, click __Helm Apps__ -> __Helm chart__ in the left navigation bar, and enter __velero__ in the search bar to search .

     

2. Read the introduction of the __velero__ plugin, select the version and click the __Install__ button. This page will take __3.0.0__ version as an example to install, and it is recommended that you install __3.0.0__ and later versions.

     

3. Configure basic parameters on the installation configuration interface.

     

     - Name: Enter the plugin name, please note that the name can be up to 63 characters, can only contain lowercase letters, numbers and separators ("-"), and must start and end with lowercase letters or numbers, such as metrics-server-01.
     - Namespace: Select the namespace for plugin installation, it must be __velero__ namespace.
     - Version: The version of the plugin, here we take __3.0.0__ version as an example.
     - Ready Wait: When enabled, it will wait for all associated resources under the application to be ready before marking the application installation as successful.
     - Failed to delete: After it is enabled, the synchronization will be enabled by default and ready to wait. If the installation fails, the installation-related resources will be removed.
     - Verbose log: Turn on the verbose output of the installation process log.

     !!! note

         After enabling __Ready Wait__ and/or __Failed Delete__ , it takes a long time for the app to be marked as __Running__ .

4. Installation parameter configuration

     - Required parameters

         - __S3url__ : object storage access address (currently only Minio has been verified for compatibility).
         - __Use existing secret__ : The name of the secret used to record the username and password of the object storage.
         After enabling __Ready Wait__ and/or __Failed Delete__ , it takes a long time for the app to be marked as __Running__ .
         - __Features__ : Enabled kubernetes features plugin modules.

     - optional parameter

         - __Backupstoragelocation__ : location of velero backup data storage.
         - __Name__ : The name of the BackupStorageLocation object that has been created.
         - __Bucket__ : Bucket name for saving backup data.
         - __Accessmode__ : velero’s access mode to data, you can choose __ReadWrite__ : allow velero to read and write backup data; __ReadOnly__ : allow velero to read backup data, but cannot modify backup data; __WriteOnly__ : only allow velero to write Backup data, backup data cannot be read.
         - __Region__ : The geographical region of the cloud storage. The __us-east-1__ parameter is used by default, provided by the system administrator
         - __S3forcepathstyle__ : Turn on or off to use S3 forcepath style access, that is, use the bucket name as part of the URL path.
         - __Use secret__ : Turn on or off to use secret to access object storage.

     

     !!! note "The main content of the secret in the __Use existing secret__ parameter includes key and vaule. The key is a fixed __cloud__ parameter, and the vaule value is as follows:"

         ```yaml
         [default]
         aws_access_key_id = minio
         aws_secret_access_key = minio123
         ```

     

5. Click the __OK__ button to complete the installation of the __velero__ plug-in, and then the system will automatically jump to the __Helm Apps__ list page. After a few minutes, refresh the page to see the application just installed.
