# 自定义 Jenkins Agent

如果需要使用特定环境的 Jenkins Agent，如特殊版本的JDK，或者特定的工具，可以通过自定义 Jenkins Agent 来实现。
本文档描述了如何在 DCE 5.0 中自定义 Jenkins Agent，添加的 Agent 为全局范围，即所有的流水线都能使用此 Agent。

## 配置 Jenkins

1. 前往 __容器管理__ -> __集群列表__ ，选择您安装 Jenkins 的集群和命名空间（默认集群名称为 kpanda-global-cluster，命名空间为 amamba-system）
2. 选择 __配置与密钥__ -> __配置项__ ，选择 Jenkins 安装的命名空间，搜索配置项 `jenkins-casc-config`
3. 选择 __编辑 YAML__ , 搜索`jenkins.clouds.kubernetes.templates`，添加以下内容（以添加 maven-jdk11 为例）

    ```yaml
    - name: "maven-jdk11" # (1)!
      label: "maven-jdk11" # (2)!
      inheritFrom: "maven" # (3)!
      containers:
      - name: "maven" # (4)!
        image: "my-maven-image" # (5)!
    ```

    1. 自定义 Jenkins Agent 的名称
    2. 自定义 Jenkins Agent 的标签。若要指定多个标签，请用空格来分隔标签
    3. 该自定义 Jenkins Agent 所继承的现有容器组模板的名称
    4. 该自定义 Jenkins Agent 所继承的现有容器组模板中指定的容器名称
    5. 使用自定义的镜像

    !!! note

        您也可以在 containers 中添加其他与 podTemplate 相关的配置项，Jenkins 采用 yaml merge 的方式，未填字段则继承自父模板。

5. 保存配置项，等待约一分钟后，Jenkins 会自动重新加载配置。

## 使用

1. 通过 DAG 页面编排流水线

    在 DAG 的编排页面，点击 __全局设置__ ，类型选择 **node** ，标签选择您自定义的标签即可。

2. 通过 Jenkinsfile 编排流水线

    在 Jenkinsfile 的 agent 片段中引用自定义的标签：

    ```groovy
    pipeline {
      agent {
        node {
          label 'maven-jdk11'  # 指定自定义的标签
        }
      }
      stages {
        stage('print jdk version') {
          steps {
            container('maven') {
              sh '''
              java -version
              '''
            }
          }
        }
      }
    }
    ```
