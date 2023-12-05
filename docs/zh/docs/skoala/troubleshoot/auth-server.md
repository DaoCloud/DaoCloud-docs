
# skoala-init 的 x-kubernets-validations 未知字段问题

将 skoala-init 从 v0.11.0 升级到 v0.12.0 时报错导致无法升级：

```
unknown field "x-kubernets-validations" in io.k8s.apiextensions-apiserver....
```

![error](./images/error.jpg)

## 排查过程

1. Q: 操作步骤是否正确?

   A: 先 kubectl apply CRD(s)，再 helm upgrade，所以此操作步骤无误，排除操作问题.

1. Q: 版本是 QA 测试通过版本，且内部测试时升级功能正常?

   A: 确认无误。

1. Q: 确认使用版本与测试时使用的 k8s 集群版本?

   A: v1.21 (使用版本) ，v1.26 (测试版本)。

1.  Q: 至此及根据相应的错误截图，初步推断是客户 k8s 集群版本与相应 CRD 不匹配，
    同时 skoala-init 为微服务相关的所有的服务提供初始条件配置，即其包含有多个 CRD，
    而根据 skoala-init v0.12.0 的 ChangeLog 可知，在此版本中 Gateway-API 的 CRD 有过升级，所以得出:<br>

    A: 由 Gateway-API 相关升级引发。

## 参考文档:

- [Rollout, Upgrade and Rollback Planning](https://github.com/kubernetes/enhancements/blob/master/keps/sig-api-machinery/2876-crd-validation-expression-language/README.md#rollout-upgrade-and-rollback-planning)

    ![Rollout](./images/rollout.jpg)

- [KEP-2876：使用通用表达式语言（CEL）来验证 CRD](https://docs.daocloud.io/blogs/230412-k8s-1.27.html#kep-2876cel-crd)

    ![KEP-2876](./images/KEP-287.png)

- [CRD validation error for x-kubernetes-preserve-unknown-fields: true #88252](https://github.com/kubernetes/kubernetes/issues/88252#issuecomment-587250746)

## 解决方案

根据实际情况，选择适合的解决方案。

- 方案一：升级使用的 k8s 集群版本为至少 v1.25
- 方案二：按[CRD validation error for x-kubernetes-preserve-unknown-fields: true
](https://github.com/kubernetes/kubernetes/issues/88252#issuecomment-587250746) 中所示，添加：

   ```shell
    –validate=false
   ``` 
