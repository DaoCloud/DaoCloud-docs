# 在其他 Linux 上离线部署 DCE 5.0 商业版

本文将介绍如何在其他 Linux 上部署 DCE 5.0。
安装器 v0.7.0 及更高版本支持这种部署方式。

Other Linux 本质上是由于 DCE 对某些 Linux 没有提供安装系统离线包（OS package），需要您自己去制作。

## 已验证操作系统

| 架构  | 操作系统              | 所属系统族   | 推荐内核        |
| ----- | ------------------- | ------------ | ------------- |
| AMD64 | 统信 UOS V20 (1050d) | Debian | 4.19.0-server-amd64 |
| AMD64 | AnolisOS 8.8 GA  | Redhat | 5.10.134-13.an8.x86_64 |
| AMD64 | Ubuntu 22.04.3  | Debian | 5.15.0-78-generic |

!!! note

    没有验证的操作系统，可以尝试通过本文档的教程尝试部署。

## 前提条件

- 请提前阅读[部署架构](../commercial/deploy-arch.md)，确认本次部署模式。
- 请提前阅读[部署要求](../commercial/deploy-requirements.md)，确认网络、硬件、端口等是否符合需求。
- 请提前阅读[准备工作](../commercial/prepare.md)，确认机器资源及前置检查。

## 制作操作系统离线包（OS package）

### 制作及安装

1. 下载制作工具。

    ```bash
    cd /home
    curl -Lo ./pkgs.yml https://raw.githubusercontent.com/kubean-io/kubean/main/build/os-packages/others/pkgs.yml
    curl -Lo ./other_os_pkgs.sh https://raw.githubusercontent.com/kubean-io/kubean/main/build/os-packages/others/other_os_pkgs.sh && chmod +x other_os_pkgs.sh
    ```

2. 构建操作系统离线包

    ```bash
    # 指定 pkgs.yml 包配置文件路径（若 pkgs.yml 位于 other_os_pkgs.sh 同级路径，则可以不设置此环境变量）
    export PKGS_YML_PATH=/home/pkgs.yml
    # 执行系统离线包构建命令
    ./other_os_pkgs.sh build
    ```

3. 安装操作系统离线包

    ```bash
    # 指定 pkgs.yml 包配置文件路径（若 pkgs.yml 位于 other_os_pkgs.sh 同级路径，则可以不设置此环境变量）
    export PKGS_YML_PATH=/home/pkgs.yml
    # 指定 os pkgs 离线包的路径
    export PKGS_TAR_PATH=/home/os-pkgs-${DISTRO}-${VERSION}.tar.gz
    # 指定集群 master/worker 节点 IP（多节点 IP 地址以空格分割）
    export HOST_IPS='192.168.10.11 192.168.10.12'
    # 指定安装的目标节点接入信息（多节点用户名密码需保持一致）
    export SSH_USER=root
    export SSH_PASS=dangerous
    # 执行安装命令，并输出日志
    ./other_os_pkgs.sh install >>log.txt
    ```

4. 安装成功后，会输出如下日志：

    ```console
    [root@master test]# cat log.txt |egrep 'INFO|WARN'
    [WARN]   skip install yq ...
    [INFO]   succeed to install package 'python-apt'
    [INFO]   succeed to install package 'python3-apt'
    [INFO]   succeed to install package 'aufs-tools'
    [INFO]   succeed to install package 'apt-transport-https'
    [INFO]   succeed to install package 'software-properties-common'
    [INFO]   succeed to install package 'conntrack'
    [INFO]   succeed to install package 'apparmor'
    [WARN]   the package 'libseccomp2' has been installed
    [INFO]   succeed to install package 'ntp'
    [WARN]   the package 'openssl' has been installed
    [INFO]   succeed to install package 'curl'
    [INFO]   succeed to install package 'rsync'
    [INFO]   succeed to install package 'socat'
    [WARN]   the package 'unzip' has been installed
    [WARN]   the package 'e2fsprogs' has been installed
    [WARN]   the package 'xfsprogs' has been installed
    [INFO]   succeed to install package 'ebtables'
    [WARN]   the package 'bash-completion' has been installed
    [WARN]   the package 'tar' has been installed
    [INFO]   succeed to install package 'ipvsadm'
    [INFO]   succeed to install package 'ipset'
    [INFO]   All packages for Node (192.168.10.11) have been installed.
    ```

### 注意

1. 通过 `cat log.txt |egrep 'INFO|WARN'`检查安装情况：

    如果出现`failed to install package` 关键字，则说明未安装成功，并且最终失败时，
    会输出`the packages that failed to install are: ipset ipvsadm xfsprogs`。

2. 相同系统族（os family）的不同版本（major version）所对应的包名存在差异:

    | 系统族               | 版本  | 包名               |
    | -------------------- | ----- | ------------------ |
    | Debian               | < 11  | python-apt         |
    |                      | >= 11 | python3-apt        |
    | Redhat Major Version | < 8   | libselinux-python  |
    |                      | \>= 8 | python3-libselinux |

## 开始离线安装

1. 下载全模式离线包，可以在[下载中心](../../download/index.md)下载最新版本。

    | CPU 架构 | 版本   | 下载地址     |
    | -------- | ------ | --------- |
    | AMD64    | v0.17.0 | <https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-v0.17.0-amd64.tar> |

    下载完毕后解压离线包：

    ```bash
    curl -LO https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-v0.17.0-amd64.tar
    tar -xvf offline-v0.17.0-amd64.tar
    ```

