# 升级注意事项

本页说明将 Skoala 升级到新版本时需要注意的相关事项。

## 从 v0.52.0（或更低版本）升级到 v0.52.1

Skoala v0.52.1 AI 网关 Higress 版本升级至 v2.1.9，CRD 发生变更，故升级后请在对应工作集群进行下述操作，手动升级 CRD。

### 前置条件

- addon 包已更新到最新版本。

### 操作步骤

1. 进入 **容器管理** -> **Helm 应用** -> **Helm 模板**，在插件列表中找到 **skoala-init** 插件，选择最新版本 0.52.1，下载到本地。
2. 在本地解压下载的 chat 包，进入 `/charts/contour-provisioner/crds` 目录，找到 `higress.gen.yaml` 文件，复制 CRD 内容。
3. 在已经升级了 skoala-init 版本的工作集群执行以下命令，更新 Higress CRD 中的内容到工作集群中。

```shell
kubectl apply -f - <<EOF
#crd内容
EOF
```
