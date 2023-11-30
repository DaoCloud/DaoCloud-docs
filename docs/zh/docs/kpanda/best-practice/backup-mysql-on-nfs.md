# MySQL 应用及数据的跨集群备份恢复

本次演示将基于 DCE 5.0 的应用备份功能，实现一个有状态应用的跨集群备份迁移。

!!! note

    当前操作者应具有 DCE 5.0 平台管理员的权限。

## 准备演示环境

### 准备两个集群

`main-cluster` 作为备份数据的源集群，`recovery-cluster` 集群作为需要恢复数据的目标集群。

| 集群             | IP           | 节点   |
| ---------------- | ------------ | ------ |
| main-cluster     | 10.6.175.100 | 1 节点 |
| recovery-cluster | 10.6.175.110 | 1 节点 |

### 搭建 MinIO 配置

| MinIO 服务器访问地址 | 存储桶 | 用户名 | 密码 |
| ------------------------ | ---------- | ---------- | -------- |
| http://10.7.209.110:9000 | mysql-demo | root       | dangerous |

### 在两个集群部署 NFS 存储服务

!!! note

    需要在 **源集群和目标集群** 上的所有节点上部署 NFS 存储服务。

1. 在两个集群中的所有节点安装 NFS 所需的依赖。

    ```yaml
    yum install nfs-utils iscsi-initiator-utils nfs-utils iscsi-initiator-utils nfs-utils iscsi-initiator-utils -y
    ```

    预期输出为：

    ```bash
    [root@g-master1 ~]# kubectl apply -f nfs.yaml
    clusterrole.rbac.authorization.k8s.io/nfs-provisioner-runner created
    clusterrolebinding.rbac.authorization.k8s.io/run-nfs-provisioner created
    role.rbac.authorization.k8s.io/leader-locking-nfs-provisioner created
    rolebinding.rbac.authorization.k8s.io/leader-locking-nfs-provisioner created
    serviceaccount/nfs-provisioner created
    service/nfs-provisioner created
    deployment.apps/nfs-provisioner created
    storageclass.storage.k8s.io/nfs created
    ```

