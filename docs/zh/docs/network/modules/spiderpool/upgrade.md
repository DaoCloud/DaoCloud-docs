# 升级

本页说明如何将 DCE 5.0 的旧版本 Spiderpool（小于或等于v0.5.0），升级到新版本。本文中以 Spiderpool 到 v0.7.0 为例。

## 前提条件

1. 一套 Kubernetes 集群
2. 已安装 [Helm](https://helm.sh/docs/intro/install/)。

## 升级环境

DCE 5.0 中已部署其他更低版本的 Spiderpool，例如。

![spiderpool 0.5.0](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/network/images/spiderpool-before-upgrade.png)

## 获取 Chart 包与镜像

您可以根据下面两种方式之一，同步镜像包和 chart 包到离线仓库。

### 方式一：升级 addon 离线包，同步更新 Spiderpool chart 包和镜像

Spiderpool 的离线包存放在 addon 中，你可以参考[下载 addon 离线包](../../../download/addon/history.md)，下载最新的 addon 离线包，在下载后，打开 clusterConfig.yaml，修改 addonOfflinePackagePath 字段，指定 addon 所在的路径，完成 addon 离线包的升级。

1. addon 升级后，即可通过如下方式，获取 Chart 包

    参考如下方式，通过 DCE 5.0 界面下载 v0.7.0 的 chart 包

    ![spiderpool chart](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/network/images/spiderpool-chart-version-7.png)

2. 上传并解压 Chart 包到环境中

    ```bash
    tar -xvf spiderpool-0.7.0.tgz -C /root/spiderpool
    ```

### 方式二：手动升级 Spiderpool

1. 获取 Chart 包

    在环境上通过如下 helm 方式，获取 Chart 包。

    ```bash
    $ helm repo add spiderpool https://spidernet-io.github.io/spiderpool
    $ helm repo update spiderpool
    $ helm search repo spiderpool/spiderpool --versions
    NAME                   CHART VERSION   APP VERSION  DESCRIPTION
    spiderpool/spiderpool  0.7.0           0.7.0        ipam for kubernetes cni
    ...
    $ helm fetch spiderpool/spiderpool --version 0.7.0
    $ ls spiderpool-0.7.0.tgz
    spiderpool-0.7.0.tgz
    ```

    将 chart 包上传到离线仓库。

    ```shell
    # 传 charts 包
    helm repo add [addon] http://10.5.10.210:8081 # addon 替换为离线仓库名称，以及替换你的镜像仓库 url
    helm cm-push -u rootuser -p rootpass123 --insecure {chart 目录或 tar 包} # 替换你的镜像仓库用户名与密码。
    ```

2. 获取离线镜像包

    在任意可通外网的且安装了 docker 的环境上，执行下列命令获取 Spiderpool 的镜像。

    ```shell
    docker pull ghcr.m.daocloud.io/spidernet-io/spiderpool/spiderpool-controller:v0.7.0
    docker pull ghcr.m.daocloud.io/spidernet-io/spiderpool/spiderpool-agent:v0.7.0
    ```

    通过 `docker save` 保存为离线镜像 tar 包，并上传到离线环境。

    ```shell
    $ docker save -o spiderpool-0.7.0.tar ghcr.m.daocloud.io/spidernet-io/spiderpool/spiderpool-controller:v0.7.0 ghcr.m.daocloud.io/spidernet-io/spiderpool/spiderpool-agent:v0.7.0
    ```

3. 在需升级的环境中加载镜像到 Docker 或 Containerd。
  
    === "Docker"

        ```shell
        docker load -i spiderpool-0.7.0.tar
        ```

    === "containerd"

        ```shell
        ctr -n k8s.io image import spiderpool-0.7.0.tar
        ```

!!! note

    每个 node 都需要做 Docker 或 containerd 加载镜像操作，
    加载完成后需要 tag 镜像，保持 Registry、Repository 与安装时一致。

## 删除 spiderpool-init

在 v0.7.0 版本开始，Spiderpool 引入了 Spidercoordinators 插件，Spidercoordinators 的默认配置将在 spiderpool-init 被创建时自动下发，在进行升级前，请先删除该 Pod。通过 helm upgrade 更新时，会自动创建 spiderpool-init Pod，并下发创建 Spidercoordinators 的默认配置。

```bash
[root@controller-node-1 ~]# kubectl get po -n kube-system spiderpool-init
NAME              READY   STATUS      RESTARTS   AGE
spiderpool-init   0/1     Completed   0          49m
[root@controller-node-1 ~]# kubectl delete po -n kube-system spiderpool-init
pod "spiderpool-init" deleted
```

## 更新 CRD

由于通过 helm 无法在界面完成 CRD 的更新，在集群 master 节点上通过 kubectl apply 更新 Spiderpool 版本的 CRD。

```bash
[root@controller-node-1 crds]# ls
spiderpool.spidernet.io_spidercoordinators.yaml  spiderpool.spidernet.io_spiderippools.yaml        spiderpool.spidernet.io_spiderreservedips.yaml
spiderpool.spidernet.io_spiderendpoints.yaml     spiderpool.spidernet.io_spidermultusconfigs.yaml  spiderpool.spidernet.io_spidersubnets.yaml

[root@controller-node-1 crds]# ls | grep '\.yaml$' | xargs -I {} kubectl apply -f {}
customresourcedefinition.apiextensions.k8s.io/spidercoordinators.spiderpool.spidernet.io created
customresourcedefinition.apiextensions.k8s.io/spiderendpoints.spiderpool.spidernet.io configured
customresourcedefinition.apiextensions.k8s.io/spiderippools.spiderpool.spidernet.io configured
customresourcedefinition.apiextensions.k8s.io/spidermultusconfigs.spiderpool.spidernet.io created
customresourcedefinition.apiextensions.k8s.io/spiderreservedips.spiderpool.spidernet.io configured
customresourcedefinition.apiextensions.k8s.io/spidersubnets.spiderpool.spidernet.io configured
```

## 通过 DCE 5.0 界面升级

在前面的步骤中，已经正确上传离线 chart 与镜像包到离线环境中，现在可通过 5.0 界面执行升级。在低于 0.7.0 的版本中 Spiderpool 会搭配 Multus-underlay 插件使用，而新版本的 Spiderpool 中已经集成了 Multus 插件，在界面进行更新操作时，请关闭「安装 multus」按钮，避免重复安装，如下图所示。点击更新，等待更新完成。

![disable multus](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/network/images/spiderpool-disable-multus.png)

## 验证

升级后检查版本正常。

![spiderpool 0.7.0](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/network/images/spiderpool-after-upgrade.png)

在 0.7.0 及以上的 Spiderpool 版本中，提供了 SpiderMultusConfig CR 来自动管理 Multus NetworkAttachmentDefinition CR 。如果您的集群中存在旧的 Multus CR，在新版本由于创建机制的不同，UI 中并不会显示出来您旧有的 MUltus CR，你可以通过界面创建同名的 Multus CR 进行纳管，并不会影响您原有功能的使用。注意，界面上所填写的 `Vlan ID`、`网卡接口`等值，需要与您原本的 Multus CR 中保持完全一致。

![multus cr create](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/network/images/spiderpool-multus-cr-create.png)
