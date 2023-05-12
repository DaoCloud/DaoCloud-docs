# Pipeline template file

The pipeline template file mainly consists of two parts: `parameterDefinitions` and `jenkinsfileTemplate`.

- `parameterDefinitions` area: defines which parameters are exposed by the pipeline template. Multiple parameter types are supported such as Boolean, dropdown, credential, password, text, etc.
- `jenkinsfileTemplate` area: defines the `jenkinsfile` of the Jenkins pipeline, and can refer to the parameters exposed in `parameterDefinitions`.

## `parameterDefinitions` section

| Field | Type | Description | Default | Required |
| --- | --- | --- | --- | --- |
| name | string | parameter name | - | required |
| displayName | []byte | The name displayed on the form, the length is less than X characters | "" | optional |
| description | string | description of the parameter | "" | optional |
| default | json.Value | default value, if filled, the field is optional, otherwise it is required | nil | not required |
| type | string | For parameter type support, please refer to the parameter type (need to link to the following) | string | required |

## Supported parameter types

- boolean: Boolean value, the default value can only be `true` or `false`
- choice: a drop-down list, a default value must be provided, for example

    ```yaml
    type: choice
    default:
      - choice 1
      - choice 2
    ```

- credential: Credentials, which will get the list of credentials under the current workspace
- password: password
- text: text, input box

## Template file example

```yaml
parameterDefinitions:
  - name: gitCloneURL
    displayName: code warehouse address
    description: The git clone url of the source code
    type: string
  - name: gitRevision
    displayName: code warehouse branch
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
    displayName: mirror repository credentials
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