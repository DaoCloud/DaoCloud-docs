# 自定义 Jenkins Agent

如果需要使用特定环境的 Jenkins Agent，如特殊版本的JDK，或者特定的工具，可以通过自定义 Jenkins Agent 来实现。
本文档描述了如何在 DCE 5.0 中自定义 Jenkins Agent，其中工作台支持全局范围的自定义 Agent、流水线级别的自定义 Agent，可根据实际使用场景来决定选用哪种方式。

关于如何构建自定义的镜像请参考文档[在 Jenkins 中使用自定义工具链](../../quickstart/jenkins-custom.md#_1)

## 自定义全局范围 Agent

当前环境中有很多流水线对某个特定的工具均有需求时，则可以在全局范围定义 Agent 以供所有流水线可以使用

### 配置 Jenkins

1. 前往 __容器管理__ -> __集群列表__ ，选择您安装 Jenkins 的集群和命名空间
   （默认集群名称为 kpanda-global-cluster，命名空间为 amamba-system）
2. 选择 __配置与密钥__ -> __配置项__ ，选择 Jenkins 安装的命名空间，搜索配置项 `global-jenkins-casc-config`
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
    4. 该自定义 Jenkins Agent 所继承的现有容器组模板中指定的容器名称，如果不同名则按照原来模版新增一个容器
    5. 使用自定义的镜像

    !!! note

        您也可以在 containers 中添加其他与 podTemplate 相关的配置项，Jenkins 采用 yaml merge 的方式，未填字段则继承自父模板。

5. 保存配置项，等待约一分钟后，Jenkins 会自动重新加载配置，也可以选择重启 Jenkins 实例快速加载。

### 使用

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

## 自定义流水线级别的 Agent

如果当前环境中只有一条流水线对某个特定的工具均有需求时，则只需要流水线中自定义 Agent 即可

### 在流水线中使用

1. 选择一条流水线，进入 __编辑 Jenkinsfile__ 界面

2. 参考如下文件进行编辑：

    ```groovy
    pipeline {
      agent {
        kubernetes {
          inheritFrom 'base' # 指定继承 pod 的模版标签
          yaml '''
          spec:
            containers:
            - name: mavenjdk11 # 声明容器名称
              image: maven:3.8.1-jdk-11 # 定义容器镜像
    '''
        …
        }
    }
      stages {
        stage('print jdk version') {
          steps {
            container('mavenjdk11') { 
              sh '''
              java -version # 查看当前环境的 jdk 版本
              '''
            }
          }
        }
      }
    }
    ```

## FAQ

### 使用流水线自定义流水线级别的 Agent，如何默认继承父模版中的声明的 YAML 信息？

`yamlMergeStrategy` 参数支持 merge() 或 override()，用来控制模版中的 YAML 信息是被覆盖还是与继承的 pod 模版合并，默认为 override() 。

```groovy
pipeline {
  agent {
    kubernetes {
      yamlMergeStrategy merge() // 定义该策略后，将合并 base 模版中定义的 YAML
      inheritFrom 'base' // 指定继承 pod 的模版标签
      yaml '''
      spec:
        containers:
        - name: mavenjdk11 // 声明容器名称
          image: maven:3.8.1-jdk-11 // 定义容器镜像
      '''
    }
  }
  // 这里可以继续添加 pipeline 的其他部分
}
```

### 使用 inheritFrom 语法时，是否会继承父模版中的 volumeMounts 信息？

在使用 inheritFrom 语法时，分以下两种情况：

- 如果新增的容器有匹配到父模版同名容器，将继承父模板下容器的所有配置，即包含 volumeMounts、command、arguments 等等配置

- 如果没有匹配到父模版的容器，则不会继承父模板的 volumeMounts 信息，即按照当前定义信息添加到容器组中

### 当流水线运行失败后执行任务的容器组的也会被删除，如何延长存活时间，以便查看失败容器组的日志？

可以通过配置流水线的 `activeDeadlineSeconds`、`podRetention` 参数，来实现容器组在指定时间后才会删除容器组。

1. 前往 __容器管理__ -> __集群列表__ ，选择您安装 Jenkins 的集群和命名空间（默认集群名称为 kpanda-global-cluster，命名空间为 amamba-system）
2. 选择 __配置与密钥__ -> __配置项__ ，选择 Jenkins 安装的命名空间，搜索配置项 `global-jenkins-casc-config`
3. 选择 __编辑 YAML__ , 搜索 `jenkins.clouds.kubernetes.templates`，可以在每个容器模版下添加上述两个参数：

    ```yaml
    - name: "maven"
      label: "maven" 
      # 设置为 podRetention: onFailure() 时，将会在 activeDeadlineSeconds 定义的时间超过后删除 pod 
      podRetention: onFailure() 
      activeDeadlineSeconds: 100  # 单位为秒
      containers:
      - name: "maven" 
        image: "my-maven-image" 
    ```

4. 保存配置项，等待约一分钟后，Jenkins 会自动重新加载配置，也可以选择重启 Jenkins 实例快速加载。
