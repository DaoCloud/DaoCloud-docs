# MinIO 对象存储 Release Notes

本页列出 MinIO 对象存储的 Release Notes，便于您了解各版本的演进路径和特性变化。

## v0.1.2

发布日期：2022-11-08

- **新增** `mcamel-minio` 获取用户列表接口。
- **新增** minio 实例创建
- **新增** minio 实例的修改
- **新增** minio 实例的删除
- **新增** minio 实例的配置修改
- **新增** minio 实例支持 nodeport 的 svc
- **新增** minio 实例的监控数据导出
- **新增** minio 实例的监控查看
- **新增** 多租户全局管理的对接
- **新增** mcamel-minio-ui 的创建/列表/修改/删除/查看
- **新增** APIServer/UI 支持 mtls
- **修复** `mcamel-minio` 单例模式下，只有一个 pod，修复 grafana 无法获取数据问题
- **优化** `mcamel-minio-ui` 完善了计算器功能
