# 创建配置项

配置项（ConfigMap）以键值对的形式存储非机密性数据，实现配置数据和应用代码相互解耦的效果。配置项可用作容器的环境变量、命令行参数或者存储卷中的配置文件。

!!! note

    - 在配置项中保存的数据不可超过 1 MiB。如果需要存储体积更大的数据，建议挂载存储卷或者使用独立的数据库或者文件服务。

    - 配置项不提供保密或者加密功能。如果要存储加密数据，建议使用[密钥](use-secret.md)，或者其他第三方工具来保证数据的私密性。

支持两种创建方式：

- 图形化表单创建
- YAML 创建

## 前提条件

- 容器管理模块[已接入 Kubernetes 集群](../clusters/integrate-cluster.md)或者[已创建 Kubernetes 集群](../clusters/create-cluster.md)，且能够访问集群的 UI 界面

- 已完成一个[命名空间的创建](../namespaces/createns.md)、[用户的创建](../../../ghippo/user-guide/access-control/user.md)，并将用户授权为 [NS Edit](../permissions/permission-brief.md#ns-edit) 角色 ，详情可参考[命名空间授权](../permissions/cluster-ns-auth.md)。

## 图形化表单创建

1. 在 __集群列表__ 页面点击某个集群的名称，进入 __集群详情__ 。

    ![集群详情](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/deploy01.png)

2. 在左侧导航栏，点击 __配置与密钥__ -> __配置项__ ，点击右上角 __创建配置项__ 按钮。

    ![创建配置项](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/configmap01.png)

3. 在 __创建配置项__ 页面中填写配置信息，点击 __确定__ 。

    !!! note

        点击 __上传文件__ 可以从本地导入已有的文件，快速创建配置项。

    ![创建配置项](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/configmap03.png)

4. 创建完成后在配置项右侧点击更多可以，可以编辑 YAML、更新、导出、删除等操作。

    ![创建配置项](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/configmap04.png)

## YAML 创建

1. 在 __集群列表__ 页面点击某个集群的名称，进入 __集群详情__ 。

    ![集群详情](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/deploy01.png)

2. 在左侧导航栏，点击 __配置与密钥__ -> __配置项__ ，点击右上角 __YAML 创建__ 按钮。

    ![创建配置项](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/configmap02.png)

3. 填写或粘贴事先准备好的配置文件，然后在弹框右下角点击 __确定__ 。

    !!! note

        - 点击 __导入__ 可以从本地导入已有的文件，快速创建配置项。
        - 填写数据之后点击 __下载__ 可以将配置文件保存在本地。

    ![创建配置项](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/configmap05.png)

4. 创建完成后在配置项右侧点击更多可以，可以编辑 YAML、更新、导出、删除等操作。

    ![创建配置项](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/configmap04.png)

## 配置项 YAML 示例

    ```yaml
    kind: ConfigMap
    apiVersion: v1
    metadata:
      name: kube-root-ca.crt
      namespace: default
      annotations:
    data:
      version: '1.0'
    ```

[下一步：使用配置项](use-configmap.md){ .md-button .md-button--primary }
