# etcd Backup Restore

Using the ETCD backup feature to create a backup policy, you can back up the etcd data of a specified cluster to S3 storage on a scheduled basis. This page focuses on how to restore the data that has been backed up to the current cluster.

!!! note

    - DCE 5.0 ETCD backup restores are limited to backups and restores for the same cluster (with no change in the number of nodes and IP addresses). For example, after the etcd data of Cluster A is backed up, the backup data can only be restored to Cluster A, not to Cluster B.
    - The feature is recommended [app backup and restore](../user-guide/backup/deployment.md) for cross-cluster backups and restores.
    - First, create a backup strategy to back up the current status. It is recommended to refer to the [ETCD 备份](../user-guide/backup/etcd-backup.md) function.

The following is a specific case to illustrate the whole process of backup and restore.

## Environmental Information

Begin with basic information about the target cluster and S3 storage for the restore. Here, MinIo is used as S3 storage, and the whole cluster has 3 control planes (3 etcd copies).

|IP|Host|Role|Remarks|
|--|--|--|--|
|10.6.212.10|host01|k8s-master01|k8s node 1|
|10.6.212.11|host02|k8s-master02|k8s node 2|
|10.6.212.12|host03|k8s-master03|k8s node 3|
|10.6.212.13|host04|minio|minio service|

## Prerequisites

### Install the etcdbrctl tool

To implement ETCD data backup and restore, you need to install the etcdbrctl open source tool on any of the above k8s nodes. This tool does not have binary files for the time being and needs to be compiled by itself. Please refer to the compilation mode: <https://github.com/gardener/etcd-backup-restore/blob/master/doc/development/local_setup.md#build>.

After installation, use the following command to check whether the tool is available:

```shell
etcdbrctl -v
```

The expected output is as follows:

```none
INFO[0000] etcd-backup-restore Version: v0.23.0-dev
INFO[0000] Git SHA: b980beec
INFO[0000] Go Version: go1.19.3
INFO[0000] Go OS/Arch: linux/amd64
```

### Check the backup data

You need to check the following before restoring:

- Have you successfully backed up your data in DCE 5.0
- Check if backup data exists in S3 storage

!!! note

    The backup of DCE 5.0 is a full data backup, and the full data of the last backup will be restored when restoring.

### Shut down the cluster

Before backing up, the cluster must be shut down. The default clusters `etcd` and `kube-apiserver` are started as static pods. To close the cluster here means to move the static Pod manifest file out of the `/etc/kubernetes/manifest` directory, and the cluster will remove the corresponding Pod to close the service.

1. First, delete the previous backup data. Removing the data does not delete the existing etcd data, but refers to modifying the name of the etcd data directory. Wait for the backup to be successfully restored before deleting this directory. The purpose of this is to also try to restore the current cluster if the etcd backup restore fails. This step needs to be performed for each node.

    ```shell
    rm -rf /var/lib/etcd_bak
    ```

2. The service then needs to be shut down `kube-apiserver` to ensure that there are no new changes to the etcd data. This step needs to be performed for each node.

    ```shell
    mv /etc/kubernetes/manifests/kube-apiserver.yaml /tmp/kube-apiserver.yaml
    ```

3. You also need to turn off the etcd service. This step needs to be performed for each node.

    ```shell
    mv /etc/kubernetes/manifests/etcd.yaml /tmp/etcd.yaml
    ```

4. Ensure that all control plane `kube-apiserver` and `etcd` services are turned off.
   
