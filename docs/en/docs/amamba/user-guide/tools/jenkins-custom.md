# Using a custom toolchain in Jenkins

The image of the running pipeline of Workbench has built-in commonly used tools, including: make, wget, gcc, etc. [^1]. Workbench supports the integration of user-defined tools or tools of a specific version, which can be used in the following cases:

- Upgrade/downgrade to a specific version to fix bugs of the tool;
- Install the tools that the pipeline operation depends on (for example: yq, curl, kustomize, etc.);
- Prepare the packages that the code depends on in advance to speed up compilation;

Workbench supports adding a custom toolchain through volume mounting or building a custom image.

## Mount via Volume

The first way is to use the `init` container and `volumeMount` to copy tools to the agent container. Modify the default behavior of the container by modifying the configmap of jenkins casc. Taking go as an example, in the following example, the `init` container uses another version of Helm to override the Helm that comes with the agent:

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
                        mv linux-amd64/helm/custom-tools/
                      command:
                      -sh
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

## Create a custom image

The second method is BYOI (Build Your Own Image), which refers to packaging the custom toolchain into the image by customizing the image. The advantage of this approach is that there is no need to download tools in each pipeline, but a custom image needs to be maintained. Below is an example:

```dockerfile
ARG RUNTIME
ARG REGISTRY_REPO
FROM $REGISTRY_REPO/amamba/jenkins-agent/builder-base:latest$RUNTIME

# Install tools needed for your repo-server to retrieve & decrypt secrets, render manifests
# (e.g. curl, awscli, gpg, sops)
RUN apt-get update && \
    apt-get install -y \
        curl \
        awscli\
        gpg && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \
    curl -o /usr/local/bin/sops -L https://github.com/mozilla/sops/releases/download/3.2.0/sops-3.2.0.linux && \
    chmod +x /usr/local/bin/sops

```

When creating a pipeline, select the Agent type and select kubernetes. The YAML file is as follows:

```groovy
pipeline {
  agent {
    kubernetes {
      yaml'''
        apiVersion: v1
        kind: Pod
        metadata:
          labels:
            some-label: some-label-value
        spec:
          containers:
          -name: maven
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

## refer to

- <https://plugins.jenkins.io/kubernetes>
- <https://argo-cd.readthedocs.io/en/stable/operator-manual/custom_tools/>

[^1]: For a complete list, please refer to: <https://docs.daocloud.io/amamba/user-guide/pipeline/config/agent/#label_1>