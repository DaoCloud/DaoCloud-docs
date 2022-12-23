---
hide:
  - toc
---

# Functions supported by the UI interface

The DCE service mesh supports three types of meshs: hosted mesh, dedicated mesh, and external mesh.
On the UI interface, the functions supported by these three meshs are as follows.

**mesh Management**

| Subclasses | Managed meshs | Proprietary meshs | External meshs |
| :--: | :------: | :------: | :------: |
| Create | √ | √ | √ |
| Configuration | √ | √ | √ |
| Delete | √ | √ | √ |

**mesh Overview**

| Subclasses | Managed meshs | Proprietary meshs | External meshs |
| :------: | :------: | :------: | :------: |
| mesh Overview | √ | √ | √ |

**Cluster Management**

| Subclasses | Managed meshs | Proprietary meshs | External meshs |
| :--: | :------: | :------: | :------: |
| Access | √ | × | × |
| Remove | √ | × | × |

**Service Management**

| Subclasses | Managed meshs | Proprietary meshs | External meshs |
| :------------------: | :------: | :------: | :------: |
| Service List | √ | √ | √ |
| Service Details | √ | √ | √ |
| Service Editor | √ | √ | √ |
| Service entry (addition, deletion, modification and query) | √ | √ | √ |

**Traffic management**

| Subclasses | Managed meshs | Proprietary meshs | External meshs |
| :------------------: | :------: | :------: | :------: |
| Virtual service (add, delete, modify, check) | √ | √ | √ |
| Target rules (add, delete, modify, check) | √ | √ | √ |
| Gateway rules (add, delete, modify, check) | √ | √ | √ |

**Security Governance**

| Subclasses | Managed meshs | Proprietary meshs | External meshs |
| ------------------------ | -------- | -------- | ------ -- |
| Peer-to-peer identity authentication (addition, deletion, modification and query) | √ | √ | √ |
| Request identity authentication (addition, deletion, modification and query) | √ | √ | √ |
| Authorization policy (addition, deletion, modification and query) | √ | √ | √ |

**data monitoring**

| Subclasses | Managed meshs | Proprietary meshs | External meshs |
| :--: | :------: | :------: | :------: |
| Topology | √ | √ | √ |
| Chart | √ | √ | √ |

**Sidecar Management**

| Subclasses | Managed meshs | Proprietary meshs | External meshs |
| :------: | :------: | :------: | :------: |
| Injection | √ | √ | √ |
| Uninstall | √ | √ | √ |
| Resource Limit | √ | √ | × |

**mesh Gateway**

| Subclasses | Managed meshs | Proprietary meshs | External meshs |
| :--: | :------: | :------: | :------: |
| Create | √ | √ | × |
| Delete | √ | √ | × |
| Settings | √ | √ | × |

**Istio Resource Management**

| Subclasses | Managed meshs | Proprietary meshs | External meshs |
| :--: | :------: | :------: | :------: |
| Create | √ | √ | √ |
| Edit | √ | √ | √ |
| Delete | √ | √ | √ |