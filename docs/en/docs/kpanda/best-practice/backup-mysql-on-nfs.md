# Cross-Cluster Backup and Recovery of MySQL Application and Data

This demonstration will show how to use the application backup feature in DCE 5.0 to
perform cross-cluster backup migration for a stateful application.

!!! note

    The current operator should have admin privileges on the DCE 5.0 platform.

## Prepare the Demonstration Environment

### Prepare Two Clusters

 __main-cluster__ will be the source cluster for backup data, and __recovery-cluster__ will be the target cluster for data recovery.

| Cluster           | IP            | Nodes  |
| ----------------- | ------------- | ------ |
| main-cluster      | 10.6.175.100  | 1 node |
| recovery-cluster  | 10.6.175.110  | 1 node |

### Set Up MinIO Configuration

| MinIO Server Address     | Bucket      | Username | Password  |
| ------------------------| ----------- | ---------| ----------|
| http://10.7.209.110:9000 | mysql-demo  | root     | dangerous |

### Deploy NFS Storage Service in Both Clusters

!!! note

    NFS storage service needs to be deployed on **all nodes** in both the source and target clusters.

1. Install the dependencies required for NFS on all nodes in both clusters.

    ```yaml
    yum install nfs-utils iscsi-initiator-utils nfs-utils iscsi-initiator-utils nfs-utils iscsi-initiator-utils -y
    ```

    <details>
    <summary>Expected output</summary>
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
    </details>

2. Prepare NFS storage service for the MySQL application.

   Log in to any control node of both __main-cluster__ and __recovery-cluster__ .
   Use the command __vi nfs.yaml__ to create a file named __nfs.yaml__ on the node,
   and copy the following YAML content into the __nfs.yaml__ file.

    <details>
    <summary>nfs.yaml</summary>
    ```yaml
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

3. Run the __nfs.yaml__ file on the control nodes of both clusters.

    ```bash
    kubectl apply -f nfs.yaml
    ```

4. Check the status of the NFS Pod and wait for its status to become __running__ (approximately 2 minutes).

    ```bash
    kubectl get pod -n nfs-system -owide
    ```

    <details>
    <summary>Expected output</summary>
    ```bash
    [root@g-master1 ~]# kubectl get pod -owide
    NAME                               READY   STATUS    RESTARTS   AGE     IP              NODE        NOMINATED NODE   READINESS GATES
    nfs-provisioner-7dfb9bcc45-74ws2   1/1     Running   0          4m45s   10.6.175.100   g-master1   <none>           <none>
    ```
    </details>

### Deploy MySQL Application

1. Prepare a PVC (Persistent Volume Claim) based on NFS storage for the MySQL application to store its data.

    Use the command __vi pvc.yaml__ to create a file named __pvc.yaml__ on the node,
    and copy the following YAML content into the __pvc.yaml__ file.

    <details>
    <summary>pvc.yaml</summary>
    ```yaml
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

2. Run the __pvc.yaml__ file using the kubectl tool on the node.

    ```bash
    kubectl apply -f pvc.yaml
    ```

    <details>
    <summary>Expected output</summary>
    ```bash
    [root@g-master1 ~]# kubectl apply -f pvc.yaml
    persistentvolumeclaim/mydata created
    ```
    </details>

3. Deploy the MySQL application.

    Use the command __vi mysql.yaml__ to create a file named __mysql.yaml__ on the node,
    and copy the following YAML content into the __mysql.yaml__ file.

    <details>
    <summary>mysql.yaml</summary>
    ```yaml
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

4. Run the __mysql.yaml__ file using the kubectl tool on the node.

    ```bash
    kubectl apply -f mysql.yaml
    ```

    <details>
    <summary>Expected output</summary>
    ```bash
    [root@g-master1 ~]# kubectl apply -f mysql.yaml
    deployment.apps/mysql-deploy created
    ```
    </details>

5. Check the status of the MySQL Pod.

    Execute `kubectl get pod | grep mysql` to view the status of the MySQL Pod and wait for its status to become __running__ (approximately 2 minutes).

    <details>
    <summary>Expected output</summary>
    ```bash
    [root@g-master1 ~]# kubectl get pod |grep mysql
    mysql-deploy-5d6f94cb5c-gkrks      1/1     Running   0          2m53s
    ```
    </details>

    !!! note

        - If the MySQL Pod remains in a non-running state for a long time, it is usually because NFS dependencies are not installed on all nodes in the cluster.
        - Execute __kubectl describe pod ${mysql pod name}__ to view detailed information about the Pod.
        - If there is an error message like __MountVolume.SetUp failed for volume "pvc-4ad70cc6-df37-4253-b0c9-8cb86518ccf8" : mount failed: exit status 32__ , please delete the previous resources by executing __kubectl delete -f nfs.yaml/pvc.yaml/mysql.yaml__ and start from deploying the NFS service again.

6. Write data to the MySQL application.

    To verify the success of the data migration later, you can use a script to write test data to the MySQL application.

    1. Use the command __vi insert.sh__ to create a script named __insert.sh__ on the node,
       and copy the following content into the script.

        <details>
        <summary>insert.sh</summary>
        ```
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
        </details>

    2. Add permission to __insert.sh__ and run this script.

        ```bash
        [root@g-master1 ~]# chmod +x insert.sh
        [root@g-master1 ~]# ./insert.sh
        ```

        <details>
        <summary>Expected output</summary>
        ```
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
        </details>

    3. Press __Ctrl + C__ on the keyboard simultaneously to pause the script execution.

    4. Go to the MySQL Pod and check the data written in MySQL.

        ```bash
        kubectl exec deploy/mysql-deploy -- mysql -uroot -pdangerous -e "SELECT * FROM test.users;"
        ```

        <details>
        <summary>Expected output</summary>
        ```bash
        [root@g-master1 ~]# kubectl exec deploy/mysql-deploy -- mysql -uroot -pdangerous -e "SELECT * FROM test.users;"
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
        </details>

