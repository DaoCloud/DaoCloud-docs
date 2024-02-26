# Jenkins **Pipeline 语法**

Jenkins 支持**声明式 Pipeline** 、**脚本式 Pipeline**，工作台主要采用**声明式 Pipeline 语法**，所以本文将重点介绍 Jenkins 声明式语法。

## **声明式 Pipeline 语法概述**

Pipeline 脚本基于 Groovy 语言，但即便你不熟悉 Groovy，也可以通过简单的学习来编写基础的 Pipeline 脚本，以下是一个精简的声明式 Pipeline 示例：

```groovy
pipeline {
    agent any // 定义在哪里运行Pipeline，`any`表示可以在任何可用的agent上运行

    parameters {
        // 设置构建参数
    }

     environment { 
        // 设置环境变量
    }

    stages { // 定义执行的阶段
        stage('Build') { // 构建阶段
            steps {
                // 定义在构建阶段要执行的步骤
            }
        }
        stage('Test') { // 测试阶段
            steps {
                // 定义在测试阶段要执行的步骤
            }
        }
        stage('Deploy') { // 部署阶段
            steps {
                // 定义在部署阶段要执行的步骤
            }
        }
    }
    
}
```

## 部分模块介绍

### Agent

`agent` 部分指定了整个流水线或特定的部分，将会在Jenkins环境中执行的位置，这取于 `agent` 区域的位置。该部分必须在 `pipeline` 块的顶层被定义，但是 stage 级别的使用是可选的。

目前工作台界面上已经支持了：

- **any**

    在任何可用的代理上执行流水线或阶段。例如 `agent any`

- **none**

    当在 `pipeline` 块的顶部没有全局代理， 该参数将会被分配到整个流水线的运行中并且每个
    `stage` 部分都需要包含他自己的 `agent` 部分。比如 `agent none`

- **node**

    `agent { node { label 'labelName' } }`，有关应用工作台内置的 node 请参考文档[使用内置 lable](../pipeline/config/agent.md)

- **kubernetes**

    Pod 模板在 kubernetes { } 块内定义。 例如，如果您想要一个内部包含 podman 容器的 Pod，您可以按如下方式定义。
    注意：一定要定义 jnlp 容器，目的是与 Jenkins 服务进行通信。

    ```groovy
    agent {
        kubernetes {
            defaultContainer 'kaniko'
            yaml '''
            apiVersion: v1
            kind: Pod
            metadata:
              labels:
                jenkins-pipeline: pipeline-amamba-pod
            spec: 
              containers:
                - name: podman
                  image: release-ci.daocloud.io/amamba/jenkins-agent/builder-base:v0.2.1-podman
                  resources:
                    limits:
                      cpu: 500m
                      memory: 1024Mi
                    requests:
                      cpu: 100m
                      memory: 100Mi
                  securityContext:
                    privileged: true
                  command:
                    - cat
                  tty: true
                - name: jnlp
                  image: release-ci.daocloud.io/amamba/jenkins-agent/inbound-agent:4.10-2
                  resources:
                    limits:
                      cpu: 100m
                      memory: 256Mi
                    requests:
                      cpu: 100m
                      memory: 128Mi
    '''
      }
    ```

### `environment`

`environment` 指令制定一个 键-值对序列，该序列将被定义为所有步骤的环境变量，或者是特定于阶段的步骤，
这取决于 `environment` 指令在流水线内的位置。
详细介绍参考 [Jenkins 官方文档](https://www.jenkins.io/doc/book/pipeline/syntax/#environment)，简单示例如下：

```groovy
pipeline {
    agent any
    environment { 
        CC = 'clang'
				//	顶层流水线块中使用的 environment 指令将适用于流水线中的所有步骤。
    }
    stages {
        stage('Example') {
            environment {  // 在一个 stage 中定义的 environment 指令只会将给定的环境变量应用于 stage 中的步骤。
                AN_ACCESS_KEY = credentials('my-prefined-secret-text') 
								// environment 块有一个 助手方法 credentials() 定义，该方法可以在 Jenkins 环境中用于通过标识符访问预定义的凭证。						
            }
            steps {
                sh 'printenv'
            }
        }
    }
}
```

#### 在 `environment` 区域中使用凭证

对于 secret text、 username and password 和 secret file 类型的凭据，支持通过使用 `environment` 的方式直接在流水线中使用，其他的凭证使用方式参考[使用凭证](https://www.jenkins.io/doc/book/pipeline/jenkinsfile/#handling-credentials)。

使用方式请参考：

- [通过 `environment` 使用 Secret text 凭证](https://www.jenkins.io/doc/book/pipeline/jenkinsfile/#secret-text)
- [通过 `environment` 使用 Usernames and passwords 凭证](https://www.jenkins.io/doc/book/pipeline/jenkinsfile/#usernames-and-passwords)
- [通过 `environment` 使用 Secret files 凭证](https://www.jenkins.io/doc/book/pipeline/jenkinsfile/#secret-files)

### `parameters`

`parameters` 指令提供了一个用户在触发流水线时应该提供的参数列表。这些用户指定参数的值可通过 `params` 对象提供给流水线步骤。
详细介绍参考 [Jenkins 官方文档](https://www.jenkins.io/doc/book/pipeline/syntax/#parameters)，简单示例如下：

```groovy
pipeline {
    agent any
    parameters { 
        
       // 支持的 parameters 类型
        
        string(name: 'PERSON', defaultValue: 'Mr Jenkins', description: 'Who should I say hello to?')

        text(name: 'BIOGRAPHY', defaultValue: '', description: 'Enter some information about the person')

        booleanParam(name: 'TOGGLE', defaultValue: true, description: 'Toggle this value')

        choice(name: 'CHOICE', choices: ['One', 'Two', 'Three'], description: 'Pick something')

        password(name: 'PASSWORD', defaultValue: 'SECRET', description: 'Enter a password')
    }
    stages {
        stage('Example') {
            steps {
                echo "Hello ${params.PERSON}"

                echo "Biography: ${params.BIOGRAPHY}"

                echo "Toggle: ${params.TOGGLE}"

                echo "Choice: ${params.CHOICE}"

                echo "Password: ${params.PASSWORD}"
            }
        }
    }
}
```

### `stages`

包含一系列一个或多个 stage 指令，`stages` 部分是流水线描述的大部分"work" 的位置。
建议 `stages` 至少包含一个 stage 指令用于连续交付过程的每个离散部分，比如构建，测试,，和部署。

```groovy
pipeline {
    agent any
    stages { 
        stage('Example') {
            steps {
                echo 'Hello World'
            }
        }
    }
}
```

### `steps`

`steps` 部分在给定的 `stage` 指令中执行的定义了一系列的一个或多个 steps。

```groovy
pipeline {
    agent any
    stages {
        stage('Example') {
            steps { // steps 部分必须包含一个或多个步骤。
                echo 'Hello World'
            }
        }
    }
}
```

以上仅描述了部分声明式 Pipeline，详细可参考 Jenkins
官方的[语法介绍](https://www.jenkins.io/doc/book/pipeline/syntax/#declarative-pipeline)。
