# 边缘集群部署和管理实践

对于资源受限的边缘或物联网场景，Kubernetes 无法很好的满足资源要求，为此需要一个轻量化 Kubernetes 方案，
既能实现容器管理和编排能力，又能给业务应用预留更多资源空间。本文介绍边缘集群 k3s 的部署和全生命周期管理实践。

## 节点规划

**架构**

- x86_64
- armhf
- arm64/aarch64

**操作系统**

- 可以在大多数现代 Linux 系统上工作

**CPU/内存**

- 单节点 K3s 集群

    |             | 最小 CPU | 推荐 CPU | 最小内存 | 推荐内存 |
    | :---------- | :------- | -------- | -------- | -------- |
    | K3s cluster | 1 core   | 2 cores  | 1.5 GB   | 2 GB     |

- 多节点 K3s 集群

    |            | 最小 CPU | 推荐 CPU | 最小内存 | 推荐内存 |
    | :--------- | :------- | -------- | -------- | -------- |
    | K3s server | 1 core   | 2 cores  | 1 GB     | 1.5 GB   |
    | K3s agent  | 1 core   | 2 cores  | 512 MB   | 1 GB     |

- 节点入站规则

    - 根据需要确保以下端口未被占用
    - 若有特殊要求不能关闭防火墙，需确保端口为放行

    | 协议 | 端口      | 源        | 目的      | 描述                                    |
    | :--- | :-------- | :-------- | :-------- | :-------------------------------------- |
    | TCP  | 2379-2380 | Servers   | Servers   | 适用于 HA与嵌入式etcd                   |
    | TCP  | 6443      | Agents    | Servers   | K3s supervisor 和 Kubernetes API Server |
    | UDP  | 8472      | All nodes | All nodes | 仅适用于Flannel VXLAN                   |
    | TCP  | 10250     | All nodes | All nodes | Kubelet metrics                         |
    | UDP  | 51820     | All nodes | All nodes | 仅适用于带有 IPv4的Flannel Wireguard    |
    | UDP  | 51821     | All nodes | All nodes | 仅适用于带有 IPv6的Flannel Wireguard    |
    | TCP  | 5001      | All nodes | All nodes | 仅适用于嵌入分布式注册表（Spegel）      |
    | TCP  | 6443      | All nodes | All nodes | 仅适用于嵌入分布式注册表（Spegel）      |

- 节点角色

    登录用户需具备 root 权限

    | server node | agent node | 描述                              |
    | :---------- | :--------- | :-------------------------------- |
    | 1           | 0          | 一台 server 节点                  |
    | 1           | 2          | 一台 server 节点、两台 agent 节点 |
    | 3           | 0          | 三台 server 节点                  |

## 前置准备

