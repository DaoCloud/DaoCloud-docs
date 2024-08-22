---
MTPE: windsonsea
Date: 2024-08-22
---

# Create an Ubuntu Worker Cluster on CentOS

This page explains how to create an Ubuntu worker cluster on an existing CentOS.

!!! note

    This page is specifically for the offline mode, using the DCE 5.0 platform to create a worker cluster,
    where both the CentOS platform and the worker cluster to be created are based on AMD architecture. 
    Heterogeneous (mixed AMD and ARM) deployments are not supported during cluster creation; however,
    after the cluster is created, you can manage a mixed deployment by adding heterogeneous nodes.

## Prerequisite

- A fully deployed DCE 5.0 system, with the bootstrap node still active. For deployment reference, see the documentation [Offline Install DCE 5.0 Enterprise](../../install/commercial/start-install.md).

## Download and Import Ubuntu Offline Packages

Please ensure you are logged into the bootstrap node! Also, make sure that the
clusterConfig.yaml file used during the DCE 5.0 deployment is still available.

### Download Ubuntu Offline Packages

Download the required Ubuntu OS packages and ISO offline packages:

| Resource Name | Description | Download Link |
| -------------- | ----------- | -------------- |
| os-pkgs-ubuntu2204-v0.18.2.tar.gz | Ubuntu 20.04 OS package | https://github.com/kubean-io/kubean/releases/download/v0.18.2/os-pkgs-ubuntu2204-v0.18.2.tar.gz |
| ISO Offline Package | ISO Package | http://mirrors.melbourne.co.uk/ubuntu-releases/ |

### Import OS and ISO Packages into MinIO on the Bootstrap Node

Refer to the documentation [Importing Offline Resources](../../install/import.md#introduction-to-import-commands)
to import offline resources into MinIO on the bootstrap node.

## Create Cluster on UI

Refer to the documentation [Creating a Worker Cluster](../user-guide/clusters/create-cluster.md)
to create the Ubuntu cluster.
