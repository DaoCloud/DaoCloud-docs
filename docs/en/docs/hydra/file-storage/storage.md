# Create File Storage

File storage is mainly used to store model files, dataset files, and other file resources. Users can easily preheat local files or remote files to the cluster environment to improve model deployment and operation efficiency.
The management of file storage in ops management view and regular user view is separate, but their management logic is the same, and related operations can be referenced.

!!! note

    The platform provides 500Gi space for each cluster file storage by default. If you need to modify the capacity, refer to the [File Storage Expansion](./file-scale.md) guide.

## Operation Steps

1. Enter the large model service platform, select **File Storage** from the left navigation menu, click the **Create File Storage** button in the top right corner.

    ![Click create](../images/file-storage01.png)

2. On the create page, select the cluster and fill in the description information, click **OK**. The file storage is created successfully, and you will be returned to the file storage list.

    ![Fill parameters](../images/file-storage02.png)

3. Perform more operations.

    - Update: In the file storage list, click the **┇** menu on the right side of the target file storage and select **Update**.
    - Delete: In the file storage list, click the **┇** menu on the right side of the target file storage and select **Delete**. After deletion, it cannot be recovered. Please operate with caution.

    ![More operations](../images/file-storage03.png)
