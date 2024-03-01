# 手动管理服务

添加成功的服务会出现在服务列表页面，添加 API 时也可以选择列表中的服务作为目标后端服务。
微服务网关支持通过手动接入和自动发现两种方式添加服务。本页介绍如何手动接入服务。

## 接入服务

1. 在 __云原生网关列表__ 页面点击目标网关的名称，然后在左侧导航栏点击 __服务列表__ ，接着在右上角点击 __添加服务__ 。

    ![服务列表](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/gw-service03.png)

2. 选择服务来源，配置服务连接信息，点击 __确定__ 。

    === "集群服务"

        选择目标服务所在的集群和命名空间，填写访问协议、地址以及端口。

        ![添加集群服务](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/gw-service01.png)

        对于集群服务的访问方式，可在 __容器管理__ -> __容器网络__ -> __服务__ 中点击服务名称进行查看：

        ![获取服务访问地址](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/gateway/service/images/service-access.png)
    
    === "网格服务"
     
        选择目标服务所在的集群和命名空间，填写访问协议、地址以及端口。

        ![添加网格服务](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/gateway/service/images/mesh-access.png)
            
    === "接入注册中心服务"

        选择目标服务所在的注册中心，填写访问协议、地址和端口。

        ![添加注册中心服务](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/gateway/service/images/gw-access-service.png)
    
    === "注册配置中心服务"
         
        选择目标服务所在的注册中心，填写访问协议、地址和端口。

        ![添加注册中心服务](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/gw-service04.png)
        
    === "外部服务"

        填写服务名称、访问协议、地址、端口。
  
        ![添加外部服务](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/gw-service02.png)

## 查看服务详情

1. 在服务列表页面点击目标服务的名称，进入服务详情页面。

    ![服务详情](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/gw-service05.png)

2. 查看服务来源、连接信息、关联 API 等信息。

    ![服务详情](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/gw-service06.png)

## 更新服务

### 更新基础配置

更新基础配置指修改服务的名称、协议、地址和端口等连接信息。

1. 在 __服务列表__ 页面找到需要更新的服务，在服务右侧点击 __ⵗ__ ，选择 __修改基础配置__ 。

    ![更新服务](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/gw-service07.png)

2. 更新基本信息，点击 __确定__ 。

    ![更新服务](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/gateway/service/images/gw-service08.png)

!!! danger

    如果更新基础配置时选择了其他服务或修改了外部服务的连接信息，那么原来的服务会被删除，相当于添加了一个新的服务。
    但原服务关联的 API 会被自动关联到新的服务。

### 更新策略配置

1. 在 __服务列表__ 页面找到需要更新的服务，在服务右侧点击 __ⵗ__ ，选择 __修改策略配置__ 。

    ![更新服务](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/gw-service09.png)

2. 更新策略配置，点击 __确定__ 。

    ![更新服务](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/gateway/service/images/update4.png)

## 删除服务

在 __服务列表__ 页面找到需要删除的服务，在服务右侧点击 __ⵗ__ ，选择 __删除__ 。

![删除服务](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/gw-service10.png)

删除服务之前，需要确保没有 API 正在使用该服务。如果该服务正在被某个 API 使用，需要先根据页面提示，
点击 __API 管理__ 删除关联的 API 之后才能删除该服务。

![删除服务](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/gateway/service/images/delete1.png)
