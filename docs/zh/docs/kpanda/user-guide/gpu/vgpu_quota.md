# GPU 配额管理

本节介绍如何在 DCE 5.0 平台使用 vGPU 能力。

## 前提条件

当前集群已通过 Operator 或手动方式部署对应类型 GPU 驱动（NVIDIA GPU、NVIDIA MIG、天数、昇腾）

## 操作步骤

1. 进入 Namespaces 中，点击配额管理可以配置当个 Namespace 可以使用的 GPU 资源。

    ![Alt text](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/kpanda/user-guide/gpu/images/cluster-ns.png)

2. 当前命名空间配额管理覆盖的卡类型为：NVIDIA vGPU、NVIDIA MIG、天数、昇腾。

    - **NVIDIA vGPU 配额管理**：配置具体可以使用的配额，会创建 ResourcesQuota CR：

        - 物理卡数量（nvidia.com/vgpu）：表示当前 POD 需要挂载几张物理卡，并且要 **小于等于** 宿主机上的卡数量。
        - GPU 算力（nvidia.com/gpucores）: 表示每张卡占用的 GPU 算力，值范围为 0-100；如果配置为 0，则认为不强制隔离；配置为 100，则认为独占整张卡。
        - GPU 显存（nvidia.com/gpumem）: 表示每张卡占用的 GPU 显存，值单位为 MB，最小值为 1，最大值为整卡的显存值。

    ![Alt text](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/kpanda/user-guide/gpu/images/vgpu-quota.png)
