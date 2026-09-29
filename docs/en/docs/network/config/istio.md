# Istio Service Mesh Adaptation (Underlay)

When Istio is used together with the Spiderpool Underlay network, sidecars may fail to hijack traffic.
This page describes the recommended adaptation configuration.

## Background

Traffic of Underlay Pods is forwarded through veth0. Istio uses iptables rules to hijack traffic,
but if veth0 has no IP address, packets may be dropped by the kernel. Spiderpool provides
`vethLinkAddress` to configure a link-local address for veth0 to resolve this issue.

## Configuration Methods

### Method 1: Enable at the cluster level (recommended)

Set `coordinator.vethLinkAddress=169.254.100.1` when installing Spiderpool.

For the installation entry, refer to [Install Spiderpool](../modules/spiderpool/install/install.md).

### Method 2: Modify at runtime

Make it take effect by modifying the default SpiderCoordinator:

```shell
kubectl patch spidercoordinators default --type='merge' -p '{"spec": {"vethLinkAddress": "169.254.100.1"}}'
```

### Method 3: For a specific NIC only

Enable it for a single Multus configuration:

```yaml
spec:
  coordinator:
    vethLinkAddress: 169.254.100.1
```

## Verification

Check veth0 inside the Pod:

```shell
kubectl exec -it <pod-name> -n <namespace> -- ip addr show veth0
```

Confirm that veth0 has the configured link-local address.

!!! note

    - `vethLinkAddress` must be a valid IP address
    - A globally consistent configuration is recommended to avoid inconsistent behavior across NICs
