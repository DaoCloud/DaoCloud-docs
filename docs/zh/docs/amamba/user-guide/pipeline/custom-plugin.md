# 自定义流水线插件

在使用流水线功能时，各个团队的使用场景各有差异，可以将一些常用的脚本，命名，工具等封装成一个自定义插件，方便复用，或者当工作台提供的功能无法满足需求时，可以通过自定义插件来扩展功能。

## 配置jenkins

自定义插件功能依赖于jenkins的共享库功能，因此首先需要在jenkins中配置共享库。有以下两种方式可以配置：

1. 在安装jenkins时，通过设置helm参数：`Master.GlobalPipelineLibraries.enabled=true`来开启

2. 在已经安装的jenkins中，通过修改jenkins的casc配置项开启，步骤如下：
   1. 点击左上角的 **≡** 打开导航栏，选择 __容器管理__ -> __集群列表__ ，找到需要安装 Jenkins 的集群，点击该集群的名称。
   2. 找到 __配置与密钥__ -> __配置项__ , 搜索 __jenkins-casc-config__ ，在操作列点击 __编辑 YAML__ 。
   3. 在 __data__ -> __jenkins.yaml__ -> __unclassified__ 字段下添加如下内容：

```yaml
unclassified:
   xxxxx # 其余配置项
   globalLibraries:        # 共享库配置
     libraries:
       - name: amamba-shared-lib
         defaultVersion: main
         implicit: true
         retriever:
           modernSCM:
               libraryPath: ./
               scm:
                  git:
                     remote: https://github.com/amamba-io/amamba-shared-lib.git
```

参数说明：

- implicit: true 表示该共享库会被默认引入到所有流水线中，在jenkinsfile中不需要使用@Library注解引入。如果不需要则设置为false，如果某个流水线需要使用到自定义插件功能，则需要在jenkinsfile中使用`@Library('amamba-shared-lib@main') _` 引入。
- remote: 表示工作台维护的共享库地址，是实现自定义插件的代码仓库地址。仓库地址是公开的。**在网络受限的环境下，您可以将其clone到内网的git服务器上，然后将地址改为内网地址。**

## 创建自定义插件

自定义插件目前支持以yaml文件的形式定义，yaml格式如下：

```yaml
apiVersion: pipeline.amamba.io/v1alpha1
kind: PipelinePlugin
metadata:
  name: deploy_application      # 插件的ID 
  labels:
    pipeline.amamba.io/category: build   # 插件的分类，支持[others，build，test，security，release，deploy，command，general，repository，quality]
    pipeline.amamba.io/version: 1.0.0  # 插件的版本,必须支持语义化版本
  annotations:
    pipeline.amamba.io/description: 部署应用到k8s集群     # 插件的描述 
    pipeline.amamba.io/versionDescription: 修复了xxx问题 # 插件的版本描述
    pipeline.amamba.io/icon: 插件的图标                  # 图标链接,可以是链接或者base64以后的图片
spec:
  image: amamba/deploy-application:1.0.0  # 插件的基础镜像，必须是公网镜像，并且不需要登录
  entrypoint: ""                       # 可以自定义入口脚本, 本质上是替换镜像的--entrypoint
  shell: /bin/bash                     # 指定解释器
  script: "kubectl apply xxx"          # 需要在容器中执行的脚本 
  params:                              # 插件的参数
    - name: namespace                  # 参数名称
      sort: 1                          # 参数展示的顺序
      uiType: NamespaceSelector        # UI类型，前端根据UI类型展示不同的组件
      description: 命名空间             # 参数描述
      type: string                     # 参数类型，支持【string,int,bool,float,array, map】
      uiConfig:                        # UI配置
        displayName: 命名空间           # 参数展示的名称
        placeholder: namespace         # 参数的placeholder
        tips: 应用部署的命名空间          # 参数的提示
        helper: 未找到命名空间？请前往全局管理配置 # 参数的帮助信息
      validate:                        # 参数校验
        required: true                 # 是否必填
        requiredMessage: 命名空间不能为空 # 必填校验提示
        pattern: ^[a-zA-Z0-9_-]+$      # 正则校验，必须是一个合法的正则表达式 
        regexMessage: 命名空间只能包含字母，数字，下划线和中划线 # 正则校验提示
        minLength: 1                   # 最小长度
        maxLength: 64                  # 最大长度
        immutable: false                  # 是否可修改
        default: cluster1                 # 默认值
        options:                       # 下拉框选项
          - label: 默认
            value: default
      env: NAMESPACE               # 存在env这个属性则将env的值作为环境变量的key传递到插件，否则按照name的值传递
      dependProperties: ["cluster"]    # 属性依赖，如namespace字段依赖于cluster字段，给前端交互使用 
```

