# 管理 Helm 仓库

Helm 仓库是用来存储和发布 Chart 的存储库。Helm 应用模块支持通过 HTTP(s) 协议来访问存储库中的 Chart 包。系统默认内置了下表所示的 4 个 Helm 仓库以满足企业生产过程中的常见需求。

| 仓库      | 描述                                                         | 示例  |
| --------- | ------------------------------------------------------------ | ------------ |
| partner   | 由生态合作伙伴所提供的各类优质特色 Chart                     | tidb         |
| system    | 系统核心功能组件及部分高级功能所必需依赖的 Chart，如必需安装 insight-agent 才能够获取集群的监控信息| Insight      |
| addon     | 业务场景中常见的 Chart                                       | cert-manager |
| community | Kubernetes 社区较为热门的开源组件 Chart                      | Istio        |

除上述预置仓库外，您也可以自行添加第三方 Helm 仓库。本文将介绍如何添加、更新第三方 Helm 仓库。

## 前提条件

- 容器管理模块[已接入 Kubernetes 集群](../clusters/integrate-cluster.md)或者[已创建 Kubernetes 集群](../clusters/create-cluster.md)，且能够访问集群的 UI 界面

- 已完成一个[命名空间的创建](../namespaces/createns.md)、[用户的创建](../../../ghippo/user-guide/access-control/user.md)，并为用户授予 [NS Admin](../permissions/permission-brief.md#ns-admin) 或更高权限 ，详情可参考[命名空间授权](../permissions/cluster-ns-auth.md)。

- 如果使用私有仓库，当前操作用户应拥有对该私有仓库的读写权限。

## 引入第三方 Helm 仓库

下面以 Kubevela 公开的镜像仓库为例，引入 Helm 仓库并管理。

1. 找到需要引入第三方 Helm 仓库的集群，点击集群名称，进入 __集群详情__ 。

    ![集群详情](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/crd01.png)

2. 在左侧导航栏，依次点击 __Helm 应用__ -> __Helm 仓库__ ，进入 Helm 仓库页面。

    ![helm仓库](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/helmrepo01.png)

3. 在 Helm 仓库页面点击 __创建仓库__ 按钮，进入创建仓库页面，按照下表配置相关参数。

    - 仓库名称：设置仓库名称。最长 63 个字符，只能包含小写字母、数字及分隔符 __-__ ，且必须以小写字母或数字开头并结尾，例如 kubevela
    - 仓库地址：用来指向目标 Helm 仓库的 http（s）地址。例如 <https://charts.kubevela.net/core>
    - 认证方式：连接仓库地址后用来进行身份校验的方式。对于公开仓库，可以选择 __None__ ，私有的仓库需要输入用户名/密码以进行身份校验
    - 标签：为该 Helm 仓库添加标签。例如 key: repo4；value: Kubevela
    - 注解：为该 Helm 仓库添加注解。例如 key: repo4；value: Kubevela
    - 描述：为该 Helm 仓库添加描述。例如：这是一个 Kubevela 公开 Helm 仓库

    ![填写参数](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/helmrepo02.png)

4. 点击 __确定__ ，完成 Helm 仓库的创建。页面会自动跳转至 Helm 仓库列表。

    ![确定](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/helmrepo03.png)

## 更新 Helm 仓库

当 Helm 仓库的地址信息发生变化时，可以更新 Helm 仓库的地址、认证方式、标签、注解及描述信息。

1. 找到待更新仓库所在的集群，点击集群名称，进入 __集群详情__ 。

    ![集群详情](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/crd01.png)

2. 在左侧导航栏，依次点击 __Helm 应用__ -> __Helm 仓库__ ，进入 Helm 仓库列表页面。

    ![helm仓库](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/helmrepo01.png)

3. 在仓库列表页面找到需要更新的 Helm 仓库，在列表右侧点击 __⋮__ 按钮，在弹出菜单中点击 __更新__ 。

    ![点击更新](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/helmrepo04.png)

4. 在 __编辑 Helm 仓库__ 页面进行更新，完成后点击 __确定__ 。

    ![确定](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/helmrepo05.png)

5. 返回 Helm 仓库列表，屏幕提示更新成功。

## 删除 Helm 仓库

除了引入、更新仓库外，您也可以将不需要的仓库删除，包括系统预置仓库和第三方仓库。

1. 找到待删除仓库所在的集群，点击集群名称，进入 __集群详情__ 。

    ![集群详情](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/crd01.png)

2. 在左侧导航栏，依次点击 __Helm 应用__ -> __Helm 仓库__ ，进入 Helm 仓库列表页面。

    ![helm仓库](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/helmrepo01.png)

3. 在仓库列表页面找到需要更新的 Helm 仓库，在列表右侧点击 __⋮__ 按钮，在弹出菜单中点击 __删除__ 。

    ![点击删除](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/helmrepo07.png)

4. 输入仓库名称进行确认，点击 __删除__ 。

    ![确认删除](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/helmrepo08.png)

5. 返回 Helm 仓库列表，屏幕提示删除成功。
