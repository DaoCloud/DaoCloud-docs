---
hide:
  - toc
---

# 对等身份认证

对等身份认证指的是在不对应用源码做侵入式修改的情况下，提供服务间的双向安全认证，同时密钥以及证书的创建、分发、轮转也都由系统自动完成，对用户透明，从而大大降低了安全配置管理的复杂度。

!!! note

    启用对等身份认证后，相应的目标规则也需要开启 mTLS 模式，否则将无法正常访问。

一个对全网格生效的严格 mTLS 策略。生效后，网格内部服务间访问将必须启用 mTLS。

YAML 示例：

```yaml
apiVersion: security.istio.io/v1beta1
kind: PeerAuthentication
metadata:
  name: "default"
  namespace: "istio-system"
spec:
  selector:
    matchLabels:
      app: reviews
  mtls:
    mode: STRICT
```

服务网格提供了两种创建方式：向导和 YAML。通过向导创建的具体操作步骤如下：

1. 在左侧导航栏点击 __安全治理__ -> __对等身份认证__ ，点击右上角的 __创建__ 按钮。

    ![创建](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/images/peer01.png)

2. 在 __创建对等身份认证__ 界面中，先进行基本配置后点击 __下一步__ 。

    ![基本配置](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/images/peer02.png)

3. 按屏幕提示进行认证设置后，点击 __确定__ 。参阅 [mTLS 模式参数配置](./params.md#-mtls)。

    ![认证设置](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/images/peer03.png)

4. 屏幕提示创建成功。

    ![成功](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/images/peer04.png)

5. 在列表右侧，点击操作一列的 __⋮__ ，可通过弹出菜单进行更多操作。

    ![更多操作](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/images/peer05.png)

!!! note

    - 具体参数的配置，请参阅[对等身份认证参数配置](./params.md#_2)
    - 参阅[服务网格身份和认证](./mtls.md)。
    - 更直观的操作演示，可参阅[视频教程](../../../videos/mspider.md#_5)
