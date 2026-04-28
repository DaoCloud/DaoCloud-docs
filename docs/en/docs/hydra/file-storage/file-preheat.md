# Remote File Preheat

The remote file preheat function is used to preheat remote files to the cluster environment to improve model deployment and operation efficiency.

## Prerequisites

- Cluster file storage has been created successfully. For creation steps, refer to [Create File Storage](./storage.md).
- The cluster has installed the preheat task dependency component Dataset. For installation process, refer to [Install Helm App](../../kpanda/user-guide/helm/helm-app.md).

## Operation Steps

1. Enter the large model service platform, select **File Storage** from the left navigation menu. In the file storage list, click the **target file storage name** to enter the file storage details page.

    ![File storage list](../images/file-preheat01.png)

2. On the file storage details page, select the **Preheat Task** tab, click the **Create Preheat Task** button in the top right corner.

    ![Create preheat task](../images/file-preheat02.png)

3. On the create preheat task page, select the file storage directory, source type, fill in the source information, and click **OK**. The preheat task is created successfully, and you will be returned to the file storage details page.

    ![Fill parameters](../images/file-preheat03.png)

    | Parameter | Constraint / Description | Remarks |
    |---|---|---|
    | File Storage Directory | Select the file storage directory to preheat | Click "Go Create" to jump to the File Info tab to create a directory |
    | Source Type | Select the file source type | Platform supports GIT, S3, HTTP, HuggingFace, ModelScope five source types |
    | Source Information | Fill in the file source information | Fill in according to the source type |

4. Perform more operations.
