# Preparation

This page explains the preparation required for deploying DCE 5.0 Enterprise package.

## Host Requirements

### All-in-One Mode

Refer to [All-in-One Mode](./deploy-arch.md#all-in-one).

| **Number** | **Server Role** | **Server Purpose**                               | **CPU Cores** | **Memory** | **System Disk** | **Unpartitioned Disk** |
| ---------- | --------------- | ------------------------------------------------ | ------------- | ---------- | -------------- | ---------------------- |
| 1          | all in one      | container registry, chart museum, global cluster | 16            | 32G        | 200G           | 400G                   |

### 4-Nodes Mode

Refer to [4 Nodes Mode](./deploy-arch.md#4).

| **Number** | **Server Role** | **Server Purpose**                                             | **CPU Cores** | **Memory** | **System Disk** | **Unpartitioned Disk** |
| ---------- | --------------- | -------------------------------------------------------------- | ------------- | ---------- | -------------- | ---------------------- |
| 1          | Bootstraping Node       | 1. Run installation and deployment procesures<br />2. Host image registry and chart museum required by DCE 5.0 | 2             | 4G         | 200G           | -                      |
| 3          | Controller Node          | 1. Run DCE 5.0 submodules<br />2. Run Kubernetes system components | 8             | 16G        | 100G           | 200G                   |

### 7-Nodes Mode

Refer to [7 Nodes Mode](./deploy-arch.md#7-1-6).

| **Number** | **Server Role** | **Server Purpose**                                             | **CPU Cores** | **Memory** | **System Disk** | **Unpartitioned Disk** |
| ---------- | --------------- | -------------------------------------------------------------- | ------------- | ---------- | -------------- | ---------------------- |
| 1          | Bootstraping Node       | 1. Run installation and deployment procedures<br />2. Host image registry and chart museum required by DCE 5.0 | 2             | 4G         | 200G           | -                      |
| 3          | Controller Node          | 1. Run DCE 5.0 submodules<br />2. Run Kubernetes system components   | 8             | 16G        | 100G           | 200G

## Prerequisites Check

### Machine Check

| **Check Item** | **Requirements**               | **Description**                                                                                                                                                                                                                                                               |
| -------------- | ---------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| User Permissions | root                                      | Use root root account to install DCE 5.0, and the root user must be allowed to log into all all servers by SSH.                                                                                                                                                                 |
| Swap             | Turn off                                  | If it's turned on, the system may experience an I/O surge, causing the container runtime crash.                                                                                                                                        |
| Firewall        | Turn off (not mandatory)                  | -                                                                                                                                                                                                                                                                             |
| Selinux         | Turn off (not mandatory)                  | -                                                                                                                                                                                                                                                                             |
| Time syn| All nodes must have synchronized time. | This is explicitly required by Docker and Kubernetes. Otherwise, `kube.conf` will report an error of`Unable to connect to the server: x509: certificate has expired or is not yet`.                                                                                               |
| Time zone       | The time zone of all servers must be consistent. | It is recommended to set as Asia/Shanghai. <br />Command: timedatectl set-timezone Asia/Shanghai                                                                                                                                                              |
| Nameserver      | `/etc/resolv.conf` must have at least one nameserver. | Required for CoreDNS, otherwise there will be an error. This nameserver can be a non-existent IP address in a pure offline environment. Centos8minial does not have the `/etc/resolv` file by default and needs to be created manually. |

### Bootstraping Node Dependency Check

| **Check Item**   | **Versions** | **Description** |
| ---------------- |-------------| --------------- |
| podman           | v4.4.1      | -               |
| helm             | ≥ 3.11.1    | -               |
| skopeo           | ≥ 1.11.1    | -               |
| kind             | v0.19.0     | -               |
| kubectl          | ≥ 1.25.6    | -               |
| yq               | ≥ 4.31.1    | -               |
| MinIO client     | `mc.RELEASE.2023-02-16T19-20-11Z`            | -|

If these dependencies have not been installed, refer to [Install Dependencies](../install-tools.md)。

```bash
export VERSION=v0.9.0
# download install script
curl -LO https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/install_prerequisite_${VERSION}.sh

# add execution permission
chmod +x install_prerequisite_${VERSION}.sh

# start install
bash install_prerequisite_${VERSION}.sh online full
```

## External Component Preparation

If you need to use existing components from the customer, you can refer to the following documents for preparation:

- [Using External Service to Store Binary Resources](external/external-binary.md)

- [Using External Image and Chart Repositories to Store Images and Chart Packages](external/external-imageandchart.md)

- [Using External Middleware Services](external/external-middlewares.md)

- [Using External Service to Store OS Repo Resources](external/external-os.md)
