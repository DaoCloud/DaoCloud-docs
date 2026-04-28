# Managing Files

This article introduces how to manage files in file storage, including folder creation, file deletion, and other operations.

## Creating a Folder

1. On the file storage details page, select the **File Info** tab, click the **Create Folder** button in the top right corner.

    ![Create folder](../images/file-upload01.png)

2. In the create folder dialog, fill in the folder name and click **OK**. The folder is created successfully, and you will be returned to the file storage details page.

    ![Fill parameters](../images/file-upload02.png)

    !!! note

        To avoid file management confusion, it is recommended to have one folder for each model or dataset.

## Uploading Files

The platform supports two ways to upload files to file storage.

1. Upload local files via SFTP tool. For operation steps, refer to the upload instructions on the file storage details interface.
2. Load remote files such as Git repository, S3 object storage, HTTP files, HuggingFace, ModelScope via preheat task. For operation steps, refer to [Remote File Preheat](./file-preheat.md).

## Deleting Files

1. On the file storage details page, select the **File Info** tab, click the **┇** menu on the right side of the target file or folder, and select **Delete**.

    ![Delete file](../images/file-upload03.png)

2. On the delete file page, click **OK**. The file is deleted successfully, and you will be returned to the file storage details page.

    ![Confirm](../images/file-upload04.png)

    !!! note

        If the file is mounted by inference services, deleting the file may cause service anomalies. Please operate with caution.
