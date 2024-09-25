---
MTPE: windsonsea
date: 2024-05-21
---

# Create, Use and Delete Datasets

AI Lab provides comprehensive dataset management functions needed for model development, 
training, and inference processes. Currently, it supports unified access to various data sources.

With simple configurations, you can connect data sources to AI Lab, achieving unified data management, 
preloading, dataset management, and other functionalities.

## Create a Dataset

1. In the left navigation bar, click **Data Management** -> **Dataset List**, and then click the **Create** button 
   on the right.

    ![Click Create](../../images/dataset01.png)

2. Select the worker cluster and namespace to which the dataset belongs, then click **Next**.

    ![Fill in Parameters](../../images/dataset02.png)

3. Configure the data source type for the target data, then click **OK**.

    ![Task Resource Configuration](../../images/dataset03.png)

    Currently supported data sources include:

    - GIT: Supports repositories such as GitHub, GitLab, and Gitee
    - S3: Supports object storage like Amazon Cloud
    - HTTP: Directly input a valid HTTP URL
    - PVC: Supports pre-created Kubernetes PersistentVolumeClaim
    - NFS: Supports NFS shared storage

4. Upon successful creation, the dataset will be returned to the dataset list.
   You can perform more actions by clicking **┇** on the right.

    ![Dataset List](../../images/dataset04.png)

!!! info

    The system will automatically perform a one-time data preloading after the dataset is successfully created; the dataset cannot be used until the preloading is complete.

## Use a Dataset

Once the dataset is successfully created, it can be used in tasks such as model training and inference.

### Use in Notebook

In creating a Notebook, you can directly use the dataset; the usage is as follows:

- Use the dataset as training data mount
- Use the dataset as code mount

![Dataset List](../../images/dataset05.png)

### Use in Training obs

- Use the dataset to specify job output
- Use the dataset to specify job input
- Use the dataset to specify TensorBoard output

![jobs](../../images/dataset06.png)

### Use in Inference Services

- Use the dataset to mount a model

![Inference Service](../../images/dataset07.png)

## Delete a Dataset

If you find a dataset to be redundant, expired, or no longer needed, you can delete it from the dataset list.

1. Click the **┇** on the right side of the dataset list, then choose **Delete** from the dropdown menu.

    ![Delete](../../images/ds-delete01.png)

2. In the pop-up window, confirm the dataset you want to delete, enter the dataset name, and then click **Delete**.

    ![Confirm](../../images/ds-delete02.png)

3. A confirmation message will appear indicating successful deletion, and the dataset will disappear from the list.

!!! caution

    Once a dataset is deleted, it cannot be recovered, so please proceed with caution.
