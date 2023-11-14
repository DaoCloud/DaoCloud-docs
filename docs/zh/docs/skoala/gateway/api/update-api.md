# 更新和删除 API

微服务网关支持对网关实例的 API 进行全生命周期管理，包括 API 的添加、更新和删除。

## 更新 API

可以通过两种方式更新 API 的基础配置、策略配置和安全配置。

- 在 `API 管理`页面找到需要更新的 API，在该 API 的右侧点击 `ⵗ` 选择`修改基础配置`、`修改策略配置`或`修改安全配置`。

    ![在列表页更新基础信息](https://docs.daocloud.io/daocloud-docs-images/docs/skoala/ms-gateway/api/imgs/update-api-1.png)

- 点击 API 名称进入 API 详情页，在页面右上角`修改基础配置`、`修改策略配置`或`修改安全配置`。

    ![在详情页更新](https://docs.daocloud.io/daocloud-docs-images/docs/skoala/ms-gateway/api/imgs/update-api-2.png)

## 删除 API

微服务网关支持对网关实例的 API 进行全生命周期管理，包括 API 的添加、更新和移除。

可以通过两种方式移除 API。

!!! danger

    注意：删除操作是不可逆的。无论 API 是否处于在线状态，删除后均立即失效并且不可恢复。

- 在 `API 管理`页面找到需要删除的 API，在该 API 的右侧点击 `ⵗ` 并选择`移除`。

    ![在列表页删除](https://docs.daocloud.io/daocloud-docs-images/docs/skoala/ms-gateway/api/imgs/delete-api-1.png)

- 点击 API 名称进入 API 详情页，在页面右上角点击 `ⵗ` 操并选择`移除`。

    ![在详情页删除](https://docs.daocloud.io/daocloud-docs-images/docs/skoala/ms-gateway/api/imgs/delete-api-2.png)
