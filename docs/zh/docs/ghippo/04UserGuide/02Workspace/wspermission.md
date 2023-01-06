# 工作空间权限说明

工作空间具有权限映射和资源隔离能力，能够将用户/用户组在工作空间的权限映射到其下的资源上。
若用户/用户组在工作空间是 Workspace Admin 角色，同时工作空间-资源组中绑定了资源 Namespace，则映射后该用户/用户组将成为 Namespace Admin。

!!! note

    工作空间的权限映射能力不会作用到共享资源上，因为共享是将集群的使用权限共享给多个工作空间，而不是将管理权限受让给工作空间，因此不会实现权限继承和角色映射。

## 应用场景

通过将资源绑定到不同的工作空间能够实现资源隔离。
因此借助权限映射、资源隔离和共享资源能力能够将资源灵活分配给各个工作空间（租户）。

通常适用于以下两个场景：

- 集群一对一

    | 普通集群 | 部门/租户（工作空间） | 用途       |
    | -------- | ---------------- | -------- |
    | 集群 01  | A                | 管理和使用 |
    | 集群 02  | B                | 管理和使用 |

- 集群一对多

    | 集群    | 部门/租户（工作空间） | 资源限额   |
    | ------- | ---------------- | ---------- |
    | 集群 01 | A                | 100 核 CPU |
    |         | B                | 50 核 CPU  |

## 权限说明

| 操作对象 | 操作              | Workspace Admin | Workspace Editor | Workspace Viewer |
| :------- | :---------------- | :-------------- | :--------------- | :--------------- |
| 本身     | 查看              | &check;         | &check;          | &check;          |
| -        | 授权              | &check;         | &cross;          | &cross;          |
| -        | 修改别名          | &check;         | &check;          | &cross;          |
| 资源组   | 查看              | &check;         | &check;          | &check;          |
| -        | 资源绑定          | &check;         | &cross;          | &cross;          |
| -        | 解除绑定          | &check;         | &cross;          | &cross;          |
| 共享资源 | 查看              | &check;         | &check;          | &check;          |
| -        | 新增共享          | &check;         | &cross;          | &cross;          |
| -        | 解除共享          | &check;         | &cross;          | &cross;          |
| -        | 资源限额          | &check;         | &cross;          | &cross;          |
| -        | 使用共享资源 [^1] | &check;         | &cross;          | &cross;          |

[^1]:
    授权用户可前往应用工作台、微服务引擎、中间件、多云编排、服务网格等模块使用工作空间中的资源。
    有关 Workspace Admin、Workspace Editor、Workspace Viewer 角色在各产品模块的操作范围，请查阅各模块的权限说明：

    - [应用工作台权限说明](../../permissions/amamba.md)
    - [服务网格权限说明](../../permissions/mspider.md)
    - [中间件权限说明](../../permissions/mcamel.md)
    - [微服务引擎权限说明](../../permissions/skoala.md)
    - [容器管理权限说明](../../../kpanda/07UserGuide/Permissions/PermissionBrief.md)
