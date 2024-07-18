# 全局服务集群重装后，原工作集群如何重新纳管至新环境

## 背景

某客户由于 Global 集群的架构调整，需要废弃现有环境并重新部署。考虑到在原环境中已部署了多套工作集群，客户希望在新环境中重新接管这些工作集群，从而对工作集群进行生命周期管理。

## 解决方案

### 备份资源

现有环境在废弃之前需要备份以下相关资源，以便在新环境中还原。

#### 备份 Kubean 相关资源

Kubean 是一个基于 Kubespray 构建的集群生命周期管理工具。

1. 获取命名空间 `kubean-system` 下的 `configmap` 资源，并对资源 `<cluster-name>-hosts-conf`、`<cluster-name>-kubeconf`、`<cluster-name>-vars-conf`、 `kubean-localservice` 备份，本示例资源为 `migrate-cluster-hosts-conf`、`migrate-cluster-kubeconf`、`migrate-cluster-vars-conf`、 `kubean-localservice`

    ```shell
    # 获取资源
    kubectl -n kubean-system get cm --no-headers  | awk '{print $1}'

    # 备份资源
    kubectl -n kubean-system get cm migrate-cluster-hosts-conf -o yaml >> hosts-conf.yaml
    kubectl -n kubean-system get cm mirateg-cluster-kubeconf -o yaml >> kubeconf.yaml
    kubectl -n kubean-system get cm migrate-cluster-vars-conf -o yaml >> vars-conf.yaml
    ```

2. 获取命名空间 `kubean-system` 下的 `secret` 资源，并对资源 `sh.helm.release.v1.kubean.v1`、`webhook-http-ca-secret` 备份，如果部署时虚拟机使用的是用户名/密码则无需执行

    ```shell
    # 获取资源
    kubectl -n kubean-system get secret --no-headers |awk '{print $1}'

    # 如果 clusterconfig.yaml 虚拟机使用的是用户名/密码无需备份
    ```

3. 备份 `cluster.kubean.io` 资源，该资源用于标识目前环境下的所有 K8s 集群

    ```shell
    # 获取资源
    $ kubectl get cluster.kubean.io --no-headers | awk '{print $1}'

    migrate-cluster
    my-cluster

    ```

    ```shell
    # 备份除 my-cluster 外其他的资源
    kubectl get cluster.kubean.io migrate-cluster -o yaml >> migrate-cluster.yaml
    ```

4. 备份 `localartifactsets.kubean.io` 资源，该资源用于记录当前环境离线包支持的组件及版本信息

    ```shell
    # 获取资源
    kubectl get localartifactsets.kubean.io --no-headers | awk '{print $1}'

    # 备份资源
    kubectl get localartifactsets.kubean.io <localartifactsets-name> -o yaml >> localartifactset.yaml
    ```

5. 备份 `manifests.kubean.io` 资源，该资源用于记录和维护当前版本的 Kubean 使用和兼容的组件、包及版本

    ```shell
    # 获取资源
    kubectl get manifests.kubean.io --no-headers | awk '{print $1}'

    # 备份资源
    kubectl get manifests.kubean.io <manifest-name> -o yaml >> manifest.yaml
    ```

#### 备份 Kpanda 组件相关资源

Kpanda 是容器管理模块的内部代码。

1. 备份 `clusters.cluster.kpanda.io`，只备份工作集群的信息，如下，只需要备份 `migrate-cluster` 信息

    ```shell
    [root@g-master1]# kubectl get clusters.cluster.kpanda.io
    NAME                    VERSION   MODE   PROVIDER             RUNNING   KUBESYSTEMID                           AGE
    kpanda-global-cluster   v1.27.5   Push   DAOCLOUD_KUBESPRAY   True      b4a1404d-04fd-4b48-bd87-c1494322bebb   50m
    migrate-cluster         v1.27.5   Push   DAOCLOUD_KUBESPRAY   True      7a45e8c4-b693-4c4c-a06b-19bd9052be64   44m

    [root@g-master1]# kubectl get clusters.cluster.kpanda.io migrate-cluster -o yaml >> kpanda-migrate-cluster.yaml
    ```

