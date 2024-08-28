# 系统消息

系统消息用于通知所有用户，类似于系统公告，会在特定时间显示在 DCE 5.0 UI 的顶部栏。

## 配置系统消息

通过在[全局服务集群](../../kpanda/user-guide/clusters/cluster-role.md#_2) apply 系统消息的 YAML 即可创建一条系统消息，消息的显示时间由 YAML 中的时间字段决定。
系统消息仅在 start、end 字段配置的时间范围之内才会显示。

1. 在集群列表中，点击全局服务集群的名称，进入全局服务集群。

    ![选择集群](../images/system-message1.png)

2. 选择左侧导航栏的 __自定义资源__ ，搜索 `ghippoconfig`，点击搜索出来的 `ghippoconfigs.ghippo.io`

    ![选择自定义资源](../images/system-message2.png)

3. 点击 __YAML 创建__ ，或修改已存在的 YAML

    ![选择自定义资源](../images/system-message3.png)

以下是一个 YAML 示例：

```yaml
apiVersion: ghippo.io/v1alpha1
kind: GhippoConfig
metadata:
  name: system-message
spec:
  message: "this is a message"
  start: 2024-01-02T15:04:05+08:00
  end: 2024-07-24T17:26:05+08:00
```
