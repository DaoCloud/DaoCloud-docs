# VXLAN Performance

`EgressGateway` utilizes VXLAN tunnels, which typically introduce an approximate **10% performance loss**. If you observe that `EgressGateway` performance is below expectations, follow these steps for troubleshooting:

## 1. Verify Node-to-Node Throughput

The network speed between **host nodes** should be as expected. VXLAN performance depends on the host NIC offload settings.

- **NIC Offloading**: The offload settings of the host network interface impact VXLAN performance slightly (in **10G** network tests, the difference is about **0.5 Gbits/sec**).
- **Enable Offloading**: Run the following command on the host to enable offloading:

    ```bash
    ethtool --offload <host-interface-name> rx on tx on
    ```

## 2. Verify VXLAN Offload Settings

VXLAN interface offload settings can significantly impact performance.

- In **10G network tests**, VXLAN throughput was:
  - **Without checksum offload**: **2.5 Gbits/sec**
  - **With checksum offload**: **8.9 Gbits/sec**
- Check VXLAN checksum offload status with:

    ```bash
    ethtool -k egress.vxlan
    ```

- If offload is **disabled**, enable it by setting the following **Helm values**:

    ```yaml
    feature:
      vxlan:
        disableChecksumOffload: false
    ```

## Performance Benchmark

### Physical Server Benchmark

**Test Environment:**

| Name        | CPU                                       | Memory | Network Interface |
|------------|------------------------------------------|--------|------------------|
| **Node 1** | Intel(R) Xeon(R) E5-2680 v4 @ 2.40GHz | 128GB  | 10G Mellanox    |
| **Node 2** | Intel(R) Xeon(R) E5-2680 v4 @ 2.40GHz | 128GB  | 10G Mellanox    |
| **Target** | Intel(R) Xeon(R) E5-2680 v4 @ 2.40GHz | 128GB  | 10G Mellanox    |

| **Test Case** | **Scenario**                 | **Throughput**                                 |
|--------------|-----------------------------|----------------------------------------------|
| **Case 1**   | Node → Node                  | **9.44 Gbits/sec** (send) - **9.41 Gbits/sec** (receive) |
| **Case 2**   | Egress VXLAN → Egress VXLAN | **9.11 Gbits/sec** (send) - **9.09 Gbits/sec** (receive) |
| **Case 3**   | Pod → Egress Node → Target  | **9.01 Gbits/sec** (send) - **8.98 Gbits/sec** (receive) |

![egress-check](../../images/speed.svg)

### Virtual Machine Benchmark (VMware)

**Test Environment:**

- **VMware virtual machines** with **4 vCPUs** and **8GB RAM**

| Name        | CPU                                         | Memory | Network Interface |
|------------|--------------------------------------------|--------|------------------|
| **Node 1** | Intel(R) Xeon(R) Gold 5118 @ 2.30GHz (4C) | 8GB    | VMXNET3         |
| **Node 2** | Intel(R) Xeon(R) Gold 5118 @ 2.30GHz (4C) | 8GB    | VMXNET3         |
| **Target** | Intel(R) Xeon(R) Gold 5118 @ 2.30GHz (4C) | 8GB    | VMXNET3         |

| **Test Case** | **Scenario**                 | **Throughput**                                 |
|--------------|-----------------------------|----------------------------------------------|
| **Case 1**   | Node → Node                  | **2.99 Gbits/sec** (send) - **2.99 Gbits/sec** (receive) |
| **Case 2**   | Egress VXLAN → Egress VXLAN | **1.73 Gbits/sec** (send) - **1.71 Gbits/sec** (receive) |
| **Case 3**   | Pod → Egress Node → Target  | **1.23 Gbits/sec** (send) - **1.22 Gbits/sec** (receive) |

### Key Observations

- **Physical servers** provide near **90%+ efficiency** even with VXLAN.
- **VMware VMs** show significant performance degradation in VXLAN due to **virtualization overhead**.
- Enabling **checksum offload** improves VXLAN performance significantly.

For best performance:

- **Ensure host NIC offload settings are optimized**
- **Enable VXLAN checksum offload** via Helm values
- **Use physical servers** where high throughput is required
