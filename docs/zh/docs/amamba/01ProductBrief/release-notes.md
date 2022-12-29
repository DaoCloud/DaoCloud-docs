# 应用工作台 Release Notes

本页列出应用工作台的 Release Notes，便于您了解各版本的演进路径和特性变化。

## 2022-11-30

### v0.10

#### 新功能

- **新增** 新增了 gitops 中的仓库功能，支持导入、删除
- **新增** 新增了 gitops 应用的同步功能

#### 优化

- **优化** 优化了应用接入服务网格流程

#### 修复

- **修复** 修复了 admin 用户未对部署目标（cluster/namespace）鉴权的问题
- **修复** 修复了 gitops 应用创建时间、同步开始时间和同步结束时间为 `Invalida date` 的错误
- **修复** 修复了获取 nacos 注册中心列表数据的错误
- **修复** 修复了列出工作负载接口通过名称排序报错
- **修复** 修复了集群解绑并重新绑定后，在 ArgoCD 中 destionation 中的 cluster 和 namespace 丢失的问题
- **修复** 修复了在更新 namespace 的 label 导致 namespace 和 workspace 绑定关系丢失的问题
- **修复** 修复了在完成流水线后，同步 jenkins 的 config 到数据库时，trigger 转换的错误
- **修复** 修复了因为集群的 kubeconfig 变更导致的 ArgoCD cluster 和 jenkins 中 kubeconfig 类型的 credential 不同步的问题
- **修复** 修复了仓库列表出现的无序和分页问题
- **修复** 修复了 from-jar 上传超过 32M 文件失败的问题

## 2022-11-18

### v0.9

#### 新功能

- **新增** jenkins-agent 镜像持续发布
- **新增** 添加了使用中间件的数据库的选项
- **升级** jenkins 从 2.319.1 升级到 2.346.2,kubernetes plugin 升级到 3734.v562b_b_a_627ea_c，相关的 plugins 也作了升级

#### 优化

- **优化** 获取 rollout 镜像列表，应用组列表，原生应用列表等性能优化
- **优化** from-jar 用到的 image 不再写死在源代码中，通过 env 的方式传递，并保证安装器能正确获取

#### 修复

- **修复** rollout 在不同 workspace 下无法区分的问题
- **修复** gitops 模块未鉴权的问题
- **修复** 偶现的 pipeline step 状态不正确的问题
- **修复** 获取 helmchart 的 description 为空的问题
- **修复** 创建 namespace 没有校验 storage 的问题
- **修复** list argocd repository 出现的无序和分页问题的修复
- **修复** from-jar 上传超过 32M 文件失败的问题的修复
- **修复** 获取 pipeline 日志的时候如果日志量过大则无法获取全量日志的问题
