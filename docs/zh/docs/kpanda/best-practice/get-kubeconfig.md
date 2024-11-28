# 接入外部集群时获取永久 Token

通过 kubeconfig 可以快速将一个外部集群接入到集群管理中。为了保障接入的稳定性，kubeconfig 内需要使用较长时效的 Token（建议为永久 `TOKEN`）。
然而，不同集群服务提供商，如 `AWS EKS` 和 `GKE`，获取永久 Token 的方式不同，他们通常只提供有效期为 24 小时的 Token。

!!! note

    具体的产品操作界面参考： [接入集群](../user-guide/clusters/integrate-cluster.md)

## 创建具有集群管理员权限的 Service Account

为了解决上述问题，可以创建一个拥有集群管理员权限的 Service Account，并使用该 Service Account 的 kubeconfig 来接入集群。

!!! warning

    执行以下步骤时，请确保已经配置了 AWS 或者 GCP CLI，并有权限访问该集群，否则会报错。

1. 创建 Service Account 和 ClusterRoleBinding 的 YAML 配置：

    ```bash
    cat >eks-admin-service-account.yaml <<EOF
    apiVersion: v1
    kind: ServiceAccount
    metadata:
      name: eks-admin
      namespace: kube-system
    ---
    apiVersion: rbac.authorization.k8s.io/v1
    kind: ClusterRoleBinding
    metadata:
      name: eks-admin
    roleRef:
      apiGroup: rbac.authorization.k8s.io
      kind: ClusterRole
      name: cluster-admin
    subjects:
    - kind: ServiceAccount
      name: eks-admin
      namespace: kube-system
    EOF
    ```

2. 使用以下命令应用配置：

    ```bash
    kubectl apply -f eks-admin-service-account.yaml
    ```

## 为 Service Account 生成 Secret

在 Kubernetes 1.24 及以上版本中，创建 Service Account 默认不会创建包含 ca 证书和 user token 的 secret，需要自行关联。

1. 创建 Secret 的 YAML 配置：

    ```bash
    kubectl apply -f - <<EOF
    apiVersion: v1
    kind: Secret
    metadata:
      name: eks-admin-secret
      namespace: kube-system
      annotations:
        kubernetes.io/service-account.name: eks-admin
        type: kubernetes.io/service-account-token
    EOF
    ```

2. 查找名为 eks-admin 的 Service Account 密钥：

    ```bash
    kubectl -n kube-system get secret | grep eks-admin | awk '{print $1}'
    ```

## 检索 Service Account Token

1. 查看 eks-admin-secret 密钥的详情:

    ```bash
    kubectl -n kube-system describe secret eks-admin-secret
    ```

    现在，就可以看到 token 信息。查看是否有 `exp` 字段，这个字段的值就是 token 的过期时间。如果没有就是永久 token。 

## 配置 kubeconfig

1. 使用获取到的 token，设置 kubeconfig：

    ```bash
    kubectl config set-credentials eks-admin --token=eyJhbGciOiJSUzI...
    kubectl config set-cluster joincluster --insecure-skip-tls-verify=true --server=https://XXXXXX.gr7.ap-southeast-1.eks.amazonaws.com
    kubectl config set-context ekscontext --cluster=joincluster --user=eks-admin
    ```

2. 本地测试是否可以连接集群：

    ```bash
    kubectl config use-context ekscontext
    kubectl get node
    ```

## 导出并使用 kubeconfig

导出 kubeconfig 信息：

```bash
kubectl config view --minify --flatten --raw
```

复制导出的内容，添加到集群管理中，完成集群的接入。

!!! note

    - 1.24 及以上的集群版本创建 Service Account 默认不会创建包含 ca 证书和 user token 的 secret，需要自行关联。
      参阅 K8s 官方说明：[Kubernetes Service Account](https://kubernetes.io/zh-cn/docs/tasks/configure-pod-container/configure-service-account/#manually-create-an-api-token-for-a-serviceaccount)。
    - 使用 JWT 工具解析 token 可以查看 token 的过期时间，如 [jwt.io](https://jwt.io)。
