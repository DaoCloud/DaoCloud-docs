---
hide:
  - toc
---

# 离线安装 DCE 5.0 商业版

请在安装之前确保您以阅读并理解[部署规划](deploy-plan.md)、[部署架构](deploy-arch.md)、[准备工作](prepare.md)

请查看[产品发布记录](../release-notes.md)，避免所安装版本的已知问题

## 离线安装步骤

### 第一步 下载离线包

#### 离线镜像包

可以在[下载中心](https://docs.daocloud.io/download/dce5/)下载最新版本并使用

| 离线包                                | CPU 架构 | 版本   | 下载地址                                                     |
| :------------------------------------ | :------- | :----- | :----------------------------------------------------------- |
| offline-centos7-v0.4.0-amd64.tar      | AMD64    | v0.4.0 | [https://proxy-qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-centos7-v0.4.0-amd64.tar](https://proxy-qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-centos7-) |
| offline-kylin-v10sp2-v0.4.0-arm64.tar | ARM64    | v0.4.0 | [https://proxy-qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-kylin-v10sp2-v0.4.0-arm64.tar](https://proxy-qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-kylin-v10sp2-) |

下载完毕后解压离线包：

```bash
tar -xvf offline-centos7-v0.4.0-amd64.tar
```

#### ISO 离线包

ISO 离线包需要在集群配置文件中进行配置，请根据操作系统进行下载

| CPU 架构 | 操作系统版本                                        | 下载地址                                                     |
| :------- | :-------------------------------------------------- | :----------------------------------------------------------- |
| AMD64    | Centos 7                                            | https://mirrors.tuna.tsinghua.edu.cn/centos/7.9.2009/isos/x86_64/CentOS-7-x86_64-DVD-2009.iso |
| ARM64    | Kylin Linux Advanced Server release V10 (Sword) SP2 | 申请地址：https://www.kylinos.cn/scheme/server/1.html 注意：麒麟操作系统需要提供个人信息才能下载使用，下载时请选择 V10 (Sword) SP2 |

### 第二步 配置集群配置文件

集群配置文件会在离线镜像包 offline/sample 目录下，集群配置文件具体的参数介绍请参考[clusterconfig.yaml](cluster-config.md)

注：目前离线镜像包中提供了标准的 7 节点模式模版，后续还会内置更过的模版，敬请期待。

### 第三步 开始安装

1. 执行以下命令开始安装 DCE 5.0，安装器二进制文件位置：offline/dce5-installer

```shell
./offline/dce5-installer cluster-create -c ./offline/sample/clusterConfig.yaml -m ./offline/sample/manifest.yaml  -p ./offline/
```

!!! note

```
安装器脚本命令说明：
-c 参数用来指定 clusterConfig 文件，必选
-m 参数指定 manifest 文件，
-p 指定离线镜像文件
更多命令请使用 --help查询
```

1. 安装完成后，命令行会提示安装成功。恭喜您！现在可以通过屏幕提示的 URL 使用默认的账户和密码（admin/changeme）探索全新的 DCE 5.0 啦！

![success](../images/success.png)

!!! success

```
请记录好提示的 URL，方便下次访问。
```

1. 成功安装 DCE 5.0 商业版之后，请联系我们授权：电邮 info@daocloud.io 或致电 400 002 6898。
