---
date: 2022-11-17
hide:
  - toc
---

# 安装服务网格

请确认您的集群已成功接入 __容器管理__ 平台，然后执行以下步骤安装服务网格。

1. 从左侧导航栏点击 __容器管理__ ，进入 __集群列表__ ，点击准备安装服务网格的集群名称。

    ![安装采集器](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/images/login01.jpg)

2. 在 __集群概览__ 页面中点击 __控制台__ 。

    ![安装采集器](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/images/login02.jpg)

3. 自控制台中逐行输入如下命令（请修改对应的 VERSION 版本号）：

    ```sh
    # 添加 mspider 仓库，并更新，如果使用私有仓库，请将 release.daocloud.io 替换为私有仓库地址
    helm repo add mspider https://release.daocloud.io/chartrepo/mspider
    helm repo update
    
    # 找到 mspider 仓库中的版本号，一般选择最新的版本
    helm search repo mspider/mspider
    NAME                            CHART VERSION   APP VERSION     DESCRIPTION                                       
    mspider/mspider         v0.30.1         v0.30.1         Mspider management plane application, deployed ...
    mspider/mspider-mcpc    v0.30.1         v0.30.1         Mspider control plane application, independent ...

    # 指定版本号
    export VERSION=v0.30.1
    
    helm upgrade --install mspider mspider/mspider \
        --create-namespace -n mspider-system  \
        -set global.imageRegistry=release.daocloud.io/mspider \
        --version=${VERSION}
    ```

    ![安装采集器](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/images/install01.jpg)

    !!! note

        请将 __0.0.0-xxx__ 替换为计划安装的服务网格版本号。

4. 查看命名空间 __mspider-system__ 下 Pod 信息，看到相关 Pod 已创建并运行，表示服务网格安装成功。

    ![安装采集器](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/images/install02.jpg)

下一步：[创建网格](../user-guide/service-mesh/README.md)
