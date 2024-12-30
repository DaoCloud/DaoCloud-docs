---
hide:
  - toc
---

# 仪表盘

Grafana 是一种开源的数据可视化和监控平台，它提供了丰富的图表和面板，用于实时监控、分析和可视化各种数据源的指标和日志。可观测性 Insight 使用开源 Grafana 提供监控服务，支持从集群、节点、命名空间等多维度查看资源消耗情况，

关于开源 Grafana 的详细信息，请参见 [Grafana 官方文档](https://grafana.com/docs/grafana/latest/getting-started/?spm=a2c4g.11186623.0.0.1f34de53ksAH9a)。

## 操作步骤

1. 在左侧导航栏选择 __仪表盘__。

    - 在 __Insight /概览__ 仪表盘中，可查看多选集群的资源使用情况，并以命名空间、容器组等多个维度分析了资源使用、网络、存储等情况。

    - 点击仪表盘左上侧的下拉框可切换集群。

    - 点击仪表盘右下侧可切换查询的时间范围。

    ![dashboard](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/insight/images/dashboard00.png){ width="1000"}

2. Insight 精选多个社区推荐仪表盘，可从节点、命名空间、工作负载等多个维度进行监控。点击 __insight-system / Insight /概览__ 区域切换仪表盘。

    ![dashboard](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/insight/images/dashboard01.png){ width="1000"}

!!! note
    
    1. 导入自定义仪表盘请参考[导入自定义仪表盘](./import-dashboard.md)。

## 其他

### 访问 Grafana UI

1. 系统 Grafana 的登陆密码由 Grafana Operator 自动生成，通过解密 `insight-system` 命名空间中的 `grafana-admin-credentials` 的 `secret` 即可查找登陆密码。
2. 通过浏览器访问“`http://ip:port/ui/insight-grafana/login` 使用用户名 `admin`  和解密 `secret` 的密码进行登录。

### 自定义配置 Grafana 访问密码

#### 方案一：手动配置

将 Grafana CR `insight-grafana-operator-grafana` 的 `spec.config.security.admin_password` 设置输入指定密码。

```diff
apiVersion: integreatly.org/v1alpha1
kind: Grafana
spec:
  config:
    security:
      admin_user: admin
+     admin_password: admin
      allow_embedding: true
      disable_gravatar: false
```

#### 方案二：自动生成密码

删除掉 Grafana CR `insight-grafana-operator-grafana` 的 `security.admin_password` 的字段，`GrafanaOperator` 将自动给 grafana 实例生成新的 admin 的密码。

```diff
apiVersion: integreatly.org/v1alpha1
kind: Grafana
spec:
  config:
    security:
      admin_user: admin
-     admin_password: admin
      allow_embedding: true
      disable_gravatar: false
```

#### 方案三：通过 Secret 手动配置

将 CR 的 `spec.config.security.admin_password` 字段删除。并将 `insight-system` 命名空间下的 `grafana-admin-credentials`     secret 的 `GF_SECURITY_ADMIN_PASSWORD` 字段设置为新密码。
