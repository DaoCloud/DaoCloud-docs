# 使用外接服务存储 Binaries 资源

本文描述如何使用第三方存储服务存储 Binaries 资源并且在安装器安装时进行指定。
支持两种类型：S3 兼容服务（如 minio）、非 S3 兼容服务（如 nginx）。

## 操作步骤

### 使用 S3 兼容服务

S3 兼容的服务只需要在 [集群配置文件 clusterConfig.yaml](../cluster-config.md) 中简单配置即可，无需其他操作。

1. 配置 clusterConfig.yaml，设置 binaries 相关的参数，如下：

    ```yaml
    apiVersion: provision.daocloud.io/v1alpha3
    kind: ClusterConfig
    metadata:
    spec:
      ..........
      binaries:
        type: external
        externalRepoEndpoint: https://external-repo.daocloud.io
        externalRepoUsername: rootuser
        externalRepoPassword: rootpass123
      ..........
    ```

    !!! note

        给定的用户名需要具有 bucket 的读写权限

### 使用非 S3 兼容服务

非 S3 兼容的服务需要先手动将下载好的[镜像离线包](../start-install.md/#_1) 目录下的 `offline/kubespray-binary/offline-files.tar.gz` binaries 离线包导入，
然后在[集群配置文件 clusterConfig.yaml](../cluster-config.md) 中配置相关参数。

以下内容以 CentOS 7.9 x86_64 作为集群节点，使用 nignx 作为 http server，
理论上其他通用 http server 也能支持，需要注意 URL 访问路径和文件路径的映射关系。

1. 确保有一个可用的 nginx 服务，及服务所在节点的登录和文件写入权限；
2. 将 binaries 离线包从火种节点（<解压后离线包路径>/offline/kubespray-binary/offline-files.tar.gz, <解压后离线包路径>/offline/component-tools.tar.gz）拷贝至 nginx 服务所在节点；

    !!! note

        binaries 离线包路径为 `./offline/kubespray-binary/offline-files.tar.gz`

3. 确定需要导入的路径;

    1. 通过 `nginx.conf` 检测 nginx 服务所在节点的文件路径和 URL 路径的映射关系，下方示例供参考：

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

        上方配置说明 nginx http服务的访问根路径映射本地目录 `/usr/share/nginx/html`

    2. 如果是普通方式部署的 nginx 服务，则选定导入路径为 `/usr/share/nginx/html`

    3. 如果是容器部署的 nginx 服务，需要挂载宿主机路径至容器，且挂载的宿主机路径对应着映射了 http 服务的容器本地路径，
       即存在这样的关系： `http-path -> container-path -> host-path`。则导入路径应为 host-path。host-path 需要手动按照附录确认。

4. 执行如下命令导入离线 binaries 离线包：

    ```bash
    cat > import.sh << "EOF"
    [ ! -d "${MAPPING_PATH}" ] && echo "mapping path ${MAPPING_PATH} not found" && exit 1
    [ ! -f "${BINARIRES_PKG_PATH}" ] && echo "binaries package path ${BINARIRES_PKG_PATH} not found" && exit 1
    [ ! -f "${COMPONENT_TOOLS_PATH}" ] && echo "comonent-tools package path ${COMPONENT_TOOLS_PATH} not found" && exit 1
    tar -xzvf ${BINARIRES_PKG_PATH} --strip-components=1 -C ${MAPPING_PATH}
    tar -xzvf ${COMPONENT_TOOLS_PATH} --strip-components=1 -C ${MAPPING_PATH}
    EOF
    export MAPPING_PATH="/usr/share/nginx/html"
    export BINARIRES_PKG_PATH="./offline-files.tar.gz"
    export COMPONENT_TOOLS_PATH="./component-tools.tar.gz"
    bash ./import.sh
    ```

    其中环境变量 `MAPPING_PATH` 代表步骤 3 中提及的导入路径。

5. 在 [集群配置文件 clusterConfig.yaml](../cluster-config.md) 中，配置 `binaries` 相关的参数。

    ```yaml
    apiVersion: provision.daocloud.io/v1alpha3
    kind: ClusterConfig
    metadata:
    spec:
      ..........
      binaries:
        type: external
        externalRepoEndpoint: http://10.0.1.1:8080
      ..........
    ```

6. 完成上述配置后，可以继续执行[部署 DCE 5.0 商业版](../start-install.md)。

### 附录

查看容器卷挂载列表：

| CLI tool | Command |
| --- | --- |
|docker|`docker inspect ${CONTAINER_ID} -f '{{range .Mounts}}{{printf "hostPath: %s containerPath: %s\n" .Source .Destination}}{{end}}'`|
|nerdctl|`nerdctl inspect ${CONTAINER_ID} -f '{{range .Mounts}}{{printf "hostPath: %s containerPath: %s\n" .Source .Destination}}{{end}}'`|
|podman| `podman inspect ${CONTAINER_ID} -f '{{range .Mounts}}{{printf "hostPath: %s containerPath: %s\n" .Source .Destination}}{{end}}'`|
|crictl| `crictl inspect -o go-template --template '{{range .status.mounts}}{{printf "hostPath: %s containerPath: %s\n" .hostPath .containerPath }}{{end}}' ${CONTAINER_ID}`|
|ctr| `ctr c info ${CONTAINER_ID} --spec` 检查 mounts 字段 |
|kubectl|`kubectl -n ${NAMESPACE} get pod ${POD_NAME} -oyaml` 检查 volumes 和 volumeMounts 字段 |
