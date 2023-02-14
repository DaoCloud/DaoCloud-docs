---
hide:
  - toc
---

# Benefits

## Hwameistor cloud-native local storage

**IO localization**

100% local throughput, no network overhead, Pod starts on the replica node when the node fails, and uses the replica data volume for local IO read and write.

**High Performance, High Availability**

- 100% IO localization to achieve high-performance local throughput
- 2 copies of data volume redundant backup to ensure high availability of data

**Linear expansion**

- Independent node unit, minimum 1 node, unlimited number of extensions
- Separation of control plane and data plane, node expansion, does not affect business application data I/O

**Small CPU and memory overhead**

IO localization, the same IO read and write, CPU is stable, no large fluctuations, memory resource overhead is small

**Production can be operated and maintained**

- Support node, disk, data volume group (VG) dimension migration
- Support operation and maintenance behaviors such as disk replacement