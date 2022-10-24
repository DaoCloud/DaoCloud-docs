# 登录无限循环，报错 401 或 403

出现这个问题可能有几种原因。

### helm install 设置的 --set global.reverseProxy 参数不正确

解决步骤如下：

1. 查看 RequestAuthentication ghippo CR。

    ```shell
    kubectl get RequestAuthentication ghippo -n istio-system -o yaml
    ```

    确保 JWT 令牌中的 iss 字段包含在 `RequestAuthentication ghippo CR` 中。

    ![](../images/401-01.png)

    ![](../images/401-02.png)

2. 如果 issuer 地址不对，请执行如下命令:

    ```
    helm get values ghippo -n ghippo-system -o yaml > ghippo-bak.yaml

    helm upgrade ghippo ghippo-release/ghippo \
    -n ghippo-system \
    -f ./ghippo-bak.yaml \
    --set global.reverseProxy=https://虚拟机IP(域名、LB):30443(80、443)

    helm rollout restart deploy/ghippo-apierver -n ghippo-system
    ```

### 更换了 keycloak 数据库，导致 isito gateway 的 authn 模块的 jwks 公钥可能错了

这种情况需要重启 istiod

```shell
kubectl rollout restart deploy/istiod -n istio-system
```

### RequestAuthentication CR 中的 spec.jwtRules.jwksUri 地址访问不通

![](../images/401-03.png)

1. 进入到一个有 curl 或者 wget 命令的容器。

    ```shell
    kubectl exec -it ghippo-anakin-cd6859496-flf9j sh
    ```

2. 使用 curl 或者 wget 命令访问 jwtRules.jwksUri 的地址

    ```shell
    curl http://ghippo-apiserver.ghippo-system.svc.cluster.local:80/apis/ghippo.io/v1alpha1/certs
    {"keys":[{"kid":"DJV9ALtA-vx2kPP-SBuFKGBIg5rp_vLbAUj3e7EPrZs", "kty":"RSA", "e":"AQAB", "n":"lZ4UjUlYytbJDdtbv5oGNinoWC3aFERK09dEMd3dvlxvxb05LwBVcO0Ktpmfo49LbYQoQ5Vjjyu59hSh5oDbCeJoP4rnf0YDw6xbBkjZTx5SaqVmdBnLtNeAnz11PWrLBZJhPtd4PNu4AuqyN1pYtXPPCaeCwO_JHPlUp2YwIu-mGaJ4JqCH9r4Dzrt4z9-FeSc-U_OBVYvqRYe_1H38opEpf12j7eIyHJEdvsKFeWaskSc9jQbhUbRMW_Smr78R7nUcrb2QpDTmPcvW7E9IDQgvJHs7Jl6OXvUK5kjgjqBzjPGKSO6VYnUVBQ_SLV57lWMujC8ji3m1NsUlezQ0-w", "alg":"", "use":""}]}
    ```

3. 如果任意一个 jwtRules.jwksUri 地址访问不通，请尝试解决为什么访问不通这个问题
