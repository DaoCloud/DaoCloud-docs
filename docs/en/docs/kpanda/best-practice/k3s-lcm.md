# Edge Cluster Deployment and Management Practice

For resource-constrained edge or IoT scenarios, Kubernetes cannot well meet resource requirements. Therefore, a lightweight Kubernetes solution is needed that can not only implement container management and orchestration capabilities but also reserve more resource space for business applications. This article introduces the deployment and full lifecycle management practice of edge cluster k3s.

## Node Planning

**Architecture**

- x86_64
- armhf
- arm64/aarch64

**Operating System**

- Can work on most modern Linux systems

**CPU/Memory**

- Single-node K3s cluster

    |             | Min CPU | Recommended CPU | Min Memory | Recommended Memory |
    | :---------- | :------- | -------- | -------- | -------- |
    | K3s cluster | 1 core   | 2 cores  | 1.5 GB   | 2 GB     |

- Multi-node K3s cluster

    |            | Min CPU | Recommended CPU | Min Memory | Recommended Memory |
    | :--------- | :------- | -------- | -------- | -------- |
    | K3s server | 1 core   | 2 cores  | 1 GB     | 1.5 GB   |
    | K3s agent  | 1 core   | 2 cores  | 512 MB   | 1 GB     |

- Node inbound rules

    - Make sure the following ports are not occupied as required
    - If the firewall cannot be turned off due to special requirements, make sure the ports are allowed

    | Protocol | Port      | Source    | Destination | Description                                 |
    | :--- | :-------- | :-------- | :-------- | :-------------------------------------- |
    | TCP  | 2379-2380 | Servers   | Servers   | For HA with embedded etcd                 |
    | TCP  | 6443      | Agents    | Servers   | K3s supervisor and Kubernetes API Server |
    | UDP  | 8472      | All nodes | All nodes | For Flannel VXLAN only                   |
    | TCP  | 10250     | All nodes | All nodes | Kubelet metrics                         |
    | UDP  | 51820     | All nodes | All nodes | For Flannel Wireguard with IPv4 only     |
    | UDP  | 51821     | All nodes | All nodes | For Flannel Wireguard with IPv6 only     |
    | TCP  | 5001      | All nodes | All nodes | For the embedded distributed registry (Spegel) only |
    | TCP  | 6443      | All nodes | All nodes | For the embedded distributed registry (Spegel) only |

- Node roles

    The logged-in user must have root privileges.

    | server node | agent node | Description                       |
    | :---------- | :--------- | :-------------------------------- |
    | 1           | 0          | One server node                   |
    | 1           | 2          | One server node and two agent nodes |
    | 3           | 0          | Three server nodes                |

## Prerequisites

1. Save the installation script to the installation node (any node that can access the cluster nodes).

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

2. (Optional) In an offline environment, download the K3s-related offline resources on a node with internet access and copy them to the installation node.

    ```shell
    ## [Run on the node with internet access]

    # Set the K3s version to v1.30.2+k3s1
    $ export k3s_version=v1.30.2+k3s1
    
    # Offline image package
    # The arm64 link is https://github.com/k3s-io/k3s/releases/download/$k3s_version/k3s-airgap-images-arm64.tar.zst
    $ curl -LO https://github.com/k3s-io/k3s/releases/download/$k3s_version/k3s-airgap-images-amd64.tar.zst
    
    # k3s binary
    # The arm64 link is https://github.com/k3s-io/k3s/releases/download/$k3s_version/k3s-arm64
    $ curl -LO https://github.com/k3s-io/k3s/releases/download/$k3s_version/k3s
    
    # Installation and deployment script
    $ curl -Lo k3s-install.sh https://get.k3s.io/
    
    ## Copy the above resources to the installation node's file system
    
    ## [Run on the installation node]
    $ export K3S_AIRGAP_IMAGE=<resource directory>/k3s-airgap-images-amd64.tar.zst 
    $ export K3S_BINARY=<resource directory>/k3s 
    $ export K3S_INSTALL_SCRIPT=<resource directory>/k3s-install.sh
    ```

3. Disable the firewall and swap (if the firewall cannot be disabled, allow the inbound ports listed above).

    ```shell
    # How to disable the firewall on Ubuntu
    $ sudo ufw disable
    # How to disable the firewall on RHEL / CentOS / Fedora / SUSE
    $ systemctl disable firewalld --now
    $ sudo swapoff -a
    $ sudo sed -i '/swap/s/^/#/' /etc/fstab
    ```

## Deploy the Cluster

The test environment information below is Ubuntu 22.04 LTS, amd64, offline installation.

