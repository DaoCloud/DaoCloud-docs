# 安装 DCE 5.0

本页简要说明 DCE 5.0 社区版的安装步骤。

## 软硬件环境

目前仅支持 X86_64 架构。

- 主机节点：
    - 正常：1 个 Master，3 个 Worker
    - 高可用：3 个 Master，3 个 Worker

- CPU > 10 核
- 内存 > 10 GB
- 硬盘 > 40 GB

- 操作系统：CentOS 7.0
- Kubernetes 版本：1.24
- 支持的 CRI：Docker 和 containerd

## 在线安装步骤

1. [部署 k8s 集群](install-k8s.md)。

2. [安装所有依赖项](install-tools.md)。

3. 下载并将 DCE 5.0 二进制包复制到 Master 节点

    ```shell
    # 假定 VERSION 为 v0.3.7
    export VERSION=v0.3.7
    curl -Lo ./dce5-installer https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/dce5-installer-${VERSION}
    chmod +x dce5-installer
    ```

4. 编写 clusterConfig.yaml

    - 如果是非公有云环境（虚拟机、物理机），请启用负载均衡 (metallb)，以规避 NodePort 因节点 IP 变动造成的不稳定。请仔细规划您的网络，设置 2 个必要的 VIP，配置文件范例如下：

        ```yaml
        apiVersion: provision.daocloud.io/v1alpha1
        kind: ClusterConfig
        spec:
        LoadBalancer: metallb
        istioGatewayVip: 10.6.229.59/32     # 这是 Istio gateway 的 VIP，用于如控制台等的入口
        insightVip: 10.6.229.57/32          # 这是 Global 集群的 Insight-Server 采集所有子集群的日志/指标/链路的网络路径所用的 VIP
        ```
    
    - 如果是公有云环境，并通过预先准备好的 Cloud Controller Manager 的机制提供了公有云的 k8s 负载均衡能力, 则上述文件改为:

        ``` yaml
        apiVersion: provision.daocloud.io/v1alpha1
        kind: ClusterConfig
        spec:
        LoadBalancer: cloudLB
        ```

    - 如果欲使用 NodePort 暴露控制台（不推荐，仅实验性质），可以不指定任何 clusterConfig 文件，直接执行下一步。

5. 安装 DCE 5.0

    ```
    ./dce5-installer install-app -c clusterConfig.yaml
    ```

## 离线安装步骤

1. [部署 k8s 集群](install-k8s.md)。

2. [安装所有依赖项](install-tools.md)。

3. 下载社区版的对应离线包并解压。

    ``` bash
    # 假定版本 VERSION=0.3.6
    $ wget https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-community-${VERSION}.tar
    $ tar -zxvf offline-community-${VERSION}.tar
    ```

4. 导入镜像。

    - 如果使用镜像仓库，请将离线包的镜像推送到镜像仓库。

        ```bash
        # 指定镜像仓库地址
        $ export REGISTRY_ADDR=registry.daocloud.io:30080
        # 指定离线包解压目录
        $ export OFFLINE_DIR=$(pwd)/offline
        # 执行脚本导入镜像，该脚本内容见下文
        $ ./utils/offline_image_import.sh
        ```

        !!! note

            注: 若导入镜像的过程出现失败, 则失败会被跳过且脚本将继续执行，
            失败镜像信息将被记录在脚本同级目录 `import_image_failed.list` 文件中，便于定位。

    - 如果没有镜像仓库，请将离线包拷贝到每一台节点之后，通过 `docker load/nerdctl load` 加载:

        ```
        脚本 T.B.D
        ```

5. 执行安装命令，通过 -p 指定解压离线包的 offline 目录

    ``` bash
    ./dce5-installer install-app -c clusterConfig.yaml -p offline
    ```

## offline_image_import.sh

为了方便查阅和修改，在此处列出上述离线安装中所调用的 `offline_image_import.sh` 脚本内容：

```bash
#!/bin/bash

OFFLINE_DIR=${OFFLINE_DIR:-"offline"}
REGISTRY_ADDR=${REGISTRY_ADDR:-""}
REGISTRY_USER=${REGISTRY_USER:-""}
REGISTRY_PASS=${REGISTRY_PASS:-""}
CMD_PATH=$(
  cd "$(dirname "$0")"
  pwd
)
IMPORT_FAILED_LIST=${CMD_PATH}/import_image_failed.list

function log_error() {
  echo -e "\033[31m[ERROR]: $1 \033[0m"
}

function log_warn() {
  echo -e "\033[33m[WARN]: $1 \033[0m"
}

function log_info() {
  echo -e "\033[36m[INFO]: $1 \033[0m"
}

function log_debug() {
  echo -e "\033[34m[DEBUG]: $1 \033[0m"
}

function import_images() {
  cat /dev/null >${IMPORT_FAILED_LIST}
  if [ -z "${REGISTRY_ADDR}" ]; then
    log_error "registry address cannot be empty."
    exit 1
  fi
  if [ "${REGISTRY_USER}" != "" ] && [ "${REGISTRY_PASS}" != "" ]; then
    log_debug "skopeo login to ${REGISTRY_ADDR}"
    skopeo login ${REGISTRY_ADDR} -u ${REGISTRY_USER} -p ${REGISTRY_PASS} --tls-verify=false
  fi
  for sub_dir in $(ls -d ${OFFLINE_DIR}/*/); do
    if [ -f "${sub_dir}/images.list" ]; then
      log_info "sync the image files in the ${sub_dir} directory to registry."
      while read -r line; do
        tar_name=$(echo ${line} | awk '{print $1}')
        img_name=$(echo ${line} | awk '{print $2}')
        if [ -z "${tar_name}" ]; then
          log_error "failed to get tar_name for line: ${line}"
          exit 1
        fi
        if [ -z "${img_name}" ]; then
          log_error "failed to get img_name for line: ${line}"
          exit 1
        fi
        log_debug "from ${tar_name} to ${REGISTRY_ADDR}/${img_name}"
        skopeo copy --insecure-policy --retry-times=3 --src-tls-verify=false --dest-tls-verify=false \
          docker-archive:${sub_dir}/${tar_name} docker://${REGISTRY_ADDR}/${img_name}
        if [ $? -ne 0 ]; then
          log_error "skopeo copy ${tar_name} failed!"
          echo "${line}" >>${IMPORT_FAILED_LIST}
          continue
        fi
      done <<<"$(cat ${sub_dir}/images.list)"
    else
      log_warn "skip folder ${sub_dir}"
    fi
  done
}

start=$(date +%s)

import_images

end=$(date +%s)
take=$((end - start))
echo ""
log_info "Time taken to execute commands is ${take} seconds."
```
