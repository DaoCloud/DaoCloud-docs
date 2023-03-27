# 流水线模板文件

流水线模版文件主要包含两部分：`parameterDefinitions` 和 `jenkinsfileTemplate`。

- `parameterDefinitions` 区域：定义流水线模版暴露哪些参数。支持布尔值、下拉列表、凭证、密码、文本等多种参数类型。
- `jenkinsfileTemplate` 区域：定义 Jenkins 流水线的 `jenkinsfile`，可以引用 `parameterDefinitions` 中暴露的参数。

## `parameterDefinitions` 区域

| 字段 | 类型 | 说明 | 默认值 | 是否必填 |
| --- | --- | --- | --- | --- |
| name | string | 参数名称 | - | 必填 |
| displayName | []byte | 表单上显示的名称，长度小于X个字符 | “” | 非必填 |
| description | string | 参数的描述 | “” | 非必填 |
| default | json.Value | 默认值，如果填了则该字段是选填，否则是必填 | nil | 非必填 |
| type | string | 参数的类型支持请看参数类型(需要链接到下面) | string | 必填 |

## 支持的参数类型

- boolean：布尔值，默认值只能为 `true` 或 `false`
- choice：下拉列表，必须提供默认值，例如

    ```yaml
    type: choice
    default:
      - choice 1
      - choice 2
    ```

- credential：凭证，会获取当前工作空间下的凭证列表
- password：密码
- text：文本，输入框

## 模版文件示例

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
