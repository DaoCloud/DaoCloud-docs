# containerd v2.0, nerdctl v2.0, and Lima v1.0

> source from [medium.com](https://medium.com/nttlabs/containerd-v2-0-nerdctl-v2-0-lima-v1-0-93026b5839f8)

Ahead of the [KubeCon North America 2024](https://events.linuxfoundation.org/kubecon-cloudnativecon-north-america/)
(November 12–15), this week saw the releases of [containerd](https://github.com/containerd/containerd) v2.0,
[nerdctl](https://github.com/containerd/nerdctl) (*contaiNERD CTL*) v2.0, and [Lima](https://lima-vm.io/) v1.0 🎉.

![three-container-runtime](./images/containerd01.png)

## containerd v2.0

[containerd](https://github.com/containerd/containerd) is the industry’s standard container runtime
used by Docker and several Kubernetes-based products such as Azure Kubernetes Service (AKS),
Amazon Elastic Kubernetes Service (EKS), and Google Kubernetes Engine (GKE).

containerd was originally written by Docker, Inc. in [2015](http://web.archive.org/web/20151217223538/https://containerd.tools/)
to provide a minimalistic daemon to manage the lifecycles of containers, under the hood of the Docker daemon.

containerd was [transferred](https://www.cncf.io/announcements/2017/03/29/containerd-joins-cloud-native-computing-foundation/)
to the [Cloud Native Computing Foundation](https://cncf.io/) (CNCF) and reached its
[v1.0](https://github.com/containerd/containerd/releases/tag/v1.0.0) in 2017,
with the expanded scope of the project to support non-Docker use cases.
The built-in support for Kubernetes was merged in
[v1.1](https://github.com/containerd/containerd/releases/tag/v1.1.0) (2018).

containerd v2.0 focuses on the removal of the legacy features that have been deprecated
through the past nine years. This breaking change resulted in bumping up the major number from v1 to v2.

### Removed features

- [The old containerd-shim](https://github.com/containerd/containerd/pull/8262) and
  [containerd-shim-runc-v1](https://github.com/containerd/containerd/pull/8262),
  in favor of `containerd-shim-runc-v2`. The old shims lacked the support for modern
  features such as cgroup v2, and were inefficient to support Kubernetes pods.
  Those old shims had been deprecated since containerd v1.4 (2020).
- [The support for AUFS](https://github.com/containerd/containerd/pull/8263),
  in favor of OverlayFS that has been merged in the upstream of the Linux kernel.
  The support for AUFS had been deprecated since containerd v1.5 (2021).
- [The support for the Kubernetes CRI v1alpha2 API](https://github.com/containerd/containerd/pull/8276),
  in favor of CRI v1. Kubernetes has already dropped the support for CRI v1alpha2, in
  [Kubernetes v1.26](https://github.com/kubernetes/kubernetes/blob/v1.26.0/CHANGELOG/CHANGELOG-1.26.md?plain=1#L482) (2022).
- [The support for "Docker Schema 1" images is now disabled](https://github.com/containerd/containerd/pull/9765),
  in preparation of removal in containerd v2.1. Schema 1 has been substantially deprecated since 2017 in favor of
  Schema 2 introduced in Docker v1.10 (2016), but some image registries did not support Schema 2 until 2020-ish.
  Docker has already disabled pushing Schema 1 images in [Docker v20.10](https://github.com/moby/moby/pull/41295) (2020),
  so almost all images built in the last few years should have been formatted in Schema 2, or, its successor
  [OCI Image Spec](https://github.com/opencontainers/image-spec) v1.
  ("OCI" here refers to "Open Container Initiative", not to "Oracle Cloud Infrastructure".)

containerd v1.6.27+/v1.7.12+ users can investigate whether they are using those removed features,
by running the `ctr deprecations list` command.

### New features

- [User Namespaces for Kubernetes](https://kubernetes.io/docs/concepts/workloads/pods/user-namespaces/),
  so as to map the user IDs in pods to different user IDs on the host. Especially, this features allows
  mapping the root user in the pod to an unprivileged user on the host.
- [Recursive Read-only Mounts for Kubernetes](https://kubernetes.io/docs/concepts/storage/volumes/#read-only-mounts),
  so as to prohibit accidentally having writable submounts. See also
[Kubernetes 1.30: Read-only volume mounts can be finally literally read-only](https://kubernetes.io/blog/2024/04/23/recursive-read-only-mounts/).
- [Image verifier plugins](https://github.com/containerd/containerd/blob/v2.0.0/docs/image-verification.md),
  so as to enforce cryptographic signing, malware scanning, etc.

### Other notable changes

- [Sandboxed CRI](https://github.com/containerd/containerd/issues/4131)
  is now enabled by default, for efficient handling of pods
- [NRI](https://github.com/containerd/nri) (Node Resource Interface) is now enabled
  by default, for plugging vendor-specific logic into runtimes
- [CDI](https://github.com/cncf-tags/container-device-interface) (Container Device Interface)
  is now enabled by default, for the enhanced support for
  [Kubernetes Device Plugins](https://github.com/kubernetes/enhancements/tree/master/keps/sig-node/4009-add-cdi-devices-to-device-plugin-api).
- `/etc/containerd/config.toml` now expects the `version=3` header.
  The previous config versions are still supported.
- The Go package `github.com/containerd/containerd` is now renamed
  to `github.com/containerd/containerd/v2/client` .

See also:

- [containerd 2.0 official document](https://github.com/containerd/containerd/blob/v2.0.0/docs/containerd-2.0.md)
- [containerd 2.0.0 release notes](https://github.com/containerd/containerd/releases/tag/v2.0.0)

## nerdctl v2.0

[nerdctl](https://github.com/containerd/nerdctl) (*contaiNERD CTL*)
is a Docker-like command line interface tool for containerd.

nerdctl was originally written by myself in 2020 to facilitate experimental features such as
[eStargz](https://github.com/containerd/nerdctl/blob/master/docs/stargz.md) that were not
supported in Docker at that time. nerdctl became a subproject of containerd in
[2021](https://github.com/containerd/project/issues/69), and reached its v1.0 in 2022.

nerdctl v2.0 enables `detach-netns` for Rootless mode by default:

- Faster and more stable `nerdctl pull`, `nerdctl push`, and `nerdctl build`
- Proper support for `nerdctl pull 127.0.0.1:.../...`
- Proper support for `nerdctl run --net=host` .

The `detach-netns`mode may sound similar to `bypass4netns`, which utilizes `SECCOMP_IOCTL_NOTIF_ADDFD`
to accelerate socket syscalls in rootless containers. While `bypass4netns` accelerates containers,
`detach-netns` accelerates the runtime layers that are responsible for pulling and pushing images,
by leaving them in the host network namespace. Containers are executed in the "detached" network
namespace so that they can obtain IP addresses used for container-to-container communications.

Other major changes in nerdctl v2.0 include the addition of `nerdctl run --systemd` for
running systemd in containers. Also, the stability was significantly improved in this release,
thanks to lots of refactoring and testing by the GitHub user `@apostasie` .

See also the [nerdctl v2.0 release note](https://github.com/containerd/nerdctl/releases/tag/v2.0.0).

## Lima v1.0

[Lima](https://lima-vm.io/) is a command line utility to run
[containerd](https://github.com/containerd/containerd) and
[nerdctl](https://github.com/containerd/nerdctl) on desktop operating systems
such as macOS, by running a Linux virtual machine with automatic filesystem
sharing and port forwarding. Lima is often compared with WSL2, former Docker Machine, and Vagrant.

```shell
brew install lima
limactl start
lima nerdctl run -p 80:80 nginx
```

Lima was originally written by myself too in 2021, and joined CNCF in 2022.
Lima has been adapted by several famous third-party projects such as
[Colima](https://github.com/abiosoft/colima), [Rancher Desktop](https://rancherdesktop.io/),
and [AWS’s Finch](https://aws.amazon.com/blogs/opensource/introducing-finch-an-open-source-client-for-container-development/).
[Lima is also used by several organizations including NTT Communications.](https://github.com/lima-vm/lima/discussions/2390#discussioncomment-9732082)

!!! info

    Lima is now a CNCF project. Lima, the Linux virtual machine for running containerd on macOS, is accepted in the CNCF Sandbox (Sep 13).

Lima finally reached v1.0 today, with the support from 110+ contributors and 15,000+ stargazers in the past 3+ years.

![star history](./images/containerd02.png)

This release introduces several breaking changes, such as switching the default machine
driver on macOS from QEMU to `Virtualization.framework` (VZ) for better filesystem performance.

The `limactl` CLI is designed to print hints when the user hits those breaking changes. e.g.,
`limactl create template://experimental/vz` now fails with a hint that suggests using
`limactl create --vm-type=vz template://default` instead.

Other notable changes include the addition of the support for
[nested virtualization](https://github.com/lima-vm/lima/pull/2530),
[UDP port forwarding](https://github.com/lima-vm/lima/pull/2411),
and the `limactl tunnel` command (SOCKS proxy).

See also the [Lima v1.0 release note](https://github.com/lima-vm/lima/releases/tag/v1.0.0).
