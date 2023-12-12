# 纳管边缘节点

纳管边缘节点就是在实际的边缘节点上根据批量注册边缘节点中创建任务的安装指南，获取到安装文件和接入命令，
安装边缘核心软件 EdgeCore，这样边缘节点就能与平台建立连接，纳入平台管理。

边缘节点初次纳管时，自动安装最新版本的边缘核心软件 EdgeCore。

!!! note

    在平台上注册的批量任务与实际的边缘节点机器是一对多的关系，一个批量任务的安装文件和接入命令可以在多台实际的边缘节点上使用。

## 前提条件

- 已经按要求准备好节点，并配置好节点环境，具体请参见[边缘节点接入要求](./join-rqmt.md)。
- 已经注册好节点批量任务并获取到安装指南，具体请参见[批量注册边缘节点](./batch-registration.md)。

![安装指南](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/kant/images/node-managed-01.png)

## 纳管边缘节点

1. 以具备 sudo 权限的用户登录边缘节点。

1. 根据节点运行时环境，执行相应的操作命令，从镜像仓库中获取安装文件。

    - 情境一：边缘节点可以直接访问镜像仓库，操作如下。

        直接从安装指南中复制镜像地址：

        ```shell
        release.daocloud.io/kant/kantadm-installation:v0.5.0-dev-7c54ddd4
        ```

        获取安装文件，可以参考以下示例：

        ```shell
        docker run --rm release.daocloud.io/kant/kantadm-installation:v0.5.0-dev-7c54ddd4 cat /usr/local/bin/kantadm > /usr/local/bin/kantadm && chmod +x /usr/local/bin/kantadm
        ```

    - 情境二：边缘节点无法访问镜像仓库，操作如下。

        1. 在安装指南界面，点击第一步`获取安装文件`按钮，右侧弹出获取安装文件抽屉。

        1. 根据节点运行时环境，将以下镜像安装包文件拷贝到指定文件夹下。
            
            Kant 安装包镜像
            
            ```
            release.daocloud.io/kant/kantadm-installation:v0.5.1
            ```
            KubeEdge Mosquitto 镜像 
              
            ```
            docker.m.daocloud.io/kubeedge/eclipse-mosquitto:1.6.15
            ```
            KubeEdge 容器沙箱镜像 
            
            ```
            kubeedge/pause:3.1
            ```
            KubeEdge 安装包镜像 
            
            ```
            docker.m.daocloud.io/kubeedge/installation-package:v1.12.5
            ```

            示例操作如下：

            1. 在一台可以访问镜像仓库的机器上执行操作命令，获取边端安装资源镜像。

                ```shell
                docker pull release.daocloud.io/kant/kantadm-installation:v0.5.1
                ```

            1. 将资源镜像打包，完成后上传至目标节点。

                ```shell
                docker save release.daocloud.io/kant/kantadm-installation:v0.5.0-dev-7c54ddd4 > kantadm-installation.tar
                ```

            1. 登录节点，加载已上传的资源镜像包。

                ```shell
                docker load -i kantadm-installation.tar
                ```

1. 执行如下命令，纳管边缘节点。

    - 通过 token 注册.

        ```shell
        kantadm join --cloudcore-host=10.31.226.14 --websocket-port=30000 --node-prefix=edge --token=b2d6bb5d9312c39ffac08ecfd5030bed006b8b67d0799d632d381f19fca9e765.eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2OTQ2NTk3NDV9.0sdaWbYSTURmAYmQwDn_zF7P9TwcRTSMhwPw6l87U7E --cgroup-driver=cgroupfs --remote-runtime-endpoint= --version=v1.12.2 --batch-name=edge --edge-registry=docker.m.daocloud.io/kubeedge --quic-port=30001 --http-port=30002 --stream-port=30003  --tunnel-port=30004 --labels=test=1,test1=1
        ```

    - 通过证书注册。

        1. 安装指南界面，第二步点击`证书安装`，弹出安装提示信息。

        1. 点击`下载证书`按钮，将证书下载到本地。

        1. 保存证书，执行如下命令。

            ```shell
            mkdir -p /etc/kant && mv ./cert.tar /etc/kant/cert.tar
            ```

        1. 接入纳管节点，执行如下命令。

            ```shell
            kantadm join --cloudcore-host=10.31.226.14 --websocket-port=30000 --node-prefix=edge --remote-runtime-endpoint= --cgroup-driver=cgroupfs --version=v1.12.2 --batch-name=edge --edge-registry=docker.m.daocloud.io/kubeedge --quic-port=30001 --http-port=30002 --stream-port=30003 --tunnel-port=30004 --labels=test=1,test1=1
            ```

1. 验证边缘节点是否纳管成功。

    1. 选择左侧导航栏的`边缘计算` -> `云边协同`，进入边缘单元列表页面。

    1. 点击边缘单元名称，进入边缘单元详情页。

    1. 选择左侧导航栏的`边缘资源` -> `边缘节点`，进入边缘节点列表页面。

    1. 查看边缘节点的状态，当前状态为`健康`表示纳管成功。

        ![边缘节点纳管成果](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/kant/images/node-managed-02.png)
