# 编辑流水线

创建自定义流水线之后，需要手动定义流水线阶段。目前支持通过编辑 Jenkinsfile 或通过图形化界面表单为流水线定义执行阶段。此外，如需更改流水线各阶段的配置，也可参考本文调整各项配置。

!!! note

    - 有关编辑流水线时涉及到的概念，可参考[流水线中的概念](config/concept.md)
    - 有关编辑流水线时涉及到的参数，可参考[图形化任务模板参数说明](config/step.md)

## 前提条件

- [创建工作空间](../../../ghippo/user-guide/workspace/workspace.md)、[创建用户](../../../ghippo/user-guide/access-control/user.md)。
- 将该用户添加至该工作空间，并赋予 __workspace editor__ 或更高权限。
- 创建可以访问代码仓库、镜像仓库、集群的三个凭证，可参考[凭证管理](credential.md)。
- [创建自定义流水线](create/custom.md)，并且需要在构建参数中添加两个字符串参数。这些参数将用于镜像构建的命令中。参数说明如下：

    | 参数类型 | 参数名称 | 描述信息                                          |
    | -------- | -------- | ------------------------------------------------- |
    | 字符串   | registry | 镜像仓库地址。本例中使用 __release-ci.daocloud.io__ |
    | 字符串   | project  | 镜像仓库中的项目名称。本例中使用 __demo__            |
    | 字符串   | name     | 镜像的名称。本例中使用 __http-hello__                |

## 通过界面表单编辑流水线

