# 服务网格组件资源自定义

本文介绍如何对通过[容器管理](../../../kpanda/user-guide/workloads/create-deployment.md)配置网格的[控制面组件](../../intro/comp-archi-ui/cp-component.md)资源。

## 前提条件

集群已被服务网格纳管，网格组件已正常安装；
登录账号具有全局管理集群及工作集群中命名空间 istio-system 的 `admin` 或 `editor` 权限；

## 自定义操作

以托管网格下工作集群上 `istiod` 为例，具体操作如下：

1. 服务网格下查看托管网格 nicole-dsm-mesh 的接入集群为 nicole-dsm-c2，如下图所示。

    ![接入集群](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/user-guide/mesh-config/images/meshrcfg01.png)

2. 点击集群名称，跳转至`容器管理`模块中集群页面，点击进入`工作负载` -> `无状态负载`页面查找 `istiod`；

    ![查找 istiod](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/user-guide/mesh-config/images/meshrcfg02.png)

3. 点击工作负载名称进入`容器配置` -> `基本信息`标签页；

    ![查看配额](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/user-guide/mesh-config/images/meshrcfg03.png)

4. 点击编辑按钮，修改 CPU 和内存配额，点击`下一步`、`确定`。

    ![修改配额](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/user-guide/mesh-config/images/meshrcfg04.png)

5. 查看该工作负载下的 Pod 资源信息，可见已变更.

    ![确认配额](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/user-guide/mesh-config/images/meshrcfg05.png)


