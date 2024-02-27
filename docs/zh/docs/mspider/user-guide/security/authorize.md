---
hide:
  - toc
---

# 授权策略

授权策略类似于一种四层到七层的“防火墙”，它会像传统防火墙一样，对数据流进行分析和匹配，然后执行相应的动作。
无论是来自内部还是外部的请求，都适用授权策略。

授权策略的参考 YAML 示例如下：

```yaml
apiVersion: security.istio.io/v1
kind: AuthorizationPolicy
metadata:
  name: "ratings-viewer"
  namespace: default
spec:
  selector:
    matchLabels:
      app: ratings
  action: ALLOW
  rules:
  - from:
    - source:
        principals: ["cluster.local/ns/default/sa/bookinfo-reviews"]
    to:
    - operation:
        methods: ["GET"]
```

服务网格提供了两种创建方式：向导和 YAML。通过向导创建的具体操作步骤如下：

1. 在左侧导航栏点击 __安全治理__ -> __授权策略__ ，点击右上角的 __创建__ 按钮。

    ![创建](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/images/authorize01.png)

2. 在 __创建授权策略__ 界面中，先进行基本配置后点击 __下一步__ 。

    ![基本配置](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/images/authorize02.png)

3. 按屏幕提示进行策略设置后，点击 __确定__ 。参阅[策略设置参数说明](./params.md#_10)。

    ![策略设置](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/images/authorize03.png)

4. 返回授权列表，屏幕提示创建成功。

    ![创建成功](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/images/authorize04.png)

5. 在列表右侧，点击操作一列的 __⋮__ ，可通过弹出菜单进行更多操作。

    ![更多操作](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/images/authorize05.png)

!!! note

    - 具体参数的配置，请参阅[授权策略参数配置](./params.md#_8)。
    - 更直观的操作演示，可参阅[视频教程](../../../videos/mspider.md)。
