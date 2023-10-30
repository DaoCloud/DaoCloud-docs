# Building Red Hat 8.4 Offline Yum Source

## Scenario Introduction

DCE 5 comes with pre-installed CentOS 7.9 and GPU Operator offline packages with kernel version 3.10.0-1160. For other OS types or nodes with different kernels, users need to manually build the offline yum source.

This guide explains how to build an offline yum source package for Red Hat 8.4 based on any node in the Global cluster. It also demonstrates how to use it during the installation of the GPU Operator by specifying the `RepoConfig.ConfigMapName` parameter.

## Prerequisites

1. The user has already installed the addon offline package version v0.12.0 or higher on the platform.
2. The OS of the cluster nodes where the GPU Operator will be deployed must be Red Hat 8.4, and the kernel version must be identical.
3. Prepare a file server that can communicate with the cluster network where the GPU Operator will be deployed, such as Nginx or MinIO.
4. Prepare a node that can access the internet, the cluster where the GPU Operator will be deployed, and the file server. Ensure that Docker is already installed on this node.
5. The nodes in the Global cluster must be Red Hat 8.4 4.18.0-305.el8.x86_64.

## Procedure

This guide uses a node with Red Hat 8.4 4.18.0-305.el8.x86_64 as an example to demonstrate how to build an offline yum source package for Red Hat 8.4 based on any node in the Global cluster. It also explains how to use it during the installation of the GPU Operator by specifying the `RepoConfig.ConfigMapName` parameter.

### Step 1: Download the Yum Source from the Seed Node

Perform the following steps on the master node of the Global cluster.

1. Use SSH or any other method to access any node in the Global cluster and run the following command:

    ```bash
    cat /etc/yum.repos.d/extension.repo # View the contents of extension.repo.
    ```

    The expected output should resemble the following:

    ```ini
    [extension-0]
    baseurl = http://10.5.14.200:9000/kubean/redhat/$releasever/os/$basearch
    gpgcheck = 0
    name = kubean extension 0

    [extension-1]
    baseurl = http://10.5.14.200:9000/kubean/redhat-iso/$releasever/os/$basearch/AppStream
    gpgcheck = 0
    name = kubean extension 1

    [extension-2]
    baseurl = http://10.5.14.200:9000/kubean/redhat-iso/$releasever/os/$basearch/BaseOS
    gpgcheck = 0
    name = kubean extension 2
    ```

2. Create a folder named `redhat-base-repo` under the root directory:

    ```bash
    mkdir redhat-base-repo
    ```

3. Download the RPM packages from the yum source to your local machine:

    Download the RPM packages from `extension-1`:

    ```bash
    reposync -p redhat-base-repo -n --repoid=extension-1
    ```

    Download the RPM packages from `extension-2`:

    ```bash
    reposync -p redhat-base-repo -n --repoid=extension-2
    ```

### Step 2: Download the `elfutils-libelf-devel-0.187-4.el8.x86_64.rpm` Package

Perform the following steps on a node with internet access. Before proceeding, ensure that there is network connectivity between the node with internet access and the master node of the Global cluster.

1. Run the following command on the node with internet access to download the `elfutils-libelf-devel-0.187-4.el8.x86_64.rpm` package:

    ```bash
    wget https://rpmfind.net/linux/centos/8-stream/BaseOS/x86_64/os/Packages/elfutils-libelf-devel-0.187-4.el8.x86_64.rpm
    ```

2. Transfer the `elfutils-libelf-devel-0.187-4.el8.x86_64.rpm` package from the current directory to the node mentioned in step 1:

    ```bash
    scp elfutils-libelf-devel-0.187-4.el8.x86_64.rpm user@ip:~/redhat-base-repo/extension-2/Packages/
    ```

    For example:

    ```bash
    scp elfutils-libelf-devel-0.187-4.el8.x86_64.rpm root@10.6.175.10:~/redhat-base-repo/extension-2/Packages/
    ```

### Step 3: Generate the Local Yum Repository

Perform the following steps on the master node of the Global cluster mentioned in Step 1.

