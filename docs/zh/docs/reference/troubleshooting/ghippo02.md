---
hide:
  - toc
---

# 登录无限循环，报错 401 或 403

出现这个问题原因为：ghippo-keycloak 连接的 Mysql 数据库出现故障, 导致 `OIDC Public keys` 被重置

在全局管理 0.11.1 及以上版本，您可以参照以下步骤，使用 `helm` 更新全局管理配置文件即可恢复正常。

```shell
# 更新 helm 仓库
helm repo update ghippo

# 备份 ghippo 参数
helm get values ghippo -n ghippo-system -o yaml > ghippo-values-bak.yaml

# 获取当前部署的 ghippo 版本号
version=$(helm get notes ghippo -n ghippo-system | grep "Chart Version" | awk -F ': ' '{ print $2 }')

# 执行更新操作, 使配置文件生效
helm upgrade ghippo ghippo/ghippo \
-n ghippo-system \
-f ./ghippo-values-bak.yaml \
--version ${version}
```
