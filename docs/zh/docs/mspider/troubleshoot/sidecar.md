---
hide:
  - toc
---

# 命名空间边车与工作负载边车配置冲突

## 现象描述

修改命名空间边车策略后，马上进行边车注入，`Pod` 不会重启生效。

## 原因分析

`Namespace` 的配置是，当前命名空间内 Sidecar 的 默认边车注入策略；`Pod` 启用时会根据当前命名空间策略，自动进行边车注入。
注入行为发生在启动节点；当 `Pod` 在运行中时修改命名空间边车策略。

为保证生产环境的稳定性，Istio 不会自动重启 `Pod`，需要用户手动重启 `Pod`。

## 解决方案

* 需要手工重启 `Pod`，请根据实际业务情况谨慎操作，建议提前做好规划。
* 通过 `kubectl rollout restart deployment <deployment-name> -n <namespace>` 命令重启 `Pod`。
