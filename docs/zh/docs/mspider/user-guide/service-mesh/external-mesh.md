---
hide:
  - toc
---

# 创建外接网格

外接网格指的是可以将企业现成的网格接入到 DCE 5.0 服务网格中进行统一管理。

下文说明创建外接网格的步骤：

1. 在网格列表页面的右上角，点击 __创建网格__ 按钮，在下拉列表中选择 __创建外接网格__ 。

    ![创建外接网格](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/mspider/images/external01.png)

1. 系统会自动检测安装环境，检测成功后填写以下基本信息，点击 __确定__ 。

    - 网格名称：以小写字母开头，由小写字母、数字、中划线 (-) 组成，且不能以中划线 (-) 结尾
    - Istio 版本：所有被纳管集群的 Istio 都将使用此版本。
    - 集群：这是运行网格控制面的集群，集群下拉列表中展示了每个集群的版本及其健康状态。
    - 控制面入口方式：支持负载均衡和自定义。
    - 网格组件仓库：输入包含数据面组件镜像的镜像仓库地址，例如 __release-ci.daocloud.io/mspider__ 。
  
    ![基本信息](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/mspider/images/create-mesh02.png)

1. 自动返回网格列表，新创建的网格默认位于第一个，一段时间后状态将从 __创建中__ 变为 __运行中__ 。
   点击右侧的 __...__ ，可以编辑基本信息、添加集群、进入控制台以及删除等操作。

    ![网格列表](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/mspider/images/external02.png)

下一步：[服务管理](../service-list/README.md)
