# Creating a Cluster on Non-Supported Operating Systems

This document outlines how to create a working cluster on an **unsupported OS** in offline mode. For the range of OS supported by DCE 5.0, please refer to [DCE 5.0 Supported Operating Systems](../../install/commercial/deploy-requirements.md).

The main process for creating a working cluster on an unsupported OS in offline mode is illustrated in the diagram below:

![Process](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/kpanda/images/otherlinux.png)

Next, we will use the openAnolis operating system as an example to demonstrate how to create a cluster on a non-mainstream operating system.

## Prerequisites

- DCE 5.0 Full Mode has been deployed following the documentation: [Offline Installation of DCE 5.0 Enterprise](../../install/commercial/start-install.md).
- At least one node with the same architecture and version that can connect to the internet.

## Procedure

### Online Node - Building an Offline Package

Find an online environment with the same architecture and OS as the nodes in the target cluster. In this example, we will use [AnolisOS 8.8 GA](https://openanolis.cn/download). Run the following command to generate an offline `os-pkgs` package:

```bash
# Download relevant scripts and build os packages package
$ curl -Lo ./pkgs.yml https://raw.githubusercontent.com/kubean-io/kubean/main/build/os-packages/others/pkgs.yml
$ curl -Lo ./other_os_pkgs.sh https://raw.githubusercontent.com/kubean-io/kubean/main/build/os-packages/others/other_os_pkgs.sh && chmod +x other_os_pkgs.sh
$ ./other_os_pkgs.sh build # Build the offline package
```

After executing the above command, you should have a compressed package named **`os-pkgs-anolis-8.8.tar.gz`** in the current directory. The file structure in the current directory should look like this:

```bash
    .
    ├── other_os_pkgs.sh
    ├── pkgs.yml
    └── os-pkgs-anolis-8.8.tar.gz
```

### Offline Node - Installing the Offline Package

Copy the three files generated on the online node (`other_os_pkgs.sh`, `pkgs.yml`, and `os-pkgs-anolis-8.8.tar.gz`) to **all** nodes in the target cluster in the offline environment.

Login to any one of the nodes in the offline environment that is part of the target cluster, and run the following command to install the `os-pkg` package on the node:

```bash
# Configure environment variables
$ export PKGS_YML_PATH=/root/workspace/os-pkgs/pkgs.yml # Path to the pkgs.yml file on the current offline node
$ export PKGS_TAR_PATH=/root/workspace/os-pkgs/os-pkgs-anolis-8.8.tar.gz # Path to the os-pkgs-anolis-8.8.tar.gz file on the current offline node
$ export SSH_USER=root # Username for the current offline node
$ export SSH_PASS=dangerous # Password for the current offline node
$ export HOST_IPS='172.30.41.168' # IP address of the current offline node
$ ./other_os_pkgs.sh install # Install the offline package
```

After executing the above command, wait for the interface to prompt: `All packages for node (X.X.X.X) have been installed`, which indicates that the installation is complete.

### Go to the User Interface to Create Cluster

Refer to the documentation on [Creating a Working Cluster](../user-guide/clusters/create-cluster.md) to create an openAnolis cluster.
