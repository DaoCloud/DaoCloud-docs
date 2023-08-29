# 使用外接服务存储 OS Repo 资源

本文描述如何使用第三方存储服务的 OS Repo 资源并且在安装器安装时进行指定。支持两种类型：S3 兼容服务(如 minio)，非 S3 兼容服务(如 nginx)

## 前提条件

- 根据要部署的环境下载 [ISO 操作系统镜像文件](../start-install.md/#iso)
- 根据要部署的环境下载 [osPackage 离线包](../start-install.md/#ospackage)

## 操作步骤

### 使用 S3 兼容服务

S3 兼容的服务只需要在 [集群配置文件 clusterConfig.yaml](../cluster-config.md) 中简单配置即可，无需其他操作。

1. 在 [集群配置文件 clusterConfig.yaml](../cluster-config.md) 中，配置 `osRepo` 相关的参数：

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

        给定的用户名需要具有 bucket 的读写权限。

### 使用非 S3 兼容服务

非 S3 兼容的服务需要先手动将下载好的 ISO 操作系统镜像文件、osPackage 离线包导入，
然后在[集群配置文件 clusterConfig.yaml](../cluster-config.md) 中配置相关参数。

以下内容以 CentOS 7.9 x86_64 作为集群节点，使用 nignx 作为 http server，
理论上其他通用 http server 也能支持，需要注意 URL 访问路径和文件路径的映射关系。

1. 确保有一个可用的 nginx 服务，及服务所在节点的登录和文件写入权限；

2. 下载/拷贝 ISO 操作系统镜像文件、osPackage 离线包至 nginx 服务所在节点，并将 ISO 导入脚本从火种节点拷贝至 nginx 服务所在节点；

    !!! note

        ISO 导入脚本在[离线包镜像包](../start-install.md/#_2)中，路径为 `./offline/offline-iso/import_iso.sh`

3. 确定需要导入的路径；

    1. 通过 nginx.conf (`nginx -t` 命令查看改文件路径) 检测 nginx 服务所在节点的文件路径和 URL 路径的映射关系，下方示例供参考：

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

       上方配置说明 nginx http 服务的访问根路径映射本地目录 `/usr/share/nginx/html`。

    2. 如果是普通方式部署的 nginx 服务，则选定导入路径为 `/usr/share/nginx/html`。

    3. 如果是容器部署的 nginx 服务，需要挂载宿主机路径至容器，且挂载的宿主机路径对应着映射了 http 服务的容器本地路径，即存在这样的关系：
       `http-path -> container-path -> host-path`。则导入路径应为 host-path，host-path 需要手动按照附录 2 确认。

4. 执行如下命令导入 ISO 操作系统镜像文件、osPackage 离线包：

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

    其中环境变量 MAPPING_PATH 代表步骤 3 中提及的导入路径

5. 验证是否导入成功

    登录一台全局服务集群节点，假设 nignx 访问地址为 `http://10.0.1.1:8080`，参考附录 1 进行配置，执行如下命令：

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

        其他操作系统也是类似操作，因为具体的操作系统的包管理器的软件源配置有一些差异

6. 在 [集群配置文件 clusterConfig.yaml](../cluster-config.md) 中，配置 `osRepo` 相关的参数，`externalRepoURLs` 参考附录 1。

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

7. 完成上述配置后，可以继续执行[部署 DCE 5.0 商业版](../start-install.md)。

### 附录

#### 1. 操作系统与对应的 RepoURLs

`${address_prefix}` 替换为 HTTP 服务的外部访问地址，如 `http://10.0.1.1:8080`

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

#### 2. 查看容器卷挂载列表

| CLI tool | Command |
| --- | --- |
|docker|`docker inspect ${CONTAINER_ID} -f '{{range .Mounts}}{{printf "hostPath: %s containerPath: %s\n" .Source .Destination}}{{end}}'`|
|nerdctl|`nerdctl inspect ${CONTAINER_ID} -f '{{range .Mounts}}{{printf "hostPath: %s containerPath: %s\n" .Source .Destination}}{{end}}'`|
|podman| `podman inspect ${CONTAINER_ID} -f '{{range .Mounts}}{{printf "hostPath: %s containerPath: %s\n" .Source .Destination}}{{end}}'`|
|crictl| `crictl inspect -o go-template --template '{{range .status.mounts}}{{printf "hostPath: %s containerPath: %s\n" .hostPath .containerPath }}{{end}}' ${CONTAINER_ID}`|
|ctr| `ctr c info ${CONTAINER_ID} --spec` 检查 mounts 字段 |
|kubectl|`kubectl -n ${NAMESPACE} get pod ${POD_NAME} -oyaml` 检查 volumes 和 volumeMounts 字段 |