2. 为 MySQL 应用准备 NFS 存储服务。

    登录 `main-cluster` 集群和 `recovery-cluster` 集群的任一控制节点，使用 `vi nfs.yaml` 命令在节点上创建一个 名为 `nfs.yaml` 的文件，将下面的 YAML 内容复制到 `nfs.yaml` 文件。

    <details>
    <summary>点击查看完整的 nfs.yaml</summary>
    ```yaml title="nfs.yaml"
    kind: ClusterRole
    apiVersion: rbac.authorization.k8s.io/v1
    metadata:
    name: nfs-provisioner-runner
    namespace: nfs-system
    rules:
    - apiGroups: [""]
        resources: ["persistentvolumes"]
        verbs: ["get", "list", "watch", "create", "delete"]
    - apiGroups: [""]
        resources: ["persistentvolumeclaims"]
        verbs: ["get", "list", "watch", "update"]
    - apiGroups: ["storage.k8s.io"]
        resources: ["storageclasses"]
        verbs: ["get", "list", "watch"]
    - apiGroups: [""]
        resources: ["events"]
        verbs: ["create", "update", "patch"]
    - apiGroups: [""]
        resources: ["services", "endpoints"]
        verbs: ["get"]
    - apiGroups: ["extensions"]
        resources: ["podsecuritypolicies"]
        resourceNames: ["nfs-provisioner"]
        verbs: ["use"]
    ---
    kind: ClusterRoleBinding
    apiVersion: rbac.authorization.k8s.io/v1
    metadata:
    name: run-nfs-provisioner
    subjects:
    - kind: ServiceAccount
        name: nfs-provisioner
        # replace with namespace where provisioner is deployed
        namespace: default
    roleRef:
    kind: ClusterRole
    name: nfs-provisioner-runner
    apiGroup: rbac.authorization.k8s.io
    ---
    kind: Role
    apiVersion: rbac.authorization.k8s.io/v1
    metadata:
    name: leader-locking-nfs-provisioner
    rules:
    - apiGroups: [""]
        resources: ["endpoints"]
        verbs: ["get", "list", "watch", "create", "update", "patch"]
    ---
    kind: RoleBinding
    apiVersion: rbac.authorization.k8s.io/v1
    metadata:
    name: leader-locking-nfs-provisioner
    subjects:
    - kind: ServiceAccount
        name: nfs-provisioner
        # replace with namespace where provisioner is deployed
        namespace: default
    roleRef:
    kind: Role
    name: leader-locking-nfs-provisioner
    apiGroup: rbac.authorization.k8s.io
    ---
    apiVersion: v1
    kind: ServiceAccount
    metadata:
    name: nfs-provisioner
    ---
    kind: Service
    apiVersion: v1
    metadata:
    name: nfs-provisioner
    labels:
        app: nfs-provisioner
    spec:
    ports:
        - name: nfs
        port: 2049
        - name: nfs-udp
        port: 2049
        protocol: UDP
        - name: nlockmgr
        port: 32803
        - name: nlockmgr-udp
        port: 32803
        protocol: UDP
        - name: mountd
        port: 20048
        - name: mountd-udp
        port: 20048
        protocol: UDP
        - name: rquotad
        port: 875
        - name: rquotad-udp
        port: 875
        protocol: UDP
        - name: rpcbind
        port: 111
        - name: rpcbind-udp
        port: 111
        protocol: UDP
        - name: statd
        port: 662
        - name: statd-udp
        port: 662
        protocol: UDP
    selector:
        app: nfs-provisioner
    ---
    kind: Deployment
    apiVersion: apps/v1
    metadata:
    name: nfs-provisioner
    spec:
    selector:
        matchLabels:
        app: nfs-provisioner
    replicas: 1
    strategy:
        type: Recreate
    template:
        metadata:
        labels:
            app: nfs-provisioner
        spec:
        serviceAccount: nfs-provisioner
        containers:
            - name: nfs-provisioner
            resources:
                limits:
                cpu: "1"
                memory: "4294967296"
            image: release.daocloud.io/velero/nfs-provisioner:v3.0.0
            ports:
                - name: nfs
                containerPort: 2049
                - name: nfs-udp
                containerPort: 2049
                protocol: UDP
                - name: nlockmgr
                containerPort: 32803
                - name: nlockmgr-udp
                containerPort: 32803
                protocol: UDP
                - name: mountd
                containerPort: 20048
                - name: mountd-udp
                containerPort: 20048
                protocol: UDP
                - name: rquotad
                containerPort: 875
                - name: rquotad-udp
                containerPort: 875
                protocol: UDP
                - name: rpcbind
                containerPort: 111
                - name: rpcbind-udp
                containerPort: 111
                protocol: UDP
                - name: statd
                containerPort: 662
                - name: statd-udp
                containerPort: 662
                protocol: UDP
            securityContext:
                capabilities:
                add:
                    - DAC_READ_SEARCH
                    - SYS_RESOURCE
            args:
                - "-provisioner=example.com/nfs"
            env:
                - name: POD_IP
                valueFrom:
                    fieldRef:
                    fieldPath: status.podIP
                - name: SERVICE_NAME
                value: nfs-provisioner
                - name: POD_NAMESPACE
                valueFrom:
                    fieldRef:
                    fieldPath: metadata.namespace
            imagePullPolicy: "IfNotPresent"
            volumeMounts:
                - name: export-volume
                mountPath: /export
        volumes:
            - name: export-volume
            hostPath:
                path: /data
    ---
    kind: StorageClass
    apiVersion: storage.k8s.io/v1
    metadata:
    name: nfs
    provisioner: example.com/nfs
    mountOptions:
    - vers=4.1
    ```
    </details>

3. 在两个集群的控制节点上执行 `nfs.yaml` 文件。

    ```bash
    kubectl apply -f nfs.yaml
    ```

