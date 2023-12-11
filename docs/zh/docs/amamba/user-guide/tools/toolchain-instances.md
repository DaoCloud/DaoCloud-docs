# 管理工具链实例

对集成进来的工具链进行管理，分为两种：工作空间集成的工具链、管理员集成的工具链

## 解除集成

### 工作空间

对于 **工作空间分配** 的工具链实例，支持 **解除集成** 操作：

![tool04](https://docs.daocloud.io/daocloud-docs-images/docs/amamba/images/tool04.png)

对于 **平台分配** 的工具链实例，不支持 **解除集成** 操作：

### 管理员

解除集成后，分配给工作空间下的实例也会自动被删除。

## 分配项目

### 工作空间

对于 **工作空间分配** 的工具链实例，支持 **绑定** 实例下的项目到当前工作空间下并进行使用。

另外已绑定的项目支持解除绑定。

![tool05](https://docs.daocloud.io/daocloud-docs-images/docs/amamba/images/tool05.png)

对于 **平台分配** 的工具链实例，仅支持查看，不支持 **绑定** 操作。

### 管理员

支持 **分配项目** 到工作空间，分配成功后，会在工作空间下生成一条实例，并且项目可以被该工作空间使用。

![tool06](https://docs.daocloud.io/daocloud-docs-images/docs/amamba/images/tool06.png)
