# How to Add Heterogeneous Nodes to a Working Cluster

This article explains how to add ARM architecture nodes with Kylin v10 sp2 operating system to an AMD architecture working cluster with CentOS 7.9 operating system.

!!! note

    This article is only applicable to adding heterogeneous nodes to a working cluster created using the DCE 5.0 platform in offline mode, excluding connected clusters.

## Prerequisites

- A DCE 5.0 Full Mode deployment has been successfully completed, and the Spark node is still alive. Refer to the documentation [Offline Installation of DCE 5.0 Enterprise](../../install/commercial/start-install.md) for the deployment process.
- A working cluster with AMD architecture and CentOS 7.9 operating system has been created through the DCE 5.0 platform. Refer to the documentation [Creating a Working Cluster](../user-guide/clusters/create-cluster.md) for the creation process.

## Procedure

### Download and Import Offline Packages (Using ARM architecture and Kylin v10 sp2 operating system as examples)

Make sure you are logged into the Spark node! Also, make sure the `clusterConfig.yaml` file used during the DCE 5.0 deployment is available.

#### Offline Image Package

!!! note

    The latest version can be downloaded from the [Download Center](https://docs.daocloud.io/download/dce5/).

| CPU Architecture | Version | Download Link |
| :--------------- | :------ | :------------ |
| AMD64            | v0.8.0  | <https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-v0.8.0-amd64.tar> |
| ARM64            | v0.8.0  | <https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-v0.8.0-arm64.tar> |

After downloading, extract the offline package:

```bash
# Here we download the offline package for ARM64 architecture
tar -xvf offline-v0.8.0-arm64.tar
```

#### ISO Offline Package (Kylin v10 sp2)

| CPU Architecture | Operating System Version                     | Download Link |
| :--------------- | :------------------------------------------- | :------------ |
| ARM64            | Kylin Linux Advanced Server release V10 (Sword) SP2 | Application: <https://www.kylinos.cn/scheme/server/1.html> <br />Note: Kylin operating system requires personal information to be provided for downloading and usage. Select V10 (Sword) SP2 when downloading. |

#### osPackage Offline Package (Kylin v10 sp2)

The [Kubean](https://github.com/kubean-io/kubean) project provides osPackage offline packages for different operating systems. Visit <https://github.com/kubean-io/kubean/releases> to view the available packages.

| Operating System Version                     | Download Link |
| :------------------------------------------- | :------------ |
| Kylin Linux Advanced Server release V10 (Sword) SP2 | <https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.5.2/os-pkgs-kylinv10-v0.5.2.tar.gz> |

!!! note

    Please check the specific version of the osPackage offline package in the `offline/sample/clusterConfig.yaml` file of the offline image package.

#### Importing Offline Packages to the Spark Node

Execute the import-artifact command:

```bash
./offline/dce5-installer import-artifact -c clusterConfig.yaml \
    --target-arch=arm64 \
    --offline-path=/root/offline \
    --iso-path=/root/Kylin-Server-10-SP2-aarch64-Release-Build09-20210524.iso \
    --os-pkgs-path=/root/os-pkgs-kylinv10-v0.5.2.tar.gz
```

!!! note

    Parameter Explanation:

    - `-c clusterConfig.yaml` specifies the clusterConfig.yaml file used during the previous DCE 5.0 deployment.
    - `--target-arch` specifies the architecture, supporting arm64 and amd64.
    - `--offline-path` specifies the file path of the downloaded offline image package.
    - `--iso-path` specifies the file path of the downloaded ISO operating system image.
    - `--os-pkgs-path` specifies the file path of the downloaded osPackage offline package.

After a successful import command execution, the offline package will be uploaded to Minio on the Spark node.

### Adding Heterogeneous Worker Nodes

Make sure you are logged into the management node of the Global cluster in DCE 5.0.

#### Modify the Host Manifest

Here is an example of host manifest:

=== "Before adding nodes"

    ```yaml
    apiVersion: v1
    kind: ConfigMap
    metadata:
        name: ${cluster-name}-hosts-conf
        namespace: kubean-system
    data:
        hosts.yml: |
            all:
            hosts:
                centos-master:
                ip: 10.5.14.122
                access_ip: 10.5.14.122
                ansible_host: 10.5.14.122
                ansible_connection: ssh
                ansible_user: root
                ansible_ssh_pass: ******
            children:
                kube_control_plane:
                hosts:
                    centos-master: 
                kube_node:
                hosts:
                    centos-master: 
                etcd:
                hosts:
                    centos-master: 
                k8s_cluster:
                children:
                    kube_control_plane: 
                    kube_node: 
    ```

=== "After adding node"

    ```yaml
    apiVersion: v1
    kind: ConfigMap
    metadata:
        name: ${cluster-name}-hosts-conf
        namespace: kubean-system
    data:
        hosts.yml: |
            all:
            hosts:
                centos-master:
                ip: 10.5.14.122
                access_ip: 10.5.14.122
                ansible_host: 10.5.14.122
                ansible_connection: ssh
                ansible_user: root
                ansible_ssh_pass: ******
                # 添加异构节点信息
                kylin-worker:
                ip: 10.5.10.220
                access_ip: 10.5.10.220
                ansible_host: 10.5.10.220
                ansible_connection: ssh
                ansible_user: root
                ansible_ssh_pass: dangerous@2022
            children:
                kube_control_plane:
                hosts:
                    centos-master: 
                kube_node:
                hosts:
                    centos-master: 
                    kylin-worker: # 添加新增的异构节点名称
                etcd:
                hosts:
                    centos-master: 
                k8s_cluster:
                children:
                    kube_control_plane: 
                    kube_node: 
    ```

To add information about the newly added worker nodes according to the above configuration comments:

```shell
# Replace "cluster-name" with the name of your working cluster, which is automatically generated when creating the cluster through container management.
kubectl edit cm ${cluster-name}-hosts-conf -n kubean-system
```

#### Add Expansion Tasks through ClusterOperation.yml

Example:

```yaml
apiVersion: kubean.io/v1alpha1
kind: ClusterOperation
metadata:
  name: add-worker-node
spec:
  cluster: ${cluster-name} # Specify cluster name
  image: ghcr.m.daocloud.io/kubean-io/spray-job:v0.5.0
  backoffLimit: 0
  actionType: playbook
  action: scale.yml
  extraArgs: --limit=kylin-worker
  preHook:
    - actionType: playbook
      action: ping.yml
    - actionType: playbook
      action: disable-firewalld.yml
    - actionType: playbook
      action: enable-repo.yml
      extraArgs: |
        -e "{repo_list: ["http://10.5.14.30:9000/kubean/kylin-iso/\$releasever/os/\$basearch","http://10.5.14.30:9000/kubean/kylin/\$releasever/os/\$basearch"]}"
  postHook:
    - actionType: playbook
      action: cluster-info.yml
```

Note:

- Ensure that the `spec.image` image address matches the image used in the previous deployment job.
- Set `spec.action` to `scale.yml`.
- Set `spec.extraArgs` to `--limit=g-worker`.
- Fill in the correct `repo_list` parameter for the relevant OS in `spec.preHook`'s `enable-repo.yml` script.

To create and deploy `join-node-ops.yaml` according to the above configuration:

```shell
# Copy the manifest file mentioned above
vi join-node-ops.yaml
kubectl apply -f join-node-ops.yaml -n kubean-system
```

Check the status of the task execution:

```shell
kubectl -n kubean-system get pod | grep add-worker-node
```

To check the progress of the scaling task, you can view the logs of the corresponding pod.

### Verify in the User Interface

1. Go to `Container Management` -> `Clusters` -> `Nodes`.

    ![Node Management](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/kpanda/images/arm02.png)

2. Click on the newly added node to view details.

    ![Node Details](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/kpanda/images/arm01.png)
