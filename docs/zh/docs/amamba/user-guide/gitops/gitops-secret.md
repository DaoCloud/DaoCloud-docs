# GitOps Secret 加密

在 GitOps 运维模式中，待部署资源都是以 yaml 的形式存放在 Git 仓库中，而这些文件中可能包含敏感信息，
例如数据库密码、API 密钥等，它们不应该以明文的形式存储，
同时，当这些资源被部署在 kubernetes 集群中时，即使是以 secret 的方式，依旧可以通过 base64 很轻易的查看，这会造成很多安全问题。

为了解决这些问题，本文将介绍以下几种方案来实现 GitOps 中 manifest 文件的加密功能。
实现方案主要分为两类：

1. 基于 argocd 的 plugin 机制，在渲染 manifest 文件时进行解密并替换敏感信息

    这种方式的优点是：

    - 与 argocd 结合紧密，不需要安装额外的组件
    - 可以方便的与现有的凭证管理系统集成
    - 支持很多的凭证存储后端，如 vault、k8s secret、aws secret 等
    - 可以支持任意 kubernetes 资源的加密，如 secret、configmap、deployment 的环境变量等

    缺点：敏感信息变更后需要 **手动同步**

2. 不依赖于 argocd，依赖于项目或工具本身的加解密能力对敏感信息进行加解密

    这种方式的优点是：

    - 不依赖与具体的 GitOps 实现
    - 安全性更强（如无法轻易解密，或无法通过 kubectl describe 等方式查看）
    - 配置简单
    - 完全的 GitOps 体验，不需要手动同步

    缺点：需要单独安装工具，需要手动配置

请根据实际的使用情况选择合适的方案。

## 基于 argocd 的 plugin 机制

