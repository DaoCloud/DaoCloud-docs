# 创建网格时一直处于“创建中”

## 问题描述

mcpc-ckube-remote pod 一直 __ContainerCreating__ 。
mcpc-remote-kube-api-server configmap 等待很长时间没有创建。

![故障截图](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/troubleshoot/images/creating01.png)

### 日志

1. 查看 Pod 日志

    ```bash
    kubectl describe pod mspider-mcpc-ckube-remote-5447c5bcfc-25t7t -n istio-system
    ```

    ```none
    Events:
    Type     Reason       Age                  From               Message
    ----     ------       ----                 ----               -------
    Normal   Scheduled    18m                  default-scheduler  Successfully assigned istio-system/mspider-mcpc-ckube-remote-5447c5bcfc-25t7t to yl-cluster1
    Warning  FailedMount  6m59s                kubelet            Unable to attach or mount volumes: unmounted volumes=[remote-kube-api-server], unattached volumes=[remote-kube-api-server kube-api-access-ljncs ckube-config]: timed out waiting for the condition
    Warning  FailedMount  2m23s (x5 over 16m)  kubelet            Unable to attach or mount volumes: unmounted volumes=[remote-kube-api-server], unattached volumes=[ckube-config remote-kube-api-server kube-api-access-ljncs]: timed out waiting for the condition
    Warning  FailedMount  105s (x16 over 18m)  kubelet            MountVolume.SetUp failed for volume "remote-kube-api-server" : configmap "mspider-mcpc-remote-kube-api-server" not found
    Warning  FailedMount  5s (x2 over 13m)     kubelet            Unable to attach or mount volumes: unmounted volumes=[remote-kube-api-server], unattached volumes=[kube-api-access-ljncs ckube-config remote-kube-api-server]: timed out waiting for the condition
    ```

