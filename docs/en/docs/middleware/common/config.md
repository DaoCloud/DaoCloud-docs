# Configuration Management

The configuration management feature provides a general configuration solution for object storage, enabling data backup and recovery for various middleware instances. The specific configuration steps are as follows:

1. Click `Configuration Management` to access the `Configuration Management` list.


2. Click `Create` to create a new configuration item in the configuration management page.


3. In the creation page, configure the following information:



    - **Name**: User-defined name used to identify the configuration item.
  
    - **Backup Type**: This configuration has two options. By default, it is set to `Managed MinIO`, which will display all MinIO instances in the middleware MinIO list. Selecting `S3` allows the use of external storage. Users need to enter the address of the external storage themselves. The address structure is similar to: http://172.30.120.201:30456.
  
    - **Access_Key, Secret_Key**: This information needs to be obtained from the MinIO management page, following these steps:
  
        1. Click `Access Address` in the MinIO instance to go to the management interface.
  
  
        2. Click `Identity` -> `Service Account` to create a new service account.
  

  
        3. Copy the Access_Key and Secret_Key created here to the configuration creation page.
  

  
    - **Bucket Name**: This name is used to define the object storage bucket required for backup, which can be obtained from the MinIO management platform, as shown in the following image:
  


4. Click `OK` to complete the creation. This configuration will be available for middleware `Backup/Restore`.

