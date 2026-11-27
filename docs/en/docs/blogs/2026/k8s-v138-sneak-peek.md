# Kubernetes v1.38 Sneak Peek: Legacy cgroup Mechanisms Exit as Resource Management Advances

> The original blog is published at
> [k8s.io/blog/](https://kubernetes.io/blog/2026/11/23/kubernetes-v1-38-sneak-peek/)

Kubernetes v1.38 is shaping up to be a release centered on
**streamlined configuration and more advanced resource management**:
`kubectl` removes two legacy configuration options, and the retirement of cgroup v1 is
entering its countdown.
Meanwhile, kuberc, pod-level resources, and DRA partitionable devices are expected to graduate
to stable, and the EvictionRequest API arrives in alpha with a more coordinated way to evict Pods.

This post outlines the planned changes in v1.38 that platform teams and cluster operators should
prioritize. The information below reflects the current state of the release cycle and may change
before the actual release date.

!!! tip

    If your cluster still runs on cgroup v1, put its migration on the near-term roadmap;
    if your workloads use pod-level resources and rely on swap, complete compatibility
    validation before upgrading.

## v1.38 at a glance

| Area | Key changes |
| --- | --- |
| kubectl | The `KUBECTL_REMOTE_COMMAND_WEBSOCKETS` and `KUBECTL_PORT_FORWARD_WEBSOCKETS` environment variables are removed; kuberc is expected to graduate to stable, retiring the `name` field in credential plugin allowlist entries. |
| Nodes and runtimes | Support for cgroup v1 continues to be phased out; the modernization of kubelet cgroup driver configuration is deferred to v1.39. |
| Scheduling and resources | Pod-level resources and DRA partitionable devices are expected to graduate to stable; swap limits on `LimitedSwap` nodes are computed from pod-level memory settings instead. |
| New feature | The EvictionRequest API (alpha) introduces coordinated Pod eviction, giving applications a chance to finish cleanup before they are terminated. |

## Deprecations and removals in Kubernetes v1.38

### kubectl: WebSocket opt-out environment variables removed

`kubectl` has used WebSockets instead of SPDY by default for `kubectl exec`, `attach` and `cp` since
v1.30, and for `kubectl port-forward` since v1.31. The `KUBECTL_REMOTE_COMMAND_WEBSOCKETS` and
`KUBECTL_PORT_FORWARD_WEBSOCKETS` environment variables let you turn that behavior off. These
variables are going to be removed in v1.38. `kubectl` will then always try WebSockets first and fall
back to SPDY when it needs to (the same as the current default behavior). If your scripts or CI
environments set either of these environment variables, you can remove them since they will no
longer have any effect.

To learn more, refer to
[KEP-4006: Transition from SPDY to WebSockets](https://kubernetes.dev/resources/keps/4006).

### kubectl: `name` dropped from kuberc credential plugin allowlist entries

The `kuberc` file keeps kubectl user preferences separate from cluster credentials in the
kubeconfig, including an allowlist of the credential plugins `kubectl` is allowed to run. In the
beta `kubectl.config.k8s.io/v1beta1` API, an allowlist entry can use `name` as an alias for
`command`. The `name` field (not `command`) has been deprecated since v1.36.

With `kuberc` expected to graduate to stable in v1.38, the new `kubectl.config.k8s.io/v1` API will
not include `name`. If any of your allowlist entries use `name`, change them to `command` now.

To learn more, refer to
[KEP-3104: Separate kubectl user preferences from cluster configs](https://kubernetes.dev/resources/keps/3104).

## Ongoing major changes

### Future removal of cgroup v1 support

Support for cgroup v1 is being phased out. Since v1.35, the kubelet fails to start on nodes that use
cgroup v1 unless you set `failCgroupV1: false` in the kubelet configuration. This option remains
available in v1.38, but it should be treated as a short-term fix as support for cgroup v1 is planned
to be removed in a future release. If you haven't already, please plan your migration to
[cgroup v2](https://kubernetes.io/docs/concepts/architecture/cgroups/).

To learn more, refer to
[KEP-5573: Remove cgroup v1 support](https://kubernetes.dev/resources/keps/5573).

### Admission webhooks no longer receive authentication and authorization review requests

Since v1.37, the `ExcludeAdmissionWebhookVirtualResources` feature gate has been enabled by default.
With it on, validating and mutating admission webhooks no longer receive requests for (virtual)
writes to TokenReview, SelfSubjectReview, SubjectAccessReview, SelfSubjectAccessReview,
LocalSubjectAccessReview or SelfSubjectRulesReview. Creating or updating a webhook configuration
whose rules name one of these resources returns a deprecation warning, and the API server logs any
existing configurations that are affected when it starts.

If you rely on a webhook to see these requests, you can turn the feature gate off for now, but note
that the gate is planned to be locked on when the feature graduates to stable.

To learn more, refer to
[KEP-5793: Manifest Based Admission Control Config](https://kubernetes.dev/resources/keps/5793).

### Container runtimes reporting the cgroup driver: migration deferred to v1.39

The kubelet in v1.37 and older supported releases provides a legacy mechanism to configure the
cgroup driver. The modern way to do that is via the CRI `RuntimeConfig` RPC, which reports the
cgroup driver that the container runtime recommends using. As originally planned, v1.38 would
disable this legacy configuration mechanism by default and require container runtimes to run
**before** the kubelet starts (see
[kubernetes/kubernetes#136731](https://github.com/kubernetes/kubernetes/pull/136731)).
Because the relevant change did not land within the v1.38 release cycle, this migration is
**deferred to v1.39**.

In v1.38, the `cgroupDriver` field in the kubelet configuration file continues to work as before,
and no extra action is needed for this during the upgrade. If you manage your own nodes or node
images, verify ahead of time that your container runtime supports `RuntimeConfig` so that you are
ready for the migration in v1.39. To learn more, refer to
[KEP-4033: Discover cgroup driver from CRI](https://kubernetes.dev/resources/keps/4033).

## Breaking changes in Kubernetes v1.38

### Pod-level resources: swap behavior changes on `LimitedSwap` nodes {#pod-level-resources-swap}

If you use pod-level resources on Linux nodes that use cgroup v2 and are configured with
`LimitedSwap`, the kubelet in v1.38 will start applying swap limits based on the Pod's pod-level
memory settings. This means that Pods whose pod-level memory request equals their memory limit will
get no swap at all (both for the Pod and for every container in it), even if a container sets a
memory request lower than its limit. Check any workloads that rely on swap before you upgrade, and
be sure to read the official release notes for v1.38 for detailed advice.

To learn more, refer to
[KEP-2837: Pod Level Resource Specifications](https://kubernetes.dev/resources/keps/2837).

## Featured enhancements in Kubernetes v1.38

The following list of enhancements is likely to be included in the upcoming v1.38 release. This is
not a commitment and the release content is subject to change.

### kubectl user preferences (kuberc) graduating to stable

kuberc, the separate kubectl configuration file for user preferences such as aliases, default
options and a credential plugin policy, is expected to graduate to stable in v1.38.

To learn more, read
[Kubectl user preferences (kuberc)](https://kubernetes.io/docs/reference/kubectl/kuberc/)
or refer to
[KEP-3104: Separate kubectl user preferences from cluster configs](https://kubernetes.dev/resources/keps/3104).

### Pod-level resources graduating to stable

Pod-level resources, which let you set CPU, memory and hugepages requests and limits for a Pod as a
whole, are expected to graduate to stable in v1.38. If you run Linux nodes with `LimitedSwap`, see
the [swap behavior change](#pod-level-resources-swap) above before you upgrade.

To learn more, read
[Assign Pod-level CPU and memory resources](https://kubernetes.io/docs/tasks/configure-pod-container/assign-pod-level-resources/)
or refer to
[KEP-2837: Pod Level Resource Specifications](https://kubernetes.dev/resources/keps/2837).

### DRA support for partitionable devices graduating to stable

Partitionable devices let a
[Dynamic Resource Allocation](https://kubernetes.io/docs/concepts/resource-management/dynamic-resource-allocation/)
(DRA) driver advertise a device such as a GPU both as a whole and as smaller partitions, and the
scheduler allocates only combinations that fit within the physical device. The feature is expected
to graduate to stable in v1.38, and the `DRAPartitionableDevices` feature gate will then be locked
on.

To learn more, read
[Partitionable devices](https://kubernetes.io/docs/concepts/resource-management/dynamic-resource-allocation/dra-features/#partitionable-devices)
or refer to
[KEP-4815: DRA: Add support for partitionable devices](https://kubernetes.dev/resources/keps/4815).

### EvictionRequest API (alpha)

Evicting a Pod isn't always as simple as terminating it. Some applications may be in the middle of
important work, such as data migration or cleanup, and terminating them without giving them time to
prepare can cause disruptions.

The EvictionRequest API introduces a more coordinated way to evict Pods. It gives applications and
controllers time to prepare before a Pod is evicted. For example, when a node needs to be drained or
a Pod needs to be moved to another node, a controller can create an EvictionRequest to signal that
this Pod needs to be evicted.

The eviction request controller coordinates with the responders configured for the Pod. These
responders can perform application-specific tasks such as completing ongoing work, cleaning up
resources, or migrating data before the Pod is terminated.

If no custom responder is available or responders don't complete the process, Kubernetes can fall
back to the existing API-initiated eviction mechanism, which continues to respect
PodDisruptionBudgets (PDBs). The EvictionRequest API does not replace PDBs. It gives applications a
chance to participate in the eviction process.

As this is an alpha feature, you will need to enable the `EvictionRequestAPI` feature gate **and**
the relevant alpha API group. Check the v1.38 release notes and documentation, once they're
available, to confirm exactly what's required.

To learn more, refer to [KEP-4563: EvictionRequest API](https://kubernetes.dev/resources/keps/4563).

## DaoCloud and the Kubernetes community: governance, technology, and advocacy

The continued evolution of Kubernetes depends on the long-term commitment of contributors worldwide
across governance, technical implementation, and community advocacy.
The DaoCloud team has been an active participant:

- **[Paco Xu](https://github.com/pacoxu)** serves on the Kubernetes Steering Committee
  (elected in 2023, re-elected in 2025 through 2027), contributing to project governance and
  community leadership, and also serves as Chair of the CNCF TAG Workloads Foundation and a
  CNCF Ambassador.
- **[Baofa Fan](https://github.com/carlory)** continuously invests in Kubernetes technical
  features and engineering practices, contributing professional expertise to the community's
  technical evolution.
- **[Wei Cai](https://github.com/iceber)** and **[Michael Yao](https://github.com/windsonsea)**
  are both CNCF Ambassadors, connecting developers, users, and community contributors.
  Michael Yao has served multiple times on the KubeCon Program Committee, organizes community
  events such as KCD, reviews pull requests and issues across Kubernetes ecosystem projects,
  and is continuously engaged in community building.
- **[Weizhou Lan](https://github.com/weizhoublue)** and **[yankay](https://github.com/yankay)**
  focus on networking and scheduling respectively and have spoken at KubeCon multiple times,
  sharing their practices and insights in cloud native infrastructure.
- More than ten other DaoCloud maintainers contribute core code across Kubernetes SIGs, and
  DaoCloud engineers have received the Kubernetes annual Contributor Award six times in total.

According to CNCF DevStats, DaoCloud ranks **among the top three worldwide and first in China**
in Kubernetes core code contributions; DaoCloud engineers hold several spots among the top 100
contributors of the `kubernetes/kubernetes` repository. DaoCloud is also deeply involved in
AI compute scheduling and inference projects such as HAMi, Kueue, and llm-d, helping more
organizations turn new community capabilities into stable, production-ready practices.

As a Kubernetes Certified Service Provider (KCSP) certified by the CNCF as early as 2017,
see [DaoCloud is a certified Kubernetes and AI Platform provider](../../dce/kcsp.md) for details
of our certifications and per-release conformance.

## Want to know more?

New features and deprecations are also announced in the Kubernetes release notes. We will formally
announce what's new in [Kubernetes v1.38](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.38.md)
as part of the CHANGELOG for that release.

The Kubernetes v1.38 release is planned for **Wednesday, December 16th, 2026**. Stay tuned for updates!

You can see the announcements of changes in the release notes for:

- [Kubernetes v1.37](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.37.md)
- [Kubernetes v1.36](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.36.md)
- [Kubernetes v1.35](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md)
