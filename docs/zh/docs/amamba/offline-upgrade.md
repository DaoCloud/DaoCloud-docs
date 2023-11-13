# 离线升级

应用工作台支持离线升级。您需要先从[安装包](../download/modules/amamba.md)中加载镜像，然后执行相应命令进行升级。

## 从安装包中加载镜像

支持通过两种方式加载镜像。

### 通过 charts-syncer 同步镜像

如果环境中存在镜像仓库，建议通过 charts-syncer 将镜像同步到镜像仓库，更加高效便捷。

1. 创建 `load-image.yaml` 文件。

    > 注意：该 YAML 文件中的各项参数均为必填项。您需要一个私有的镜像仓库，并修改相关配置。

    ```yaml title="load-image.yaml"
    source:
      intermediateBundlesPath: ghippo-offline # 到执行 charts-syncer 命令的相对路径，而不是此 YAML 文件和离线包之间的相对路径
    target:
      containerRegistry: 10.16.10.111 # 镜像仓库 url
      containerRepository: amamba # 镜像仓库的具体项目
      repo:
        kind: HARBOR # 也可以是任何其他支持的 Helm Chart 仓库类别，比如 ChartMuseum
        url: http://10.16.10.111/chartrepo/amamba #  需更改为 chart repo url
        auth: # 用户名/密码
          username: "admin"
          password: "Harbor12345"
      containers:
        auth: # 用户名/密码
          username: "admin"
          password: "Harbor12345"
    ```

    !!! note "若当前环境未安装 chart repo，也可以通过 chart-syncer 将 chart 导出为 `tgz` 文件，并存放在指定路径。"

        ```yaml title="load-image.yaml"
        source:
            intermediateBundlesPath: amamba-offline #  到执行 charts-syncer 命令的相对路径，而不是此 YAML 文件和离线包之间的相对路径
        target:
            containerRegistry: 10.16.10.111 # 需更改为你的镜像仓库 url
            containerRepository: release.daocloud.io/amamba # 需更改为你的镜像仓库
            repo:
              kind: LOCAL
              path: ./local-repo # chart 本地路径
            containers:
              auth:
                username: "admin" # 你的镜像仓库用户名
                password: "Harbor12345" # 你的镜像仓库密码
        ```

2. 执行如下命令同步镜像。

    ```bash
    charts-syncer sync --config load-image.yaml
    ```

### 通过 Docker 或 containerd 直接加载镜像

1. 执行下列命令解压镜像。

    ```shell
    tar xvf amamba.bundle.tar
    ```

    解压成功后会得到 3 个文件: `images.tar`、`hints.yaml`、`original-chart`。

1. 执行如下命令从本地加载镜像到 Docker 或 containerd。

    > 注意：需要在集群中的 **每个节点** 上执行如下操作。加载完成后需要为镜像打标签，确保 Registry、Repository 与安装时一致。

    ```shell
    docker load -i images.tar # for Docker
    ctr -n k8s.io image import images.tar # for containerd
    ```

## 升级

1. 检查应用工作台的 Helm 仓库是否存在。

    ```shell
    helm repo list | grep amamba
    ```

    若返回结果为空或出现 `Error: no repositories to show` 提示，则执行如下命令添加应用工作台的 Helm 仓库。

    ```shell
    helm repo add amamba http://{harbor url}/chartrepo/{project}
    ```

2. 更新应用工作台的 Helm 仓库。

    ```shell
    helm repo update amamba
    ```

    Helm 版本过低会导致失败。若失败，请尝试执行 helm update repo

3. 备份 `--set` 参数。在升级全局管理版本之前，建议执行如下命令备份旧版本的 `--set` 参数。

    ```shell
    helm get values ghippo -n ghippo-system -o yaml > amamba.bak.yaml
    ```

4. 选择想安装的应用工作台版本（建议安装最新版本）。

    ```shell
    helm search  repo amamba-release-ci --versions |head
    ```

    输出类似于：
    
    ```console
    NAME                       CHART VERSION   APP VERSION  DESCRIPTION                               
    amamba-release-ci/amamba   0.14.0  	       0.14.0  	    Amamba is the entrypoint to DCE 5.0, provides de...
    ```

