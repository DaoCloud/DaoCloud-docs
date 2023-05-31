# 合并 openapi 到仓库内

## 介绍

解决目前 openapi 上传较慢的问题，将 openapi 文档转移到 `daocloud/dao-openapi` 这个仓库下，各个模块仅需要给这个模块提交 PR 即可.

文档站在 build 过程中，会自动拉取该仓库的 dao-openapi 文档，并且 build 到文档站内

- 具体脚本内容: `scripts/merged_nav.py`
- workflow 更新部分
    - 增加 checkout daocloud/dao-openapi 仓库
    - 增加 执行 openapi 文档迁移和 navigation 合并脚本

## dao-openapi 仓库介绍

> 每次更新

- 文件内容增加到 `openapi` 目录
- 修改 `openapi-nav.yml` 引用对应的文件
