# 微服务引擎集群初始化组件

本教程旨在补充需要手工 **单独在线安装** 微服务引擎集群初始化组件的的场景。下文出现的 `skoala-init` 是微服务引擎集群初始化组件的内部开发代号，代指微服务引擎集群初始化组件。

微服务引擎集群初始化组件部署结构：

![image](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/skoala-init-cn.png)

蓝色框内的 chart 即 `skoala-init` 组件，需要安装在工作集群。安装 `skoala-init`
组件之后即可以使用微服务引擎的各项功能，例如创建注册中心、网关实例等。另外需要注意，
`skoala-init` 组件依赖 DCE 5.0 可观测模块的 `insight-agent` 组件提供指标监控和链路追踪等功能。
如您需要使用该项功能，则需要事先安装好 `insight-agent` 组件，
具体步骤可参考[安装组件 insight-agent](../../insight/quickstart/install/install-agent.md)。

!!! note

    - 如果安装 `skoala-init` 之前没有事先安装 `insight-agent`，则不会安装 `service-monitor`。
    - 如果需要安装 `service-monitor`，请先安装 `insight-agent`，然后再安装 `skoala-init`。

## 在线安装

skoala-init 是微服务引擎所有的组件 Operator：

- 仅安装到工作集群即可
- 包含组件有：skoala-agent、nacos-operator、sentinel-operator、seata-operator、contour-provisioner、gateway-api-adminssion-server
- 未安装时，创建注册中心和网关时会提示缺少组件

由于 Skoala 涉及的组件较多，我们将这些组件打包到同一个 Chart 内，也就是 skoala-init，
所以我们应该在用到微服务引擎的工作集群安装好 skoala-init。此安装命令也可用于更新该组件。

配置好 Skoala 仓库，即可查看和获取到 skoala-init 的应用 chart。

```bash
helm repo add skoala-release https://release.daocloud.io/chartrepo/skoala
helm repo update
```

```bash
$ helm search repo skoala-release/skoala-init --versions
NAME                        CHART VERSION   APP VERSION DESCRIPTION
skoala-release/skoala-init	0.28.1       	0.28.1     	A Helm Chart for Skoala init, it includes Skoal...
skoala-release/skoala-init	0.28.0       	0.28.0     	A Helm Chart for Skoala init, it includes Skoal...
skoala-release/skoala-init	0.27.2       	0.27.2     	A Helm Chart for Skoala init, it includes Skoal...
skoala-release/skoala-init	0.27.1       	0.27.1     	A Helm Chart for Skoala init, it includes Skoal...
......
```

执行以下命令，注意对应的版本号：

```bash
helm upgrade --install skoala-init --create-namespace -n skoala-system --cleanup-on-fail \
    skoala-release/skoala-init \
    --version 0.28.1
```

查看 Pod 是否启动成功：

```bash
$ kubectl get pods -n skoala-system
NAME                                   READY   STATUS    RESTARTS        AGE
contour-provisioner-54b55958b7-5ltng                  1/1     Running     0          2d6h
gateway-api-admission-patch-bk7c8                     0/1     Completed   0          2d6h
gateway-api-admission-pwhdh                           0/1     Completed   0          2d6h
gateway-api-admission-server-77545d74c4-v6fpr         1/1     Running     0          2d6h
nacos-operator-6d94bdccc8-wx4w5                       1/1     Running     0          2d6h
seata-operator-f556d989d-8qrf8                        1/1     Running     0          2d6h
sentinel-operator-6fb9dc98f4-d44k5                    1/1     Running     0          2d6h
skoala-agent-54d4df7897-7p4pz                         1/1     Running     0          2d6h
```

除了通过终端安装，也可以在 `容器管理`-> __Helm 应用__ 内找到 `skoala-init` 进行安装。

![image](https://docs.daocloud.io/daocloud-docs-images/docs/skoala/images/skoala-init.png)

## 在线升级

由于 `skoala-init` 组件安装在工作集群中，所以需要在每个工作集群中各执行一次下列操作。
<!--如果需要升级，会在release notes中强调-->

1. 备份原有参数

    ```bash
    helm get values skoala-init -n skoala-system -o yaml > skoala-init.yaml
    ```

2. 添加微服务引擎的 Helm 仓库

    ```bash
    helm repo add skoala https://release.daocloud.io/chartrepo/skoala
    ```

3. 添加微服务引擎的 Helm 仓库

    ```bash
    helm repo update
    ```

4. 删除 gateway-api 相关 job

    ```bash
    kubectl delete jobs gateway-api-admission gateway-api-admission-patch -n skoala-system
    ```

5. 执行 `helm upgrade` 命令

    ```bash
    helm upgrade --install --create-namespace -n skoala-system skoala-init skoala/skoala-init --version=0.28.1 --set nacos-operator.image.tag=v0.28.1 --set skoala-agent.image.tag=v0.28.1 --set sentinel-operator.image.tag=v0.28.1 --set seata-operator.image.tag=v0.28.1 -f skoala-init.yaml
    ```

    !!! note

        需要将 `version`、`nacos-operator.image.tag`、`skoala-agent.image.tag`、`sentinel-operator.image.tag`、`seata-operator.image.tag` 五个参数的值调整为您需要升级到的微服务引擎的版本号。

6. 根据自身需要，手动更新需要升级的网关相关 CRD 文件。

    ```bash
    # projectcontour 相关 crd
    kubectl apply -f skoala-init/charts/contour-provisioner/crds/contour.yaml
    # gateway-api 相关 crd
    kubectl apply -f skoala-init/charts/contour-provisioner-prereq/crds/gateway-api.yaml
    ```

## 离线升级

参考微服务引擎管理组件的[离线升级](./skoala.md#_11)方式

## 卸载微服务引擎集群初始化组件

!!! note

    - nacos sentinel seata 的 crd 会随之卸载，特别注意，相关 cr 会被删除。
    - 网关相关 crd 不会被随之卸载，如需清除需手动处理，特别注意，清除 crd 时相关 cr 会被删除。

??? note "网关相关 crd 清单"

    contourconfigurations.projectcontour.io  
    contourdeployments.projectcontour.io  
    extensionservices.projectcontour.io  
    gatewayclasses.gateway.networking.k8s.io  
    gateways.gateway.networking.k8s.io  
    grpcroutes.gateway.networking.k8s.io  
    httpproxies.projectcontour.io  
    httproutes.gateway.networking.k8s.io  
    referencegrants.gateway.networking.k8s.io  
    tcproutes.gateway.networking.k8s.io  
    tlscertificatedelegations.projectcontour.io  
    tlsroutes.gateway.networking.k8s.io  
    udproutes.gateway.networking.k8s.io

```bash
helm uninstall skoala-init -n skoala-system
```

### 手动清理 gateway-api 相关 job

```bash
kubectl delete jobs gateway-api-admission gateway-api-admission-patch -n skoala-system
```

### 手动清理网关相关 crd

```bash
kubectl delete crds `kubectl get crds | grep -E "projectcontour.io|gateway.networking.k8s.io" | awk '{print $1}'`
```
