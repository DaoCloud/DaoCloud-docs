# 文件夹权限说明

文件夹具有权限映射能力，能够将用户/用户组在本文件夹的权限映射到其下的子文件夹、工作空间以及资源上。

若用户/用户组在本文件夹是 Folder Admin 角色，映射到子文件夹仍为 Folder Admin 角色，映射到其下的工作空间则为 Workspace Admin；
若在 __工作空间与层级__ -> __资源组__ 中绑定了 Namespace，则映射后该用户/用户组同时还是 Namespace Admin。

!!! note

    文件夹的权限映射能力不会作用到共享资源上，因为共享是将集群的使用权限共享给多个工作空间，而不是将管理权限受让给工作空间，因此不会实现权限继承和角色映射。

## 应用场景

文件夹具有层级能力，因此将文件夹对应于企业中的部门/供应商/项目等层级时，

- 若用户/用户组在一级部门具有管理权限（Admin），其下的二级、三级、四级部门或项目同样具有管理权限；
- 若用户/用户组在一级部门具有使用权限（Editor），其下的二级、三级、四级部门或项目同样具有使用权限；
- 若用户/用户组在一级部门具有只读权限（Viewer），其下的二级、三级、四级部门或项目同样具有只读权限。

| 对象                        | 操作     | Folder Admin | Folder Editor | Folder Viewer |
| --------------------------- | -------- | ------------ | ------------- | ------------- |
| 对文件夹本身                | 查看     | &check;            | &check;             | &check;             |
|                             | 授权     | &check;            | &cross;             | &cross;             |
|                             | 修改别名 | &check;            | &check;             | &cross;             |
| 对子文件夹                  | 创建     | &check;            | &cross;             | &cross;             |
|                             | 查看     | &check;            | &check;             | &check;             |
|                             | 授权     | &check;            | &cross;             | &cross;             |
|                             | 修改别名 | &check;            | &check;             | &cross;             |
| 对其下的工作空间            | 创建     | &check;            | &cross;             | &cross;             |
|                             | 查看     | &check;            | &check;             | &check;             |
|                             | 授权     | &check;            | &cross;             | &cross;             |
|                             | 修改别名 | &check;            | &check;             | &cross;             |
| 对其下的工作空间 - 资源组   | 查看     | &check;            | &check;             | &check;             |
|                             | 资源绑定 | &check;            | &cross;             | &cross;             |
|                             | 解除绑定 | &check;            | &cross;             | &cross;             |
| 对其下的工作空间 - 共享资源 | 查看     | &check;            | &check;             | &check;             |
|                             | 新增共享 | &check;            | &cross;             | &cross;             |
|                             | 解除共享 | &check;            | &cross;             | &cross;             |
|                             | 资源限额 | &check;            | &cross;             | &cross;             |
