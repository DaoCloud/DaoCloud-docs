# 快速入门

本文提供了简单的操作手册以便用户使用 DCE 5.0 AI Lab 进行数据集、Notebook、任务训练的整个开发、训练流程。

点击 **数据管理** -> **数据集列表** ，选择 **创建** ，分别创建以下三个数据集。

## 准备数据集

### 数据集：训练代码

- 代码数据源：[https://github.com/d-run/drun-samples.git](https://github.com/d-run/drun-samples.git)，主要是一个简单的 Tensorflow 代码。
- 国内慢可以使用 gitee 加速：[https://gitee.com/samzong_lu/training-sample-code.git](https://gitee.com/samzong_lu/training-sample-code.git)
- 代码路径在 `tensorflow/tf-fashion-mnist-sample` 下。

![训练代码的数据集](../images/baize-01.png)

!!! note

    目前仅支持读写模式为 `ReadWriteMany` 的 `StorageClass`，请使用 NFS 或者推荐的 [JuiceFS](https://juicefs.com/zh-cn/)。

### 数据集：训练数据

本次训练使用的数据：[https://github.com/zalandoresearch/fashion-mnist.git](https://github.com/zalandoresearch/fashion-mnist.git)，
这是 Fashion-MNIST 数据集。

国内慢可以使用 Gitee 加速：[https://gitee.com/samzong_lu/fashion-mnist.git](https://gitee.com/samzong_lu/fashion-mnist.git)

![训练数据的数据集](../images/baize-02.png)

### 数据集：空 PVC

AI Lab 支持将 PVC 作为数据集的数据源类型，所以你可以创建空数据集，用于存储训练结束的模型和日志。

![空pvc数据集](../images/baize-03.png)

## 创建并使用 Notebook

准备开发环境，点击导航栏的 **Notebooks** ，点击 **创建** 。将上一步中创建的三个数据集进行关联，挂载路径请参照下图填写：

![挂载路径](../images/baize-04.png)

等待 Notebook 创建成功，点击列表中的访问地址，进入 Notebook。并在 Notebook 的终端中执行以下命令进行任务训练。

!!! note

    脚本使用 Tensorflow，需要在 Notebook 中执行 `pip install -r requirements.txt` 安装。 

    ```shell
    python /home/jovyan/code/tensorflow/tf-fashion-mnist-sample/train.py
    ```

![进入 notebook](../images/baize-05.png)

## 创建训练任务

1. 点击导航栏的 **任务中心** -> **训练任务** ，创建一个 `Tensorflow` 单机任务
1. 先填写基本参数后，点击 **下一步**
1. 在任务资源配置中，正确配置任务资源后，点击 **下一步**

    ![任务资源配置](../images/baize-06.png)

    - 镜像地址填写：`release.daocloud.io/baize/jupyter-tensorflow-full:v1.8.0-baize`
    - Command：`python`
    - Arguments：`/home/jovyan/code/tensorflow/tf-fashion-mnist-sample/train.py`

    !!! note

        数据集或模型较大时，建议开启 GPU 配置。

1. 在高级配置中，启用 **任务分析（Tersorboard）** ，点击 **确定** 。

    ![高级配置](../images/enable-analy.png)

1. 返回训练任务列表，等到状态变为 **成功** 。点击列表右侧的 **┇** ，可以查看详情、克隆任务、更新优先级、查看日志和删除等操作。

    ![提交训练任务](../images/othera.png)

成功创建任务后，在左侧导航栏点击 **任务分析** ，可以查看任务状态并对任务训练进行调优。

![查看任务](../images/baize-07.png)
