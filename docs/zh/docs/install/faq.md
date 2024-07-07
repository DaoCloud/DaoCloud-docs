# 安装排障

本页汇总了常见的安装问题及排障方案，便于用户快速解决安装及运行过程中遇到的问题。

## DCE 5.0 界面打不开时，执行 diag.sh 脚本快速排障

安装器自 v0.12.0 版本之后新增了 diag.sh 脚本，方便用户在 DCE 5.0 界面打不开时快速排障。

执行命令：

```bash
./offline/diag.sh
```

执行结果示例：

![FAQ1](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/install/images/faq11.png)

## kind 容器重启后，kubelet 服务无法启动

kind 容器重启后，kubelet 服务无法启动，并报以下错误：

```text
failed to initialize top level QOS containers: root container [kubelet kubepods] doesn't exist
```

解决方案：

- 方案 1：重启，执行命令 `podman restart [kind] --time 120`，执行过程中不能通过 Ctrl+C 中断该任务

- 方案 2：运行 `podman exec` 进入 kind 容器，执行以下命令：
  
    ```bash
    for i in $(systemctl list-unit-files --no-legend --no-pager -l | grep --color=never -o .*.slice | grep kubepod);
    do systemctl stop $i;
    done
    ```

## 禁用 IPv6 后安装时 Podman 无法创建容器

报错信息如下：

```text
ERROR: failed to create cluster: command "podman run --name kind-control-plane...
```

解决方案：重新启用 IPv6 或者更新火种节点底座为 Docker。

Podman 相关 Issue 地址：
https://github.com/containers/podman/issues/13388

## kind 集群重装 DCE 5.0 时 Redis 卡住

问题：Redis Pod 出现了 0/4 running 很久的情况，提示：`primary ClusterIP can not unset`

1. 在 `mcamel-system` 命名空间下删除 rfs-mcamel-common-redis

    ```shell
    kubectl delete svc rfs-mcamel-common-redis -n mcamel-system
    ```

1. 然后重新执行安装命令

## 使用 Metallb 时 VIP 访问不通导致 DCE 登录界面无法打开

1. 排查 VIP 的地址是否和主机在同一个网段，Metallb L2 模式下需要确保在同一个网段
2. 如果是在 Global 集群中的控制节点新增了网卡导致访问不通，需要手动配置 L2Advertisement。
   
    请参考 [Metallb 这个问题的文档](https://metallb.universe.tf/configuration/_advanced_l2_configuration/#specify-network-interfaces-that-lb-ip-can-be-announced-from)。

## 社区版 fluent-bit 安装失败

报错：

```text
DaemonSet is not ready: insight-system/insight-agent-fluent-bit. 0 out of 2 expected pods are ready
```

排查 Pod 日志是否出现下述关键信息：

```text
[warn] [net] getaddrinfo(host='mcamel-common-es-cluster-masters-es-http.mcamel-system.svc.cluster.local',errt11):Could not contact DNS servers
```

出现上述问题是一个 fluent-bit 的 bug，可以参考：
https://github.com/aws/aws-for-fluent-bit/issues/233

## 在 CentOS 7.6 安装时报错

![FAQ1](https://docs.daocloud.io/daocloud-docs-images/docs/install/images/FAQ1.png)

在安装全局服务集群的每个节点上执行 `modprobe br_netfilter`，将 `br_netfilter` 加载之后就好了。

## CentOS 环境准备问题

运行 `yum install docker` 时报错：

```text
Failed to set locale, defaulting to C.UTF-8
CentOS Linux 8 - AppStream                                                                    93  B/s |  38  B     00:00    
Error: Failed to download metadata for repo 'appstream': Cannot prepare internal mirrorlist: No URLs in mirrorlist
```

可以尝试下述方法来解决：

- 安装 `glibc-langpack-en`

    ```bash
    sudo yum install -y glibc-langpack-en
    ```

- 如果问题依然存在，尝试：

    ```bash
    sed -i 's/mirrorlist/#mirrorlist/g' /etc/yum.repos.d/CentOS-*
    sed -i 's|#baseurl=http://mirror.centos.org|baseurl=http://vault.centos.org|g' /etc/yum.repos.d/CentOS-*
    sudo yum update -y
    ```

## 火种节点关机重启后，kind 集群无法正常重启

火种节点关机重启后，由于部署时在 openEuler 22.03 LTS SP2 操作系统上未设置 kind 集群开机自启动，会导致 kind 集群无法正常开启。

需要执行如下命令开启：

```bash
podman restart $(podman ps | grep installer-control-plane | awk '{print $1}') 
```

!!! note

    如果其他环境中发生了上述场景，也可以执行该命令进行重启。

## Ubuntu 20.04 作为火种机器部署时缺失 ip6tables

Ubuntu 20.04 作为火种机器部署，由于缺失 ip6tables 会导致部署过程中报错。

请参阅 [Podman 已知问题](https://github.com/containers/podman/issues/3655)。

临时解决方案：手动安装 iptables，参考
[Install and Use iptables on Ubuntu 22.04](https://orcacore.com/install-use-iptables-ubuntu-22-04/#:~:text=In%20this%20guide%2C%20we%20want%20to%20teach%20you,your%20network%20traffic%20packets%20by%20using%20these%20filters)。

## 如何卸载火种节点的数据

商业版部署后，如果进行卸载，除了本身的集群节点外，还需要对火种节点进行重置，重置步骤如下：

需要使用 `sudo rm -rf` 命令删除这三个目录：

- /tmp
- /var/lib/dce5/
- /home/kind/etcd