4. 查看 NFS Pod 状态，等待其状态变为 `running`（大约需要 2 分钟）。

    ```bash
    kubectl get pod -n nfs-system -owide
    ```

    预期输出为：

    ```bash
    [root@g-master1 ~]# kubectl get pod -owide
    NAME                               READY   STATUS    RESTARTS   AGE     IP              NODE        NOMINATED NODE   READINESS GATES
    nfs-provisioner-7dfb9bcc45-74ws2   1/1     Running   0          4m45s   10.6.175.100   g-master1   <none>           <none>
    ```

### 部署 MySQL 应用

1. 为 MySQL 应用准备基于 NFS 存储的 PVC，用来存储 MySQL 服务内的数据。

    使用 `vi pvc.yaml` 命令在节点上创建名为 `pvc.yaml` 的文件，将下面的 YAML 内容复制到 `pvc.yaml` 文件内。

    ```yaml  title="pvc.yaml"
    apiVersion: v1
    kind: PersistentVolumeClaim
    metadata:
      name: mydata
      namespace: default
    spec:
      accessModes:
      - ReadWriteOnce
      resources:
        requests:
          storage: "1Gi"
      storageClassName: nfs
      volumeMode: Filesystem
    ```
    </details>

2. 在节点上使用 kubectl 工具执行 `pvc.yaml` 文件。

    ```bash
    kubectl apply -f pvc.yaml
    ```

    预期输出为：

    ```bash
    [root@g-master1 ~]# kubectl apply -f pvc.yaml
    persistentvolumeclaim/mydata created
    ```
    </details>

3. 部署 MySQL 应用。

    使用 `vi mysql.yaml` 命令在节点上创建名为 `mysql.yaml` 的文件，将下面的 YAML 内容复制到 `mysql.yaml` 文件。

    <details>
    <summary>点击查看完整的 mysql.yaml</summary>
    ```yaml title="nfs.yaml"
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      labels:
        app: mysql-deploy
      name: mysql-deploy
      namespace: default
    spec:
      progressDeadlineSeconds: 600
      replicas: 1
      revisionHistoryLimit: 10
      selector:
        matchLabels:
          app: mysql-deploy
      strategy:
        rollingUpdate:
          maxSurge: 25%
          maxUnavailable: 25%
        type: RollingUpdate
      template:
        metadata:
          creationTimestamp: null
          labels:
            app: mysql-deploy
          name: mysql-deploy
        spec:
          containers:
          - args:
            - --ignore-db-dir=lost+found
            env:
            - name: MYSQL_ROOT_PASSWORD
              value: dangerous
            image: release.daocloud.io/velero/mysql:5
            imagePullPolicy: IfNotPresent
            name: mysql-deploy
            ports:
            - containerPort: 3306
              protocol: TCP
            resources:
              limits:
                cpu: "1"
                memory: "4294967296"
            terminationMessagePath: /dev/termination-log
            terminationMessagePolicy: File
            volumeMounts:
            - mountPath: /var/lib/mysql
              name: data
          dnsPolicy: ClusterFirst
          restartPolicy: Always
          schedulerName: default-scheduler
          securityContext:
            fsGroup: 999
          terminationGracePeriodSeconds: 30
          volumes:
          - name: data
            persistentVolumeClaim:
              claimName: mydata
    ```
    </details>

4. 在节点上使用 kubectl 工具执行 `mysql.yaml` 文件。

    ```bash
    kubectl apply -f mysql.yaml
    ```

    预期输出为：

    ```bash
    [root@g-master1 ~]# kubectl apply -f mysql.yaml
    deployment.apps/mysql-deploy created
    ```

5. 查看 MySQL Pod 状态。

    执行 `kubectl get pod | grep mysql` 查看 MySQL Pod 状态，等待其状态变为 `running`（大约需要 2 分钟）。

    预期输出为：

    ```bash
    [root@g-master1 ~]# kubectl get pod |grep mysql
    mysql-deploy-5d6f94cb5c-gkrks      1/1     Running   0          2m53s
    ```

    !!! note
        
        - 如果  MySQL Pod 状态长期处于非 running 状态，通常是因为没有在集群的所有节点上安装 NFS 依赖。
        - 执行 `kubectl describe pod ${mysql pod 名称}` 查看 Pod 的详细信息。
        - 如果报错中有 `MountVolume.SetUp failed for volume "pvc-4ad70cc6-df37-4253-b0c9-8cb86518ccf8" : mount failed: exit status 32`
          之类的信息，请分别执行 `kubectl delete -f nfs.yaml/pvc.yaml/mysql.yaml` 删除之前的资源后，重新从部署 NFS 服务开始。

