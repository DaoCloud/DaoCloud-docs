# Spidernet Release Notes

This page lists the Release Notes of Spidernet, so that you can understand the
evolution path and feature changes of each version.

Spidernet includes:

- Spiderpool, an open-source IPAM module developed by DaoCloud. Refer to
  [Spiderpool Release Notes](https://github.com/spidernet-io/spiderpool/releases).
- Egressgateway, an open-source egress gateway module developed by DaoCloud. Refer to
  [Egressgateway Release Notes](https://github.com/spidernet-io/egressgateway/releases).

### 2023-10-30

#### v0.10.1

- Compatible with **Spiderpool v0.8.0**
- Compatible with **Egressgateway v0.3.0**

#### New Features

- **Added** Support for Egress gateway to select a group of nodes using node selectors as Egress nodes
  and forward external traffic through specified nodes.
- **Added** Support for configuring IP pools for node groups to ensure sufficient available IP addresses
  for different nodes or node groups in the network.
- **Added** Support for setting EIP (Egress IP) for namespaces or workloads under Calico, Flannel, Weave,
  and Spiderpool network modes. Pods will use this EIP as the outbound address when accessing the external network.
- **Added** Support for setting a default Egress IP as the cluster or namespace's outbound address.
- **Added** Support for outbound traffic control through gateway policies, including filtering
  outbound traffic based on destination CIDR.
- **Added** Support for viewing default EgressIP, EgressIP pools, node lists, and node IP address ranges
  in Egress gateway.
- **Added** Support for using Pod label selectors or source addresses in gateway policies to select Pods
  that will use Egress and specify Pods that follow specific gateway policies.
- **Added** Support for network configuration control by viewing selected gateways, EgressIPs or node IPs,
  container group, etc., in gateway policies.
- **Added** Support for using Egressgateway in lower kernel versions.
- **Added** Management interface for Multus CR, supporting the creation of CR instances using different
  Multus CNI types (including Macvlan, IPvlan, SRIOV, custom).
- **Added** RDMA CNI and RDMA device plugin integration in Spiderpool.
- **Added** Chart configuration information for `sriov network operator`.
- **Added** Support for assigning static IP addresses to KubeVirt virtual machines.
- **Added** Installation of CNI, OVS, and RDMA in the initialization container of SpiderAgent.

#### Optimizations

- **Optimized** Upgrade OpenTelemetry version to 1.19.0.
- **Optimized** During Spiderpool initialization, if the default SpiderMultusConfig network is not empty,
  it will be automatically created.
- **Optimized** All plugins have built new Docker images.
- **Optimized** Improved GetTopController method.
- **Optimized** Corresponding CNI types in Multus CR management for workload network configuration.

#### Fixes

- **Fixed** Issue with eth0 source IP in packets transmitted by coordinator through veth0.
- **Fixed** Error caused by empty `spidermultusconfig.spec` in SpiderMultusConfig.
- **Fixed** Issue with SpiderCoordinator when automatically determining PodCIDR type.

## 2023-08-30

### v0.9.0

Compatible with **Spiderpool v0.7.0**

#### New Features

- **Added** Annotation Webhook validation for SpiderMultusConfig
- **Added** Allocation of single-stack IP under dual-stack SpiderSubnet auto pool functionality
- **Added** Optimization of IPAM core algorithm, prioritizing IP allocation in affinity pools
- **Added** Creation of orphan IPPool under SpiderSubnet auto pool functionality
- **Added** Removal of CNI configuration files in Multus uninstallation hooks
- **Added** Support for automatic mode (default) in Coordinator, which automatically detects the working mode
  without the need for manual specification of Underlay or Overlay. The same multus CNI configuration can be
  used as both Underlay and Overlay modes.
- **Added** Configuration of `ovs-cni` through `spidermultusconfig`

#### Bug Fixes

- **Fixed** Bug where pods without controllers fail to start when annotated with auto pool
- **Fixed** Coordinator Webhook validation bug
- **Fixed** Coordinator listening to Calico resources bug
- **Fixed** Incorrect VLAN range in CRD
- **Fixed** Resource name length limitation in auto pool
- **Fixed** Failed route addition in Coordinator
- **Fixed** Clearing of collected cluster subnet information if `spidercoordinator.status.phase`
  is not Ready and preventing pod creation
- **Fixed** Clearing of `resourceName` field for `sriov-cni` in `spidermultusconfig`
- **Fixed** Validation of custom CNI configuration file in `spidermultusconfig` to ensure it is a valid JSON format
- **Fixed** Uniform creation of routes for all nodes and pods in host's `table500` instead of each pod having its own table

## 2023-07-28

### v0.8.1

Compatible with **Spiderpool v0.6.0**

#### New Features

- **Added** `nodeName` and `multusName` fields in Spiderpool CR to support node topology and
  configure networks as needed
- **Added** Spiderpool provides SpiderMultusConfig CR, which simplifies the configuration of
  Multus CNI in JSON format and automatically manages Multus NetworkAttachmentDefinition CR
- **Added** Spiderpool provides Coordinator plugin to solve issues such as Underlay Pods unable to
  access ClusterIP, routing of tuned Pods, detection of IP conflicts in Pods, and reachability of
  Pod gateways. Refer to
  [Coordinator documentation](https://github.com/spidernet-io/spiderpool/blob/main/docs/usage/coordinator.md)
- **Added** Deep support for IPVlan, suitable for any public cloud environment
- **Added** Support for multiple default IP pools to simplify usage
- **Added** CNI plugin `Ifacer` for automatic creation of sub-interfaces. Refer to
  [`Ifacer` documentation](https://github.com/spidernet-io/spiderpool/blob/main/docs/usage/ifacer.md)
- **Added** Ability to specify default route network interfaces through Pod annotations
- **Added** Support for automatic pool recycling switch to customize whether automatic pools should be deleted
- **Improved** Support for elastic IPs in cluster subnets, resolving the issue where new Pods do not
  have available IPs while old Pods are not yet deleted during rolling updates of applications.

## 2023-06-28

### v0.8.0

Compatible with **Spiderpool v0.5.0**

#### Enhancements

- **Added** definition of Multus API in `spidernet`
- **Improved** stability of `spidernet` e2e
- **Fixed** `spidernet` `goproduct` Proxy Config
- **Optimized** default replication to 2 in `spidernet`

## 2023-05-28

### v0.7.0

Compatible with **Spiderpool v0.4.1**

#### Fixes

- **Fixed** subnet sorting issue based on IP in `spidernet`

## 2022-04-28

### v0.6.0

Compatible with **Spiderpool v0.4.1**

#### Fixes

- **Fixed** Pointer error when viewing workload on single stack
- **Fixed** Controller timeout when adding large number of IPs
- **Fixed** Affinity can be filled in Chinese
- **Fixed** Workload name does not match with namespace
- **Fixed** Auto pool display problem
- **Fixed** Route deletion issue
- **Fixed** Paging number display issue
- **Fixed** Get IP pools by Pod issue
- **Fixed** Cache issue with sequential fast delete

#### Features

- **Added** Fill in VLAN ID when creating IP pools
- **Added** Show IP total and used number
- **Added** `e2e` automatically uses the latest version of the DCE component

## 2022-03-28

### v0.5.0

#### Optimization

- **Optimized** Spidernet API, adapted to **Spiderpool v0.4.0** new version CRD

#### Fixes

- **Fixed** The stateful load uses the automatic IP pool, the IP pool is created successfully,
  the IP allocation is successful, and the query IP pool is empty.
- **Fixed** Subnet Management-Delete Subnet, choose to delete a subnet, the system prompts success,
  but the subnet is still there after refreshing.
- **Fixed** Click "Container Network Card" several times, but can't get data.
- **Fixed** Spidernet-UI Service Label in `Spidernet Chart` is incorrect.

## 2022-02-28

### v0.4.4

#### Optimization

- **Optimized** Adjust the CPU memory Request value.

#### Fixes

- **Fixed** The stateful load uses the automatic IP pool, the IP pool is created successfully,
  the IP allocation is successful, and the query IP pool is empty.
- **Fixed** Subnet Management - Delete subnet, choose to delete a subnet, the system prompts
  success, but the subnet is still there after refreshing.
- **Fixed** Click "Container Network Card" several times, but can't get data.
- **Fixed** Spidernet-UI Service Label in `Spidernet Chart` is incorrect.

## 2022-11-30

### v0.4.3

#### Optimization

- **Optimized** resource usage, reduce CPU and memory requests.

### v0.4.2

#### Optimization

- **Optimized** resource usage, reduce CPU and memory requests.
- **Optimized** Subnet or IPPool cannot be deleted when IP is occupied.
- **Optimized** pagination issue

### v0.4.1

#### Features

- **Added** Added features such as interface-based IP reservation and IP release reservation.
- **Added** IP pool management, which can be created, edited, and deleted based on the interface.
- **Added** The workload uses the multi-NIC feature of the container, and the IP pool can be selected and fixed.
- **Added** Check the number of available IPs/total IPs in the application fixed IP pool.

#### Optimization

- **Optimized** resource usage, reduce CPU and memory requests.