上述参数中，必填的值有：
- name
- image
- params
- version
- parameter中name字段
- 如果immutable为true，则default字段不能为空
- options的label和value都不能为空

某些参数具有默认值:
- uiType: Input
- type: string
- category: others

uiType用于定义前端展示的组件，目前支持的组件及使用场景如下：

| 参数类型   | UI类型                 | 说明                     |
|--------|----------------------|------------------------|
| string | Text                 | 大文本输入框                 |
| string | Shell                | Shell 高亮输入框            |
| string | Yaml                 | Yaml 高亮输入框             |
| string | Input                | 输入框,单行文本               |
| string | Select               | 下拉框,与参数定义中的options配合使用 |
| string | Radio                | 单选框                    |
| bool   | Switch               | 开关                     |
| string | Password             | 密码，****                |
| int    | Number               | 数字输入框                  |
| string | ImageInput           | 镜像选择器                  |
| string | ClusterSelector      | 集群选择器                  |
| string | NamespaceSelector    | 命名空间选择器                |
| string | DeployTargetSelector | 集群/命名空间选择器             |
| string | CredentialSelector   | 凭证选择器                  |
| string | WorkloadSelector     | 工作负载选择器                |
| array  | Strings              | 字符串数组                  |
| array  | Numbers              | 数字数组                   |
| map    | KV                   | kv键值对结构，如环境变量          |
| bool   | Ignore               | 不展示此字段                 |
| float  | CPUNumber            | CPU数量输入框               |
| float  | MemoryNumber         | 内存数量输入框                |
| string | K8sObjectsCode       | k8s对象代码输入框             |

在创建插件之后，为了保证插件的兼容性，当您需要更改插件定义时，最佳实践是递增插件的版本号，并在版本描述中说明更改的内容。

## 使用自定义插件

在流水线的编辑页面 -> 点击添加步骤 -> 选择自定义步骤 -> 选择自定义插件及对应版本 -> 填写参数 -> 点击确定即可。

注意，自定义步骤有以下限制：
- **必须要在一个包含docker或者podman的容器中运行**
- **插件的镜像必须是公网镜像，不需要登录即可拉取**
- 如果需要在插件中使用凭证，可以在步骤设置中选择【使用凭证】即可

自定义插件使用时会被渲染成如下的jenkinsfile片段：

```groovy
amambaCustomStep(
                        pluginID: 'printEnv',      # 插件名称
                        version: 'v1.0.0',         # 插件版本 
                        args: [
                            image: 'alpine',       # 插件使用的镜像
                            shell: '/bin/bash',    # 解释器
                            script: 'env',         # 在镜像中执行的脚本
                            key1: 'val',           # 插件中定义的参数
                            key2: [
                                'key3': 'val3'
                            ]
                        ],
                    )
```
args中的所有参数都会以环境变量的形式传递到插件中，因此您可以在script中通过`$key1`的形式获取到参数的值。如果参数的类型时kv，参数的key会以`_`连接后传递到插件中，如`key2_key3=val3`。

因此，即使您不采用DAG的形式编排，依旧可以按照上述标准在jenkinsfile中使用自定义插件。只是需要注意，参数的值类型为string时请使用单引号,避免无法替换环境变量的问题。