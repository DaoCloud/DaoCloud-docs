# 流水线相关问题

本页列出使用应用工作台的流水线功能时时可能遇到的一些问题，并给出相应的解决方案。

## 执行流水线时报错

当 Jenkins 所在集群与应用部署集群跨数据中心时，网络通信延迟会变高，可能遇到如下的报错信息：

```bash
E0113 01:47:27.690555 50 request.go:1058] Unexpected error when reading response body: net/http: request canceled (Client.Timeout or context cancellation while reading body)
error: unexpected error when reading response body. Please retry. Original error: net/http: request canceled (Client.Timeout or context cancellation while reading body)
```

**解决方案**：

在该流水线的 Jenkinsfile 中将部署命令由 `kubectl apply -f` 修改为 `kubectl apply -f . --request-timeout=30m`。

## 如何更新内置 Label 的 podTemplate 镜像？

应用工作台通过 podTemplate 能力声明了 7 个 label：`base`、`maven`、`mavenjdk11`、`go`、`go16`、`node.js` 和 `python`。您可以指定具体的 Agent 标签来使用对应的 podTemplate。

如果内置 podTemplate 中的镜像不满足您的需求，可以通过以下方式替换容器镜像或者添加容器镜像。

1. 前往容器管理模块，找到 Jenkins 组件所在的集群，点击集群名称。

    ![faq-ci2](../images/faq-ci2.png)

2. 在左侧导航栏依次点击`配置与密钥`->`配置项`。

3. 搜索 `jenkins-casc-config` ，在操作列点击`编辑YAML` 。

    ![faq-ci3](../images/faq-ci3.png)

4. 在 `data` -> `jenkins.yaml` -> `jenkins.clouds.kubernetes.templates` 字段下选择需要更改的 podTemplate 的镜像。

    ![faq-ci4](../images/faq-ci4.png)

5. 更新完成后，前往`工作负载`重启 jenkins。

## 流水线构建环境为 maven 时，如何在 settings.xml 中修改依赖包来源？

当流水线构建环境为 maven 时，大多数客户需要修改 `settings.xml` 以更换依赖源。可参考以下步骤：

1. 前往容器管理模块，在`集群列表` 界面选择 Jenkins 组件所在的集群，点击集群名称。

    ![faq-ci2](../images/faq-ci2.png)

2. 在左侧导航栏依次点击`配置与密钥`->`配置项`。

3. 搜索 `amamba-devops-agent` ，在操作列点击 `编辑YAML` 。

    ![faq-ci5](../images/faq-ci5.png)

4. 在 `data` 模块 下的 `MavenSetting` 按需修改。

    ![faq-ci6](../images/faq-ci6.png)

5. 更新完成后，需要前往`工作负载`重启 Jenkins。

## 通过 Jenkins 构建镜像时，容器无法访问私有镜像仓库

### 集群运行时为 podman

1. 在容器管理模块的 `集群列表` 界面找到 Jenkins 组件所在的集群，点击集群名称。

2. 在左侧导航栏依次点击`配置与密钥`->`配置项`。

3. 搜索 `insecure-registries`，在操作列点击`编辑YAML` 。

4. 在 `data` 模块下的 `registries.conf` 下配置。

    修改时注意格式缩进，并且每个 registry 需要一个单独的 `[[registry]]` 部分，如下图所示：

    ![faq-ci1](../images/faq-ci1.png)
