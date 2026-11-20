---
hide:
  - toc
---

# AI Lab 训练模型 - 用户

前面的教程用的是模型广场里的现成模型。如果要用自己的数据和代码训练模型，
可以在 [AI Lab](../baize/intro/index.md) 中完成数据集管理、Notebook 调试与分布式训练的完整流程。
本教程以 Tensorflow 训练 Fashion-MNIST 为例走通最小链路。

## 前提条件

- 已创建带 GPU 节点的工作集群，参见[创建工作集群](join-cluster.md)。
- 已用具有 AI Lab 权限的用户登录控制台，且工作空间已绑定命名空间。
- 集群中存在读写模式为 `ReadWriteMany` 的存储类（推荐 NFS 或 JuiceFS），供数据集挂载使用。

!!! note

    AI Lab（`baize`）在 manifest 中默认开启；若控制台未显示该模块，
    参阅[安装 AI Lab 组件](../baize/intro/install.md)。

## 操作步骤

1. **准备数据集**：在 **数据管理** -> **数据集** 中点击 **创建**，依次创建三个数据集：

    | 数据集 | 用途 | 数据源 |
    |---|---|---|
    | 训练代码 | 存放训练脚本 | `tensorflow/tf-fashion-mnist-sample`（[示例仓库](https://gitee.com/samzong_lu/training-sample-code.git)） |
    | 训练数据 | Fashion-MNIST 数据集 | [gitee.com/samzong_lu/fashion-mnist.git](https://gitee.com/samzong_lu/fashion-mnist.git) |
    | 空数据集（PVC） | 存放训练产物 | 空数据源，由平台分配 PVC |

    ![训练代码的数据集](../baize/images/baize-01.png)

2. **准备环境依赖**：在 **环境依赖** 中创建一个 CONDA 环境，预装 Tensorflow，
   预热成功后即可挂载到 Notebook 和训练任务，无需构建镜像：

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

    ![创建环境依赖](../baize/images/baize-08.png)

3. **Notebook 中调试脚本**：

    1. 在 **Notebooks** 中点击 **创建**，关联上述三个数据集（挂载路径参考创建页提示）并绑定 Tensorflow 环境。
    2. 创建成功后，点击列表中的访问地址进入 Notebook，在终端运行：

        ```bash
        python /home/jovyan/code/tensorflow/tf-fashion-mnist-sample/train.py
        ```

    ![进入 Notebook](../baize/images/baize-05.png)

4. **提交训练任务**：

    1. 在 **任务中心** -> **训练任务** 中创建一个 Tensorflow 单机任务，镜像用默认镜像，启用命令：

        ```bash
        python /home/jovyan/code/tensorflow/tf-fashion-mnist-sample/train.py
        ```

    2. 在高级配置中启用 **任务分析（Tensorboard）**，点击 **确定** 提交。

        ![提交训练任务](../baize/images/othera.png)

    3. 等任务状态变为 **成功** 后，在左侧导航 **任务分析** 中查看训练曲线并对任务调优。

        ![查看任务](../baize/images/baize-07.png)

## 验证结果

训练任务状态为 **成功**，且任务分析中能看到 Loss/Accuracy 曲线，输出数据集中已写入模型与日志，即表示训练链路贯通。

## 下一步

把训练好的模型发布为推理服务，参阅[创建模型](../hydra/models/index.md)后在[大模型服务平台](deploy-model.md)中部署；
了解 Notebook 的 SSH 访问、闲置关机等完整用法，参阅 [Notebook](../baize/developer/notebooks/index.md)与[训练任务](../baize/developer/jobs/index.md)。