1. 保存安装脚本到安装节点（任意可以访问到集群节点的节点）

    ```shell
    $ cat > k3slcm <<'EOF'
    #!/bin/bash
    set -e
    
    airgap_image=${K3S_AIRGAP_IMAGE:-}
    k3s_bin=${K3S_BINARY:-}
    install_script=${K3S_INSTALL_SCRIPT:-}
    
    servers=${K3S_SERVERS:-}
    agents=${K3S_AGENTS:-}
    ssh_user=${SSH_USER:-root}
    ssh_password=${SSH_PASSWORD:-}
    ssh_privatekey_path=${SSH_PRIVATEKEY_PATH:-}
    extra_server_args=${EXTRA_SERVER_ARGS:-}
    extra_agent_args=${EXTRA_AGENT_ARGS:-}
    first_server=$(cut -d, -f1 <<<"$servers,")
    other_servers=$(cut -d, -f2- <<<"$servers,")
    
    install_script_env="INSTALL_K3S_SKIP_SELINUX_RPM=true INSTALL_K3S_SELINUX_WARN=true "
    [ -n "$K3S_VERSION" ] && install_script_env+="INSTALL_K3S_VERSION=$K3S_VERSION "
    
    ssh_opts="-q -o StrictHostkeyChecking=no -o UserKnownHostsFile=/dev/null -o ControlPath=/tmp/ssh_mux_%h_%p_%r -o ControlMaster=auto -o ControlPersist=10m"
    
    if [ -n "$ssh_privatekey_path" ]; then
      ssh_opts+=" -i $ssh_privatekey_path"
    elif [ -n "$ssh_password" ]; then
      askpass=$(mktemp)
      echo "echo -n $ssh_password" > $askpass
      chmod 0755 $askpass
      export SSH_ASKPASS=$askpass SSH_ASKPASS_REQUIRE=force
    else
      echo "SSH_PASSWORD or SSH_PRIVATEKEY_PATH must be provided" && exit 1
    fi
    
    log_info() { echo -e "\033[36m* $*\033[0m"; }
    clean() { rm -f $askpass; }
    trap clean EXIT
    
    IFS=',' read -ra all_nodes <<< "$servers,$agents"
    if [ -n "$k3s_bin" ]; then
      for node in ${all_nodes[@]}; do
        chmod +x "$k3s_bin" "$install_script"
        ssh $ssh_opts "$ssh_user@$node" "mkdir -p /usr/local/bin /var/lib/rancher/k3s/agent/images"
        log_info "Copying $airgap_image to $node"
        scp -O $ssh_opts "$airgap_image" "$ssh_user@$node:/var/lib/rancher/k3s/agent/images"
        log_info "Copying $k3s_bin to $node"
        scp -O $ssh_opts "$k3s_bin" "$ssh_user@$node:/usr/local/bin/k3s"
        log_info "Copying $install_script to $node"
        scp -O $ssh_opts "$install_script" "$ssh_user@$node:/usr/local/bin/k3s-install.sh"
      done
      install_script_env+="INSTALL_K3S_SKIP_DOWNLOAD=true "
    else
      for node in ${all_nodes[@]}; do
        log_info "Downloading install script for $node"
        ssh $ssh_opts "$ssh_user@$node" "curl -sSLo /usr/local/bin/k3s-install.sh https://get.k3s.io/ && chmod +x /usr/local/bin/k3s-install.sh"
      done
    fi
    
    restart_k3s() {
      local node=$1
      previous_k3s_version=$(ssh $ssh_opts "$ssh_user@$first_server" "kubectl get no -o wide | awk '\$6==\"$node\" {print \$5}'")
      [ -n "$previous_k3s_version" -a "$previous_k3s_version" != "$K3S_VERSION" -a -n "$k3s_bin" ] && return 0 || return 1
    }
    
    token=mynodetoken
    install_script_env+=${K3S_INSTALL_SCRIPT_ENV:-}
    if [ -z "$other_servers" ]; then
      log_info "Installing on server node [$first_server]"
      ssh $ssh_opts "$ssh_user@$first_server" "env $install_script_env /usr/local/bin/k3s-install.sh server --token $token $extra_server_args"
      ! restart_k3s "$first_server" || ssh $ssh_opts "$ssh_user@$first_server" "systemctl restart k3s.service"
    else
      log_info "Installing on first server node [$first_server]"
      ssh $ssh_opts "$ssh_user@$first_server" "env $install_script_env /usr/local/bin/k3s-install.sh server --cluster-init --token $token $extra_server_args"
      ! restart_k3s "$first_server" || ssh $ssh_opts "$ssh_user@$first_server" "systemctl restart k3s.service"
      IFS=',' read -ra other_server_nodes <<< "$other_servers"
      for node in ${other_server_nodes[@]}; do
        log_info "Installing on other server node [$node]"
        ssh $ssh_opts "$ssh_user@$node" "env $install_script_env /usr/local/bin/k3s-install.sh server --server https://$first_server:6443 --token $token $extra_server_args"
        ! restart_k3s "$node" || ssh $ssh_opts "$ssh_user@$node" "systemctl restart k3s.service"
      done
    fi
    
    if [ -n "$agents" ]; then
      IFS=',' read -ra agent_nodes <<< "$agents"
      for node in ${agent_nodes[@]}; do
        log_info "Installing on agent node [$node]"
        ssh $ssh_opts "$ssh_user@$node" "env $install_script_env K3S_TOKEN=$token K3S_URL=https://$first_server:6443 /usr/local/bin/k3s-install.sh agent --token $token $extra_agent_args"
        ! restart_k3s "$node" || ssh $ssh_opts "$ssh_user@$node" "systemctl restart k3s-agent.service"
      done
    fi
    EOF
    ```

