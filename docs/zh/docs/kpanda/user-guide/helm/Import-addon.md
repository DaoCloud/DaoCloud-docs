# 将自定义 Helm 应用导入系统内置 Addon

本文从离线和在线两种环境说明如何将 Helm 应用导入到系统内置的 Addon 中。

## 离线环境

离线环境指的是无法连通互联网或封闭的私有网络环境。

### 前提条件

- 存在可以运行的 [charts-syncer](https://github.com/DaoCloud/charts-syncer)。
  若没有，可[点击下载](https://github.com/DaoCloud/charts-syncer/releases)。
- Helm Chart 已经完成适配 [charts-syncer](https://github.com/DaoCloud/charts-syncer)。
  即在 Helm Chart 内添加了 `.relok8s-images.yaml` 文件。该文件需要包含 Chart 中所有使用到镜像，
  也可以包含 Chart 中未直接使用的镜像，类似 Operator 中使用的镜像。

!!! note

    - 如何编写 Chart 可参考 [image-hints-file](https://github.com/vmware-tanzu/asset-relocation-tool-for-kubernetes#image-hints-file)。
      要求镜像的 registry 和 repository 必须分开，因为 load 镜像时需替换或修改 registry/repository。
    - 安装器所在的火种集群已安装 [charts-syncer](https://github.com/DaoCloud/charts-syncer)。
      若将自定义 Helm 应用导入安装器所在火种集群，可跳过下载直接适配；
      若未安装 [charts-syncer](https://github.com/DaoCloud/charts-syncer)二进制文件，
      可[立即下载](https://github.com/DaoCloud/charts-syncer/releases)。

### 同步 Helm Chart

1. 进入`容器管理` -> `Helm 应用` -> `Helm 仓库`，搜索 addon，获取内置仓库地址和用户名/密码（系统内置仓库默认用户名/密码为 rootuser/rootpass123）。

![helm list](.kpanda/images/helmlist.png)

![helm detail](./images/helmdetail.png)

1. 同步 Helm Chart 到容器管理内置仓库 Addon

    * 编写如下配置文件，可以根据具体配置修改，并保存为 `sync-dao-2048.yaml`。

        ```yaml
        source:  # helm charts 源信息
          repo:
            kind: HARBOR # 也可以是任何其他支持的 Helm Chart 仓库类别，比如 CHARTMUSEUM
            url: https://release-ci.daocloud.io/chartrepo/community #  需更改为 chart repo url
            #auth: # 用户名/密码,若没有设置密码可以不填写
              #username: "admin"
              #password: "Harbor12345"
        charts:  # 需要同步
          - name: dao-2048 # helm charts 信息，若不填写则同步源 helm repo 内所有 charts
            versions:
              - 1.4.1
        target:  # helm charts 目标信息
          containerRegistry: 10.5.14.40 # 镜像仓库 url
          repo:
            kind: CHARTMUSEUM # 也可以是任何其他支持的 Helm Chart 仓库类别，比如 HARBOR
            url: http://10.5.14.40:8081 #  需更改为正确 chart repo url，可以通过 helm repo add $HELM-REPO 验证地址是否正确
            auth: # 用户名/密码，若没有设置密码可以不填写
              username: "rootuser"
              password: "rootpass123"
          containers:
            # kind: HARBOR # 若镜像仓库为 HARBOR 且希望 charts-syncer 自动创建镜像 Repository 则填写该字段  
            # auth: # 用户名/密码，若没有设置密码可以不填写 
              # username: "admin"
              # password: "Harbor12345"
 
        # leverage .relok8s-images.yaml file inside the Charts to move the container images too
        relocateContainerImages: true
        ```

    * 执行 charts-syncer 命令同步 Chart 及其包含的镜像

        ```sh
        charts-syncer sync --config sync-dao-2048.yaml --insecure --auto-create-repository
        ```

        预期输出为：

        ```console
        I1222 15:01:47.119777    8743 sync.go:45] Using config file: "examples/sync-dao-2048.yaml"
        W1222 15:01:47.234238    8743 syncer.go:263] Ignoring skipDependencies option as dependency sync is not supported if container image relocation is true or syncing from/to intermediate directory
        I1222 15:01:47.234685    8743 sync.go:58] There is 1 chart out of sync!
        I1222 15:01:47.234706    8743 sync.go:66] Syncing "dao-2048_1.4.1" chart...
        .relok8s-images.yaml hints file found
        Computing relocation...
 
        Relocating dao-2048@1.4.1...
        Pushing 10.5.14.40/daocloud/dao-2048:v1.4.1...
        Done
        Done moving /var/folders/vm/08vw0t3j68z9z_4lcqyhg8nm0000gn/T/charts-syncer869598676/dao-2048-1.4.1.tgz
        ```

3. 待上一步执行完成后，进入`容器管理` -> `Helm 应用` -> `Helm 仓库`，找到对应 Addon，
   在操作栏点击`同步仓库`，回到 Helm 模板就可以看到上传的 Helm 应用

![helm 同步](./images/helmsyn.png)

![详情2048](./images/helm2048.png)

4. 后续可正常进行安装、升级、卸载

![安装升级](./images/Installation-and-upgrade.png)

## 在线环境

在线环境的 Helm Repo 地址为 `release.daocloud.io`。
如果用户无权限添加 Helm Repo，则无法将自定义 Helm 应用导入系统内置 Addon。
您可以添加自己搭建的 Helm 仓库，然后按照离线环境中同步 Helm Chart 的步骤将您的 Helm 仓库集成到平台使用。
