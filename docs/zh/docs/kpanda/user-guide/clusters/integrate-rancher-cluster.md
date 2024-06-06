# 接入 rancher 集群

本文介绍如何接入 rancher 集群。

## 前提条件

- 准备一个具有管理员权限的待接入 ranhcer 集群，确保容器管理集群和待接入集群之间网络通畅。
- 当前操作用户应具有 [Kpanda Owner](../permissions/permission-brief.md) 或更高权限。

## 操作步骤

### 步骤一：在 rancher 集群创建具有管理员权限的 ServiceAccount 用户

1. 使用具有管理员权限的角色进入 rancher 集群，并使用终端新建一个名为 __sa.yaml__ 的文件。

    ```bash
    vi sa.yaml
    ```

    然后按下 i 键进入插入模式，输入以下内容：

    ```yaml title="sa.yaml"
    apiVersion: rbac.authorization.k8s.io/v1
    kind: ClusterRole
    metadata:
      name: rancher-rke
    rules:
      - apiGroups:
      - '*'
      resources:
      - '*'
      verbs:
      - '*'
      - nonResourceURLs:
      - '*'
      verbs:
      - '*'
    ---
    apiVersion: rbac.authorization.k8s.io/v1
    kind: ClusterRoleBinding
    metadata:
      name: rancher-rke
    roleRef:
        apiGroup: rbac.authorization.k8s.io
        kind: ClusterRole
        name: rancher-rke
      subjects:
      - kind: ServiceAccount
        name: rancher-rke
        namespace: kube-system
    ---
    apiVersion: v1
    kind: ServiceAccount
    metadata:
      name: rancher-rke
      namespace: kube-system
    ```

    按下 __esc__ 键退出插入模式，然后输入 __ :wq__ 保存并退出。

2. 在当前路径下执行如下命令，新建名为 __rancher-rke__ 的 ServiceAccount（以下简称为 __SA__ ）：

    ```bash
    kubectl apply -f sa.yaml
    ```

    预期输出如下：

    ```console
    clusterrole.rbac.authorization.k8s.io/rancher-rke created
    clusterrolebinding.rbac.authorization.k8s.io/rancher-rke created
    serviceaccount/rancher-rke created
    ```

3. 创建名为 __rancher-rke-secret__ 的密钥，并将密钥和 __rancher-rke__ SA 绑定。

    ```bash
    kubectl apply -f - <<EOF
    apiVersion: v1
    kind: Secret
    metadata:
      name: rancher-rke-secret
      namespace: kube-system
      annotations:
        kubernetes.io/service-account.name: rancher-rke
      type: kubernetes.io/service-account-token
    EOF
    ```

    预期输出如下：

    ```bash
    secret/rancher-rke-secret created
    ```

    !!! note

        如果您的集群版本低于 1.24，请忽略此步骤，直接前往下一步。

4. 查找 __rancher-rke__ SA 的密钥：

    ```bash
    kubectl -n kube-system get secret | grep rancher-rke | awk '{print $1}'
    ```

    预期输出：

    ```bash
    rancher-rke-secret
    ```

    查看密钥 __rancher-rke-secret__ 的详情：

    ```bash
    kubectl -n kube-system describe secret rancher-rke-secret
    ```

    预期输出：

    ```console
    Name:         rancher-rke-secret
    Namespace:    kube-system
    Labels:       <none>
    Annotations:  kubernetes.io/service-account.name: rancher-rke
                kubernetes.io/service-account.uid: d83df5d9-bd7d-488d-a046-b740618a0174

    Type:  kubernetes.io/service-account-token

    Data
    ====
    ca.crt:     570 bytes
    namespace:  11 bytes
    token:      eyJhbGciOiJSUzI1NiIsImtpZCI6IjUtNE9nUWZLRzVpbEJORkZaNmtCQXhqVzRsZHU4MHhHcDBfb0VCaUo0V1kifQ.eyJpc3MiOiJrdWJlcm5ldGVzL3NlcnZpY2VhY2NvdW50Iiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9uYW1lc3BhY2UiOiJrdWJlLXN5c3RlbSIsImt1YmVybmV0ZXMuaW8vc2VydmljZWFjY291bnQvc2VjcmV0Lm5hbWUiOiJyYW5jaGVyLXJrZS1zZWNyZXQiLCJrdWJlcm5ldGVzLmlvL3NlcnZpY2VhY2NvdW50L3NlcnZpY2UtYWNjb3VudC5uYW1lIjoicmFuY2hlci1ya2UiLCJrdWJlcm5ldGVzLmlvL3NlcnZpY2VhY2NvdW50L3NlcnZpY2UtYWNjb3VudC51aWQiOiJkODNkZjVkOS1iZDdkLTQ4OGQtYTA0Ni1iNzQwNjE4YTAxNzQiLCJzdWIiOiJzeXN0ZW06c2VydmljZWFjY291bnQ6a3ViZS1zeXN0ZW06cmFuY2hlci1ya2UifQ.VNsMtPEFOdDDeGt_8VHblcMRvjOwPXMM-79o9UooHx6q-VkHOcIOp3FOT2hnEdNnIsyODZVKCpEdCgyozX-3y5x2cZSZpocnkMcBbQm-qfTyUcUhAY7N5gcYUtHUhvRAsNWJcsDCn6d96gT_qo-ddo_cT8Ri39Lc123FDYOnYG-YGFKSgRQVy7Vyv34HIajZCCjZzy7i--eE_7o4DXeTjNqAFMFstUxxHBOXI3Rdn1zKQKqh5Jhg4ES7X-edSviSUfJUX-QV_LlAw5DuAyGPH7bDH4QaQ5k-p6cIctmpWZE-9wRDlKA4LYRblKE7MJcI6OmM4ldlMM0Jc8N-gCtl4w
    ```

