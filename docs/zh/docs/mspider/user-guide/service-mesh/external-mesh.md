---
hide:
  - toc
---

# 创建外接网格

外接网格指的是可以将企业现成的网格接入到 DCE 5.0 服务网格中进行统一管理。

1. 在服务网格列表页面的右上角，点击`创建网格`。

    ![创建网格](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/images/servicemesh01.png)

1. 选择`外接网格`，填写网格基本信息后点击`下一步`。

    - 网格名称：以小写字母开头，由小写字母、数字、中划线(-)组成，且不能以中划线(-)结尾
    - 集群：用于运行网格管理面的集群，列表包含当前网格平台可以访问且状态正常的集群。
      点击`创建集群`将跳转至`容器管理`创建新集群，创建完成后返回本页面，点击刷新图标更新列表。
    - Istio 根命名空间：网格所在的 Istio 根命名空间。
    - 网格组件仓库：输入镜像仓库的 URL 地址。
  
    ![基本信息](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/images/external01.png)

1. 系统设置。设置可观测与否以及网格规模后点击`下一步`。

    ![系统设置](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/images/external02.png)

1. 治理设置。设置出站流量策略、位置感知负载均衡、请求重试等。

    ![治理设置](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/images/external03.png)

1. 边车设置。设置全局边车、资源限制、日志后点击`确定`。

    ![边车设置](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/images/external04.png)

1. 自动返回网格列表，新创建的网格默认位于第一个，一段时间后状态将从`创建中`变为`运行中`。点击右侧的 `...` 可以执行编辑、删除等操作。

    ![网格列表](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/images/external05.png)

下一步：[服务管理](../service-list/README.md)
