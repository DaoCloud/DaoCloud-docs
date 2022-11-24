# Kafka 消息队列 Release Notes

本页列出 Kafka 消息队列的 Release Notes，便于您了解各版本的演进路径和特性变化。

## v0.1.2

- **新增** `mcamel-kafka-ui` 同步 pod 状态到实例详情页
- **优化** `mcamel-kafka-ui` workspace 界面逻辑调整
- **优化** `mcamel-kafka-ui` 不符合设计规范的样式调整
- **优化** `mcamel-kafka-ui` password 获取逻辑调整
- **优化** `mcamel-kafka-ui` cpu&内存请求量应该小于限制量逻辑调整

## v0.1.1

- **新增** `mcamel-kafka` 支持 kafka 列表查询，状态查询，创建，删除和修改
- **新增** `mcamel-kafka` 支持 kafka-manager 对 kafka 进行管理
- **新增** `mcamel-kafka` 支持 kafka 的指标监控，查看监控图表
- **新增** `mcamel-kafka` 支持 ghippo 权限联动
- **新增** `mcamel-elasticsearch` 获取用户列表接口
- **优化** `mcamel-kafka` 更新 release note 脚本，执行 release-process 规范
