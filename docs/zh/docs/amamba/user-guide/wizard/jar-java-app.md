# 基于 Jar 包部署 Java 应用

应用工作台支持通过 [Git 仓库](create-app-git.md)、Jar 包、容器镜像、Helm 模板等四种方式构建应用。本文介绍如何通过 Jar 文件部署 Java 应用程序。

## 前提条件

1. 创建一个[工作空间](../../../ghippo/user-guide/workspace/workspace.md)和一个[用户](../../../ghippo/user-guide/access-control/user.md)，该用户需加入该工作空间并具备 `Workspace Editor` 角色。

2. [创建访问镜像仓库的凭证](../pipeline/credential.md)，例如 `registry`。

3. 准备一个镜像仓库，例如 Harbor 仓库。

4. 下载 [daocloud-demo.jar](https://github.com/huoyinghao/filedownload/raw/main/daocloud-demo.jar)

## 操作步骤

1. 在左侧导航栏点击`向导`，然后选择`基于 Jar 包构建`。

    ![基于jar包](https://docs.daocloud.io/daocloud-docs-images/docs/amamba/images/jar01.png)

2. 参考下列要求填写基本信息，然后点击`下一步`。

    - 名称：填写资源负载的名称。
    - 资源类型：本演示选择无状态负载，目前仅支持无状态堵在
    - 部署位置：选择将应用部署到哪个集群下的哪个命名空间。如果要接入微服务，请确保当前工作空间下已经[创建了注册中心](../../../skoala/trad-ms/hosted/index.md)。
    - 所属应用：原生应用名称，支持从已有的原生应用列表中选择，也可以新建，默认与名称一致。
    - 实例数：填写实例的数量，Pod 的数量。

        ![基本信息](../../images/git01.png)

3. 参考下列要求配置流水线，然后点击`下一步`。

    - 目标镜像名称：为目标镜像命名，需包含目标镜像的存储路径，例如 `release-ci.daocloud.io/test-lfj/fromjar`。
    - Tag：为目标镜像打标签，例如版本号 `v1.0`。
    - 凭证：选择访问镜像仓库的凭证，例如 `registry-credential`。
    - JAVA_OPTS：用来设置 JVM 相关运行参数的变量，例如 `-server -Xms2048m -Xmx2048m -Xss512k`。
    - 构建参数：构建参数会以 `--build-arg` 的形式传递到 build 命令中，支持将上游制品下载地址、上游镜像下载地址设置为参数，也支持自定义任意参数。

        ![流水线构建](https://docs.daocloud.io/daocloud-docs-images/docs/amamba/images/jar03.png)

4. 参考下列要求填写容器配置，然后点击`下一步`。

    - 访问类型：支持通过 clusterIP 仅允许在集群内访问该应用，或者通过 NodePort 允许在集群外部访问，或者通过负载均衡器进行访问。
    - 端口配置：根据实际业务场景填写需要暴露的端口号，此示例中的 jar 包需要暴露 8080 端口。

        > 有关服务配置的更多详细说明，可参考[创建服务](../../../kpanda/user-guide/network/create-services.md)。

    - 资源限制：CPU 和内存配额不得超出应用所在的命名空间在当前工作空间中的剩余资源。

    - 生命周期：设置容器启动时、启动后、停止前需要执行的命令。详情可参考[容器生命周期配置](../../../kpanda/user-guide/workloads/pod-config/lifecycle.md)。

    - 健康检查：用于判断容器和应用的健康状态，有助于提高应用的可用性。详情可参考[容器健康检查配置](../../../kpanda/user-guide/workloads/pod-config/health-check.md)。

    - 环境变量：配置 Pod 内的容器参数，为 Pod 添加环境变量或传递配置等。详情可参考[容器环境变量配置](../../../kpanda/user-guide/workloads/pod-config/env-variables.md)。

    - 数据存储：配置容器挂载数据卷和数据持久化的设置。

        ![容器配置](https://docs.daocloud.io/daocloud-docs-images/docs/amamba/images/jar04.png)

5. 参考下列说明选择是否开启高级功能，然后点击`创建并上传 Jar 包`。

    - 服务网格：选择是否启用 [DCE 5.0 的服务网格](../../../mspider/intro/index.md)模块来治理微服务流量。
    - 微服务引擎：是否将新创建的应用接入 [DCE 5.0 的微服务引擎](../../../skoala/intro/index.md)模块。
        > 有关微服务引擎的配置，可参考[基于 Git 仓构建微服务应用](create-app-git.md)。
    - 可观测性：支持开启指标监控、链路追踪、JVM 监控。

        ![高级配置](../../images/jar01.png)

6. 选择需要上传的文件，点击`确定` 。

    ![上传文件](../../images/jar02.png)

7. 创建成功后会触发运行对应的流水线，在左侧导航栏点击`流水线`可查看其运行状态。

    > 流水线的命名规则为“对应的应用名称-随机数”，例如通过流水线名称 `demo-4615a8` 即可得知对应的应用名为 `demo`。

    ![运行流水线](https://docs.daocloud.io/daocloud-docs-images/docs/amamba/images/jar07.png)

8. 等待流水线执行成功后，在左侧导航栏点击`概览`，选择`原生应用`页签即可查看新建的应用。

    ![创建成功](https://docs.daocloud.io/daocloud-docs-images/docs/amamba/images/jar08.png)
