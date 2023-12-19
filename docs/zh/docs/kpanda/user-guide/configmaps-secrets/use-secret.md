# 使用密钥

密钥是一种用于存储和管理密码、OAuth 令牌、SSH、TLS 凭据等敏感信息的资源对象。使用密钥意味着您不需要在应用程序代码中包含敏感的机密数据。

## 使用场景

您可以在 Pod 中使用密钥，有多种使用场景，主要包括：

- 作为容器的环境变量使用，提供容器运行过程中所需的一些必要信息。
- 使用密钥作为 Pod 的数据卷。
- 在 kubelet 拉取容器镜像时用作镜像仓库的身份认证凭证使用。

## 使用密钥设置容器的环境变量

您可以通过图形化界面或者终端命令行来使用密钥作为容器的环境变量。

!!! note

    密钥导入是将密钥作为环境变量的值；密钥键值导入是将密钥中某一参数作为环境变量的值。

### 图形界面操作

在通过镜像创建工作负载时，您可以在 __环境变量__ 界面通过选择 __密钥导入__ 或 __密钥键值导入__ 为容器设置环境变量。

1. 进入[镜像创建工作负载](../workloads/create-deployment.md)页面。

    ![创建 deployment](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/secret05.png)

2. 在 __容器配置__ 选择 __环境变量__ 配置，点击 __添加环境变量__ 按钮。

    ![添加环境变量](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/secret06.png)

3. 在环境变量类型处选择 __密钥导入__ 或 __密钥键值导入__ 。

    ![密钥导入](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/secret07.png)

    - 当环境变量类型选择为 __密钥导入__ 时，依次输入 __变量名__ 、 __前缀__ 、 __密钥__ 的名称。

    - 当环境变量类型选择为 __密钥键值导入__ 时，依次输入 __变量名__ 、 __密钥__ 、 __键__ 的名称。

### 命令行操作

如下例所示，您可以在创建工作负载时将密钥设置为环境变量，使用 __valueFrom__ 参数引用 Secret 中的 Key/Value。

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: secret-env-pod
spec:
  containers:
  - name: mycontainer
    image: redis
    env:
      - name: SECRET_USERNAME
        valueFrom:
          secretKeyRef:
            name: mysecret
            key: username
            optional: false # (1)
      - name: SECRET_PASSWORD
        valueFrom:
          secretKeyRef:
            name: mysecret
            key: password
            optional: false # (2)

```

1. 此值为默认值；意味着 "mysecret"，必须存在且包含名为 "username" 的主键
2. 此值为默认值；意味着 "mysecret"，必须存在且包含名为 "password" 的主键

## 使用密钥作为 Pod 的数据卷

### 图形界面操作

在通过镜像创建工作负载时，您可以通过在 __数据存储__ 界面选择存储类型为 __密钥__ ，将密钥作为容器的数据卷。

1. 进入[镜像创建工作负载](../workloads/create-deployment.md)页面。

    ![创建deployment](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/secret05.png)

2. 在 __容器配置__ 选择 __数据存储__ 配置，在 __节点路径映射__ 列表点击 __添加__ 按钮。

    ![创建deployment](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/secret08.png)

3. 在存储类型处选择 __密钥__ ，并依次输入 __容器路径__ 、 __子路径__ 等信息。

### 命令行操作

下面是一个通过数据卷来挂载名为 __mysecret__ 的 Secret 的 Pod 示例：

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: mypod
spec:
  containers:
  - name: mypod
    image: redis
    volumeMounts:
    - name: foo
      mountPath: "/etc/foo"
      readOnly: true
  volumes:
  - name: foo
    secret:
      secretName: mysecret
      optional: false # (1)
```

1. 默认设置，意味着 "mysecret" 必须已经存在

如果 Pod 中包含多个容器，则每个容器需要自己的 __volumeMounts__ 块，不过针对每个 Secret 而言，只需要一份 `.spec.volumes` 设置。

## 在 kubelet 拉取容器镜像时用作镜像仓库的身份认证凭证

您可以通过图形化界面或者终端命令行来使用密钥作为镜像仓库身份认证凭证。

### 图形化操作

在通过镜像创建工作负载时，您可以通过在 __数据存储__ 界面选择存储类型为 __密钥__ ，将密钥作为容器的数据卷。

1. 进入[镜像创建工作负载](../workloads/create-deployment.md)页面。

    ![创建deployment](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/secret05.png)

2. 在第二步 __容器配置__ 时选择 __基本信息__ 配置，点击 __选择镜像__ 按钮。

    ![选择镜像](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/secret09.png)

3. 在弹框的 __镜像仓库__ 下拉选择私有镜像仓库名称。关于私有镜像密钥创建请查看[创建密钥](create-secret.md)了解详情。

    ![选择镜像](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/secret10.png)

4. 输入私有仓库内的镜像名称，点击 __确定__ ，完成镜像选择。

!!! note

    创建密钥时，需要确保输入正确的镜像仓库地址、用户名称、密码并选择正确的镜像名称，否则将无法获取镜像仓库中的镜像。