1. On the installation node, set the node information according to the deployment plan and export the environment variables. Separate multiple nodes with a half-width comma `,`.

    === "1 server / 0 agent"

        ```shell
        export K3S_SERVERS=172.30.41.5 $ export SSH_USER=root
        # If you log in with a public key, make sure the public key has been added to ~/.ssh/authorized_keys on each node

        export SSH_PRIVATEKEY_PATH=<private key path>
        export SSH_PASSWORD=<SSH password>
        ```

    === "1 server / 2 agent"

        ```shell
        export K3S_SERVERS=172.30.41.5
        export K3S_AGENTS=172.30.41.6,172.30.41.7
        export SSH_USER=root

        # If you log in with a public key, make sure the public key has been added to ~/.ssh/authorized_keys on each node
        export SSH_PRIVATEKEY_PATH=<private key path>
        export SSH_PASSWORD=<SSH password>
        ```

    === "3 server / 0 agent"

        ```shell
        export K3S_SERVERS=172.30.41.5,172.30.41.6,172.30.41.7
        export SSH_USER=root
   
        # If you log in with a public key, make sure the public key has been added to ~/.ssh/authorized_keys on each node
        export SSH_PRIVATEKEY_PATH=<private key path>
        export SSH_PASSWORD=<SSH password>
        ```

2. Perform the deployment.

    Taking the 3 server / 0 agent mode as an example, each machine must have a unique hostname.

    ```shell
    # If you need to set more environment variables for the K3s installation script, set K3S_INSTALL_SCRIPT_ENV; for its value, refer to https://docs.k3s.io/reference/env-variables
    # If you need to make additional configurations for server or agent nodes, set EXTRA_SERVER_ARGS or EXTRA_AGENT_ARGS; for their values, refer to https://docs.k3s.io/cli/server and https://docs.k3s.io/cli/agent
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

3. Check the cluster status.

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

## Upgrade the Cluster

1. To upgrade to `v1.30.3+k3s1`, re-download the offline resources and copy them to the installation node according to step 2 of Prerequisites, and export the offline resource path environment variables on the installation node. (Skip this operation for an online upgrade.)
2. Perform the upgrade.

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

3. Check the cluster status.

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
    kube-system   svclb-traefik-f95cc81c-zcsxl              2/2     Running     0         16m     10.42.0.7   server1   <none>           <none>
    kube-system   traefik-5fb479b77-6pbh5                   1/1     Running     0          16m     10.42.1.2   server2   <none>           <none>
    ```

## Scale Out the Cluster

1. To add a new agent node:

    ```shell
    export K3S_AGENTS=172.30.41.8
    ```

    To add a new server node:

    ```diff
    < export K3S_SERVERS=172.30.41.5,172.30.41.6,172.30.41.7
    ---
    > export K3S_SERVERS=172.30.41.5,172.30.41.6,172.30.41.7,172.30.41.8,172.30.41.9
    ```

2. Perform the scale-out operation (taking adding an agent node as an example).

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
    
3. Check the cluster status.

    ```shell
    $ kubectl get node -owide
    NAME      STATUS   ROLES                       AGE   VERSION        INTERNAL-IP   EXTERNAL-IP   OS-IMAGE             KERNEL-VERSION      CONTAINER-RUNTIME
    agent1    Ready    <none>                      57s   v1.30.3+k3s1   172.30.41.8   <none>        Ubuntu 22.04.3 LTS   5.15.0-78-generic   containerd://1.7.17-k3s1
    server1   Ready    control-plane,etcd,master   12m   v1.30.3+k3s1   172.30.41.5   <none>        Ubuntu 22.04.3 LTS   5.15.0-78-generic   containerd://1.7.17-k3s1
    server2   Ready    control-plane,etcd,master   11m   v1.30.3+k3s1   172.30.41.6   <none>        Ubuntu 22.04.3 LTS   5.15.0-78-generic   containerd://1.7.17-k3s1
    server3   Ready    control-plane,etcd,master   11m   v1.30.3+k3s1   172.30.41.7   <none>        Ubuntu 22.04.3 LTS   5.15.0-78-generic   containerd://1.7.17-k3s1
    ```

## Scale In the Cluster

1. Run `k3s-uninstall.sh` or `k3s-agent-uninstall.sh` only on the node to be deleted.
2. Run the following command on any server node:

    ```shell
    kubectl delete node <node name>
    ```

## Uninstall the Cluster

1. Manually run `k3s-uninstall.sh` on all server nodes.
2. Manually run `k3s-agent-uninstall.sh` on all agent nodes.