6. 向 MySQL 应用写入数据。

    为了便于后期验证迁移数据是否成功，可以使用脚本向 MySQL 应用中写入测试数据。

    1. 使用 `vi insert.sh` 命令在节点上创建名为 `insert.sh` 的脚本，将下面的 YAML 内容复制到该脚本。

        ```shell title="insert.sh"
        #!/bin/bash

        function rand(){
            min=$1
            max=$(($2-$min+1))
            num=$(date +%s%N)
            echo $(($num%$max+$min))
        }

        function insert(){
            user=$(date +%s%N | md5sum | cut -c 1-9)
            age=$(rand 1 100)

            sql="INSERT INTO test.users(user_name, age)VALUES('${user}', ${age});"
            echo -e ${sql}

            kubectl exec deploy/mysql-deploy -- mysql -uroot -pdangerous -e "${sql}"

        }

        kubectl exec deploy/mysql-deploy -- mysql -uroot -pdangerous -e "CREATE DATABASE IF NOT EXISTS test;"
        kubectl exec deploy/mysql-deploy -- mysql -uroot -pdangerous -e "CREATE TABLE IF NOT EXISTS test.users(user_name VARCHAR(10) NOT NULL,age INT UNSIGNED)ENGINE=InnoDB DEFAULT CHARSET=utf8;"

        while true;do
            insert
            sleep 1
        done
        ```

    2. 为 `insert.sh` 脚本添加权限并运行该脚本。

        ```bash
        [root@g-master1 ~]# chmod +x insert.sh
        [root@g-master1 ~]# ./insert.sh
        ```

        预期输出为：

        ```console
        mysql: [Warning] Using a password on the command line interface can be insecure.
        mysql: [Warning] Using a password on the command line interface can be insecure.
        INSERT INTO test.users(user_name, age)VALUES('dc09195ba', 10);
        mysql: [Warning] Using a password on the command line interface can be insecure.
        INSERT INTO test.users(user_name, age)VALUES('80ab6aa28', 70);
        mysql: [Warning] Using a password on the command line interface can be insecure.
        INSERT INTO test.users(user_name, age)VALUES('f488e3d46', 23);
        mysql: [Warning] Using a password on the command line interface can be insecure.
        INSERT INTO test.users(user_name, age)VALUES('e6098695c', 93);
        mysql: [Warning] Using a password on the command line interface can be insecure.
        INSERT INTO test.users(user_name, age)VALUES('eda563e7d', 63);
        mysql: [Warning] Using a password on the command line interface can be insecure.
        INSERT INTO test.users(user_name, age)VALUES('a4d1b8d68', 17);
        mysql: [Warning] Using a password on the command line interface can be insecure.
        ```

    3. 在键盘上同时按下 `control` 和 `c` 暂停脚本的执行。

    4. 前往 MySQL Pod 查看 MySQL 中写入的数据。

        ```bash
        kubectl exec deploy/mysql-deploy -- mysql -uroot -pdangerous -e "SELECT * FROM test.users;"
        ```

        预期输出为：

        ```console
        mysql: [Warning] Using a password on the command line interface can be insecure.
        user_name	age
        dc09195ba	10
        80ab6aa28	70
        f488e3d46	23
        e6098695c	93
        eda563e7d	63
        a4d1b8d68	17
        ea47546d9	86
        a34311f2e	47
        740cefe17	33
        ede85ea28	65
        b6d0d6a0e	46
        f0eb38e50	44
        c9d2f28f5	72
        8ddaafc6f	31
        3ae078d0e	23
        6e041631e	96
        ```

### 在两个集群安装 velero 插件

