# 自定义 Jenkins Agent

如果需要使用特定环境的JenkinsAgent，如特殊版本的JDK，或者特定的工具，可以通过自定义Jenkins Agent来实现。
本文档描述了如何在DCE5中自定义Jenkins Agent，添加的Agent为全局范围，即所有的流水线都能使用此agent。

## 配置Jenkins

1. 前往 __容器管理__ -> __集群列表__, 选择您安装jenkins的集群和命名空间（默认集群名称为kpanda-global-cluster，命名空间为amamba-system）
2. 选择 __配置与密钥__ -> __配置项__，选择jenkins安装的命名空间，搜索配置项`jenkins-casc-config`
3. 选择 __编辑yaml__, 搜索`jenkins.clouds.kubernetes.templates`，添加以下内容(以添加maven-jdk11为例)

    ```yaml
    - name: "maven-jdk11" # 自定义 Jenkins Agent 的名称。
      label: "maven-jdk11" # 自定义 Jenkins Agent 的标签。若要指定多个标签，请用空格来分隔标签。
      inheritFrom: "maven" # 该自定义 Jenkins Agent 所继承的现有容器组模板的名称。
      containers:
      - name: "maven" # 该自定义 Jenkins Agent 所继承的现有容器组模板中指定的容器名称。
        image: "my-maven-image" # 使用自定义的镜像。
    ```

    !!! note

        您也可以在containers中添加其他与podTemplate相关的配置项，jenkins采用yaml merge的方式，未填字段则继承自父模板。

5. 保存配置项，等待约一分钟后，jenkins会自动重新加载配置。

## 使用

1. 通过DAG页面编排流水线

    在DAG的编排页面，点击 __全局设置__，类型选择 **node**，标签选择您自定义的标签即可。

2. 通过JenkinsFile编排流水线

    在JenkinsFile的agent片段中引用自定义的标签：

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
