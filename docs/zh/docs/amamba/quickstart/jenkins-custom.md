# 在 Jenkins 中使用自定义工具链

应用工作台运行流水线的镜像内置了常用的工具，包括：make、wget、gcc等[^1]。
应用工作台支持集成用户自定义的工具或者是特定版本的工具，可用于以下场景：

- 升级/降级到特定版本以修复工具的 Bug;
- 安装流水线运行依赖的工具（例如：yq、curl、kustomize 等）；
- 提前准备代码依赖的包以加快编译；

应用工作台支持通过 Volume 挂载或构建自定义镜像两种方式添加自定义工具链。

## 通过 Volume 挂载

第一种方式是使用 **init** 容器和 **volumeMount** 的方式拷贝工具到 agent 容器里。
通过修改 jenkins casc 的 ConfigMap，修改容器的默认行为。以 go 为例，下面这个例子中，
**init** 容器使用另一个版本的 Helm 覆盖了 agent 中自带的 Helm：

```yaml
 jenkins.yaml: |
    jenkins:
      mode: EXCLUSIVE
      ...
      clouds:
        - kubernetes:
            templates:
              - name: go
                label: go
                yaml: |
                  spec:
                    volumes:
                    # 1. Define an emptyDir volume which will hold the custom binaries
                    - emptyDirVolume:
                        memory: true
                        name: custom-tools
                    # 2. Use an init container to download/copy custom binaries into the emptyDir
                    initContainers:
                    - args:
                      - wget -qO- https://storage.googleapis.com/kubernetes-helm/helm-v2.12.3-linux-amd64.tar.gz
                        | tar -xvzf - &&
                        mv linux-amd64/helm /custom-tools/
                      command:
                      - sh
                      - -c
                      image: alpine:3.8
                      name: download-tools
                      volumeMounts:
                      - mountPath: /custom-tools
                        name: custom-tools
                    # 3. Volume mount the custom binary to the bin directory (overriding the existing version)
                    containers:
                    - name: go
                      volumeMounts:
                      - mountPath: /usr/local/bin/helm
                        name: custom-tools
                        subPath: helm
```

## 创建自定义镜像

第二种方式是 BYOI (Build Your Own Image)，指通过自定义镜像的方式，将自定义工具链打包到镜像中。
这种方式的好处是不需要在每个流水线中都下载工具，但是需要维护一个自定义镜像。下面是一个例子：

```dockerfile
ARG RUNTIME
ARG REGISTRY_REPO
FROM $REGISTRY_REPO/amamba/jenkins-agent/builder-base:latest$RUNTIME

# Install tools needed for your repo-server to retrieve & decrypt secrets, render manifests 
# (e.g. curl, awscli, gpg, sops)
RUN apt-get update && \
    apt-get install -y \
        curl \
        awscli \
        gpg && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \
    curl -o /usr/local/bin/sops -L https://github.com/mozilla/sops/releases/download/3.2.0/sops-3.2.0.linux && \
    chmod +x /usr/local/bin/sops

```

在创建流水线的时候选择 Agent 类型选择 kubernetes，YAML 文件如下：

```groovy
pipeline {
  agent {
    kubernetes {
      yaml '''
        apiVersion: v1
        kind: Pod
        metadata:
          labels:
            some-label: some-label-value
        spec:
          containers:
          - name: maven
            image: your-custom-tooling-image
            command:
            - cat
            tty: true
        '''
      retries 2
    }
  }
  stages {
    stage('Run maven') {
      steps {
        container('maven') {
          sh 'mvn -version'
        }
        container('busybox') {
          sh '/bin/busybox'
        }
      }
    }
  }
}
```

## 参考

- <https://plugins.jenkins.io/kubernetes>
- <https://argo-cd.readthedocs.io/en/stable/operator-manual/custom_tools/>

[^1]: 完整列表可以参考：<https://docs.daocloud.io/amamba/user-guide/pipeline/config/agent/#label_1>
