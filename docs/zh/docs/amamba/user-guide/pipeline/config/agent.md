# 流水线节点（Agent）

Agent 描述了整个 __流水线__ 执行过程或者某个 __阶段__ 的执行环境，必须出现在 __描述文件__ 顶部或每一个 __阶段__ 。

本文基于 [Kubernetes plugin for Jenkins](https://plugins.jenkins.io/kubernetes/) 插件描述如何扩展 Kubernetes 中运行的 Jenkins Agent。

## Kubernetes Pod 模板介绍

这个 Kubernetes 插件会在 Jenkins Agent Pod 中运行一个特殊的容器 __jnlp__ ，目的是为了在 Jenkins Controller 和 Jenkins Agent 之间进行通信，所以需要定义其他容器来运行流水线步骤，并且可以通过 __container__ 命令来切换不同的容器。

## 内置 Label 说明

应用工作台通过 podTemplate 能力声明了 Label，提供了一些内置 SDK 供用户使用。

### SDK

底层运行时都支持 docker 和 podman，而操作系统有所区别

| SDK(Label)      | 版本信息                                              | 默认容器名称 | 操作系统                     |
| --------------- | ----------------------------------------------------- | ------------ | ---------------------------- |
| base            | -                                                     | base         | Centos 7.9<br />Ubuntu 22.04 |
| maven           | java: 8 <br />maven: 3.9.9                            | maven        | Centos 7.9<br />Ubuntu 22.04 |
| maven-jdk11     | java: 11 <br />maven: 3.9.9                           | maven        | Centos 7.9<br />Ubuntu 22.04 |
| maven-jdk17     | java: 17 <br />maven: 3.9.9                           | maven        | Ubuntu 22.04                 |
| maven-jdk21     | java: 21 <br />maven: 3.9.9                           | maven        | Ubuntu 22.04                 |
| go              | go: 1.17.13                                           | go           | Centos 7.9<br />Ubuntu 22.04 |
| go-1.18.10      | go: 1.18.10                                           | go           | Ubuntu 22.04                 |
| go-1.20.14      | go: 1.20.14                                           | go           | Ubuntu 22.04                 |
| go-1.22.6       | go: 1.22.6                                            | go           | Ubuntu 22.04                 |
| python          | python: 3.8.19<br />python、python3 均指向 python3.8  | python       | Centos 7.9<br />Ubuntu 22.04 |
| python-2.7.9    | python: 2.7.9<br />python、python2 均指向 python2.7   | python       | Ubuntu 22.04                 |
| python-3.10.9   | python: 3.10.9<br />python、python3 均指向 python3.10 | python       | Ubuntu 22.04                 |
| python-3.11.9   | python: 3.11.9<br />python、python3 均指向 python3.11 | python       | Ubuntu 22.04                 |
| node.js         | node: 16.20.2 <br />yarn: 1.22.22                     | nodejs       | Centos 7.9<br />Ubuntu 22.04 |
| node.js-18.20.4 | node: 18.20.4 <br />yarn: 1.22.22                     | nodejs       | Ubuntu 22.04                 |
| node.js-20.17.0 | node: 20.17.0 <br />yarn: 1.22.22                     | nodejs       | Ubuntu 22.04                 |

### 内置命令行工具

| 内置工具             | 版本                                         | 操作系统                 |
| -------------------- | -------------------------------------------- | ------------------------ |
| podman               | Ubuntu 22.04：5.1.0、<br />Centos 7.9：3.0.1 | Ubuntu 22.04、Centos 7.9 |
| docker               | 27.1.2                                       | Ubuntu 22.04、Centos 7.9 |
| helm                 | 3.15.4                                       | Ubuntu 22.04、Centos 7.9 |
| kubectl              | v1.31.0                                      | Ubuntu 22.04、Centos 7.9 |
| argocd               | v2.12.1                                      | Ubuntu 22.04、Centos 7.9 |
| argo rollouts        | v1.7.2                                       | Ubuntu 22.04、Centos 7.9 |
| sonar_scanner        | 4.8.0.2856                                   | Ubuntu 22.04、Centos 7.9 |
| yq                   | v4.44.3                                      | Ubuntu 22.04、Centos 7.9 |
| make                 | -                                            | Ubuntu 22.04、Centos 7.9 |
| build-essential      |                                              | Ubuntu 22.04             |
| libcurl4-openssl-dev | -                                            | Ubuntu 22.04             |
| libssl-dev           | -                                            | Ubuntu 22.04             |
| wget                 | -                                            | Ubuntu 22.04、Centos 7.9 |
| git                  | -                                            | Ubuntu 22.04、Centos 7.9 |
| curl                 | -                                            | Ubuntu 22.04、Centos 7.9 |
| autoconf             | -                                            | Ubuntu 22.04、Centos 7.9 |
| zip                  | -                                            | Ubuntu 22.04、Centos 7.9 |
| unzip                | -                                            | Ubuntu 22.04、Centos 7.9 |
| jq                   | -                                            | Ubuntu 22.04、Centos 7.9 |
| locales              | -                                            | Ubuntu 22.04             |
| vim                  | -                                            | Ubuntu 22.04、Centos 7.9 |
| gettext              | -                                            | Ubuntu 22.04、Centos 7.9 |
| tree                 | -                                            | Ubuntu 22.04、Centos 7.9 |
| gcc                  | -                                            | Centos 7.9               |
| gcc-c++              | -                                            | Centos 7.9               |
| curl-devel           | -                                            | Centos 7.9               |
| glibc-common         | -                                            | Centos 7.9               |

!!!note

  注意 Centos 7.9 已经EOL，目前保留仅是为了兼容旧版本的流水线构建环境数据，建议新环境统一使用 Ubuntu 22.04 支持的 SDK

## 使用内置 Label

- 可以在 Jenkinsfile 中通过 **node('go')** 使用 go 的 podTemplate。

  ```
  pipeline {
    agent {
      node {
        label 'go'
      }
    }
    
    stages {
      stage('go') {
        steps {
          container('go') {
            sh 'go version'
          }
        }
      }
    }
  }
  ```

- 也可以在 **编辑流水线** 页面上选择类型为 **node** 且 label 为 **go** 的 Agent。

  ![agent-base](https://docs.daocloud.io/daocloud-docs-images/docs/amamba/images/agent-base.jpeg)

## 自定义 podTemplate

如果对构建环境有特定要求，可以参考[创建自定义镜像](https://docs.daocloud.io/amamba/quickstart/jenkins-custom/#_1)来实现。