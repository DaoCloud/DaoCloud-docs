# 流水线相关问题

本页列出使用应用工作台的流水线功能时时可能遇到的一些问题，并给出相应的解决方案。

## 执行流水线时报错

当 Jenkins 所在集群与应用部署集群跨数据中心时，网络通信延迟会变高，可能遇到如下的报错信息：

```console
E0113 01:47:27.690555 50 request.go:1058] Unexpected error when reading response body: net/http: request canceled (Client.Timeout or context cancellation while reading body)
error: unexpected error when reading response body. Please retry. Original error: net/http: request canceled (Client.Timeout or context cancellation while reading body)
```

__解决方案__：

在该流水线的 Jenkinsfile 中将部署命令由 `kubectl apply -f` 修改为 `kubectl apply -f . --request-timeout=30m`。

## 如何更新内置 Label 的 podTemplate 镜像？

应用工作台通过 podTemplate 能力声明了 7 个 label： __base__ 、 __maven__ 、 __mavenjdk11__ 、 __go__ 、 __go16__ 、 __node.js__ 和 __python__ 。
您可以指定具体的 Agent 标签来使用对应的 podTemplate。

如果内置 podTemplate 中的镜像不满足您的需求，可以通过以下方式替换容器镜像或者添加容器镜像。

1. 前往容器管理模块，找到 Jenkins 组件所在的集群，点击集群名称。

    ![faq-ci2](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/amamba/images/faq-ci2.png)

2. 在左侧导航栏依次点击 __配置与密钥__ -> __配置项__ 。

3. 搜索 __jenkins-casc-config__ ，在操作列点击 __编辑 YAML__ 。

    ![faq-ci3](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/amamba/images/faq-ci3.png)

4. 在 __data__ -> __jenkins.yaml__ -> __jenkins.clouds.kubernetes.templates__ 字段下选择需要更改的 podTemplate 的镜像。

    ![faq-ci4](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/amamba/images/faq-ci4.png)

5. 更新完成后，前往 __工作负载__ 重启 Jenkins。

## 流水线构建环境为 maven 时，如何在 settings.xml 中修改依赖包来源？

当流水线构建环境为 maven 时，大多数客户需要修改 __settings.xml__ 以更换依赖源。可参考以下步骤：

1. 前往容器管理模块，在 __集群列表__ 界面选择 Jenkins 组件所在的集群，点击集群名称。

    ![faq-ci2](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/amamba/images/faq-ci2.png)

2. 在左侧导航栏依次点击 __配置与密钥__ -> __配置项__ 。

3. 搜索 __amamba-devops-agent__ ，在操作列点击 __编辑 YAML__ 。

    ![faq-ci5](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/amamba/images/faq-ci5.png)

4. 在 __data__ 模块 下的 __MavenSetting__ 按需修改。

    ![faq-ci6](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/amamba/images/faq-ci6.png)

5. 更新完成后，需要前往 __工作负载__ 重启 Jenkins。

## 通过 Jenkins 构建镜像时，容器无法访问私有镜像仓库

### 集群运行时为 Podman

1. 在容器管理模块的 __集群列表__ 界面找到 Jenkins 组件所在的集群，点击集群名称。

2. 在左侧导航栏依次点击 __配置与密钥__ -> __配置项__ 。

3. 搜索 __insecure-registries__ ，在操作列点击 __编辑 YAML__ 。

