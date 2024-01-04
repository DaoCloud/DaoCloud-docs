# 云原生混沌工程--Chaos Mesh 实战篇

![chaos mesh](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/blogs/images/chaos01.png)

通过《[云原生混沌工程 -- Chaos Mesh 总览篇](https://mp.weixin.qq.com/s?__biz=MzA5NTUxNzE4MQ==&mid=2659279670&idx=1&sn=67d4d3c542de5e913531ef87731d7a49&scene=21#wechat_redirect)》和《[云原生混沌工程 -- Chaos Mesh 控制器篇](https://mp.weixin.qq.com/s?__biz=MzA5NTUxNzE4MQ==&mid=2659279798&idx=1&sn=646474b92d16c211816205107a6e3c7a&scene=21#wechat_redirect)》这两篇文章的介绍，可以大概了解 Chaos Mesh 在做什么样的事情以及基本的工作原理。接下来，从安装和使用 Chaos Mesh 的角度，来具体介绍一下 Chaos Mesh 的能力。

## 存储

1. 安装 nfs sevrer：

    ```bash
    sudo dnf install nfs-utils
    sudo systemctl enable --now nfs-server
    ```

2. 创建 nfs server 的导出的文件系统：

    ```bash
    sudo mkdir -p /srv/nfs4/k8s
    ```

3. 挂载实际的目录：

    ```bash
    sudo mkdir /opt/k8s
    sudo mount --bind /opt/k8s /srv/nfs4/k8s
    ```

4. 想要这个挂载持久化，添加下面的条目到 /etc/fstab 文件，以下是编辑完的结果：

    ```bash
    cat /etc/fstab
    ```

    ```
    /opt/k8s /srv/nfs4/k8s none bind 0 0
    ```

5. 导出文件系统，以下是编辑完的结果：

    ```bash
    cat /etc/exports
    ```

    ```
    /srv/nfs4 10.1.3.0/24(rw,sync,no_root_squash,no_subtree_check,crossmnt,fsid=0)
    /srv/nfs4/k8s 10.1.3.0/24(rw,sync,no_root_squash,no_subtree_check)
    ```

    ```bash
    sudo exportfs -ra
    ```

6. 查看倒出来的文件系统：

    ```bash
    sudo exportfs -v
    ```

7. 安装 Helm

    ```bash
    wget https://get.helm.sh/helm-v3.8.1-linux-amd64.tar.gz
    tar -zxvf helm-v3.8.1-linux-amd64.tar.gz
    mv linux-amd64/helm /usr/local/bin/helm
    ```

    安装 nfs-subdir-external-provisioner

    ```bash
    helm repo add nfs-subdir-external-provisioner https://kubernetes-sigs.github.io/nfs-subdir-external-provisioner/
    helm install nfs-subdir-external-provisioner nfs-subdir-external-provisioner/nfs-subdir-external-provisioner --set nfs.server=10.1.3.210 --set nfs.path=/k8s --set image.repository=k8s.m.daocloud.io/sig-storage/nfs-subdir-external-provisioner --set image.tag=v4.0.2 --set storageClass.defaultClass=true
    ```

## 数据库

1. 准备 pvc mysqlpvc.yaml

    ```yaml
    apiVersion: v1
    kind: PersistentVolumeClaim
    metadata:
      name: mysql-pv-claim
      labels:
        app: mysql
    spec:
      accessModes:
        - ReadWriteOnce
      resources:
        requests:
        storage: 20Gi
    ```

    ```bash
    kubectl apply -f mysqlpvc.yaml
    ```

2. 安装 mysql mysql.yaml

    ```yaml
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: mysql-deployment
    spec:
      selector:
        matchLabels:
        app: mysql
      template:
        metadata:
          labels:
            app: mysql
        spec:
          containers:
            - image: mysql:5.6
            name: mysql-con
            env:
              - name: MYSQL_ROOT_PASSWORD
                value: dangerous
            ports:
              - containerPort: 3306
                name: mysql
            volumeMounts:
              - name: mysql-persistent-storage
                mountPath: /var/lib/mysql
        volumes:
          - name: mysql-persistent-storage
            persistentVolumeClaim:
              claimName: mysql-pv-claim
    ---
    apiVersion: v1
    kind: Service
    metadata:
      name: mysql-service
      labels:
        app: mysql
    spec:
      type: NodePort
      selector:
        app: mysql
      ports:
        - protocol: TCP
        port: 3306
        targetPort: 3306
    ```

    ```bash
    kubectl apply -f mysql.yaml
    ```

3. 检查 mysql 的安装

    ```bash
    kubectl get pvc|grep mysql-pv-claim
    ```

    ```
    mysql-pv-claim            Bound    pvc-c64c8f7b-0408-49e2-953e-09d36003a3d8   20Gi       RWO            nfs-client     6d3h
    ```

    ```bash
    kubectl get pods|grep mysql-deployment
    ```

    ```
    mysql-deployment-68bd7964d7-x9c8h                  1/1     Running   0          6d3h
    ```

4. 连接数据库

    ```bash
    kubectl run my-release-mysql-client --rm --tty -i --restart='Never' --image  docker.io/bitnami/mysql:8.0.32-debian-11-r8 --namespace default --env MYSQL_ROOT_PASSWORD=dangerous --command -- bash
    kubectl exec -it my-release-mysql-client bash
    mysql -h 10.1.3.210 -P32265 -uroot -pdangerous
    ```

## 安装 Chaos Mesh

```bash
kubectl create ns chaos-mesh
helm repo add chaos-mesh https://charts.chaos-mesh.org
helm install chaos-mesh chaos-mesh/chaos-mesh -n=chaos-mesh --set chaosDaemon.runtime=containerd --set chaosDaemon.socketPath=/run/containerd/containerd.sock --set controllerManager.leaderElection.enabled=false --set controllerManager.replicaCount=1 --set dashboard.env.DATABASE_DRIVER=mysql --set dashboard.env.DATABASE_DATASOURCE=root:dangerous@tcp'(10.1.3.210:32265)'/chaosmesh?parseTime=true
```

## 检查 Chaos Mesh

```bash
kubectl get po -n chaos-mesh
```

```
NAME                                        READY   STATUS    RESTARTS   AGE
chaos-controller-manager-77558f4c96-zv8s4   1/1     Running   0          5d
chaos-daemon-2nm9v                          1/1     Running   0          6d2h
chaos-daemon-mrvh6                          1/1     Running   0          6d2h
chaos-dashboard-544c89d476-d29kt            1/1     Running   0          6d2h
```

## 使用 Chaos Mesh

### 准备

部署一个 nginx 容器用于测试使用。

```bash
helm repo add my-repo https://charts.bitnami.com/bitnami
helm install nginx --set service.type=NodePort my-repo/nginx
```

### 登录

- 输入令牌登录：

    ![input token](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/blogs/images/chaos02.png)

- 点击 link 来打开令牌的辅助生成器：

    ![input token](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/blogs/images/chaos03.png)

- 复制授权的 yaml，进行授权，并生成登录的 token，之后使用 ServiceAccount 的 name 和生成的 token 登录：

    ```bash
    vi rbac.yaml
    ```

    ```yaml
    kind: ServiceAccount
    apiVersion: v1
    metadata:
      namespace: default
      name: account-default-viewer-xfddq

    ---
    kind: Role
    apiVersion: rbac.authorization.k8s.io/v1
    metadata:
      namespace: default
      name: role-default-viewer-xfddq
    rules:
    - apiGroups: [""]
      resources: ["pods", "namespaces"]
      verbs: ["get", "watch", "list"]
    - apiGroups: ["chaos-mesh.org"]
      resources: ["*"]
      verbs: ["get", "list", "watch"]

    ---
    apiVersion: rbac.authorization.k8s.io/v1
    kind: RoleBinding
    metadata:
      name: bind-default-viewer-xfddq
      namespace: default
    subjects:
    - kind: ServiceAccount
      name: account-default-viewer-xfddq
      namespace: default
    roleRef:
      kind: Role
      name: role-default-viewer-xfddq
      apiGroup: rbac.authorization.k8s.io
    ```

    ```bash
    kubectl apply -f rbac.yaml
    kubectl create token account-default-viewer-xfddq
    ```

    ```none
    eyJhbGciOiJSUzI1NiIsImtpZCI6IjZjbVpnWEpzNWxrNHdDNXBZWGZaYlItYldqVzRDR1RRcnozVS1Oc0pGVk0ifQ.eyJhdWQiOlsiaHR0cHM6Ly9rdWJlcm5ldGVzLmRlZmF1bHQuc3ZjLmNsdXN0ZXIubG9jYWwiXSwiZXhwIjoxNjc3ODM4MzQ0LCJpYXQiOjE2Nzc4MzQ3NDQsImlzcyI6Imh0dHBzOi8va3ViZXJuZXRlcy5kZWZhdWx0LnN2Yy5jbHVzdGVyLmxvY2FsIiwia3ViZXJuZXRlcy5pbyI6eyJuYW1lc3BhY2UiOiJkZWZhdWx0Iiwic2VydmljZWFjY291bnQiOnsibmFtZSI6ImFjY291bnQtZGVmYXVsdC1tYW5hZ2VyLXR5eHB4IiwidWlkIjoiY2VlOWQ5OTItMjEwYy00NWRjLTk2ODQtMjUwYTdlZTdlMTk2In19LCJuYmYiOjE2Nzc4MzQ3NDQsInN1YiI6InN5c3RlbTpzZXJ2aWNlYWNjb3VudDpkZWZhdWx0OmFjY291bnQtZGVmYXVsdC1tYW5hZ2VyLXR5eHB4In0.ffnSlmHHfewt8B5ErxIxMRbvk8gloKjazF3ocD9jFkqHMcNedqLo1XZSTE7lDlbdKgKJept6Vq03R4GusW5doKqC51laIwh-aWLFYL_lJZ-wAOenU5-HLM_L3SgFSYIuSCwraLfwcatLuzqtkOT_hO8IMoGYLEJQghw6iHlogXf-Z6ckPGt6VGsP6bU40Xaz2EVQw76qJwg2HpkAEbx-ucF6lID_J9Pg5pVsMBW75lgYy3FgITOPXKh85kIm15VqopvNJCRMRHjg-5RcoLBbhIhBVuU9FBwVRqt0TwVXX2CH-f6H8LUlMcDDbrHjBntnOfiBO4r1dru2X38rujRpVg
    ```

- 使用 account-default-viewer-xfddq 作为名称，生成出来的 token 作为令牌，就可以登录到对应 namespace。
  支持 namespace 和 cluster 范围的令牌申请。

### 仪表盘

![dashboard](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/blogs/images/chaos04.png)

### 实验

以 PodChaos 为例，创建一个 Chaos 类型的实验，完成删除 Pod 的故障注入。

- 定义：

    ```yaml
    apiVersion: chaos-mesh.org/v1alpha1
    kind: PodChaos
    metadata:
      name: pod-kill-example2
      namespace: default
    spec:
      action: pod-kill
      mode: one
      selector:
        namespaces:
          - default
        labelSelectors:
          "app.kubernetes.io/instance": "nginx"
    ```

- 列表：

    ![list](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/blogs/images/chaos05.png)

- 创建：

    ![create](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/blogs/images/chaos06.png)

- 详情：其中包含元数据，完整的 yaml 定义，以及对应的事件。同时 可以将其进行归档，归档完之后就只能在归档的菜单中可以查看到，
  因为对应的资源对象已经从 Kubernetes 中删除了，只保存在了数据中。

    ![details](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/blogs/images/chaos07.png)

### 计划

定义一个在每小时的 05 分会定时执行的计划，计划中的任务是删除选中的 nginx 的 Pod。

- 定义：

    ```yaml
    apiVersion: chaos-mesh.org/v1alpha1
    kind: Schedule
    metadata:
      name: schedule-delay-example
      namespace: default
    spec:
      schedule: "5 * * * *"
      historyLimit: 2
      concurrencyPolicy: Allow
      type: "PodChaos"
      podChaos:
        action: "pod-kill"
        mode: one
        selector:
          namespaces:
            - default
        labelSelectors:
            "app.kubernetes.io/instance": "nginx"
    ```

- 列表：

    ![list](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/blogs/images/chaos08.png)

- 创建：

    ![create](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/blogs/images/chaos09.png)

- 详情：其中包含元数据，完整的 yaml 定义，以及对应的事件。同时 可以将其进行归档，归档完之后就只能在归档的菜单中可以查看到，
  因为对应的资源对象已经从 Kubernetes 中删除了，只保存在了数据中。

    ![details](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/blogs/images/chaos10.png)

### 工作流

定义一个工作流，包含入口节点 the-entry 和 Chaos 类型的节点 workflow-pod-chaos。

- 定义：

    ```yaml
    apiVersion: chaos-mesh.org/v1alpha1
    kind: Workflow
    metadata:
      name: try-workflow-parallel
    spec:
      entry: the-entry
      templates:
        - name: the-entry
        templateType: Parallel
        deadline: 240s
        children:
          - workflow-pod-chaos
        - name: workflow-pod-chaos
        templateType: PodChaos
        deadline: 20s
        podChaos:
            action: pod-kill
            mode: one
            selector:
            namespaces:
                - default
            labelSelectors:
                "app.kubernetes.io/instance": "nginx"
    ```

- 列表：

    ![list](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/blogs/images/chaos11.png)

- 创建：

    ![create](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/blogs/images/chaos12.png)

    为了快速创建去看效果，直接通过 kubectl 命令行 apply 的方式创建 Workflow 资源对象，页面操作会慢一点。

- 详情：其中包含工作流运行的拓扑情况，完整的 yaml 定义，以及对应的事件。同时 可以将其进行归档，归档完之后就只能在归档的菜单中可以查看到，因为对应的资源对象已经从 Kubernetes 中删除了，只保存在了数据中。以及在工作流运行完成之后，在过程中创建的 Chaos 类型的资源对象也会被自动删除掉。

    ![details](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/blogs/images/chaos13.png)

### 事件

这里汇聚了所有资源对象相关的事件，可以进行查询操作。这些事件数据是从数据库中查出来的，之前的文章提到过数据库中事件数据的来源的原理。同时，支持可以设置事件数据的过期时间，一旦到达过期时间，就会将其从数据库中删除掉。

![details](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/blogs/images/chaos14.png)

### 归档

当在页面上对相关资源对象点击归档，或者是从底层 Kubernetes 直接删除资源对象，都是可以将其变成归档状态，归档的数据是保存在数据库中的。归档完的数据就会在这里进行展示，同时可以设置归档数据的过期时间，一旦到达过期时间，就会将其从数据库中删除掉。

- 列表：

    ![list](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/blogs/images/chaos15.png)

- 详情：已经归档的实验，计划，工作流对象是不能查看详情了，原因是归档的资源对象在 Kubernetes 中已经不存在了。

    ![details](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/blogs/images/chaos16.png)

### 设置

主要包含登录/登出，主题色彩，中英文设置，还有一些其它的设置开关。

![setting](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/blogs/images/chaos17.png)

### StatusCheck

在目前的版本中，页面上还不支持显示 StatusCheck 的类型，这里以命令行的方式来展示 Continuous 和 Synchronous 两种方式的 StatusCheck 的使用。

- Continuous 类型：

    ```yaml
    apiVersion: chaos-mesh.org/v1alpha1
    kind: StatusCheck
    metadata:
      name: status-check-example
    spec:
      mode: Continuous
      type: HTTP
      intervalSeconds: 30
      timeoutSeconds: 5
      successThreshold: 1
      failureThreshold: 3
      http:
        url: http://10.1.3.210:30028
        method: GET
        criteria:
          statusCode: "200"
    ```

    检查状态：

    ```bash
    kubectl describe StatusCheck status-check-example
    ```

    ```yaml
    Name:         status-check-example
    Namespace:    default
    Labels:       <none>
    Annotations:  <none>
    API Version:  chaos-mesh.org/v1alpha1
    Kind:         StatusCheck
    Metadata:
      Creation Timestamp:  2023-03-05T09:20:57Z
      Generation:          1
      ......
    Spec:
      Failure Threshold:  3
      Http:
        Criteria:
          Status Code:        200
        Method:               GET
        URL:                  http://10.1.3.210:30029
      Interval Seconds:       30
      Mode:                   Continuous
      Records History Limit:  100
      Success Threshold:      1
      Timeout Seconds:        5
      Type:                   HTTP
    Status:
      Conditions:
        Last Probe Time:       2023-03-05T09:22:23Z
        Last Transition Time:  2023-03-05T09:21:23Z
        Reason:
        Status:                True
        Type:                  SuccessThresholdExceed
        Last Probe Time:       2023-03-05T09:22:23Z
        Last Transition Time:  2023-03-05T09:20:53Z
        Reason:
        Status:                False
        Type:                  Completed
        Last Probe Time:       2023-03-05T09:22:23Z
        Last Transition Time:  2023-03-05T09:20:53Z
        Reason:
        Status:                False
        Type:                  DurationExceed
        Last Probe Time:       2023-03-05T09:22:23Z
        Last Transition Time:  2023-03-05T09:20:53Z
        Reason:
        Status:                False
        Type:                  FailureThresholdExceed
      Count:                   3
      Records:
        Outcome:     Success
        Start Time:  2023-03-05T09:21:23Z
        Outcome:     Success
        Start Time:  2023-03-05T09:21:53Z
        Outcome:     Success
        Start Time:  2023-03-05T09:22:23Z
      Start Time:    2023-03-05T09:20:53Z
    Events:
      Type    Reason                             Age   From         Message
      ----    ------                             ----  ----         -------
      Normal  StatusCheckExecutionSucceed        69s   statuscheck  HTTP execution of status check succeed
      Normal  StatusCheckSuccessThresholdExceed  69s   statuscheck  success threshold exceed
      Normal  StatusCheckSuccessThresholdExceed  69s   statuscheck  success threshold exceed
      Normal  StatusCheckSuccessThresholdExceed  69s   statuscheck  success threshold exceed
      Normal  StatusCheckExecutionSucceed        39s   statuscheck  HTTP execution of status check succeed
      Normal  StatusCheckSuccessThresholdExceed  39s   statuscheck  success threshold exceed
      Normal  StatusCheckSuccessThresholdExceed  39s   statuscheck  success threshold exceed
      Normal  StatusCheckSuccessThresholdExceed  39s   statuscheck  success threshold exceed
      Normal  StatusCheckSuccessThresholdExceed  39s   statuscheck  success threshold exceed
      Normal  StatusCheckExecutionSucceed        9s    statuscheck  HTTP execution of status check succeed
      Normal  StatusCheckSuccessThresholdExceed  9s    statuscheck  success threshold exceed
      Normal  StatusCheckSuccessThresholdExceed  9s    statuscheck  success threshold exceed
    ```

- Synchronous 类型：

    ```yaml
    apiVersion: chaos-mesh.org/v1alpha1
    kind: StatusCheck
    metadata:
      name: status-check-example
    spec:
      mode: Synchronous
      type: HTTP
      intervalSeconds: 30
      timeoutSeconds: 5
      successThreshold: 1
      failureThreshold: 3
      http:
        url: http://10.1.3.210:30028
        method: GET
        criteria:
          statusCode: "200"
    ```

    检查状态：

    ```bash
    kubectl describe StatusCheck status-check-example
    ```

    ```yaml
    Name:         status-check-example
    Namespace:    default
    Labels:       <none>
    Annotations:  <none>
    API Version:  chaos-mesh.org/v1alpha1
    Kind:         StatusCheck
    Metadata:
      Creation Timestamp:  2023-03-05T09:25:15Z
      ......
    Spec:
      Failure Threshold:  3
      Http:
        Criteria:
          Status Code:        200
        Method:               GET
        URL:                  http://10.1.3.210:30029
      Interval Seconds:       30
      Mode:                   Synchronous
      Records History Limit:  100
      Success Threshold:      1
      Timeout Seconds:        5
      Type:                   HTTP
    Status:
      Completion Time:  2023-03-05T09:25:53Z
      Conditions:
        Last Probe Time:       2023-03-05T09:25:53Z
        Last Transition Time:  2023-03-05T09:25:53Z
        Reason:                StatusCheckSuccessThresholdExceed
        Status:                True
        Type:                  Completed
        Last Probe Time:       2023-03-05T09:25:53Z
        Last Transition Time:  2023-03-05T09:25:12Z
        Reason:
        Status:                False
        Type:                  DurationExceed
        Last Probe Time:       2023-03-05T09:25:53Z
        Last Transition Time:  2023-03-05T09:25:12Z
        Reason:
        Status:                False
        Type:                  FailureThresholdExceed
        Last Probe Time:       2023-03-05T09:25:53Z
        Last Transition Time:  2023-03-05T09:25:53Z
        Reason:
        Status:                True
        Type:                  SuccessThresholdExceed
      Count:                   1
      Records:
        Outcome:     Success
        Start Time:  2023-03-05T09:25:42Z
      Start Time:    2023-03-05T09:25:12Z
    Events:
      Type    Reason                             Age    From         Message
      ----    ------                             ----   ----         -------
      Normal  StatusCheckExecutionSucceed        4m40s  statuscheck  HTTP execution of status check succeed
      Normal  StatusCheckCompleted               4m29s  statuscheck  status check completed: StatusCheckSuccessThresholdExceed
      Normal  StatusCheckSuccessThresholdExceed  4m29s  statuscheck  success threshold exceed
    ```

## 总结

经过安装和实践，可以更好地理解使用 Chaos Mesh 的一些方式。这里只是举了一些例子帮助理解，对于其它更多的使用方式可以参考官方的文档。

Chaos Mesh 简介：
<https://chaos-mesh.org/zh/docs/>

作者：熊先生
