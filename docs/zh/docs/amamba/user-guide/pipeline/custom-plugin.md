# 自定义流水线插件

在使用流水线功能时，各个团队的使用场景各有差异，可以将一些常用的脚本，命令，工具等封装成一个自定义插件，方便复用，或者当工作台提供的功能无法满足需求时，可以通过自定义插件来扩展功能。

## 配置jenkins

自定义插件功能依赖于jenkins的[共享库](https://www.jenkins.io/doc/book/pipeline/shared-libraries/)功能，因此首先需要在jenkins中配置共享库。配置方式如下

修改jenkins的casc配置项开启，步骤如下：

1.  点击左上角的 **≡** 打开导航栏，选择 **容器管理** -> **集群列表** ，找到需要安装 Jenkins 的集群，点击该集群的名称。
2.  找到 **配置与密钥** -> **配置项** , 搜索 **jenkins-casc-config** ，在操作列点击 **编辑 YAML** 。
3.  在 **data** -> **jenkins.yaml** -> **unclassified** 字段下添加如下内容：

    ```yaml
    unclassified:
      globalLibraries: # 共享库配置
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

- implicit: true 表示该共享库会被默认引入到所有流水线中，在jenkinsfile中就**不在需要**使用@Library注解引入。如果开启了此参数将会对所有的流水线生效，会略微延长流水线的执行时间。如果不需要则设置为false，后续如果某个流水线需要使用到自定义插件功能，则需要在jenkinsfile中使用`@Library('amamba-shared-lib@main') _` 引入。
- remote: 表示工作台维护的共享库地址，是实现自定义插件的代码仓库地址。仓库地址是公开的。**在网络受限的环境下，您可以将其clone到内网的git服务器上，然后将地址改为内网地址。**

## 创建自定义插件

创建自定义插件需要工作台的管理员权限，在【工作台管理】-> [流水线设置] -> [自定义步骤]页面对插件进行管理。

自定义插件目前只支持以yaml文件的形式定义，yaml格式如下：

    ```yaml
    apiVersion: pipeline.amamba.io/v1alpha1
    kind: PipelinePlugin
    metadata:
      name: deploy-application # required 插件的ID，只能包含小写字母、数字及分隔符（"- _"）
      labels:
        pipeline.amamba.io/category: build # 必须定义为其中一个：others，build，test，security，release，deploy，command，general，repository，quality
        pipeline.amamba.io/version: 1.0.0 # required 插件的版本，与 name 必须唯一
      annotations:
        pipeline.amamba.io/description: 部署应用到k8s集群 # 插件的描述
        pipeline.amamba.io/versionDescription: 修复了xxx问题 # 插件的版本描述
        pipeline.amamba.io/icon: 插件的图标 # 图标链接
    spec:
      image: "docker.m.daocloud.io/amambadev/jenkins-agent-base:v0.3.2-podman" # required 插件的基础镜像
      entrypoint: "" # 可以自定义入口脚本, 本质上是替换 --entrypoint
      shell: "/bin/bash" # 脚本解释器，如shell, python等
      script: "kubectl apply -f ." # required 需要在容器中执行的脚本
      params: # required
        - name: namespace # required 名称必须唯一
          sort: 2 # 参数展示的顺序
          uiType: NamespaceSelector
          type: string
          uiConfig:
            displayName: "命名空间"
            placeholder: "namespace"
            tips: "应用部署的命名空间"
            helper: "未找到命名空间？请前往全局管理配置"
          validate:
            required: true
            requiredMessage: "命名空间不能为空"
            pattern: ^[a-zA-Z0-9_-]+$
            patternMessage: "命名空间只能包含字母，数字，下划线和中划线"
            minLength: 1
            maxLength: 64
            immutable: false # 是否可修改
            default: "my-namespace" # 默认值
            options:
              - label: 默认
                value: default
          env: NAMESPACE # 存在env这个属性则将env的值作为环境变量的key传递到插件，否则按照name的值传递
          dependProperties: # 属性依赖，如 namespace 字段依赖于 cluster 字段，给前端交互使用
            cluster: cls
    ```

Param 参数介绍：

| 属性名           | 含义                                         | 示例                                        |
| ---------------- | -------------------------------------------- | ------------------------------------------- |
| name             | 参数名称                                     | cluster                                     |
| type             | 参数类型                                     | string                                      |
| env              | 对应环境变量的值，没有此字段则默认与name相同 | CLUSTER_NAME                                |
| validateConfig   | 参数的校验规则                               | {}                                          |
| uiConfig         | ui页面上的一些选项                           | {}                                          |
| dependProperties | ui上的属性依赖项                             | 比如namespace依赖于cluster， 给前端交互使用 |

dependProperties 依赖参数介绍：
因为某些参数之间存在着依赖关系，例如namespace依赖于cluster，为了更好的UI交互体验，可以在dependProperties中添加属性依赖项说明，那么前端会自动根据uiType以及dependProperties来动态获取数据进行交互。dependProperties是一个map结构，key是前端在组件中会使用到的参数，value是在params中定义的参数名称，可以声明多个依赖项。

依赖项举例：
NamespaceSelector：

    ```yaml
    params:
      - name: cls
        uiType: ClusterSelector
      - name: namespace
        uiType: NamespaceSelector
        dependProperties:
          cluster: cls # key是前端在组件中会使用到的参数，value是在params中定义的参数名称*
    ```

WorkloadSelector：

    ```yaml
    params:
      - name: cls
        uiType: ClusterSelector
      - name: namespace
        uiType: NamespaceSelector
        dependProperties:
          cluster: cls
      - name: workloadType
        uiType: Select
      - name: workloadName
        uiType: WorkloadSelector # 级连依赖于cluster,namespace,workloadType属性*
        dependProperties:
          cluster: cls
          namespace: namespace
          workloadType: workloadType
    ```

ContainerSelector:

    ```yaml
    params:
      - name: cls
        uiType: ClusterSelector
      - name: namespace
        uiType: NamespaceSelector
        dependProperties:
          cluster: cls
      - name: workload_type
        uiType: Select
      - name: workloadName
        uiType: WorkloadSelector
        dependProperties:
          cluster: cls
          namespace: namespace
          workloadType: workloadType
      - name: containerName
        uiType: ContainerSelector
        dependProperties:
          cluster: cls
          namespace: namespace
          workloadType: workload_type
          workloadName: workloadName
    ```

validate 参数校验规则介绍:

    ```yaml
    required: true # 是否必填
    requiredMessage: "xxx必须填写" # 必填时的提示信息
    pattern: "*" # 合法的正则表达式
    patternMessage: "xxx不匹配" # 正则表达式不匹配时的提示信息
    min: 0 # 最小值，合法的数字
    max: 1 # 最大值，合法的数字，需要 > min
    minLength: 64 # 最小长度
    maxLength: 64 # 最大长度
    integer: true # 是否为整数
    immutable: false # 是否可修改，false 代表可以修改，true 代表不可修改，
    default: "cluster1" # 默认值
    options:
      - label: "无状态负载" # 针对下拉框
        value: "Deployment"
      - label: "有状态负载"
        value: "StatefulSet"
    ```

uiConfig 参数介绍:
uiConfig 必须是预定义的类型，主要是一些ui展示上的配置项：

    ```yaml
    displayName: 显示的名称
    helper: 帮助信息（位于输入框的下面）
    tips: 提示信息（鼠标点击?时的提示）
    placeholder: 占位符信息
    ```

UI参数预定义类型及使用场景如下：

| 参数类型 | UI类型             | 说明                                 | 依赖项说明                                               |
| -------- | ------------------ | ------------------------------------ | -------------------------------------------------------- |
| string   | Text               | 大文本输入框                         |                                                          |
| string   | Shell              | Shell 高亮输入框                     |                                                          |
| string   | Yaml               | Yaml 高亮输入框                      |                                                          |
| string   | Input              | 输入框,单行文本                      |                                                          |
| string   | Select             | 下拉框,与参数定义中的options配合使用 |                                                          |
| string   | Radio              | 单选框                               |                                                          |
| bool     | Switch             | 开关                                 |                                                          |
| string   | Password           | 密码，\*\*\*\*                       |                                                          |
| int      | Number             | 数字输入框                           |                                                          |
| string   | ImageInput         | 镜像选择器                           |                                                          |
| string   | ClusterSelector    | 集群选择器                           |                                                          |
| string   | NamespaceSelector  | 命名空间选择器                       | 依赖于cluster属性                                        |
| string   | CredentialSelector | 凭证选择器                           |                                                          |
| string   | WorkloadSelector   | 工作负载选择器                       | 依赖于cluster，namespace，workloadType属性               |
| string   | ContainerSelector  | 容器选择器                           | 依赖于cluster，namespace，workloadType，workloadName属性 |
| array    | Strings            | 字符串数组                           |                                                          |
| array    | Numbers            | 数字数组                             |                                                          |
| map      | KV                 | kv键值对结构，如环境变量             |                                                          |
| bool     | Ignore             | 不展示此字段                         |                                                          |
| string   | CPUNumber          | CPU数量输入框                        |                                                          |
| string   | MemoryNumber       | 内存数量输入框                       |                                                          |

在创建插件之后，为了保证插件的兼容性，当您需要更改插件定义时，最佳实践是递增插件的版本号，并在版本描述中说明更改的内容。

## 使用自定义插件

在流水线的编辑页面(DAG) -> 点击添加步骤 -> 选择自定义步骤 -> 选择自定义插件及对应版本 -> 填写参数 -> 点击确定即可。

注意，自定义步骤有以下限制：

- **必须要在一个包含docker或者podman的容器中运行**,因此您需要选择【使用容器】
- 因为本质上是在容器中执行脚本，某些脚本可能需要一些特殊的权限，当自定义步骤无法实现时，推荐使用【执行shell】步骤，自行编写脚本。

自定义插件使用时会被渲染成如下的jenkinsfile片段：

    ```groovy
    container("base") {
        amambaCustomStep(
            pluginID: 'printEnv',      # 插件名称
            version: 'v1.0.0',         # 插件版本
            docker: [
                image: 'alpine',       # 插件使用的镜像
                shell: '/bin/bash',    # 解释器
                script: 'env',         # 在镜像中执行的脚本
            ],
            args: [
                key1: 'val',           # 插件中定义的参数
                key2: [
                    'key3': 'val3'
                ],
                key4: ["val4", "val5"]
            ],
        )
    }
    ```

args中的所有参数都会以环境变量的形式传递到插件中，因此您可以在script中通过`$key1`的形式获取到参数的值。如果参数的类型时kv，参数的key会以`_`连接后传递到插件中，如`key2_key3=val3`。如果参数定义的是数组类型，则传递到插件中的值是`["val4", "val5"]`,您需要按照不同的语言自行解析。

因此，即使您不采用DAG的形式编排，依旧可以按照上述标准在jenkinsfile中使用自定义插件。只是需要注意，参数的值类型为string时请使用单引号,避免无法替换环境变量的问题。

### 环境变量和凭证

在Jenkinsfile中定义的环境变量和凭证，都可以在插件中读取到，比如：

    ```yaml
    withCredential([usernamePassword(credentialsId: 'my-credential', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
       amambaCustomStep(
           pluginID: 'printEnv',
           version: 'v1.0.0',
           docker: [
             image: 'alpine',
             shell: '/bin/bash', # 可以在插件的script中读取到USERNAME和PASSWORD变量
             script: 'env',
           ],
           args: [],
       )
    }
    ```

### 如何拉取私有镜像

如果您在定义插件时使用的是私有镜像，则需要通过以下方式使用自定义步骤：

1. 在工作台中创建一个用户名密码类型的凭证，用于存储私有镜像的用户名和密码。
2. 在使用自定义步骤之前，添加一个【使用凭证】的步骤，用户名变量填写`PLUGIN_REGISTRY_USER`,密码变量填写`PLUGIN_REGISTRY_PASSWORD`。

渲染出的Jenkinsfile片段如下：

    ```groovy
    withCredential([usernamePassword(credentialsId: 'my-credential', usernameVariable: 'PLUGIN_REGISTRY_USER', passwordVariable: 'PLUGIN_REGISTRY_PASSWORD')]) {
       amambaCustomStep(
           xxx
       )
    }
    ```

后续即可使用私有的镜像作为插件的基础镜像。
