# 保留 Jenkins 配置参数

Jenkins 的配置文件是通过 ConfigMap 存储的。
但是在实际使用中，您可能会修改某些配置项，如（修改 agent 的镜像，修改最大并行数）等，
通过 Helm 升级方式就会将您的配置覆盖，为了平衡 Jenkins 升级与您自定义配置之间的差异，
工作台提供了保留 Jenkins 配置参数的功能。

!!! tip

    应用工作台版本 >= v0.33.0，或者安装器版本 >= v0.24.0

## 配置步骤

1. 点击左上角的 **≡** 打开导航栏，选择 **容器管理** -> **集群列表** ，找到 `kpanda-global-cluster`，点击该集群的名称。
2. 在集群详情页，依次点击 **配置与密钥** -> **配置项** ，命名空间选择 `amamba-system`，通过名称 `global-jenkins-casc-config` 进行搜索。
3. 点击 **编辑 YAML** ，在 `data` 字段中添加如下配置：

    ```yaml
    kind: ConfigMap
    apiVersion: v1
    metadata:
      name: global-jenkins-casc-config
      namespace: amamba-system
    data:
      jenkins.yaml: | # 编辑这一部分
        xxxxx
    ```

    其中，`jenkins.yaml` 需要与 Jenkins CASC 配置项中的 `jenkins.yaml` **格式保持一致** 。
    你完成修改后，其中的内容会以 `patch` 的方式合并到 Jenkins 的配置文件中。

4. 在只升级了 Jenkins 的情况下，需要手动更新此 configmap 的 annotation 中的
   `amamba.io/casc-sync-at` 字段，以便更新到 Jenkins 中。

## 配置示例

下面给出一些配置示例：

- 添加一个 agent

    ```yaml
    jenkins.yaml: |
      jenkins:
        clouds:
          - kubernetes:
            name: "kubernetes"
            templates:
              - name: "new"
                label: "new"
                inheritFrom: "nodejs"
                containers:
                  - name: "nodejs"
                    image: "docker.m.daocloud.io/amambadev/jenkins-agent-nodejs:v0.4.6-20.17.0-ubuntu-podman"
    ```

- 设置最大并行的 agent 数量

    ```yaml
    jenkins.yaml: |
      jenkins:
        clouds:
          - kubernetes:
            containerCapStr: "100"
    ```

- 添加共享库配置:

    ```yaml
    jenkins.yaml: |
      unclassified:
        globalLibraries:
          libraries:
          - defaultVersion: "main"
            name: "amamba-shared-lib"
            retriever:
              modernSCM:
                scm:
                  git:
                    remote: "https://github.com/amamba-io/amamba-shared-lib.git"
    ```
