# Spidernet Release Notes

This page lists the Release Notes of Spidernet, so that you can understand the evolution path and feature changes of each version.

## 2022-03-28

### v0.5.0

#### Optimization

- **Optimized** Spidernet API, adapted to **Spiderpool v0.4.0** new version CRD

#### Fix

- **Fixed** The stateful load uses the automatic IP pool, the IP pool is created successfully, the IP allocation is successful, and the query IP pool is empty.

- **Fixed** Subnet Management-Delete Subnet, choose to delete a subnet, the system prompts success, but the subnet is still there after refreshing.

- **Fixed** Click "Container Network Card" several times, but can't get data.

- **Fixed** Spidernet-UI Service Label in `Spidernet Chart` is incorrect.

## 2022-02-28

### v0.4.4

#### Optimization

- **Optimization** Adjust the CPU memory Request value.

#### Fix

- **Fixed** The stateful load uses the automatic IP pool, the IP pool is created successfully, the IP allocation is successful, and the query IP pool is empty.

- **Fixed** Subnet Management - Delete subnet, choose to delete a subnet, the system prompts success, but the subnet is still there after refreshing.

- **Fixed** Click "Container Network Card" several times, but can't get data.

- **Fixed** Spidernet-UI Service Label in `Spidernet Chart` is incorrect.

## 2022-11-30

### v0.4.3

#### Optimization

- **Optimize** resource usage, reduce CPU and memory requests.

### v0.4.2

#### Optimization

- **Optimize** resource usage, reduce CPU and memory requests.
- **Optimization** Subnet or IPPool cannot be deleted when IP is occupied.
- **Optimize** pagination issue

### v0.4.1

#### Features

- **Added** Added functions such as interface-based IP reservation and IP release reservation.

- **Added** IP pool management, which can be created, edited, and deleted based on the interface.

- **Added** The workload uses the multi-NIC function of the container, and the IP pool can be selected and fixed.

- **Added** Check the number of available IPs/total IPs in the application fixed IP pool.

#### Optimization

- **Optimize** resource usage, reduce CPU and memory requests.