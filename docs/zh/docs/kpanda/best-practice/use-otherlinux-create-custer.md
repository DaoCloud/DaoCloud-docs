# 在非主流操作系统上创建集群

本文介绍离线模式下如何在 **未声明支持的 OS** 上创建工作集群。DCE 5.0 声明支持的 OS 范围请参考
[DCE 5.0 支持的操作系统](../../install/commercial/deploy-requirements.md)

离线模式下在未声明支持的 OS 上创建工作集群，主要的流程如下图：

![流程](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/kpanda/images/otherlinux.png)

接下来，本文将以 openAnolis 操作系统为例，介绍如何在非主流操作系统上创建集群。

## 前提条件

- 已经部署好一个 DCE 5.0 全模式，部署参考文档[离线安装 DCE 5.0 商业版](../../install/commercial/start-install.md)
- 至少拥有一台可以联网的同架构同版本的节点。

## 在线节点构建离线包

找到一个和待建集群节点架构和 OS 均一致的在线环境，本文以 [AnolisOS 8.8 GA](https://openanolis.cn/download) 为例。执行如下命令，生成离线 os-pkgs 包。

```bash
# 下载相关脚本并构建 os packages 包
curl -Lo ./pkgs.yml https://raw.githubusercontent.com/kubean-io/kubean/main/build/os-packages/others/pkgs.yml
curl -Lo ./other_os_pkgs.sh https://raw.githubusercontent.com/kubean-io/kubean/main/build/os-packages/others/other_os_pkgs.sh && chmod +x  other_os_pkgs.sh
./other_os_pkgs.sh build # 构建离线包
```

执行完上述命令后，预期将在当前路径下生成一个名为 `os-pkgs-anolis-8.8.tar.gz` 的压缩包。当前路径下文件目录大概如下：

```console
    .
    ├── other_os_pkgs.sh
    ├── pkgs.yml
    └── os-pkgs-anolis-8.8.tar.gz
```

## 离线节点安装离线包

将在线节点中生成的 `other_os_pkgs.sh`、`pkgs.yml`、`os-pkgs-anolis-8.8.tar.gz` 三个文件拷贝至离线环境中的待建集群的**所有**节点上。

登录离线环境中，任一待建集群的其中一个节点上，执行如下命令，为节点安装 os-pkg 包。

```bash
# 配置环境变量
export PKGS_YML_PATH=/root/workspace/os-pkgs/pkgs.yml # 当前离线节点 pkgs.yml 文件的路径
export PKGS_TAR_PATH=/root/workspace/os-pkgs/os-pkgs-anolis-8.8.tar.gz # 当前离线节点 os-pkgs-anolis-8.8.tar.gz 的路径
export SSH_USER=root # 当前离线节点的用户名
export SSH_PASS=dangerous # 当前离线节点的密码
export HOST_IPS='172.30.41.168' # 当前离线节点的 IP
./other_os_pkgs.sh install #安装离线包
```

执行完成上述命令后，等待界面提示： `All packages for node (X.X.X.X) have been installed` 即表示安装完成。

## 下一步

参考文档[创建工作集群](../user-guide/clusters/create-cluster.md)，在 UI 界面上创建 openAnolis 集群。
