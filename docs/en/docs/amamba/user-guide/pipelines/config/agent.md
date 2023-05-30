# Pipeline node (Agent)

Agent describes the entire `pipeline` execution process or the execution environment of a certain `stage`, and must appear at the top of the `description file` or each `stage`.

This article describes how to extend the Jenkins Agent running in Kubernetes based on the [Kubernetes plugin for Jenkins](https://plugins.jenkins.io/kubernetes/) plugin.

## Kubernetes Pod template introduction

This Kubernetes plugin will run a special container `jnlp` in the Jenkins Agent Pod. The purpose is to communicate between the Jenkins Controller and the Jenkins Agent, so you need to define other containers to run the pipeline steps, and you can use the `container` command to Switch between different containers.

## Use the built-in Label

Workbench declares 6 labels through the podTemplate capability: `base`, `maven`, `go`, `go16`, `node.js` and `python`. You can specify a specific Agent label to use the corresponding podTemplate.

- Can use go podTemplate via `node('go')` in Jenkinsfile.

    ```bash
    pipeline {
      agent {
        node {
          label 'go'
        }
      }
      
      stages {
        stage('go') {
          steps {
            container('go') {
              sh 'go version'
            }
          }
        }
      }
    }
    ```

- You can also select an Agent whose type is `node` and whose label is `go` on the `Edit Pipeline` page.

    <!--![]()screenshots-->

### Built-in Label environment description

**Jenkins Agent Label: base**

| name | type/version |
| -------- | ----------------------------------------- -------------------- |
| container name | base |
| OS | centos-7 (7.9.2009) |
| podman | podman version 3.0.1 |
| Kubectl | v1.22.0 |
| Built-in tools | unzip, which, make (GNU Make 3.82), wget, zip, bzip2, git (2.9.5) |

**Jenkins Agent Label: maven**

| name | type/version |
| -------- | ----------------------------------------- -------------------- |
| container name | maven |
| OS | centos-7 (7.9.2009) |
| Jdk | openjdk-1.8.0_322 |
| Maven | 3.5.3 |
| podman | podman version 3.0.1 |
| Kubectl | v1.22.0 |
| Built-in tools | unzip, which, make (GNU Make 3.82), wget, zip, bzip2, git (2.9.5) |

**Jenkins Agent Label: go**

| name | type/version |
| -------- | ----------------------------------------- -------------------- |
| container name | go |
| OS | centos-7 (7.9.2009) |
| Go | 1.12.10 |
| GOPATH | /home/jenkins/go |
| GOROOT | /usr/local/go |
| podman | podman version 3.0.1 |
| Kubectl | v1.22.0 |
| Built-in tools | unzip, which, make (GNU Make 3.82), wget, zip, bzip2, git (2.9.5) |

**Jenkins Agent Label: go16**

| name | type/version |
| -------- | ----------------------------------------- -------------------- |
| container name | go |
| OS | centos-7 (7.9.2009) |
| Go | 1.16.8 |
| GOPATH | /home/jenkins/go |
| GOROOT | /usr/local/go |
| podman | podman version 3.0.1 |
| Kubectl | v1.22.0 |
| Built-in tools | unzip, which, make (GNU Make 3.82), wget, zip, bzip2, git (2.9.5) |

**Jenkins Agent Label: node.js**

| name | type/version |
| -------- | ----------------------------------------- -------------------- |
| container name | nodejs |
| OS | centos-7 (7.9.2009) |
| Node | v10.16.3 |
| Yarn | 1.16.0 |
| podman | podman version 3.0.1 |
| Kubectl | v1.22.0 |
| Built-in tools | unzip, which, make (GNU Make 3.82), wget, zip, bzip2, git (2.9.5) |

**Jenkins Agent Label: python**

| name | type/version |
| -------- | ----------------------------------------- -------------------- |
| container name | python |
| OS | centos-7 (7.9.2009) |
| Python | 3.7.11 |
| podman | podman version 3.0.1 |
| Kubectl | v1.22.0 |
| Built-in tools | unzip, which, make (GNU Make 3.82), wget, zip, bzip2, git (2.9.5) |

## Customize podTemplate using YAML

If you need to run the Jenkins Agent in a specific environment, you can customize the Jenkins Agent on the pipeline.

1. Select the Agent type as `kubernetes` on the `Edit Pipeline` page.

    <!--![]()screenshots-->

2. Click `YAML Editor` and fill in the YAML statement in the dialog box, please refer to the following example:

    ```bash
    apiVersion: v1
    kind: Pod
    spec:
      containers:
      -name: maven
        image: maven:3.8.1-jdk-8
        command:
        - sleep
        args:
        -99d
      -name: golang
        image: golang:1.16.5
        command:
        - sleep
        args:
        -99d
      ```

3. Enter `golang` in Container as the default container for pipeline operation.

    <!--![]()screenshots-->

4. To use other containers of the above examples in other steps of the pipeline, you can select `Specify container` to fill in the required container name.

    <!--![]()screenshots-->