1. （可选）离线环境下，在一台可联网节点下载 K3s 相关离线资源，并拷贝到安装节点

    ```shell
    ## [联网节点执行]

    # 设置 K3s 版本为 v1.30.2+k3s1
    $ export k3s_version=v1.30.2+k3s1
    
    # 离线镜像包
    # arm64链接为 https://github.com/k3s-io/k3s/releases/download/$k3s_version/k3s-airgap-images-arm64.tar.zst
    $ curl -LO https://github.com/k3s-io/k3s/releases/download/$k3s_version/k3s-airgap-images-amd64.tar.zst
    
    # k3s 二进制文件
    # arm64链接为 https://github.com/k3s-io/k3s/releases/download/$k3s_version/k3s-arm64
    $ curl -LO https://github.com/k3s-io/k3s/releases/download/$k3s_version/k3s
    
    # 安装部署脚本
    $ curl -Lo k3s-install.sh https://get.k3s.io/
    
    ## 上述资源拷贝到安装节点文件系统上
    
    ## [安装节点执行]
    $ export K3S_AIRGAP_IMAGE=<资源存放目录>/k3s-airgap-images-amd64.tar.zst 
    $ export K3S_BINARY=<资源存放目录>/k3s 
    $ export K3S_INSTALL_SCRIPT=<资源存放目录>/k3s-install.sh
    ```

1. 关闭防火墙和 swap（若防火墙无法关闭，可放行上述入站端口）

    ```shell
    # Ubuntu 关闭防火墙方法
    $ sudo ufw disable
    # RHEL / CentOS / Fedora / SUSE 关闭防火墙方法
    $ systemctl disable firewalld --now
    $ sudo swapoff -a
    $ sudo sed -i '/swap/s/^/#/' /etc/fstab
    ```

## 部署集群

下文测试环境信息为 Ubuntu 22.04 LTS, amd64，离线安装

1. 在安装节点根据部署规划设置节点信息，并导出环境变量，多个节点以半角逗号 `,` 分隔 

    === "1 server / 0 agent"

        ```shell
        export K3S_SERVERS=172.30.41.5 $ export SSH_USER=root
        # 若使用 public key 方式登录，确保已将公钥添加到各节点的 ~/.ssh/authorized_keys

        export SSH_PRIVATEKEY_PATH=<私钥路径>
        export SSH_PASSWORD=<SSH密码>
        ```

    === "1 server / 2 agent"

        ```shell
        export K3S_SERVERS=172.30.41.5
        export K3S_AGENTS=172.30.41.6,172.30.41.7
        export SSH_USER=root

        # 若使用 public key 方式登录，确保已将公钥添加到各节点的 ~/.ssh/authorized_keys
        export SSH_PRIVATEKEY_PATH=<私钥路径>
        export SSH_PASSWORD=<SSH密码>
        ```

    === "3 server / 0 agent"

        ```shell
        export K3S_SERVERS=172.30.41.5,172.30.41.6,172.30.41.7
        export SSH_USER=root
   
        # 若使用 public key 方式登录，确保已将公钥添加到各节点的 ~/.ssh/authorized_keys
        export SSH_PRIVATEKEY_PATH=<私钥路径>
        export SSH_PASSWORD=<SSH密码>
        ```

1. 执行部署操作

    以 3 server / 0 agent 模式为例，每台机器必须有一个唯一的主机名

    ```shell
    # 若有更多 K3s 安装脚本环境变量设置需求，请设置 K3S_INSTALL_SCRIPT_ENV，其值参考 https://docs.k3s.io/reference/env-variables
    # 若需对 server 或 agent 节点作出额外配置，请设置 EXTRA_SERVER_ARGS 或 EXTRA_AGENT_ARGS，其值参考 https://docs.k3s.io/cli/server https://docs.k3s.io/cli/agent
    $ bash k3slcm
    * Copying ./v1.30.2/k3s-airgap-images-amd64.tar.zst to 172.30.41.5
    * Copying ./v1.30.2/k3s to 172.30.41.5
    * Copying ./v1.30.2/k3s-install.sh to 172.30.41.5
    * Copying ./v1.30.2/k3s-airgap-images-amd64.tar.zst to 172.30.41.6
    * Copying ./v1.30.2/k3s to 172.30.41.6
    * Copying ./v1.30.2/k3s-install.sh to 172.30.41.6
    * Copying ./v1.30.2/k3s-airgap-images-amd64.tar.zst to 172.30.41.7
    * Copying ./v1.30.2/k3s to 172.30.41.7
    * Copying ./v1.30.2/k3s-install.sh to 172.30.41.7
    * Installing on first server node [172.30.41.5]
    [INFO]  Skipping k3s download and verify
    [INFO]  Skipping installation of SELinux RPM
    [INFO]  Creating /usr/local/bin/kubectl symlink to k3s
    [INFO]  Creating /usr/local/bin/crictl symlink to k3s
    [INFO]  Creating /usr/local/bin/ctr symlink to k3s
    [INFO]  Creating killall script /usr/local/bin/k3s-killall.sh
    [INFO]  Creating uninstall script /usr/local/bin/k3s-uninstall.sh
    [INFO]  env: Creating environment file /etc/systemd/system/k3s.service.env
    [INFO]  systemd: Creating service file /etc/systemd/system/k3s.service
    [INFO]  systemd: Enabling k3s unit
    Created symlink /etc/systemd/system/multi-user.target.wants/k3s.service → /etc/systemd/system/k3s.service.
    [INFO]  systemd: Starting k3s
    * Installing on other server node [172.30.41.6]
    ......
    ```

