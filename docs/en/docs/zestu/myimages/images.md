# My Images

**My Images** provides a Harbor-based image repository service that allows users to save the system disk of container instances as images.  
This helps prevent data loss and simplifies the process of creating new container instances from saved images.

!!! note

    d.run provides each user with **50 GB** of free image storage. For additional quota, please contact **400-002-6898**.

## Prerequisites

- Logged in to your d.run account

## Initialize Image Repository

1. Log in to d.run, go to **Compute Cloud** -> **My Images**, select a region, and click **Initialize Image Repository**.

    <!-- ![My Images](../images/image01.png) -->

2. Set a username and password for the image repository, then click **Start Initialization**.

    <!-- ![Initialize](../images/image02.png) -->

3. After initialization, you can access the **Harbor repository** using the provided repository address.

    <!-- ![Harbor Repository](../images/image03.png) -->

## Using Images

To create a new container instance using a saved image:

- Go to **Compute Marketplace** -> **Buy Now** or  
- Go to **Container Instances** -> **Create**, then select **My Images** as the image source.

    <!-- ![Use Image](../images/image09.png) -->

## Delete Image or Image Tags

1. In **Compute Cloud** -> **My Images**, find the image you want to delete and click **Delete** in the action column.

    <!-- ![Delete Image](../images/image06.png) -->

2. In the confirmation popup, click **OK** to delete all versions of the selected image.

    ![Confirm Deletion](../images/image07.png)

3. To delete a specific version of an image, click into the image details page, find the version you want to delete, and click **Delete**.

    ![Delete Image Version](../images/image08.png)

    !!! warning

        Deleted images or image versions **cannot be recovered**. Please proceed with caution!
