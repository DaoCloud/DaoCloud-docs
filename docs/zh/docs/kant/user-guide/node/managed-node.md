# 纳管边缘节点

纳管边缘节点就是在实际的边缘节点上根据批量注册边缘节点中创建任务的安装指南，获取到安装文件和接入命令，安装边缘核心软件 EdgeCore，这样边缘节点就能与平台建立连接，纳入平台管理。

边缘节点初次纳管时，自动安装最新版本的边缘核心软件 EdgeCore。

说明：

在平台上注册的批量任务与实际的边缘节点机器是一对多的关系，一个批量任务的安装文件和接入命令可以在多台实际的边缘节点上使用。

## 前提条件

- 已经按要求准备好节点，并配置好节点环境，具体请参见[边缘节点接入要求](./join-rqmt.md)。

- 已经注册好节点批量任务并获取到安装指南，具体请参见批量注册边缘节点[批量注册边缘节点](./batch-registration.md)。

![安装指南](../../images/node-managed-01.png)

## 纳管边缘节点

1. 以具备 sudo 权限的用户登录边缘节点。

2. 根据节点运行时环境，执行相应的操作命令，从镜像仓库中获取安装文件。

    - 情境一：边缘节点可以直接访问镜像仓库，操作如下。

        镜像地址可以从安装指南中直接复制：


        ```shell
        release.daocloud.io/kant/kantadm-installation:v0.5.0-dev-7c54ddd4
        ```

        获取安装文件，可以参考给出的示例：

        ```shell
        docker run --rm release.daocloud.io/kant/kantadm-installation:v0.5.0-dev-7c54ddd4 cat /usr/local/bin/kantadm > /usr/local/bin/kantadm && chmod +x /usr/local/bin/kantadm
        ```

    - 情境二：边缘节点无法访问镜像仓库，操作如下。

        安装指南界面，点击第一步`获取安装文件`按钮，右侧弹出获取安装文件抽屉。

        根据节点运行时环境，将镜像安装包文件拷贝到指定文件夹下。

        镜像地址直接从界面复制：

        ```shell
        release.daocloud.io/kant/kantadm-installation:v0.5.0-dev-7c54ddd4
        ```

        示例操作如下：

        a.在一台可以访问镜像仓库的机器上执行操作命令，获取边端安装资源镜像。

        ```shell
        docker pull release.daocloud.io/kant/kantadm-installation:v0.5.0-dev-7c54ddd4
        ```

        b.将资源镜像打包，完成后上传至目标节点。

        ```shell
        docker save release.daocloud.io/kant/kantadm-installation:v0.5.0-dev-7c54ddd4 > kantadm-installation.tar
        ```

        c.登录节点，加载已上传的资源镜像包。

        ```shell
        docker load -i kantadm-installation.tar
        ```

3.执行如下命令，纳管边缘节点。

- 通过 token 注册.

    ```shell
    kantadm join --cloudcore-host=10.31.226.14 --websocket-port=30000 --node-prefix=edge --token=b2d6bb5d9312c39ffac08ecfd5030bed006b8b67d0799d632d381f19fca9e765.eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2OTQ2NTk3NDV9.0sdaWbYSTURmAYmQwDn_zF7P9TwcRTSMhwPw6l87U7E --cgroup-driver=cgroupfs --remote-runtime-endpoint= --version=v1.12.2 --batch-name=edge --edge-registry=docker.m.daocloud.io/kubeedge --quic-port=30001 --http-port=30002 --stream-port=30003  --tunnel-port=30004 --labels=test=1,test1=1
    ```

- 通过证书注册。

    a.安装指南界面，第二步点击`证书安装`，弹出安装提示信息。

    b.点击`下载证书`按钮，将证书下载到本地。

    c.保存证书，执行如下命令。

    ```shell
    mkdir -p /etc/kant && mv ./cert.tar /etc/kant/cert.tar
    ```

    d.接入纳管节点，执行如下命令。

    ```shell
    kantadm join --cloudcore-host=10.31.226.14 --websocket-port=30000 --node-prefix=edge --remote-runtime-endpoint= --cgroup-driver=cgroupfs --version=v1.12.2 --batch-name=edge --edge-registry=docker.m.daocloud.io/kubeedge --quic-port=30001 --http-port=30002 --stream-port=30003 --tunnel-port=30004 --labels=test=1,test1=1
    ```

4.验证边缘节点是否纳管成功。

- a.选择左侧导航栏的`边缘计算` -> `云边协同`，进入边缘单元列表页面。

- b.点击边缘单元名称，进入边缘单元详情页。

- c.选择左侧导航栏的`边缘资源` -> `边缘节点`，进入边缘节点列表页面。

- d.查看边缘节点的状态，当前状态为“健康”表示纳管成功。

![边缘节点纳管成果](../../images/node-managed-02.png)



        


