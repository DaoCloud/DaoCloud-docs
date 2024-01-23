# 应用跨集群通信

## 介绍

随着微服务进程发展，为了满足应用隔离、高可用/容灾以及运维管理的需求，许多企业选择部署多个 Kubernetes（K8s）集群。然而，这种多集群部署带来了一个问题：一些应用依赖于其他 K8s 集群中的微服务，需要实现集群间的通信。具体而言，需要从一个集群的 Pod 去访问另外一个集群的 Pod 或者 Service。

## 前提条件

请确认操作系统 Kernel 版本号 >= 4.9.17，推荐 5.10+。查看并安装升级最新的 Linux 内核版本，您可以按照如下命令进行操作：

1. 查看当前内核版本：

    ```bash
    uname -r
    ```

2. 安装 ELRepo 存储库，ELRepo 存储库中提供的最新 Linux 内核版本：

    ```bash
    rpm --import https://www.elrepo.org/RPM-GPG-KEY-elrepo.org
    rpm -Uvh https://www.elrepo.org/elrepo-release-7.el7.elrepo.noarch.rpm
    ```

3. 安装最新的 Linux 内核版本：

    ```bash
    yum --enablerepo=elrepo-kernel install kernel-ml
    ```

    > `kernel-ml` 是最新文档版内核，您可以根据需要选择其他版本。

4. 更新 GRUB 配置，以便在启动时使用新内核版本：

    ```bash
    grub2-mkconfig -o /boot/grub2/grub.cfg
    ```

## 创建集群

> 关于创建集群的更多信息，可参考[创建集群](../../../kpanda/user-guide/clusters/create-cluster.md)

1. 创建两个名称不同的集群分别为 cluster01 和 cluster02。

    ![创建集群1](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/network/images/network-cross-cluster1.png)

    - 集群 cluster01 的网络插件选择 cilium
    - 添加两个参数 `cluster-id`和 `cluster-name`
    - 其他均使用默认配置项

2. 以同样的步骤创建集群 cluster02。

    ![创建集群2](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/network/images/network-cross-cluster2.png)

    > 两个集群使用的容器网段和服务网段一定不能冲突。两个参数的值不能冲突，便于标识集群确保唯一性，避免跨集群通信时出现冲突。

## 为 API Server 创建 Service

1. 集群创建成功后，在两个集群上分别创建一个 Service，用于将该集群的 API server 对外暴露。

    ![创建service](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/network/images/network-cross-cluster3.png)

    ![创建service](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/network/images/network-cross-cluster4.png)

    - 集群 cluster01 访问类型选择 NodePort， 便于外部访问
    - 命名空间选择 `kube-system`，即 API Server 所在命名空间
    - 标签选择器筛选 API Server 组件，可返回查看 API Server 的选择器
    - 配置 Service 的访问端口，容器端口为 6443
    - 获取该 Service 的外部访问链接

2. 再以同样方式在集群 cluster02 上为 API Server 创建 Service。

    ![创建service](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/network/images/network-cross-cluster5.png)

    ![创建service](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/network/images/network-cross-cluster6.png)

## 修改集群配置

通过 `vi` 命令开始编辑 集群 cluster01 和集群  cluster02 的  `kubeconfig` 文件:

    ```bash
    vi $HOME/.kube/config
    ```

1. 在两个集群 cluster01 和 cluster02 里分别添加新的 `cluster`、`context`、`user` 信息。

    - 在`clusters`下面添加新的`cluster`信息：两个集群原有的 CA 颁发机构不变；新的 `server`  地址改为上述创建的 API Server Service 地址；`name` 改为两个集群本身的名称：cluster01 和 cluster02。

        > API Server Service 的地址可以从 DCE5.0 的页面查看或复制，需要使用 https 协议。

    - 在 `contexts` 下面添加新的 `context` 信息：将 `context` 中集群的 `name` 、`user`、`cluster` 三个字段的值均修改为两个集群本身的名称：cluster01 和 cluster02 。

    - 在 `users` 下面添加新的 `user` 信息：两个集群 cluster01 和 cluster02 分别复制本身原有的证书信息，将 name 改为两个集群本身的名称：cluster01 和 cluster02。

2. 在对端集群中分别互相添加已经创建好的 `cluster` 、`context`、`user` 信息。

    如下为操作过程中的 yaml 示例：

    ```yaml
    clusters:
    - cluster: #添加本集群 cluster01 `cluster`信息
        certificate-authority-data: {{cluster01}}
        server: https://{{https://10.6.124.66:31936}}
      name: {{cluster01 }}
    - cluster: #添加对端集群 cluster02`cluster`信息
        certificate-authority-data: {{cluster02}}
        server: https://{{https://10.6.124.67:31466}}
      name: {{cluster02}}
    ```

    ```yaml
    contexts:
    - context: #添加本集群 cluster01 `context` 信息
        cluster: {{cluster01 name}}
        user: {{cluster01 name}}
      name: {{cluster01 name}}
    - context: #添加对端集群 cluster02 `context`信息
        cluster: {{cluster02 name}}
        user: {{cluster02 name}}
      name: {{cluster02 name}}
    current-context: kubernetes-admin@cluster.local
    ```

    ```yaml
    users:
    - name: {{cluster01}} #添加本集群 cluster01 `user`信息
      user:
        client-certificate-data: {{cluster01 certificate-data}}
        client-key-data: {{cluster01 key-data}}
    - name: {{cluster02}} #添加对端集群 cluster02 `user`信息
      user:
        client-certificate-data: {{cluster02 certificate-data}}
        client-key-data: {{cluster02 key-data}}
    ```

