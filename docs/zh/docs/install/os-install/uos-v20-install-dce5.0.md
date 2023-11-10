# UOS V20 (1020a) 操作系统上部署 DCE 5.0 商业版

本文将介绍如何在 UOS V20(1020a) 操作系统上部署 DCE 5.0，v0.6.0 及以上支持。

## 前提条件

- 请提前阅读[部署架构](../commercial/deploy-arch.md)，确认本次部署模式。
- 请提前阅读[部署要求](../commercial/deploy-requirements.md)，确认网络、硬件、端口等是否符合需求。
- 请提前阅读[准备工作](../commercial/prepare.md)，确认机器资源及前置检查。

## 离线安装

1. 由于安装器依赖 python，所以需要在火种机器中先安装 `python3.6`。

    ```bash
    ## 执行以下命令下载依赖
    dnf install -y --downloadonly --downloaddir=rpm/python36

    ## 执行以下命令开始安装
    rpm -ivh python3-pip-9.0.3-18.uelc20.01.noarch.rpm python3-setuptools-39.2.0-7.uelc20.2.noarch.rpm python36-3.6.8-2.module+uelc20+36+6174170c.x86_64.rpm
    ```

2. 下载全模式离线包，可以在[下载中心](../../download/index.md)下载最新版本。

    | CPU 架构 | 版本   | 下载地址    |
    | -------- | ----- | -------- |
    | AMD64    | v0.6.1 | <https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-v0.6.1-amd64.tar> |

    下载完毕后解压离线包：

    ```bash
    curl -LO https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-v0.6.1-amd64.tar
    tar -xvf offline-v0.6.1-amd64.tar
    ```

3. 下载 UnionTech Server V20 1020a ISO 镜像文件。

    ```bash
    curl -LO https://cdimage-download.chinauos.com/uniontechos-server-20-1020a-amd64.iso
    ```

4. 制作 **os-pkgs-uos-20.tar.gz** 文件。

    下载制作脚本

    ```bash
    curl -Lo ./build.sh https://raw.githubusercontent.com/kubean-io/kubean/main/build/os-packages/others/uos_v20/build.sh
    chmod +x build.sh
    ```

    执行脚本生成 **os-pkgs-uos-20.tar.gz** 文件：

    ```bash
    ./build.sh
    ```

5. 下载 addon 离线包，可以在[下载中心](../../download/index.md)下载最新版本（可选）

6. 设置[集群配置文件 clusterConfig.yaml](../commercial/cluster-config.md)，可以在离线包 `offline/sample` 下获取该文件并按需修改。
    参考配置为：

    ```yaml
    apiVersion: provision.daocloud.io/v1alpha3
    kind: ClusterConfig
    metadata:
    spec:
      clusterName: my-cluster
      loadBalancer:
        type: metallb
        istioGatewayVip: 172.30.41.XXX/32
        insightVip: 172.30.41.XXX/32
      masterNodes:
        - nodeName: "g-master1"
          ip: 10.5.14.XXX
          ansibleUser: "root"
          ansiblePass: "******"
      fullPackagePath: "/home/offline"
      osRepos:
        type: builtin
        isoPath: "/home/uniontechos-server-20-1020a-amd64.iso" ## ISO 的目录
        osPackagePath: "/home/os-pkgs-uos-20.tar.gz" ## os-pkgs 的目录
      imagesAndCharts:
        type: builtin
      addonPackage:
        path: "/home/addon-offline-full-package-v0.5.3-alpha2-amd64.tar.gz" ## addon 的目录
      binaries:
        type: builtin
    ```

7. 开始安装 DCE 5.0。

    ```bash
    ./dce5-installer cluster-create -m ./sample/mainfest.yaml -c ./sample/clusterConfig.yaml
    ```

    !!! note

        部分参数介绍，更多参数可以通过 `./dce5-installer --help` 来查看：

        - `-z` 最小化安装
        - `-c` 指定集群配置文件，使用 NodePort 暴露控制台时不需要指定 `-c`
        - `-d` 开启 debug 模式
        - `--serial` 指定后所有安装任务串行执行

8. 安装完成后，命令行会提示安装成功。恭喜您！:smile: 现在可以通过屏幕提示的 URL 使用默认的账户和密码（admin/changeme）探索全新的 DCE 5.0 啦！

    ![success](https://docs.daocloud.io/daocloud-docs-images/docs/install/images/success.png)

    !!! success

        请记录好提示的 URL，方便下次访问。

9. 成功安装 DCE 5.0 商业版之后，请联系我们授权：电邮 [info@daocloud.io](mailto:info@daocloud.io) 或致电 400 002 6898。