5. 修改 `amamba.bak.yaml` 文件里的 `registry` 和 `tag`。

    ??? note "点击查看示例的 YAML 文件"

        ```yaml title="amamba.bak.yaml"
        amambaSyncer:
          resources:
            limits:
              cpu: 200m
              memory: 256Mi
            requests:
              cpu: 20m
              memory: 128Mi
        apiServer:
          configMap:
            debug: true
          fromJar:
            image:
              registry: releas-ci.daocloud.io
              repository: docker/library/openjdk
              tag: 11.0-jre-slim
          image:
            registry: release-ci.daocloud.io
            repository: amamba/amamba-apiserver
          resources:
            limits:
              cpu: "2"
              memory: 2Gi
            requests:
              cpu: 20m
              memory: 150Mi
        argo-cd:
          applicationSet:
            enabled: false
            image:
              repository: release-ci.daocloud.io/quay/argoproj/argocd
              tag: v2.4.12
          controller:
            image:
              repository: release-ci.daocloud.io/quay/argoproj/argocd
              tag: v2.4.12
            resources:
              limits:
                cpu: "2"
                memory: 2Gi
              requests:
                cpu: 100m
                memory: 256Mi
          dex:
            enabeld: true
            image:
              repository: release-ci.daocloud.io/ghcr/dexidp/dex
              tag: v2.32.0
            initImage:
              repository: release-ci.daocloud.io/quay/argoproj/argocd
              tag: v2.4.12
            resources:
              limits:
                cpu: 50m
                memory: 64Mi
              requests:
                cpu: 10m
                memory: 16Mi
          enabled: true
          notifications:
            enabled: false
          redis:
            enabled: true
            image:
              repository: release-ci.daocloud.io/docker/library/redis
              tag: 7.0.4-alpine
            metrics:
              enabled: false
            resources:
              limits:
                cpu: 200m
                memory: 128Mi
              requests:
                cpu: 5m
                memory: 16Mi
          repoServer:
            image:
              repository: release-ci.daocloud.io/quay/argoproj/argocd
              tag: v2.4.12
            resources:
              limits:
                cpu: 200m
                memory: 256Mi
              requests:
                cpu: 5m
                memory: 8Mi
          server:
            image:
              repository: release-ci.daocloud.io/quay/argoproj/argocd
              tag: v2.4.12
            resources:
              limits:
                cpu: 250m
                memory: 256Mi
              requests:
                cpu: 5m
                memory: 8Mi
            service:
              nodePortHttp: 31886
              nodePortHttps: 31887
              type: NodePort
        argo-rollouts:
          controller:
            image:
              registry: release-ci.daocloud.io
              repository: quay/argoproj/argo-rollouts
              tag: v1.2.0
            resources:
              limits:
                cpu: 100m
                memory: 128Mi
              requests:
                cpu: 16m
                memory: 128Mi
          dashboard:
            enabled: true
            image:
              registry: release-ci.daocloud.io
              repository: quay/argoproj/kubectl-argo-rollouts
              tag: v1.2.0
            resources:
              limits:
                cpu: 100m
                memory: 128Mi
              requests:
                cpu: 10m
                memory: 16Mi
            service:
              nodePort: 30070
              type: NodePort
          enabled: true
        devopsServer:
          enabled: true
          image:
            registry: release-ci.daocloud.io
            repository: amamba/amamba-devops-server
          resources:
            limits:
              cpu: "2"
              memory: 2Gi
            requests:
              cpu: 50m
              memory: 160Mi
        global:
          amamba:
            imageTag: v0.13-dev-a8ca782a
          imageRegistry: release-ci.daocloud.io
        mysql:
          busybox:
            repository: docker/busybox
            tag: 1.35.0
          image:
            repository: docker/mysql
            tag: 5.7.30
          persistence:
            size: 20Gi
          resources:
            limits:
              cpu: 500m
              memory: 512Mi
            requests:
              cpu: 20m
              memory: 256Mi
        ui:
          image:
            tag: v0.15.0-dev-fd64789e
          resources:
            limits:
              cpu: 100m
              memory: 128Mi
            requests:
              cpu: 5m
              memory: 4Mi
        
        ```

6. 执行如下命令进行升级

    ```shell
    helm upgrade amamba . \
      -n amamba-system \
      -f ./amamba.bak.yaml
    ```
