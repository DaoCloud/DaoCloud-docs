# Create an Ubuntu Work Cluster on CentOS Management Platform

This article explains how to create an Ubuntu work cluster on an existing CentOS management platform.

!!! note

    This article is only applicable for offline mode, using the DCE 5.0 platform to create a work cluster with an AMD architecture. The management platform and the cluster being created should both have an AMD architecture. Creating mixed clusters (AMD and ARM) is not supported during cluster creation. However, you can manage mixed clusters by adding heterogeneous nodes after the cluster creation.

## Prerequisites

- A fully deployed DCE 5.0 Enterprise Package in offline mode, with all components running. For deployment instructions, refer to the documentation [Offline Installation of DCE 5.0 Enterprise Package](../../install/commercial/start-install.md).

## Procedure

### Download and Import Ubuntu Offline Packages

Make sure you are logged in to the "bootstrap" node and that you still have the __clusterConfig.yaml__ file used during the deployment of DCE 5.0.

#### Download Ubuntu Offline Packages

Download the required Ubuntu OS package and ISO offline packages:

| Resource Name                   | Description                | Download Link                                                |
| ------------------------------- | -------------------------- | ------------------------------------------------------------ |
| os-pkgs-ubuntu1804-v0.6.6.tar.gz | Ubuntu1804 OS package      | [Download](https://github.com/kubean-io/kubean/releases/download/v0.6.6/os-pkgs-ubuntu1804-v0.6.6.tar.gz) |
| ISO offline package             | Script to import OS package | http://mirrors.melbourne.co.uk/ubuntu-releases/             |
| import-iso                      | Script to import ISO        | [Download](https://github.com/kubean-io/kubean/releases/download/v0.6.6/import_iso.sh) |

#### Import Ubuntu OS Package to the "bootstrap" Node's MinIO

**Extract the Ubuntu OS package**

Run the following command to extract the downloaded OS package:

```bash
# Replace 'os-pkgs-ubuntu1804-v0.6.6.tar.gz' with the actual name of the Ubuntu OS package you downloaded
tar -xvf os-pkgs-ubuntu1804-v0.6.6.tar.gz 
```

The extracted contents of the OS package are as follows:

```text
    os-pkgs
    ├── import_ospkgs.sh       # Script used to import OS packages to the MinIO file service
    ├── os-pkgs-amd64.tar.gz   # OS packages for amd64 architecture
    ├── os-pkgs-arm64.tar.gz   # OS packages for arm64 architecture
    └── os-pkgs.sha256sum.txt  # sha256sum verification file for OS packages
```

**Import OS Packages to the MinIO on the "bootstrap" Node**

Run the following command to import the OS packages to the MinIO file service:

```bash
MINIO_USER=rootuser MINIO_PASS=rootpass123 ./import_ospkgs.sh  http://127.0.0.1:9000 os-pkgs-ubuntu1804-v0.6.6.tar.gz
```

!!! note

    The above command is only applicable for the built-in MinIO service on the "bootstrap" node.
    If you are using an external MinIO service, please replace "http://127.0.0.1:9000" with the
    access address of your external MinIO. "rootuser" and "rootpass123" are the default credentials
    for the built-in MinIO service on the "bootstrap" node. "os-pkgs-ubuntu1804-v0.6.6.tar.gz" should
    be replaced with the actual name of the downloaded OS package offline package.

#### Import ISO Offline Package to the MinIO on the "bootstrap" Node

Run the following command to import the ISO package to the MinIO file service:

```bash
MINIO_USER=rootuser MINIO_PASS=rootpass123 ./import_iso.sh http://127.0.0.1:9000 ubuntu-16.04.7-server-amd64.iso
```

!!! note

    The above command is only applicable for the built-in MinIO service on the "bootstrap" node.
    If you are using an external MinIO service, please replace "http://127.0.0.1:9000" with the
    access address of your external MinIO. "rootuser" and "rootpass123" are the default credentials
    for the built-in MinIO service on the "bootstrap" node. "ubuntu-16.04.7-server-amd64.iso" should
    be replaced with the actual name of the downloaded ISO offline package.

### Go to create cluster

Refer to [Create Cluster](../user-guide/clusters/create-cluster.md) to create a ubuntu cluster.
