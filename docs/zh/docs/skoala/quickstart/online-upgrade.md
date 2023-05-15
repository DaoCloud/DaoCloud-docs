# 在线升级微服务引擎

开始升级操作之前，了解一下微服务引擎的部署架构有助于更好地理解后续的升级过程。

微服务引擎由两个组件构成：

- `skoala` 组件安装在控制面集群，用于在 DCE 5.0 的一级导航栏中加载微服务引擎模块
- `skoala-init` 组件安装在工作集群，用于提供微服务引擎的核心功能，例如创建注册中心、网关实例等

!!! note

    - 升级微服务引擎时需要同时升级这两个组件，否则会存在版本不兼容的情况。
    - 有关微服务引擎的版本更新情况，可参考 [release notes](../intro/release-notes.md)。

## 升级 `skoala` 组件

由于 `skoala` 组件安装在控制面集群中，所以需要在控制面集群中执行下列操作。

1. 升级依赖的数据库

    !!! note “此步骤为可选项”

        - 如果从低于 0.19.0 的 **微服务引擎版本** 升级到 0.19.0，则 **必须** 执行此步骤。
        - 如果从 0.19.0 版本升级到更高的 **微服务引擎版本**，则查看对应版本的 [release notes](../intro/release-notes.md) 是否提及需要升级依赖的数据库：
            
            - 如果需要升级数据库，则执行此步骤。
            - 如果未提及升级数据库，则跳过此步骤。

    在 `job.yaml` 文件中按照如下说明修改配置之后，通过 `kubectl apply` 命令运行该文件。

    ```yaml
    sweet:
    type:  UPGRADE
      target: 0.17.0  # (1) 
      tag: v0.19.0   # (2) 
    ```

    1. 固定值，无需修改
    2. 固定值，无需修改

2. 执行如下命令备份原有数据

    ```bash
    helm -n skoala-system get values skoala > skoala.yaml
    ```

3. 添加微服务引擎的 Helm 仓库

    ```bash
    helm repo add skoala https://release.daocloud.io/chartrepo/skoala
    ```

4. 更新微服务引擎的 Helm 仓库

    ```bash
    helm repo update
    ```

5. 执行 `helm upgrade` 命令

    ```bash
    helm --kubeconfig /tmp/deploy-kube-config upgrade --install --create-namespace -n skoala-system skoala skoala/skoala --version=0.19.2 --set hive.image.tag=v0.19.2 --set sesame.image.tag=v0.19.2 -f skoala.yaml
    ```

    > 需要将 `version`、`hive.image.tag`、`sesame.image.tag` 三个参数的值调整为您需要升级到的微服务引擎的版本号。

## 升级 `skoala-init` 组件

由于 `skoala-init` 组件安装在工作集群中，所以需要在每个工作集群中各执行一次下列操作。
<!--如果需要升级，会在release notes中强调-->

1. 备份原有参数

    ```bash
    helm -n skoala-system get values skoala-init > skoala-init.yaml
    ```

2. 添加微服务引擎的 Helm 仓库

    ```bash
    helm repo add skoala https://release.daocloud.io/chartrepo/skoala
    ```

3. 添加微服务引擎的 Helm 仓库

    ```bash
    helm repo update
    ```

4. 执行 `helm upgrade` 命令

    ```bash
    helm --kubeconfig /tmp/deploy-kube-config upgrade --install --create-namespace -n skoala-system skoala-init skoala/skoala-init --version=0.19.2 --set nacos-operator.image.tag=v0.19.2 --set skoala-agent.image.tag=v0.19.2 --set sentinel-operator.image.tag=v0.19.2 -f skoala-init.yaml
    ```
  
    !!! note

        - 需要将 `version`、`nacos-operator.image.tag`、`skoala-agent.image.tag`、`sentinel-operator.image.tag` 四个参数的值调整为您需要升级到的微服务引擎的版本号。

5. 根据自身需要，手动删除所需更新的其他 crd 文件，重新运行对应的文件。

    ```bash
    kubectl apply -f xxx.yaml
    ```
