# 推送镜像

创建托管 Harbor 和镜像空间后，您可以按照如下说明登录并将镜像推送的镜像仓库中；
或者登录原生 Harbor，查看原生 Harbor 在每个镜像空间（项目）下提供的引导。

## 推送方式一

前提：已创建托管 Harbor 和镜像空间

您可在本地构建新的容器镜像或从 DockerHub 上获取一个公开镜像用于测试。
本文以 DockerHub 官方的 Nginx 最新镜像为例，在命令行工具中依次执行以下指令，即可推送该镜像。
请将 library 及 `nginx` 依次替换为您实际创建的镜像空间名称及镜像仓库名。

1. 登录镜像仓库

    ```bash
    docker login --username=<镜像仓库登录名> <镜像仓库地址>
    ```

    示例：`docker login --username=admin http://test.lrf02.kangaroo.com`

    在返回结果中输入镜像仓库密码（创建托管 Harbor 时设置的密码）。

1. 给镜像加标签

    执行以下命令，给镜像打标签。

    ```bash
    docker tag <镜像仓库名称>:<镜像版本号> <镜像仓库地址>/<镜像空间名称>/<镜像仓库名称>:<镜像版本号>
    ```

    示例：`docker tag nginx:latest test.lrf02.kangaroo.com/library/nginx:latest`

1. 推送镜像

    执行以下命令，推送镜像至镜像空间 library 中。

    ```bash
    docker push <镜像仓库地址>/<镜像空间名称>/<镜像仓库名称>:<镜像版本号>
    ```

    示例：`docker push test.lrf02.kangaroo.com/library/nginx:latest`

1. 拉取镜像

    执行以下命令，拉取镜像。

    ```bash
    docker pull <镜像仓库地址>/<镜像空间名称>/<镜像仓库名称>:<镜像版本号>
    ```

    示例：`docker pull test.lrf02.kangaroo.com/library/nginx:latest`

## 推送方式二

前提：已创建托管 Harbor 和镜像空间。

1. 在托管 Harbor 列表页面中，点击目标镜像仓库右侧的 `...`，点击`原生 Harbor`，进入原生 Harbor 的登录页。

    ![原生 Harbor](https://docs.daocloud.io/daocloud-docs-images/docs/kangaroo/images/push01.png)

1. 输入创建托管 Harbor 时设置的用户名和密码进入原生 Harbor。

    ![输入用户名和密码](https://docs.daocloud.io/daocloud-docs-images/docs/kangaroo/images/push02.png)

1. 点击目标镜像空间（项目）的名称，进入镜像空间。

    ![镜像空间](https://docs.daocloud.io/daocloud-docs-images/docs/kangaroo/images/push03.png)

1. 点击右侧的推送命令，查看原生 Harbor 提供的推送命令。

    ![查看推送命令](https://docs.daocloud.io/daocloud-docs-images/docs/kangaroo/images/push04.png)

!!! tip

    相对于[方式一](#_2)，原生 Harbor 的推送命令自动填入了镜像仓库地址和镜像空间名称。
