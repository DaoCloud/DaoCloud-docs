# Get Permanent Token When Accessing External Clusters

You can quickly integrate an external cluster into cluster management using kubeconfig.
To ensure the stability of the integration, it is recommended to use a long-lasting token
(preferably a permanent token) in the kubeconfig. However, different cluster service providers,
such as AWS EKS and GKE, have different methods for getting a permanent token,
typically only providing tokens with a validity of 24 hours.

!!! note

    For specific product operation interface reference: [Integrate Cluster](../user-guide/clusters/integrate-cluster.md)

## Create a ServiceAccount with Cluster Administrator Permissions

To address the above issue, you can create a ServiceAccount with cluster administrator permissions and use the kubeconfig of this ServiceAccount to access the cluster.

!!! warning

    When executing the following steps, ensure that you have configured the AWS or GCP CLI and have permissions to access the cluster, otherwise an error will occur.

1. Create the YAML configuration for the ServiceAccount and ClusterRoleBinding:

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

2. Apply the configuration using the following command:

    ```bash
    kubectl apply -f eks-admin-service-account.yaml
    ```

## Generate Secret for ServiceAccount

In Kubernetes versions 1.24 and above, creating a ServiceAccount does not automatically create a secret containing the CA certificate and user token; you need to associate it manually.

1. Create the YAML configuration for the Secret:

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

2. Find the secret corresponding to the ServiceAccount named eks-admin:

    ```bash
    kubectl -n kube-system get secret | grep eks-admin | awk '{print $1}'
    ```

## Retrieve ServiceAccount Token

1. View the details of the eks-admin-secret:

    ```bash
    kubectl -n kube-system describe secret eks-admin-secret
    ```

    Now, you can see the token information. Check if there is an `exp` field;
    the value of this field is the expiration time of the token. If there is no such field, it is a permanent token.

## Configure kubeconfig

1. Using the token, set up the kubeconfig:

    ```bash
    kubectl config set-credentials eks-admin --token=eyJhbGciOiJSUzI...
    kubectl config set-cluster joincluster --insecure-skip-tls-verify=true --server=https://XXXXXX.gr7.ap-southeast-1.eks.amazonaws.com
    kubectl config set-context ekscontext --cluster=joincluster --user=eks-admin
    ```

2. Test locally to see if you can connect to the cluster:

    ```bash
    kubectl config use-context ekscontext
    kubectl get node
    ```

## Export and Use kubeconfig

Export the kubeconfig information:

```bash
kubectl config view --minify --flatten --raw
```

Copy the exported content and add it to the cluster management to complete the integration of the cluster.

!!! note

    - In cluster versions 1.24 and above, creating a ServiceAccount does not automatically create a secret
      containing the CA certificate and user token; you need to associate it manually.
      Refer to the official K8s documentation: [Kubernetes ServiceAccount](https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/#manually-create-an-api-token-for-a-serviceaccount).
    - You can use JWT tools to parse the token and check its expiration time; refer to [jwt.io](https://jwt.io).
