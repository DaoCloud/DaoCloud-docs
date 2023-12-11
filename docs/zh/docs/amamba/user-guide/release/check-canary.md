# 查看金丝雀发布任务

创建灰度发布任务并关联工作负载后，修改工作负载的镜像、资源配置、启动参数等使得容器组重启时，会自动触发灰度发布任务更新版本，并按照定义好的发布规则进行流量调度。

本文主要介绍查看金丝雀发布任务时涉及到的相关操作，例如查看任务详情、更新版本、更新发布任务、回滚版本等。

## 查看任务详情

1. 进入**应用工作台**模块，在左侧导航栏点击**灰度发布**，点击目标任务的名称。

    ![点击名称](https://docs.daocloud.io/daocloud-docs-images/docs/amamba/images/checkcanary01.png)

2. 查看灰度发布任务详情页面。

    - **基本信息**区域：查看任务的名称、状态、发布类型、发布对象等信息。

    - **灰度进度**区域：以可视化的形式展示灰度发布任务的执行进度，可以直观地了解任务目前执行到了哪一步，以及执行的状态如何。

    - **版本信息**区域：

        - 主要版本：展示当前版本以及金丝雀版本信息。
        - 历史版本：展示历史版本记录。

          ![详情页](https://docs.daocloud.io/daocloud-docs-images/docs/amamba/images/checkcanary02.png)

## 更新版本

发布对象更新版本后，会自动触发灰度发布任务。

1. 点击目标任务的名称，然后在右上角点击**更新版本**。

    ![详情页](https://docs.daocloud.io/daocloud-docs-images/docs/amamba/images/checkcanary02.png)

2. 设置金丝雀发布的镜像。

    ![镜像地址](https://docs.daocloud.io/daocloud-docs-images/docs/amamba/images/checkcanary03.png)

3. 应用更新成功后会触发一次新的灰度发布过程。

    ![自动触发](https://docs.daocloud.io/daocloud-docs-images/docs/amamba/images/checkcanary04.png)

## 更新发布任务

通过更新发布任务，可以修改灰度发布过程的流量调度策略。

1. 在**灰度发布任务** 详情页面，在页面右上角点击 **ⵗ** 并选择**更新发布任务**。

    ![详情页](https://docs.daocloud.io/daocloud-docs-images/docs/amamba/images/checkcanary02.png)

2. 调整发布规则并点击**确定**。

    ![修改发布规则](https://docs.daocloud.io/daocloud-docs-images/docs/amamba/images/checkcanary05.png)

## 回滚

支持查看以往发布过的历史版本，可以一键回滚到之前的某个版本。

1. 在**灰度发布任务**详情页面，点击**历史版本** 标签。

    ![点击历史版本](https://docs.daocloud.io/daocloud-docs-images/docs/amamba/images/checkcanary06.png)

2. 选择目标版本，点击**回滚**。

    ![回滚](https://docs.daocloud.io/daocloud-docs-images/docs/amamba/images/checkcanary07.png)

3. 回滚成功后会触发一次新的灰度发布过程。

    ![查看灰度进度](https://docs.daocloud.io/daocloud-docs-images/docs/amamba/images/checkcanary08.png)

## 其他操作说明

| 操作 |  |
| --- | --- |
| 继续发布 | 对于正在进行中或者暂停的金丝雀发布任务，继续发布可以推动金丝雀发布过程进入到下一阶段的发布。 |
| 发布 | 对于正在进行中或者暂停的金丝雀发布任务，发布可以推动金丝雀发布过程直接完成发布，将金丝雀版本更新为稳定版本。 |
| 终止发布 | 对于正在进行中或者暂停的金丝雀发布任务，终止发布会暂停当前所有步骤，并回滚到稳定版本。 |