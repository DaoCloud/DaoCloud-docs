# 升级注意事项

本页说明将安装器升级到新版本或者升级 Kubernetes 版本时需要注意的相关事项。

## Kubernetes 升级到 v1.35 及更高版本

**核心建议：安装和升级到 Kubernetes v1.35 版本及以上的操作系统采用 cgroup v2。**

自 v1.35 起，Kubelet 的 `FailCgroupV1` 默认值已改为 `true`。这意味着：

- 未显式关闭该开关的节点，若操作系统使用 cgroup v1，**Kubelet 将直接报错退出**。
- `kubeadm init/join/upgrade` 的预检也会将 cgroup v1 判定为**错误（Error）**而非警告。
- cgroup v1 已正式进入 **Deprecated（弃用）** 状态，社区承诺不早于 v1.38 完全移除相关代码。

!!! warning

    - 继续使用 cgroup v1 将导致功能缺失（MemoryQoS、Swap、MemoryReservationPolicy 等）、稳定性风险、可观测性受限，并最终面临**完全不可升级**的死胡同。
    - Linux 生态（systemd、RHEL、Fedora、Debian 等）也在同步废弃 cgroup v1，停留 v1 意味着需要锁定旧版本内核与发行版。

若因特殊原因暂时无法迁移到 cgroup v2，可通过以下方式**非安全地**跳过检测：

!!! note

    跳过开关仅为过渡期的应急手段，不应作为长期策略。请在 v1.35–v1.37 的迁移窗口内，将节点操作系统升级到 cgroup v2，并验证工作负载兼容性。

1. 跳过 Kubelet 检测

    **手动配置：**

    在 Kubelet 配置中显式关闭：

    ```yaml
    # /var/lib/kubelet/config.yaml
    failCgroupV1: false
    ```

    或通过命令行：

    ```bash
    kubelet --fail-cgroupv1=false ...
    ```

    **Kubean 部署：**

    Kubean 通过 `Cluster` CR 的 `spec.varsConfRef` 引用 ConfigMap 传递 Kubespray 变量。在对应的 ConfigMap 的 `group_vars.yml` 中添加：

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

2. 跳过 kubeadm 预检

    **手动执行：**

    ```bash
    kubeadm init --ignore-preflight-errors=SystemVerification
    ```

    **Kubean 部署：**

    在 `Cluster` CR 引用的 vars ConfigMap 的 `group_vars.yml` 中添加：

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

    > ⚠️ **注意**：此操作会跳过完整的系统级验证，降低集群健康基线。

**使用上述跳过开关可能存在未知风险：**

- 社区已停止在 cgroup v1 上验证新功能，仅保留一个 sanity check lane，生产环境可靠性需自行承担。
- 即使跳过启动检测，cgroup v1 上仍存在功能缺失（无 MemoryQoS、LimitedSwap、CPU 硬封顶等）。
- OOM 行为、资源指标统计等与 v2 存在差异，混合环境可能导致监控偏差。
- 不早于 v1.38 将彻底删除 cgroup v1 代码，届时即使关闭 `FailCgroupV1` 也无法启动，集群将被锁定在最后一个支持版本。
- 部分工作负载（如旧版 JVM、Node.js、监控/安全 Agent）在 v2 上的兼容性需单独评估；但反过来，这些组件的新版本已默认面向 v2 优化。



