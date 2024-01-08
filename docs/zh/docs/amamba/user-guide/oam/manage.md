# OAM 应用管理

[创建好 OAM 应用](create.md)之后，可以查看应用详情并更新应用的组件或运维特征。

## 查看应用详情

1. 在 __应用工作台__ -> __概览__ 页面，点击 __OAM 应用__ 页签，查看 OAM 应用列表
2. 点击应用名称可以查看应用详情，包括应用名称、状态、别名、描述信息、创建时间等字段。
3. 在应用详情页面点击 __组件__ 页签，可以查看当前应用定义的组件数量、类型、运维特征。

    ![component](../../images/oam07.png)

4. 在应用详情页面点击 __应用状态__ 页签，可以查看组件状态和应用资源。

    - 组件状态：展示当前应用下的每个组件的健康状态。存在不健康的组件时需要及时排查运维。

        ![status](../../images/oam08.png)

    - 应用资源：当前应用下部署的 Kubernetes 资源的信息。

        ![resources](../../images/oam09.png)

5. 在应用详情页面点击 __应用版本__ 页签，可以查看应用的版本信息，对应用的变更操作都会自动生成版本进行记录，并在需要时可以进行版本回滚。

    ![oam-version](../../images/oam-version.png)

## 编辑 OAM 应用基本信息

1. 点击 OAM 应用名称，然后在页面右上角点击 __ⵈ__ 选择 __编辑基本信息__ 。
2. 根据需要设置别名，或补充描述信息描述信息。

    ![edit](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/amamba/images/oam10.png)

## 编辑 OAM 应用 YAML 文件

1. 点击 OAM 应用名称，然后在页面右上角点击 __ⵈ__ 选择 __编辑 YAML__ 。
2. 根据需要编辑 OAM 应用的 YAML 文件。

    ![edit](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/amamba/images/oam11.png)

## 添加组件

1. 点击 OAM 应用名称，点击 __组件__ 页签，然后在右侧点击 __添加组件__ 。

    ![add-component](../../images/oam12.png)

2. 选择需要添加的组件类型，参考[内置组件列表](https://kubevela.io/zh/docs/end-user/components/references)填写对应的组件参数。

    ![add-component](../../images/oam13.png)

### 添加/更新运维特征

1. 点击 OAM 应用名称，点击 __组件__ 页签，在组件右侧点击 __ⵗ__ 选择 __编辑运维特征__ 。

    ![add-component](../../images/oam14.png)

2. 参考[内置运维特征列表](https://kubevela.io/zh/docs/end-user/traits/references)更新运维特征属性。

    ![add-component](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/amamba/images/oam15.png)

## 应用版本回滚

1. 点击 __应用版本__ 页签，选择某一版本（除当前版本外）右侧点击 __ⵗ__ 选择 __回滚__ 。

    ![rollback01](../../images/rollback01.png)

2. 点击 __确认__ 按钮，回滚成功后会返回列表，并提示。

    ![rollback02](../../images/rollback02.png)

    ![rollback03](../../images/rollback03.png)
