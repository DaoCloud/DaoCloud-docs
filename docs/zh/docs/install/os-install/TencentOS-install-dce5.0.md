# TencentOS Server 3.1 操作系统上部署 DCE 5.0 商业版

本文将介绍如何在 TencentOS Server 3.1 操作系统上部署 DCE 5.0，v0.9.0 及以上支持。

## 前提条件

- 请提前阅读[部署架构](../commercial/deploy-arch.md)，确认本次部署模式。
- 请提前阅读[部署要求](../commercial/deploy-requirements.md)，确认网络、硬件、端口等是否符合需求。
- 请提前阅读[准备工作](../commercial/prepare.md)，确认机器资源及前置检查。

## 离线安装

1. 下载全模式离线包，可以在[下载中心](https://docs.daocloud.io/download/dce5/)下载最新版本。

    | CPU 架构 | 版本   | 下载地址                                                                                          |
    | -------- | ------ | ------------------------------------------------------------------------------------------------- |
    | AMD64    | v0.9.0 | <https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-v0.9.0-amd64.tar> |

    下载完毕后解压离线包：

    ```bash
    curl -LO https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-v0.9.0-amd64.tar
    tar -xvf offline-v0.9.0-amd64.tar
    ```

2. 下载 TencentOS Server 3.1 镜像文件。

    ```bash
    curl -LO http://mirrors.tencent.com/tlinux/3.1/iso/x86_64/TencentOS-Server-3.1-TK4-x86_64-minimal-2209.3.iso
    ```

3. 下载 TencentOS Server 3.1 osPackage 离线包。

     ```bash
    curl -LO https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.6.6/os-pkgs-tencent31-v0.6.6.tar.gz
    ```

4. 下载 addon 离线包，可以在[下载中心](../../download/index.md)下载最新版本（可选）

5. 设置[集群配置文件 clusterConfig.yaml](../commercial/cluster-config.md)，可以在离线包 `offline/sample` 下获取该文件并按需修改。
    参考配置为：

    ```yaml
    apiVersion: provision.daocloud.io/v1alpha3
    kind: ClusterConfig
    metadata:
    spec:
      clusterName: tencent-cluster
      loadBalancer:
        type: metallb
        istioGatewayVip: 172.30.41.XXX/32
        insightVip: 172.30.41.XXX/32
      masterNodes:
        - nodeName: "g-master"
          ip: 172.30.41.XXX
          ansibleUser: "root"
          ansiblePass: "******"
      fullPackagePath: "/root/workspace/offline"
      osRepos:
        type: builtin
        isoPath: "/root/workspace/iso/TencentOS-Server-3.1-TK4-x86_64-minimal-2209.3.iso"
        osPackagePath: "/root/workspace/os-pkgs/os-pkgs-tencent31-v0.6.1.tar.gz"
      imagesAndCharts:
        type: builtin
      binaries:
        type: builtin
      kubeanConfig: |-
        allow_unsupported_distribution_setup: true
        redhat_os_family_extensions:
          - "TencentOS"
    ```

    !!! note

        - TencentOS Server 3.1 操作系统属于 Redhat 系统族，所以需要在 kubeanConfig 中定义 `redhat_os_family_extensions` 参数。
        - 执行如下命令查看 TencentOS Server 3.1 操作系统的 OS Family 标识，输出结果为 `TencentOS`。

            ```bash
            export USER=root
            export PASS=dangerous
            export ADDR=172.30.41.166
            export ANSIBLE_HOST_KEY_CHECKING=False
            ansible -m setup -a 'filter=ansible_os_family' -e "ansible_user=${USER} ansible_password=${PASS}" -i ${ADDR}, all
            ```

6. 开始安装 DCE 5.0。

    ```bash
    ./dce5-installer cluster-create -m ./sample/mainfest.yaml -c ./sample/clusterConfig.yaml
    ```

    !!! note

        部分参数介绍，更多参数可以通过 `./dce5-installer --help` 来查看：

        - `-z` 最小化安装
        - `-c` 指定集群配置文件，使用 NodePort 暴露控制台时不需要指定 `-c`
        - `-d` 开启 debug 模式
        - `--serial` 指定后所有安装任务串行执行

7. 安装完成后，命令行会提示安装成功。恭喜您！:smile: 现在可以通过屏幕提示的 URL 使用默认的账户和密码（admin/changeme）探索全新的 DCE 5.0 啦！

    ![success](https://docs.daocloud.io/daocloud-docs-images/docs/install/images/success.png)

    !!! success

        请记录好提示的 URL，方便下次访问。

8. 成功安装 DCE 5.0 商业版之后，请联系我们授权：电邮 [info@daocloud.io](mailto:info@daocloud.io) 或致电 400 002 6898。
