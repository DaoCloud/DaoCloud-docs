# Preparation

This page describes the preparations necessary for deploying DCE 5.0.

## Machine Preparation

### all-in-one mode

| **Quantity** | **Server Role** | **Server Use**                                    | **CPU Count** | **Memory Capacity** | **System Disk** | **Unpartitioned Disk** |
| ------------ | --------------- | ------------------------------------------------- | ------------- | ------------------ | --------------- | ---------------------- |
| 1            | all in one      | image repository, chart museum, global cluster itself | 16 core       | 32G                | 200G            | 400G                   |

Refer to [all-in-one mode](./deploy-arch.md#all-in-one)

### 4 node mode

| **Quantity** | **Server Role** | **Server Use**                                                                 | **CPU Count** | **Memory Capacity** | **System Disk** | **Unpartitioned Disk** |
| ------------ | --------------- | ------------------------------------------------------------------------------ | ------------- | ------------------ | --------------- | ---------------------- |
| 1            | Bootstrapping Node        | 1. Executes installation deployment program<br />2. Runs the image repository and chart museum required by the platform | 2             | 4G                 | 200G            | -                      |
| 3            | Master          | 1. Runs DCE 5.0 components<br /> 2. Runs Kubernetes system components                   | 8             | 16G                | 100G            | 200G                   |

Refer to [4 node mode](./deploy-arch.md#4)

### 7 node mode

| **Quantity** | **Server Role** | **Server Use**                                                                 | **CPU Count** | **Memory Capacity** | **System Disk** | **Unpartitioned Disk** |
| ------------ | --------------- | ------------------------------------------------------------------------------ | ------------- | ------------------ | --------------- | ---------------------- |
| 1            | Bootstrapping Node        | 1. Executes installation deployment program<br />2. Runs the image repository and chart museum required by the platform | 2             | 4G                 | 200G            | -                      |
| 3            | Master          | 1. Runs DCE 5.0 components<br /> 2. Runs Kubernetes system components                   | 8             | 16G                | 100G            | 200G                   |
| 3            | Worker          | Runs log-related components alone                                           | 8             | 16G                | 100G            | -                      |

Refer to [7 node mode](./deploy-arch.md#7-1-6)

## Pre-check

### Machine check

| **Check Item** | **Specific Requirements** | **Explanation**                                                                                               |
| -------------- | ------------------------ | ------------------------------------------------------------------------------------------------------------ |
| User permission | root                     | Deployment must be done using the root user, and each server must allow root user ssh login.                  |
| Swap           | Disabled                 | If not satisfied, there is a chance of I/O spikes in the system, which can cause the container runtime to freeze. |
| Firewall       | Off (not mandatory)      | -                                                                                                            |
| Selinux        | Off (not mandatory)      | -                                                                                                            |
| Time Sync      | All cluster nodes must have synchronized time | This is a requirement of Docker and Kubernetes. Otherwise, kube.conf will report an error "Unable to connect to the server: x509: certificate has expired or is not yet" |
| Timezone       | All servers must have the same timezone | It is recommended to set it to Asia/Shanghai. <br />Reference command: timedatectl set-timezone Asia/Shanghai |
| Nameserver     | /etc/resolv.conf must have at least one nameserver | Required by coredns, otherwise there will be errors. This nameserver can be a non-existent IP address in a pure offline environment. The default Centos8minial operating system does not have the /etc/resolv file, and it needs to be created manually. |

### Starter Machine Dependency Component Check

| **Check Item**   | **Version Requirement** | **Explanation**                                                                 |
| ---------------- | ---------------------- | ------------------------------------------------------------------------------ |
| podman           | v4.4.1                 | -                                                                              |
| helm             | ≥ 3.11.1               | -                                                                              |
| skopeo           | ≥ 1.11.1               | -                                                                              |
| kind             | v0.17.0                | -                                                                              |
| kubectl          | ≥ 1.25.6               | -                                                                              |
| yq               | ≥ 4.31.1               | -                                                                              |
| minio client     | -                      | `mc.RELEASE.2023-02-16T19-20-11Z`                                                |

If the dependent components do not exist, install them using the script [Install Prerequisites](../install-tools.md).

```bash
# Download script
curl -LO https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/install_prerequisite.sh

# Add execution permission
chmod +x install_prerequisite.sh

# Start with installation
bash install_prerequisite.sh online full
```
