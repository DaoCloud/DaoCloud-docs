---
hide:
  - toc
---

# 离线安装 DCE 5.0 商业版

请在安装之前确保您以阅读并理解[部署要求](deploy-requirements.md)、[部署架构](deploy-arch.md)、[准备工作](prepare.md)

请查看[产品发布记录](../release-notes.md)，避免所安装版本的已知问题，以及查看新增功能

## 离线安装步骤

### 第 1 步：下载离线包

请根据业务环境下载对应的离线包。

#### 离线镜像包 （必需）

可以在[下载中心](https://docs.daocloud.io/download/dce5/)下载最新版本。

| CPU 架构 | 版本   | 下载地址                                                     |
| :------- | :----- | :----------------------------------------------------------- |
| AMD64    | v0.6.1 | https://proxy-qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-v0.6.1-amd64.tar |
| ARM64    | v0.6.1 | https://proxy-qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-v0.6.1-arm64.tar |

下载完毕后解压离线包：

```bash
# 以 amd64 架构离线包为例
tar -xvf offline-v0.6.1-amd64.tar
```

#### addon 离线包 （可选）

安装器从 v0.5.0 版本，支持了 addon 的离线包导入能力，如果需要支持 addon 中所有的 helm chart 离线化。可以在[下载中心](https://docs.daocloud.io/download/dce5/)下载最新版本。

首先需要事先下载好离线包，并在[集群配置文件（clusterConfig.yaml）](./cluster-config.md)中定义 `addonOfflinePackagePath`。

| CPU 架构 | 版本   | 下载地址                                                     |
| :------- | :----- | :----------------------------------------------------------- |
| AMD64    | v0.6.0 | https://qiniu-download-public.daocloud.io/DaoCloud_DigitalX_Addon/addon-offline-full-package-v0.6.0-amd64.tar.gz |
| ARM64    | v0.6.0 | https://qiniu-download-public.daocloud.io/DaoCloud_DigitalX_Addon/addon-offline-full-package-v0.6.0-arm64.tar.gz |

#### ISO 离线包 （必需）

ISO 离线包需要在[集群配置文件](./cluster-config.md)中进行配置，请根据操作系统进行下载。

| CPU 架构 | 操作系统版本                                        | 下载地址                                                     |
| :------- | :-------------------------------------------------- | :----------------------------------------------------------- |
| AMD64    | Centos 7                                            | https://mirrors.tuna.tsinghua.edu.cn/centos/7.9.2009/isos/x86_64/CentOS-7-x86_64-DVD-2009.iso |
|          | Redhat 7、8                                          | https://developers.redhat.com/products/rhel/download#assembly-field-downloads-page-content-61451<br />注意：Redhat 操作系统需要 Redhat 的账号才可以下载 |
| ARM64    | Kylin Linux Advanced Server release V10 (Sword) SP2 | 申请地址：https://www.kylinos.cn/scheme/server/1.html <br />注意：麒麟操作系统需要提供个人信息才能下载使用，下载时请选择 V10 (Sword) SP2 |

#### osPackage 离线包 （必需）

安装器从 v0.5.0 版本，需要提供操作系统的 osPackage 离线包，并在[集群配置文件（clusterConfig.yaml）](./cluster-config.md)中定义 `osPackagePath`。

其中 [Kubean](https://github.com/kubean-io/kubean) 提供了不同操作系统的osPackage 离线包，可以前往 https://github.com/kubean-io/kubean/releases/tag/v0.4.8 查看。

| 操作系统版本                                        | 下载地址                                                     |
| :-------------------------------------------------- | :----------------------------------------------------------- |
| Centos 7                                            | https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.4.8/os-pkgs-centos7-v0.4.8.tar.gz |
| Redhat 8                                            | https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.4.8/os-pkgs-redhat8-v0.4.8.tar.gz |
| Redhat 7                                            | https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.4.8/os-pkgs-redhat7-v0.4.8.tar.gz |
| Kylin Linux Advanced Server release V10 (Sword) SP2 | https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.4.8/os-pkgs-kylinv10-v0.4.8.tar.gz |

### 第 2 步：配置集群配置文件

集群配置文件位于离线镜像包 `offline/sample` 目录下，具体的参数介绍请参考 [clusterConfig.yaml](cluster-config.md)。

!!! note

    目前离线镜像包中提供了标准的 7 节点模式模板。

### 第 3 步：开始安装

1. 执行以下命令开始安装 DCE 5.0，安装器二进制文件位置为 `offline/dce5-installer`

    ```shell
    ./offline/dce5-installer cluster-create -c ./offline/sample/clusterConfig.yaml -m ./offline/sample/manifest.yaml
    ```

    !!! note

        安装器脚本命令说明：
    
        - -c 来指定集群配置文件，必选
        - -m 参数指定 manifest 文件，
        - -z 最小化安装
        - -d 开启 debug 模式
        - 更多命令请使用 --help 查询

1. 安装完成后，命令行会提示安装成功。恭喜您！现在可以通过屏幕提示的 URL 使用默认的账号和密码（admin/changeme）探索全新的 DCE 5.0 啦！

    ![success](../images/success.png)

    !!! success

        请记录好提示的 URL，方便下次访问。

1. 成功安装 DCE 5.0 商业版之后，请联系我们授权：电邮 info@daocloud.io 或致电 400 002 6898。