1. 检查集群状态

    ```shell
    $ kubectl get no -owide
    NAME      STATUS   ROLES                       AGE     VERSION        INTERNAL-IP   EXTERNAL-IP   OS-IMAGE             KERNEL-VERSION      CONTAINER-RUNTIME
    server1   Ready    control-plane,etcd,master   3m51s   v1.30.2+k3s1   172.30.41.5   <none>        Ubuntu 22.04.3 LTS   5.15.0-78-generic   containerd://1.7.17-k3s1
    server2   Ready    control-plane,etcd,master   3m18s   v1.30.2+k3s1   172.30.41.6   <none>        Ubuntu 22.04.3 LTS   5.15.0-78-generic   containerd://1.7.17-k3s1
    server3   Ready    control-plane,etcd,master   3m7s    v1.30.2+k3s1   172.30.41.7   <none>        Ubuntu 22.04.3 LTS   5.15.0-78-generic   containerd://1.7.17-k3s1
    
    $ kubectl get pod --all-namespaces -owide
    NAMESPACE     NAME                                      READY   STATUS      RESTARTS   AGE     IP          NODE      NOMINATED NODE   READINESS GATES
    kube-system   coredns-576bfc4dc7-z4x2s                  1/1     Running     0          8m31s   10.42.0.3   server1   <none>           <none>
    kube-system   helm-install-traefik-98kh5                0/1     Completed   1          8m31s   10.42.0.4   server1   <none>           <none>
    kube-system   helm-install-traefik-crd-9xtfd            0/1     Completed   0          8m31s   10.42.0.5   server1   <none>           <none>
    kube-system   local-path-provisioner-86f46b7bf7-qt995   1/1     Running     0          8m31s   10.42.0.6   server1   <none>           <none>
    kube-system   metrics-server-557ff575fb-kptsh           1/1     Running     0          8m31s   10.42.0.2   server1   <none>           <none>
    kube-system   svclb-traefik-f95cc81c-mgcjh              2/2     Running     0          6m28s   10.42.1.3   server2   <none>           <none>
    kube-system   svclb-traefik-f95cc81c-xtb8f              2/2     Running     0          6m28s   10.42.2.2   server3   <none>           <none>
    kube-system   svclb-traefik-f95cc81c-zcsxl              2/2     Running     0          6m28s   10.42.0.7   server1   <none>           <none>
    kube-system   traefik-5fb479b77-6pbh5                   1/1     Running     0          6m28s   10.42.1.2   server2   <none>           <none>
    ```

## 升级集群