5. After shutting down all the nodes, use the following command to check `etcd` the cluster status. This command can be executed at any node.

    > The `endpoints` value of needs to be replaced with the actual node name

    ```shell
    etcdctl endpoint status --endpoints=controller-node-1:2379,controller-node-2:2379,controller-node-3:2379 -w table \
      --cacert="/etc/kubernetes/ssl/etcd/ca.crt" \
      --cert="/etc/kubernetes/ssl/apiserver-etcd-client.crt" \
      --key="/etc/kubernetes/ssl/apiserver-etcd-client.key"
    ```

    The expected output is as follows, indicating that all `etcd` nodes have been destroyed:

    ```none
    {"level":"warn","ts":"2023-03-29T17:51:50.817+0800","logger":"etcd-client","caller":"v3@v3.5.6/retry_interceptor.go:62","msg":"retrying of unary invoker failed","target":"etcd-endpoints://0xc0001ba000/controller-node-1:2379","attempt":0,"error":"rpc error: code = DeadlineExceeded desc = latest balancer error: last connection error: connection error: desc = \"transport: Error while dialing dial tcp 10.5.14.31:2379: connect: connection refused\""}
    Failed to get the status of endpoint controller-node-1:2379 (context deadline exceeded)
    {"level":"warn","ts":"2023-03-29T17:51:55.818+0800","logger":"etcd-client","caller":"v3@v3.5.6/retry_interceptor.go:62","msg":"retrying of unary invoker failed","target":"etcd-endpoints://0xc0001ba000/controller-node-2:2379","attempt":0,"error":"rpc error: code = DeadlineExceeded desc = latest balancer error: last connection error: connection error: desc = \"transport: Error while dialing dial tcp 10.5.14.32:2379: connect: connection refused\""}
    Failed to get the status of endpoint controller-node-2:2379 (context deadline exceeded)
    {"level":"warn","ts":"2023-03-29T17:52:00.820+0800","logger":"etcd-client","caller":"v3@v3.5.6/retry_interceptor.go:62","msg":"retrying of unary invoker failed","target":"etcd-endpoints://0xc0001ba000/controller-node-1:2379","attempt":0,"error":"rpc error: code = DeadlineExceeded desc = latest balancer error: last connection error: connection error: desc = \"transport: Error while dialing dial tcp 10.5.14.33:2379: connect: connection refused\""}
    Failed to get the status of endpoint controller-node-3:2379 (context deadline exceeded)
    +----------+----+---------+---------+-----------+------------+-----------+------------+--------------------+--------+
    | ENDPOINT | ID | VERSION | DB SIZE | IS LEADER | IS LEARNER | RAFT TERM | RAFT INDEX | RAFT APPLIED INDEX | ERRORS |
    +----------+----+---------+---------+-----------+------------+-----------+------------+--------------------+--------+
    +----------+----+---------+---------+-----------+------------+-----------+------------+--------------------+--------+
    ```

## Restore the backup

You only need to restore the data of one node, and the etcd data of other nodes will be automatically synchronized.

1. Set environment variables

    Before restoring the data using etcdbrctl, run the following command to set the authentication information of the connection S3 as an environment variable:

    ```shell
    export ECS_ENDPOINT=http://10.6.212.13:9000 # (1)
    export ECS_ACCESS_KEY_ID=AKIAIOSFODNN7EXAMPLE # (2)
    export ECS_SECRET_ACCESS_KEY=wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY # (3)
    ```

    1. Access points for S3 storage
    2. S3 Stored username
    3. S3 Stored Password

