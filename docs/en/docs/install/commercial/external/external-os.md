# Using External Service to Store OS Repo Resources

This document describes how to use a third-party storage service for OS repo resources and specify it during the installer installation. There are two supported types: S3-compatible services (such as MinIO) and non-S3-compatible services (such as Nginx).

## Prerequisites

- Download the [ISO operating system image file](../start-install.md/#iso) according to the environment to be deployed.
- Download the [osPackage offline package](../start-install.md/#ospackage) according to the environment to be deployed.

## Procedure

### Using S3-Compatible Service

Configuring an S3-compatible service is straightforward and requires only simple configuration in the [clusterConfig.yaml](../cluster-config.md). No further actions are needed.

1. In the [clusterConfig.yaml](../cluster-config.md), configure the `osRepo` related parameters:

    ```yaml
    apiVersion: provision.daocloud.io/v1alpha3
    kind: ClusterConfig
    metadata:
    spec:
    ..........
    osRepos:
        type: external
        isoPath: "/root/CentOS-7-x86_64-DVD-2009.iso"
        osPackagePath: "/root/os-pkgs-centos7-v0.4.4.tar.gz"
        externalRepoEndpoint: https://external-repo.daocloud.io
        externalRepoUsername: rootuser
        externalRepoPassword: rootpass123
    ..........
    ```

    !!! note

        The given username should have read and write permissions for the bucket.

### Using Non-S3-Compatible Service

For non-S3-compatible services, you need to manually import the downloaded ISO operating system image file and osPackage offline package. Then, configure the relevant parameters in the [clusterConfig.yaml](../cluster-config.md).

The following content assumes that CentOS 7.9 x86_64 is used as the cluster node, and Nginx is used as the HTTP server. In theory, other commonly used HTTP servers should also be supported, but you need to pay attention to the mapping relationship between the URL access path and file path.

1. Ensure that an available Nginx service exists with login and file writing permissions on the node where the service is located.

2. Download/copy the ISO operating system image file and osPackage offline package to the node where the Nginx service is located. Also, copy the ISO import script from the bootstrap node to the node where the Nginx service is located.

    !!! note

        The ISO import script is located in the [offline package](../start-install.md/#_2) at the path `./offline/offline-iso/import_iso.sh`.

3. Determine the path to import:

   - To check the mapping relationship between the file path on the Nginx service node and the URL path, use the nginx.conf file (`nginx -t` command to view the file path). The example below is provided for reference:

        ```bash
        http {
            server {
                listen       8080;
                server_name  _;
                location / {
                    root   /usr/share/nginx/html;
                    index  index.html index.htm;
                }
            }
        }
        ```

       The above configuration indicates that the root path for accessing the nginx HTTP service is mapped to the local directory `/usr/share/nginx/html`.

   - If Nginx service is deployed in the usual way, select the import path as `/usr/share/nginx/html`.

   - If Nginx service is deployed in a container, the host path should be mounted into the container, and the mounted host path corresponds to the mapped local path of the container's HTTP service. This means that there is a relationship as follows: `http-path -> container-path -> host-path`. The import path should be the host-path, which needs to be manually confirmed according to Appendix 2.

4. Run the following command to import the ISO operating system image file and osPackage offline package:

    ```bash
    cat > import.sh << "EOF"
    [ ! -d "${MAPPING_PATH}" ] && echo "mapping path ${MAPPING_PATH} not found" && exit 1
    [ ! -x "${ISO_IMPORT_SH_PATH}" ] && echo "iso import script ${ISO_IMPORT_SH_PATH} not found or not executable" && exit 1
    [ ! -f "${OS_PKGS_PATH}" ] && echo "os pkgs ${OS_PKGS_PATH} not found" && exit 1
    [ ! -f "${ISO_PATH}" ] && echo "iso ${ISO_PATH} not found" && exit 1
    tar -xzvf ${OS_PKGS_PATH} && for arch in amd64 arm64; do tar --strip-components=1 -xzvf os-pkgs/os-pkgs-${arch}.tar.gz -C ${MAPPING_PATH}; done && rm -rf os-pkgs
    bash ${ISO_IMPORT_SH_PATH} ${MAPPING_PATH} ${ISO_PATH}
    EOF
    export MAPPING_PATH="/usr/share/nginx/html"
    export ISO_IMPORT_SH_PATH="./import_iso.sh"
    export OS_PKGS_PATH="./os-pkgs-centos7-v0.4.5-rc3.tar.gz"
    export ISO_PATH="./CentOS-7-x86_64-DVD-2009.iso"
    bash ./import.sh
    ```

    The environment variable `MAPPING_PATH` represents the import path mentioned in step 3.

5. Verify the successful import

   Log in to a node in the global service cluster. Assuming the Nginx access address is `http://10.0.1.1:8080`, refer to Appendix 1 for configuration and run the following command:

    ```bash
    cat > /etc/yum.repos.d/test.repo << "EOF"
    [test0]
    baseurl = http://10.1.1.1:8080/centos/$releasever/os/$basearch
    gpgcheck = 0
    name = test0
    
    [test1]
    baseurl = http://10.1.1.1:8080/kubean/centos-iso/$releasever/os/$basearch
    gpgcheck = 0
    name = test0
    EOF
    yum clean all && yum makecache --disablerepo=* --enablerepo=test0,test1
    ```

    !!! note

        The same steps can be applied to other operating systems as well, as the software source configuration
        for each specific operating system's package manager may have some differences.

6. In the [clusterConfig.yaml](../cluster-config.md), configure the `osRepo` related parameters, and for `externalRepoURLs`, refer to Appendix 1.

    ```yaml
    apiVersion: provision.daocloud.io/v1alpha3
    kind: ClusterConfig
    metadata:
    spec:
      ..........
      osRepos:
        type: external
        # `centos` as CentOS, RedHat,kylin AlmaLinux or Fedora,Openeuler
        # `debian` as Debian
        # `ubuntu` as Ubuntu
        externalRepoType: centos
        externalRepoURLs:
          - 'http://10.0.1.1:8080/centos/\$releasever/os/\$basearch/'
          - 'http://10.0.1.1:8080/centos-iso/\$releasever/os/\$basearch/'
      ..........
    ```

7. After completing the above configuration, you can proceed with [deploying DCE 5.0 Enterprise](../start-install.md).

### Appendix

#### 1. Operating Systems and Corresponding RepoURLs

Replace `${address_prefix}` with the external access address of the HTTP service, such as `http://10.0.1.1:8080`.

| OS | RepoURLs |
| --- | --- |
| CentOS| ['\${address_prefix}/centos/\\\$releasever/os/\\\$basearch','\${address_prefix}/centos-iso/\\\$releasever/os/\\\$basearch'] |
| RedHat | ['\${address_prefix}/redhat/\\\$releasever/os/\\\$basearch','\${address_prefix}/redhat-iso/\\\$releasever/os/\\\$basearch/BaseOS','\${address_prefix}/redhat-iso/\\\$releasever/os/\\\$basearch/AppStream'] |
| Kylin V10| ['\${address_prefix}/kubean/kylin/\\\$releasever/os/\\\$basearch','\${address_prefix}/kubean/kylin-iso/\\\$releasever/os/\\\$basearch'] |
| UOS V20| ['\${address_prefix}/kubean/uos/\\\$releasever/os/\\\$basearch','\${address_prefix}/kubean/uos-iso/\\\$releasever/os/\\\$basearch/AppStream','\${address_prefix}/kubean/uos-iso/\\\$releasever/os/\\\$basearch/BaseOS'] |
| Oracle 9 | ['\${address_prefix}/kubean/oracle/\\\$releasever/os/\\\$basearch','\${address_prefix}/kubean/oracle-iso/\\\$releasever/os/\\\$basearch/AppStream','\${address_prefix}/kubean/oracle-iso/\\\$releasever/os/\\\$basearch/BaseOS'] |
| OpenEuler 20.03 | ['\${address_prefix}/kubean/openeuler/22.03/os/\\\$basearch','\${address_prefix}/kubean/openeuler-iso/22.03/os/\\\$basearch'] |
| Ubuntu bionic | ['deb [trusted=yes] \${address_prefix}/kubean/ubuntu/amd64 bionic/','deb [trusted=yes] \${address_prefix}/kubean/ubuntu-iso bionic main restricted'] |
| Ubuntu focal | ['deb [trusted=yes] \${address_prefix}/kubean/ubuntu/amd64 focal/','deb [trusted=yes] \${address_prefix}/kubean/ubuntu-iso focal main restricted']|

#### 2. View the list of mounted volumes for containers

| CLI tool | Command |
| --- | --- |
|docker|`docker inspect ${CONTAINER_ID} -f '{{range .Mounts}}{{printf "hostPath: %s containerPath: %s\n" .Source .Destination}}{{end}}'`|
|nerdctl|`nerdctl inspect ${CONTAINER_ID} -f '{{range .Mounts}}{{printf "hostPath: %s containerPath: %s\n" .Source .Destination}}{{end}}'`|
|podman| `podman inspect ${CONTAINER_ID} -f '{{range .Mounts}}{{printf "hostPath: %s containerPath: %s\n" .Source .Destination}}{{end}}'`|
|crictl| `crictl inspect -o go-template --template '{{range .status.mounts}}{{printf "hostPath: %s containerPath: %s\n" .hostPath .containerPath }}{{end}}' ${CONTAINER_ID}`|
|ctr| `ctr c info ${CONTAINER_ID} --spec` check the mounts field |
|kubectl|`kubectl -n ${NAMESPACE} get pod ${POD_NAME} -oyaml` Check the volumes and volumeMounts fields |
