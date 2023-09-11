# Installation Troubleshooting

This page summarizes common issues with the installer and provides troubleshooting solutions to help users quickly resolve problems encountered during installation and operation.

## Troubleshooting DCE 5.0 Platform Interface Unavailability with diag.sh Script

Since installer version v0.12.0, a new diag.sh script has been added to facilitate troubleshooting when the DCE 5.0 platform interface is unavailable.

Run the command:

```bash
./offline/diag.sh
```

Example of execution result:

![FAQ1](images/faq11.png)

## Failure to Start kubelet Service After Kind Container Restart

After restarting the Kind container, the kubelet service fails to start and reports an error:

```text
failed to initialize top level QOS containers: root container [kubelet kubepods] doesn't exist
```

Solution:

- Solution 1: Restart by executing the command `podman restart [kind] --time 120`, and do not interrupt this task with ctrl+c during the execution process.

- Solution 2: Enter the Kind container using `podman exec` and Run the following command:

    ```bash
    for i in $(systemctl list-unit-files --no-legend --no-pager -l | grep --color=never -o .*.slice | grep kubepod);
    do systemctl stop $i;
    done
    ```

## Podman fails to create containers after disabling `IPv6`

**Error message**:

```text
ERROR: failed to create cluster: command "podman run --name kind-control-plane...  
```

**Solutions**

Re-enable IPv6 or change bootstrapping node base to Docker.

Podman-related issues: <https://github.com/containers/podman/issues/13388>

## Redis get stuck when reinstalling DCE 5.0 in kind cluster

Issue: The Redis Pod remains in a 0/4 running state for a long time with the error message `primary ClusterIP can not unset`.

1. Delete the rfs-mcamel-common-redis service in the mcamel-system namespace:

    ```shell
    kubectl delete svc rfs-mcamel-common-redis -n mcamel-system
    ```

2. Then, retry the installation command.

## When using Metallb, the VIP access is blocked and cannot log into DCE

1. Check whether the VIP is in the same network segment as the host. In Metallb L2 mode, they should be in the same network segment.

2. If this error occurs after you added a new NIC to the control node in the global cluster, you need to manually declare and configure `L2Advertisement`.

    Refer to related [Metallb issues](https://metallb.universe.tf/configuration/_advanced_l2_configuration/#specify-network-interfaces-that-lb-ip-can-be-announced-from)

## Community package: `fluent-bit` installation failed

**Error**:

```text
DaemonSet is not ready: insight-system/insight-agent-fluent-bit. 0 out of 2 expected pods are ready
```

**Solutions**:

Check if the following key information appears in the Pod log:

```text
[warn] [net] getaddrinfo(host='mcamel-common-es-cluster-masters-es-http.mcamel-system.svc.cluster.local',errt11):Could not contact DNS servers
```

If yes, it is a known bug of `fluent-bit` bug`, Refer to: <https://github.com/aws/aws-for-fluent-bit/issues/233>

## Error reported during CentOS 7.6 installation

**Error**:

![FAQ1](https://docs.daocloud.io/daocloud-docs-images/docs/install/images/FAQ1.png)

**Solutions**:

Run `modprobe br_netfilter` on each node where the global service cluster is installed, and wait until `br_netfilter` is loaded.

## CentOS environment preparation issues

Running `yum install docker` reports an error:

```text
Failed to set locale, defaulting to C.UTF-8
CentOS Linux 8 - AppStream                                                                    93  B/s |  38  B     00:00    
Error: Failed to download metadata for repo 'appstream': Cannot prepare internal mirrorlist: No URLs in mirrorlist
```

You can try the following methods to resolve the issue:

- Install `glibc-langpack-en` package:

    ```bash
    sudo yum install -y glibc-langpack-en
    ```

- If the issue persists, try the following:

    ```bash
    sed -i 's/mirrorlist/#mirrorlist/g' /etc/yum.repos.d/CentOS-*
    sed -i 's|#baseurl=http://mirror.centos.org|baseurl=http://vault.centos.org|g' /etc/yum.repos.d/CentOS-*
    sudo yum update -y
    ```
