# 安装依赖项

[部署好 k8s 集群](install-k8s.md)后，若想安装 DCE 5.0，还需要安装一些依赖项。

## 一条命令安装所有依赖项

在 k8s 集群的某一台 master 节点上，执行以下一条命令安装依赖项：

```shell
curl -s https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/install_prerequisite.sh | bash
```

!!! note

    这条命令中的脚本内容见下文。目前此脚本安装的依赖项包括：

    - Docker 17.03.2
    - helm 3.9.4
    - skopeo 1.9.2
    - kind 0.15.0
    - kubectl 1.25.0
    - yq 4.27.5
    - minio 

## 离线安装依赖项

离线安装意味着目标主机的网络处于离线状态，无法下载上述工具的文件及压缩包，所以需要先在一个在线环境中制作好所需的离线包。

1. 制作离线包的命令如下:

    ```bash
    bash install_prerequisite.sh export
    ```

2. 当上述命令执行完成后, 会在当前目录生成名为 `pre_pkgs.tar.gz` 的压缩包, 该压缩包中会包含安装所需的所有文件。

    然后上传脚本及压缩包到离线环境中，并执行离线安装：

    ``` bash
    # 脚本与离线包都位于同一目录层级
    $ tree .
    .
    ├── install_prerequisite.sh
    └── pre_pkgs.tar.gz

    # 执行离线安装
    $ bash install_prerequisite.sh offline
    ```

## install_prerequisite.sh

为了方便查阅和修改，在此处列出上述命令中所调用的 .sh 脚本内容：

