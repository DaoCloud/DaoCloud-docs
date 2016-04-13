---
title: 升级 DCE
---

本页面将向你介绍如何将旧版 DCE 升级至新版本 DCE。

在你设计新版 DCE 前，请先查看 [Release Notes](http://docs.daocloud.io/daocloud-enterprise/release-notes) 中的版本升级信息。你可以通过这些信息了解到 DCE 的新特性，大的产品升级和其他相关的信息。

在开始升级之前，你需要确保待升级的容器集群是健康可用的。如果集群发生了故障，你需要先进行故障排查，并在解决该故障后再进行升级。除此之外，在 DCE 升级的时候，请不要修改 DCE 的相关配置，因为这可能会导致 DCE 配置丢失。


## DCE 升级命令

在需要升级时，可以通过在容器集群的每个节点上执行 `upgrade` 命令进行升级。如果你对相关命令不熟悉，你可以通过 `--help` 查看帮助信息。
```
bash -c "$(docker run --rm daocloud.io/daocloud/dce:1.0.0-dev upgrade --help)"
Upgrade the DCE Controller or Engine.

Usage: do-upgrade [options] [VERSION]

Description:
  The command will upgrade the DCE Controller or Engine on this machine.
  You should run the command on every machine in your cluster

Options:
  -q, --quiet        Quiet. Do not ask for anything.
  --force-pull       Always Pull Image, default is pull when missing
  --no-experimental  Disable experimental Swarm Experimental Features.
```

当你对 DCE 进行升级时，系统会进行多个操作，这些操作都会在执行 `upgrade` 命令后自动进行。

升级流程如下：
1. 从 DaoCloud Hub 拉取最新的服务镜像
2. 检查当前版本是否可以直接升级到最新版本，避免因为新旧版本的不兼容问题造成集群崩溃
3. 停止当前运行中的 DCE 容器，并移除该容器。当系统移除旧版容器时，不会对当前主机的其它容器，当前集群的其它主机和容器集群的配置造成任何修改和变更
4. 基于步骤 1 中拉取的服务镜像，部署新的容器，并自动接入容器集群

## DCE 升级步骤

DCE 升级非常方便，你只需要需要升级的节点上运行如下命令，就能够自动地升级至新版本 DCE：
```
	bash -c "$(docker run -i --rm daocloud.io/daocloud/dce:{{当前版本号}} upgrade --force-pull {{新版本号}})"
```

## 升级Docker

由于 Docker 不支持热升级，所以当你需要升级容器集群的 Docker Engine 时，你需要暂停当前容器集群中的所有容器和应用，或者将容器集群中的容器和应用暂时迁移到其它平台，待升级完成后再迁移会当前容器集群。
