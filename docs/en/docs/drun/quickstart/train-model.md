# Train Models in AI Lab - User

The previous tutorials use ready-made models from the Model Gallery. To train models with your own data and code,
use [AI Lab](../baize/intro/index.md) for the complete workflow of dataset management, Notebook debugging, and distributed training.
This tutorial walks through the minimal pipeline with a Tensorflow training job on Fashion-MNIST.

## Prerequisites

- A work cluster with GPU nodes has been created. See [Create a Work Cluster](join-cluster.md).
- Sign in to the console with a user who has the AI Lab role, and the workspace is bound to a namespace.
- A StorageClass with `ReadWriteMany` access mode (NFS or JuiceFS recommended) exists in the cluster for dataset mounting.

!!! note

    AI Lab (`baize`) is enabled in the manifest by default. If the module is not shown in the console,
    see [Install AI Lab](../baize/intro/install.md).

## Steps

1. **Prepare datasets**: in **Data Management** -> **Datasets**, click **Create** and create three datasets:

    | Dataset | Purpose | Data Source |
    |---|---|---|
    | Training code | Store the training script | `tensorflow/tf-fashion-mnist-sample` ([sample repo](https://github.com/samzong/training-sample-code.git)) |
    | Training data | The Fashion-MNIST dataset | [github.com/zalandoresearch/fashion-mnist](https://github.com/zalandoresearch/fashion-mnist.git) |
    | Empty dataset (PVC) | Store training artifacts | Empty source; the PVC is provisioned by the platform |

2. **Prepare the environment**: create a CONDA environment in **Environment Dependencies** with Tensorflow preinstalled.
   After the environment is warmed up, it can be mounted into Notebooks and training jobs without building images:

    ```yaml
    name: tensorflow
    channels:
      - defaults
      - conda-forge
    dependencies:
      - python=3.12
      - tensorflow
    prefix: /opt/conda/envs/tensorflow
    ```

3. **Debug the script in a Notebook**:

    1. Click **Create** in **Notebooks**, associate the three datasets (mount paths follow the hints on the creation page) and bind the Tensorflow environment.
    2. After the Notebook is created, open it from the access address in the list and run the following command in the terminal:

        ```bash
        python /home/jovyan/code/tensorflow/tf-fashion-mnist-sample/train.py
        ```

    ![Enter the Notebook](../baize/images/baize-05.png)

4. **Submit a training job**:

    1. Create a single-node Tensorflow job under **Job Center** -> **Training Jobs**. Use the default image and the following command:

        ```bash
        python /home/jovyan/code/tensorflow/tf-fashion-mnist-sample/train.py
        ```

    2. Enable **Job Analysis (Tensorboard)** in the advanced settings and click **OK** to submit.

    3. When the job status changes to **Succeeded**, view the training curves and tune the job under **Job Analysis** in the left navigation.

        ![View the job](../baize/images/baize-07.png)

## Verify

The training job is **Succeeded**, the Loss/Accuracy curves are visible in Job Analysis, and the output dataset contains the model and logs, which means the training pipeline works end to end.

## Next step

To publish the trained model as an inference service, see [Create Model](../hydra/models/index.md) and then deploy it in [LLM Studio](deploy-model.md).
For the complete usage of Notebooks (SSH access, idle shutdown, etc.), see [Create Notebook](../baize/developer/notebooks/index.md) and [Create Job](../baize/developer/jobs/index.md).
