# 请求身份认证

当一个外部用户对网格内部服务发起请求时，可以采用这种认证模式。在这种模式下，使用 JSON Web Token (JWT) 实现请求加密。
每个请求身份认证需要配置一个[授权策略](./authorize.md)。

所有标签为 `app: httpbin` 的工作负载需要使用 JWT 认证。示例如下：

```yaml
apiVersion: security.istio.io/v1beta1
kind: RequestAuthentication
metadata:
  name: httpbin
  namespace: foo
spec:
  selector:
    matchLabels:
      app: httpbin
  jwtRules:
  - issuer: "issuer-foo"
    jwksUri: https://example.com/.well-known/jwks.json
```

服务网格提供了两种创建方式：表单向导和 YAML。通过向导创建的具体操作步骤如下：

1. 在左侧导航栏点击`安全治理` -> `请求身份认证`，点击右上角的`创建`按钮。

    ![创建](../../images/request01.png)

2. 在`创建请求身份认证`界面中，先进行基本配置后点击`下一步`。

    ![创建](../../images/request02.png)

3. 按屏幕提示进行认证设置后，点击`确定`，系统将验证所配置信息。

    ![创建](../../images/request03.png)

4. 验证通过后，屏幕提示创建成功。

    ![创建](../../images/request04.png)

5. 在列表右侧，点击操作一列的 `⋮`，可通过弹出菜单进行更多操作。

    ![创建](../../images/request05.png)

!!! note

    具体参数的配置，请参阅[安全治理参数配置](./params.md)。