1. 查看 gsc controller 日志

    ??? note "点击查看详细日志"

        ```none
        time="2022-12-27T08:08:10Z" level=error msg="unable to get livez for cluster hosted-mesh-hosted: client rate limiter Wait returned an error: context deadline exceeded - error from a previous attempt: read tcp 192.188.110.245:51674->10.105.106.29:6443: read: connection reset by peer" func="mesh-cluster.(*Reconciler).checkAPIServerHealthy.func1()" file="mesh-cluster.go:191"
        time="2022-12-27T08:08:10Z" level=error msg="cluster hosted-mesh-hosted reconcile api-server-healthy error: client rate limiter Wait returned an error: context deadline exceeded - error from a previous attempt: read tcp 192.188.110.245:51674->10.105.106.29:6443: read: connection reset by peer" func="mesh-cluster.(*Reconciler).Reconcile()" file="mesh-cluster.go:1212"
        time="2022-12-27T08:08:13Z" level=error msg="unable to get livez for cluster hosted-mesh-hosted: client rate limiter Wait returned an error: context deadline exceeded - error from a previous attempt: read tcp 192.188.110.245:35842->10.105.106.29:6443: read: connection reset by peer" func="mesh-cluster.(*Reconciler).checkAPIServerHealthy.func1()" file="mesh-cluster.go:191"
        time="2022-12-27T08:08:13Z" level=error msg="cluster hosted-mesh-hosted reconcile api-server-healthy error: client rate limiter Wait returned an error: context deadline exceeded - error from a previous attempt: read tcp 192.188.110.245:35842->10.105.106.29:6443: read: connection reset by peer" func="mesh-cluster.(*Reconciler).Reconcile()" file="mesh-cluster.go:1212"
        time="2022-12-27T08:08:16Z" level=error msg="unable to get livez for cluster hosted-mesh-hosted: client rate limiter Wait returned an error: context deadline exceeded - error from a previous attempt: read tcp 192.188.110.245:35874->10.105.106.29:6443: read: connection reset by peer" func="mesh-cluster.(*Reconciler).checkAPIServerHealthy.func1()" file="mesh-cluster.go:191"
        time="2022-12-27T08:08:16Z" level=error msg="cluster hosted-mesh-hosted reconcile api-server-healthy error: client rate limiter Wait returned an error: context deadline exceeded - error from a previous attempt: read tcp 192.188.110.245:35874->10.105.106.29:6443: read: connection reset by peer" func="mesh-cluster.(*Reconciler).Reconcile()" file="mesh-cluster.go:1212"
        time="2022-12-27T08:08:19Z" level=error msg="unable to get livez for cluster hosted-mesh-hosted: client rate limiter Wait returned an error: context deadline exceeded - error from a previous attempt: read tcp 192.188.110.245:35902->10.105.106.29:6443: read: connection reset by peer" func="mesh-cluster.(*Reconciler).checkAPIServerHealthy.func1()" file="mesh-cluster.go:191"
        time="2022-12-27T08:08:19Z" level=error msg="cluster hosted-mesh-hosted reconcile api-server-healthy error: client rate limiter Wait returned an error: context deadline exceeded - error from a previous attempt: read tcp 192.188.110.245:35902->10.105.106.29:6443: read: connection reset by peer" func="mesh-cluster.(*Reconciler).Reconcile()" file="mesh-cluster.go:1212"
        time="2022-12-27T08:08:22Z" level=error msg="unable to get livez for cluster hosted-mesh-hosted: client rate limiter Wait returned an error: context deadline exceeded - error from a previous attempt: read tcp 192.188.110.245:35940->10.105.106.29:6443: read: connection reset by peer" func="mesh-cluster.(*Reconciler).checkAPIServerHealthy.func1()" file="mesh-cluster.go:191"
        time="2022-12-27T08:08:22Z" level=error msg="cluster hosted-mesh-hosted reconcile api-server-healthy error: client rate limiter Wait returned an error: context deadline exceeded - error from a previous attempt: read tcp 192.188.110.245:35940->10.105.106.29:6443: read: connection reset by peer" func="mesh-cluster.(*Reconciler).Reconcile()" file="mesh-cluster.go:1212"
        time="2022-12-27T08:08:23Z" level=error msg="cluster cluster1-141 reconcile component-status error: deployment: istio-system/mspider-mcpc-mcpc-controller, error: {type: Available, reason: Deployment does not have minimum availability.;type: Progressing, reason: ReplicaSet \"mspider-mcpc-mcpc-controller-d7b76b945\" has timed out progressing.};deployment: istio-system/mspider-mcpc-ckube-remote, error: {type: Available, reason: Deployment does not have minimum availability.;type: Progressing, reason: ReplicaSet \"mspider-mcpc-ckube-remote-5447c5bcfc\" has timed out progressing.}" func="mesh-cluster.(*Reconciler).Reconcile()" file="mesh-cluster.go:1212"
        time="2022-12-27T08:08:23Z" level=info msg="get mesh hosted-mesh's address: 0.0.0.0:30527" func="hosted-apiserver-proxy.(*proxyServer).GetMeshPort()" file="proxy.go:87"
        time="2022-12-27T08:08:23Z" level=error msg="cluster cluster1-141 reconcile component-status error: deployment: istio-system/mspider-mcpc-mcpc-controller, error: {type: Available, reason: Deployment does not have minimum availability.;type: Progressing, reason: ReplicaSet \"mspider-mcpc-mcpc-controller-d7b76b945\" has timed out progressing.};deployment: istio-system/mspider-mcpc-ckube-remote, error: {type: Available, reason: Deployment does not have minimum availability.;type: Progressing, reason: ReplicaSet \"mspider-mcpc-ckube-remote-5447c5bcfc\" has timed out progressing.}" func="mesh-cluster.(*Reconciler).Reconcile()" file="mesh-cluster.go:1212"
        time="2022-12-27T08:08:25Z" level=error msg="unable to get livez for cluster hosted-mesh-hosted: client rate limiter Wait returned an error: context deadline exceeded - error from a previous attempt: read tcp 192.188.110.245:52050->10.105.106.29:6443: read: connection reset by peer" func="mesh-cluster.(*Reconciler).checkAPIServerHealthy.func1()" file="mesh-cluster.go:191"
        time="2022-12-27T08:08:25Z" level=error msg="cluster hosted-mesh-hosted reconcile api-server-healthy error: client rate limiter Wait returned an error: context deadline exceeded - error from a previous attempt: read tcp 192.188.110.245:52050->10.105.106.29:6443: read: connection reset by peer" func="mesh-cluster.(*Reconciler).Reconcile()" file="mesh-cluster.go:1212"
        1.672128505418613e+09   ERROR   Reconciler error        {"controller": "meshcluster", "controllerGroup": "discovery.mspider.io", "controllerKind": "MeshCluster", "MeshCluster": {"name":"hosted-mesh-hosted","namespace":"mspider-system"}, "namespace": "mspider-system", "name": "hosted-mesh-hosted", "reconcileID": "e3583462-c271-4e58-ae00-18ba923362b8", "error": "Operation cannot be fulfilled on meshclusters.discovery.mspider.io \"hosted-mesh-hosted\": the object has been modified; please apply your changes to the latest version and try again"}
        sigs.k8s.io/controller-runtime/pkg/internal/controller.(*Controller).reconcileHandler
                /go/pkg/mod/sigs.k8s.io/controller-runtime@v0.13.0/pkg/internal/controller/controller.go:326
        sigs.k8s.io/controller-runtime/pkg/internal/controller.(*Controller).processNextWorkItem
                /go/pkg/mod/sigs.k8s.io/controller-runtime@v0.13.0/pkg/internal/controller/controller.go:273
        sigs.k8s.io/controller-runtime/pkg/internal/controller.(*Controller).Start.func2.2
                /go/pkg/mod/sigs.k8s.io/controller-runtime@v0.13.0/pkg/internal/controller/controller.go:234
        time="2022-12-27T08:08:25Z" level=error msg="update cluster status error: Operation cannot be fulfilled on meshclusters.discovery.mspider.io \"hosted-mesh-hosted\": the object has been modified; please apply your changes to the latest version and try again" func="mesh-cluster.(*Reconciler).Reconcile()" file="mesh-cluster.go:1241"
        time="2022-12-27T08:08:28Z" level=error msg="unable to get livez for cluster hosted-mesh-hosted: client rate limiter Wait returned an error: context deadline exceeded - error from a previous attempt: EOF" func="mesh-cluster.(*Reconciler).checkAPIServerHealthy.func1()" file="mesh-cluster.go:191"
        time="2022-12-27T08:08:28Z" level=error msg="cluster hosted-mesh-hosted reconcile api-server-healthy error: client rate limiter Wait returned an error: context deadline exceeded - error from a previous attempt: EOF" func="mesh-cluster.(*Reconciler).Reconcile()" file="mesh-cluster.go:1212"
        time="2022-12-27T08:08:31Z" level=error msg="unable to get livez for cluster hosted-mesh-hosted: client rate limiter Wait returned an error: context deadline exceeded - error from a previous attempt: read tcp 192.188.110.245:52104->10.105.106.29:6443: read: connection reset by peer" func="mesh-cluster.(*Reconciler).checkAPIServerHealthy.func1()" file="mesh-cluster.go:191"
        time="2022-12-27T08:08:31Z" level=error msg="cluster hosted-mesh-hosted reconcile api-server-healthy error: client rate limiter Wait returned an error: context deadline exceeded - error from a previous attempt: read tcp 192.188.110.245:52104->10.105.106.29:6443: read: connection reset by peer" func="mesh-cluster.(*Reconciler).Reconcile()" file="mesh-cluster.go:1212"
        1.6721285114885132e+09  ERROR   Reconciler error        {"controller": "meshcluster", "controllerGroup": "discovery.mspider.io", "controllerKind": "MeshCluster", "MeshCluster": {"name":"hosted-mesh-hosted","namespace":"mspider-system"}, "namespace": "mspider-system", "name": "hosted-mesh-hosted", "reconcileID": "b3abe28d-8ec4-4a69-8ecb-1e69e2f8c12d", "error": "Operation cannot be fulfilled on meshclusters.discovery.mspider.io \"hosted-mesh-hosted\": the object has been modified; please apply your changes to the latest version and try again"}
        sigs.k8s.io/controller-runtime/pkg/internal/controller.(*Controller).reconcileHandler
                /go/pkg/mod/sigs.k8s.io/controller-runtime@v0.13.0/pkg/internal/controller/controller.go:326
        sigs.k8s.io/controller-runtime/pkg/internal/controller.(*Controller).processNextWorkItem
                /go/pkg/mod/sigs.k8s.io/controller-runtime@v0.13.0/pkg/internal/controller/controller.go:273
        sigs.k8s.io/controller-runtime/pkg/internal/controller.(*Controller).Start.func2.2
        time="2022-12-27T08:08:31Z" level=error msg="update cluster status error: Operation cannot be fulfilled on meshclusters.discovery.mspider.io \"hosted-mesh-hosted\": the object has been modified; please apply your changes to the latest version and try again" func="mesh-cluster.(*Reconciler).Reconcile()" file="mesh-cluster.go:1241"
                /go/pkg/mod/sigs.k8s.io/controller-runtime@v0.13.0/pkg/internal/controller/controller.go:234
        time="2022-12-27T08:08:34Z" level=error msg="unable to get livez for cluster hosted-mesh-hosted: client rate limiter Wait returned an error: context deadline exceeded - error from a previous attempt: read tcp 192.188.110.245:49646->10.105.106.29:6443: read: connection reset by peer" func="mesh-cluster.(*Reconciler).checkAPIServerHealthy.func1()" file="mesh-cluster.go:191"
        time="2022-12-27T08:08:34Z" level=error msg="cluster hosted-mesh-hosted reconcile api-server-healthy error: client rate limiter Wait returned an error: context deadline exceeded - error from a previous attempt: read tcp 192.188.110.245:49646->10.105.106.29:6443: read: connection reset by peer" func="mesh-cluster.(*Reconciler).Reconcile()" file="mesh-cluster.go:1212"
        time="2022-12-27T08:08:37Z" level=error msg="unable to get livez for cluster hosted-mesh-hosted: client rate limiter Wait returned an error: context deadline exceeded - error from a previous attempt: read tcp 192.188.110.245:49656->10.105.106.29:6443: read: connection reset by peer" func="mesh-cluster.(*Reconciler).checkAPIServerHealthy.func1()" file="mesh-cluster.go:191"
        time="2022-12-27T08:08:37Z" level=error msg="cluster hosted-mesh-hosted reconcile api-server-healthy error: client rate limiter Wait returned an error: context deadline exceeded - error from a previous attempt: read tcp 192.188.110.245:49656->10.105.106.29:6443: read: connection reset by peer" func="mesh-cluster.(*Reconciler).Reconcile()" file="mesh-cluster.go:1212"
        time="2022-12-27T08:08:37Z" level=error msg="update cluster status error: Operation cannot be fulfilled on meshclusters.discovery.mspider.io \"hosted-mesh-hosted\": the object has been modified; please apply your changes to the latest version and try again" func="mesh-cluster.(*Reconciler).Reconcile()" file="mesh-cluster.go:1241"
        1.6721285175748258e+09  ERROR   Reconciler error        {"controller": "meshcluster", "controllerGroup": "discovery.mspider.io", "controllerKind": "MeshCluster", "MeshCluster": {"name":"hosted-mesh-hosted","namespace":"mspider-system"}, "namespace": "mspider-system", "name": "hosted-mesh-hosted", "reconcileID": "4cc3c5be-dbe1-4bdc-a606-70ff2b7bc3f2", "error": "Operation cannot be fulfilled on meshclusters.discovery.mspider.io \"hosted-mesh-hosted\": the object has been modified; please apply your changes to the latest version and try again"}
        sigs.k8s.io/controller-runtime/pkg/internal/controller.(*Controller).reconcileHandler
                /go/pkg/mod/sigs.k8s.io/controller-runtime@v0.13.0/pkg/internal/controller/controller.go:326
        sigs.k8s.io/controller-runtime/pkg/internal/controller.(*Controller).processNextWorkItem
                /go/pkg/mod/sigs.k8s.io/controller-runtime@v0.13.0/pkg/internal/controller/controller.go:273
        sigs.k8s.io/controller-runtime/pkg/internal/controller.(*Controller).Start.func2.2
                /go/pkg/mod/sigs.k8s.io/controller-runtime@v0.13.0/pkg/internal/controller/controller.go:234
        time="2022-12-27T08:08:39Z" level=error msg="mesh hosted-mesh reconcile remote-config error: create mesh hosted-mesh hosted ns error: an error on the server (\"unknown\") has prevented the request from succeeding (post namespaces)" func="global-mesh.(*Reconciler).Reconcile()" file="global-mesh.go:1198"
        time="2022-12-27T08:08:40Z" level=error msg="unable to get livez for cluster hosted-mesh-hosted: client rate limiter Wait returned an error: context deadline exceeded - error from a previous attempt: read tcp 192.188.110.245:49676->10.105.106.29:6443: read: connection reset by peer" func="mesh-cluster.(*Reconciler).checkAPIServerHealthy.func1()" file="mesh-cluster.go:191"
        time="2022-12-27T08:08:40Z" level=error msg="cluster hosted-mesh-hosted reconcile api-server-healthy error: client rate limiter Wait returned an error: context deadline exceeded - error from a previous attempt: read tcp 192.188.110.245:49676->10.105.106.29:6443: read: connection reset by peer" func="mesh-cluster.(*Reconciler).Reconcile()" file="mesh-cluster.go:1212"
        time="2022-12-27T08:08:40Z" level=error msg="update cluster status error: Operation cannot be fulfilled on meshclusters.discovery.mspider.io \"hosted-mesh-hosted\": the object has been modified; please apply your changes to the latest version and try again" func="mesh-cluster.(*Reconciler).Reconcile()" file="mesh-cluster.go:1241"
        1.6721285206091342e+09  ERROR   Reconciler error        {"controller": "meshcluster", "controllerGroup": "discovery.mspider.io", "controllerKind": "MeshCluster", "MeshCluster": {"name":"hosted-mesh-hosted","namespace":"mspider-system"}, "namespace": "mspider-system", "name": "hosted-mesh-hosted", "reconcileID": "31adec56-ca5b-4636-a74e-3ce4ae8b07af", "error": "Operation cannot be fulfilled on meshclusters.discovery.mspider.io \"hosted-mesh-hosted\": the object has been modified; please apply your changes to the latest version and try again"}
        sigs.k8s.io/controller-runtime/pkg/internal/controller.(*Controller).reconcileHandler
                /go/pkg/mod/sigs.k8s.io/controller-runtime@v0.13.0/pkg/internal/controller/controller.go:326
        sigs.k8s.io/controller-runtime/pkg/internal/controller.(*Controller).processNextWorkItem
                /go/pkg/mod/sigs.k8s.io/controller-runtime@v0.13.0/pkg/internal/controller/controller.go:273
        sigs.k8s.io/controller-runtime/pkg/internal/controller.(*Controller).Start.func2.2
                /go/pkg/mod/sigs.k8s.io/controller-runtime@v0.13.0/pkg/internal/controller/controller.go:234
        time="2022-12-27T08:08:43Z" level=error msg="unable to get livez for cluster hosted-mesh-hosted: client rate limiter Wait returned an error: context deadline exceeded - error from a previous attempt: read tcp 192.188.110.245:47316->10.105.106.29:6443: read: connection reset by peer" func="mesh-cluster.(*Reconciler).checkAPIServerHealthy.func1()" file="mesh-cluster.go:191"
        time="2022-12-27T08:08:43Z" level=error msg="cluster hosted-mesh-hosted reconcile api-server-healthy error: client rate limiter Wait returned an error: context deadline exceeded - error from a previous attempt: read tcp 192.188.110.245:47316->10.105.106.29:6443: read: connection reset by peer" func="mesh-cluster.(*Reconciler).Reconcile()" file="mesh-cluster.go:1212"
        time="2022-12-27T08:08:43Z" level=error msg="update cluster status error: Operation cannot be fulfilled on meshclusters.discovery.mspider.io \"hosted-mesh-hosted\": the object has been modified; please apply your changes to the latest version and try again" func="mesh-cluster.(*Reconciler).Reconcile()" file="mesh-cluster.go:1241"
        1.6721285236628819e+09  ERROR   Reconciler error        {"controller": "meshcluster", "controllerGroup": "discovery.mspider.io", "controllerKind": "MeshCluster", "MeshCluster": {"name":"hosted-mesh-hosted","namespace":"mspider-system"}, "namespace": "mspider-system", "name": "hosted-mesh-hosted", "reconcileID": "908883a2-78a3-48f0-8a91-4f963903ae19", "error": "Operation cannot be fulfilled on meshclusters.discovery.mspider.io \"hosted-mesh-hosted\": the object has been modified; please apply your changes to the latest version and try again"}
        sigs.k8s.io/controller-runtime/pkg/internal/controller.(*Controller).reconcileHandler
                /go/pkg/mod/sigs.k8s.io/controller-runtime@v0.13.0/pkg/internal/controller/controller.go:326
        sigs.k8s.io/controller-runtime/pkg/internal/controller.(*Controller).processNextWorkItem
                /go/pkg/mod/sigs.k8s.io/controller-runtime@v0.13.0/pkg/internal/controller/controller.go:273
        sigs.k8s.io/controller-runtime/pkg/internal/controller.(*Controller).Start.func2.2
                /go/pkg/mod/sigs.k8s.io/controller-runtime@v0.13.0/pkg/internal/controller/controller.go:234
        ```