应用工作台设计了图形化流水线编辑视图，能够兼容编辑 Jenkinsfile 中的大部分自定义操作，
便于查看或定义流水线的每个[阶段 (Stage)](https://www.jenkins.io/zh/doc/book/pipeline/#阶段)
和每个[步骤 (Step)](https://www.jenkins.io/zh/doc/book/pipeline/#步骤)，实现所见即所得的流水线编辑体验。

### 界面布局说明

1. 点击一个创建好的自定义流水线。在右上角点击 __编辑流水线__ ，进入图形化编辑页面。

    ![pipelisetting](https://docs.daocloud.io/daocloud-docs-images/docs/amamba/images/editpipe02.png)

2. 图形化编辑页面包括两个区域：__画布（左侧）__ 和 __阶段设置（右侧）__ 。

    ![canvasdescribe](https://docs.daocloud.io/daocloud-docs-images/docs/amamba/images/canvasdescribe.png)

    - 点击 __+添加阶段__ 后，会生成一个串行阶段，点击后，会生成一个新的阶段，可以在该阶段中添加流水线步骤，
      通过选择步骤类型，可以快速创建当前阶段中的流水线步骤。

    - 点击 __+添加并行阶段__ 后，会生成一个并行阶段，点击后，会生成一个新的阶段，可以在该阶段中添加流水线步骤，
      通过选择步骤类型，可以快速创建当前阶段中的流水线步骤。

    - 阶段创建后，点击 __阶段__ ，可以用过阶段进行阶段配置。支持设置阶段的名称、Agent、触发条件、步骤。

### 配置全局设置

点击 __全局设置__ ，从 __类型__ 下拉列表中选择 node，从 label 下拉列表选择 go 。

![pipelisetting](https://docs.daocloud.io/daocloud-docs-images/docs/amamba/images/pipelisetting.png)

### 添加阶段 - 拉取源代码

1. 点击画布中的 __添加阶段__ 。在右侧的阶段设置中设置名称：git clone。

2. 点击 __添加步骤__ ，在弹出的对话框中步骤类型下选择 __git clone__ ，参照下表，对相关参数进行配置。

    - 仓库 URL：输入仓库地址。
    - 分支：不填写，默认为 master 分支。
    - 凭证：如果您的仓库属于私有仓库则需要提供一个凭证。

    ![git_clone](https://docs.daocloud.io/daocloud-docs-images/docs/amamba/images/git_clone.png)

### 添加阶段 - 单元测试

1. 点击画布中的 __添加阶段__ 。在右侧的阶段设置中设置名称：unit test。

2. 在步骤模块中选择开启 __指定容器__ ，在弹出的对话框中填写容器名称：go，然后点击 __确定__ 。

    ![container1](https://docs.daocloud.io/daocloud-docs-images/docs/amamba/images/container1.png)

3. 点击 __添加步骤以对代码进行单元测试，并生成测试报告__ ，在弹出的对话框中步骤类型下选择 shell，并在命令行中输入以下命令，然后点击 __确定__ 。

    ```go
    go test -coverprofile=coverage.out
    ```

    ![go-test](https://docs.daocloud.io/daocloud-docs-images/docs/amamba/images/go-test.png)

### 添加阶段 - 构建并推送镜像

1. 点击画布中的 __添加阶段__ 。在右侧的阶段设置中设置名称：build & push。

2. 在步骤模块中选择开启 __指定容器__ ，在弹出的对话框中填写容器名称：go，然后点击 __确定__ 。

    ![container2](https://docs.daocloud.io/daocloud-docs-images/docs/amamba/images/container2.png)

3. 在步骤模块中选择开启 __使用凭证__ ，在弹出的对话框中填写相关参数，然后点击 __确定__ 。

    - 凭证：选择创建的 docker hub 凭证，用户访问镜像仓库。选择已创建好的 “docker-credential” 凭证。
    - 密码变量：PASS
    - 用户名变量：USER

    ![creditional1](https://docs.daocloud.io/daocloud-docs-images/docs/amamba/images/creditional1.png)

4. 点击 __添加步骤__ 进行代码构建，在弹出的对话框中步骤类型下选择 shell，参并在命令行中输入以下命令，然后点击 __确定__ 。

    ```go
    go build -o simple-http-server main.go
    ```

5. 点击 __添加步骤__ 以根据源码中的 Dockerfile 构建 Docker 镜像，在弹出的对话框中步骤类型下选择 shell，
   参并在命令行中输入以下命令，然后点击 __确定__ 。

    ```docker
    docker build -f Dockerfile . -t $REGISTRY/$PROJECT/$NAME:latest
    ```

6. 点击 __添加步骤__ 以登录镜像仓库并将镜像推送至镜像仓库中，在弹出的对话框中步骤类型下选择 shell，
   参并在命令行中输入以下命令，然后点击 __确定__ 。

    ```docker
    docker login $REGISTRY -u $USER -p $PASS
    ```

    ![build3](https://docs.daocloud.io/daocloud-docs-images/docs/amamba/images/build3.png)

6. 点击 __添加步骤__ 以将镜像推送至镜像仓库中，在弹出的对话框中步骤类型下选择 shell，参并在命令行中输入以下命令，然后点击 __确定__ 。

    ```docker
    docker push $REGISTRY/$PROJECT/$NAME:latest
    ```

    ![build4](https://docs.daocloud.io/daocloud-docs-images/docs/amamba/images/build4.png)

!!! note
    
    镜像更新后还可以实现触发流水线，具体操作请参考[触发流水线](run/trigger.md)

### 添加阶段 - 审核

1. 点击画布中的 __添加阶段__ 。在右侧的阶段设置中设置名称：review。

2. 点击 __添加步骤__ ，在弹出的对话框中步骤类型下选择 __审核__ ，在消息字段中填入 __@admin__ ，即 __admin__ 
   帐户在流水线运行到该阶段时会进行审核，然后点击 __确定__ 。

    ![review](https://docs.daocloud.io/daocloud-docs-images/docs/amamba/images/review.png)

### 添加阶段 - 部署至集群

1. 点击画布中的 __添加阶段__ 。在右侧的阶段设置中设置名称：deploy。

2. 在步骤模块中选择开启 __指定容器__ ，在弹出的对话框中填写容器名称：go，然后点击 __确定__ 。

    ![container3](https://docs.daocloud.io/daocloud-docs-images/docs/amamba/images/container3.png)

3. 在步骤模块中选择开启 __使用凭证__ ，在弹出的对话框中填写相关参数，然后点击 __确定__ 。

    - 凭证：选择 kubeconfig 类型的凭证。

    - kubeconfig 变量：如果使用的是 kubectl apply 的部署方式，变量值必须为 KUBECONFIG。

    ![credentials2](https://docs.daocloud.io/daocloud-docs-images/docs/amamba/images/credentials2.png)

4. 点击 __添加步骤__ 以进行集群部署操作，在弹出的对话框中步骤类型下选择 shell，参并在命令行中输入以下命令，然后点击 __确定__ 。

    ```shell
    kubectl apply -f deploy.yaml
    ```

### 运行流水线

1. 在流水详情页面点击 __立即执行__ 。在弹出的对话框中设置前提条件中定义的三个字符串参数，点击 __确定__ 来运行流水线。

    ![run](https://docs.daocloud.io/daocloud-docs-images/docs/amamba/images/run.png)

2. 成功开始运行后，页面会自动切换到流水线详情页面，点击当前运行的流水线记录。

3. 进入流水线记录详情页面后，您可以查看到当前流水线运行的过程，需要 admin 或者平台管理员来为流水线进行审核，审核成功后，资源会部署至集群。

    ![report](https://docs.daocloud.io/daocloud-docs-images/docs/amamba/images/report.png)

### 验证集群资源

1. 如果流水线的每个阶段都成功运行，则会自动构建一个 Docker 镜像并推送至您的 Docker Hub 仓库。
   最终，流水线将在您事先设置的项目中自动创建一个无状态负载。

2. 前往容器管理平台，点击集群下的 __工作负载__ ，您可以看到列表中显示的无状态工作负载。

    ![deployment](https://docs.daocloud.io/daocloud-docs-images/docs/amamba/images/deployment.png)

## 通过 Jenkinsfile 编辑流水线

通过 Jenkinsfile 可以快速定义流水线的各个阶段。

1. 在流水线列表页面找到需要新建的流水线，在右侧点击 __编辑 Jenkinsfile__ 。

    ![edit](https://docs.daocloud.io/daocloud-docs-images/docs/amamba/images/edit01.png)

    > 也可以点击流水线名称后，在页面右上角点击 __编辑 Jenkinsfile__ 。

2. 输入或粘贴事先准备好的 Jenkinsfile，然后点击 __确定__ 即可。

    ![edit](https://docs.daocloud.io/daocloud-docs-images/docs/amamba/images/edit02.png)
