# 部署策略

多云编排支持在界面上查看当前实例的部署策略列表及其关联的多云资源，支持以 YAML 的方式维护创建和编辑部署策略信息，仅对空闲的部署策略提供删除按钮。

部署策略定义了在多云多集群中如何分发资源。

参照以下步骤创建一个部署策略。

1. 进入某一个多云实例后，在左侧导航栏中，点击`策略管理` -> `部署策略`，点击右上角的 `YAML 创建`按钮。

    ![image](../images/deploy01.png)

2. 在 `YAML 创建`页面中，输入正确的 YAML 语句后，点击`确定`。

    ![image](../images/deploy02.png)

3. 返回部署策略列表，新创建的默认位于第一个。点击列表右侧的 `⋮`，可以编辑 YAML 和执行删除操作。

    ![image](../images/deploy03.png)

    !!! note

        若要删除一个部署策略，需要先移除该策略相关的工作负载，删除之后该策略有关的信息都将被删除，请谨慎操作。

## YAML 示例

此处列出一个部署策略的 YAML 示例，您稍加修改就可以使用。

```yaml
kind: PropagationPolicy
apiVersion: policy.karmada.io/v1alpha1
metadata:
  name: nginx-propagation
  namespace: default
  uid: 2190e122-a6b0-4994-80e6-5c03a9d1d3a4
  resourceVersion: '24258'
  generation: 1
  creationTimestamp: '2022-09-15T10:04:20Z'
  annotations:
    shadow.clusterpedia.io/cluster-name: k-kairshiptest
spec:
  resourceSelectors:
    - apiVersion: apps/v1
      kind: Deployment
      namespace: default
      name: nginx
  placement:
    clusterAffinity:
      clusterNames:
        - skoala-dev
    clusterTolerations:
      - key: cluster.karmada.io/not-ready
        operator: Exists
        effect: NoExecute
        tolerationSeconds: 300
      - key: cluster.karmada.io/unreachable
        operator: Exists
        effect: NoExecute
        tolerationSeconds: 300
```