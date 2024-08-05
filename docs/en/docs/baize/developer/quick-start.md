---
hide:
  - toc
---

# Quick Start

This document provides a simple guide for users to use the DCE 5.0 Intelligent Engine platform for
the entire development and training process of datasets, Notebooks, and job training.

1. Click **Data Management** -> **Datasets** in the navigation bar,
   then click **Create**. Create three datasets as follows:

    - Code: [https://github.com/d-run/drun-samples](https://github.com/d-run/drun-samples/tree/main/tensorflow/tf-fashion-mnist-sample)
        - For faster access in China, use Gitee: [https://gitee.com/samzong_lu/training-sample-code.git](https://gitee.com/samzong_lu/training-sample-code.git)
    - Data: [https://github.com/zalandoresearch/fashion-mnist](https://github.com/zalandoresearch/fashion-mnist)
        - For faster access in China, use Gitee: [https://gitee.com/samzong_lu/fashion-mnist.git](https://gitee.com/samzong_lu/fashion-mnist.git)
    - Empty PVC: Create an empty PVC to output the trained model and logs after training.

    !!! note

        Currently, only `StorageClass` with `ReadWriteMany` mode is supported. Please use NFS or the recommended [JuiceFS](https://juicefs.com/zh-cn/).

    <!-- add screenshot later -->

    <!-- add screenshot later -->

    <!-- add screenshot later -->

2. Prepare the development environment by clicking on **Notebooks** in the navigation bar,
   then click **Create**. Associate the three datasets created in the previous step and
   fill in the mount paths as shown in the image below:

    <!-- add screenshot later -->

3. Wait for the Notebook to be created successfully, click the access link in
   the list to enter the Notebook. Execute the following command in the Notebook terminal to start the job training.

    ```shell
    python /home/jovyan/code/tensorflow/tf-fashion-mnist-sample/train.py
    ```

    <!-- add screenshot later -->

4. Click **Job Center** -> **Jobs** in the navigation bar, create a `Tensorflow Single` job.
   Refer to the image below for job configuration and enable the **Job Analysis (Tensorboard)** feature.
   Click **Create** and wait for the status to complete.

    - Image address: `release.daocloud.io/baize/jupyter-tensorflow-full:v1.8.0-baize`
    - Command: `python`
    - Arguments: `/home/jovyan/code/tensorflow/tf-fashion-mnist-sample/train.py`

    !!! note

        For large datasets or models, it is recommended to enable GPU configuration in the resource configuration step.

    <!-- add screenshot later -->

5. In the job created in the previous step, you can click the specific job analysis to
   view the job status and optimize the job training.

    <!-- add screenshot later -->