!!! note

    需要在 **源集群和目标集群** 上均安装 velero 插件。

参考[安装 velero 插件](../user-guide/backup/install-velero.md)文档和下方的 MinIO 配置，在 `main-cluster` 集群和 `recovery-cluster` 集群上安装 velero 插件。

| minio 服务器访问地址     | 存储桶     | 用户名 | 密码      |
| ------------------------ | ---------- | ------ | --------- |
| `http://10.7.209.110:9000` | mysql-demo | root   | dangerous |

!!! note

    安装插件时需要将 S3url 替换为此次演示准备的 MinIO 服务器访问地址，存储桶替换为 MinIO 中真实存在的存储桶。

## 备份 MySQL 应用及数据

1. 为 MySQL 应用及 PVC 数据添加独有的标签：`backup=mysql`，便于备份时选择资源。

    ```bash
    kubectl label deploy mysql-deploy backup=mysql # 为 `mysql-deploy` 负载添加标签
    kubectl label pod mysql-deploy-5d6f94cb5c-gkrks backup=mysql # 为 mysql pod 添加标签
    kubectl label pvc mydata backup=mysql # 为 mysql 的 pvc 添加标签
    ```

2. 参考[应用备份](../user-guide/backup/deployment.md#_3)中介绍的步骤，以及下方的参数创建应用备份。

    - 名称：`backup-mysql`（可以自定义）
    - 源集群： `main-cluster`
    - 命名空间：default
    - 资源过滤-指定资源标签：backup:mysql

    ![img](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/kpanda/images/mysql03.png)

3. 创建好备份计划之后页面会自动返回备份计划列表，找到新建的备份计划 `backup-mysq`，在计划点击更多操作按钮 `...` 选择 `立即执行` 执行新建的备份计划。

    ![img](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/kpanda/images/mysql05.png)

4. 等待备份计划执行完成后，即可执行后续操作。

## 跨集群恢复 MySQL 应用及数据

1. 登录 DCE 5.0 平台，在左侧导航选择`容器管理` -> `备份恢复` -> `应用备份`。

    ![img](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/kpanda/images/mysql06.png)

2. 在左侧功能栏选择 `恢复`，然后在右侧点击 `恢复备份`。

    ![img](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/kpanda/images/mysql07.png)

3. 查看以下说明填写参数：
  
    - 名称：`restore-mysql`（可以自定义）
    - 备份源集群：`main-cluster`
    - 备份计划：`backup-mysql`
    - 备份点：default
    - 恢复目标集群：`recovery-cluster`

    ![img](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/kpanda/images/mysql08.png)
  
4. 刷新备份计划列表，等待备份计划执行完成。

## 验证数据是否成功恢复

1. 登录 `recovery-cluster` 集群的控制节点，查看 `mysql-deploy` 负载是否已经成功备份到当前集群。

    ```bash
    kubectl get pod
    ```

    预期输出如下：
    
    ```
    NAME                               READY   STATUS    RESTARTS   AGE
    mysql-deploy-5798f5d4b8-62k6c      1/1     Running   0          24h
    ```

2. 检查 MySQL 数据表中的数据是否恢复成功。

    ```bash
    kubectl exec deploy/mysql-deploy -- mysql -uroot -pdangerous -e "SELECT * FROM test.users;"
    ```

    预期输出如下：

    ```console
    mysql: [Warning] Using a password on the command line interface can be insecure.
    user_name	age
    dc09195ba	10
    80ab6aa28	70
    f488e3d46	23
    e6098695c	93
    eda563e7d	63
    a4d1b8d68	17
    ea47546d9	86
    a34311f2e	47
    740cefe17	33
    ede85ea28	65
    b6d0d6a0e	46
    f0eb38e50	44
    c9d2f28f5	72
    8ddaafc6f	31
    3ae078d0e	23
    6e041631e	96
    ```

    !!! success
    
        可以看到，Pod 中的数据和 `main-cluster` 集群中 Pod 里面的数据一致。这说明已经成功地将 `main-cluster` 中的 MySQL 应用及其数据跨集群恢复到了 `recovery-cluster` 集群。
