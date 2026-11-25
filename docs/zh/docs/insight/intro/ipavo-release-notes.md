# Ipavo Release Notes

本页列出仪表盘组件 Ipavo 的 Release Notes，便于您了解各版本的演进路径和特性变化。Insight 可观测性的发布说明见 [Release Notes](release-notes.md)。

## 2026-10-31

### v0.15.2

- **新增** TokenFactory 模式。设置 `global.tokenfactory.enable=true` 后不创建侧边栏菜单，代理和版本注册保持不变，`/ipavo` 仍可访问。已部署环境开启该参数并升级后，原有的 `<release>-menus` 会被删除

## 2026-09-30

### v0.15.1

- **优化** 全局管理中的菜单、代理和版本资源名称跟随 Helm release
- **优化** 这些资源增加注解 `argocd.argoproj.io/sync-options: SkipDryRunOnMissingResource=true`，在 Ghippo CRD 尚未就绪时允许 Argo CD 跳过 dry-run 校验
- **优化** `ui.enabled` 为 false 时不注册 UI 反代
- **修复** 内置 MySQL 的 DSN 使用 `mysql.password`，镜像地址使用 `mysql.image.repository`

## 2026-08-31

### v0.15.0

- **升级** 服务端镜像至 **v0.15.0**，UI 镜像至 **v0.13.0**
