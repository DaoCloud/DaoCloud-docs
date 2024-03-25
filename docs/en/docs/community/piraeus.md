# Piraeus Datastore - High-Availability Datastore for Kubernetes

Piraeus is a high performance, highly-available, simple, secure, and cloud agnostic storage solution for Kubernetes.

The Piraeus Project consists of:

* A [Kubernetes Operator](https://github.com/piraeusdatastore/piraeus-operator) to create, configure and maintain all components of Piraeus.
* A [CSI Driver](https://github.com/piraeusdatastore/linstor-csi) to provision persistent volumes and snapshots on the storage cluster maintained by Piraeus.
* A [High Availability Controller](https://github.com/piraeusdatastore/piraeus-ha-controller) to speed up the failover process of stateful workloads
* A [Volume Affinity Controller](https://github.com/piraeusdatastore/linstor-affinity-controller), keeping Kubernetes Persistent Volumes reported affinity in sync with the cluster.
* Container images for the open source components Piraeus is built on:
    * [DRBD](https://github.com/LINBIT/drbd) is used as the underlying storage replication mechanism between cluster nodes.
      [Documentation](https://docs.linbit.com/docs/users-guide-9.0/) is provided by [LINBIT](https://www.linbit.com/).
    * [LINSTOR](https://github.com/LINBIT/linstor-server) creates and manages volumes on request of the CSI Driver, sets up replication using DRBD and prepares
      the backing storage devices.
      [Documentation](https://docs.linbit.com/docs/linstor-guide/) is provided by [LINBIT](https://www.linbit.com/).

Piraeus is a [CNCF Sandbox Project](https://www.cncf.io/sandbox-projects/).

## Getting started

Installing Piraeus can be as easy as:

```bash
$ kubectl apply --server-side -k "https://github.com/piraeusdatastore/piraeus-operator//config/default?ref=v2"
namespace/piraeus-datastore configured
...
$ kubectl wait pod --for=condition=Ready -n piraeus-datastore -l app.kubernetes.io/component=piraeus-operator
pod/piraeus-operator-controller-manager-dd898f48c-bhbtv condition met
$ kubectl apply -f - <<EOF
apiVersion: piraeus.io/v1
kind: LinstorCluster
metadata:
  name: linstorcluster
spec: {}
EOF
```

Head on over to the [Piraeus Operator docs](https://github.com/piraeusdatastore/piraeus-operator/tree/v2/docs) to learn more. It contains detailed instructions on how to get started
using Piraeus.

It also contains a [basic Helm chart](https://github.com/piraeusdatastore/piraeus-operator/tree/v2/charts/piraeus).

## Community

Active communication channels:

* [Slack](https://piraeus-datastore.slack.com/join/shared_invite/enQtOTM4OTk3MDcxMTIzLTM4YTdiMWI2YWZmMTYzYTg4YjQ0MjMxM2MxZDliZmEwNDA0MjBhMjIxY2UwYmY5YWU0NDBhNzFiNDFiN2JkM2Q)

Piraeus Datastore is mainly a glue project that connects LINSTOR and DRBD to Kubernetes. Therefore,
communication channels for [LINSTOR] and [DRBD] are also relevant for people interested in Piraeus
Datastore. This is ...

* [LINBIT community slack](https://linbit-community.slack.com/join/shared_invite/enQtOTg0MTEzOTA4ODY0LTFkZGY3ZjgzYjEzZmM2OGVmODJlMWI2MjlhMTg3M2UyOGFiOWMxMmI1MWM4Yjc0YzQzYWU0MjAzNGRmM2M5Y2Q#/shared-invite/email)
* [DRBD related mailing lists](https://lists.linbit.com/)
* [LINBIT community meetings](https://linbit.com/community-meeting/)

## Reference

- [Piraeus Repo](https://github.com/piraeusdatastore/piraeus)
- [Piraeus Website](https://piraeus.io/)
