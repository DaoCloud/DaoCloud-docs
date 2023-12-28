# Configuration Management

The configuration management function provides a common configuration scheme for object storage, used for data backup and recovery of various middleware instances. The specific configuration method is as follows:

1. Click `Configuration Management` to enter the `Configuration Management` list;

    

2. Click `Create` to create a new configuration item on the configuration management page;

    

3. On the creation page, configure the following content:

    

    - **Name**: User-defined, used to identify the configuration item;

    - **Backup Type**: This configuration has two options, default is `Managed MinIO`, which will display all instances in the MinIO list of middleware; select `S3` to use external storage, and the user needs to enter the address of the external storage on their own, the address structure is similar to: http://172.30.120.201:30456;

    - **Access_Key, Secret_Key**: This item needs to be obtained on the MinIO management page, the steps are as follows:

        1. Click `Access Address` in the MinIO instance to enter the management interface;

            

        2. Click `Identity` -> `Service Account`, create a new `Service Account`;

            

        3. Copy the created `Access_Key` and `Secret_Key` to the create configuration page.

            

    - **Bucket Name**: This name is used to define the object storage bucket required for backup, which can be obtained from the MinIO management platform, as shown in the following figure:

        

4. Click `OK` to complete the creation, and this configuration will be available for `Backup/Recovery` of the middleware.

    
