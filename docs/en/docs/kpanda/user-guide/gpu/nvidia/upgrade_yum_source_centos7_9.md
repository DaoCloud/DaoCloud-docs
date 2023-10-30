## Building CentOS 7.9 Offline Yum Source

## Use Case Overview

DCE 5 comes with a pre-installed GPU Operator offline package for CentOS 7.9 with kernel version 3.10.0-1160. For other OS types or kernel versions, users need to manually build an offline yum source.

This guide explains how to build an offline yum source for CentOS 7.9 with a specific kernel version and use it when installing the GPU Operator by specifying the `RepoConfig.ConfigMapName` parameter.

## Prerequisites

1. The user has already installed the v0.12.0 or later version of the addon offline package on the platform.
2. The nodes in the cluster where the GPU Operator will be deployed must have CentOS 7.9 installed with the exact same kernel version.
3. Prepare a file server that is accessible from the cluster network, such as Nginx or MinIO.
4. Prepare a node that has internet access, can access the cluster where the GPU Operator will be deployed, and can access the file server. Docker should also be installed on this node. You can refer to [Installing Docker](../../../../install/community/kind/online.md#安装-docker) for installation instructions.

## Procedure

This guide uses CentOS 7.9 with kernel version 3.10.0-1160.95.1.el7.x86_64 as an example to explain how to upgrade the pre-installed GPU Operator offline package's yum source.

### Step 1: Check the Kernel Version of the Cluster Nodes

Run the following command to check the kernel version of the nodes in the cluster where the GPU Operator will be deployed:

```bash
uname -a
```

The expected output should resemble the following:

```
Linux localhost.localdomain 3.10.0-1160.95.1.el7.x86_64 #1 SMP Mon Oct 19 16:18:59 UTC 2020 x86_64 x86_64 x86_64 GNU/Linux
```

The output shows the current node's kernel version as `3.10.0-1160.el7.x86_64`.

### Step 2: Create the Offline Yum Source

Perform the following steps on a node that has internet access and can access the file server:

1. Create a script file named `yum.sh` by running the following command:

    ```bash
    vi yum.sh
    ```

    Then press the "i" key to enter insert mode and enter the following content:

    ```bash
    export TARGET_KERNEL_VERSION=$1

    cat >> run.sh << \EOF
    #! /bin/bash
    echo "start install kernel repo"
    echo ${KERNEL_VERSION}
    mkdir centos-base

    if [ "$OS" -eq 7 ]; then
        yum install --downloadonly --downloaddir=./centos-base perl
        yum install --downloadonly --downloaddir=./centos-base elfutils-libelf.x86_64
        yum install --downloadonly --downloaddir=./redhat-base elfutils-libelf-devel.x86_64
        yum install --downloadonly --downloaddir=./centos-base kernel-headers-${KERNEL_VERSION}.el7.x86_64
        yum install --downloadonly --downloaddir=./centos-base kernel-devel-${KERNEL_VERSION}.el7.x86_64
        yum install --downloadonly --downloaddir=./centos-base kernel-${KERNEL_VERSION}.el7.x86_64
        yum install  -y --downloadonly --downloaddir=./centos-base groff-base
    elif [ "$OS" -eq 8 ]; then
        yum install --downloadonly --downloaddir=./centos-base perl
        yum install --downloadonly --downloaddir=./centos-base elfutils-libelf.x86_64
        yum install --downloadonly --downloaddir=./redhat-base elfutils-libelf-devel.x86_64
        yum install --downloadonly --downloaddir=./centos-base kernel-headers-${KERNEL_VERSION}.el8.x86_64
        yum install --downloadonly --downloaddir=./centos-base kernel-devel-${KERNEL_VERSION}.el8.x86_64
        yum install --downloadonly --downloaddir=./centos-base kernel-${KERNEL_VERSION}.el8.x86_64
        yum install  -y --downloadonly --downloaddir=./centos-base groff-base
    else
        echo "Error os version"
    fi

    createrepo centos-base/
    ls -lh centos-base/
    tar -zcf centos-base.tar.gz centos-base/
    echo "end install kernel repo"
    EOF

    cat >> Dockerfile << EOF
    FROM centos:7
    ENV KERNEL_VERSION=""
    ENV OS=7
    RUN yum install -y createrepo
    COPY run.sh .
    ENTRYPOINT ["/bin/bash","run.sh"]
    EOF

    docker build -t test:v1 -f Dockerfile .
    docker run -e KERNEL_VERSION=$TARGET_KERNEL_VERSION --name centos7.9 test:v1
    docker cp centos7.9:/centos-base.tar.gz .
    tar -xzf centos-base.tar.gz
    ```

    Press the `Esc` key to exit insert mode, then enter `:wq` to save and exit.

2. Run the `yum.sh` file:

    ```bash
    bash -x yum.sh TARGET_KERNEL_VERSION
    ```

    The `TARGET_KERNEL_VERSION` parameter is used to specify the kernel version of the cluster nodes. Note: You don't need to include the distribution identifier (e.g., `.el7.x86_64`).

    For example:

    ```bash
    bash -x yum.sh 3.10.0-1160.95.1
    ```

Now you have generated an offline yum source, `centos-base`, for the kernel version `3.10.0-1160.95.1.el7.x86_64`.

### Step 3: Upload the Offline Yum Source to the File Server

Perform the following steps on a node that has internet access and can access the file server. This step is used to upload the generated yum source from the previous step to a file server that can be accessed by the cluster where the GPU Operator will be deployed. The file server can be Nginx, MinIO, or any other file server that supports the HTTP protocol.

In this example, we will use the built-in MinIO in DCE5 as the file server. The MinIO details are as follows:

- Access URL: `http://10.5.14.200:9000` (usually `{seed-node IP} + {9000 port}`)
- Login username: rootuser
- Login password: rootpass123

1. Run the following command in the current directory of the node to establish a connection between the node's local `mc` command-line tool and the MinIO server:

    ```bash
    mc config host add minio http://10.5.14.200:9000 rootuser rootpass123
    ```

    The expected output should resemble the following:

    ```bash
    Added `minio` successfully.
    ```

    `mc` is the command-line tool provided by MinIO for interacting with the MinIO server. For more details, refer to the [MinIO Client](https://min.io/docs/minio/linux/reference/minio-mc.html) documentation.

2. In the current directory of the node, create a bucket named `centos-base`:

    ```bash
    mc mb -p minio/centos-base
    ```

    The expected output should resemble the following:

    ```bash
    Bucket created successfully `minio/centos-base`.
    ```

3. Set the access policy of the bucket `centos-base` to allow public download. This will enable access during the installation of the GPU Operator:

    ```bash
    mc anonymous set download minio/centos-base
    ```

    The expected output should resemble the following:

    ```bash
    Access permission for `minio/centos-base` is set to `download`
    ```

4. In the current directory of the node, copy the generated `centos-base` offline yum source to the `minio/centos-base` bucket on the MinIO server:

    ```bash
    mc cp centos-base minio/centos-base --recursive
    ```

### Step 4: Create a Configuration Item to Store the Yum Source Information in the Cluster

Perform the following steps on the control node of the cluster where the GPU Operator will be deployed.

1. Run the following command to create a file named `CentOS-Base.repo` that specifies the configuration information for the yum source storage:

    ```bash
    # The file name must be CentOS-Base.repo, otherwise it cannot be recognized during the installation of the GPU Operator
    cat > CentOS-Base.repo << EOF
    [extension-0]
    baseurl = http://10.5.14.200:9000/centos-base/centos-base # The file server address where the yum source is placed in step 3
    gpgcheck = 0
    name = kubean extension 0
    
    [extension-1]
    baseurl = http://10.5.14.200:9000/centos-base/centos-base # The file server address where the yum source is placed in step 3
    gpgcheck = 0
    name = kubean extension 1
    EOF
    ```

2. Based on the created `CentOS-Base.repo` file, create a configmap named `local-repo-config` in the `gpu-operator` namespace:

    ```bash
    kubectl create configmap local-repo-config -n gpu-operator --from-file=./CentOS-Base.repo
    ```

    The expected output should resemble the following:

    ```
    configmap/local-repo-config created
    ```

    The `local-repo-config` configmap will be used to provide the value for the `RepoConfig.ConfigMapName` parameter during the installation of the GPU Operator. You can customize the configuration file name.

3. View the content of the `local-repo-config` configmap:

    ```bash
    kubectl get configmap local-repo-config -n gpu-operator -oyaml
    ```

    The expected output should resemble the following:

    ```yaml
    apiVersion: v1
    data:
    CentOS-Base.repo: "[extension-0]\nbaseurl = http://10.6.232.5:32618/centos-base# The file server path where the yum source is placed in step 2\ngpgcheck = 0\nname = kubean extension 0\n  \n[extension-1]\nbaseurl = http://10.6.232.5:32618/centos-base # The file server path where the yum source is placed in step 2\ngpgcheck = 0\nname = kubean extension 1\n"
    kind: ConfigMap
    metadata:
    creationTimestamp: "2023-10-18T01:59:02Z"
    name: local-repo-config
    namespace: gpu-operator
    resourceVersion: "59445080"
    uid: c5f0ebab-046f-442c-b932-f9003e014387
    ```

You have successfully created an offline yum source configuration file for the cluster where the GPU Operator will be deployed. You can use it during the [offline installation of the GPU Operator](./install_nvidia_driver_of_operator.md) by specifying the `RepoConfig.ConfigMapName` parameter.
