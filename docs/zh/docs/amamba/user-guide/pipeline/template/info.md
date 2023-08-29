# 流水线模板文件

流水线模板文件按照YAML的格式组织，主要包含两部分：`parameterDefinitions` 和 `jenkinsfileTemplate`。

- `parameterDefinitions` 区域：定义流水线模板暴露哪些参数。支持布尔值、下拉列表、凭证、密码、文本等多种参数类型。
- `jenkinsfileTemplate` 区域：定义 Jenkins 流水线的 `jenkinsfile`，使用[go template](https://pkg.go.dev/text/template)作为模板引擎渲染，可以引用 `parameterDefinitions` 中暴露的参数。

## `parameterDefinitions` 区域

| 字段 | 类型 | 说明 | 默认值 | 是否必填 |
| --- | --- | --- | --- | --- |
| name | string | 参数名称，命名需遵循 [go template specification](https://pkg.go.dev/text/template#hdr-Arguments)，不允许重复，正则 "^[a-zA-Z_][a-zA-Z0-9_]*$" | - | 必填 |
| displayName | []byte | 表单上显示的名称，长度小于24个字符 | “” | 非必填 |
| description | string | 参数的描述 | “” | 非必填 |
| default | json.Value | 为对应的参数设置默认值| nil | 非必填 |
| type | string | 参数的类型, 支持布尔值、下拉列表、凭证、密码、文本 | string | 非必填 |

### 支持的参数类型

- boolean：布尔值，默认值只能为 `true` 或 `false`，在UI上是一个checkbox
- string: 字符串，输入框
- text：文本，文本框
- password：字符串，密码输入框
- choice：在UI上是一个下拉列表，必须按列表的格式提供默认值，例如

    ```yaml
    type: choice
    default:
      - choice 1
      - choice 2
    ```

- credential：凭证，在UI上是一个下拉列表，会获取当前工作空间下的凭证列表

## `jenkinsfileTemplate` 区域

整体上依然遵循[Jenkinsfile的语法](https://www.jenkins.io/doc/book/pipeline/syntax/)，但是可以使用[go template](https://pkg.go.dev/text/template)作为模板引擎，基于 `parameterDefinitions` 中定义的参数渲染。

### 变量

通过 `{{ .params.<name> }}` 的方式引用上文定义的参数，例如 `{{ .params.gitCloneURL }}`。

### 条件语句

支持以下三种格式的条件语句：

```go
{{if pipeline}} T1 {{end}}
    如果pipeline的值是空，不会输出任何内容；否则，执行T1。
    空值在模板中主要是false的布尔值和长度为零的字符串两种情况。

{{if pipeline}} T1 {{else}} T0 {{end}}
    如果pipeline的值是空，执行T0；否则，执行T1。

{{if pipeline}} T1 {{else if pipeline}} T0 {{end}}
    为了简化if-else链的外观，if的else动作可以直接包含另一个if；效果与写法完全相同
    {{if pipeline}} T1 {{else}}{{if pipeline}} T0 {{end}}{{end}}
```

### 循环语句

支持以下两种格式的循环语句：

```go
{{range pipeline}} T1 {{end}}
    pipeline的值必须是数组、切片、map或者channel。
    我们暂时不支持定义上述类型的Parameter。

{{range pipeline}} T1 {{else}} T0 {{end}}
    如果pipeline的长度是空，执行T0；否则，执行T1。
```

### 其他

上文描述的只是部分go template的语法，除此以外，你还能使用管道符`|`，函数（例如`printf`,），注释等，更多语法请参考[go template](https://pkg.go.dev/text/template)。

## 模板文件示例

```yaml
parameterDefinitions:
  - name: gitCloneURL
    displayName: 代码仓库地址
    description: The git clone url of the source code
    type: string
  - name: gitRevision
    displayName: 代码仓库分支
    description: The git revision of the source code
    type: string
    default: master
  - name: gitCredential
    displayName: 凭证
    description: The credential to access the source code
    type: credential
    default: ""
  - name: testCommand
    displayName: 测试命令
    description: The command to run the test
    type: string
    default: go test -v -coverprofile=coverage.out
  - name: reportLocation
    displayName: 测试报告位置
    description: The location of the test report
    type: string
    default: ./target/**
  - name: dockerfilePath
    displayName: Dockerfile路径
    description: The path of the Dockerfile
    type: string
    default: .
  - name: image
    displayName: 目标镜像地址
    description: The target image to build
    type: string
  - name: tag
    displayName: tag
    description: The tag of the target image
    type: string
    default: latest
  - name: registryCredential
    displayName: 镜像仓库凭证
    description: The credential to access the image registry
    type: credential
    default: ""
jenkinsfileTemplate: |
  pipeline {
    agent {
      node {
        label 'go'
      }
    }
    environment {
      IMG = '{{.params.image}}:{{.params.tag}}'
    }
    stages {
      stage('clone') {
        steps {
          container('go') {
            git(url: '{{ .params.gitCloneURL }}', branch: '{{ .params.gitRevision }}', credentialsId: '{{ .params.gitCredential }}')
          }
        }
      }
      stage('test') {
        steps {
          container('go') {
            sh '{{ .params.testCommand }}'
            archiveArtifacts '{{ .params.reportLocation }}'
          }
        }
      }
      stage('build') {
        steps {
          container('go') {
            sh 'docker build -f {{.params.dockerfilePath}} -t $IMG .'
          {{- if .params.registryCredential }}
            withCredentials([usernamePassword(credentialsId: '{{ .params.registryCredential }}', passwordVariable: 'PASS', usernameVariable: 'USER',)]) {
              sh 'docker login {{ .params.image }} -u $USER -p $PASS'
              sh 'docker push $IMG'
            }
          {{- else }}
            sh 'docker push $IMG'
          {{- end }}
          }
        }
      }
    }
  }
```