4. 在 __data__ 模块下的 __registries.conf__ 下配置。

    修改时注意格式缩进，并且每个 registry 需要一个单独的 __[[registry]]__ 部分，如下图所示：

    ![faq-ci1](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/amamba/images/faq-ci1.png)

    !!! note

        __registries__ 关键字的值应该是完整的镜像仓库域名或 IP 地址，无需增加 __http__ 或 __https__ 前缀。
        如果镜像仓库使用非标准端口号，可以在地址后面加上冒号 __:__ 和端口号。

        ```
        [[registry]]
        location = "registry.example.com:5000"
        insecure = true

        [[registry]]
        location = "192.168.1.100:8080"
        insecure = true
        ```

    另请参考 [Podman 官网指导文档](https://podman-desktop.io/docs/containers/registries/insecure-registry)。

### 集群运行时为 Docker

1. 打开 Docker 的配置文件。在大多数 Linux 发行版上，配置文件位于 __/etc/docker/daemon.json__ ，如果不存在，请创建此配置文件。

2. 在 __insecure-registries__ 的字段将仓库地址添加进去。

    ```json
    {
      "insecure-registries": ["10.16.10.120:4443"]
    }
    ```

3. 保存后重启 Docker，执行如下命令：

    ```bash
    sudo systemctl daemon-reload
    sudo systemctl restart docker
    ```

!!! note

    参考 [Docker 官方指导文档](https://docs.docker.com/engine/reference/commandline/dockerd/#configuration-reload-behavior)。

## 如何修改 Jenkins 流水线并发执行数量

目前 DCE 5.0 部署出来后 Jenkins 流水线并发执行数量为 2，下述将描述如何更改并发执行数量：

1. 前往容器管理模块，找到 Jenkins 组件所在的集群，点击集群名称。

2. 在左侧导航栏依次点击 __配置与密钥__ -> __配置项__ 。

3. 搜索 __jenkins-casc-config__ ，在操作列点击 __编辑 YAML__ 。

4. 在 __data__ -> __jenkins.yaml__ -> __jenkins.clouds.kubernetes.containerCapStr__ 字段下修改数值。

    ![jenkins001](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/amamba/images/jenkinsadd.png)

5. 更新完成后，前往 __工作负载__ 重启 Jenkins。

## 流水线运行状态更新不及时？

在Jenkins的pod中，会存在一个名为`event-proxy`的sidecar容器，通过此容器将jenkins的事件发送到工作台中。目前通过dce5-installer安装的jenkins会默认开启此容器，当然，你也可以选择在容器管理平台的Addon模块中自己创建Jenkins（这通常用于Jenkins部署在工作集群）, 在创建时也可以选择是否开启此容器。

下面基于此容器是否开启，请分别检查不同的配置项是否正确：

### 开启了 event-proxy 容器

1. 前往容器管理模块，找到 Jenkins 组件所在的集群，点击集群名称。

2. 在左侧导航栏依次点击 __配置与密钥__ -> __配置项__ 。

3. 搜索 __jenkins-casc-config__ ，在操作列点击 __编辑 YAML__ 。

4. 在 __data__ -> __jenkins.yaml__ -> 搜索 `eventDispatcher.receiver`，它的值应该为 `http://localhost:9090/event` 

    如果 Jenkins 是部署在工作集群（需要穿透 DCE 5.0 的网关），则还需要检查以下几个配置项。

5. 再次查询名为 __event-proxy-config__ 的配置项，查看 YAML，配置项说明：

    ```yaml
    eventProxy:
      host: amamba-devops-server.amamba-system:80   # 此处为dce5的网关地址，如果为dce5-installer安装的jenkins，此处不需要修改
      proto: http                                   # 此处为dce5的网关协议（http或者https）
    ```

6. 在 Jenkins 所在集群， __配置与密钥__ -> __配置项__ 中搜索密钥 __amamba-jenkins__ 。

7. 检查密钥中的 __event-proxy-token__ 是否正确。此 Token 用于 DCE 5.0 的网关认证。
   如果不正确，Jenkins 将无法发送事件到工作台。有关如何生成此 Token，可以查看[访问密钥](../../ghippo/user-guide/personal-center/accesstoken.md)。

如果以上配置项都正确，但是 Jenkins 的流水线状态还是无法更新，请先查看 Jenkins 的 `event-proxy` 的容器日志。

### 未开启 event-proxy 容器

1. 前往容器管理模块，找到 Jenkins 组件所在的集群，点击集群名称。

2. 在左侧导航栏依次点击 __配置与密钥__ -> __配置项__ 。

3. 搜索 __jenkins-casc-config__ ，在操作列点击 __编辑 YAML__ 。

4. 在 __data__ -> __jenkins.yaml__ -> 搜索 `eventDispatcher.receiver`, 它的值应该为 `http://amamba-devops-server.amamba-system:80/apis/internel.amamba.io/devops/pipeline/v1alpha1/webhooks/jenkins` 其中 `amamba-system` 为工作台所部署的命名空间。