2. 参考[制作操作系统离线包（OS package）](#os-package)。

3. 下载 addon 离线包，可以在[下载中心](../../download/index.md)下载最新版本（可选）

4. 设置[集群配置文件 clusterConfig.yaml](../commercial/cluster-config.md)，
   可以在离线包 `offline/sample` 下获取该文件并按需修改。

    === "UnionTech OS Server 20 1050d"

        ```yaml
        apiVersion: provision.daocloud.io/v1alpha3
        kind: ClusterConfig
        metadata:
        spec:
          clusterName: test-cluster
          loadBalancer:
            type: metallb
            istioGatewayVip: 172.30.41.XXX/32
            insightVip: 172.30.41.XXX/32
          masterNodes:
            - nodeName: "g-master1"
              ip: 172.30.41.xxx
              ansibleUser: "root"
              ansiblePass: "******"
          fullPackagePath: "/root/offline"
          osRepos:
            type: none
          imagesAndCharts:
            type: builtin
          binaries:
            type: builtin
          kubeanConfig: |-
          allow_unsupported_distribution_setup: true
            debian_os_family_extensions:
              - "UnionTech OS Server 20\" "
        ```

    === "AnolisOS 8.8 GA"

        ```yaml
        apiVersion: provision.daocloud.io/v1alpha3
        kind: ClusterConfig
        metadata:
        spec:
          clusterName: test-cluster
          loadBalancer:
            type: metallb
            istioGatewayVip: 172.30.41.XXX/32
            insightVip: 172.30.41.XXX/32
          masterNodes:
            - nodeName: "g-master1"
              ip: 172.30.41.xxx
              ansibleUser: "root"
              ansiblePass: "******"
          fullPackagePath: "/root/offline"
          osRepos:
            type: none
          imagesAndCharts:
            type: builtin
          binaries:
            type: builtin
          kubeanConfig: |-
          allow_unsupported_distribution_setup: true
            redhat_os_family_extensions:
              - "Anolis OS"
        ```

    === "Ubuntu 22.04.3"

        ```yaml
        apiVersion: provision.daocloud.io/v1alpha3
        kind: ClusterConfig
        metadata:
        spec:
          clusterName: test-cluster
          loadBalancer:
            type: metallb
            istioGatewayVip: 172.30.41.XXX/32
            insightVip: 172.30.41.XXX/32
          masterNodes:
            - nodeName: "g-master1"
              ip: 172.30.41.xxx
              ansibleUser: "root"
              ansiblePass: "******"
          fullPackagePath: "/root/offline"
          osRepos:
            type: none
          imagesAndCharts:
            type: builtin
          binaries:
            type: builtin
          kubeanConfig: |-
          allow_unsupported_distribution_setup: true
            debian_os_family_extensions:
              - "Debian"
        ```

    配置参数说明：

    | 参数 | 说明 | 是否必填 |
    | --- | ---- | ------ |
    | spec.kubeanConfig.allow_unsupported_distribution_setup | 是否跳过已支持发行版检测 | 必填 |
    | spec.kubeanConfig.debian_os_family_extensions          | 可通过查看 `ansible_os_family` 来填写 | 若为 Debian 系统族则需填写 |
    | spec.kubeanConfig.redhat_os_family_extensions          | 可通过查看 `ansible_os_family` 来填写 | 若为 Redhat 系统族则需填写 |

    如何查看当前发行版环境的系统族标识：

    ```bash
    export USER=root
    export PASS=xxxx
    export ADDR=192.168.10.xxx
    export ANSIBLE_HOST_KEY_CHECKING=False
    ansible -m setup -a 'filter=ansible_os_family' -e "ansible_user=${USER} ansible_password=${PASS}" -i ${ADDR}, all
    ```

    执行成功后将输出以下信息：

    ```bash
    192.168.10.xxx | SUCCESS => {
        "ansible_facts": {
            "ansible_os_family": "UnionTech OS Server 20\" ",
            "discovered_interpreter_python": "/usr/bin/python"
        },
        "changed": false
    }
    ```

5. 开始安装 DCE 5.0。

    ```bash
    ./dce5-installer cluster-create -m ./sample/manifest.yaml -c ./sample/clusterConfig.yaml
    ```

    !!! note

        部分参数介绍，更多参数可以通过 `./dce5-installer --help` 来查看：

        - `-z` 最小化安装
        - `-c` 指定集群配置文件，使用 NodePort 暴露控制台时不需要指定 `-c`
        - `-d` 开启 debug 模式
        - `--serial` 指定后所有安装任务串行执行

6. 安装完成后，命令行会提示安装成功。恭喜您！:smile: 现在可以通过屏幕提示的 URL 使用默认的账户和密码（admin/changeme）探索全新的 DCE 5.0 啦！

    ![success](https://docs.daocloud.io/daocloud-docs-images/docs/install/images/success.png)

    !!! success

        请记录好提示的 URL，方便下次访问。

7. 成功安装 DCE 5.0 商业版之后，请联系我们授权：电邮 [info@daocloud.io](mailto:info@daocloud.io) 或致电 400 002 6898。
