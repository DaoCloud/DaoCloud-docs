# Unifabric Installation Guide

## Prerequisites

1. **Kubernetes cluster**: Ensure that you have a working Kubernetes cluster.
2. **Helm 3.x**: Used to install Unifabric.
3. **RDMA network environment**: An RDMA network environment is required, supporting the RoCE
   protocol.
4. **Switch LLDP support**: Ensure that LLDP is enabled on the network switch.

## Installation Steps

> If you need to use the RDMA neighbor detection feature, ensure that LLDP is enabled on the
> network switch.

### 1. Node Label Configuration

The Unifabric Controller only runs on nodes labeled with `unifabric.io/deploy=true`. You need to
add the label to the nodes that run the Unifabric Controller:

```bash
kubectl label node <node-name> unifabric.io/deploy=true
```

The Unifabric Agent should only run on nodes with RDMA network capabilities. For nodes or virtual
machine nodes that do not support RDMA networking, set the label `unifabric.io/deploy=false` to
prevent the Unifabric Agent from running on them.

```bash
kubectl label node <node-name> unifabric.io/deploy=false
```

### 2. Add the Helm Repository

```bash
helm repo add unifabric https://release.daocloud.io/chartrepo/unifabric
helm repo update
```

### 3. Configure Installation Parameters

```shell
$ helm upgrade --install unifabric unifabric/unifabric \
  --namespace unifabric \
  --create-namespace \
  --set features.rdmaNeighbor.storageRdmaNicFilter="interface=ens2f0*"
```

`storageRdmaNicFilter` specifies which RDMA NICs on the node are used as RDMA storage NICs.
The other RDMA NICs are used as GPU compute network NICs. If this field is not configured, all
RDMA NICs are used as GPU compute network NICs.

### 4. Verify the Installation

#### Check the Pod Status

```bash
kubectl get pods -n unifabric -o wide
```

Expected output:

```
NAME                         READY   STATUS    RESTARTS   AGE
unifabric-746d4f8d75-qbknh   1/1     Running   0          2m
unifabric-agent-4rpbw        2/2     Running   0          2m
unifabric-agent-fgpkc        2/2     Running   0          2m
```

Note: The `unifabric-agent` Pod contains two containers: `lldpd` and `unifabric-agent`.

- Check the status of the FabricNode CRD:

    ```bash
    kubectl get fabricnodes.unifabric.io
    ```

    View the neighbor information of a specific node:

    ```bash
    kubectl get fabricnodes.unifabric.io <node-name> -o yaml
    ```

    Confirm that the `status.computeNics` and `status.storageNics` fields contain the correct
    LLDP neighbor information.

- Verify the ScaleoutGroup automatic grouping feature and check the ScaleoutLeafGroup CRD:

    ```bash
    kubectl get scaleoutleafgroup.unifabric.io
    ```

    Check whether the nodes have been labeled with `scaleoutleafgroup`:

    ```bash
    kubectl get nodes -l dce.unifabric.io/scaleout-group
    ```

- Check whether metrics are being collected properly:

    ```bash
    kubectl get pods -n unifabric -o jsonpath='{.items[0].status.podIP}' | xargs -I {} curl {}:5026/metrics
    ```

## Troubleshooting

See [Troubleshooting](troubleshooting.md).

## Upgrade

Upgrade Unifabric to a new version:

```bash
helm upgrade unifabric unifabric/unifabric \
  --namespace unifabric \
  --values values.yaml \
  --wait
```

## Uninstall

Uninstall Unifabric:

```bash
helm uninstall unifabric --namespace unifabric
```

For a complete cleanup, you also need to delete the CRDs and the namespace:

```bash
kubectl delete namespace unifabric
```

## Monitoring and Visualization

If the Grafana dashboard is installed, you can view Unifabric monitoring data and network
topology visualization through DCE Insight or by accessing Grafana directly.
