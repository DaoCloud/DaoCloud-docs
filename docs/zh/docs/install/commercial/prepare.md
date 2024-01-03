# 前置检查

本页说明了部署 DCE 5.0 需要进行的准备工作。

!!! note

    目前安装器的脚本中仅会针对火种机器进行前置检查，主要包含了是否已经安装前置依赖工具，及当前火种的 CPU > 10Core、Memory > 12G、disk > 100GB

## 机器检查

| **检查项** | **具体要求**  | **说明** |
| --------- | ------------ | ------- |
| 用户权限   | root                                   | 必须使用 root 用户部署，各个服务器也必须允许 root 用户 ssh 登录 |
| swap       | 关闭                                   | 如果不满足，系统会有一定几率出现 io 飙升，造成 容器运行时 卡死 |
| 防火墙     | 关闭（不强制）                         | -                                                            |
| selinux    | 关闭（不强制）                         | -                                                            |
| 时间同步   | 所有集群节点要求时间必须同步           | 这是 Docker 和 Kubernetes 官方要求。否则 kube.conf 会报错 `Unable to connect to the server: x509: certificate has expired or is not yet` |
| 时区       | 所有服务器时区必须统一                 | 建议设置为 Asia/Shanghai。 <br />参考命令：timedatectl set-timezone Asia/Shanghai |
| Nameserver | /etc/resolv.conf 至少有一个 Nameserver | CoreDNS 要求，否则会有报错。该 nameserver 在纯离线环境下可以是一个不存在的 IP 地址。Centos8minial 默认没有 /etc/resolv 文件，需要手动创建 |

## 火种机器依赖组件检查

| **检查项**   | **版本要求** | **说明** |
| ----------- | ----------- | ------- |
| podman      | v4.4.4      | -       |
| helm         | ≥ 3.11.1   | -       |
| skopeo       | ≥ 1.11.1   | -       |
| kind         | v0.19.0    | -       |
| kubectl      | ≥ 1.25.6   | -       |
| yq           | ≥ 4.31.1   | -       |
| minio client | `mc.RELEASE.2023-02-16T19-20-11Z` | |

如果不存在依赖组件，通过脚本进行安装依赖组件，[安装前置依赖](../install-tools.md)。

```bash
export VERSION=v0.13.0
# 下载脚本
curl -LO https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/install_prerequisite_${VERSION}.sh

# 添加可执行权限
chmod +x install_prerequisite_${VERSION}.sh

# 开始安装
bash install_prerequisite_${VERSION}.sh online full
```
