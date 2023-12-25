# 实现 DCE4 到 DCE5 应用的一键转换

本节将以无状态负载 nginx 为例介绍如何通过多云编排界面实现 DCE4 到 DCE5 应用的一键转换，

## 前提条件

- 容器管理模块接入集群厂商为 DaoCloud DCE 的集群，可参考[已接入 Kubernetes 集群](../cluster.md)，且能够访问集群的 UI 界面。
- DCE4 集群中工作负载能够正常运行。

## 一键转移

1. 进入 __多云实例-工作负载管理__ ，点击 __接入集群__ 选择将 DCE4 集群接入多云实例。

    ![接入集群](https://docs.daocloud.io/daocloud-docs-images/docs/kairship/images/conversion01.png)

2. 进入 __多云工作负载-无状态负载__ ，点击立即体验，选中目标应用，将会自动勾选其关联的 service，同时相关联的配置项、密钥也会被同步转换。

    ![一键转移](https://docs.daocloud.io/daocloud-docs-images/docs/kairship/images/conversion02.png)

    ![同步转换](https://docs.daocloud.io/daocloud-docs-images/docs/kairship/images/conversion03.png)

3. 转换成功后点击更新，选择目标部署集群，并开启自动传播（将默认自动检测多云工作负载配置中依赖的 ConfigMap 与 Secret 等资源，并实现自动传播）。

    ![更新nginx](https://docs.daocloud.io/daocloud-docs-images/docs/kairship/images/conversion04.png)

4. 更新 service 的部署策略，选择部署集群。

    ![更新部署策略](https://docs.daocloud.io/daocloud-docs-images/docs/kairship/images/conversion05.png)

5. 验证多云 nginx 是否运行成功：在两个集群内 Pod 都成功运行，并且可以正常访问。

    ![验证是否成功](https://docs.daocloud.io/daocloud-docs-images/docs/kairship/images/conversion06.png)

6. DCE4 集群内的工作负载 nginx 不受影响，应用不断服。

    ![不断服](https://docs.daocloud.io/daocloud-docs-images/docs/kairship/images/conversion07.png)
