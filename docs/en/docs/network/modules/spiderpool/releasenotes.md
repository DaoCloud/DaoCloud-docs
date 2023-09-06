# Spidernet Release Notes

This page lists the Release Notes of Spidernet, so that you can understand the evolution path and feature changes of each version.

The included Spiderpool is an IPAM module developed by DaoCloud. Please refer to the [Spiderpool Release Notes](https://github.com/spidernet-io/spiderpool/releases) for more information.

## 2023-07-28

### v0.8.1

Compatible with **Spiderpool version** : `v0.6.0`

#### New Features

- **Added** `nodeName` and `multusName` fields in Spiderpool CR to support node topology and configure networks as needed
- **Added** Spiderpool provides SpiderMultusConfig CR, which simplifies the configuration of Multus CNI in JSON format and automatically manages Multus NetworkAttachmentDefinition CR
- **Added** Spiderpool provides Coordinator plugin to solve issues such as Underlay Pods unable to access ClusterIP, routing of tuned Pods, detection of IP conflicts in Pods, and reachability of Pod gateways. Refer to [Coordinator documentation](https://github.com/spidernet-io/spiderpool/blob/main/docs/usage/coordinator-zh_CN.md)
- **Added** Deep support for IPVlan, suitable for any public cloud environment
- **Added** Support for multiple default IP pools to simplify usage
- **Added** CNI plugin `Ifacer` for automatic creation of sub-interfaces. Refer to [`Ifacer` documentation](https://github.com/spidernet-io/spiderpool/blob/main/docs/usage/ifacer-zh_CN.md)
- **Added** Ability to specify default route network interfaces through Pod annotations
- **Added** Support for automatic pool recycling switch to customize whether automatic pools should be deleted
- **Improved** Support for elastic IPs in cluster subnets, resolving the issue where new Pods do not have available IPs while old Pods are not yet deleted during rolling updates of applications.

## 2023-06-28

### v0.8.0

Compatible with Spiderpool version: `v0.5.0`

#### Enhancements

- **Added** definition of Multus API in `spidernet`
- **Improved** stability of `spidernet` e2e
- **Fixed** `spidernet` `goproduct` Proxy Config
- **Optimized** default replication to 2 in `spidernet`

## 2023-05-28

### v0.7.0

Compatible with Spiderpool version: `v0.4.1`

#### Fixes

- **Fixed** subnet sorting issue based on IP in `spidernet`

## 2022-04-28

### v0.6.0

Adapted to **Spiderpool version** : `v0.4.1`

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

- **Fixed** The stateful load uses the automatic IP pool, the IP pool is created successfully, the IP allocation is successful, and the query IP pool is empty.

- **Fixed** Subnet Management-Delete Subnet, choose to delete a subnet, the system prompts success, but the subnet is still there after refreshing.

- **Fixed** Click "Container Network Card" several times, but can't get data.

- **Fixed** Spidernet-UI Service Label in `Spidernet Chart` is incorrect.

## 2022-02-28

### v0.4.4

#### Optimization

- **Optimized** Adjust the CPU memory Request value.

#### Fixes

- **Fixed** The stateful load uses the automatic IP pool, the IP pool is created successfully, the IP allocation is successful, and the query IP pool is empty.

- **Fixed** Subnet Management - Delete subnet, choose to delete a subnet, the system prompts success, but the subnet is still there after refreshing.

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