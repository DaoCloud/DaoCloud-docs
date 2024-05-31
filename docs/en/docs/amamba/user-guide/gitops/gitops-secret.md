# GitOps Secret Encryption

In the GitOps operational model, resources to be deployed are stored in a Git repository in YAML format.
These files may contain sensitive information, such as database passwords, API keys, etc.,
which should not be stored in plain text. Additionally, even when these resources are deployed in a
Kubernetes cluster as secrets, they can still be easily viewed through base64 encoding,
leading to many security issues.

To address these problems, this article will introduce several solutions to implement
encryption for manifest files in GitOps. The solutions are mainly divided into two categories:

1. Based on ArgoCD's plugin mechanism, decrypt and replace sensitive information when rendering manifest files

    Advantages of this method:

    - Closely integrated with ArgoCD, no need to install additional components
    - Can be easily integrated with existing credential management systems
    - Supports many credential storage backends, such as Vault, Kubernetes Secret, AWS Secret, etc.
    - Supports encryption of any Kubernetes resource, such as secrets, configmaps,
      deployment environment variables, etc.

    Disadvantage: Sensitive information changes require **manual synchronization**

2. Independent of ArgoCD, relying on the project's or tool's own encryption/decryption
   capabilities for sensitive information

    Advantages of this method:

    - Does not depend on a specific GitOps implementation
    - Higher security (e.g., cannot be easily decrypted or viewed using `kubectl describe`)
    - Simple configuration
    - Full GitOps experience, no need for manual synchronization

    Disadvantage: Requires separate tool installation and manual configuration

Choose an appropriate solution based on the actual usage scenario.

## Based on ArgoCD's Plugin Mechanism

