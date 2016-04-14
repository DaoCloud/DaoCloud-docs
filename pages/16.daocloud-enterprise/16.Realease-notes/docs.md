---
title: 'Release Note'
---

## 版本 1.0.0

### 功能清单

>* 企业级容器集群解决方案
>* 兼容性 - 可以部署在on-premises或cloud。支持Linux。
>* 容器管理 - 可以管理 应用，容器，存储卷，虚拟网络和主机。
>* 监控功能 - 看板 ，系统状态提醒。性能和日志
>* 高可用 - 一键配置
>* 安全 - 多用户管理
>* 镜像支持 - 支持DaoCloud Hub和Docker Hub私有镜像
>* 应用仓库 - 包括 tomcat， hadoop，elasticsearch等应用
>* 兼容Docker API - 支持Docker/Docker Compose命令
>* 自发现应用和容器 -可以兼容其他方案对容器和集群的管理
>* Reference Architecture - 高可用负载均衡，Scale IO

#### 企业级容器集群支持

>* 运维工具套件
>  * 一键安装(控制器，Agent)
>  * 一键卸载，升级，配置虚拟网络，启动，关闭
>  * trouble shooting。日志，状态，信息
>* 架构简单可控
>* 离线化安装
>* 正版授权支持
>* 在线客户支持

#### 兼容性

>* 部署环境
>  * 支持公有云 AWS 阿里云
>  * 支持私有云 VMware OpenStack
>  * 支持物理机，超融合
>* 操作系统
>  * Linux - Ubuntu, RedHat, Centos, Suse 等
>  * Mac/Window 通过boot2docker 
>* 最小化安装
>  * 一台主机，1core 1G mem


#### 容器管理

>* 应用管理
>  * 通过界面向导或者Compose创建应用
>  * 重新发布应用，并支持持续发布- webhook和命令行
>  * 应用-启动，停止，卸载，扩展
>  * 按服务、容器操作应用
>  * 应用操作事件记录
>* 容器管理
>  * 容器创建
>  * 容器操作-启动，停止，打开控制台
>  * 查看容器内进程
>* 存储卷管理
>  * 存储卷创建
>* 网络
>  * 创建 Overlay 虚拟网络
>  * 创建 Bridge 本地网络

#### 监控

>* 系统看板
>  * 一览整个系统状态
>* 日志
>  * 支持应用日志查看
>  * 支持日志导出，包括splunk等
>* 性能
>  * 支持查看应用容器，CPU，内存，网络等性能
>* 消息中心
>  * 当系统出现异常的时候，会有消息提示在消息中心

#### 高可用

>* 一键部署
>  * 支持一键部署高可用控制器
>* Out Of Box
>  * 不依赖第三方功能如数据库等高可用特性

#### 安全

>* 支持多用户管理

#### 镜像支持

>* 支持DaoCloud Hub镜像
>* 支持DockerHub镜像
>* 支持开源Docker Registry


#### 应用仓库

>* 应用仓库功能
>  * 支持搜索
>  * 一键部署
>  * 配置参数
>* 应用仓库列表
>  * [compose-catalog](https://github.com/DaoCloud/compose-catalog)

#### 兼容 Docker API

>* 支持Docker命令操作容器
>* 支持Docker Compose操作应用
>* 完整兼容Docker API，可以通过各种工具调用

#### 自发现应用和容器

>* 支持发现用户不通过DCE创建的容器
>* 支持发现用户不通过DCE创建的应用(Docker Compose)
>* 支持对自发现的应用和容器进行操作，统一管理

#### Reference Architecture

>* 负载均衡
>  * [Balancing-Feb](https://www.docker.com/sites/default/files/RA_UCP%20Load%20Balancing-Feb%202016_0.pdf)
>* ScaleIO
>* 持续发布
>  * 通过应用的URL或者命令行
>  * [RA-CI with Docker](https://www.docker.com/sites/default/files/UseCase/RA_CI%20with%20Docker_08.25.2015.pdf)



