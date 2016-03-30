---
title: 快速开始
---

DCE 提供了一整套安装套件。你可以在10分钟之内安装DaoCloud Enterprise (DCE)。 

在这里，你会安装一套最简的DCE环境，并通过DCE部署一些应用。

## 简单介绍


![](small-install.png)


## 准备环境

登陆 Master 机器，执行 sudo su 切换到 # root 帐户状态

	curl -sSL https://get.daocloud.io/docker | sh

## 安装控制器

	bash -c "$(docker run -i --rm daocloud.io/daocloud/dce install)"
 
## 接入主机

	bash -c "$(docker run -i --rm daocloud.io/daocloud/dce join {你的控制器IP})"

## 部署应用



## 管理应用