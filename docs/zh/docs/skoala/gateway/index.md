# 微服务网关

微服务网关支持多租户实例的高可用架构，兼容多种模式微服务的统一网关接入能力。本页介绍如何管理微服务网关实例。

## 创建微服务网关

创建微服务网关的步骤如下：

1. 在左侧导航栏点击`云原生网关`，然后在右上角点击`创建网关`。

    ![进入创建页面](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/gw-create01.png)

2. 参考以下说明填写基本信息

    - 网关名称：长度不超过 63 个字符，支持字母、数字、连字符并且必须以字母或数字字符开头及结尾。名称在网关创建完成后不可更改。
    - 部署集群：选择将网关部署在哪个集群。

        > 如果可选列表中没有出现目标集群，可以去容器管理模块中[接入](../../kpanda/user-guide/clusters/integrate-cluster.md)或[创建](../../kpanda/user-guide/clusters/create-cluster.md)集群并通过全局管理模块将该[集群或其中的某个命名空间绑定到当前工作空间](../../ghippo/user-guide/workspace/quota.md#_4)。

    - 命名空间：选择将网关部署在哪个命名空间。一个命名空间中只能部署一个网关。
    - 安装环境检测：选择集群和命名空间后，系统会自动检测安装环境。未通过检测时，页面会给出原因和操作建议，根据页面提示操作即可。
    - 管辖命名空间：设置新建的网关可以管辖哪些命名空间。默认管辖网关所在的命名空间。支持同时管辖多个命名空间。同一个命名空间不能被两个网关同时管辖。

    ![填写基本配置](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/gw-create02.png)

3. 参考以下说明填写配置信息

    === "服务配置"

        - 集群内部访问：只能在同一集群的内部访问服务。

            ![填写基本配置](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/gw-create03.png)

        - 节点访问：通过节点的 IP 和静态端口访问服务，支持从集群外部访问服务。
        
            外部流量策略：`Cluster` 指流量可以转发到集群中其他节点上的 Pod；`Local`指流量只能转发到本节点上的 Pod。

            ![填写基本配置](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/gw-create04.png)

        - 负载均衡器：使用云服务提供商的负载均衡器使得服务可以公开访问

            - 外部流量策略：`Cluster` 指流量可以转发到集群中其他节点上的 Pod；`Local`指流量只能转发到本节点上的 Pod
            - 负载均衡类型：MetalLB 或其他
            - MetalLB IP 池：支持自动选择或指定 IP 池子
            - 负载均衡器 IP 地址：支持自动选择或指定 IP

            ![填写基本配置](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/gw-create05.png)

    === "资源配置"

        为当前网关配置多少控制节点和工作节点。单副本存在不稳定性，需谨慎选择。

        ![填写基本配置](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/gw-create06.png)

    === "高级配置"

        - 控制节点：设置为控制节点（contour）配置多少 CPU 和内存资源
        - 工作节点：设置为工作节点 （envoy）配置多少 CPU 和内存资源

        ![填写高级配置](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/gw-create07.png)

4. 参考以下信息填写高级配置

    - 日志配置：设置工作节点 （envoy）的日志级别和 Pod 的日志级别
    - 更新机制：`重新创建`指删除原来的网关并新建一个网关，`滚动更新`指不删除网关，而是滚动式地更新网关相关的 Pod
    - 网关前置代理层数：请求从客户端到网关中途需要经过几个代理端点。需要根据实际情况填写。例如`客户端-Nginx-网关`的代理层数为 1，因为中间只经过 1 个 Nginx 代理端点。
    - 网关链路：启用后，可以根据通过网关进行的请求生成链路信息并发送给可观测模块进行数据采集。

    ![填写高级配置](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/gw-create08.png)

5. 参考以下信息填写插件配置（选填），最后在页面右下角点击`确认`即可。

    选择是否启用`全局限流`插件。

    需要事先在插件中心接入插件，或在当前页面点击蓝色文字跳转到相应页面接入创建。

    ![填写高级配置](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/gw-create09.png)

!!! note

    系统会自动返回云原生网关列表页面，在右侧可以执行[更新网关](./api/update-api.md)或[删除网关](./api/update-api.md#api_2)的操作。

    ![确认所填信息](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/gw-create10.png)

## 查看微服务网关

可以在`概览`页面查看网关的详细信息，包括名称、部署位置、网关运行状态、服务入口方式、控制节点/工作节点的健康状态、API、插件等信息。

### 进入网关详情页面

在`网关列表`页面，选择目标网关的名称，即可进入网关概览页面`。

![概览页面](https://docs.daocloud.io/daocloud-docs-images/docs/skoala/ms-gateway/gateway/imgs/overview.png)

### 网关详情

网关详情分为：基本信息、网络信息、TOP10 热门 API 情况、资源情况、资源负载、插件信息等部分。

部分数据的说明如下：

<!--
- 手工服务接入数：指在`服务列表`页面通过`添加服务`手工添加到当前网关的服务数量。
- 自动服务接入数：指在`服务列表`页面通过`纳管服务`自动添加到当前网关的服务数量。
- 域名管理：指当前网关下的域名数量。
- API 数量：指当前网关中使用的 API 数量。
-->
- 控制/工作节点实例数：显示节点实例的总数和健康状况。`/`左侧的数字表示当前在线的实例数，右侧的数字表示节点实例总数。

    - 如果在线节点`/左侧数字`等于全部应在线节点`/右侧数字`，则显示为绿色。
    - 如果在线节点`/左侧数字`小于全部应在线节点`/右侧数字`，则显示为红色。

- Top 10 APIs：按照 API 响应代码 2xx、4xx、5xx 的数量由高到低排列的前 10 个 API，默认按照响应代码 200 的数量降序排列。可查看过去 15 分钟、过去 1 小时、过去 24 小时的数据。
- 资源负载：以折线图的形式显示网关控制节点和工作节点在过去 1 小时内或过去 3 小时内的 CPU 使用情况和 Memory 使用情况。
- 插件信息：显示当前网关的插件启停情况以及其他的可用插件。

### 相关操作

除了查看网关详情，您还可以通过网关详情页面进行更新网关配置、删除网关等操作。

- 更新网关：在页面顶部点击`编辑`可以跳转到更新网关配置的页面，具体步骤参见[更新网关配置](./api/update-api.md)。
- 删除网关：在页面顶部点击 `⋯` 后选择`删除`可以跳转到删除网关的页面，具体步骤参见[删除网关](./api/update-api.md#api_2)。
<!--- 管理 API：在“网关数据”部分点击“API 数量”可以进入 API 列表，进行增删改查等操作。-->

## 更新微服务网关

微服务网关支持多租户实例的高可用架构，兼容多种模式微服务的统一网关接入能力。

有两种方式可以更新网关配置。

- 在`微服务网关列表`页选择需要更新的网关实例，在实例右侧点击 `⋯` 并选择`编辑`。

    ![更新网关](https://docs.daocloud.io/daocloud-docs-images/docs/skoala/ms-gateway/gateway/imgs/update.png)

- 点击网关名称进入进入概览页面后，在右上角点击`编辑`。

    ![更新网关](https://docs.daocloud.io/daocloud-docs-images/docs/skoala/ms-gateway/gateway/imgs/update-gateway.png)

## 删除微服务网关

微服务网关支持多租户实例的高可用架构，兼容多种模式微服务的统一网关接入能力。

删除网关同样也有两种方式。为保证服务不受影响，删除网关之前需要释放到网关中全部路由的 API。

!!! danger

    网关删除后不可恢复，请谨慎操作。

- 在`微服务网关列表`页选择需要移除的网关实例，在实例右侧点击 `⋯` 并选择`删除`。

    ![移除网关](https://docs.daocloud.io/daocloud-docs-images/docs/skoala/ms-gateway/gateway/imgs/delete.png)

- 点击网关名称进入进入概览页面后，在右上角 `⋯` 并选择`删除`。

    ![移除网关](https://docs.daocloud.io/daocloud-docs-images/docs/skoala/ms-gateway/gateway/imgs/delete-gateway.png)
