---
hide:
  - toc
---

# Create MinIO

In the list of MinIO instances, do the following to create a MinIO instance.

1. Select `Minio Storage` from the left navigation bar.

    

2. Click `Deploy Now` to create a MinIO instance when using it for the first time. You can then click the `New Instance` button in the upper right corner of the list.

    

3. On the `Create MinIO instance` page, after setting the basic information, click `Next`.

    

4. After configuring the specifications, click `Next`.

    - Version: MinIO version number, currently only supports MinIO 4.0.15
    - Number of replicas: more than 4 replicas are required for high availability
    - Resource quota: select the rules according to the actual situation
    - Storage: Select the storage volume and the total amount of storage space for the MinIO instance

    

5. After the service is set, click `Next`.

    - Access method: You can choose intra-cluster access or Nodeport access.
    - Service Settings: Set the username and password for connecting to the MinIO instance.

    

6. Confirm that the instance configuration information is correct, and click `Confirm` to complete the creation.

    

7. On the instance list page, check whether the instance is successfully created. The status of the newly created instance is `Not Ready`, and it will change to `Running` after a few minutes.

    