### 步骤二：在本地使用 rancher-rke SA 的认证信息更新 kubeconfig 文件

在任意一台安装了 __kubelet__ 的本地节点执行如下操作：

1. 配置 kubelet token：

    ```bash
    kubectl config set-credentials rancher-rke --token=`rancher-rke-secret` 里面的 token 信息
    ```

    例如：

    ```
    kubectl config set-credentials eks-admin --token=eyJhbGciOiJSUzI1NiIsImtpZCI6IjUtNE9nUWZLRzVpbEJORkZaNmtCQXhqVzRsZHU4MHhHcDBfb0VCaUo0V1kifQ.eyJpc3MiOiJrdWJlcm5ldGVzL3NlcnZpY2VhY2NvdW50Iiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9uYW1lc3BhY2UiOiJrdWJlLXN5c3RlbSIsImt1YmVybmV0ZXMuaW8vc2VydmljZWFjY291bnQvc2VjcmV0Lm5hbWUiOiJyYW5jaGVyLXJrZS1zZWNyZXQiLCJrdWJlcm5ldGVzLmlvL3NlcnZpY2VhY2NvdW50L3NlcnZpY2UtYWNjb3VudC5uYW1lIjoicmFuY2hlci1ya2UiLCJrdWJlcm5ldGVzLmlvL3NlcnZpY2VhY2NvdW50L3NlcnZpY2UtYWNjb3VudC51aWQiOiJkODNkZjVkOS1iZDdkLTQ4OGQtYTA0Ni1iNzQwNjE4YTAxNzQiLCJzdWIiOiJzeXN0ZW06c2VydmljZWFjY291bnQ6a3ViZS1zeXN0ZW06cmFuY2hlci1ya2UifQ.VNsMtPEFOdDDeGt_8VHblcMRvjOwPXMM-79o9UooHx6q-VkHOcIOp3FOT2hnEdNnIsyODZVKCpEdCgyozX-3y5x2cZSZpocnkMcBbQm-qfTyUcUhAY7N5gcYUtHUhvRAsNWJcsDCn6d96gT_qo-ddo_cT8Ri39Lc123FDYOnYG-YGFKSgRQVy7Vyv34HIajZCCjZzy7i--eE_7o4DXeTjNqAFMFstUxxHBOXI3Rdn1zKQKqh5Jhg4ES7X-edSviSUfJUX-QV_LlAw5DuAyGPH7bDH4QaQ5k-p6cIctmpWZE-9wRDlKA4LYRblKE7MJcI6OmM4ldlMM0Jc8N-gCtl4w
    ```

2. 配置 kubelet APIServer 信息：

    ```bash
    kubectl config set-cluster {集群名} --insecure-skip-tls-verify=true --server={APIServer}
    ```

    - __{集群名}__ ：指 rancher 集群的名称。
    - __{APIServer}__ ：指集群的访问地址，一般为集群控制节点 IP + 6443 端口，如 `https://10.X.X.X:6443`

    例如：

    ```bash
    kubectl config set-cluster rancher-rke --insecure-skip-tls-verify=true --server=https://10.X.X.X:6443
    ```

3.  配置 kubelet 上下文信息：

    ```bash
    kubectl config set-context {上下文名称} --cluster={集群名} --user={SA 用户名}
    ```

    例如：

    ```bash
    kubectl config set-context rancher-rke-context --cluster=rancher-rke --user=rancher-rke
    ```

4. 在 kubelet 中指定我们刚刚新建的上下文 __rancher-rke-context__ ：

    ```bash
    kubectl config use-context rancher-rke-context
    ```

5. 获取上下文 __rancher-rke-context__ 中的 kubeconfig 信息。

    ```bash
    kubectl config view --minify --flatten --raw
    ```

    预期输出：

    ```yaml
    apiVersion: v1
      clusters:
      - cluster:
        insecure-skip-tls-verify: true
        server: https://77C321BCF072682C70C8665ED4BFA10D.gr7.ap-southeast-1.eks.amazonaws.com
      name: joincluster
      contexts:
      - context:
        cluster: joincluster
        user: eks-admin
      name: ekscontext
      current-context: ekscontext
      kind: Config
      preferences: {}
      users:
      - name: eks-admin
      user:
        token: eyJhbGciOiJSUzI1NiIsImtpZCI6ImcxTjJwNkktWm5IbmRJU1RFRExvdWY1TGFWVUtGQ3VIejFtNlFQcUNFalEifQ.eyJpc3MiOiJrdWJlcm5ldGVzL3NlcnZpY2VhY2NvdW50Iiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9uYW1lc3BhY2UiOiJrdWJlLXN5c3RlbSIsImt1YmVybmV0ZXMuaW8vc2VydmljZWFjY291bnQvc2V
    ```

### 步骤三：在 DCE 界面接入集群

使用刚刚获取的 kubeconfig 文件，参考[接入集群](./integrate-cluster.md)文档，将 rancher 集群接入 global 集群。
