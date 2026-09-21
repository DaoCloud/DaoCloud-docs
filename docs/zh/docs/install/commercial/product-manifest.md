# 选产品与 manifest

安装器通过 **manifest** 决定装哪些模块。同一套安装流程下，先选对产品对应的 manifest，再执行安装。

社区版继续走[现有社区版安装](../community/kind/online.md)。下列三个商业产品共用离线安装流程，差别主要在 `-m` 指定的文件。

## 产品与 manifest 对照

| 产品 | 安装命令 | manifest 文件 |
| --- | --- | --- |
| DCE 社区版 | `install-app` | 内置，或 `sample/manifest-community.yaml` |
| DCE 商业版 | `cluster-create` | `sample/manifest-enterprise.yaml` |
| d.run AI 操作系统 | `cluster-create` | `sample/manifest-cloud.yaml` |
| d.run Token 工厂效能平台 | `cluster-create` | `sample/manifest-cloud-tokfact.yaml` |

离线包解压后，上述路径相对于 `offline/` 目录，例如：

```shell
./offline/dce5-installer cluster-create \
  -c ./offline/sample/clusterConfig.yaml \
  -m ./offline/sample/manifest-enterprise.yaml
```

将最后一行换成上表中对应产品的 manifest 即可。

## 下载包说明

- **DCE 商业版**、**d.run AI 操作系统**、**Token 工厂**在下载中心使用同一类完整离线包（包名形如 `offline-v0.x.y-amd64.tar`），**靠 manifest 区分产品**，不要混用错误的 `-m`。
- **DCE 社区版**使用独立的 `offline-community-v0.x.y-*.tar`。

下载入口见[下载中心](../../download/index.md)。完成选品后，按[开始安装](start-install.md)继续配置与安装。

## 商业产品差异（简要）

- **DCE 商业版**（`manifest-enterprise.yaml`）：云原生底座与商业模块为主；大模型服务平台等 AI 能力可按需再装，不在默认 BOM 中一次性全部打开。
- **d.run AI 操作系统**（`manifest-cloud.yaml`）：面向企业 AI 场景的 BOM，默认纳入大模型服务平台等能力；工作台、微服务引擎、多云编排等不在该默认清单中。
- **Token 工厂**（`manifest-cloud-tokfact.yaml`）：在 cloud 基础上打开 Token 工厂相关开关，并纳入大模型服务平台与驾驶舱等组件。

更细的字段说明见 [manifest.yaml](manifest.md)。部署架构、端口、外接仓库等与产品无关的步骤，三套商业产品共用同一套文档。
