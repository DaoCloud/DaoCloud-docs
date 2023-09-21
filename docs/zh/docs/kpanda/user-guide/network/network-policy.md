# 网络策略

网络策略（NetworkPolicy）可以在 IP 地址或端口层面（OSI 第 3 层或第 4 层）控制网络流量。容器管理模块目前支持创建基于 Pod 或命名空间的网络策略，支持通过标签选择器来设定哪些流量可以进入或离开带有特定标签的 Pod。

有关网络策略的更多详情，可参考 Kubernetes 官方文档[网络策略](https://kubernetes.io/zh-cn/docs/concepts/services-networking/network-policies/)。

## 创建网络策略

目前支持通过 YAML 和表单两种方式创建网络策略，这两种方式各有优劣，可以满足不同用户的使用需求。

通过 YAML 创建步骤更少、更高效，但门槛要求较高，需要熟悉网络策略的 YAML 文件配置。

通过表单创建更直观更简单，根据提示填写对应的值即可，但步骤更加繁琐。

### YAML 创建

1. 在集群列表中点击目标集群的名称，然后在左侧导航栏点击`容器网络`->`网络策略`->`YAML 创建`。

    ![路径](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/networkpolicy01.png)

2. 在弹框中输入或粘贴事先准备好的 YAML 文件，然后在弹框底部点击`确定`。

    ![yaml](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/networkpolicy02.png)

### 表单创建

1. 在集群列表中点击目标集群的名称，然后在左侧导航栏点击`容器网络`->`网络策略`->`创建策略`。

    ![路径](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/networkpolicy03.png)

2. 填写基本信息。

    名称和命名空间在创建之后不可更改。

    ![基本信息](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/networkpolicy04.png)

3. 填写策略配置。

    策略配置分为入流量策略和出流量策略。如果源 Pod 想要成功连接到目标 Pod，源 Pod 的出流量策略和目标 Pod 的入流量策略都需要允许连接。如果任何一方不允许连接，都会导致连接失败。

    - 入流量策略：点击`➕`开始配置策略，支持配置多条策略。多条网络策略的效果相互叠加，只有同时满足所有网络策略，才能成功建立连接。

        ![ingress](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/networkpolicy05.png)

    - 出流量策略

        ![egress](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/networkpolicy06.png)

## 查看网络策略

1. 在集群列表中点击目标集群的名称，然后在左侧导航栏点击`容器网络`->`网络策略`，点击网络策略的名称。

    ![路径](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/networkpolicy07.png)

2. 查看该策略的基本配置、关联实例信息、入流量策略、出流量策略。

    ![详情](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/networkpolicy08.png)

!!! info

    在关联实例页签下，支持查看实例监控、日志、容器列表、YAML 文件、事件等。

    ![查看实例信息](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/networkpolicy09.png)

## 更新网络策略

有两种途径可以更新网络策略。支持通过表单或 YAML 文件更新网络策略。

- 在网络策略列表页面，找到需要更新的策略，在右侧的操作栏下选择`更新`即可通过表单更新，选择`编辑 YAML` 即可通过 YAML 更新。

    ![更新](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/networkpolicy10.png)

- 点击网络策略的名称，进入网络策略的详情页面后，在页面右上角选择`更新`即可通过表单更新，选择`编辑 YAML` 即可通过 YAML 更新。

    ![更新](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/networkpolicy11.png)

## 删除网络策略

有两种途径可以删除网络策略。支持通过表单或 YAML 文件更新网络策略。

- 在网络策略列表页面，找到需要更新的策略，在右侧的操作栏下选择`更新`即可通过表单更新，选择`编辑 YAML` 即可通过 YAML 删除。

    ![删除](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/networkpolicy12.png)

- 点击网络策略的名称，进入网络策略的详情页面后，在页面右上角选择`更新`即可通过表单更新，选择`编辑 YAML` 即可通过 YAML 删除。

    ![删除](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/networkpolicy13.png)