1. 如升级到 `v1.30.3+k3s1` 版本，按照 `前置准备` 步骤 2 重新下载离线资源并拷贝到安装节点，同时在安装节点导出离线资源路径环境变量。（若为联网升级，则跳过此操作）
1. 执行升级操作

    ```shell
    $ export K3S_VERSION=v1.30.3+k3s1
    $ bash k3slcm
    * Copying ./v1.30.3/k3s-airgap-images-amd64.tar.zst to 172.30.41.5
    * Copying ./v1.30.3/k3s to 172.30.41.5
    * Copying ./v1.30.3/k3s-install.sh to 172.30.41.5
    * Copying ./v1.30.3/k3s-airgap-images-amd64.tar.zst to 172.30.41.6
    * Copying ./v1.30.3/k3s to 172.30.41.6
    * Copying ./v1.30.3/k3s-install.sh to 172.30.41.6
    * Copying ./v1.30.3/k3s-airgap-images-amd64.tar.zst to 172.30.41.7
    * Copying ./v1.30.3/k3s to 172.30.41.7
    * Copying ./v1.30.3/k3s-install.sh to 172.30.41.7
    * Installing on first server node [172.30.41.5]
    [INFO]  Skipping k3s download and verify
    [INFO]  Skipping installation of SELinux RPM
    [INFO]  Skipping /usr/local/bin/kubectl symlink to k3s, already exists
    [INFO]  Skipping /usr/local/bin/crictl symlink to k3s, already exists
    [INFO]  Skipping /usr/local/bin/ctr symlink to k3s, already exists
    [INFO]  Creating killall script /usr/local/bin/k3s-killall.sh
    [INFO]  Creating uninstall script /usr/local/bin/k3s-uninstall.sh
    [INFO]  env: Creating environment file /etc/systemd/system/k3s.service.env
    [INFO]  systemd: Creating service file /etc/systemd/system/k3s.service
    [INFO]  systemd: Enabling k3s unit
    Created symlink /etc/systemd/system/multi-user.target.wants/k3s.service → /etc/systemd/system/k3s.service.
    [INFO]  No change detected so skipping service start
    * Installing on other server node [172.30.41.6]
    ......
    ```

1. 检查集群状态

    ```shell
    $ kubectl get node -owide
    NAME      STATUS   ROLES                       AGE   VERSION        INTERNAL-IP   EXTERNAL-IP   OS-IMAGE             KERNEL-VERSION      CONTAINER-RUNTIME
    server1   Ready    control-plane,etcd,master   18m   v1.30.3+k3s1   172.30.41.5   <none>        Ubuntu 22.04.3 LTS   5.15.0-78-generic   containerd://1.7.17-k3s1
    server2   Ready    control-plane,etcd,master   17m   v1.30.3+k3s1   172.30.41.6   <none>        Ubuntu 22.04.3 LTS   5.15.0-78-generic   containerd://1.7.17-k3s1
    server3   Ready    control-plane,etcd,master   17m   v1.30.3+k3s1   172.30.41.7   <none>        Ubuntu 22.04.3 LTS   5.15.0-78-generic   containerd://1.7.17-k3s1
    
    $ kubectl get po --all-namespaces -owide
    NAMESPACE     NAME                                      READY   STATUS      RESTARTS   AGE     IP          NODE      NOMINATED NODE   READINESS GATES
    kube-system   coredns-576bfc4dc7-z4x2s                  1/1     Running     0          18m     10.42.0.3   server1   <none>           <none>
    kube-system   helm-install-traefik-98kh5                0/1     Completed   1          18m     <none>      server1   <none>           <none>
    kube-system   helm-install-traefik-crd-9xtfd            0/1     Completed   0          18m     <none>      server1   <none>           <none>
    kube-system   local-path-provisioner-6795b5f9d8-t4rvm   1/1     Running     0          2m49s   10.42.2.3   server3   <none>           <none>
    kube-system   metrics-server-557ff575fb-kptsh           1/1     Running     0          18m     10.42.0.2   server1   <none>           <none>
    kube-system   svclb-traefik-f95cc81c-mgcjh              2/2     Running     0          16m     10.42.1.3   server2   <none>           <none>
    kube-system   svclb-traefik-f95cc81c-xtb8f              2/2     Running     0          16m     10.42.2.2   server3   <none>           <none>
    kube-system   svclb-traefik-f95cc81c-zcsxl              2/2     Running     0          16m     10.42.0.7   server1   <none>           <none>
    kube-system   traefik-5fb479b77-6pbh5                   1/1     Running     0          16m     10.42.1.2   server2   <none>           <none>
    ```

## 扩容集群

1. 如添加新的 agent 节点：

    ```shell
    export K3S_AGENTS=172.30.41.8
    ```

    添加新的 server 节点如下：

    ```diff
    < export K3S_SERVERS=172.30.41.5,172.30.41.6,172.30.41.7
    ---
    > export K3S_SERVERS=172.30.41.5,172.30.41.6,172.30.41.7,172.30.41.8,172.30.41.9
    ```