2. Perform the restore operation

    Run the etcdbrctl command line tool to perform the restore, which is the most critical step.

    ```shell
    etcdbrctl restore --data-dir /var/lib/etcd/ --store-container="etcd-backup" \ 
      --storage-provider=ECS \
      --initial-cluster=controller-node1=https://10.6.212.10:2380 \
      --initial-advertise-peer-urls=https://10.6.212.10:2380 
    ```

    The parameters are described as follows:

    - --data-dir: etcd data directory. This directory must be consistent with the etcd data directory so that etcd can load data normally.
    - --store-container: The location of S3 storage, the corresponding bucket in MinIO, must correspond to the bucket of data backup.
    - --initial-cluster: etcd is configured initially. The name of the etcd cluster must be the same as the original one.
    - --initial-advertise-peer-urls: etcd member inter-cluster access address. Must be consistent with etcd configuration.

    The expected output is as follows:

    ```none
    INFO[0000] Finding latest set of snapshot to recover from...
    INFO[0000] Restoring from base snapshot: Full-00000000-00111147-1679991074  actor=restorer
    INFO[0001] successfully fetched data of base snapshot in 1.241380207 seconds  actor=restorer
    {"level":"info","ts":1680011221.2511616,"caller":"mvcc/kvstore.go:380","msg":"restored last compact revision","meta-bucket-name":"meta","meta-bucket-name-key":"finishedCompactRev","restored-compact-revision":110327}
    {"level":"info","ts":1680011221.3045986,"caller":"membership/cluster.go:392","msg":"added member","cluster-id":"66638454b9dd7b8a","local-member-id":"0","added-peer-id":"123c2503a378fc46","added-peer-peer-urls":["https://10.6.212.10:2380"]}
    INFO[0001] Starting embedded etcd server...              actor=restorer

    ....

    {"level":"info","ts":"2023-03-28T13:47:02.922Z","caller":"embed/etcd.go:565","msg":"stopped serving peer traffic","address":"127.0.0.1:37161"}
    {"level":"info","ts":"2023-03-28T13:47:02.922Z","caller":"embed/etcd.go:367","msg":"closed etcd server","name":"default","data-dir":"/var/lib/etcd","advertise-peer-urls":["http://localhost:0"],"advertise-client-urls":["http://localhost:0"]}
    INFO[0003] Successfully restored the etcd data directory.
    ```

    !!! note “You can check the YAML file of etcd for comparison to avoid configuration errors”

        ```shell
        cat /tmp/etcd.yaml | grep initial-
        - --experimental-initial-corrupt-check=true
        - --initial-advertise-peer-urls=https://10.6.212.10:2380
        - --initial-cluster=controller-node-1=https://10.6.212.10:2380
        ```

3. The following command is executed on node 01 in order to restore the etcd service for node 01.

    First, move the manifest file of etcd static Pod to the `/etc/kubernetes/manifests` directory, and kubelet will restart etcd:

    ```shell
    mv /tmp/etcd.yaml /etc/kubernetes/manifests/etcd.yaml
    ```

    Then wait for the etcd service to finish starting, and check the status of etcd. The default directory of etcd-related certificates is: `/etc/kubernetes/ssl`. If the cluster certificate is stored in another location, specify the corresponding path.

    - Check the etcd cluster list:

        ```shell
        etcdctl member list -w table \
        --cacert="/etc/kubernetes/ssl/etcd/ca.crt" \
        --cert="/etc/kubernetes/ssl/apiserver-etcd-client.crt" \
        --key="/etc/kubernetes/ssl/apiserver-etcd-client.key" 
        ```

        The expected output is as follows:

        ```none
        +------------------+---------+-------------------+--------------------------+--------------------------+------------+
        |        ID        | STATUS  |       NAME        |        PEER ADDRS        |       CLIENT ADDRS       | IS LEARNER |
        +------------------+---------+-------------------+--------------------------+--------------------------+------------+
        | 123c2503a378fc46 | started | controller-node-1 | https://10.6.212.10:2380 | https://10.6.212.10:2379 |      false |
        +------------------+---------+-------------------+--------------------------+--------------------------+------------+
        ```

    - To view the status of controller-node-1:

        ```shell
        etcdctl endpoint status --endpoints=controller-node-1:2379 -w table \
        --cacert="/etc/kubernetes/ssl/etcd/ca.crt" \
        --cert="/etc/kubernetes/ssl/apiserver-etcd-client.crt" \
        --key="/etc/kubernetes/ssl/apiserver-etcd-client.key"
        ```

        The expected output is as follows:

        ```none
        +------------------------+------------------+---------+---------+-----------+------------+-----------+------------+--------------------+--------+
        |        ENDPOINT        |        ID        | VERSION | DB SIZE | IS LEADER | IS LEARNER | RAFT TERM | RAFT INDEX | RAFT APPLIED INDEX | ERRORS |
        +------------------------+------------------+---------+---------+-----------+------------+-----------+------------+--------------------+--------+
        | controller-node-1:2379 | 123c2503a378fc46 |   3.5.6 |   15 MB |      true |      false |         3 |       1200 |               1199 |        |
        +------------------------+------------------+---------+---------+-----------+------------+-----------+------------+--------------------+--------+
        ```

