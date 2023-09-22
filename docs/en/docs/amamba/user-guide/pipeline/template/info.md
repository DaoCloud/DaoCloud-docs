## Pipeline Template File

The pipeline template file mainly contains two parts: `parameterDefinitions` and `jenkinsfileTemplate`.

- The `parameterDefinitions` section defines which parameters are exposed in the pipeline template. Multiple parameter types are supported, such as booleans, drop-down lists, credentials, passwords, and text.
- The `jenkinsfileTemplate` section defines a `jenkinsfile` for the Jenkins pipeline and can reference the parameters exposed in `parameterDefinitions` part.

## `parameterDefinitions` Section

| Field | Type | Description | Default Value | Required |
| --- | --- | --- | --- | --- |
| name | string | Parameter name | - | Required |
| displayName | []byte | Name displayed on the UI form, less than X characters | "" | Optional |
| description | string | Parameter description | "" | Optional |
| default | json.Value | Set a default value for the corresponding parameter | nil | Optional |
| type | string | Parameter type (booleans, drop-down lists, credentials, passwords, or text)| string | Required |

## Supported Parameter Types

- boolean: a Boolean value, with a default value of either `true` or `false`
- choice: a drop-down list, must provide a default value, for example,

    ```yaml
    type: choice
    default:
      - choice 1
      - choice 2
    ```

- credential: a credential, which can obtain the credential list in the current workspace
- password: a password
- text: a text input box

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
            archiveArtifacts '{{ .params. reportLocation }}'
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