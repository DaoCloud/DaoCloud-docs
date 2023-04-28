# 流水线节点（Agent）

Agent 描述了整个`流水线`执行过程或者某个`阶段`的执行环境，必须出现在`描述文件`顶部或每一个`阶段`。

本文基于 [Kubernetes plugin for Jenkins](https://plugins.jenkins.io/kubernetes/) 插件描述如何扩展 Kubernetes 中运行的 Jenkins Agent。

## Kubernetes Pod 模板介绍

这个 Kubernetes 插件会在 Jenkins Agent Pod 中运行一个特殊的容器 `jnlp`，目的是为了在 Jenkins Controller 和 Jenkins Agent 之间进行通信，所以需要定义其他容器来运行流水线步骤，并且可以通过 `container` 命令来切换不同的容器。

## 使用内置 Label

应用工作台通过 podTemplate 能力声明了 6 个 label：`base`、`maven`、`go`、`go16`、`node.js` 和 `python`。您可以指定具体的 Agent 标签来使用对应的 podTemplate。

- 可以在 Jenkinsfile 中通过 `node('go')` 使用 go 的 podTemplate。

    ```bash
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

- 也可以在`编辑流水线`页面上选择类型为 `node` 且 label 为 `go` 的 Agent。

    ![agent-base](https://docs.daocloud.io/daocloud-docs-images/docs/amamba/images/agent-base.jpeg)

### 内置 Label 环境说明

**Jenkins Agent Label: base**

| 名称     | 类型/版本                                                    |
| -------- | ------------------------------------------------------------ |
| 容器名称 | base                                                         |
| 操作系统 | centos-7 (7.9.2009)                                          |
| podman   | podman version 3.0.1                                         |
| Kubectl  | v1.22.0                                                      |
| 内置工具 | unzip、which、make(GNU Make 3.82)、wget、zip、bzip2、git (2.9.5) |

**Jenkins Agent Label: maven**

| 名称     | 类型/版本                                                    |
| -------- | ------------------------------------------------------------ |
| 容器名称 | maven                                                        |
| 操作系统 | centos-7 (7.9.2009)                                          |
| Jdk      | openjdk-1.8.0_322                                            |
| Maven    | 3.5.3                                                        |
| podman   | podman version 3.0.1                                         |
| Kubectl  | v1.22.0                                                      |
| 内置工具 | unzip、which、make(GNU Make 3.82)、wget、zip、bzip2、git (2.9.5) |

**Jenkins Agent Label: go**

| 名称     | 类型/版本                                                    |
| -------- | ------------------------------------------------------------ |
| 容器名称 | go                                                           |
| 操作系统 | centos-7 (7.9.2009)                                          |
| Go       | 1.12.10                                                      |
| GOPATH   | /home/jenkins/go                                             |
| GOROOT   | /usr/local/go                                                |
| podman   | podman version 3.0.1                                         |
| Kubectl  | v1.22.0                                                      |
| 内置工具 | unzip、which、make(GNU Make 3.82)、wget、zip、bzip2、git (2.9.5) |

**Jenkins Agent Label: go16**

| 名称     | 类型/版本                                                    |
| -------- | ------------------------------------------------------------ |
| 容器名称 | go                                                           |
| 操作系统 | centos-7 (7.9.2009)                                          |
| Go       | 1.16.8                                                       |
| GOPATH   | /home/jenkins/go                                             |
| GOROOT   | /usr/local/go                                                |
| podman   | podman version 3.0.1                                         |
| Kubectl  | v1.22.0                                                      |
| 内置工具 | unzip、which、make(GNU Make 3.82)、wget、zip、bzip2、git (2.9.5) |

**Jenkins Agent Label: node.js**

| 名称     | 类型/版本                                                    |
| -------- | ------------------------------------------------------------ |
| 容器名称 | nodejs                                                       |
| 操作系统 | centos-7 (7.9.2009)                                          |
| Node     | v10.16.3                                                     |
| Yarn     | 1.16.0                                                       |
| podman   | podman version 3.0.1                                         |
| Kubectl  | v1.22.0                                                      |
| 内置工具 | unzip、which、make(GNU Make 3.82)、wget、zip、bzip2、git (2.9.5) |

**Jenkins Agent Label: python**

| 名称     | 类型/版本                                                    |
| -------- | ------------------------------------------------------------ |
| 容器名称 | python                                                       |
| 操作系统 | centos-7 (7.9.2009)                                          |
| Python   | 3.7.11                                                       |
| podman   | podman version 3.0.1                                         |
| Kubectl  | v1.22.0                                                      |
| 内置工具 | unzip、which、make(GNU Make 3.82)、wget、zip、bzip2、git (2.9.5) |

## 使用 YAML 自定义 podTemplate

如果需要运行特定环境的 Jenkins Agent，可以在流水线上自定义 Jenkins Agent。

1. 在`编辑流水线`页面上选择 Agent 类型为 `kubernetes`。

    ![agent-kubernets](https://docs.daocloud.io/daocloud-docs-images/docs/amamba/images/agent-kubernets.jpeg)

2. 点击 `YAML 编辑器`，在对话框中填写 YAML 语句，请参考以下示例：

    ```bash
    apiVersion: v1
    kind: Pod
    spec:
      containers:
      - name: maven
        image: maven:3.8.1-jdk-8
        command:
        - sleep
        args:
        - 99d
      - name: golang
        image: golang:1.16.5
        command:
        - sleep
        args:
        - 99d
      ```

3. 在 Container 中输入 `golang` 作为流水线运行的默认容器。

    ![agent-golang](https://docs.daocloud.io/daocloud-docs-images/docs/amamba/images/agent-golang.jpeg)

4. 要在流水线其他步骤中使用上述示例的其他容器，可以选择`指定容器`填写所需要的容器名称。

    ![agent-maven](https://docs.daocloud.io/daocloud-docs-images/docs/amamba/images/agent-maven.jpeg)
