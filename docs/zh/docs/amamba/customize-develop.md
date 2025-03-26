# 自定义步骤开发指南

## YAML 文件模板

声明文件用于定义自定义步骤的名称、版本、参数等信息，为了更加的云原生化，应用工作台定义的 plugin 信息保持了 K8s resource 的风格，虽然目前它们不会以 CRD 的形式存在，插件的定义如下：

```yaml
apiVersion: pipeline.amamba.io/v1alpha1
kind: PipelinePlugin
metadata:
  name: deploy-application      # required 插件的ID，只能包含小写字母、数字及分隔符（"- _"）
  labels:
    pipeline.amamba.io/category: build  # 必须定义为其中一个：others，build，test，security，release，deploy，command，general，repository，quality
    pipeline.amamba.io/hidden: false  # 是否隐藏插件
    pipeline.amamba.io/version: 1.0.0  # required 插件的版本，与 name 必须唯一
  annotations:
    pipeline.amamba.io/description: 部署应用到k8s集群      # 插件的描述 
    pipeline.amamba.io/versionDescription: 修复了xxx问题 # 插件的版本描述
    pipeline.amamba.io/icon: 插件的图标   # 图标链接
spec:
  image: "docker.m.daocloud.io/amambadev/jenkins-agent-base:v0.3.2-podman"  # required 插件的基础镜像，必须是公网镜像，并且不需要登录 
  entrypoint: ""    # 可以自定义入口脚本, 本质上是替换 --entrypoint
  shell: "/bin/bash"
  script: "kubectl apply -f ."   # required 需要在容器中执行的脚本 
  params:         # required
    - name: namespace    # required 必须唯一
      sort: 2     # 参数展示的顺序
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
        immutable: false     # 是否可修改
        default: "my-namespace"  # 默认值
        options:
          - label: 默认
            value: default
      env: NAMESPACE  # 存在env这个属性则将env的值作为环境变量的key传递到插件，否则按照name的值传递        
      dependProperties: # 属性依赖，如 namespace 字段依赖于 cluster 字段，给前端交互使用
        cluster: cluster
        namespace: namespace
```

## 参数介绍

| 属性名 | 含义 | 示例 |
| ----- | --- | ---- |
| name | 参数名称 | cluster |
| type | 参数类型 | 支持 string, int, bool, float, array, map |
| env | 对应环境变量的值，没有此字段则默认与 name 相同 | CLUSTER_NAME |
| validate | 参数的校验规则 | {} |
| uiConfig | ui 页面上的一些选项 | {} |
| dependProperties | ui 上的属性依赖项 | 比如namespace依赖于cluster， 给前端交互使用 |

### dependProperties 依赖参数介绍

因为某些参数之间存在着依赖关系，例如 namespace 依赖于 cluster，为了更好的 UI 交互体验，可以在 dependProperties 中添加属性依赖项说明，
那么前端会自动根据 uiType 以及dependProperties来动态获取数据进行交互。dependProperties 是一个 map 结构，
key 是前端在组件中会使用到的参数，value 是在 params 中定义的参数名称，可以声明多个依赖项。

#### 依赖项举例

**NamespaceSelector：**

```yaml
params:
  - name: cls                 
    uiType: ClusterSelector
  - name: namespace                 
    uiType: NamespaceSelector
    dependProperties:
      cluster: cls      # key是前端在组件中会使用到的参数，value是在params中定义的参数名称*
```

**WorkloadSelector：**

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
    uiType: WorkloadSelector    # 级连依赖于cluster,namespace,workloadType属性*
    dependProperties:  
      cluster: cls
      namespace: namespace   
      workloadType: workloadType  
```

**ContainerSelector：**

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

### validate 参数校验规则介绍

```yaml
required:  true # 是否必填
requiredMessage: '必须填写' # 必填时的提示信息
pattern: '*' # 合法的正则表达式
patternMessage: '不匹配' # 正则表达式不匹配时的提示信息
min: 0 # 最小值，合法的数字
max: 1 # 最大值，合法的数字，需要 > min
minLength: 64 # 最小长度
maxLength: 64 # 最大长度
integer: true # 是否为整数
immutable: false # 是否可修改，false 代表可以修改，true 代表不可修改，
default: 'cluster1' # 默认值
options:
  - label: '集群1'    # 针对下拉框
    value: 'cluster1'
```

## uiConfig 参数介绍

uiConfig 必须是预定义的类型，主要是一些 ui 展示上的配置项：

```yaml
displayName: 显示的名称
helper: 帮助信息（位于输入框的下面）
tips: 提示信息（鼠标点击?时的提示）
placeholder: 占位符信息
```

UI 参数预定义类型及使用场景如下：

| UI 类型 | 参数类型 | 说明 | 依赖项说明 |
| ------ | ------- | --- | --------- |
| Text | string | 大文本输入框 | |
| Shell | string | Shell 高亮输入框 | |
| Yaml | string | YAML 高亮输入框 | |
| Input | string | 输入框，单行文本 | |
| Select | string | 下拉框，与参数定义中的 options 配合使用 | |
| Radio | string | 单选框 | |
| Switch | bool | 开关 | |
| Password | string | 密码 `****` | |
| Number | int | 数字输入框 | |
| ImageInput | string | 镜像选择器 | |
| ClusterSelector | string | 集群选择器 | |
| NamespaceSelector | string | 命名空间选择器 | 依赖于 cluster 属性 |
| CredentialSelector | string | 凭证选择器 | |
| WorkloadSelector | string | 工作负载选择器 | 依赖于 cluster、namespace、workloadType 属性 |
| ContainerSelector | string | 容器选择器 | 依赖于 cluster、namespace、workloadType、workloadName 属性 |
| Strings | array | 字符串数组 | |
| Numbers | array | 数字数组 | |
| KV | map | kv 键值对结构，如环境变量 | |
| Ignore | bool | 不展示此字段 | |
| CPUNumber | float | CPU 数量输入框 | |
| MemoryNumber | float | 内存数量输入框 | |
