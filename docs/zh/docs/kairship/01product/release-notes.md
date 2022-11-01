# Release Notes

本页将以时间为序，列出多云编排的发布说明。

## v0.3.0

- **新增** 多云编排开启权限校验

- **新增** 多云编排 list instance 接口，根据权限展示数据

- **新增** 多云编排根据用户权限查询 cluster 资源概览信息

- **新增** 多云编排查询所有 member 集群的 labels

- **新增** 多云编排单机集群应用一键转换为多集群应用

- **新增** 多云编排查询 member 集群的 namespace 和 deployment 资源

- **新增** 多云资源创建的提示语

- **修复** 多云编排修复实例下所有 PropagationPolicy 资源的排序不生效的问题

- **修复** 多云编排修复移除 member 集群的问题

- **优化** 多云编排优化 karmada PropagationPolicy 和 OverridePolicy 的 protobuf 数据结构

- **修复** 若干 bug 修复
