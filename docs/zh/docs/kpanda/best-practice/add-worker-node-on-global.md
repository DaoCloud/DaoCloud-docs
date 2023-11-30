# 为全局服务集群的工作节点扩容

本文将介绍离线模式下，如何手动为全局服务集群的工作节点进行扩容，默认情况下，不建议在平台部署后对全局服务集群进行扩容，请在平台部署前做好资源规划。

!!! note

    注意：全局服务集群的控制节点不支持扩容。

## 前提条件

- 已经通过[火种节点](../../install/commercial/deploy-arch.md)完成 DCE 平台的部署，并且火种节点上的 kind 集群运行正常。
- 必须使用平台 admin 权限的用户登录。

## 获取火种节点上 kind 集群的 kubeconfig

1. 执行如下命令登录火种节点：

    ```bash
    ssh root@火种节点 IP 地址
    ```

2. 在火种节点上执行如下命令获取 kind 集群的 `CONTAINER ID`：

    ```bash
    [root@localhost ~]# podman ps

    # 预期输出如下：
    CONTAINER ID  IMAGE                                      COMMAND     CREATED      STATUS      PORTS                                                                                                         NAMES
    220d662b1b6a  docker.m.daocloud.io/kindest/node:v1.26.2              2 weeks ago  Up 2 weeks  0.0.0.0:443->30443/tcp, 0.0.0.0:8081->30081/tcp, 0.0.0.0:9000-9001->32000-32001/tcp, 0.0.0.0:36674->6443/tcp  my-cluster-installer-control-plane
    ```

3. 执行如下命令，进入 kind 集群容器内：

    ```bash
    podman exec -it {CONTAINER ID} bash
    ```

    `{CONTAINER ID}` 替换为您真实的容器 ID

4. 在 kind 集群容器内执行如下命令获取 kind 集群的 kubeconfig 配置信息：

    ```bash
    kubectl config view --minify --flatten --raw
    ```

    `{CONTAINER ID}` 替换为您真实的容器 ID

待控制台输出后，复制 kind 集群的 kubeconfig 配置信息，为下一步做准备。

## 在火种节点上 kind 集群内创建 `cluster.kubean.io` 资源

1. 使用 `podman exec -it {CONTAINER ID} bash` 命令进入 kind 集群容器内。

2. 复制并执行如下命令，在 kind 集群内执行，以创建 `cluster.kubean.io` 资源：

    ```bash
    kubectl apply -f - <<EOF
    apiVersion: kubean.io/v1alpha1
    kind: Cluster
    metadata:
    labels:
        clusterName: kpanda-global-cluster
    name: kpanda-global-cluster
    spec:
    hostsConfRef:
        name: my-cluster-hosts-conf
        namespace: kubean-system
    kubeconfRef:
        name: my-cluster-kubeconf
        namespace: kubean-system
    varsConfRef:
        name: my-cluster-vars-conf
        namespace: kubean-system
    EOF
    ```

3. 在 kind 集群内执行如下命令，检验 cluster.kubean.io` 资源是否正常创建：

    ```bash
    root@my-cluster-installer-control-plane:/# kubectl get clusters
    ```

    预期输出如下：

    ```console
    NAME                    AGE
    kpanda-global-cluster   3s
    my-cluster              16d
    ```

## 更新火种节点上的 kind 集群里的 containerd 配置

1. 执行如下命令，登录全局服务集群的其中一个控制节点：

    ```bash
    ssh root@全局服务集群控制节点 IP 地址
    ```

2. 在全局服务集群控制节点上执行如下命令，将控制节点的 containerd 配置文件 `config.toml` 复制到火种节点上：

    ```bash
    scp /etc/containerd/config.toml root@{火种节点 IP}:/root
    ```

3. 在火种节点上执行如下命令，将 `config.toml` 配置文件复制到 kind 集群内：

    ```bash
    cd /root
    podman cp config.toml {CONTAINER ID}:/etc/containerd
    ```

    `{CONTAINER ID}` 替换为您真实的容器 ID

4. 在 kind 集群内执行如下命令，重启 containerd 服务

    ```bash
    systemctl restart containerd
    ```

## 将 kind 集群接入 DCE 集群列表

1. 登录 DCE 管理控制台，进入容器管理，在集群列表页右侧点击 `接入集群` 按钮，进入接入集群页面。

2. 在接入配置处，填入并编辑刚刚复制的 kind 集群的 kubeconfig 配置。需要配置参数如下：

    * `集群名称`：接入集群的名称，默认为 `my-cluster`。
    * `insecure-skip-tls-verify: true`：用以跳过 tls 验证，需要手动添加。
    * `server`：将默认的 `https://my-cluster-installer-control-plane:6443` 参数中的 IP 替换为火种节点的 IP；
       `6443` 替换为 6443 端口在节点映射的端口。可执行 `podman ps ｜ grep 6443` 命令查看。

    ![img](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/kpanda/images/add-global-node01.png)

3. 点击`确认`按钮，完成 kind 集群的接入。

## 为全局服务集群添加标签

1. 登录 DCE 管理控制台，进入容器管理，找到 `kapnda-glabal-cluster` 集群，在右侧操作列表找到`基础配置`操作按钮并进入基础配置界面。

2. 在基础配置页面，为全局服务集群添加的标签：`kpanda.io/managed-by=my-cluster`，如下图：

!!! note

    标签 “kpanda.io/managed-by=my-cluster” 中的 vaule 值为接入集群时指定的集群名称，默认为 "my-cluster"，具体依据您的实际情况。

    ![img](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/kpanda/images/add-global-node02.png)

## 为全局服务集群添加节点

1. 进入全局服务集群节点列表页，在节点列表右侧找到`接入节点`按钮并点击进入节点配置页面。

2. 填入待接入节点的 IP 和认证信息。

3. 在`自定义参数`处添加如下自定义参数：

    ```console
    download_run_once: false
    download_container: false
    download_force_cache: false
    download_localhost: false
    ```

    ![img](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/kpanda/images/add-global-node03.png)

4. 点击确认按钮，等待节点添加完成。
