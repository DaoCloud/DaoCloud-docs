# Installation Troubleshooting

This page summarizes common installer problems and their troubleshooting solutions, so that users can quickly solve problems encountered during the installation process.

## Podman cannot auto-recover after bootstrapping node restart

After the bootstrapping node restarts, wait for kind to start successfully:

1. Execute `podman exec` to enter the container.
2. `sed -i 's/server: .*:6443/server: https://127.0.0.1:6443/g' /etc/kubernetes/controller-manager.conf`
3. `sed -i 's/server: .*:6443/server: https://127.0.0.1:6443/g ' /etc/kubernetes/scheduler.conf`

## Podman fails to create containers when installing after disabling IPv6

The error message is as follows:

```bash
ERROR: failed to create cluster: command "podman run --name kind-control-plane...  
```

Solution: Re-enable IPv6 or update bootstrapping node base to Docker.

Podman-related issue address: https://github.com/containers/podman/issues/13388

## Redis stuck when reinstalling DCE 5.0 in Kind cluster

Problem: Redis Pod has 0/4 running for a long time, prompting: primary ClusterIP can not unset

1. Delete rfs-mcamel-common-redis under the mcamel-system namespace

     ```shell
     kubectl delete svc rfs-mcamel-common-redis -n mcamel-system
     ```

1. Then re-execute the installation command

## When using Metallb, the VIP access is blocked and the DCE login interface cannot be opened

1. Check whether the address of the VIP is in the same network segment as the host. In Metallb L2 mode, it is necessary to ensure that they are in the same network segment
2. If a new network card is added to the control node in the global cluster and the access fails, you need to manually declare and configure L2Advertisement.
    Please refer to [Metallb documentation for this issue](https://metallb.universe.tf/configuration/_advanced_l2_configuration/#specify-network-interfaces-that-lb-ip-can-be-announced-from)

## community edition fluent-bit installation failed

Error: `DaemonSet is not ready: insight-system/insight-agent-fluent-bit. 0 out of 2 expected pods are ready`

Check to see if the following key information appears in the Pod log:

```bash
  [ warn] [net] getaddrinfo(host='mcamel-common-es-cluster-masters-es-http.mcamel-system.svc.cluster.local',errt11):Could not contact DNS servers
```

The above problem is a fluent-bit bug, you can refer to: https://github.com/aws/aws-for-fluent-bit/issues/233

## Error reported during CentOS 7.6 installation

![FAQ1](https://docs.daocloud.io/daocloud-docs-images/docs/install/images/FAQ1.png)

Execute `modprobe br_netfilter` on each node where the global service cluster is installed, and it will be fine after loading `br_netfilter`.

## CentOS environment preparation issues

Running `yum install docker` reports an error:

```text
Failed to set locale, defaulting to C.UTF-8
CentOS Linux 8 - AppStream 93 B/s | 38 B 00:00
Error: Failed to download metadata for repo 'appstream': Cannot prepare internal mirrorlist: No URLs in mirrorlist
```

You can try to solve it in the following ways:

- Install `glibc-langpack-en`

     ```bash
     sudo yum install -y glibc-langpack-en
     ```

- If the problem persists, try:

     ```bash
     sed -i 's/mirrorlist/#mirrorlist/g' /etc/yum.repos.d/CentOS-*
     sed -i 's|#baseurl=http://mirror.centos.org|baseurl=http://vault.centos.org|g' /etc/yum.repos.d/CentOS-*
     sudo yum update -y
     ```