此方案中使用到的是[argocd-vault-plugin](https://github.com/argoproj-labs/argocd-vault-plugin)插件，
它将会从指定的后端存储中获取敏感信息，可以与 argocd 较好的结合。

它支持的后端储存很多，本文以 **HashiCorp Vault** 和 **kubernetes secret** 为例。

> 如何使用 vault 不是本文的重点，这里只介绍如何配置此插件使用 vault 作为后端敏感信息的存储。

在使用之前需要在安装 argocd 时进行一些配置，具体步骤如下：

### 安装配置

#### 管理员设置后端存储访问密钥

安装 argocd 之前，需要管理员先创建一下 secret，用于此插件访问后端存储

1. 后端存储为 HashiCorp Vault

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

    1. argocd 部署的命名空间
    2. 指定后端存储的类型 vault
    3. 指定后端存储的 auth 类型
    4. valut 的地址
    5. 通过 vault 的 pod 日志获取到的初始化 token（在实际使用时，需要设置为具体的权限和访问策略获取到的 token）

    通过配置上述 secret，在 argocd 运行期间，会将 data 中的配置项以环境变量的形势传递给
    `argocd-vault-plugin`，用于此插件访问具体的 vault 来获取敏感数据。

2. 后端存储为 Kubernetes Secret

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

    1. 设置后端存储类型为 kubernetessecret

上面为最基础的配置，如果后端存储为其他类型，
或者需要有其他的配置项请查看[后端存储配置](https://argocd-vault-plugin.readthedocs.io/en/stable/backends/)。

#### 安装 argocd

应用工作台中默认安装了 argoCD，也可以单独安装，具体的安装步骤请看[安装 argocd](../../pluggable-components.md)，
下面根据两种情况进行配置。

##### 修改工作台默认安装的 argoCD

1. 添加一个 ConfigMap，用于配置插件

    前往 **容器管理** -> 集群列表选择 **kpanda-global-cluster** -> **配置与密钥** -> 通过 yaml 新建， 内容如下:

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

2. 修改 argocd-repo-server 的 Deployment

    前往 **容器管理** -> 集群列表选择 **kpanda-global-cluster** -> **工作负载** -> **无状态负载** ->
    选择命名空间 argocd -> 编辑 argocd-repo-server 的 yaml，进行如下修改：

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

    1. 添加 volumes
    2. 添加一个新的 initContainer
    3. 如果是离线环境需要替换地址
    4. 添加一个 sidecar 容器
    5. 镜像地址需要与 repo-server 的相同
    6. 修改原有的 repo-server container，添加 envFrom 和 volumeMounts

##### 单独安装 argoCD

在安装时需要修改如下 helm values:

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

1. 需要修改 repo-server 的配置
2. 添加 volumes
3. 新增一个 initContainer 插件二进制文件的拷贝
4. 如果是离线环境，还需要添加离线环境的前缀地址
5. 将 argocd-vault-plugin 需要使用的配置以环境变量的形式进行挂载
6. 将相关 plugin 的目录和配置进行挂载
7. 添加一个新的 container
8. 此处的镜像需要与 repo-server 的镜像保持一致
9. 除此之外，还需要修改 configmap 添加插件配置

#### 管理员配置敏感信息

在创建 GitOps 应用之前，需要管理员提前设置好敏感数据。

例如使用 vault：

```shell
vault kv put secret/test-secret username="xxxx" password="xxxx"
```

使用 Secret：

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

#### 修改 Git 仓库中的 manifest 文件

修改 Git 仓库中的 manifest 文件，将敏感信息替换为占位符的形式，如果后端存储采用的是 vault，示例：

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

说明：

- 需要添加对应的 annotations，用于插件识别，annotation 说明：
    - `avp.kubernetes.io/path`：指定敏感信息的路径，如后端存储使用 vault，
      此路径为 vault 中的路径. 值可以通过 `vault kv get secret/test-secret` 得到。通过需要在 secret 后面加上 /data.
    - `avp.kubernetes.io/secret-version`：指定敏感信息的版本，如果后端存储支持版本管理，可以指定版本号
- `stringData` 中的 `password` 和 `username` 为敏感信息的 key，`<password>` 和 `<username>`
  为占位符，`<password>` 中的 password 为指定 vault 中的 key

如果后端存储使用的是 kubernetes secret，示例：

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

说明：

- kubernetes secret 不支持版本管理，因此 `avp.kubernetes.io/secret-version` 是无效的
- `avp.kubernetes.io/path` 中的值为 secret 的命名空间和名称，如 `default/test-secret`
  表示在 default 命名空间下的 `test-secret` secret。
  这个 secret 通常由管理员创建，并且部署在指定权限的 namespace 中，不会保存在 Git 仓库中。
- `stringData` 中的占位符与 vault 的占位符一致

支持的 annotations 如下：

| Annotation                       | 描述 |
| -------------------------------- | ---- |
| avp.kubernetes.io/path           | vault 的 path 路径 |
| avp.kubernetes.io/ignore         | 为 true 则忽略渲染 |
| avp.kubernetes.io/kv-version     | KV 存储引擎的版本 |
| avp.kubernetes.io/secret-version | 指定 value 的版本 |
| avp.kubernetes.io/remove-missing | 对于 secret 和 configmap 而言，忽略 key 未在 vault 中的报错 |

同时在 `<placeholder>` 中还支持使用函数，如 `<password | base64>` 表示将 password 的值进行 base64 编码。

#### 查看部署结果

```shell
$ > kubectl get secret test-secret-k8s -o yaml | yq eval ".data" -
> password: dGVzdC1wYXNz
  username: dGVzdC1wd2Q=
```

可以看到 secret 中的敏感信息已经被替换为实际的值。

#### 敏感信息更新

!!! note

    如果敏感信息发生变更，argocd是 **无法感知** 到的（即使创建的 Application 选择自动同步），
    需要进入 argocd 的后台页面，点击 **hard-refresh **按钮，再点击 **sync** 按钮才能进行同步。

## 依赖于项目或工具本身的加解密能力

这种方式实现的有很多，最大的优点就是他们不与 argocd 绑定，但是仍然可以采用 GitOps 的方式进行部署。
本文中采用 [sealed-secrets](https://github.com/bitnami-labs/sealed-secrets)来实现。

sealed-secrets 包含两个工具：

- 一个 controller，用户加解密和创建 secret
- 一个客户端工具 kubeseal

### 安装

1. 安装 Controller

    ```shell
    helm repo add sealed-secrets https://bitnami-labs.github.io/sealed-secrets
    helm install sealed-secrets -n kube-system --set-string fullnameOverride=sealed-secrets-controller sealed-secrets/sealed-secrets
    ```

2. 安装客户端工具

    ```shell
    KUBESEAL_VERSION='0.26.1'
    wget "https://github.com/bitnami-labs/sealed-secrets/releases/download/v${KUBESEAL_VERSION:?}/kubeseal-${KUBESEAL_VERSION:?}-linux-amd64.tar.gz" \
    tar -xvzf kubeseal-${KUBESEAL_VERSION:?}-linux-amd64.tar.gz kubeseal \
    sudo install -m 755 kubeseal /usr/local/bin/kubeseal
    ```

### 使用

管理员生成加密的 CR 文件：

```shell
# 使用命令行工具将 secret 加密
kubectl create secret generic mysecret -n argo-cd --dry-run=client --from-literal=username=xxxx -o yaml | \
    kubeseal \
      --controller-name=sealed-secrets-controller \  # 注意名称和命名空间
      --controller-namespace=kube-system \
      --format yaml > mysealedsecret.yaml
```

生成的文件如下：

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

1. 通过 kubeseal 生成的密文
2. 除此以外，还可以指定生成 secret 的模板，类似于 pod template

加密的数据采用的是 **非对称加密** 的方式，只有 controller 才能解密，因此可以放心的将加密后的数据存放在 Git 仓库中。

当 argocd 同步时，sealed controller 会根据 `SealedSecret` 去生成 secret。
最终生成的 secret 中的数据会被解密，因此当敏感信息发生变更后，仅需要更新 Git 仓库中的 `SealedSecret` 即可实现自动同步。
