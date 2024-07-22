# RDMA Usage Comparison

*[VF]: Virtual Function, a lightweight PCIe function on a network adapter that supports single root I/O virtualization (SR-IOV)

This section compares RDMA network usage across various CNIs (Container Network Interfaces).

| Functionality Comparison | Passthrough via MACVLAN/IPVLAN + RoCE | Passthrough via SRIOV + RoCE | Passthrough via SRIOV + InfiniBand |
| ------------------ | ----------------------------- | ---------------------- | -------------------------- |
| Performance | Good | Very Good | Best |
| Number of pods supported per node | Unlimited | Number of split Virtual Functions on a restricted SmartNIC | Number of split Virtual Functions on a restricted SmartNIC |
| Switch | Ethernet Switch | Ethernet Switch | InfiniBand Switch |
| Cost | Low | Medium | High |
| Stability | Good | Very Good | Best |
| Bandwidth Isolation | Fair | Good | Good |
