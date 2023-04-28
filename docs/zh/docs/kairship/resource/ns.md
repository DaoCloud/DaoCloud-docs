---
hide:
  - toc
---

# 多云命名空间

多云命名空间可以跨云、跨集群管理工作负载。目前提供了基于向导创建的方式。

本文以向导创建为例，参照以下步骤操作。

1. 进入某一个多云实例后，在左侧导航栏中，点击`资源管理` -> `多云命名空间`，点击右上角的`创建`按钮。

    ![点击创建按钮](https://docs.daocloud.io/daocloud-docs-images/docs/kairship/images/ns01.png)

2. 在`创建多云命名空间`页面中，输入名称，添加标签后，点击`确定`。

    ![填写表单](https://docs.daocloud.io/daocloud-docs-images/docs/kairship/images/ns02.png)

3. 返回多云命名空间列表，新创建的默认位于第一个。点击列表右侧的 `⋮`，可以编辑 YAML 和删除该命名空间。

    ![其他操作](https://docs.daocloud.io/daocloud-docs-images/docs/kairship/images/ns03.png)

    !!! note

        若要删除一个命名空间，需要先移除该命名空间下的所有工作负载，删除之后命名空间内的工作负载和服务都会受到影响，请谨慎操作。
