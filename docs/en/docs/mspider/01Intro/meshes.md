---
hide:
  - toc
---

# Functions supported by the UI interface

The DCE service grid supports three types of grids: hosted grid, dedicated grid, and external grid.
On the UI interface, the functions supported by these three grids are as follows.

**Grid Management**

| Subclasses | Managed Grids | Proprietary Grids | External Grids |
| :--: | :------: | :------: | :------: |
| Create | √ | √ | √ |
| Configuration | √ | √ | √ |
| Delete | √ | √ | √ |

**Grid Overview**

| Subclasses | Managed Grids | Proprietary Grids | External Grids |
| :------: | :------: | :------: | :------: |
| Grid Overview | √ | √ | √ |

**Cluster Management**

| Subclasses | Managed Grids | Proprietary Grids | External Grids |
| :--: | :------: | :------: | :------: |
| Access | √ | × | × |
| Remove | √ | × | × |

**Service Management**

| Subclasses | Managed Grids | Proprietary Grids | External Grids |
| :------------------: | :------: | :------: | :------: |
| Service List | √ | √ | √ |
| Service Details | √ | √ | √ |
| Service Editor | √ | √ | √ |
| Service entry (addition, deletion, modification and query) | √ | √ | √ |

**Traffic management**

| Subclasses | Managed Grids | Proprietary Grids | External Grids |
| :------------------: | :------: | :------: | :------: |
| Virtual service (add, delete, modify, check) | √ | √ | √ |
| Target rules (add, delete, modify, check) | √ | √ | √ |
| Gateway rules (add, delete, modify, check) | √ | √ | √ |

**Security Governance**

| Subclasses | Managed Grids | Proprietary Grids | External Grids |
| ------------------------ | -------- | -------- | ------ -- |
| Peer-to-peer identity authentication (addition, deletion, modification and query) | √ | √ | √ |
| Request identity authentication (addition, deletion, modification and query) | √ | √ | √ |
| Authorization policy (addition, deletion, modification and query) | √ | √ | √ |

**data monitoring**

| Subclasses | Managed Grids | Proprietary Grids | External Grids |
| :--: | :------: | :------: | :------: |
| Topology | √ | √ | √ |
| Chart | √ | √ | √ |

**Sidecar Management**

| Subclasses | Managed Grids | Proprietary Grids | External Grids |
| :------: | :------: | :------: | :------: |
| Injection | √ | √ | √ |
| Uninstall | √ | √ | √ |
| Resource Limit | √ | √ | × |

**Grid Gateway**

| Subclasses | Managed Grids | Proprietary Grids | External Grids |
| :--: | :------: | :------: | :------: |
| Create | √ | √ | × |
| Delete | √ | √ | × |
| Settings | √ | √ | × |

**Istio Resource Management**

| Subclasses | Managed Grids | Proprietary Grids | External Grids |
| :--: | :------: | :------: | :------: |
| Create | √ | √ | √ |
| Edit | √ | √ | √ |
| Delete | √ | √ | √ |