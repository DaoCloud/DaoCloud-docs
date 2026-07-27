---
MTPE: windsonsea
date: 2024-05-11
---

# Upgrade Notes

This page describes the considerations when upgrading the installer to a new version or upgrading the Kubernetes version.

## Use cgroup v2 for the Operating System When Upgrading Kubernetes to v1.35 or Later

**Key Recommendation: Use an operating system with cgroup v2 enabled when installing or upgrading to Kubernetes v1.35 and later.**

Starting from v1.35, the default value of `FailCgroupV1` in Kubelet has been changed to `true`. This means:

- Nodes that do not explicitly disable this setting and use cgroup v1 will cause **Kubelet to exit with an error directly**.
- The preflight checks of `kubeadm init/join/upgrade` will also classify cgroup v1 as an **Error** instead of a warning.
- cgroup v1 has officially entered the **Deprecated** state, and the community promises not to completely remove the related code before v1.38.

!!! warning

    - Continuing to use cgroup v1 will result in missing features (such as MemoryQoS, Swap, and MemoryReservationPolicy), stability risks, limited observability, and eventually a **dead end where upgrades become impossible**.
    - The Linux ecosystem (systemd, RHEL, Fedora, Debian, etc.) is also deprecating cgroup v1. Staying on v1 means locking the system to older kernel versions and distributions.

If you cannot migrate to cgroup v2 temporarily due to special reasons, you can **insecurely** skip the checks using the following methods:

!!! note

    Skipping these checks is only an emergency measure during the transition period and should not be used as a long-term strategy. Please upgrade node operating systems to cgroup v2 and verify workload compatibility within the v1.35–v1.37 migration window.

1. Skip Kubelet Check

    **Manual Configuration:**

    Explicitly disable it in the Kubelet configuration:

    ```yaml
    # /var/lib/kubelet/config.yaml
    failCgroupV1: false
    ```

    Or through the command line:

    ```bash
    kubelet --fail-cgroupv1=false ...
    ```

    **Kubean Deployment:**

    Kubean passes Kubespray variables through the ConfigMap referenced by `spec.varsConfRef` in the `Cluster` CR. Add the following configuration to `group_vars.yml` in the corresponding ConfigMap:

    ```yaml
    apiVersion: v1
    kind: ConfigMap
    metadata:
      name: sample-vars-conf
      namespace: kubean-system
    data:
      group_vars.yml: |
        kubelet_config_extra_args:
          failCgroupV1: false
    ```

2. Skip kubeadm Preflight Check

    **Manual Execution:**

    ```bash
    kubeadm init --ignore-preflight-errors=SystemVerification
    ```

    **Kubean Deployment:**

    Add the following configuration to `group_vars.yml` in the vars ConfigMap referenced by the `Cluster` CR:

    ```yaml
    apiVersion: v1
    kind: ConfigMap
    metadata:
      name: sample-vars-conf
      namespace: kubean-system
    data:
      group_vars.yml: |
        kubeadm_ignore_preflight_errors:
          - SystemVerification
    ```

    > ⚠️ **Note**: This operation skips complete system-level verification and lowers the cluster health baseline.

**Using the above skip options may introduce unknown risks:**

- The community has stopped validating new features on cgroup v1 and only retains one sanity check lane. Production environment reliability must be evaluated and assumed by users themselves.
- Even if startup checks are skipped, cgroup v1 still lacks features such as MemoryQoS, LimitedSwap, and CPU hard limits.
- OOM behavior, resource metric statistics, and other aspects differ from cgroup v2. Mixed environments may result in monitoring discrepancies.
- The cgroup v1 code will be completely removed no earlier than v1.38. At that point, even disabling `FailCgroupV1` will not allow startup, and clusters will be locked to the last supported version.
- The compatibility of some workloads (such as older JVM versions, Node.js versions, monitoring agents, and security agents) with v2 needs to be evaluated separately. However, newer versions of these components have already been optimized for v2 by default.