1. 执行扩容操作（以添加 agent 节点为例）

    ```shell
    $ bash k3slcm
    * Copying ./v1.30.3/k3s-airgap-images-amd64.tar.zst to 172.30.41.5
    * Copying ./v1.30.3/k3s to 172.30.41.5
    * Copying ./v1.30.3/k3s-install.sh to 172.30.41.5
    * Copying ./v1.30.3/k3s-airgap-images-amd64.tar.zst to 172.30.41.6
    * Copying ./v1.30.3/k3s to 172.30.41.6
    * Copying ./v1.30.3/k3s-install.sh to 172.30.41.6
    * Copying ./v1.30.3/k3s-airgap-images-amd64.tar.zst to 172.30.41.7
    * Copying ./v1.30.3/k3s to 172.30.41.7
    * Copying ./v1.30.3/k3s-install.sh to 172.30.41.7
    * Copying ./v1.30.3/k3s-airgap-images-amd64.tar.zst to 172.30.41.8
    * Copying ./v1.30.3/k3s to 172.30.41.8
    * Copying ./v1.30.3/k3s-install.sh to 172.30.41.8
    * Installing on first server node [172.30.41.5]
    [INFO]  Skipping k3s download and verify
    [INFO]  Skipping installation of SELinux RPM
    [INFO]  Skipping /usr/local/bin/kubectl symlink to k3s, already exists
    [INFO]  Skipping /usr/local/bin/crictl symlink to k3s, already exists
    [INFO]  Skipping /usr/local/bin/ctr symlink to k3s, already exists
    [INFO]  Creating killall script /usr/local/bin/k3s-killall.sh
    [INFO]  Creating uninstall script /usr/local/bin/k3s-uninstall.sh
    [INFO]  env: Creating environment file /etc/systemd/system/k3s.service.env
    [INFO]  systemd: Creating service file /etc/systemd/system/k3s.service
    [INFO]  systemd: Enabling k3s unit
    Created symlink /etc/systemd/system/multi-user.target.wants/k3s.service → /etc/systemd/system/k3s.service.
    [INFO]  No change detected so skipping service start
    ......
    * Installing on agent node [172.30.41.8]
    [INFO]  Skipping k3s download and verify
    [INFO]  Skipping installation of SELinux RPM
    [INFO]  Creating /usr/local/bin/kubectl symlink to k3s
    [INFO]  Creating /usr/local/bin/crictl symlink to k3s
    [INFO]  Creating /usr/local/bin/ctr symlink to k3s
    [INFO]  Creating killall script /usr/local/bin/k3s-killall.sh
    [INFO]  Creating uninstall script /usr/local/bin/k3s-agent-uninstall.sh
    [INFO]  env: Creating environment file /etc/systemd/system/k3s-agent.service.env
    [INFO]  systemd: Creating service file /etc/systemd/system/k3s-agent.service
    [INFO]  systemd: Enabling k3s-agent unit
    Created symlink /etc/systemd/system/multi-user.target.wants/k3s-agent.service → /etc/systemd/system/k3s-agent.service.
    [INFO]  systemd: Starting k3s-agent
    ```
    
1. 检查集群状态

    ```shell
    $ kubectl get node -owide
    NAME      STATUS   ROLES                       AGE   VERSION        INTERNAL-IP   EXTERNAL-IP   OS-IMAGE             KERNEL-VERSION      CONTAINER-RUNTIME
    agent1    Ready    <none>                      57s   v1.30.3+k3s1   172.30.41.8   <none>        Ubuntu 22.04.3 LTS   5.15.0-78-generic   containerd://1.7.17-k3s1
    server1   Ready    control-plane,etcd,master   12m   v1.30.3+k3s1   172.30.41.5   <none>        Ubuntu 22.04.3 LTS   5.15.0-78-generic   containerd://1.7.17-k3s1
    server2   Ready    control-plane,etcd,master   11m   v1.30.3+k3s1   172.30.41.6   <none>        Ubuntu 22.04.3 LTS   5.15.0-78-generic   containerd://1.7.17-k3s1
    server3   Ready    control-plane,etcd,master   11m   v1.30.3+k3s1   172.30.41.7   <none>        Ubuntu 22.04.3 LTS   5.15.0-78-generic   containerd://1.7.17-k3s1
    ```

## 缩容集群

1. 仅在待删除节点执行 `k3s-uninstall.sh` 或 `k3s-agent-uninstall.sh`
1. 在任意 server 节点上执行：

    ```shell
    kubectl delete node <节点名称>
    ```

## 卸载集群

1. 在所有 server 节点手动执行 `k3s-uninstall.sh`
1. 在所有 agent 节点手动执行 `k3s-agent-uninstall.sh`
