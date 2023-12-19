# 多云密钥

密钥（Secret）是一种包含密码、令牌或密钥等少量敏感信息的对象。
这样的信息可能会被放在 Pod 规约中或者镜像中。
使用 Secret 意味着您不需要在应用程序代码中包含机密数据。

由于创建 Secret 可以独立于使用它们的 Pod，因此在创建、查看和编辑 Pod 的工作流程中暴露 Secret（及其数据）的风险较小。
DCE 和在集群中运行的应用程序也可以对 Secret 采取额外的预防措施，例如避免将机密数据写入非易失性存储。

Secret 类似于 ConfigMap 但专门用于保存机密数据。

目前提供了两种创建方式：向导创建和 YAML 创建。本文以向导创建为例，参照以下步骤操作。

1. 进入某一个多云实例后，在左侧导航栏中，点击 __资源管理__ -> __多云密钥__ ，点击右上角的 __创建密钥__ 按钮。

    ![点击按钮](https://docs.daocloud.io/daocloud-docs-images/docs/kairship/images/secret01.png)

2. 在 __创建密钥__ 页面中，输入名称，选择命名空间等信息后，点击 __确定__ 。

    ![填写表单](https://docs.daocloud.io/daocloud-docs-images/docs/kairship/images/secret02.png)

3. 返回多云密钥列表，新创建的默认位于第一个。点击列表右侧的 __⋮__ ，可以编辑 YAML、更新、导出和删除 Secret。

    ![其他操作](https://docs.daocloud.io/daocloud-docs-images/docs/kairship/images/secret03.png)

    !!! note

        若删除一个 Secret，其相关信息将一并被删除，请谨慎操作。

## YAML 示例

此处列出一个多云 Secret 的 YAML 示例，您稍加修改就可以使用。

```yaml
kind: Secret
apiVersion: v1
metadata:
  name: dockerconfigjson
  namespace: default
  uid: 452c3465-e9a1-4869-8972-2f199ba2750a
  resourceVersion: '1679594'
  creationTimestamp: '2022-09-27T07:21:36Z'
  labels:
    '4': '5'
  annotations:
    kairship.io/describe: test
    shadow.clusterpedia.io/cluster-name: k-kairshiptest
data:
  .dockerconfigjson: >-
    eyJhdXRocyI6eyIxIjp7InVzZXJuYW1lIjoiMiIsInBhc3N3b3JkIjoiMyIsImF1dGgiOiJNam96In19fQ==
type: kubernetes.io/dockerconfigjson
```
