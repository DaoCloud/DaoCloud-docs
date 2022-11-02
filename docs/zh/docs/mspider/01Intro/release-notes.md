# Release Notes

本页将以时间为序，列出服务网格的发布说明。

## v0.10.0

### API

- **改进** 边车升级接口新增工作负载与边车升级信息字段：

    - 请求新增字段：`is_hot_upgrade`、`workload_id`
    - 返回新增字段：`upgrade_info`
    
- **新增** 滚动重启定义的 annotation 字段 `controller.mspider.io/rollout-restart-at`
- **新增** 服务相关指标接口
- **新增** 接口字段 `sidecar_versions`、`is_upgradable`、`expand_result`
- **新增** 字段 WorkloadShadow.Status.SidecarVersions
- **新增** 对所有请求参数添加校验
- **新增** API 的 Pipeline，用于单独发布 mspider-api 的 sdk 版本
- **新增** `/apis/mspider.io/v3alpha1/meshes/{mesh_id}/environment-statuses` 所选升级版本支持的 kubernetes 版本范围，从小到大排序
- **新增** 更新网格接口增加网格版本字段
- **新增** 网格可升级版本接口
- **新增** 网格环境检测接口
- **新增** 网格升级过程中的升级结果检测接口
- **新增** 网格列表中网格是否可以被升级字段
- **新增** 边车升级检测接口：`/apis/mspider.io/v3alpha1/meshes/{mesh_id}/clusters/{cluster}/sidecar-management/-/upgrade-detection`
- **新增** 边车热升级版本列表：`/apis/mspider.io/v3alpha1/meshes/{mesh_id}/sidecar-management/-/supported-hot-upgrade-versions`
- **修复** 获取网格网关列表对 cluster 字段的校验，该字段为可选字段
- **修复** 获取集群命名空间列表对 cluster 字段的校验规则
- **修复** 获取工作负载实例列表对 cluster 字段的校验规则
- **修复** 无法创建服务网格的问题

### API 服务

- **新增** 网格升级详细实现
- **新增** 边车升级相关接口实现：获取边车升级版本列表、检测边车升级集群
- **新增** 网格升级环境检测接口提供所选升级版本支持的 kubernetes 版本范围，从小到大排序
- **新增** 原生原地边车升级实现
- **修复**  网格网关镜像 `hub` 字段没有应用
- **修复** 边车升级整体状态，当存实例升级失败时，状态为 Failed。并且返回整体错误信息
- **修复** 边车升级时，`pods`、`workloads`、`namespace` 三个字段都为空时，将会升级全部边车
- **修复** 升级过程中，环境检测状态不正确的问题
- **修复**  更新网格报错
- **优化** 网格是否可用升级接口，增加对权限的判断
- **优化** 升级信息，引入 operator status

### 基础设施

- **修复** 网格控制面版本不带 `-mspider` 后缀的问题

### 控制器

- **修复** 网格版本显示不正确，同时优化没有找到 istiod 时的网格版本，和所填参数一致
- **修复** 不存在 workloadShadow 导致的空指针问题 **优化** workloadShadow statues 更新逻辑，当没有 istio injector configMap 的时候为未注入，而不是报错
- **修复** 从网格中移除后，MeshCluster 的 Status 未被清理
- **移除** CKube 依赖 Remote APIServer kubeconfig 的 configmap 逻辑
- **优化** mcpc controller 重试，避免重试过快导致因处理顺序产生的处理错误没有被在正确的顺序处理

### 外部

- **升级** 前端版本至 v0.8.0。

### 安装

- **改进** 构建流程，使用本地的 go 编译器加速构建。 ([Issue #261](https://gitlab.daocloud.cn/ndx/mspider/-/issues/261))
- **修复** Arm64 镜像错误的问题。 ([Issue #256](https://gitlab.daocloud.cn/ndx/mspider/-/issues/256))
- **修复** ckube 无法在非 root 用户下运行的问题。 ([Issue #229](https://gitlab.daocloud.cn/ndx/mspider/-/issues/229))
- **修复** arm64 镜像的基础镜像依然为 amd64. ([Issue #261](https://gitlab.daocloud.cn/ndx/mspider/-/issues/261))
- **修复** 修复调用 ckube 无权限问题，ckube AuthorizationPolicy 配置中组件端口错误，端口为 8080。 ([Issue #244](https://gitlab.daocloud.cn/ndx/mspider/-/issues/244))
- **修复** istio.custom_params 错误拼写的问题。 ([Issue #238](https://gitlab.daocloud.cn/ndx/mspider/-/issues/238))

### 文档

- **新增** istio 资源 e2e 测试用例(网关规则、请求身份认证、对等身份认证、授权策略、服务条目)
- **改进** ckube/ckube-remote 映射端口 80 -> 8080
