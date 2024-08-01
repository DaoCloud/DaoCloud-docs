# API 管理

微服务网关支持对网关实例的 API 进行全生命周期管理，包括 API 的添加、更新和删除。

## 添加 API

**前提条件**

- 有可选的域名，可参考[域名管理](../domain/index.md)创建域名。
- 如果 API 的目标服务为后端服务，则需要确保有可选的后端服务，可参考通过[手动](../service/manual-integrate.md)或[自动](../service/auto-manage.md)方式接入服务。

创建 API 的步骤如下：

1. 点击网关名称进入网关概览页面，然后在左侧导航栏点击 __API 管理__ ，在页面右上角点击 __添加 API__ 。

    ![进入添加页面](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/gateway/api/images/add-api-01.png)

2. 参考下方说明填写基本配置。

    配置分为基本配置和策略配置和安全配置三部分。填写基本配置信息时需要注意：

    - API 名称：包含小写字母、数字和以及特殊字符(- .)，不能以特殊字符开头和结尾。
    - API 分组：选择 API 所属的分组组名。如果输入不存在的分组名称，则自动创建一个新的分组。
    - 关联域名：填写关联域名后，可以通过`域名 + 端口号`的方式访问 API。找不到域名时可以添加新域名，可参考[添加域名](../domain/index.md)。
    - 匹配规则：只允许符合该规则的请求通过。如果设置了多条规则，需要同时满足所有规则才能放行。如果添加了请求头，则需要在访问该 API 时添加相应的请求头。
    - 请求方法：选择 HTTP 协议的请求方式。有关各种请求方式的详细说明，可参考 W3C 的官方文档[方式定义](https://www.rfc-editor.org/rfc/rfc9110.html#name-method-definitions)。
    - 目标服务：选择将请求直接发送到后端服务，或者重定向到其他服务，或者直接返回 HTTP 状态码。
    - 如果选择后端服务，则需要配置权重。权重越大，网关向其分发的流量就越多。

    ![配置信息](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/gateway/api/images/config.png)

3. 参考下方说明填写策略配置（选填）。

    支持 12 种 API 策略：负载均衡、路径改写、超时配置、重试机制、请求头重写、响应头重写、Websocket、本地限流、健康检查、cookie 重写、全局限流、访问黑白名单。有关各项策略的配置说明，可参考[API 策略配置](api-policy.md)。

    ![配置策略](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/gateway/api/images/policy01.png)

4. 参考下方说明填写安全配置（选填）。

    - JWT 认证：应用域名配置或不启用
    - 安全认证：应用域名配置或自定义

    ![安全配置](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/gateway/api/images/policy02.png)

5. 在页面右下角点击 __保存__ （不上线）。如果点击 __保存并上线__ 则可以直接上线 API。

    点击 __确定__ 后，如果所有配置都正常，右上角会弹出 __创建网关 API 成功__ 的提示信息。可以在 __API 管理__ 页面查看新建的 API。

    ![创建成功](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/gateway/api/images/result.png)

6. API 上线

    API 创建成功后，**默认处于下线状态，此时无法访问**。需要将 API 调整为 __上线__ ，才能正常访问。API 上线有两种方式。

    - 在 API在 __API 管理__ 页面找到需要更新的 API，在该 API 的右侧点击 __ⵗ__ 选择 __API 上线__ 。

        ![API 上线](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/gateway/api/images/online.png)

    - 点击 API 名称进入 API 详情页，在页面右上角点击 __ⵗ__ 并选择 __API 上线__ 。

        ![API 上线](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/gateway/api/images/online1.png)

!!! info

    点击 API 名称进入 API 详情，可查看 API 的详细配置信息，例如上下线状态、域名、匹配规则、目标服务、策略配置等。

    ![API 上线](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/gateway/api/images/online1.png)

## 更新 API

可以通过两种方式更新 API 的基础配置、策略配置和安全配置。

- 在 __API 管理__ 页面找到需要更新的 API，在该 API 的右侧点击 __ⵗ__ 选择 __修改基础配置__ 、 __修改策略配置__ 或 __修改安全配置__ 。

    ![在列表页更新基础信息](https://docs.daocloud.io/daocloud-docs-images/docs/skoala/ms-gateway/api/imgs/update-api-1.png)

- 点击 API 名称进入 API 详情页，在页面右上角 __修改基础配置__ 、 __修改策略配置__ 或 __修改安全配置__ 。

    ![在详情页更新](https://docs.daocloud.io/daocloud-docs-images/docs/skoala/ms-gateway/api/imgs/update-api-2.png)

## 删除 API

微服务网关支持对网关实例的 API 进行全生命周期管理，包括 API 的添加、更新和移除。

可以通过两种方式移除 API。

!!! danger

    删除操作是不可逆的。无论 API 是否处于在线状态，删除后均立即失效并且不可恢复。

- 在 __API 管理__ 页面找到需要删除的 API，在该 API 的右侧点击 __ⵗ__ 并选择 __移除__ 。

    ![在列表页删除](https://docs.daocloud.io/daocloud-docs-images/docs/skoala/ms-gateway/api/imgs/delete-api-1.png)

- 点击 API 名称进入 API 详情页，在页面右上角点击 __ⵗ__ 操并选择 __移除__ 。

    ![在详情页删除](https://docs.daocloud.io/daocloud-docs-images/docs/skoala/ms-gateway/api/imgs/delete-api-2.png)
