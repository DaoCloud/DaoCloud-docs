# 使用配置项

配置项（ConfigMap）是 Kubernetes 的一种 API 对象，用来将非机密性的数据保存到键值对中，可以存储其他对象所需要使用的配置。
使用时， 容器可以将其用作环境变量、命令行参数或者存储卷中的配置文件。通过使用配置项，能够将配置数据和应用程序代码分开，为应用配置的修改提供更加灵活的途径。

!!! note

    配置项并不提供保密或者加密功能。如果要存储的数据是机密的，请使用[密钥](use-secret.md)，或者使用其他第三方工具来保证数据的私密性，而不是用配置项。
    此外在容器里使用配置项时，容器和配置项必须处于同一集群的命名空间中。

## 使用场景

您可以在 Pod 中使用配置项，有多种使用场景，主要包括：

- 使用配置项设置容器的环境变量

- 使用配置项设置容器的命令行参数

- 使用配置项作为容器的数据卷

## 设置容器的环境变量

您可以通过图形化界面或者终端命令行来使用配置项作为容器的环境变量。

!!! note

    配置项导入是将配置项作为环境变量的值；配置项键值导入是将配置项中某一参数作为环境变量的值。

### 图形化界面操作

通过镜像创建工作负载时，可以在 __环境变量__ 界面通过选择 __配置项导入__ 或 __配置项键值导入__ 为容器设置环境变量。

1. 进入[镜像创建工作负载](../workloads/create-deployment.md)页面中，在 __容器配置__ 这一步中，选择 __环境变量__ 配置，点击 __添加环境变量__ 按钮。

    ![添加环境变量](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/config05.png)

2. 在环境变量类型处选择 __配置项导入__ 或 __配置项键值导入__ 。

    - 当环境变量类型选择为 __配置项导入__ 时，依次输入 __变量名__ 、 __前缀__ 名称、 __配置项__ 的名称。

    - 当环境变量类型选择为 __配置项键值导入__ 时，依次输入 __变量名__ 、 __配置项__ 名称、 __键__ 的名称。

### 命令行操作

您可以在创建工作负载时将配置项设置为环境变量，使用 valueFrom 参数引用 ConfigMap 中的 Key/Value。

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: configmap-pod-1
spec:
  containers:
    - name: test-container
      image: busybox
      command: [ "/bin/sh", "-c", "env" ]
      env:
        - name: SPECIAL_LEVEL_KEY
          valueFrom:                  # (1)!
            configMapKeyRef:
              name: kpanda-configmap  # (2)!
              key: SPECIAL_LEVEL      # (3)!
  restartPolicy: Never
```

1. 使用 __valueFrom__ 来指定 env 引用配置项的 value 值
2. 引用的配置文件名称
3. 引用的配置项 key

## 设置容器的命令行参数

您可以使用配置项设置容器中的命令或者参数值，使用环境变量替换语法 __$(VAR_NAME)__ 来进行。如下所示。

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: configmap-pod-3
spec:
  containers:
    - name: test-container
      image: busybox
      command: [ "/bin/sh", "-c", "echo $(SPECIAL_LEVEL_KEY) $(SPECIAL_TYPE_KEY)" ]
      env:
        - name: SPECIAL_LEVEL_KEY
          valueFrom:
            configMapKeyRef:
              name: kpanda-configmap
              key: SPECIAL_LEVEL
        - name: SPECIAL_TYPE_KEY
          valueFrom:
            configMapKeyRef:
              name: kpanda-configmap
              key: SPECIAL_TYPE
  restartPolicy: Never
```

这个 Pod 运行后，输出如下内容。

```none
Hello Kpanda
```

## 用作容器数据卷

您可以通过图形化界面或者终端命令行来使用配置项作为容器的环境变量。

### 图形化操作

在通过镜像创建工作负载时，您可以通过在 __数据存储__ 界面选择存储类型为 __配置项__ ，将配置项作为容器的数据卷。

1. 进入[镜像创建工作负载](../workloads/create-deployment.md)页面中，在 __容器配置__ 这一步中，选择 __数据存储__ 配置，在 __节点路径映射__ 列表点击 __添加__ 按钮。

    ![添加环境变量](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/config06.png)

2. 在存储类型处选择 __配置项__ ，并依次输入 __容器路径__ 、 __子路径__ 等信息。

### 命令行操作

要在一个 Pod 的存储卷中使用 ConfigMap。

下面是一个将 ConfigMap 以卷的形式进行挂载的 Pod 示例：

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
    configMap:
      name: myconfigmap
```

如果 Pod 中有多个容器，则每个容器都需要自己的 __volumeMounts__ 块，但针对每个 ConfigMap，您只需要设置一个 __spec.volumes__ 块。

!!! note

    将配置项作为容器挂载的数据卷时，配置项只能作为只读文件进行读取。
