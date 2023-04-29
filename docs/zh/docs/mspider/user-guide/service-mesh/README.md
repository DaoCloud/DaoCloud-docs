---
hide:
  - toc
---

# 创建托管/专有网格

DCE 5.0 服务网格支持 3 种网格：

- **托管网格** 完全托管在 DCE 5.0 服务网格内。这种网格将核心控制面组件从工作集群中分离，控制面可以部署到一个独立的集群中，能够对同一网格中的多集群服务进行统一治理。
- **专有网格** 采用 Istio 传统结构，仅支持一个集群，集群内设有专门的控制面。
- **外接网格** 指的是可以将企业现成的网格接入到 DCE 5.0 服务网格中进行统一管理。参见[创建外接网格](external-mesh.md)。

创建托管网格/专有网格的步骤如下：

1. 在服务网格列表页面的右上角，点击`创建网格`。

    ![创建网格](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/images/servicemesh01.png)

2. 选择`托管网格`或`专有网格`，填写基本信息后点击`下一步`。

    - 网格名称：以小写字母开头，由小写字母、数字、中划线 (-) 组成，且不能以中划线 (-) 结尾
    - Istio 版本：如果是托管网格，所有被纳管集群的 Istio 都将使用此版本。
    - 控制面集群：用于运行网格管理面的集群，附带一个刷新图标和`创建集群`按钮。点击`创建集群`将跳转至`容器管理`平台创建新集群，创建完成后返回本页面，点击刷新图标可更新集群列表。
    - 控制面地址：输入控制面的 IP 地址。
    - 网格组件仓库：输入包含数据面组件镜像的镜像仓库地址，例如 `release.daocloud.io/mspider`。
  
    ![基本信息](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/images/create-mesh-config.png)

3. 系统设置。配置是否开启可观测性，设置网格规模后点击`下一步`。

    ![系统设置](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/images/mesh-sys-set.png)

4. 治理设置。设置出站流量策略、位置感知负载均衡、请求重试等。参阅[请求重试参数说明](./params.md#max-retries)。

    ![治理设置](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/images/gov-set.png)

5. 边车设置。设置全局边车、资源限制、日志后点击`确定`。参阅[日志级别说明](./params.md#_2)。

    ![边车设置](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/images/create-sidecar-set.png)

6. 自动返回网格列表，新创建的网格默认位于第一个，一段时间后状态将从`创建中`变为`运行中`。点击右侧的 `...` 可以编辑网格基本信息、添加集群等。

    ![网格列表](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/images/create-list.png)

!!! info

    创建托管网格后，还未接入任何托管的集群，此时网格处于`未就绪`状态。
    用户可以[添加集群](../cluster-management/README.md)，等待集群接入完成后，选择需要服务治理的集群接入。
