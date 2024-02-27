---
hide:
  - toc

---

# 服务管理

服务管理列出了当前网格下集群中已注入边车的所有服务，您可以基于命名空间筛选服务。

![服务列表](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/images/servicelist01.png)

服务网格对各集群的服务做了聚合处理，同一个命名空间下的同名服务将聚合为一个服务，这样有利于对跨集群协同服务进行统一的流量治理。

 __服务管理__ 会对列表内服务状态做 __诊断配置__ 检测，检测结果及含义如下：

- 正常：服务在各集群的 Pod 均已注入边车，并且各项设置完全相同
- 告警：该服务下工作负载的部分 Pod 没有注入边车
- 异常：当服务存在以下任一问题时，都会显示为 __异常__ 状态
    - 所有 Pod 均未注入边车
    - 服务在各集群的端口设置不一致
    - 服务在各集群的工作负载选择器标签设置不一致
    - 服务在各集群的访问方式不一致

!!! note

    各集群内同名服务应尽量保证各项配置完全一致，否则可能导致部分工作负载无法正常工作。

服务列表中也标注了来自其他微服务注册中心的服务，如下图所示。

![其他微服务注册中心的服务](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/images/servicelist06.png)

您可以点击某个服务名称，进入详情页查看各集群的服务地址、端口等具体信息，还可以在 __地址信息__ 页签中修改通信协议。

![地址信息](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/images/servicelist03.png)

请特别关注服务列表中 __诊断配置__ 这一列。当诊断信息为 __异常__ 时，光标悬浮在 __ⓘ__ 上将显示异常原因。异常状态会影响下一阶段的服务流量治理等网格相关能力。

![异常提示](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/images/servicelist04.png)

在服务列表右侧，点击 __⋮__ 选择相应的菜单项，可以跳转至流量治理和安全治理。

![菜单项](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/images/servicelist05.png)

关于如何创建和配置服务，请参阅[创建服务](../../../kpanda/user-guide/network/create-services.md)。
