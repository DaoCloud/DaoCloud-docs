# MinIO Disaster Recovery Solution

## Feature Introduction

The MinIO client command `mc replication` is used to configure bucket replication between MinIO servers. Site Replication is a feature in MinIO used to replicate data across multiple sites. This feature can be used to implement off-site disaster recovery, ensuring real-time synchronization of data across multiple MinIO clusters at multiple physical locations.

The Site Replication feature requires MinIO to be deployed in distributed mode, and each site must have an independent MinIO cluster.
In addition, sufficient network bandwidth is required between the clusters to support data replication.

## Disaster Recovery Using the Command Line

The following are the steps to perform off-site disaster recovery using the MinIO command line:

1. Prepare two MinIO clusters and run the following two commands to add the MinIO servers that require disaster recovery to the MinIO client.

    ```shell
    mc alias set minio1 http://host1:9000 user password
    mc alias set minio2 http://host2:9000 user password
    ```
    
    - __minio1__: The alias set by the user for the MinIO service endpoint.
    - __http://host1:9000__: The URL of the MinIO service.
    - __user__: The username required to connect to the MinIO service.
    - __password__: The password required to connect to the MinIO service.

2. Run the following command on the minio1 service to add a replication rule, so that data is automatically replicated to the target MinIO service with the alias minio2.

    ```shell
    mc admin replicate add minio1 minio2
    ```

## Disaster Recovery Using the Console

The MinIO console provides a graphical interface through which you can manage the MinIO object storage service. The steps are as follows:

1. Log in to the console of the cluster to be backed up, go to **Site Replication** in the left navigation bar, and click **Add Sites**.

    ![MinIO disaster recovery](../images/minio-rc-01.png){ width=1000px }

2. Fill in the address of the current MinIO cluster and the address of the target MinIO cluster, then click **Save**.

    ![MinIO disaster recovery](../images/minio-rc-02.png){ width=1000px }
