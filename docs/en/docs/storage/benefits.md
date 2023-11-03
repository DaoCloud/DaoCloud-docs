---
hide:
  - toc
---

# Benefits

## Hwameistor Cloud-Native Local Storage

**IO Localization**

Hwameistor cloud native local storage ensures 100% local throughput, with no network overhead. In case of node failure, the Pod starts on the replica node and uses the replica data volume for local IO read and write.

**High Performance, High Availability**

- Achieve high-performance local throughput through 100% IO localization
- Ensure high data availability through two copies of data volume redundant backup

**Linear Expansion**

- Independent node unit, with a minimum of one node and an unlimited number of extensions
- Separation of control plane and data plane, node expansion does not affect business application data I/O

**Small CPU and Memory Overhead**

Hwameistor cloud native local storage ensures that CPU is stable with no large fluctuations in the same IO read and write, while memory resource overhead is minimal due to IO localization.

**Operational Manageability**

- Supports node, disk, and data volume group (VG) migration.
- Supports operation and maintenance behaviors such as disk replacement.
