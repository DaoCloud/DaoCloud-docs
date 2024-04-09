# 在 OpenShift OCP 上安装 DCE 5.0 商业版

本文将介绍如何在 OCP 上安装 DCE 5.0。

## 前提条件

- DCE 5.0 默认支持的 Kubernetes 版本为 v1.22.x、v1.23.x、v1.24.x、v1.25.x、v1.26.x
- 已经拥有一个 OCP 环境，并且版本不低于 v1.22.x
- 准备一个私有镜像仓库，并且保证集群可以访问到
- 确保资源充足，建议集群至少还有 12 核 24 GB 的可用资源

## 离线安装

1. 通过堡垒机登录到 Control plane 节点。

2. 下载全模式离线包，可以在[下载中心](../../download/index.md)下载最新版本。

    | CPU 架构 | 版本   | 下载地址                                                                                          |
    | -------- | ------ | ------------------------------------------------------------------------------------------------- |
    | AMD64    | v0.16.1 | <https://proxy-qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-v0.16.1-amd64.tar> |
    | ARM64     | v0.16.1 | <https://proxy-qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-v0.16.1-arm64.tar> |

    下载完毕后解压离线包：

    ```bash
    ## 以 amd64 架构离线包为例
    tar -xvf offline-v0.16.1-amd64.tar
    ```

3. 设置[集群配置文件 clusterConfig.yaml](../commercial/cluster-config.md)，可以在离线包 `offline/sample` 下获取该文件并按需修改。

    参考配置为：

    ```yaml
    apiVersion: provision.daocloud.io/v1alpha3
    kind: ClusterConfig
    metadata:
      creationTimestamp: null
    spec:
      loadBalancer:
        type: metallb # 建议 metallb
        istioGatewayVip: 10.5.14.XXX/32
        insightVip: 10.5.14.XXX/32
      fullPackagePath: /home/offline # 离线包目录
      imagesAndCharts:
        type: external
        externalImageRepo: http://10.5.14.XXX:XXXX # 私有镜像仓库地址
        externalImageRepoUsername: admin
        externalImageRepoPassword: Harbor12345
    ```

4. 配置 manifest 文件（可选），可以在离线包 `offline/sample` 下获取该文件并按需修改。

    !!! note

        如果要使用 `hwameiStor`作为 StorageClass，请确保当前集群中有没有默认的 StorageClass。
        如果有，需要去除。如果不去除，默认 StorageClass 需要关闭 `hwameiStor`，即更改 enable 的值为 `fasle`。

5. 开始安装 DCE 5.0。

    ```bash
    ./offline/dce5-installer install-app -m ./offline/sample/manifest.yaml -c ./offline/sample/clusterConfig.yaml --platform openshift -z
    ```

    !!! note

        部分参数介绍，更多参数可以通过 `./dce5-installer --help` 来查看：

        - `-z` 最小化安装
        - `-c` 指定集群配置文件，使用 NodePort 暴露控制台时不需要指定 -c
        - `-d` 开启 debug 模式
        - `--platform` 用来声明在哪个 Kubernetes 发行版上部署 DCE 5.0，目前仅支持 openshift
        - `--serial` 指定后所有安装任务串行执行

6. 安装完成后，命令行会提示安装成功。恭喜您！:smile: 现在可以通过屏幕提示的 URL 使用默认的账户和密码（admin/changeme）探索全新的 DCE 5.0 啦！

    ![success](https://docs.daocloud.io/daocloud-docs-images/docs/install/images/success.png)

    !!! success

        请记录好提示的 URL，方便下次访问。

7. 成功安装 DCE 5.0 商业版之后，请联系我们授权：电邮 [info@daocloud.io](mailto:info@daocloud.io) 或致电 400 002 6898。
