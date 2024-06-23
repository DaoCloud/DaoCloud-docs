# 故障排查

本文将持续统计和梳理智能算力使用过程可能因环境或操作不规范引起的报错，以及在使用过程中遇到某些报错的问题分析、解决方案。

!!! warning
    本文档仅适用于 DCE 5.0 版本，若遇到服务网格的使用问题，请优先查看此排障手册。

智能算力在 DCE 5.0 中模块名称 `baize`，提供了一站式的模型训练、推理、模型管理等功能。

## 常见故障案例

- [Notebook 不受队列配额控制](./notebook-not-controlled-by-quotas.md)
- [队列初始化失败](./local-queue-initialization-failed.md)
