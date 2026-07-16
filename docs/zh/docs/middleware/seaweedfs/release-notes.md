---
hide:
  - navigation
---

# SeaweedFS 对象存储 Release Notes

本页列出 SeaweedFS 对象存储的 Release Notes，便于您了解各版本的演进路径和特性变化。

*[mcamel-seaweedfs]: mcamel 是 DaoCloud 所有中间件的开发代号，SeaweedFS 是一款开源分布式对象存储中间件

## 2026-06-30

### v0.1.4

- **新增** SeaweedFS 生命周期管理
- **新增** 支持 LevelDB2 作为 Filer Meta Store，并在 Pod 列表中返回实例类型
- **新增** 实例 Pod 列表中的 Master、Filer、Volume 就绪数（`pod_ready_num`）
- **新增** 数据库连通性检查
- **新增** 前端日语翻译
- **修复** 实例状态展示问题
- **修复** Dashboard 展示问题
- **修复** OpenAPI 文档的 API 版本问题
- **修复** UI 展示及版本问题
- **优化** 参数校验，简化 Filer 与 Master 的暴露和存储配置
- **优化** 敏感字段处理逻辑，校验前自动填充敏感字段以避免重复输入
- **升级** SeaweedFS 至 4.35（含 4.19、4.20、4.21、4.22、4.25 中间版本），并补充 e2e 用例