## 原因分析

1. 情况 1：托管网格由于控制面集群没有提前部署 __StorageClass__ 导致无法创建高可用 ETCD。

    xxxxx-etcd-0 一直 pending，etcd pvc 无法绑定 sc 导致 pvc pending，
    进而导致 etcd pod 无法绑定 pvc。可以尝试以下步骤解决问题：

    1. 部署 hwameistor 或者 localPath 
    2. 删除 istio-system 命名空间下 pending 的 pvc
    3. 重启一下 xxx-etcd-0 pod，等待即可

    !!! note
    
        使用 hwameistor 完成部署后，每个节点必须存在一个空盘。您需要创建 LDC，然后检查 LSN LocalStorage_PoolHDD。

2. 情况 2：托管网格 istiod-xxxx-hosted-xxxx 组件异常

3. 情况 3：mspider-mcpc-ckube-remote-xxxx 组件异常，describe 出现如下报错：

    ```none
     Normal   Scheduled    18m                  default-scheduler  Successfully assigned istio-system/mspider-mcpc-ckube-remote-5447c5bcfc-25t7t to yl-cluster20
     Warning  FailedMount  6m59s                kubelet            Unable to attach or mount volumes: unmounted volumes=[remote-kube-api-server], unattached volumes=[remote-kube-api-server kube-api-access-ljncs ckube-config]: timed out waiting for the condition
     Warning  FailedMount  2m23s (x5 over 16m)  kubelet            Unable to attach or mount volumes: unmounted volumes=[remote-kube-api-server], unattached volumes=[ckube-config remote-kube-api-server kube-api-access-ljncs]: timed out waiting for the condition
     Warning  FailedMount  105s (x16 over 18m)  kubelet            MountVolume.SetUp failed for volume "remote-kube-api-server" : configmap "mspider-mcpc-remote-kube-api-server" not found
     Warning  FailedMount  5s (x2 over 13m)     kubelet            Unable to attach or mount volumes: unmounted volumes=[remote-kube-api-server], unattached volumes=[kube-api-access-ljncs ckube-config remote-kube-api-server]: timed out waiting for the condition
    ```

4. 情况 4：inotify watcher limit problems, remote-ckube 组件日志

    ```none
    panic: too many open files
    ```

## 解决方案

1. 情况 1：控制面集群提前部署 sc。

2. 情况 2：该组件异常可能控制面集群未部署 metalLB 导致网络不通，
   istiod-xxxx-hosed-lb 无法分配 endpoint。可在 addon 中为该集群部署 metalLB。

3. 情况 3：在移除原有托管网格后的环境中，再次创建托管网格的情况下，容易出现控制面还没有及时下发导致
   "mspider-mcpc-remote-kube-api-server" ConfigMap 未及时创建。可以重启一下 global 集群 gsc controller：

    ```bash
    kubectl -n mspider-system delete pod $(kubectl -n mspider-system get pod -l app=mspider-gsc-controller -o 'jsonpath={.items.metadata.name}')
    ```

4. 情况 4：修改 fs.inotify.max_user_instances = 65535
