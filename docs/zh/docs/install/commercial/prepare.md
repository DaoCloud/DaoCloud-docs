# 准备工作

本页说明了部署 DCE 5.0 需要进行的准备工作。

## 机器准备

### all-in-one 模式

参阅 [all-in-one 模式说明](./deploy-arch.md#all-in-one)。

| **数量** | **服务器角色** | **服务器用途**                             | **cpu 数量** | **内存容量** | **系统硬盘** | **未分区的硬盘** |
| -------- | -------------- | ------------------------------------------ | ------------ | ------------ | ------------ | ---------------- |
| 1        | all in one     | 镜像仓库、chart museum 、global 集群本身 | 16 core      | 32G          | 200G         | 400G             |

### 4 节点模式

参阅 [4 节点模式说明](./deploy-arch.md#4)。

| **数量** | **服务器角色** | **服务器用途**                                               | **cpu 数量** | **内存容量** | **系统硬盘** | **未分区的硬盘** |
| -------- | -------------- | ------------------------------------------------------------ | ------------ | ------------ | ------------ | ---------------- |
| 1        | 火种节点       | 1. 执行安装部署程序<br />2. 运行平台所需的镜像仓库和 chart museum | 2            | 4G           | 200G         | -                |
| 3        | 控制面         | 1. 运行 DCE 5.0 组件<br /> 2. 运行 kubernetes 系统组件                 | 8            | 16G          | 100G         | 200G             |

### 7 节点模式(生产环境推荐)

参阅 [7 节点模式说明](./deploy-arch.md#7-1-6)。

| **数量** | **服务器角色** | **服务器用途**                                               | **cpu 数量** | **内存容量** | **系统硬盘** | **未分区的硬盘** |
| -------- | -------------- | ------------------------------------------------------------ | ------------ | ------------ | ------------ | ---------------- |
| 1        | 火种节点       | 1. 执行安装部署程序<br />2. 运行平台所需的镜像仓库和 chart museum | 2            | 4G           | 200G         | -                |
| 3        | master         | 1. 运行 DCE 5.0 组件<br /> 2. 运行 kubernetes 系统组件       | 8            | 16G          | 100G         | 200G             |
| 3        | worker         | 单独运行日志相关组件                                         | 8            | 16G          | 100G         | 200G             |

## 前置检查

### 机器检查

| **检查项** | **具体要求**                           | **说明**                                                     |
| ---------- | -------------------------------------- | ------------------------------------------------------------ |
| 用户权限   | root                                   | 必须使用 root 用户部署，各个服务器也必须允许 root 用户 ssh 登录 |
| swap       | 关闭                                   | 如果不满足，系统会有一定几率出现 io 飙升，造成 容器运行时 卡死 |
| 防火墙     | 关闭（不强制）                         | -                                                            |
| selinux    | 关闭（不强制）                         | -                                                            |
| 时间同步   | 所有集群节点要求时间必须同步           | 这是 Docker 和 Kubernetes 官方要求。否则 kube.conf 会报错 `Unable to connect to the server: x509: certificate has expired or is not yet` |
| 时区       | 所有服务器时区必须统一                 | 建议设置为 Asia/Shanghai。 <br />参考命令：timedatectl set-timezone Asia/Shanghai |
| Nameserver | /etc/resolv.conf 至少有一个 Nameserver | CoreDNS 要求，否则会有报错。该 nameserver 在纯离线环境下可以是一个不存在的 IP 地址。Centos8minial 默认没有 /etc/resolv 文件，需要手动创建 |

### 火种机器依赖组件检查

| **检查项**   | **版本要求**                                                           | **说明**                          |
| ------------ |--------------------------------------------------------------------| --------------------------------- |
| podman       | v4.4.4                                                             | -                                 |
| helm         | ≥ 3.11.1                                                           | -                                 |
| skopeo       | ≥ 1.11.1                                                           | -                                 |
| kind         | v0.19.0                                                            | -                                 |
| kubectl      | ≥ 1.25.6                                                           | -                                 |
| yq           | ≥ 4.31.1                                                           | -                                 |
| minio client | `mc.RELEASE.2023-02-16T19-20-11Z`                                 |                   |

如果不存在依赖组件，通过脚本进行安装依赖组件，[安装前置依赖](../install-tools.md)。

```bash
export VERSION=v0.9.0
# 下载脚本
curl -LO https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/install_prerequisite_${VERSION}.sh

# 添加可执行权限
chmod +x install_prerequisite_${VERSION}.sh

# 开始安装
bash install_prerequisite_${VERSION}.sh online full
```

## 外接组件准备

如果需要使用客户已有的一些组件，可以参考以下文档进行准备：

- [使用外接服务存储 Binaries 资源](external/external-binary.md)

- [使用外接镜像仓库与 Chart 仓库存储镜像与 Chart 包](external/external-imageandchart.md)

- [使用外接中间件服务](external/external-middlewares.md)

- [使用外接服务存储 OS Repo 资源](external/external-os.md)
