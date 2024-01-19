# 安装 Jenkins

## 开始之前

- 安装 Jenkins 之前需要确保将要安装 Jenkins 的集群中存在默认的存储类；
- 请提前做好资源规划，评估未来最大并发的流水线数，并根据 [Jenkins 场景配置文档](../../quickstart/scenarios-config.md)进行配置；
- 请确认安装的目标集群的容器运行时：只有使用 Docker 作为容器运行时才能选择 Agent 的 `ContainerRuntime` 为 Docker；

## 开始安装

1. 进入 __容器管理__ 模块，在 __集群列表__ 中找到需要安装 Jenkins 的集群，点击该集群的名称。

    !!! note

        需要根据实际情况选择 Jenkins 的部署集群。目前不建议将其部署在全局服务集群，因为 Jenkins 执行流水线高并发时会占用大量资源，可能会导致全局服务集群的瘫痪。

    ![点击集群名称](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/amamba/images/install-jenkins11.png)

2. 在左侧导航栏中选择  __Helm 应用__ ->  __Helm 模板__ ，找到并点击  __Jenkins__ 。

    ![jenkins helm](https://docs.daocloud.io/daocloud-docs-images/docs/amamba/images/install-jenkins12.png)

3. 在 __版本选择__ 中选择想要安装的版本，点击 __安装__ 。

    ![安装](https://docs.daocloud.io/daocloud-docs-images/docs/amamba/images/install-jenkins13.png)

4. 在安装界面，填写所需的安装参数，最后在右下角点击 __确定__ 按钮。

    ![填写配置](https://docs.daocloud.io/daocloud-docs-images/docs/amamba/images/install-jenkins14.png)

    以下是重要参数说明，根据实际业务需求进行参数更换编写。

    | 参数                                 | 描述                                                         |
    | ------------------------------------ | ------------------------------------------------------------ |
    | ContainerRuntime                     | 选择运行时，支持 podman、docker。需要根据集群的容器运行时决定。               |
    | AdminUser                            | Jenkins 的用户名                                             |
    | AdminPassword                        | Jenkins 的密码                                               |
    | Deploy.JenkinsHost                   | Jenkins 的访问链接。如果选择Node Port 方式，访问地址规则为：http://{集群地址:端口} |
    | JavaOpts                             | 指定启动 Jenkins 的 JVM 启动参数                             |
    | ServiceType                          | 默认为ClusterIP，支持ClusterIP、NodePort、LoadBalancer       |
    | ServicePort                          | 服务访问端口                                                 |
    | NodePort                             | 如果 ServiceType=NodePort 则需要必填，范围为：30000-32767    |
    | resources.requests                   | Jenkins 的资源请求值                                         |
    | resources.limits                     | Jenkins 的资源限制值                                         |
    | image.registry                       | Jenkins 镜像仓库地址                                                 |
    | eventProxy.enabled                   | EventProxy 是一个旨在为 Jenkins 到 Amamba APIServer提供可靠连接的边车容器，当Jenkins部署的集群和Global集群不在同一个区域的时候，最好开启。 |
    | eventProxy.image.registry            | eventProxy 镜像仓库的地址。<br />如果 enabled=true 必须填写                                   |
    | eventProxy.configMap.eventProxy.host  | Jenkins 事件的接收地址的Host，Jenkins如果部署在Worker集群，需要设置成DCE的入口地址。<br />如果 enabled=true 必须填写。                                   |
    | eventProxy.configMap.eventProxy.proto | Jenkins 事件的接收地址的Protocol，默认是http。<br />如果 enabled=true 必须填写                                   |
    | eventProxy.configMap.eventProxy.webhookUrl | Jenkins 事件的接收地址的路径，默认是 `/apis/internel.amamba.io/devops/pipeline/v1alpha1/webhooks/jenkins` 。  |
    | eventProxy.configMap.eventProxy.token | 访问DCE的toekn，获取方式参考[全局管理访问密钥文档](../../../ghippo/user-guide/personal-center/accesstoken.md)<br />如果 enabled=true 必须填写 |

5. 前往 Helm 应用查看部署结果。

    ![完成创建](https://docs.daocloud.io/daocloud-docs-images/docs/amamba/images/install-jenkins15.png)

## 集成 Jenkins

说明：目前仅支持集成通过 DCE 5.0 平台安装的 Jenkins。

1. 使用具有应用工作台管理员角色的用户登录 DCE 5.0 并进入应用工作台。

    ![完成创建](https://docs.daocloud.io/daocloud-docs-images/docs/amamba/images/install-jenkins16.png)

2. 在左侧导航栏点击平台管理下的 __工具链集成__ ，点击右上角的 __集成__ 按钮。

    ![完成创建](https://docs.daocloud.io/daocloud-docs-images/docs/amamba/images/install-jenkins17.png)

3. 选择工具链类型 __Jenkins__ ，填写集成名称、Jenkins 地址、用户名和密码。
   如果 Jenkins 地址为 https 协议时，需要提供证书。通过 Helm 部署出来的 Jenkins 默认账户密码为 __admin/Admin01__ 。

    ![完成创建](https://docs.daocloud.io/daocloud-docs-images/docs/amamba/images/install-jenkins18.png)

4. 集成完毕后会在 __工具链列表__ 页面成功生成一条记录。

    ![完成创建](https://docs.daocloud.io/daocloud-docs-images/docs/amamba/images/install-jenkins19.png)

5. 接下来就可以前往工作空间内[创建流水线](create/custom.md)。

## 集成注意事项

如果集成的 Jenkins 实例未提供集群和命名空间信息时，会导致应用工作台无法更新 Jenkins 实例的配置文件，从而引发出下述两个问题：

- 流水线 __通知__ 步骤，在全局管理 -> 平台设置 -> 邮件服务器设置，配置好邮件服务器地址后，无法更新到 Jenkins 中配置中。
- 流水线 __SonarQube 配置__ 步骤，在工具链集成 SonarQube 实例后并绑定到当前工作空间，使用该实例会失效。

针对上述问题，需要前往 Jenkins 后台进行相关配置。

### 针对通知步骤，在 Jenkins 后台配置邮件通知

1. 前往 Jenkins 后台，点击 Manage Jenkins -> Configure System，然后下拉找到 __邮件通知__ 模块。

2. 填写相关参数，参数说明如下：

    - SMTP 服务器：能够提供邮件服务的 SMTP 服务器地址
    - 启用 SMTP 认证：根据需求选择，建议启用 SMTP 认证
    - 用户名：SMTP 用户的名称
    - 密码：SMTP 用户的密码
    - SMTP 端口：发送邮件的端口，不填写此项将使用协议默认端口.

    !!! note

        配置发件人邮箱地址需要点击 右上角个人头像 -> 设置，然后下拉找到 __邮件地址__ 

    ![Jenkins邮件配置页](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/amamba/images/install-jenkins06.png)

### 针对 SonarQube 配置步骤，在 Jenkins 后台配置 SonarQube 服务器地址

1. 前往 Jenkins 后台，点击 Manage Jenkins -> Configure System，然后下拉找到 __SonarQube servers__ ，然后点击 __Add SonarQube__ 。

2. 填写相关参数，参数说明如下：

    - Name：给 SonarQube 服务器配置一个名称，在应用工作台流水线的 SonarQube 配置步骤中需要输入相同的名字。
    - Server URL：SonarQube 服务器的 URL。
    - Server authentication token：SonarQube 服务器的身份验证令牌。您可以在 SonarQube 控制台中生成一个令牌。

    ![Jenkins Sonarqube配置页](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/amamba/images/install-jenkins08.png)

    !!! note

        如果想要将工作台已经集成的 SornarQube 更新到新的 Jenkins 的配置中，请务必保证名称一致。需要注意的是，Name不是集成的时候输入的名称，
        需要在流水线的 SonarQube 配置步骤中下拉获取。


    ![SonarQube Name](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/amamba/images/install-jenkins07.png)

