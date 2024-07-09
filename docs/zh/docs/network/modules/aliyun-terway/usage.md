# 使用文档

本文将介绍如何在阿里云上通过 `kubeadm` 工具安装一套 kubernetes 集群，并且安装 Terway 作为集群的 CNI 插件。

## 创建 ECS 实例

详细创建教程可参考阿里云官方文档，需要注意以下几点:

- 地域最好选择靠近您的地域，可降低网络时延、提高访问速度
- 需要创建专有网络(若无)，并选择可用区。创建虚拟交换机用于节点和 Pod 使用
- 根据实际需求选择实例规格，实例规格决定了 ECS 实例上 ENI 和 ENI 上辅助 IP 的数量，从而决定可运行 Pod 的数量(非 VPC 模式)

![create-ecs](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/network/images/ECS-Create.png)

!!! note

    安装 Kubernetes 集群时，要求每个节点的 CPU 不小于 2 核, 内存不小于 2 GB。

## 搭建 Kubernetes 集群

参考 [官方文档](https://kubernetes.io/zh-cn/docs/setup/production-environment/tools/kubeadm/install-kubeadm/), 在控制节点安装 kubeadm、kubectl。
在控制节点和工作节点安装：kubelet、容器运行时（如 containerd）。

!!! note

    需要修改每个节点 kubelet 的配置文件 `/usr/lib/systemd/system/kubelet.service.d/10-kubeadm.conf`，配置 `--provider-id`：

    ```shell
    META_EP=http://100.100.100.200/latest/meta-data
    provider_id=`curl -s $META_EP/region-id`.`curl -s $META_EP/instance-id`
    vi /usr/lib/systemd/system/kubelet.service.d/10-kubeadm.conf
    ...
    Environment="KUBELET_EXTRA_ARGS=--hostname-override=${provider_id} --provider-id=${provider_id}"
    ...
    ```

以 containerd 作为容器运行时为例，使用以下配置安装集群:

```shell
cat cluster.yaml
```
```yaml
apiVersion: kubeadm.k8s.io/v1beta3
bootstrapTokens:
  - groups:
      - system:bootstrappers:kubeadm:default-node-token
    token: abcdef.0123456789abcdef
    ttl: 24h0m0s
    usages:
      - signing
      - authentication
kind: InitConfiguration
localAPIEndpoint:
  bindPort: 6443
nodeRegistration:
  criSocket: unix:///var/run/containerd/containerd.sock
  imagePullPolicy: IfNotPresent
  taints: null
  kubeletExtraArgs:
    cloud-provider: "external"
---
apiServer:
  timeoutForControlPlane: 4m0s
apiVersion: kubeadm.k8s.io/v1beta3
certificatesDir: /etc/kubernetes/pki
clusterName: kubernetes
controllerManager: {}
dns: {}
etcd:
  local:
    dataDir: /var/lib/etcd
imageRepository: k8s.m.daocloud.io
kind: ClusterConfiguration
kubernetesVersion: 1.28.0
networking:
  dnsDomain: cluster.local
  serviceSubnet: 172.21.0.0/24
  podSubnet: 10.244.0.0/16
$ kubeadm init --config cluster.yaml
```

!!! note

    规划 serviceSubnet 和 podSubnet 不冲突。

    你可以使用 `k8s.m.daocloud.io` 作为镜像加速站。

创建集群之后，在工作节点使用 `kubeadm join` 加入工作节点到集群。

## 安装网络插件

### 安装 Terway CNI 插件

1. 在安装之前，Terway 访问阿里云 OpenAPI 需要得到 [RAM 权限](https://ram.console.aliyun.com/) 的 `access_id` 和 `access_key`，通过脚本编辑新建自定义权限策略，赋予 Terway 需要的权限:

    ```json
    {
      "Version": "1",
      "Statement": [{
          "Action": [
            "ecs:CreateNetworkInterface",
            "ecs:DescribeNetworkInterfaces",
            "ecs:AttachNetworkInterface",
            "ecs:DetachNetworkInterface",
            "ecs:DeleteNetworkInterface",
            "ecs:DescribeInstanceAttribute",
            "ecs:DescribeInstanceTypes",
            "ecs:AssignPrivateIpAddresses",
            "ecs:UnassignPrivateIpAddresses",
            "ecs:DescribeInstances",
            "ecs:ModifyNetworkInterfaceAttribute"
          ],
          "Resource": [
            "*"
          ],
          "Effect": "Allow"
        },
        {
          "Action": [
            "vpc:DescribeVSwitches"
          ],
          "Resource": [
            "*"
          ],
          "Effect": "Allow"
        }
      ]
    }
    ```

    !!! note
    
        为确保后续步骤中所使用的 RAM 用户具备足够的权限，请给予 RAM 用户AdministratorAccess 和 AliyunSLBFullAccess 权限。

    ![edit-ram](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/network/images/custom-ram.png)

    当创建完成，将该自定义权限策略绑定到用户或用户组:

    ![bind_ram](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/network/images/bind_ram.png)

    最后点击创建 AccessKey，并保存 `access_secret` 和 `access_key`，这需要在下面安装 Terway 的时候用到。

    ```shell 
    export ACCESS_KEY_ID=LTAI********************
    export ACCESS_KEY_SECRET=HAeS**************************
    ```

2. 安装 Terway CNI 插件。

    安装之前，需要更新[部署文件](../../yamls/terway.yaml)中 eni-config 的 configMap:

    - 更新 `access_secret` 和 `access_key`
    - 更新 vswitches, 这将决定 ENI模式下，Pod 将从哪个虚拟机交换机分配 IP 地址。格式为: "vswitches": {"cn-chengdu-a":["vsw-xxxx"]}。表示某个可用区下的虚拟交换机列表。
    - 更新 security_group，填写安全组ID, 这是集群级别生效。
    - 确保 service_cidr 为集群 service_subnet。

    执行安装:

    ```shell
    $ kubectl apply -f  terway.yaml
    $ kubectl get po -n kube-system -o wide | grep terway
    $ kubectl get po -n kube-system -o wide | grep terway
    terway-rjqbj                                                2/2     Running   0           3m   192.168.200.2   cn-chengdu.i-2vcxxxxx   <none>           <none>
    terway-z5cvh                                                2/2     Running   0           3m   192.168.200.1   cn-chengdu.i-2vcxxxxx   <none>           <none>
    ```

### 安装 CCM 组件，发布 VPC 路由

CCM 组件用于发布 Pod 跨节点访问路由以及 LoadBalancer Service 的实现:

1. 安装 ccm 的 configMap: cloud-config。 需要将 access 凭证进行 base64 转码:

    ```shell
    $ accessKeyIDBase64=`echo -n "$ACCESS_KEY_ID" |base64 -w 0`
    $ accessKeySecretBase64=`echo -n "$ACCESS_KEY_SECRET"|base64 -w 0`
    cat <<EOF | kubectl apply -f -
    apiVersion: v1
    kind: ConfigMap
    metadata:
      name: cloud-config
      namespace: kube-system
    data:
      cloud-config.conf: |-
        {
            "Global": {
                "accessKeyID": "$accessKeyIDBase64",
                "accessKeySecret": "$accessKeySecretBase64"
            }
        }
    EOF
    ```

2. 安装 CCM 组件, manifests 存放于 [cloud-controller-manager.yaml](../../yamls/cloud-controller-manager.yaml)。

    > 注意需要修改 `cluster_cidr` 为你集群真实的 podSubnet(10.244.0.0/16)。

    执行安装:

    ```shell
    kubectl apply -f cloud-controller-manager.yaml
    ```

3. 安装成功后，可在阿里云管理界面查看 VPC 路由已经成功同步:

    ![ccm-route](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/network/images/ccm-route.png)

    访问 Pod 子网路由的下一跳指向该节点。

## 验证

### VPC 模式

下面将通过创建测试应用验证安装:

```shell
cat << EOF | kubectl apply -f -
apiVersion: apps/v1
kind: Deployment
metadata:
  name: dao2048
spec:
  replicas: 2
  selector:
    matchLabels:
      app: dao-2048
  template:
    metadata:
      labels:
        app: dao-2048
    spec:
      containers:
      - image: ghcr.m.daocloud.io/daocloud/dao-2048:v1.2.0
        imagePullPolicy: IfNotPresent
        name: dao-2048
        resources:
          limits:
            cpu: 250m
            memory: 512Mi
          requests:
            cpu: 250m
            memory: 512Mi
EOF
```

创建完成后，经过测试发现：网络连通正常（包括 Pod -> Pod，Pod -> Service，nodePort，LoadBalancer Service），网络策略等功能正常。

### 使用 ENI 模式

在 VPC 模式下，Pod 的 IP 是来自虚拟子网，并且不会使用任何的弹性网卡。如果你想要 Pod 独占 ENI，在 VPC 模式，你可以通过下面的方式实现:

```shell
cat << EOF | kubectl apply -f -
apiVersion: apps/v1
kind: Deployment
metadata:
  name: dao2048-eni
spec:
  replicas: 2
  selector:
    matchLabels:
      app: dao-2048
  template:
    metadata:
      labels:
        app: dao-2048
    spec:
      containers:
      - image: ghcr.m.daocloud.io/daocloud/dao-2048:v1.2.0
        imagePullPolicy: IfNotPresent
        name: dao-2048
        resources:
          limits:
            aliyun/eni: 1
            cpu: 250m
            memory: 512Mi
          requests:
            aliyun/eni: 1
            cpu: 250m
            memory: 512Mi
EOF
```

!!! note

    通过在 resources 中声明：`aliyun/eni: 1`，使 Pod 独占 ENI 网卡。

```shell
$ kubectl get po -o wide | grep eni
dao2048-eni-7f85b8dcc4-6v97q   1/1     Running   0              15s   192.168.20.222   cn-chengdu.i-2vcxxxxxxxx   <none>           <none>
dao2048-eni-7f85b8dcc4-mvjbs   1/1     Running   0              15s   192.168.20.223   cn-chengdu.i-2vcxxxxxxxx   <none>           <none>
```

可以发现该 Pod 的 IP 与节点是同一网段，属于同一个 VPC 网卡，并且其 IP 是 ENI 网卡的主私网 IP。

![eni_ip](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/network/images/eni_ip.png)

经过测试，当设置 LoadBalancer/NodePort Service 的 **_ExternalTrafficPolicy 为 Local_** 时，会出现通信问题，参考 [#531](https://github.com/AliyunContainerService/terway/issues/531)

### ENIIP 模式(对自建集群支持不够)

- 自建集群安装 Veth 模式失败，详见 [#Issue 524](https://github.com/AliyunContainerService/terway/issues/524), 所以暂不支持 Veth 模式。
- 自建集群安装 IPVlan 模式后，有各种通信问题(Node 访问 Pod 及 LoadBalancer Service不通)，
  详见 [#Discussion 306](https://github.com/AliyunContainerService/terway/discussions/306), 所以暂不推荐使用此模式。