This solution uses the [argocd-vault-plugin](https://github.com/argoproj-labs/argocd-vault-plugin)
plugin, which will fetch sensitive information from a specified backend storage and integrate well with ArgoCD.

It supports many backend storages. This article will use **HashiCorp Vault** and **Kubernetes Secret** as examples.

!!! note 

    How to use Vault is not the focus of this article;
    here we only introduce how to configure this plugin to use Vault as the backend storage for sensitive information.

Some configurations need to be done before installing ArgoCD, as follows:

### Installation Configuration

#### Administrator Sets Backend Storage Access Credentials

Before installing ArgoCD, the administrator needs to create a secret for
the plugin to access the backend storage.

1. Backend storage is HashiCorp Vault

    ```yaml
    apiVersion: v1
    kind: Secret
    metadata:
      name: argocd-vault-plugin-credentials
      namespace: argo-cd # (1)!
    data:
      AVP_TYPE: vault # (2)!
      AVP_AUTH_TYPE: token # (3)!
      VAULT_ADDR: 10.6.10.11 # (4)!
      VAULT_TOKEN: cm9vdA==  # (5)!
    type: Opaque
    ```

    1. Namespace where ArgoCD is deployed
    2. Specify the type of backend storage as Vault
    3. Specify the auth type of the backend storage
    4. Vault's address
    5. Initialization token obtained from Vault pod logs
       (in actual use, set this to a token obtained with specific permissions and access policies)

    By configuring the above secret, during ArgoCD's runtime, the configurations in `data` will be passed
    to the `argocd-vault-plugin` as environment variables for the plugin to access Vault and fetch sensitive data.

2. Backend storage is Kubernetes Secret

    ```yaml
    apiVersion: v1
    kind: Secret
    metadata:
      name: argocd-vault-plugin-credentials
      namespace: argo-cd
    data:
      AVP_TYPE: kubernetessecret # (1)!
    type: Opaque
    ```

    1. Set the backend storage type to `kubernetessecret`

The above is the basic configuration. If the backend storage is of another type or requires
other configurations, refer to the [backend storage configuration](https://argocd-vault-plugin.readthedocs.io/en/stable/backends/).

#### Install ArgoCD

ArgoCD is pre-installed in the application workspace, but it can also be installed separately.
For detailed installation steps, see [Install ArgoCD](../../pluggable-components.md).
Below are configurations for two scenarios.

##### Modify the Default Installation of ArgoCD in the Workspace

1. Add a ConfigMap to configure the plugin

    Go to **Container Management** -> Select **kpanda-global-cluster** from the cluster list
    -> **ConfigMaps and Secrets** -> Create a new YAML, content as follows:

    ```yaml
    apiVersion: v1
    kind: ConfigMap
    metadata:
      name: cmp-plugin
      namespace: argo-cd
    data:
      avp.yaml: |
        apiVersion: argoproj.io/v1alpha1
        kind: ConfigManagementPlugin
        metadata:
          name: argocd-vault-plugin
        spec:
          allowConcurrency: true
          discover:
            find:
              command:
                - sh
                - "-c"
                - "find . -name '*.yaml' | xargs -I {} grep \"<path\\|avp\\.kubernetes\\.io\" {} | grep ."
          generate:
            command:
              - argocd-vault-plugin 
              - generate 
              - --verbose-sensitive-output=true 
              - ./
          lockRepo: false
      avp-helm.yaml:
        apiVersion: argoproj.io/v1alpha1
        kind: ConfigManagementPlugin
        metadata:
          name: argocd-vault-plugin-helm
        spec:
          allowConcurrency: true
          discover:
            find:
              command:
                - sh
                - "-c"
                - "find . -name 'Chart.yaml' && find . -name 'values.yaml'"
          generate:
            command:
              - sh
              - "-c"
              - |
                helm template $argocd_APP_NAME -n $ARGOCD_APP_NAMESPACE ${argocd_ENV_HELM_ARGS} . |
                argocd-vault-plugin generate -
          lockRepo: false
    ```

2. Modify the Deployment of `argocd-repo-server`

    Go to **Container Management** -> Select **kpanda-global-cluster** from the cluster list ->
    **Workloads** -> **Deployments** -> Select the `argocd` namespace -> Edit the YAML of
    `argocd-repo-server` with the following modifications:

    ```yaml
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: argocd-repo-server
      namespace: argo-cd
    spec:
      template:
        spec:
          volumes: # (1)!
            - name: cmp-plugin
              configMap:
                name: cmp-plugin
                defaultMode: 420
            - name: custom-tools
              emptyDir: {}
          initContainers:
            - name: init-vault-plugin # (2)!
              image: release.daocloud.io/amamba/argocd-vault-plugin:v1.17.0 # (3)!
              command:
                - sh
                - "-c"
              args:
                - cp /usr/local/bin/argocd-vault-plugin /custom-tools
              volumeMounts:
                - name: custom-tools
                  mountPath: /custom-tools
          containers:
            - name: avp # (4)!
              image: quay.io/argoproj/argocd:v2.10.4 # (5)!
              command:
                - /var/run/argocd/argocd-cmp-server
              envFrom:
                - secretRef:
                  name: argocd-vault-plugin-credentials
              volumeMounts:
                - name: var-files
                  mountPath: /var/run/argocd
                - name: plugins
                  mountPath: /home/argocd/cmp-server/plugins
                - name: tmp
                  mountPath: /tmp
                - name: cmp-plugin
                  mountPath: /home/argocd/cmp-server/config/plugin.yaml
                  subPath: avp.yaml
                - name: custom-tools
                  mountPath: /usr/local/bin/argocd-vault-plugin
                  subPath: argocd-vault-plugin
            - name: repo-server # (6)!
              envFrom:
                - secretRef:
                    name: argocd-vault-plugin-credentials
              volumeMounts:
                - name: cmp-plugin
                  mountPath: /home/argocd/cmp-server/config/plugin.yaml
                  subPath: avp.yaml
                - name: custom-tools
                  mountPath: /usr/local/bin/argocd-vault-plugin
                  subPath: argocd-vault-plugin
    ```

    1. Add volumes
    2. Add a new initContainer
    3. Replace the address if in an offline environment
    4. Add a sidecar container
    5. The image address should be the same as the `repo-server`
    6. Modify the existing `repo-server` container, adding `envFrom` and `volumeMounts`

##### Install ArgoCD Separately

Modify the following Helm values during installation:

```yaml
reposerver: # (1)!
  volumes: # (2)!
    - name: cmp-plugin
      configMap:
        name: cmp-plugin
    - name: custom-tools
      emptyDir: {}

  initContainers:
    - name: init-vault-plugin # (3)!
      image: release.daocloud.io/amamba/argocd-vault-plugin:v1.17.0 # (4)!
      command:
        - sh
        - "-c"
      args:
        - cp /usr/local/bin/argocd-vault-plugin /custom-tools
      volumeMounts:
        - name: custom-tools
          mountPath: /custom-tools

  envFrom: # (5)!
    - secretRef:
      name: argocd-vault-plugin-credentials

  volumeMounts: # (6)!
    - name: plugins
      mountPath: /home/argocd/cmp-server/plugins
    - name: tmp
      mountPath: /tmp
    - name: cmp-plugin
      mountPath: /home/argocd/cmp-server/config/plugin.yaml
      subPath: avp.yaml
    - name: custom-tools
      mountPath: /usr/local/bin/argocd-vault-plugin
      subPath: argocd-vault-plugin

  extraContainers: # (7)!
    - name: avp
      image: quay.io/argoproj/argocd:v2.10.4 # (8)!
      command:
        - /var/run/argocd/argocd-cmp-server
      envFrom:
        - secretRef:
            name: argocd-vault-plugin-credentials
      volumeMounts:
        - name: var-files
          mountPath: /var/run/argocd
        - name: plugins
          mountPath: /home/argocd/cmp-server/plugins
        - name: tmp
          mountPath: /tmp
        - name: cmp-plugin
          mountPath: /home/argocd/cmp-server/config/plugin.yaml
          subPath: avp.yaml
        - name: custom-tools
          mountPath: /usr/local/bin/argocd-vault-plugin
          subPath: argocd-vault-plugin

configs: # (9)!
  cmp:
    plugins:
      argocd-vault-plugin:
        allowConcurrency: true
        discover:
          find:
            command:
              - sh
              - "-c"
              - "find . -name '*.yaml' | xargs -I {} grep \"<path\\|avp\\.kubernetes\\.io\" {} | grep ."
        generate:
          command:
            - argocd-vault-plugin
            - generate
            - ./
        lockRepo: false
      argocd-vault-plugin-helm:
        allowConcurrency: true
        discover:
          find:
            command:
              - sh
              - "-c"
              - "find . -name 'Chart.yaml' && find . -name 'values.yaml'"
        generate:
          command:
            - sh
            - "-c"
            - |
              helm template $argocd_APP_NAME -n $ARGOCD_APP_NAMESPACE ${argocd_ENV_HELM_ARGS} . |
              argocd-vault-plugin generate -
        lockRepo: false
```

1. Modify the configuration of the `repo-server`
2. Add volumes
3. Add a new initContainer for copying the plugin binary
4. Add an offline environment prefix if necessary
5. Mount the configurations required by `argocd-vault-plugin` as environment variables
6. Mount the related plugin directories and configurations
7. Add a new container
8. The image here should be the same as the `repo-server` image
9. Additionally, modify the ConfigMap to add plugin configurations

#### Administrator Configures Sensitive Information

Before creating a GitOps application, the administrator needs to set up the sensitive data in advance.

For example, using Vault:

```shell
vault kv put secret/test-secret username="xxxx" password="xxxx"
```

Using Secret:

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: test-secret
  namespace: default
data:
  password: dGVzdC1wYXNz
  username: dGVzdC1wd2Q=
type: Opaque
```

#### Modify Manifest Files in the Git Repository

Modify the manifest files in the Git repository, replacing sensitive information with placeholders.
If the backend storage is Vault, an example:

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: test-secret-vault
  annotations:
    avp.kubernetes.io/path: "secret/data/test-secret"
    avp.kubernetes.io/secret-version: "2"
stringData:
  password: <password>
  username: <username>
```

Explanation:

- Add the corresponding annotations for the plugin to recognize. Annotation explanations:
    - `avp.kubernetes.io/path`: Specifies the path to the sensitive information.
      If the backend storage is Vault, this path is in Vault. The value can be obtained via
      `vault kv get secret/test-secret`. Add `/data` after `secret`.
    - `avp.kubernetes.io/secret-version`: Specifies the version of the sensitive information.
      If the backend storage supports version management, you can specify the version number.
- In `stringData`, `password` and `username` are the keys for the sensitive information,
  `<password>` and `<username>` are placeholders. The `password` in `<password>` is the specified key in Vault.

If the backend storage is Kubernetes Secret, an example:

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: test-secret-k8s
  annotations:
    avp.kubernetes.io/path: "default/test-secret"
stringData:
  password: <password>
  username: <username>
```

Explanation:

- Kubernetes Secret does not support version management, so `avp.kubernetes.io/secret-version` is invalid.
- The value in `avp.kubernetes.io/path` is the namespace and name of the secret. For example,
  `default/test-secret` means the `test-secret` secret in the `default` namespace. This secret
  is usually created by the administrator and deployed in a namespace with specific permissions,
  not stored in the Git repository.
- The placeholders in `stringData` are the same as the placeholders for Vault.

Supported annotations are as follows:

| Annotation                       | Description |
| -------------------------------- | ----------- |
| avp.kubernetes.io/path           | The path in Vault |
| avp.kubernetes.io/ignore         | If true, rendering is ignored |
| avp.kubernetes.io/kv-version     | The version of the KV storage engine |
| avp.kubernetes.io/secret-version | Specifies the version of the value |
| avp.kubernetes.io/remove-missing | For secrets and configmaps, ignore errors if keys are missing in Vault |

Placeholders also support functions, such as `<password | base64>` to encode the value of `password` in base64.

#### View Deployment Results

```shell
$ kubectl get secret test-secret-k8s -o yaml | yq eval ".data" -
> password: dGVzdC1wYXNz
  username: dGVzdC1wd2Q=
```

You can see that the sensitive information in the secret has been replaced with actual values.

#### Sensitive Information Update

!!! note

    If sensitive information changes, ArgoCD **cannot detect** it
    (even if the created Application is set to auto-sync).
    You need to go to the ArgoCD backend page, click the **hard-refresh** button,
    and then click the **sync** button to synchronize.

## Relying on the Project's or Tool's Encryption/Decryption Capabilities

There are many implementations of this method. The biggest advantage is that they are not
bound to ArgoCD, but can still be deployed using the GitOps approach. This article uses
[sealed-secrets](https://github.com/bitnami-labs/sealed-secrets) as an example.

Sealed-secrets includes two tools:

- A controller for encryption, decryption, and creating secrets
- A client tool `kubeseal`

### Installation

1. Install the Controller

    ```shell
    helm repo add sealed-secrets https://bitnami-labs.github.io/sealed-secrets
    helm install sealed-secrets -n kube-system --set-string fullnameOverride=sealed-secrets-controller sealed-secrets/sealed-secrets
    ```

2. Install the Client Tool

    ```shell
    KUBESEAL_VERSION='0.26.1'
    wget "https://github.com/bitnami-labs/sealed-secrets/releases/download/v${KUBESEAL_VERSION:?}/kubeseal-${KUBESEAL_VERSION:?}-linux-amd64.tar.gz" \
    tar -xvzf kubeseal-${KUBESEAL_VERSION:?}-linux-amd64.tar.gz kubeseal \
    sudo install -m 755 kubeseal /usr/local/bin/kubeseal
    ```

### Usage

The administrator generates an encrypted CR file:

```shell
# Use the command line tool to encrypt the secret
kubectl create secret generic mysecret -n argo-cd --dry-run=client --from-literal=username=xxxx -o yaml | \
    kubeseal \
      --controller-name=sealed-secrets-controller \  # Note the name and namespace
      --controller-namespace=kube-system \
      --format yaml > mysealedsecret.yaml
```

The generated file is as follows:

```yaml
apiVersion: bitnami.com/v1alpha1
kind: SealedSecret
metadata:
  name: mysecret
  namespace: argo-cd
spec:
  encryptedData:
    username: AgBy3i4OJSWK+PiTySYZZA9rO43cGDEq.....  # (1)!
  template:                                          # (2)!
    type: kubernetes.io/dockerconfigjson
    immutable: true
    metadata:
      labels:
        "xxxx":"xxxx"
      annotations:
        "xxxx":"xxxx"
```

Sure, here's the translation into English:

1. Ciphertext generated by kubeseal
2. In addition, you can specify a template for generating secrets, similar to a pod template.

The data is encrypted using **asymmetric encryption**, and only the controller can decrypt it.
Therefore, you can safely store the encrypted data in a Git repository.

When ArgoCD synchronizes, the sealed controller will generate the secret based on the `SealedSecret`.
The data in the final generated secret will be decrypted, so when sensitive information changes,
you only need to update the `SealedSecret` in the Git repository to achieve automatic synchronization.
