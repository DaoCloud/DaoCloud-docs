# 为全局服务集群的工作节点扩容

本文将介绍离线模式下，如何手动为全局服务集群的工作节点进行扩容。
默认情况下，不建议在部署 DCE 5.0 后对[全局服务集群](../user-guide/clusters/cluster-role.md#_2)进行扩容，请在部署 DCE 5.0 前做好资源规划。

!!! note

    全局服务集群的控制节点不支持扩容。

## 前提条件

- 已经通过[火种节点](../../install/commercial/deploy-arch.md)完成 DCE 5.0 平台的部署，并且火种节点上的 kind 集群运行正常。
- 必须使用平台 Admin 权限的用户登录。

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

待控制台输出后，复制 kind 集群的 kubeconfig 配置信息，为下一步做准备。

## 在火种节点上 kind 集群内创建 `cluster.kubean.io` 资源

1. 使用 `podman exec -it {CONTAINER ID} bash` 命令进入 kind 集群容器内。

1. 在 kind 集群容器内，执行如下命令，获取 **kind 集群名称** ：

    ```bash
    kubectl get clusters
    ```

1. 复制并执行如下命令，在 kind 集群内执行，以创建 `cluster.kubean.io` 资源：

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

    !!! note

        `spec.hostsConfRef.name`、`spec.kubeconfRef.name`、`spec.varsConfRef.name` 中集群名称默认为 `my-cluster`，
        需替换成上一步骤中获取的 **kind 集群名称** 。

1. 在 kind 集群内执行如下命令，检验 cluster.kubean.io` 资源是否正常创建：

    ```bash
    kubectl get clusters
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

2. 在全局服务集群控制节点上执行如下命令，将控制节点的 containerd 配置文件 __config.toml__ 复制到火种节点上：

    ```bash
    scp /etc/containerd/config.toml root@{火种节点 IP}:/root
    ```

3. 在火种节点上，从控制节点拷贝过来的 containerd 配置文件 __config.toml__ 中选取 **非安全镜像 registry 的部分** 加入到 **kind 集群内 config.toml**

    非安全镜像registry 部分示例如下：

    ```toml
    [plugins."io.containerd.grpc.v1.cri".registry]
      [plugins."io.containerd.grpc.v1.cri".registry.mirrors]
        [plugins."io.containerd.grpc.v1.cri".registry.mirrors."10.6.202.20"]
          endpoint = ["https://10.6.202.20"]
        [plugins."io.containerd.grpc.v1.cri".registry.configs."10.6.202.20".tls]
          insecure_skip_verify = true
    ```

    !!! note

        由于 kind 集群内不能直接修改 config.toml 文件，故可以先复制一份文件出来修改，再拷贝到 kind 集群，步骤如下：

        1. 在火种节点上执行以下命令，将文件拷贝出来

            ```bash
            podman cp {CONTAINER ID}:/etc/containerd/config.toml ./config.toml.kind
            ```

        1. 执行如下命令编辑 config.toml 文件

            ```bash
            vim ./config.toml.kind
            ```

        1. 将修改好的文件再复制到 kind 集群，执行如下命令

            ```bash
            podman cp ./config.toml.kind {CONTAINER ID}:/etc/containerd/config.toml
            ```

            **{CONTAINER ID}** 替换为您真实的容器 ID

    <!-- ![img](../images/) -->

1. 在 kind 集群内执行如下命令，重启 containerd 服务

    ```bash
    systemctl restart containerd
    ```

## 将 kind 集群接入 DCE 5.0 集群列表

1. 登录 DCE 5.0，进入容器管理，在集群列表页右侧点击 __接入集群__ 按钮，进入接入集群页面。

2. 在接入配置处，填入并编辑刚刚复制的 kind 集群的 kubeconfig 配置。

    ```yaml
    apiVersion: v1
    clusters:
    - cluster:
        insecure-skip-tls-verify: true # (1)!
        certificate-authority-data: LS0TLSCFDFWEFEWFEWFGGEWGFWFEWGWEGFEWGEWGSDGFSDSD
        server: https://my-cluster-installer-control-plane:6443 # (2)!
    name: my-cluster-installer
    contexts:
    - context:
        cluster: my-cluster-installer
        user: kubernetes-admin
    name: kubernetes-admin@my-cluster-installer
    current-context: kubernetes-admin@my-cluster-installer
    kind: Config
    preferences: {}
    users:
    ```

    1. 跳过 tls 验证，这一行需要手动添加
    2. 替换为火种节点的 IP，端口 6443 替换为在节点映射的端口（你可以执行 podman ps|grep 6443 命令查看映射的端口）

    ![kubeconfig](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/kpanda/images/add-global-node01.png)

3. 点击 __确认__ 按钮，完成 kind 集群的接入。

## 为全局服务集群添加标签

1. 登录 DCE 5.0，进入容器管理，找到 __kapnda-glabal-cluster__ 集群，在右侧操作列表找到 __基础配置__ 菜单项并进入基础配置界面。

2. 在基础配置页面，为全局服务集群添加的标签 `kpanda.io/managed-by=my-cluster`：

!!! note

    标签 `kpanda.io/managed-by=my-cluster` 中的 vaule 值为接入集群时指定的集群名称，默认为 `my-cluster`，具体依据您的实际情况。

    ![标签](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/kpanda/images/add-global-node02.png)

## 为全局服务集群添加节点

1. 进入全局服务集群节点列表页，点击右侧的 __接入节点__ 按钮。

2. 填入待接入节点的 IP 和认证信息后点击 __开始检查__ ，通过节点检查后点击 __下一步__ 。

3. 在 __自定义参数__ 处添加如下自定义参数：

    ```console
    download_run_once: false
    download_container: false
    download_force_cache: false
    download_localhost: false
    ```

    ![img](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/kpanda/images/add-global-node03.png)

4. 点击 __确定__ 等待节点添加完成。
