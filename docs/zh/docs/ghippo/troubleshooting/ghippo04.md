---
hide:
  - toc
---

# 单独升级全局管理时升级失败

## CRD 未更新错误

若升级失败时包含如下信息，可以参考[离线升级](../install/offline-install.md#__tabbed_3_2)中的更新
ghippo crd 步骤完成 crd 安装。

```console
ensure CRDs are installed first
```

## 数据库迁移报错

### 错误现象

Pod 启动失败，log 中出现如下信息：

```console
init database failed    {"error": "migrate failed: Dirty database version 0. Fix and force version."}
```

### 错误原因

因为环境或数据库状态异常或 SQL 语句错误等问题导致 SQL 迁移执行出错，但是仅当 Pod 第一次报错的时候输出真正的数据库错误信息，后续 Pod 重启后会出现上述错误。

### 解决方案

1. 进入 MySQL，选择启动失败的服务对应的数据库（可能出问题的数据库有 audit、ghippo）

2. 修改 schema_migrations 表的 dirty 字段

    ```console
    update schema_migrations set dirty=0;
    ```

3. 重启失败的服务

4. 如重启后 SQL 迁移还是报错，可能是 SQL 语句本身的问题，需要报 Bug 并联系开发同学来解决
