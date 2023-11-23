# 定制 DCE 5.0 对接外部身份提供商 (IdP)

身份提供商（IdP, Identity Provider）：当 DCE 5.0 需要使用客户系统作为用户源，
使用客户系统登录界面来进行登录认证时，该客户系统被称为 DCE 5 的身份提供商

## 适用场景

如果客户对 Ghippo 登录 IdP 有高度定制需求，例如支持企业微信、微信等其他社会组织登录需求，请根据本文档实施。

## 支持版本

Ghippo 0.15.0及以上版本。

## 具体方法

### 自定义 ghippo keycloak plugin

1. 定制 plugin

    参考 [keycloak 官方文档](https://www.keycloak.org/guides#getting-started)和
    [keycloak 自定义 IdP](./keycloak-idp.md) 进行开发。

2. 构建镜像

    ```sh
    # FROM scratch
    FROM scratch
    
    # plugin
    COPY ./xxx-jar-with-dependencies.jar /plugins/
    ```

!!! note

    如果需要两个定制化 IdP，需要复制两个 jar 包。

### 部署 Ghippo keycloak plugin 步骤

1. [把 Ghippo 升级到 0.15.0 或以上](../../install/offline-install.md)。
   您也可以直接安装部署 Ghippo 0.15.0 版本，但需要把以下信息手动记录下来。

    ```sh
    helm -n ghippo-system get values ghippo -o yaml
    ```

    ```yaml
    apiserver:
      image:
        repository: release.daocloud.io/ghippo-ci/ghippo-apiserver
        tag: v0.4.2-test-3-gaba5ec2
    controllermanager:
      image:
        repository: release.daocloud.io/ghippo-ci/ghippo-apiserver
        tag: v0.4.2-test-3-gaba5ec2
    global:
      database:
        builtIn: true
      reverseProxy: http://192.168.31.10:32628
    ```

1. 升级成功后，手工跑一个安装命令，`--set` 里设的参数值从上述保存的内容里得到，并且外加几个参数值：

    - global.idpPlugin.enabled：是否启用定制 plugin，默认已关闭
    - global.idpPlugin.image.repository：初始化自定义 plugin 的 initContainer 用的 image 地址
    - global.idpPlugin.image.tag：初始化自定义 plugin 的 initContainer 用的 image tag
    - global.idpPlugin.path：自定义 plugin 的目录文件在上述 image 里所在的位置

    具体示例如下：

    ```sh
    helm upgrade \
        ghippo \
        ghippo-release/ghippo \
        --version v0.4.2-test-3-gaba5ec2 \
        -n ghippo-system \
        --set apiserver.image.repository=release.daocloud.io/ghippo-ci/ghippo-apiserver \
        --set apiserver.image.tag=v0.4.2-test-3-gaba5ec2 \
        --set controllermanager.image.repository=release.daocloud.io/ghippo-ci/ghippo-apiserver \
        --set controllermanager.image.tag=v0.4.2-test-3-gaba5ec2 \
        --set global.reverseProxy=http://192.168.31.10:32628 \
        --set global.database.builtIn=true \
        --set global.idpPlugin.enabled=true \
        --set global.idpPlugin.image.repository=chenyang-idp \
        --set global.idpPlugin.image.tag=v0.0.1 \
        --set global.idpPlugin.path=/plugins/.
    ```

1. 在 keycloak 管理页面选择所要使用的插件。
