# Kubernetes v1.37 Preview: Migration Prep, Security, and Resource Management

Kubernetes v1.37 is shaping up to be a release that balances **migration prep, runtime security, and resource management**:
`kube-proxy`'s ipvs mode enters a deprecation cycle, the exit of CGroup v1 needs early planning,
and the SELinux volume labeling mechanism will also bring behavioral changes that require advance validation.
At the same time, capabilities such as the Metrics API, Rootless kubelet, and volume health monitoring continue to mature,
laying the groundwork for observability and a more secure node runtime.

This article summarizes the v1.37 planned changes that platform teams and cluster operators should prioritize.
The content below reflects the current state of the release cycle and may still change before the actual release date.

> If your cluster still uses ipvs or CGroup v1, you should incorporate the migration into your near-term plans;
> if your workloads enable SELinux and share storage volumes, you should complete compatibility validation before upgrading.

## Understand v1.37 in One Minute

- **Networking**: `kube-proxy`'s ipvs mode begins deprecation; it is expected to be disabled by default in v1.40 and fully removed in v1.43; alternative modes should be evaluated as early as possible.
- **Node Runtime**: CGroup v1 has entered its exit phase; Rootless kubelet is expected to advance to Beta, providing a new option for reducing reliance on host-level root privileges.
- **Storage and Security**: SELinuxMount is expected to be enabled by default. Pods that share the same volume using different SELinux labels need focused regression testing; volume health monitoring is being re-proposed in Alpha form.
- **Observability**: the `metrics.k8s.io` API is expected to end nearly nine years in Beta and graduate to stable (GA).

## Deprecations and Removals in Kubernetes v1.37

### kubectl: `kubectl run --filename/-f` to Be Deprecated

The `--filename` (or `-f`) flag of `kubectl run` will be deprecated,
because the resulting Pod is always built purely from CLI arguments such as `NAME` and `--image`.

