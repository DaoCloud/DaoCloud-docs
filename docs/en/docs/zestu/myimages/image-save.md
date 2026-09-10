# Save Image

This guide explains how to save the **system disk** of a container instance to **My Images** in d.run.  
There are four methods available: **manual save**, **shutdown save**, **scheduled shutdown auto-save**, and **auto-save on overdue payment**.

## Prerequisites

- The image repository must be initialized in the selected region.
- You must have sufficient image storage quota.

## Manual Image Save

Go to **Compute Cloud** → **Container Instances**, find the container instance you want to save, click the **┇** icon on the right, and select **Save Image** from the dropdown.  
Fill in the image name and tags, then click **OK**.

<!-- ![Manual Save](../images/image04.png)

![Image Settings](../images/image05.png) -->

- **Existing Image**: If you select an existing image, a new version will be added under that image's details.
- **New Image**: If you create a new image, it will be saved as a new entry in your **My Images** list.

## Shutdown Save

When shutting down a container instance, select **Shutdown and Save System Disk** to save the image.

<!-- ![Shutdown Save](../images/image10.png) -->

## Automatic Image Save

When a container instance shuts down due to a **scheduled shutdown** or **overdue payment**, the platform will automatically save the system disk to **My Images**.

!!! warning

    If your image quota is insufficient, the system disk save will fail, and data may be lost.  
    Please ensure you have enough image space!
