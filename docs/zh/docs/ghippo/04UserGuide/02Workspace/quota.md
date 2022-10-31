# 资源限额

共享资源并非意味着被共享者可以无限使用被共享的资源，Admin 角色用户或同时拥有 Kpanda Owner 和 Workspace Admin 角色的用户可以通过共享资源中的资源配额功能限制被共享人的最大使用额度。
若不限制，表示可以无限使用。一个资源（集群）可以被多个工作空间共享，一个工作空间也可以同时使用多个共享集群中的资源。

!!! tip

    共享资源和资源组中的集群资源均来自于[容器管理](../../../kpanda/03ProductBrief/WhatisKPanda.md)，但是集群绑定和共享给同一个共享空间将会产生两种截然不同的效果。

1. 绑定到资源组

    使工作空间里的用户/用户组具有该集群的全部管理和使用权限，Workspace Admin 将被映射为 Cluster Admin。
    Workspace Admin 角色用户能够进入容器管理模块管理该集群。
    资源组中的其他资源也有类似的权限映射关系，详情查看工作空间与各模块资源的映射关系。

    !!! note

        当前容器管理模块暂无 Cluster Editor 和 Cluster Viewer 角色，因此 Workspace Editor、Workspace Viewer 无法映射，无法进入容器管理模块。

2. 新增共享资源

    使工作空间里的用户/用户组具有该集群资源的使用权限，能够在资源配额范围内前往[应用工作台创建和使用命名空间（Namespace）](../../../amamba/03UserGuide/Namespace/namespace.md)。
    
    与资源组不同，将集群共享到工作空间，用户在工作空间的角色不会映射到资源身上，因此 Workspace Admin 不会被映射为 Cluster admin，无法进入容器管理模块。

## 限额内容

- CPU 请求（Core）
- CPU 限制（Core）
- 内存请求（MB）
- 内存限制（MB）
- 存储请求总量（GB）
- 存储卷声明（个）

## 限额规则

本节从 3 个场景说明如何配置限额。

### 命名空间（Namespace）创建场景

前提：该工作空间已新增了共享资源 sharedcluster-01，假设工作空间名称为 Workspace-01，操作者为 Workspace-01 Admin 角色。

- 在应用工作台的集群 sharedcluster-01 中创建命名空间（创建前需确认工作空间是否处于 Workspace-01）

- 若在共享资源中 sharedcluster-01 没有设置资源配额，则在应用工作台中创建命名空间可不设置资源配额。

- 若在共享资源中 sharedcluster-01 已经设置资源配额，并设置 CPU 请求 = 100 core，则在应用工作台中创建命名空间必须设置 CPU 请求 ≤ 100 core（其他配额可以不设置）。

### 命名空间（Namespace）绑定工作空间 Workspace-01 场景

前提：该工作空间已新增了共享资源 sharedcluster-01，假设工作空间名称为 Workspace-01，操作者为 Workspace-01 Admin + Kpanda Owner 角色或 Admin 角色。

1. 在容器管理中将 sharedcluster-01 下创建的命名空间 Namespace-01 绑定到 Workspace-01

    若在共享资源中 sharedcluster-01 没有设置资源配额，命名空间 Namespace-01 无论是否已设置资源配额，均可成功绑定。

    若在共享资源中 sharedcluster-01 已经设置资源配额，并设置 CPU 请求 = 100 core，则命名空间 Namespace-01 必须设置且满足 CPU 请求 ≤ 100 core（其他配额可以不设置）才能绑定成功。

2. 在全局管理中将 sharedcluster-01 下创建的命名空间 Namespace-01 绑定到 Workspace-01

    若在共享资源中 sharedcluster-01 没有设置资源配额，命名空间 Namespace-01 无论是否已设置资源配额，均可成功绑定。

    若在共享资源中 sharedcluster-01 已经设置资源配额，并设置 CPU 请求 = 100 core，则命名空间 Namespace-01 必须设置且满足 CPU 请求 ≤ 100 core（其他配额可以不设置）才能绑定成功。

### 命名空间（Namespace）解绑工作空间 Workspace-01 场景

1. 在容器管理中将 sharedcluster-01 下创建的 Namespace-01 从 Workspace-01 解绑

    若在共享资源中 sharedcluster-01 没有设置资源配额，命名空间 Namespace-01 无论是否已设置资源配额，解绑后均不会对资源配额产生影响。

    若在共享资源中 sharedcluster-01 已经设置资源配额，并设置 CPU 请求 = 100 core，命名空间 Namespace-01 也设置了资源配额，则解绑后 sharedcluster-01 将释放 Namespace-01 的资源额度。

2. 在全局管理中将 sharedcluster-01 下创建的 Namespace-01 从 Workspace-01 解绑

    若在共享资源中 sharedcluster-01 没有设置资源配额，命名空间 Namespace-01 无论是否已设置资源配额，解绑后均不会对资源配额产生影响。

    若在共享资源中 sharedcluster-01 已经设置资源配额，并设置 CPU 请求 = 100 core，命名空间 Namespace-01 也设置了资源配额，则解绑后 sharedcluster-01 将释放 Namespace-01 的资源额度。