See the original issue and discussion at
[kubernetes/kubernetes#138671](https://github.com/kubernetes/kubernetes/issues/138671).

### kubelet: Static Pods Can No Longer Reference Secrets or ConfigMaps

Static Pods were never intended to read API resources directly, since they are not created through the API server —
but a defect once allowed them to reference Secrets or ConfigMaps via fields such as `configMapRef` or `secretRef`.
That defect is now fixed: starting from v1.37, these references are strictly prohibited,
and the `PreventStaticPodAPIReferences` feature gate previously used to bypass this restriction has been removed.

See the original issue and discussion at
[kubernetes/kubernetes#140226](https://github.com/kubernetes/kubernetes/issues/140226).

### Deprecating kube-proxy's Support for the `ipvs` Mode

`kube-proxy`'s support for the `ipvs` mode was introduced in v1.8 to address `iptables` performance bottlenecks.
However, because the kernel `ipvs` API alone cannot fully implement Kubernetes Service,
the `ipvs` mode still continues to use `iptables` at the bottom layer
([KEP-3866, "the ipvs mode of kube-proxy will not save us"](https://github.com/kubernetes/enhancements/blob/master/keps/sig-network/3866-nftables-proxy/README.md#the-ipvs-mode-of-kube-proxy-will-not-save-us)).

Clusters running `kube-proxy` in ipvs mode (or with `mode: ipvs` set in KubeProxyConfiguration)
now log a deprecation warning at startup. The deprecation timeline is as follows:

- By v1.40, `kube-proxy`'s `ipvs` mode is expected to be disabled by default (still selectable via a feature gate)
- By v1.43, support for the `ipvs` mode will be fully removed
  [KEP-5495, graduation criteria](https://github.com/kubernetes/enhancements/blob/master/keps/sig-network/5495-deprecate-ipvs-mode-in-kube-proxy/README.md#graduation-criteria).

To confirm which mode you are currently running, use:

```bash
kubectl -n kube-system get configmap kube-proxy -o jsonpath='{.data.config\.conf}' | grep 'mode:'
```

To understand the rationale behind this deprecation, see
[KEP-5495: Deprecating the ipvs Mode in kube-proxy](https://kubernetes.dev/resources/keps/5495).

## Ongoing Major Change: Support for CGroup v1 Will Be Removed in the Future

As modern Linux distributions and container runtimes use
[CGroup v2](https://kubernetes.io/zh-cn/docs/concepts/architecture/cgroups/) as the default,
support for the legacy CGroup v1 is being formally phased out.
Since v1.35, the `failCgroupV1` setting defaults to true.
Therefore, `kubelet` will fail to initialize on any node that still depends on CGroup v1,
unless an explicit configuration override is applied.

```yaml
apiVersion: kubelet.config.k8s.io/v1beta1
kind: KubeletConfiguration
failCgroupV1: false # Temporary override
```

Using this override should be considered a short-term fix.
Advanced resource management capabilities, such as In-Place Pod Resizing and
Tiered Memory Protection, depend entirely on CGroup v2.
Although this override remains available in Kubernetes v1.37, users are encouraged to migrate to CGroup v2,
since support for CGroup v1 is planned to be removed in a future release.

To learn more about this deprecation, see
[KEP-5573: Removing CGroup v1 Support](https://kubernetes.dev/resources/keps/5573).

## Breaking Changes in Kubernetes v1.37

### SELinux Volume Relabeling ("SELinuxMount") Reaches GA  {#SELinuxMount-GA}

SELinuxMount is expected to reach GA and be enabled by default in v1.37.
At that point, volumes will be mounted using `-o context=<label>` (the default mount option),
rather than being recursively relabeled, but **only when** the volume's CSI driver opts in by setting
`.spec.seLinuxMount: true` on its CSIDriver.

Because a single mount can hold only one SELinux context,
Pods that share a volume on the same node with different SELinux labels
(which could previously coexist under recursive relabeling) may now fail to start.
To preserve the previous recursive behavior for a specific workload, set
`seLinuxChangePolicy: Recursive` in the Pod spec.

Clusters that do not enable SELinux are completely unaffected.
To learn more, see
[SELinux Volume Labeling Changes Reaching GA (and Potential Impact in v1.37)](https://kubernetes.io/zh-cn/blog/2026/04/22/breaking-changes-in-selinux-volume-labeling/)

## Key Enhancements in Kubernetes v1.37

### Metrics API Reaches GA

After nearly nine years in Beta, the
`metrics.k8s.io` API is expected to graduate to stable (GA) in Kubernetes v1.37.
This API provides a standard way to retrieve CPU and memory usage of Pods and nodes,
powering widely used Kubernetes features such as the Horizontal Pod Autoscaler (HPA)
and commands like `kubectl top`.

This graduation recognizes the API's stability and broad adoption, and no functional changes are expected.
During the transition, both `v1` and `v1beta1` will remain available,
allowing developers to adopt the stable API at their own pace without breaking existing workflows.

To learn more about this enhancement, see
[KEP-5207: metrics.k8s.io API Definition](https://www.kubernetes.dev/resources/keps/5207/).

### kubelet in UserNS, a.k.a. Rootless Mode

Traditionally, Kubernetes node components such as `kubelet` run with root privileges on the host.
While necessary for many deployments, this also means a vulnerability in one of these components could have a larger impact on the underlying system.

In Kubernetes v1.37, kubelet in a user namespace
(a.k.a. Rootless mode) is expected to graduate to Beta.
This enhancement allows Kubernetes node components to run as an unprivileged user on the host within a Linux user namespace,
while still appearing as root inside the namespace.
By reducing the need for host-level root privileges, it adds an extra layer of isolation
and helps limit the blast radius of potential vulnerabilities affecting node components.

To learn more about this enhancement, see
[KEP-2033: Kubelet in UserNS (a.k.a. Rootless Mode)](https://kubernetes.dev/resources/keps/4960).

### Volume Health Monitoring

Historically, Kubernetes lacked an API for CSI drivers to report storage failures,
which only became apparent through mount failures or I/O hangs.
Since the remediation controller had no machine-readable content to work with,
the only way to find the root cause behind such failures was to cross-reference Kubernetes
objects with external vendor dashboards.

In Kubernetes v1.37, this KEP resets its graduation status to Alpha after its initial implementation in v1.21,
and introduces four new CSI RPCs. The controller plugin uses
`ControllerListVolumeHealth` (to list unhealthy volumes) and
`ControllerGetVolumeHealth` (to inspect a specific volume) to report the health of storage volumes.
The controller-side health monitor polls these CSI controllers and stores the results in
`PersistentVolumeClaim.status.healthStatus`.

On the node side, kubelet calls `NodeGetVolumeHealth` to obtain the health of each volume on that node,
and records it in `Pod.status.volumeHealth`;
while `NodeGetStorageHealth` reports the health of drivers registered to the node in
`CSINode.status.storageHealth`.

The error vocabulary is kept simple, extensible, and machine-parseable (`Inaccessible`, `Degraded`, etc.),
and can provide more driver-specific details through `reason` and `message`.
Finally, controller-side and node-side reports are kept independent, so they are displayed separately,
providing consumers with a more comprehensive view of storage health.

To learn more about this enhancement, see
[KEP-1432: Volume Health Monitoring](https://kubernetes.dev/resources/keps/1432).

## DaoCloud and the Kubernetes Community: Governance, Technology, and Outreach

Kubernetes' continuous evolution relies on the long-term investment of global contributors across governance, technical implementation, and community outreach.
The DaoCloud team also continues to participate:

- **[Paco Xu](https://github.com/pacoxu)**, as a member of the Kubernetes Steering Committee, participates in project governance and community leadership, promoting the community's open collaboration and sustainable development.
- **[Baofa Fan](https://github.com/carlory)** continuously invests in Kubernetes technical features and engineering practices, contributing professional experience to the community's technical evolution.
- **[Wei Cai](https://github.com/iceber)**, as a CNCF Ambassador, has organized multiple KCD (Kubernetes Community Days) events, connecting developers, users, and community contributors.
- **[Weizhou Lan](https://github.com/weizhoublue)** and **[yankay](https://github.com/yankay)** focus on networking and scheduling respectively, and have appeared on the KubeCon stage multiple times as speakers, sharing practices and thoughts in cloud native infrastructure.
- DaoCloud also has a dozen-plus Maintainers distributed across various Kubernetes SIG groups contributing core code.

From version feature discussions to offline technical exchanges, DaoCloud hopes to work with more developers to turn the community's new capabilities into stable, deployable production practices.

## Want to Learn More?

New features and deprecations are also announced in the Kubernetes release notes.
We will officially announce the new content in
[Kubernetes v1.37](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.37.md)
as part of that release's CHANGELOG.

Kubernetes v1.37 is planned for release on **Wednesday, August 26, 2026**. Stay tuned for updates!

You can view the change announcements in the release notes of the following versions:

* [Kubernetes v1.36](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.36.md)
* [Kubernetes v1.35](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md)
* [Kubernetes v1.34](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md)
* [Kubernetes v1.33](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md)
