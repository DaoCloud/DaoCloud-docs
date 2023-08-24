# Install DCE Community on macOS computers via Docker and kind

This page explains how to create a single-node kind cluster using a macOS laptop, and then install DCE Community online.

!!! tip

     This is a simplified installation experience step for beginners, macOS is rarely used in actual production,
     The original author is [panpan0000](https://github.com/panpan0000).

## Hardware environment

Confirm that the performance and resources of the MacBook meet the requirements. The minimum configuration is:

- CPU: **8 cores**
- Memory: **16G**
- Free disk space: more than 20G

## Install and tune Docker

Depending on your MacBook's chip (Intel or M1), install [Docker Desktop](https://docs.docker.com/desktop/install/mac-install/).

Adjust the upper limit of container resources:

1. Start Docker.
1. Click ⚙️ in the upper right corner to open the `Settings` page.
1. Click `Resources` on the left, adjust the resource limit of the startup container to 8C14G, and click the `Apply & Restart` button.

![Adjust resources](https://docs.daocloud.io/daocloud-docs-images/docs/blogs/images/docker.png)

## install kind

According to the actual computer situation, choose one of the following to install kind.
If you encounter other problems, please refer to [kind official installation instructions](https://kind.sigs.k8s.io/docs/user/quick-start/#installation).

=== "Mac is an Intel chip"

     ```shell
     [ $(uname -m) = x86_64 ]&& curl -Lo ./kind https://kind.sigs.k8s.io/dl/v0.17.0/kind-darwin-amd64
     ```

=== "Mac is an M1/ARM chip"

     ```shell
     [ $(uname -m) = arm64 ] && curl -Lo ./kind https://kind.sigs.k8s.io/dl/v0.17.0/kind-darwin-arm64
     chmod +x ./kind
     sudo mv kind /usr/local/bin/kind
     ```

=== "Install kind via Homebrew"

     Install Homebrew:

     ```
     /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
     ```

     install kind

     ```shell
     brew install kind
     ```

Finally, run the following command to confirm that kind is successfully installed:

```shell
kind version
```

## Create kind configuration file

Expose port 32088 in the cluster to port 8888 external to kind (can be modified by yourself):

```shell
cat > kind_cluster.yaml << EOF
apiVersion: kind.x-k8s.io/v1alpha4
kind: Cluster
nodes:
-role: control-plane
   extraPortMappings:
   - containerPort: 32088
     hostPort: 8888
EOF
```

## kind Create a K8s cluster

Taking K8s version 1.25.3 as an example, run the following command to create a K8s cluster:

```shell
kind create cluster --image docker.m.daocloud.io/kindest/node:v1.25.3 --name=fire-kind-cluster --config=kind_cluster.yaml
```

Confirm that the kind cluster is successfully created:

```shell
docker exec -it fire-kind-cluster-control-plane kubectl get no
```

Expected output:

```console
NAME STATUS ROLES AGE VERSION
fire-kind-cluster-control-plane Ready control-plane 18h v1.25.3
```

## Install DCE Community

1. Install dependencies

     ```shell
     cat <<EOF | docker exec -i fire-kind-cluster-control-plane bash
     curl -LO https://proxy-qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/install_prerequisite.sh
     bash install_prerequisite.sh online community
     apt-get update && apt-get install -y wget
     EOF
     ```

1. Download the dce5-installer binary

     ```shell
     docker exec -it fire-kind-cluster-control-plane /bin/bash
     ```

     Assume `VERSION=v0.5.0`

     ```shell
     export VERSION=v0.5.0;
     curl -Lo ./dce5-installer https://proxy-qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/dce5-installer-$VERSION
     chmod +x ./dce5-installer
     exit
     ```

1. Install DCE Community

     1. Get the local IP first

         ```shell
         myIP=$(ip r get 1.1.1.1| awk '{print $NF}')
         ```

         If the error `zsh: command not found: ip` is reported, there are 2 solutions:

         - Run `myIP=$(ifconfig en0| grep "inet[ ]" | awk '{print $2}')`
         - Or install iproute2mac with a command like `brew install iproute2mac` and try again.

     1. Start the installation, it will take about 30 minutes, depending on the network speed of the image pull

         ```shell
         docker exec -it fire-kind-cluster-control-plane bash -c "./dce5-installer install-app -z -k $myIP:8888"
         ```

1. During the installation process, you can open another terminal window and run the following command to observe the pod startup.

     ```shell
     docker exec -it fire-kind-cluster-control-plane kubectl get po -A -w
     ```

     When you see the following prompt, it means the installation of DCE Community is successful.

     ![success](https://docs.daocloud.io/daocloud-docs-images/docs/blogs/images/success.jpg)

1. After entering the default user and password (admin/changeme) to log in, the system will prompt [Request License Key](../dce/license0.md).

## Experience using

After applying for a license, you will enter the main interface of DCE 5.0, displaying information such as currently installed components, clusters/nodes/resources, and alerts.

You can try:

- create a [user](../ghippo/user-guide/access-control/user.md),
   Join a [group](../ghippo/user-guide/access-control/group.md),
   Grant [role permission](../ghippo/user-guide/access-control/role.md)
- [Customized software interface](../ghippo/user-guide/platform-setting/appearance.md)
- [Integrate a cluster](../kpanda/user-guide/clusters/integrate-cluster.md)
- [Manage your nodes](../kpanda/user-guide/nodes/node-check.md)
- [Create a workload](../kpanda/user-guide/workloads/create-deployment.md)
- For more, please refer to the documentation station page

## uninstall

1. Uninstall [DCE Community](../install/uninstall.md).
1. Delete the kind cluster.

     ```
     kind delete cluster --name=fire-kind-cluster
     ```

1. Uninstall kind itself.

     ```
     rm -f $(which kind)
     ```

1. Uninstall Docker in the application list.

At this point your MacBook is back to its original state 😄
