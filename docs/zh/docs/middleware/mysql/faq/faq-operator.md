# MySQL Operator

## 未指定 __storageClass__ 

由于没有指定 __storageClass__ ，导致 __mysql-operator__ 无法获取 PVC 而处于 __pending__ 状态。

如果采用 Helm 启动，可以做如下设置：

1. 关闭 PVC 的申请

    ```console
    orchestrator.persistence.enabled=false 
    ```

2. 指定 storageClass 去获取 PVC

    ```console
    orchestrator.persistence.storageClass={storageClassName} 
    ```

如果使用其他工具，可以修改 __value.yaml__ 内对应字段，即可达到和 Helm 启动一样的效果。
