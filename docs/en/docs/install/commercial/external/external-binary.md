# Using External Service to Store Binaries Resources

This document describes how to use third-party storage services to store Binaries resources and specify them during the installation process. There are two types of supported services: S3 compatible services (such as Minio) and non-S3 compatible services (such as Nginx).

## Steps

### Using S3 Compatible Service

For S3 compatible services, simply configure the [clusterConfig.yaml](../cluster-config.md), no further operations are required.

1. Configure the clusterConfig.yaml file by setting the parameters related to binaries as follows:

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

        The given username should have read and write permissions for the bucket.

### Using Non-S3 Compatible Service

For non-S3 compatible services, you need to manually import the offline binaries package `offline/kubespray-binary/offline-files.tar.gz` from the downloaded [image offline package](../start-install.md/#_1) directory,
and then configure the relevant parameters in the [clusterConfig.yaml](../cluster-config.md).

The following instructions assume that CentOS 7.9 x86_64 is used as the cluster node and Nginx is used as the HTTP server.
In theory, other generic HTTP servers can also be supported, but pay attention to the mapping relationship between URL access paths and file paths.

1. Ensure that an available Nginx service exists, and the node where the service resides has login and file writing permissions.
2. Copy the binaries offline package from the ignition node to the node where the nginx service is located.

    !!! note

        The path of the binaries offline package is `./offline/kubespray-binary/offline-files.tar.gz`

3. Determine the path that needs to be imported;

    1. Check the mapping relationship between the file path and the URL path on the Nginx service node through `nginx.conf`. The following example can be used as a reference:

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

        The above configuration indicates that the access root path of the nginx HTTP service is mapped to the local directory `/usr/share/nginx/html`.

    2. If Nginx is deployed in the conventional way, select the import path as `/usr/share/nginx/html`.
    3. If Nginx is deployed in a container, you need to mount the host path to the container, and the mounted host path corresponds to the mapped local path of the HTTP service in the container.
       That is, there is such a relationship: `http-path -> container-path -> host-path`. Therefore, the import path should be the host-path. The host-path needs to be confirmed manually according to the appendix.

4. Run the following command to import the offline binaries package:

    ```bash
    cat > import.sh << "EOF"
    [ ! -d "${MAPPING_PATH}" ] && echo "mapping path ${MAPPING_PATH} not found" && exit 1
    [ ! -f "${BINARIES_PKG_PATH}" ] && echo "binaries package path ${BINARIES_PKG_PATH} not found" && exit 1
    tar -xzvf ${BINARIES_PKG_PATH} --strip-components=1 -C ${MAPPING_PATH}
    EOF
    export MAPPING_PATH="/usr/share/nginx/html"
    export BINARIES_PKG_PATH="./offline-files.tar.gz"
    bash ./import.sh
    ```

    In the above command, the environment variable `MAPPING_PATH` represents the import path mentioned in step 3.

5. In the [clusterConfig.yaml](../cluster-config.md), configure the parameters related to `binaries`.

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

6. After completing the above configurations, you can continue with the [deployment of DCE 5.0 Enterprise](../start-install.md).

### Appendix

View container volume mount list:

| CLI tool | Command |
| --- | --- |
|docker|`docker inspect ${CONTAINER_ID} -f '{{range .Mounts}}{{printf "hostPath: %s containerPath: %s\n" .Source .Destination}}{{end}}'`|
|nerdctl|`nerdctl inspect ${CONTAINER_ID} -f '{{range .Mounts}}{{printf "hostPath: %s containerPath: %s\n" .Source .Destination}}{{end}}'`|
|podman| `podman inspect ${CONTAINER_ID} -f '{{range .Mounts}}{{printf "hostPath: %s containerPath: %s\n" .Source .Destination}}{{end}}'`|
|crictl| `crictl inspect -o go-template --template '{{range .status.mounts}}{{printf "hostPath: %s containerPath: %s\n" .hostPath .containerPath }}{{end}}' ${CONTAINER_ID}`|
|ctr| `ctr c info ${CONTAINER_ID} --spec` Check the mounts field |
|kubectl|`kubectl -n ${NAMESPACE} get pod ${POD_NAME} -oyaml` Check the volumes and volumeMounts fields |
