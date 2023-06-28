---
hide:
  - toc
---

# 生产环境资源要求

如果在生产环境中部署 Hwameistor，请指定资源配置，并且避免部署到 Master 节点上，因此 `values.extra.prod.yaml` 文件中提供了一些推荐值，资源配置如下：

??? note "点击查看 values.extra.prod.yaml"

    ```yaml title="values.extra.prod.yaml"
    scheduler:
      replicas: 3
      resources:
        limits:
          cpu: 300m
          memory: 300Mi
        requests:
          cpu: 1m
          memory: 20Mi
    
    admission:
      replicas: 3
      resources:
        limits:
          cpu: 300m
          memory: 300Mi
        requests:
          cpu: 1m
          memory: 20Mi
    
    evictor:
      replicas: 2
      resources:
        limits:
          cpu: 300m
          memory: 300Mi
        requests:
          cpu: 1m
          memory: 20Mi
    
    metrics:
      replicas: 2
      resources:
        limits:
          cpu: 300m
          memory: 300Mi
        requests:
          cpu: 1m
          memory: 20Mi
    
    apiserver:
      replicas: 2
      resources:
        limits:
          cpu: 300m
          memory: 300Mi
        requests:
          cpu: 1m
          memory: 20Mi
    
    localDiskManager:
      tolerationsOnMaster: false
      registrar:
        resources:
          limits:
            cpu: 500m
            memory: 500Mi
          requests:
            cpu: 1m
            memory: 20Mi
      manager:
        resources:
          limits:
            cpu: 300m
            memory: 300Mi
          requests:
            cpu: 1m
            memory: 20Mi
    
    localDiskManagerCSIController:
      replicas: 3
      priorityClassName: system-node-critical
      provisioner:
        resources:
          limits:
            cpu: 500m
            memory: 500Mi
          requests:
            cpu: 1m
            memory: 20Mi
      attacher:
        resources:
          limits:
            cpu: 500m
            memory: 500Mi
          requests:
            cpu: 1m
            memory: 20Mi
    
    localStorage:
      tolerationsOnMaster: false
      priorityClassName: system-node-critical
      registrar:
        resources:
          limits:
            cpu: 500m
            memory: 500Mi
          requests:
            cpu: 1m
            memory: 20Mi
      member:
        resources:
          limits:
            cpu: 500m
            memory: 500Mi
          requests:
            cpu: 1m
            memory: 20Mi
    
    localStorageCSIController:
      replicas: 3
      priorityClassName: system-node-critical
      provisioner:
        resources:
          limits:
            cpu: 500m
            memory: 500Mi
          requests:
            cpu: 1m
            memory: 20Mi
      attacher:
        resources:
          limits:
            cpu: 500m
            memory: 500Mi
          requests:
            cpu: 1m
            memory: 20Mi
      resizer:
        resources:
          limits:
            cpu: 500m
            memory: 500Mi
          requests:
            cpu: 1m
            memory: 20Mi
    ```

1. 如通过 Helm 创建时可通过如下方式修改资源：

    ```console
    helm install hwameistor ./hwameistor \
        -n hwameistor --create-namespace \
        -f ./hwameistor/values.yaml \
        -f ./hwameistor/values.extra.prod.yaml
    ```

2. 如通过 UI 界面安装，请手动将如上资源通过 YAML 中的 Resource 值进行配置，否则默认不配置：

    ![pro-Resource](https://docs.daocloud.io/daocloud-docs-images/docs/storage/images/hwameistor-resource.jpg)
