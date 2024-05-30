# Integrate the Rancher Cluster

This guide explains how to integrate a Rancher cluster.

## Prerequisites

- Prepare a Rancher cluster with administrator privileges and ensure network connectivity between the container management cluster and the target cluster.
- You should have permissions not lower than [kpanda owner](../permissions/permission-brief.md).

## Steps

### Step 1: Create a ServiceAccount user with administrator privileges in the Rancher cluster

1. Log in to the Rancher cluster with a role that has administrator privileges, and create a file named __sa.yaml__ using the terminal.

    ```bash
    vi sa.yaml
    ```

    Press the __i__ key to enter insert mode, and enter the following content:

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

    Press the __Esc__ key to exit insert mode, then enter __:wq__ to save and exit.

2. Run the following command in the current directory to create a ServiceAccount named __rancher-rke__ (referred to as __SA__ for short):

    ```bash
    kubectl apply -f sa.yaml
    ```

    The expected output is as follows:

    ```console
    clusterrole.rbac.authorization.k8s.io/rancher-rke created
    clusterrolebinding.rbac.authorization.k8s.io/rancher-rke created
    serviceaccount/rancher-rke created
    ```

3. Create a secret named __rancher-rke-secret__ and bind the secret to the __rancher-rke__ SA.

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

    The output is similar to:

    ```bash
    secret/rancher-rke-secret created
    ```

    !!! note

        If your cluster version is lower than 1.24, please ignore this step and proceed to the next one.

4. Check secret for __rancher-rke__ SA:

    ```bash
    kubectl -n kube-system get secret | grep rancher-rke | awk '{print $1}'
    ```

    The output is similar to:

    ```bash
    rancher-rke-secret
    ```

    Check the __rancher-rke-secret__ secret:

    ```bash
    kubectl -n kube-system describe secret rancher-rke-secret
    ```

    The output is similar to:

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

### Step 2: Update kubeconfig with the rancher-rke SA authentication on your local machine

Perform the following steps on any local node where __kubelet__ is installed:

1. Configure kubelet token.

    ```bash
    kubectl config set-credentials rancher-rke --token= __rancher-rke-secret__ 里面的 token 信息
    ```

    For example,

    ```
    kubectl config set-credentials eks-admin --token=eyJhbGciOiJSUzI1NiIsImtpZCI6IjUtNE9nUWZLRzVpbEJORkZaNmtCQXhqVzRsZHU4MHhHcDBfb0VCaUo0V1kifQ.eyJpc3MiOiJrdWJlcm5ldGVzL3NlcnZpY2VhY2NvdW50Iiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9uYW1lc3BhY2UiOiJrdWJlLXN5c3RlbSIsImt1YmVybmV0ZXMuaW8vc2VydmljZWFjY291bnQvc2VjcmV0Lm5hbWUiOiJyYW5jaGVyLXJrZS1zZWNyZXQiLCJrdWJlcm5ldGVzLmlvL3NlcnZpY2VhY2NvdW50L3NlcnZpY2UtYWNjb3VudC5uYW1lIjoicmFuY2hlci1ya2UiLCJrdWJlcm5ldGVzLmlvL3NlcnZpY2VhY2NvdW50L3NlcnZpY2UtYWNjb3VudC51aWQiOiJkODNkZjVkOS1iZDdkLTQ4OGQtYTA0Ni1iNzQwNjE4YTAxNzQiLCJzdWIiOiJzeXN0ZW06c2VydmljZWFjY291bnQ6a3ViZS1zeXN0ZW06cmFuY2hlci1ya2UifQ.VNsMtPEFOdDDeGt_8VHblcMRvjOwPXMM-79o9UooHx6q-VkHOcIOp3FOT2hnEdNnIsyODZVKCpEdCgyozX-3y5x2cZSZpocnkMcBbQm-qfTyUcUhAY7N5gcYUtHUhvRAsNWJcsDCn6d96gT_qo-ddo_cT8Ri39Lc123FDYOnYG-YGFKSgRQVy7Vyv34HIajZCCjZzy7i--eE_7o4DXeTjNqAFMFstUxxHBOXI3Rdn1zKQKqh5Jhg4ES7X-edSviSUfJUX-QV_LlAw5DuAyGPH7bDH4QaQ5k-p6cIctmpWZE-9wRDlKA4LYRblKE7MJcI6OmM4ldlMM0Jc8N-gCtl4w
    ```

2. Configure the kubelet APIServer information:

    ```bash
    kubectl config set-cluster {cluster-name} --insecure-skip-tls-verify=true --server={APIServer}
    ```

    - __{cluster-name}__ : Refers to the name of your Rancher cluster.
    - __{APIServer}__ : Refers to the access address of the cluster, usually the IP address of the control node + port 6443, such as `https://10.X.X.X:6443` .

    For example,

    ```bash
    kubectl config set-cluster rancher-rke --insecure-skip-tls-verify=true --server=https://10.X.X.X:6443
    ```

3.  Configure the kubelet context:

    ```bash
    kubectl config set-context {context-name} --cluster={cluster-name} --user={SA-usename}
    ```

    For example, 

    ```bash
    kubectl config set-context rancher-rke-context --cluster=rancher-rke --user=rancher-rke
    ```

4. Specify the newly created context __rancher-rke-context__ in kubelet.

    ```bash
    kubectl config use-context rancher-rke-context
    ```

5. Retrieve the kubeconfig information for the context __rancher-rke-context__ .

    ```bash
    kubectl config view --minify --flatten --raw
    ```

    The output is similar to:

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

### Step 3: Connect the Cluster in the DCE Interface

Using the kubeconfig file obtained earlier, refer to the [Integrate Cluster](./integrate-cluster.md) documentation to connect the Rancher cluster to the Rancher cluster.