2. 备份命名空间 `kpanda-system` 下工作集群相关的 `secret`资源，命名规范为 `<集群名称>-secret`，本示例为 `migrate-cluster-secret`

    ```shell
    # 备份资源
    kubectl -n kpanda-system get secrets migrate-cluster-secret -o yaml >> kpanda-migrate-cluster-secret.yaml
    ```

3. 备份命名空间 `kpanda-system` 下工作集群相关的 `configmap`资源，命名规范为 `<集群名称>-setting`，本示例为 `migrate-cluster-setting`，该资源记录了当前集群 `集群运维->集群设置` 下的信息，如果无更新则不需要备份

    ```shell
    # 备份资源
    kubectl -n kpanda-system get cm migrate-cluster-setting -o yaml >> kpanda-migrate-cluster-setting.yaml
    ```

### 还原资源

在新环境中还原上一步备份的资源，从而使新环境可以对原有工作集群进行管理

#### 还原 Kubean 相关资源

1. 还原 `cluster.kubean.io` 资源

    ```shell
    # 创建资源
    kubectl apply -f  migrate-cluster.yaml
    ```

    ```shell
    # 查看创建成功的 cluster.kubean.io/migrate-cluster 资源信息，获取  uid 
    kubectl get cluster.kubean.io mig-cluster -o yaml |grep "uid: "
    ```

    本示例获取的 uid 为 `6b81413c-270e-4720-b215-fe7cf1364d45`

2. 还原 `localartifactsets.kubean.io` 资源

    ```shell
    # 创建资源
    kubectl apply -f localartifactset.yaml
    ```

3. 还原 `manifests.kubean.io` 资源

    ```shell
    # 创建资源
    kubectl apply -f manifest.yaml
    ```

4. 更新备份的 `hosts-conf.yaml`、`kubeconf.yaml`、`vars-conf.yaml`，在文件中的 `ownerReferences` 区域，更新成步骤一获取的 uid，如果备份了 `secret` 资源，也需要按照此步骤更新

    ```yaml
    ownerReferences:
    - apiVersion: kubean.io/v1alpha1
        blockOwnerDeletion: true
        controller: true
        kind: Cluster
        name: mig-cluster
        uid: 6b81413c-270e-4720-b215-fe7cf1364d45 ## 更新此位置，上述涉及到的 configmap 资源均需要更改
    resourceVersion: "15986"
    uid: 9075713e-79ca-436a-8765-db9d25e2667b
    ```

#### 还原 Kpanda 相关资源

1. 还原 `clusters.cluster.kpanda.io` 资源

    ```shell
    # 创建资源
    kubectl apply -f kpanda-migrate-cluster.yaml
    ```

    ```shell
    # 查看创建成功的 clusters.cluster.kpanda.io/migrate-cluster  资源信息，获取  uid 
    kubectl get clusters.cluster.kpanda.io mig-cluster -o yaml | grep "uid: "
    ```

    本示例获取的 uid 为 `6dc22267-ab04-430d-afd5-e332d509c7d3`

2. 根据上一步获取的 `clusters.cluster.kpanda.io` 资源 的 uid ，更新 `kpanda-migrate-cluster-secret.yaml` 中 ownerReferences 的 uid

    ```yaml
    ownerReferences:
    - apiVersion: cluster.kpanda.io/v1alpha1
        blockOwnerDeletion: true
        controller: true
        kind: Cluster
        name: mig-cluster
        uid: 6dc22267-ab04-430d-afd5-e332d509c7d3 ## 更新此位置
    resourceVersion: "1006873"
    uid: f726d1e3-c2aa-4341-88ad-ce9322d5d1ba
    type: Opaque
    ```

3. 如果有需要的话，根据上一步获取的 `clusters.cluster.kpanda.io` 资源 的 uid ，更新 `kpanda-migrate-cluster-setting.yaml` 中 ownerReferences 的 uid

## 验证

成功执行上述步骤后，可以在新环境对加入进来的工作集群做删除节点、增加节点操作。如果问题请联系道客官方进行支持！