```shell
#!/bin/bash
#
# 目前支持在线和离线两种模式。
# 现在仅适用于 CentOS X86-64！！！
set -e

OPTION=${1:-'online'}
BINARY_PATH="pre_pkgs"
BINARY_TAR_FILE=${BINARY_TAR_FILE:-"${BINARY_PATH}.tar.gz"}

################# 二进制文件下载的配置如下 #################
ARCH=amd64

# name: docker-ce
DOCKER_VERSION="18.06.3"
DOCKER_TAR_NAME="docker-${DOCKER_VERSION}-ce.tgz"
DOCKER_TAR_URL="https://mirrors.aliyun.com/docker-ce/linux/static/stable/x86_64/${DOCKER_TAR_NAME}"

# name: helm
HELM_VERSION="v3.9.4"
HELM_TAR_NAME="helm-${HELM_VERSION}-linux-${ARCH}.tar.gz"
HELM_TAR_URL="https://files.m.daocloud.io/get.helm.sh/${HELM_TAR_NAME}"

# name: skopeo
SKOPEO_VERSION="v1.9.2"
SKOPEO_BINARY_NAME="skopeo-linux-${ARCH}"
SKOPEO_BINARY_URL="https://files.m.daocloud.io/github.com/lework/skopeo-binary/releases/download/${SKOPEO_VERSION}/${SKOPEO_BINARY_NAME}"

# name: kind
KIND_VERSION="v0.15.0"
KIND_BINARY_NAME="kind-linux-${ARCH}"
KIND_BINARY_URL="https://files.m.daocloud.io/github.com/kubernetes-sigs/kind/releases/download/${KIND_VERSION}/${KIND_BINARY_NAME}"

# name: kubectl
KUBECTL_VERSION="v1.25.0"
KUBECTL_BINARY_NAME="kubectl"
KUBECTL_BINARY_URL="files.m.daocloud.io/storage.googleapis.com/kubernetes-release/release/${KUBECTL_VERSION}/bin/linux/${ARCH}/${KUBECTL_BINARY_NAME}"

# name: yq
YQ_VERSION="v4.27.5"
YQ_BINARY_NAME="yq_linux_${ARCH}"
YQ_BINARY_URL="https://files.m.daocloud.io/github.com/mikefarah/yq/releases/download/${YQ_VERSION}/${YQ_BINARY_NAME}"

# name: minio client
MC_BINARY_NAME="mc"
MC_BINARY_URL="https://dl.min.io/client/mc/release/linux-${ARCH}/${MC_BINARY_NAME}"

##################################
function prerequisite::install_kind() {
  if ! [ -x "$(command -v kind)" ]; then
    echo "install kind"
    mv ${BINARY_PATH}/${KIND_BINARY_NAME} /usr/local/bin/kind
    chmod +x /usr/local/bin/kind
    kind version
  fi
}

##################################
function prerequisite::install_yq() {
  if ! [ -x "$(command -v yq)" ]; then
    echo "install yq"
    mv ${BINARY_PATH}/${YQ_BINARY_NAME} /usr/local/bin/yq
    chmod +x /usr/local/bin/yq
    yq --version
  fi
}

###############################
# copied from common::version_lt
##############################
function version_le() {
  # <=
  [ "$1" == "$(echo -e "$1\n$2" | sort -V | head -n1)" ]
}
function version_lt() {
  # <
  [ "$1" == "$2" ] && return 1 || version_le $1 $2
}

##################################
function prerequisite::install_helm() {
  if ! [ -x "$(command -v helm)" ]; then
    echo "install helm"
    tar -zxvf ${BINARY_PATH}/${HELM_TAR_NAME}
    mv linux-${ARCH}/helm /usr/local/bin/helm
    helm version
  else
    local helmVer=$(helm version --short | cut -b 2-6)
    if $(version_lt $helmVer "3.9.0"); then
      echo "Warning: Ensure helm version >= 3.9.1. Current helm version=$helmVer"
    fi
  fi
}

##################################
function prerequisite::install_docker() {
  if ! [ -x "$(command -v docker)" ] &&
    ! [ -x "$(command -v podman)" ] &&
    ! [ -x "$(command -v crictl)" ] &&
    ! [ -x "$(command -v nerdctl)" ] &&
    ! [ -x "$(command -v ctr)" ]; then
    echo "install docker ${DOCKER_VERSION}"
    tar -zxvf ${BINARY_PATH}/${DOCKER_TAR_NAME}
    sudo cp docker/* /usr/bin/ && rm -rf docker/
    if [ ! -d /etc/systemd/system ]; then
      echo "[Error] script only supports CentOS 7 for now...."
      exit 0
    fi
    cat <<EOF >>/etc/systemd/system/docker.service
    [Service]
    ExecStart=
    ExecStart=/usr/bin/dockerd
EOF

    sudo systemctl daemon-reload
    sudo systemctl restart docker
  fi
}

#################################
function prerequisite::install_skopeo() {
  local currentVer=""
  if [ -x "$(command -v skopeo)" ]; then
    currentVer=$(skopeo --version | awk '{print $NF}')
  fi
  if [ ! -x "$(command -v skopeo)" ] || $(version_lt "$currentVer" "1.3.0"); then
    echo "install skopeo or upgrade skopeo($currentVer)"
    mv ${BINARY_PATH}/${SKOPEO_BINARY_NAME} /usr/local/bin/skopeo
    chmod +x /usr/local/bin/skopeo
    skopeo -v
  fi
}

##################################
function prerequisite::install_mc() {
  if [ ! -x "$(command -v mc)" ]; then
    echo "install minio client"
    mv ${BINARY_PATH}/${MC_BINARY_NAME} /usr/local/bin/mc
    chmod +x /usr/local/bin/mc
    mc -v
  fi
}

##################################
function prerequisite::install_kubectl() {
  if [ ! -x "$(command -v kubectl)" ]; then
    echo "install kubectl"
    mv ${BINARY_PATH}/${KUBECTL_BINARY_NAME} /usr/local/bin/kubectl
    chmod +x /usr/local/bin/kubectl
    kubectl version --client --short
  fi
}

##################################
function export_packages() {
  urls_list=(${DOCKER_TAR_URL} ${HELM_TAR_URL} ${SKOPEO_BINARY_URL} ${KIND_BINARY_URL} ${KUBECTL_BINARY_URL} ${YQ_BINARY_URL} ${MC_BINARY_URL})
  mkdir -p ${BINARY_PATH}
  for url in ${urls_list[@]}; do
    printf "Current package url: %s\n" "${url}"
    (cd ${BINARY_PATH} && curl -C - --retry 10 --retry-max-time 60 -LO ${url})
  done
  ls -lh ${BINARY_PATH}
  tar -zcvf ${BINARY_TAR_FILE} ${BINARY_PATH}
  rm -rf ${BINARY_PATH}
  echo ""
  echo "$(pwd)/${BINARY_TAR_FILE} is created to contain your prerequisite packages."
  echo "Please keep this file and bring it to your offline environment."
}

##################################
function install_packages() {
  tar -zxvf ${BINARY_TAR_FILE}

  prerequisite::install_docker
  prerequisite::install_helm
  prerequisite::install_skopeo
  prerequisite::install_kind
  prerequisite::install_kubectl
  prerequisite::install_yq
  prerequisite::install_mc
}

start=$(date +%s)

case $OPTION in
export)
  export_packages
  ;;

offline)
  install_packages
  ;;

online)
  export_packages
  install_packages
  ;;

*)
  echo -n "unknown operator"
  ;;
esac

end=$(date +%s)
take=$((end - start))
echo ""
echo "Time taken to execute commands is ${take} seconds."
```
