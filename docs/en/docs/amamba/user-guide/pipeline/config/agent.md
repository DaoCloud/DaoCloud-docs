# Pipeline Node (Agent)

An **Agent** defines the execution environment for an entire **pipeline** or a specific **stage**. It must be declared at the top of the **configuration file** or within each **stage**.

This document describes how to extend a Jenkins Agent running in Kubernetes using the [Kubernetes plugin for Jenkins](https://plugins.jenkins.io/kubernetes/).

## Introduction to Kubernetes Pod Templates

The Kubernetes plugin runs a special container, **jnlp**, within the Jenkins Agent Pod. This container facilitates communication between the Jenkins Controller and the Jenkins Agent. Additional containers must be defined to execute pipeline steps, and you can switch between them using the **container** command.

## Use the built-in Label

The Workbench declares labels using the `podTemplate` feature and provides built-in SDKs for users.

### SDKs

The runtime supports both Docker and Podman, but the operating system varies:

| SDK (Label) | Version Info | Default Container Name | Operating System |
|------------|-------------|----------------------|----------------|
| base | - | base | CentOS 7.9<br />Ubuntu 22.04 |
| maven | java: 8 <br />maven: 3.9.9 | maven | CentOS 7.9<br />Ubuntu 22.04 |
| maven-jdk11 | java: 11 <br />maven: 3.9.9 | maven | CentOS 7.9<br />Ubuntu 22.04 |
| maven-jdk17 | java: 17 <br />maven: 3.9.9 | maven | Ubuntu 22.04 |
| maven-jdk21 | java: 21 <br />maven: 3.9.9 | maven | Ubuntu 22.04 |
| go | go: 1.17.13 | go | CentOS 7.9<br />Ubuntu 22.04 |
| go-1.18.10 | go: 1.18.10 | go | Ubuntu 22.04 |
| go-1.20.14 | go: 1.20.14 | go | Ubuntu 22.04 |
| go-1.22.6 | go: 1.22.6 | go | Ubuntu 22.04 |
| python | python: 3.8.19<br />Both `python` and `python3` point to Python 3.8 | python | CentOS 7.9<br />Ubuntu 22.04 |
| python-2.7.9 | python: 2.7.9<br />Both `python` and `python2` point to Python 2.7 | python | Ubuntu 22.04 |
| python-3.10.9 | python: 3.10.9<br />Both `python` and `python3` point to Python 3.10 | python | Ubuntu 22.04 |
| python-3.11.9 | python: 3.11.9<br />Both `python` and `python3` point to Python 3.11 | python | Ubuntu 22.04 |
| node.js | node: 16.20.2 <br />yarn: 1.22.22 | nodejs | CentOS 7.9<br />Ubuntu 22.04 |
| node.js-18.20.4 | node: 18.20.4 <br />yarn: 1.22.22 | nodejs | Ubuntu 22.04 |
| node.js-20.17.0 | node: 20.17.0 <br />yarn: 1.22.22 | nodejs | Ubuntu 22.04 |

### Built-in Command-Line Tools

| Tool | Version | Operating System |
|------|---------|----------------|
| podman | Ubuntu 22.04: 5.1.0<br />CentOS 7.9: 3.0.1 | Ubuntu 22.04, CentOS 7.9 |
| docker | 27.1.2 | Ubuntu 22.04, CentOS 7.9 |
| helm | 3.15.4 | Ubuntu 22.04, CentOS 7.9 |
| kubectl | v1.31.0 | Ubuntu 22.04, CentOS 7.9 |
| argocd | v2.12.1 | Ubuntu 22.04, CentOS 7.9 |
| argo rollouts | v1.7.2 | Ubuntu 22.04, CentOS 7.9 |
| sonar_scanner | 4.8.0.2856 | Ubuntu 22.04, CentOS 7.9 |
| yq | v4.44.3 | Ubuntu 22.04, CentOS 7.9 |
| make | - | Ubuntu 22.04, CentOS 7.9 |
| build-essential | - | Ubuntu 22.04 |
| libcurl4-openssl-dev | - | Ubuntu 22.04 |
| libssl-dev | - | Ubuntu 22.04 |
| wget | - | Ubuntu 22.04, CentOS 7.9 |
| git | - | Ubuntu 22.04, CentOS 7.9 |
| curl | - | Ubuntu 22.04, CentOS 7.9 |
| autoconf | - | Ubuntu 22.04, CentOS 7.9 |
| zip | - | Ubuntu 22.04, CentOS 7.9 |
| unzip | - | Ubuntu 22.04, CentOS 7.9 |
| jq | - | Ubuntu 22.04, CentOS 7.9 |
| locales | - | Ubuntu 22.04 |
| vim | - | Ubuntu 22.04, CentOS 7.9 |
| gettext | - | Ubuntu 22.04, CentOS 7.9 |
| tree | - | Ubuntu 22.04, CentOS 7.9 |
| gcc | - | CentOS 7.9 |
| gcc-c++ | - | CentOS 7.9 |
| curl-devel | - | CentOS 7.9 |
| glibc-common | - | CentOS 7.9 |

!!! note

    **CentOS 7.9 has reached end-of-life (EOL).** It is retained only for compatibility with older pipeline build environments. For new environments, it is recommended to use SDKs that support Ubuntu 22.04.

## Using Built-in Labels

- You can use the `go` podTemplate in a `Jenkinsfile` like this:

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

- Alternatively, in the **Pipeline Editor**, you can select an Agent of type **node** with the label **go**.

    ![agent-base](https://docs.daocloud.io/daocloud-docs-images/docs/amamba/images/agent-base.jpeg)

## Custom podTemplate

If you have specific build environment requirements, refer to [Creating a Custom Image](../../../quickstart/jenkins-custom.md#_1) for implementation details.