1. Create the yum repository directories:

    ```bash
    mkdir /root/redhat-base-repo/extension-1/repodata
    mkdir /root/redhat-base-repo/extension-2/repodata
    ```

2. Generate the repository index for the directories:

    ```bash
    createrepo -po ~/redhat-base-repo/extension-1/repodata ~/redhat-base-repo/extension-1/Packages
    createrepo -po ~/redhat-base-repo/extension-2/repodata ~/redhat-base-repo/extension-2/Packages
    ```

You have now generated the offline yum source named `redhat-base-repo` for kernel version `4.18.0-305.el8.x86_64`.

### Step 4: Upload the Local Yum Repository to the File Server

In this example, we will use Minio, which is built-in as the file server in the DCE5 seed node. However, you can choose any file server that suits your needs. Here are the details for Minio:

- Access URL: `http://10.5.14.200:9000` (usually the {seed node IP} + {9000 port})
- Login username: rootuser
- Login password: rootpass123

1. On the current node, establish a connection between the local `mc` command-line tool and the Minio server by running the following command:

    ```bash
    mc config host add minio <file_server_access_url> <username> <password>
    ```

    For example:

    ```bash
    mc config host add minio http://10.5.14.200:9000 rootuser rootpass123
    ```

    The expected output should be similar to:

    ```bash
    Added `minio` successfully.
    ```

    The `mc` command-line tool is provided by the Minio file server as a client command-line tool. For more details, please refer to the [MinIO Client](https://min.io/docs/minio/linux/reference/minio-mc.html) documentation.

2. Create a bucket named `redhat-base` in the current location:

    ```bash
    mc mb -p minio/redhat-base
    ```

    The expected output should be similar to:

    ```bash
    Bucket created successfully `minio/redhat-base`.
    ```

3. Set the access policy of the `redhat-base` bucket to allow public downloads so that it can be accessed during the installation of the GPU Operator:

    ```bash
    mc anonymous set download minio/redhat-base
    ```

    The expected output should be similar to:

    ```bash
    Access permission for `minio/redhat-base` is set to `download`
    ```

4. Copy the offline yum repository files (`redhat-base-repo`) from the current location to the Minio server's `minio/redhat-base` bucket:

    ```bash
    mc cp redhat-base-repo minio/redhat-base --recursive
    ```

### Step 5: Create a ConfigMap to Store Yum Repository Information in the Cluster

Perform the following steps on the control node of the cluster where you will deploy the GPU Operator.

1. Run the following command to create a file named `redhat.repo`, which specifies the configuration information for the yum repository storage:

    ```bash
    # The file name must be redhat.repo, otherwise it won't be recognized when installing gpu-operator
    cat > redhat.repo << EOF
    [extension-0]
    baseurl = http://10.5.14.200:9000/redhat-base/redhat-base-repo # The file server address where the yum source is stored in Step 1
    gpgcheck = 0
    name = kubean extension 0
    
    [extension-1]
    baseurl = http://10.5.14.200:9000/redhat-base/redhat-base-repo # The file server address where the yum source is stored in Step 1
    gpgcheck = 0
    name = kubean extension 1
    EOF
    ```

2. Based on the created `redhat.repo` file, create a configmap named `local-repo-config` in the `gpu-operator` namespace:

    ```bash
    kubectl create configmap local-repo-config -n gpu-operator --from-file=./redhat.repo
    ```

    The expected output should be similar to:

    ```
    configmap/local-repo-config created
    ```

    The `local-repo-config` configuration file is used to provide the value for the `RepoConfig.ConfigMapName` parameter during the installation of the GPU Operator. You can choose a different name for the configuration file.

3. View the contents of the `local-repo-config` configuration file:

    ```bash
    kubectl get configmap local-repo-config -n gpu-operator -oyaml
    ```

You have successfully created the offline yum source configuration file for the cluster where the GPU Operator will be deployed. You can use it by specifying the `RepoConfig.ConfigMapName` parameter during the [offline installation of the GPU Operator](./install_nvidia_driver_of_operator.md).
