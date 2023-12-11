# 快速创建流水线

本节将通过编译、构建、部署来创建流水线，通过详细的步骤操作描述，帮助您快速创建一条流水线。

## 前提条件

- 需创建一个工作空间和一个用户，该用户需加入该工作空间并赋予  **workspace edit**  角色。
  参考[创建工作空间](../../ghippo/user-guide/workspace/workspace.md)、[用户和角色](../../ghippo/user-guide/access-control/user.md)。
- 创建可以访问镜像仓库、集群的两个凭证，分别命名为： **registry** 、 **kubeconfig** 。
  创建凭证的更多信息，请参考[凭证管理](../user-guide/pipeline/credential.md)。
- 准备一个 GitHub 仓库、DockerHub 仓库。

## 创建凭证

1. 在 **凭证** 页面创建两个凭证：

    - docker-credential：用户名和密码，用于访问镜像仓库。
    - demo-dev-kubeconfig：用于使用这个 kubeconfig 访问 Kubernetes 集群。

2. 创建完成后，可以在 **凭证列表** 页面看到凭证信息。

## 创建自定义流水线

1. 在流水线列表页点击 **创建流水线** 。

    ![pipeline](https://docs.daocloud.io/daocloud-docs-images/docs/amamba/images/pipelin01.png)

2. 在弹出的对话框中，选择 **自定义创建流水线** ，点击 **确定** 。

    ![pipeline](https://docs.daocloud.io/daocloud-docs-images/docs/amamba/images/pipelin02.png)

3. 进入 **自定义创建流水页面**  ，输入流水线名称 **pipeline-demo** 。

    ![pipeline](https://docs.daocloud.io/daocloud-docs-images/docs/amamba/images/pipelin03.png)

4. 在 **构建参数** 中添加三个字符串参数，这些参数将用于镜像构建的命令中。

    - registry：镜像仓库地址。示例值： **release.daocloud.io** 。
    - project：镜像仓库中的项目名称。示例值： **demo** 。
    - name：镜像的名称。示例值： **http-hello** 。

    ![pipeline](https://docs.daocloud.io/daocloud-docs-images/docs/amamba/images/pipelin04.png)

5. 添加完成后，点击 **确定** 。

## 编辑流水线

1. 在流水线列表页面点击一个流水线的名称。

    ![pipelisetting](https://docs.daocloud.io/daocloud-docs-images/docs/amamba/images/editpipe01.png)

2. 在右上角点击 **编辑流水线** ，

    ![pipelisetting](https://docs.daocloud.io/daocloud-docs-images/docs/amamba/images/editpipe02.png)

3. 在右上角点击 **全局设置** 。

    ![pipelisetting](https://docs.daocloud.io/daocloud-docs-images/docs/amamba/images/editpipe03.png)

4. 类型设为 node，且 label 设为 go，点击 **确定** 。

    ![pipelisetting](https://docs.daocloud.io/daocloud-docs-images/docs/amamba/images/editpipe04.png)

5. 添加阶段 - 拉取源代码。

    - 点击画布中的 **添加阶段** 。在右侧的阶段设置中设置名称：git clone。
    - 点击 **添加步骤** ，在弹出对话框中步骤类型下选择 git clone，配置相关参数：
        - 仓库 URL：输入 GitLab 仓库地址。
        - 分支：不填写默认为 master 分支。
        - 凭证：如果属于私有仓库，则需要提供一个凭证。

    ![quickstart01](https://docs.daocloud.io/daocloud-docs-images/docs/amamba/images/quickstart01.png)

6. 添加阶段 - 构建并推送镜像。

    - 点击画布中的 **添加阶段** 。在右侧的阶段设置中设置名称：build & push。

    - 在步骤模块中选择开启 **指定容器** ，在弹出的对话框中填写容器名称：go，然后点击 **确定** 。

        ![container](https://docs.daocloud.io/daocloud-docs-images/docs/amamba/images/container.png)

    - 在步骤模块中选择开启 **使用凭证** ，在弹出的对话框中填写相关参数，然后点击 **确定** 。

        - 凭证：选择创建的 Docker hub 凭证，用户访问镜像仓库。
        - 密码变量：PASS
        - 用户名变量：USER

        ![quickstart02](https://docs.daocloud.io/daocloud-docs-images/docs/amamba/images/quickstart02.png)

    - 点击 **添加步骤** 进行代码构建，在弹出的对话框中步骤类型下选择 shell，参并在命令行中输入以下命令，然后点击 **确定** 。

        ```go
        go build -o simple-http-server main.go
        ```

    - 点击 **添加步骤** 以根据源码中的 Dockerfile 构建 Docker 镜像，在弹出的对话框中步骤类型下选择 shell，参并在命令行中输入以下命令，然后点击 **确定** 。

        ```docker
        docker build -f Dockerfile . -t $registry/$project/$name:latest
        ```

    - 点击 **添加步骤** 以登录镜像仓库，在弹出的对话框中步骤类型下选择 shell，参并在命令行中输入以下命令，然后点击 **确定** 。

        ```docker
        docker login $registry -u $USER -p $PASS
        ```

    - 点击 **添加步骤** 将镜像推送至镜像仓库中，在弹出的对话框中步骤类型下选择 shell，参并在命令行中输入以下命令，然后点击 **确定** 。

        ```docker
        docker push $registry/$project/$name:latest
        ```

7. 添加阶段 - 部署至集群

    - 点击画布中的 **添加阶段** 。在右侧的阶段设置中设置名称：deploy。

    - 在步骤模块中选择开启 **指定容器** ，在弹出的对话框中填写容器名称：go，然后点击 **确定** 。

        ![container2](https://docs.daocloud.io/daocloud-docs-images/docs/amamba/images/container2.png)

    - 在步骤模块中选择开启 **使用凭证** ，在弹出的对话框中填写相关参数，然后点击 **确定** 。

        - 凭证：选择 kubeconfig 类型的凭证。

        - kubeconfig 变量：如果您使用的是 kubectl apply 的部署方式，变量值必须为 KUBECONFIG。

        ![quickstart03](https://docs.daocloud.io/daocloud-docs-images/docs/amamba/images/quickstart03.png)

    - 点击 **添加步骤** 以进行集群部署操作，在弹出的对话框中步骤类型下选择 shell，参并在命令行中输入以下命令，然后点击 **确定** 。

        ```shell
        kubectl apply -f deploy.yaml
        ```

## 保存并执行流水线流水线

1. 完成上一步后点击 **保存并执行** 。

    ![quickstart05](https://docs.daocloud.io/daocloud-docs-images/docs/amamba/images/quickstart05.png)

2. 在弹出的对话框中输入步骤二中的示例参数。点击 **确定** 即可成功运行该流水线。

    ![build-para](https://docs.daocloud.io/daocloud-docs-images/docs/amamba/images/build-para.png)
