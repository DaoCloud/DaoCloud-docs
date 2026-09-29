# Requirements to Join Edge Node

The edge nodes need to meet the specifications in the table below.

## Operating System (OS)

- x86_64 architecture

    Ubuntu LTS (Xenial Xerus,  Bionic Beaver, Jammy Jellyfish, or Focal Fossa), CentOS, EulerOS, RHEL, Kylin, NewStart, NeoKylin, openEuler, and Rocky Linux

<!-- - armv7i (arm32) architecture

    Raspbian GNU/Linux (stretch) -->

- aarch64 (arm64) architecture

    Ubuntu LTS (Bionic Beaver), CentOS, and EulerOS

## Memory

The general overhead of edge software is about 150MB, and it may increase appropriately depending on the pressure of edge management.

To ensure the normal operation of business, it is recommended that the memory of edge nodes should be more than 256MB.

## CPU

Not less than 1 core.

## Hard Disk

Not less than 1GB.

## Container Runtime

The container runtime supports either Docker or containerd.

- The Docker version must be higher than v19.0, and v19.03.6 is recommended.

    Note: If the installed version of KubeEdge is higher than or equal to v1.14 and the cloud Kubernetes version is higher than v1.24, CRI-Dockerd will need to be installed in addition to Docker.

- If the installed version of KubeEdge is higher than v1.12.0, it is recommended to install containerd. For the installation process, refer to [Install Container Runtime on Edge Nodes](./container-engine-install.md).

## glibc

Version must be higher than 2.17.

To check the version:

```sh
ubuntu: ldd --version
```

## Ports

The edge nodes need to use the following ports, please make sure these ports can be used normally.

- 1883: The built-in MQTT broker listening port of the edge node, and this port needs to be opened.

## Time Synchronization

The time of the edge node needs to be consistent with the time of the cloud server, and UTC standard time is recommended.

## Component Scheduling

The edge nodes do not support some running components such as Calico, KubeProxy, and Insight.
To prevent DaemonSet applications from being scheduled to the edge, which could lead to abnormal
node status, the following annotation should be added for exclusion.

```yaml
nodeAffinity:
  requiredDuringSchedulingIgnoredDuringExecution:
    nodeSelectorTerms:
      - matchExpressions:
        - key: node-role.kubernetes.io/edge
          operator: DoesNotExist
```
