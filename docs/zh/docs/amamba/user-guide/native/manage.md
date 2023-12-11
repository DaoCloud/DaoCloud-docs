# 原生应用管理

[创建好原生应用](native-app.md)之后，可以根据需要查看应用详情或更新应用配置。

## 查看应用详情

在**应用工作台**->**概览**页面，点击**原生应用**页签，点击原生应用的名称。

![entry](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/amamba/images/native-app01.png)

- 查看应用名称、别名、描述信息、命名空间、创建时间等基本信息。

    ![basic](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/amamba/images/native-app02.png)

- 点击**应用资源**页签，可以查看原生应用下的工作负载、服务、路由等 K8s 资源信息。支持对各种资源进行编辑、删除操作。

    ![resource](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/amamba/images/native-app03.png)

- 点击**应用拓扑**页签，可以查看可视化的工作负载、容器、存储、配置与密钥等资源。

    ![topology](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/amamba/images/native-app04.png)

    - 支持查看资源的基本信息，可以跳转到**容器管理** 模块查看资源的详情：

        ![basic](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/amamba/images/native-app05.png)

    - 对可视化拓扑的节点颜色进行特殊处理，一些支持存在状态的资源可通过节点颜色来判断当前资源的健康程度：

        ![color](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/amamba/images/native-app06.png)

## 编辑原生应用基本信息

1. 点击原生应用的名称，然后在页面右上角点击 **ⵈ** 选择**编辑基本信息**。
2. 根据需要设置别名，或补充描述信息描述信息。

    ![color](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/amamba/images/native-app07.png)

## 查看原生应用 YAML

1. 点击原生应用的名称，然后在页面右上角点击 **ⵈ** 选择**查看YAML**。
2. 查看原生应用的清单文件。

    ![color](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/amamba/images/native-app08.png)
