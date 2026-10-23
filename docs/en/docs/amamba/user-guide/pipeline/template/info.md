# Pipeline Template File

The pipeline template file is organized in YAML format and mainly contains two parts: __parameterDefinitions__ and __jenkinsfileTemplate__ .

- The __parameterDefinitions__ section: defines which parameters are exposed in the pipeline template. Multiple parameter types are supported, such as booleans, drop-down lists, credentials, passwords, and text.
- The __jenkinsfileTemplate__ section: defines the __jenkinsfile__ for the Jenkins pipeline, rendered with [go template](https://pkg.go.dev/text/template) as the template engine, and can reference the parameters exposed in __parameterDefinitions__ .

## __parameterDefinitions__ Section

| Field | Type | Description | Default Value | Required |
| --- | --- | --- | --- | --- |
| name | string | Parameter name. The naming must follow the [go template specification](https://pkg.go.dev/text/template#hdr-Arguments), duplicates are not allowed, and the regular expression is "^[a-zA-Z_][a-zA-Z0-9_]*$" | - | Required |
| displayName | []byte | Name displayed on the form, less than 24 characters | "" | Optional |
| description | string | Parameter description | "" | Optional |
| default | json.Value | Set a default value for the corresponding parameter | nil | Optional |
| type | string | Parameter type. Supports booleans, drop-down lists, credentials, passwords, and text | string | Optional |

### Supported Parameter Types

- boolean: a Boolean value, with a default value of either __true__ or __false__ , which is a checkbox on the UI
- string: a string, an input box
- text: text, a text box
- password: a string, a password input box
- choice: a drop-down list on the UI. When multiple options are defined, you can define multiple lines in the default field, for example,

    ```yaml
    type: choice
    default: |
      choice 1
      choice 2
    ```

- credential: a credential, a drop-down list on the UI that obtains the credential list in the current workspace

## __jenkinsfileTemplate__ Section

Overall, it still follows the [Jenkinsfile syntax](https://www.jenkins.io/doc/book/pipeline/syntax/), but you can use [go template](https://pkg.go.dev/text/template) as the template engine to render based on the parameters defined in __parameterDefinitions__ .

### Variables

Reference the parameters defined above in the form of __{{ .params.<name> }}__ , for example __{{ .params.gitCloneURL }}__ .

### Conditional Statements

The following three formats of conditional statements are supported:

```go
{{if pipeline}} T1 {{end}}
    If the value of pipeline is empty, nothing is output; otherwise, T1 is executed.
    An empty value in a template is mainly a false Boolean value or a string of zero length.

{{if pipeline}} T1 {{else}} T0 {{end}}
    If the value of pipeline is empty, T0 is executed; otherwise, T1 is executed.

{{if pipeline}} T1 {{else if pipeline}} T0 {{end}}
    To simplify the appearance of the if-else chain, the else action of an if can directly contain another if; the effect is exactly the same as writing
    {{if pipeline}} T1 {{else}}{{if pipeline}} T0 {{end}}{{end}}
```

### Loop Statements

The following two formats of loop statements are supported:

```go
{{range pipeline}} T1 {{end}}
    The value of pipeline must be an array, slice, map, or channel.
    We do not support defining Parameters of the above types for now.

{{range pipeline}} T1 {{else}} T0 {{end}}
    If the length of pipeline is empty, T0 is executed; otherwise, T1 is executed.
```

### Others

What is described above is only part of the go template syntax. In addition, you can also use the pipe symbol __|__ , functions (such as __printf__ ), comments, and so on. For more syntax, refer to [go template](https://pkg.go.dev/text/template).

## Example Template File

```yaml
parameterDefinitions:
  - name: gitCloneURL
    displayName: code repo address
    description: The git clone url of the source code
    type: string
  - name: gitRevision
    displayName: code repo branch
    description: The git revision of the source code
    type: string
    default: master
  - name: gitCredential
    displayName: credential
    description: The credential to access the source code
    type: credential
    default: ""
  - name: testCommand
    displayName: test command
    description: The command to run the test
    type: string
    default: go test -v -coverprofile=coverage.out
  - name: reportLocation
    displayName: test report location
    description: The location of the test report
    type: string
    default: ./target/**
  - name: dockerfilePath
    displayName: Dockerfile path
    description: The path of the Dockerfile
    type: string
    default: .
  - name: image
    displayName: target image address
    description: The target image to build
    type: string
  - name: tag
    displayName: tag
    description: The tag of the target image
    type: string
    default: latest
  - name: registryCredential
    displayName: container registry credentials
    description: The credential to access the container registry
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