### Install Velero Plugin on Both Clusters

!!! note

    The velero plugin needs to be installed on **both the source and target clusters**.

Refer to the [Install Velero Plugin](../user-guide/backup/install-velero.md) documentation and the MinIO configuration below to install the velero plugin on the __main-cluster__ and __recovery-cluster__ .

| MinIO Server Address     | Bucket      | Username | Password  |
| ------------------------| ----------- | ---------| ----------|
| http://10.7.209.110:9000 | mysql-demo  | root     | dangerous |

!!! note

    When installing the plugin, replace S3url with the MinIO server address prepared for this demonstration, and replace the bucket with an existing bucket in MinIO.

## Backup MySQL Application and Data

1. Add a unique label, __backup=mysql__ , to the MySQL application and PVC data. This will facilitate resource selection during backup.

    ```
    kubectl label deploy mysql-deploy backup=mysql #为 __mysql-deploy__ 负载添加标签
    kubectl label pod mysql-deploy-5d6f94cb5c-gkrks backup=mysql #为 mysql pod 添加标签
    kubectl label pvc mydata backup=mysql #为 mysql 的 pvc 添加标签
    ```

2. Refer to the steps described in [Application Backup](../user-guide/backup/deployment.md#_3) and the parameters below to create an application backup.

   - Name: __backup-mysql__ (can be customized)
   - Source Cluster: __main-cluster__ 
   - Namespace: default
   - Resource Filter - Specify resource label: backup:mysql

   ![img](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/kpanda/images/mysql03.png)

3. After creating the backup plan, the page will automatically return to the backup plan list. Find the newly created backup plan __backup-mysq__ and click the more options button __...__ in the plan. Select "Run Now" to execute the newly created backup plan.

   ![img](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/kpanda/images/mysql05.png)

4. Wait for the backup plan execution to complete before proceeding with the next steps.

## Cross-Cluster Recovery of MySQL Application and Data

1. Log in to the DCE 5.0 platform and select __Container Management__ -> __Backup & Restore__ -> __Application Backup__ from the left navigation menu.

   ![img](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/kpanda/images/mysql06.png)

2. Select __Recovery__ in the left-side toolbar, then click __Restore Backup__ on the right side.

   ![img](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/kpanda/images/mysql07.png)

3. Fill in the parameters based on the following instructions:

   - Name: __restore-mysql__ (can be customized)
   - Backup Source Cluster: __main-cluster__ 
   - Backup Plan: __backup-mysql__ 
   - Backup Point: default
   - Recovery Target Cluster: __recovery-cluster__ 

   ![img](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/kpanda/images/mysql08.png)

4. Refresh the backup plan list and wait for the backup plan execution to complete.

## 验证数据是否成功恢复

1. 登录 __recovery-cluster__ 集群的控制节点，查看 __mysql-deploy__ 负载是否已经成功备份到当前集群。

    ```bash
    kubectl get pod
    ```

    Expected output如下：
    
    ```
    NAME                               READY   STATUS    RESTARTS   AGE
    mysql-deploy-5798f5d4b8-62k6c      1/1     Running   0          24h
    ```

2. Check if the data in MySQL datasheet is restored or not.

    ```bash
    kubectl exec deploy/mysql-deploy -- mysql -uroot -pdangerous -e "SELECT * FROM test.users;"
    ```

    Expected output如下：
    ```
    [root@g-master1 ~]# kubectl exec deploy/mysql-deploy -- mysql -uroot -pdangerous -e "SELECT * FROM test.users;"
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
    
        As you can see, the data in the Pod is consistent with the data inside the Pods in the __main-cluster__ .
        This indicates that the MySQL application and its data from the __main-cluster__ have been successfully
        recovered to the __recovery-cluster__ cluster.