4. Restore other node data

    The above steps have restored the data of node 01. If you want to restore the data of other nodes, you only need to start the Pod of etcd and let etcd complete the data synchronization by itself.

    - Do the same at both node 02 and node 03:

        ```shell
        mv /tmp/etcd.yaml /etc/kubernetes/manifests/etcd.yaml
        ```

    - Data synchronization between etcd member clusters takes some time. You can check the etcd cluster status to ensure that all etcd clusters are normal:

        Check whether the etcd cluster status is normal:

        ```shell
        etcdctl member list -w table \
        --cacert="/etc/kubernetes/ssl/etcd/ca.crt" \
        --cert="/etc/kubernetes/ssl/apiserver-etcd-client.crt" \
        --key="/etc/kubernetes/ssl/apiserver-etcd-client.key"
        ```

        The expected output is as follows:

        ```none
        +------------------+---------+-------------------+-------------------------+-------------------------+------------+
        |        ID        | STATUS  |    NAME           |       PEER ADDRS        |      CLIENT ADDRS       | IS LEARNER |
        +------------------+---------+-------------------+-------------------------+-------------------------+------------+
        | 6ea47110c5a87c03 | started | controller-node-1 | https://10.5.14.31:2380 | https://10.5.14.31:2379 |      false |
        | e222e199f1e318c4 | started | controller-node-2 | https://10.5.14.32:2380 | https://10.5.14.32:2379 |      false |
        | f64eeda321aabe2d | started | controller-node-3 | https://10.5.14.33:2380 | https://10.5.14.33:2379 |      false |
        +------------------+---------+-------------------+-------------------------+-------------------------+------------+
        ```

        Check whether the three member nodes are normal:

        ```shell
        etcdctl endpoint status --endpoints=controller-node-1:2379,controller-node-2:2379,controller-node-3:2379 -w table \
        --cacert="/etc/kubernetes/ssl/etcd/ca.crt" \
        --cert="/etc/kubernetes/ssl/apiserver-etcd-client.crt" \
        --key="/etc/kubernetes/ssl/apiserver-etcd-client.key"
        ```

        The expected output is as follows:

        ```none
        +------------------------+------------------+---------+---------+-----------+------------+-----------+------------+--------------------+--------+
        |     ENDPOINT           |        ID        | VERSION | DB SIZE | IS LEADER | IS LEARNER | RAFT TERM | RAFT INDEX | RAFT APPLIED INDEX | ERRORS |
        +------------------------+------------------+---------+---------+-----------+------------+-----------+------------+--------------------+--------+
        | controller-node-1:2379 | 6ea47110c5a87c03 |   3.5.6 |   88 MB |      true |      false |         6 |     199008 |             199008 |        |
        | controller-node-2:2379 | e222e199f1e318c4 |   3.5.6 |   88 MB |     false |      false |         6 |     199114 |             199114 |        |
        | controller-node-3:2379 | f64eeda321aabe2d |   3.5.6 |   88 MB |     false |      false |         6 |     199316 |             199316 |        |
        +------------------------+------------------+---------+---------+-----------+------------+-----------+------------+--------------------+--------+
        ```

## Restore the cluster

After the etcd data of all nodes are synchronized, the kube-apiserver can be restarted to restore the entire cluster to an accessible state:

1. Restart the kube-apiserver service for node1

    ```shell
    mv /tmp/kube-apiserver.yaml /etc/kubernetes/manifests/kube-apiserver.yaml
    ```

2. Restart the kube-apiserver service for node2

    ```shell
    mv /tmp/kube-apiserver.yaml /etc/kubernetes/manifests/kube-apiserver.yaml
    ```

3. Restart the kube-apiserver service for node3

    ```shell
    mv /tmp/kube-apiserver.yaml /etc/kubernetes/manifests/kube-apiserver.yaml
    ```

4. After kubelet starts kube-apiserver, check whether the restored k8s data is normal:

    ```shell
    kubectl get nodes
    ```

    The expected output is as follows:

    ```none
    NAME                STATUS     ROLES           AGE     VERSION
    controller-node-1   Ready      <none>          3h30m   v1.25.4
    controller-node-3   Ready      control-plane   3h29m   v1.25.4
    controller-node-3   Ready      control-plane   3h28m   v1.25.4
    ```
