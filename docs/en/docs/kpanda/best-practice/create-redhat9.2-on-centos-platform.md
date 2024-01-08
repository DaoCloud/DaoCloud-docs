# Create a RedHat 9.2 Working Cluster on a CentOS Management Platform

This article explains how to create a RedHat 9.2 working cluster on an existing CentOS management platform.

!!! note

    This article only applies to the offline mode, using the DCE 5.0 platform to create a working cluster. The architecture of the management platform and the cluster to be created are both AMD.
    When creating a cluster, heterogeneous deployment (mixing AMD and ARM) is not supported. After the cluster is created, you can use the method of connecting heterogeneous nodes to achieve mixed deployment and management of the cluster.

## Prerequisites

A DCE 5.0 full-mode has been deployed, and the spark node is still alive. For deployment, see the document [Offline Installation of DCE 5.0 Commercial Edition](../../install/commercial/start-install.md).

## Download and Import RedHat Offline Packages

Make sure you are logged into the spark node! And the clusterConfig.yaml file used when deploying DCE 5.0 is still available.

### Download the Relevant RedHat Offline Packages

Download the required RedHat OS package and ISO offline packages:

| Resource Name | Description | Download Link |
| ------------- | ----------- | ------------- |
| os-pkgs-redhat9-v0.9.3.tar.gz | RedHat9.2 OS-package package | [Download](https://github.com/kubean-io/kubean/releases/download/v0.9.3/os-pkgs-redhat9-v0.9.3.tar.gz) |
| ISO Offline Package | ISO package import script | Go to [RedHat Official Download Site](https://access.cdn.redhat.com/content/origin/files/sha256/a1/a18bf014e2cb5b6b9cee3ea09ccfd7bc2a84e68e09487bb119a98aa0e3563ac2/rhel-9.2-x86_64-dvd.iso?user=cb58db6b16a8cf7e24021ebac6be33e8&_auth_=1698145622_cdb9984fa8440b24f4e126ec2e368c82) |
| import-iso | ISO import script | [Download](https://github.com/kubean-io/kubean/releases/download/v0.9.3/import_iso.sh) |

### Import the OS Package to the MinIO of the Spark Node

**Extract the RedHat OS package**

Execute the following command to extract the downloaded OS package. Here we download the RedHat OS package.

```bash
tar -xvf os-pkgs-redhat9-v0.9.3.tar.gz
```

The contents of the extracted OS package are as follows:

```text
    os-pkgs
    ├── import_ospkgs.sh       # This script is used to import OS packages into the MinIO file service
    ├── os-pkgs-amd64.tar.gz   # OS packages for the amd64 architecture
    ├── os-pkgs-arm64.tar.gz   # OS packages for the arm64 architecture
    └── os-pkgs.sha256sum.txt  # sha256sum verification file of the OS packages
```

**Import the OS Package to the MinIO of the Spark Node**

Execute the following command to import the OS packages to the MinIO file service:

```bash
MINIO_USER=rootuser MINIO_PASS=rootpass123 ./import_ospkgs.sh  http://127.0.0.1:9000 os-pkgs-redhat9-v0.9.3.tar.gz
```

!!! note

    The above command is only applicable to the MinIO service built into the spark node. If an external MinIO is used, replace `http://127.0.0.1:9000` with the access address of the external MinIO.
    "rootuser" and "rootpass123" are the default account and password of the MinIO service built into the spark node. "os-pkgs-redhat9-v0.9.3.tar.gz"
    is the name of the downloaded OS package offline package.

### Import the ISO Offline Package to the MinIO of the Spark Node

Execute the following command to import the ISO package to the MinIO file service:

```bash
MINIO_USER=rootuser MINIO_PASS=rootpass123 ./import_iso.sh http://127.0.0.1:9000 rhel-9.2-x86_64-dvd.iso
```

!!! note

    The above command is only applicable to the MinIO service built into the spark node. If an external MinIO is used, replace `http://127.0.0.1:9000` with the access address of the external MinIO.
    "rootuser" and "rootpass123" are the default account and password of the MinIO service built into the spark node.
    "rhel-9.2-x86_64-dvd.iso" is the name of the downloaded ISO offline package.

## Create the Cluster in the UI

Refer to the document [Creating a Working Cluster](../user-guide/clusters/create-cluster.md) to create a RedHat 9.2 cluster.