## 配置集群连通性

执行如下命令验证集群的连通性：

1. 在集群 cluster01 上输入：

    ```bash
    cilium clustermesh enable --create-ca --context cluster01 --service-type NodePort
    ```

2. 集群 cluster02 开启 `clustermesh` 执行如下命令：

    ```bash
    cilium clustermesh enable --create-ca --context cluster02 --service-type NodePort
    ```

3. 在集群 cluster01 上建立连接：

    ```bash
    cilium clustermesh connect --context cluster01 --destination-context cluster02
    ```

4. 集群 cluster01 出现 `connected cluster1 and cluster2!` ，集群 cluster02 出现 `ClusterMesh enabled!` 说明两个集群通了。

    ![连通](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/network/images/network-cross-cluster7.png)

    ![连通](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/network/images/network-cross-cluster8.png)

## 创建演示应用

1. 使用 cilium 官方文档中提供的 [rebel-base](https://github.com/cilium/cilium/blob/main/examples/kubernetes/clustermesh/global-service-example/cluster1.yaml) 应用，复制如下 yaml 文件：

    ```yaml
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: rebel-base
    spec:
      selector:
        matchLabels:
          name: rebel-base
      replicas: 2
      template:
        metadata:
          labels:
            name: rebel-base
        spec:
          containers:
          - name: rebel-base
            image: docker.io/nginx:1.15.8
            volumeMounts:
              - name: html
                mountPath: /usr/share/nginx/html/
            livenessProbe:
              httpGet:
                path: /
                port: 80
              periodSeconds: 1
            readinessProbe:
              httpGet:
                path: /
                port: 80
          volumes:
            - name: html
              configMap:
                name: rebel-base-response
                items:
                  - key: message
                    path: index.html
    ---
    apiVersion: v1
    kind: ConfigMap
    metadata:
      name: rebel-base-response
    data:
      message: "{\"Galaxy\": \"Alderaan\", \"Cluster\": \"Cluster-1\"}\n" #将 Cluster-1 修改为集群一的名称
    ---
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: x-wing
    spec:
      selector:
        matchLabels:
          name: x-wing
      replicas: 2
      template:
        metadata:
          labels:
            name: x-wing
        spec:
          containers:
          - name: x-wing-container
            image: quay.io/cilium/json-mock:v1.3.3@sha256:f26044a2b8085fcaa8146b6b8bb73556134d7ec3d5782c6a04a058c945924ca0
            livenessProbe:
              exec:
                command:
                - curl
                - -sS
                - -o
                - /dev/null
                - localhost
            readinessProbe:
              exec:
                command:
                - curl
                - -sS
                - -o
                - /dev/null
                - localhost
    ```

2. 在 DCE 5.0 中通过 yaml 文件快速分别创建两个集群 cluster01 和 cluster02 的应用。

    ![创建应用](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/network/images/network-cross-cluster9.png)

    分别修改 `ConfigMap` 的内容，使得访问集群 cluster01 和集群 cluster02 中的 Service 时，返回的数据分别带有 cluster01 和 cluster02 名称的标签。可在 `rebel-base` 应用中查看容器组标签。

3. 在两个集群 cluster01 和 cluster02 中分别创建一个 global service video 的 Service，指向的是已创建的 `rebel-base` 应用。

    ![创建service应用](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/network/images/network-cross-cluster10.png)

    ![创建service应用](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/network/images/network-cross-cluster11.png)

    - Service 类型为 ClusterIP
    - 添加应用的容器组标签筛选对应的应用
    - 配置端口
    - 添加注解，使当前的 Service 在全局生效

    > 在创建集群 cluster02 的 Service 时，两个集群的 service name 必须相同，并位于相同的命名空间，拥有相同的端口名称和相同的 global 注解。

## 跨集群通信

1. 先查看集群 cluster02 中应用的 Pod IP。

    ![查看pod ip](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/network/images/network-cross-cluster12.png)

2. 进入集群 cluster01 详情，点击应用 `rebel-base`  Pod 控制台，`curl` 集群 cluster02 应用 `rebel-base` 的 Pod IP，成功返回 cluster02 信息，说明两个集群中的 Pod 可以相互通信。

    ![pod 通信](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/network/images/network-cross-cluster13.png)

3. 查看集群 cluster01 的 Service 名称，进入集群 cluster02 的应用 `rebel-base` Pod 控制台，`curl` 对应的 cluster01 的 Service 名称，有些返回内容来自 cluster01，说明两个集群中的 Pod 和 Service 也可以互相通信。

    ![Pod 和 Service通信](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/network/images/network-cross-cluster14.png)
