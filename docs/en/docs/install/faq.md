# Installation Troubleshooting

This page summarizes some troubles that you may encounter when installing DCE 5.0 and provides corresponding solutions, to help you quickly solve problems.

## Podman cannot auto-recover after bootstrapping node restart

After the bootstrapping node restarts, wait for kind to start successfully:

1. Execute `podman exec` to enter the container.
2. `sed -i 's/server: .*:6443/server: https://127.0.0.1:6443/g' /etc/kubernetes/controller-manager.conf`
3. `sed -i 's/server: .*:6443/server: https://127.0.0.1:6443/g ' /etc/kubernetes/scheduler.conf`

## Podman fails to create containers after disabling `IPv6`

**Error message**:

```bash
ERROR: failed to create cluster: command "podman run --name kind-control-plane...  
```

**Solutions**

Re-enable IPv6 or change bootstrapping node base to Docker.

Podman-related issues: <https://github.com/containers/podman/issues/13388>

## Redis get stuck when reinstalling DCE 5.0 in kind cluster

**Error**:

Redis Pod has `0/4 running` status for a long time, prompting: `primary ClusterIP can not unset`

**Solutions**:

Delete `rfs-mcamel-common-redis` under the `mcamel-system` namespace, and then try again.

    ```shell
    kubectl delete svc rfs-mcamel-common-redis -n mcamel-system
    ```

## When using Metallb, the VIP access is blocked and cannot log into DCE

1. Check whether the VIP is in the same network segment as the host. In Metallb L2 mode, they should be in the same network segment.

2. If this error occurs after you added a new NIC to the control node in the global cluster, you need to manually declare and configure `L2Advertisement`.

    Refer to related [Metallb issues](https://metallb.universe.tf/configuration/_advanced_l2_configuration/#specify-network-interfaces-that-lb-ip-can-be-announced-from)

## Community package: `fluent-bit` installation failed

**Error**:

`DaemonSet is not ready: insight-system/insight-agent-fluent-bit. 0 out of 2 expected pods are ready`

**Solutions**:

Check if the following key information appears in the Pod log:

```bash
  [ warn] [net] getaddrinfo(host='mcamel-common-es-cluster-masters-es-http.mcamel-system.svc.cluster.local',errt11):Could not contact DNS servers
```

If yes, it is a known bug of `fluent-bit` bug`, Refer to: <https://github.com/aws/aws-for-fluent-bit/issues/233>

## Error reported during CentOS 7.6 installation

**Error**:

![FAQ1](https://docs.daocloud.io/daocloud-docs-images/docs/install/images/FAQ1.png)

**Solutions**:

Execute `modprobe br_netfilter` on each node where the global service cluster is installed, and wait until `br_netfilter` is loaded.

## CentOS environment preparation issues

**Error**:

Running `yum install docker` reports an error:

```text
Failed to set locale, defaulting to C.UTF-8
CentOS Linux 8 - AppStream 93 B/s | 38 B 00:00
Error: Failed to download metadata for repo 'appstream': Cannot prepare internal mirrorlist: No URLs in mirrorlist
```

**Solutions**:

- Install `glibc-langpack-en`

     ```bash
     sudo yum install -y glibc-langpack-en
     ```

- If the error persists, try:

     ```bash
     sed -i 's/mirrorlist/#mirrorlist/g' /etc/yum.repos.d/CentOS-*
     sed -i 's|#baseurl=http://mirror.centos.org|baseurl=http://vault.centos.org|g' /etc/yum.repos.d/CentOS-*
     sudo yum update -y
     ```
