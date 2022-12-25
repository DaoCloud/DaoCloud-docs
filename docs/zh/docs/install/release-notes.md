# 安装器 Release Notes

本页列出安装器的 Release Notes，便于您了解各版本的演进路径和特性变化。

## 2022-11-30

### v0.3.29

#### 新功能

- **新增** ARM64 支持：构建 arm64 离线包。
- **新增** 支持麒麟 kylin v10 sp2 离线包。
- **新增** 基础设施支持 1.25： 升级 redis-operator，eck-operator，hwameiStor 等组件。
- **新增** 支持私钥模式的集群部署。
- **新增** 工作负载基于自定义指标弹性伸缩，更加贴近用户实际业务弹性扩缩容需求。

#### 优化

- **优化** 永久 harbor 使用 operator 创建，开启 HTTPS，并使用 Postgressql operator。
- **优化** 商业版使用 contour 作为默认的 ingress-controller。
- **优化** MinIO 支持使用 VIP。
- **优化** coredns 自动注入仓库 VIP 解析。
- **优化** 优化离线包制作流程，加速打包docker镜像。

#### 修复

- **修复** 修复了公有云 service 的问题。
- **修复** 修复了各个子模块的镜像和 helm 的问题。
- **修复** 修复了离线包加载的缺陷修复。

#### 已知问题

- 因为部分 operator 需升级到支持 1.25，导致DCE5向下不支持 1.20。
- kubean 默认 k8s 版本和离线包仍然限制在 k8s 1.24 版本，还未能更新到 1.25 （是由于 postgres-operator 暂不支持）。
- Image Load 情况下，istio-ingressgateway imagePullPolicy 为 always。
- ARM 版本，不能执行第16步（harbor），因为 harbor 暂时不支持 ARM。需要修改 mainfest.yaml 文件，postgressql operator 为 fasle，执行安装命令时要添加 -j 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15
