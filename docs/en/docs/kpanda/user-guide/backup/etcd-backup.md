# etcd backup

ETCD backup is based on cluster data as the core backup. In Cases such as hardware device damage, development and test configuration errors, etc., the backup cluster data can be restored.

This section will introduce how to realize the etcd backup of the cluster through the container management interface.

## Prerequisites

- [Integrated the Kubernetes cluster](../clusters/integrate-cluster.md) or
  [created the Kubernetes cluster](../clusters/create-cluster.md),
  and you can access the UI interface of the cluster.

- Created a [namespace](../namespaces/createns.md),
  [user](../../../ghippo/user-guide/access-control/user.md),
  and granted [`NS Admin`](../permissions/permission-brief.md#ns-admin) or higher permissions to the user.
  For details, refer to [Namespace Authorization](../permissions/cluster-ns-auth.md).

- Prepared a MinIO instance. It is recommended to create it through DCE 5.0's MinIO middleware.
  For specific steps, refer to [MinIO Object Storage](../../../middleware/minio/user-guide/create.md).

## Create etcd backup

Follow the steps below to create an etcd backup.

1. On the __Backup and Recovery__ - __ETCD Backup__ page, you can see all the current backup strategies. Click __Create Backup Strategy__ on the right to create an ETCD backup strategy for the target cluster.

    

2. Fill in the basic information. After filling in, click Next to automatically verify the connectivity of ETCD. If the verification passes, proceed to the next step.
   
    - First select the backup cluster and log in to the terminal
    - Fill in the ETCD address, most standard K8s clusters are: `https://node number:2379` 
    - Fill in the CA certificate, you can use the following command to view the content of the certificate and copy and paste it to the corresponding location:

        ```shell
        cat /etc/kubernetes/ssl/etcd/ca.crt
        ```

    - Fill in the Cert certificate, you can use the following command to view the content of the certificate and copy and paste it to the corresponding location:

        ```shell
        cat /etc/kubernetes/ssl/apiserver-etcd-client.crt
        ```

    - Fill in the Key, you can use the following command to view the content of the certificate and copy and paste it to the corresponding location:

        ```shell
        cat /etc/kubernetes/ssl/apiserver-etcd-client.key
        ```

        

3. Select the backup method, which is divided into manual backup and scheduled backup.
   
    - Manual backup: Perform a backup of ETCD full data immediately based on the backup configuration. Backup chain length: The longest length of backup data to keep, the default is 30.
  
        

    - Timing backup: Perform periodic full backup of ETCD data according to the set backup frequency. Choose backup frequency: support hourly, daily, weekly, monthly levels and custom methods.

        

4. Storage location
   
    - Storage provider: S3 storage is selected by default
    - Object storage access address: MinIO access address
    - Bucket: Create a Bucket in MinIO and fill in the name
    - Username: MinIO login username
    - Password: MinIO login password
   
        

5. After the creation is successful, a piece of data will be generated in the backup policy list. __Operations__ include log, view YAML, update policy, stop, run now. When the backup method is manual, you can click __Immediately__ to back up. When the backup method is scheduled backup, the backup will be performed according to the configured time.

    

6. Click __View Log__ to display the log content. By default, 100 lines are displayed. If you want to view more log information or download logs, go to [Observability](https://demo-dev.daocloud.io/insight/logs?filterType=workload&cluster=chenwen-test&namespace=kpanda-system&workloadKind=deployment&workload=chenwen-test-etcd-backup&pod=chenwen-test-etcd-backup-5cf6d6bdfc-xstkx&container=backup-restore)

    

## Backup policy details

1. Click to enter the details of the backup strategy, including basic information and backup records.

    

2. Check the backup point. After selecting a cluster, you can view all the backup information under the cluster. Every time a backup is performed, a backup point is correspondingly generated, and the application can be quickly restored through the backup point in the successful state.
   
    