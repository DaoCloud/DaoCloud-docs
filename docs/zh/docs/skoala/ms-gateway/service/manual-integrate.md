# 手动接入服务

添加成功的服务会出现在服务列表页面，添加 API 时也可以选择列表中的服务作为目标后端服务。微服务网关支持通过手动接入和自动发现两种方式添加服务。本页介绍如何手动接入服务。

**前提条件**

需要事先在来源管理<!--待补充链接-->中添加对应的服务来源，才能在手动接入服务时选择对应的服务来源类型。

## 接入服务

1. 在`微服务网关列表`页面点击目标网关的名称，进入网关概览页后，在左侧导航栏点击`服务接入`-->`服务列表`。

    ![服务列表](imgs/service-list.png)

2. 在`服务列表`页面点击`手工接入`-->`添加服务`。

    ![服务列表](https://community-github.cn-sh2.ufileos.com/daocloud-docs-images/docs/skoala/ms-gateway/service/imgs/manual.png)

3. 选择服务来源，配置服务连接信息，点击`确定`。

    - 集群服务：选择目标服务所在的集群和命名空间，填写访问协议、地址以及端口。

        ![添加集群服务](https://community-github.cn-sh2.ufileos.com/daocloud-docs-images/docs/skoala/ms-gateway/service/imgs/config1.png)

        对于集群服务的访问方式，可在`容器管理`->`容器网络`->`服务`中点击服务名称进行查看：

        ![获取服务访问地址](https://community-github.cn-sh2.ufileos.com/daocloud-docs-images/docs/skoala/ms-gateway/service/imgs/service-access.png)

    - 网格服务：

        接入网格服务的功能正在开发中，敬请期待。

    - 注册中心服务：选择目标服务所在的注册中心，填写访问协议、地址和端口。

        ![添加注册中心服务](https://community-github.cn-sh2.ufileos.com/daocloud-docs-images/docs/skoala/ms-gateway/service/imgs/config3.png)

    - 外部服务：填写服务名称、访问协议、地址、端口。
  
        ![添加外部服务](https://community-github.cn-sh2.ufileos.com/daocloud-docs-images/docs/skoala/ms-gateway/service/imgs/config4.png)

## 查看服务详情

1. 在服务列表页面点击目标服务的名称，进入服务详情页面。

    ![服务详情](https://community-github.cn-sh2.ufileos.com/daocloud-docs-images/docs/skoala/ms-gateway/service/imgs/service-details0.png)

2. 查看服务来源、连接信息、关联 API 等信息。

    ![服务详情](https://community-github.cn-sh2.ufileos.com/daocloud-docs-images/docs/skoala/ms-gateway/service/imgs/service-details2.png)

## 更新服务

### 更新基本信息

1. 在`服务列表`页面找到需要更新的服务，在服务右侧点击 **`ⵗ`**，选择`基本信息`。

    ![更新服务](https://community-github.cn-sh2.ufileos.com/daocloud-docs-images/docs/skoala/ms-gateway/service/imgs/update1.png)

2. 更新基本信息，点击`确定`。

    ![更新服务](https://community-github.cn-sh2.ufileos.com/daocloud-docs-images/docs/skoala/ms-gateway/service/imgs/update1.png)

!!! danger

    如果更新基本信息时选择了其他的服务，那么原来的服务会被删除，相当于添加了一个新的服务。但原服务关联的 API 会被自动关联到新的服务。

![更新服务-危险](https://community-github.cn-sh2.ufileos.com/daocloud-docs-images/docs/skoala/ms-gateway/service/imgs/update-danger.png)

### 更新策略配置

1. 在`服务列表`页面找到需要更新的服务，在服务右侧点击 **`ⵗ`**，选择`策略配置`。

    ![更新服务](https://community-github.cn-sh2.ufileos.com/daocloud-docs-images/docs/skoala/ms-gateway/service/imgs/update3.png)

2. 更新策略配置，点击`确定`。

    ![更新服务](https://community-github.cn-sh2.ufileos.com/daocloud-docs-images/docs/skoala/ms-gateway/service/imgs/update4.png)

## 删除服务

在`服务列表`页面找到需要删除的服务，在服务右侧点击 **`ⵗ`**，选择`删除`。

![删除服务](https://community-github.cn-sh2.ufileos.com/daocloud-docs-images/docs/skoala/ms-gateway/service/imgs/delete.png)

删除服务之前，需要确保没有 API 正在使用该服务。如果该服务正在被某个 API 使用，需要先根据页面提示，点击 `API 管理`删除关联的 API 之后才能删除该服务。

![删除服务](https://community-github.cn-sh2.ufileos.com/daocloud-docs-images/docs/skoala/ms-gateway/service/imgs/delete1.png)
