# Pipeline node (Agent)

Agent describes the entire __pipeline__ execution process or the execution environment of a certain __stage__ , and must appear at the top of the __description file__ or each __stage__ .

This article describes how to extend the Jenkins Agent running in Kubernetes based on the [Kubernetes plugin for Jenkins](https://plugins.jenkins.io/kubernetes/) plugin.

## Kubernetes Pod template introduction

This Kubernetes plugin will run a special container __jnlp__ in the Jenkins Agent Pod. The purpose is to communicate between the Jenkins Controller and the Jenkins Agent, so you need to define other containers to run the pipeline steps, and you can use the __container__ command to Switch between different containers.

## Use the built-in Label

Workbench declares 6 labels through the podTemplate capability: __base__ , __maven__ , __go__ , __go16__ , __node.js__ and __python__ . You can specify a specific Agent label to use the corresponding podTemplate.

- Can use go podTemplate via __node('go')__ in Jenkinsfile.

    ```groovy
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

- You can also select an Agent whose type is __node__ and whose label is __go__ on the __Edit Pipeline__ page.

    <!--![]()screenshots-->

### Built-in Labels

The built-in Jenkins Agent Labels have the following options:

=== "base"

    | Name        | Type/Version                        |
    | ----------- | ----------------------------------- |
    | Container   | base                                |
    | Operating System | centos-7 (7.9.2009)             |
    | Podman      | podman version 3.0.1                |
    | Kubectl     | v1.22.0                             |
    | Built-in Tools | unzip, which, make (GNU Make 3.82), wget, zip, bzip2, git (2.9.5) |

=== "maven"

    | Name        | Type/Version                        |
    | ----------- | ----------------------------------- |
    | Container   | maven                               |
    | Operating System | centos-7 (7.9.2009)             |
    | Jdk         | openjdk-1.8.0_322                   |
    | Maven       | 3.5.3                               |
    | Podman      | podman version 3.0.1                |
    | Kubectl     | v1.22.0                             |
    | Built-in Tools | unzip, which, make (GNU Make 3.82), wget, zip, bzip2, git (2.9.5) |

=== "mavenjdk11"

    | Name        | Type/Version                        |
    | ----------- | ----------------------------------- |
    | Container   | maven                               |
    | Operating System | centos-7 (7.9.2009)             |
    | Jdk         | openjdk-11.0.19                      |
    | Maven       | 3.5.3                               |
    | Podman      | podman version 3.0.1                |
    | Kubectl     | v1.22.0                             |
    | Built-in Tools | unzip, which, make (GNU Make 3.82), wget, zip, bzip2, git (2.9.5) |

=== "go"

    | Name        | Type/Version                        |
    | ----------- | ----------------------------------- |
    | Container   | go                                  |
    | Operating System | centos-7 (7.9.2009)             |
    | Go          | 1.12.10                             |
    | GOPATH      | /home/jenkins/go                    |
    | GOROOT      | /usr/local/go                       |
    | Podman      | podman version 3.0.1                |
    | Kubectl     | v1.22.0                             |
    | Built-in Tools | unzip, which, make (GNU Make 3.82), wget, zip, bzip2, git (2.9.5) |

=== "node.js"

    | Name        | Type/Version                        |
    | ----------- | ----------------------------------- |
    | Container   | nodejs                             |
    | Operating System | centos-7 (7.9.2009)             |
    | Node        | v10.16.3                            |
    | Yarn        | 1.16.0                              |
    | Podman      | podman version 3.0.1                |
    | Kubectl     | v1.22.0                             |
    | Built-in Tools | unzip, which, make (GNU Make 3.82), wget, zip, bzip2, git (2.9.5) |

=== "python"

    | Name        | Type/Version                        |
    | ----------- | ----------------------------------- |
    | Container   | python                             |
    | Operating System | centos-7 (7.9.2009)             |
    | Python      | 3.7.11                              |
    | Podman      | podman version 3.0.1                |
    | Kubectl     | v1.22.0                             |
    | Built-in Tools | unzip, which, make (GNU Make 3.82), wget, zip, bzip2, git (2.9.5) |

## Customize podTemplate using YAML

If you need to run the Jenkins Agent in a specific environment, you can customize the Jenkins Agent on the pipeline.

1. Select the Agent type as __kubernetes__ on the __Edit Pipeline__ page.

    <!--![]()screenshots-->

2. Click __YAML Editor__ and fill in the YAML statement in the dialog box, please refer to the following example:

    ```yaml
    apiVersion: v1
    kind: Pod
    spec:
      containers:
      - name: jnlp
        image: docker.m.daocloud.io/jenkins/inbound-agent:4.10-2  # (1)!
        args:
        - ^${computer.jnlpmac} ^${computer.name}
      - name: golang
        image: golang:1.16.5   # (2)!
        command:
        - sleep
        args:
        - 99d
    ```

    1. You need to provide the address of the JNLP image,
       otherwise, the default "jenkins/inbound-agent" will be used.
    2. Fill in your custom image.

3. Enter __golang__ in Container as the default container for pipeline operation.

    <!--![]()screenshots-->

4. To use other containers of the above examples in other steps of the pipeline, you can select __Specify container__ to fill in the required container name.

    <!--![]()screenshots-->
