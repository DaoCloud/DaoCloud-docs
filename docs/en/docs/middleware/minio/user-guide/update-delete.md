---
MTPE: ModetaNiu
Date: 2024-07-08
---

# Update and Delete MinIO Instance

## Update MinIO Instance

If you want to update or modify MinIO's resource configuration, you can follow the instructions on this page.

1. In the instance list, click the __...__ button on the right, and select __Update Instance__ from the pop-up menu.

    ![Update instance](../images/minio-update.png)

2. Modify the Basic Information and click __Next__ .

    - Can be modified: Description
    - Can not be modified: Instance name, Location

    ![Basic info](../images/minio-update02.png)

3. Modify the Spec Settings, and click __Next__ .

    - Can be modified: CPU Quota and Memory Quota
    - Can not be modified: Version, Deployment Mode, Storage Class, Storage Capacity

    ![Spec settings](../images/minio-update03.png)

4. Modify the service settings and click __OK__ .

    ![Service settings](../images/minio-update04.png)

5. Back to the instance list, a message will be displayed in the upper right corner of the screen: __Update instance successful__ .

    ![Successful](../images/minio-update05.png)

## Remove MinIO Instance

If you want to delete a list of instances, you can follow the instructions on this page.

1. In the instance list, click the __...__ button on the right, and select __Delete Instance__ from the pop-up menu.

    ![Delete instance](../images/minio-delete01.png)

2. Enter the name of the instance list in the pop-up window, and click the __Delete__ button after confirming 
   that it is correct.

    !!! warning

        After an instance is deleted, all messages related to the instance will also be deleted, so please proceed with caution.

    ![Confirm](../images/minio-delete02.png)