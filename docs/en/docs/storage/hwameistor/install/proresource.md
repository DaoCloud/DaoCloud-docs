---
hide:
   - toc
---

# Production environment resource requirements

If you deploy Hwameistor in a production environment, please specify the resource configuration and avoid deploying it on the Master node. Therefore, some recommended values are provided in the `values.extra.prod.yaml` file. The resource configuration is as follows:

??? note "Click to view values.extra.prod.yaml"

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

1. If it is created through Helm, it can be created in the following way:

    ```console
    helm install hwameistor ./hwameistor \
        -n hwameistor --create-namespace \
        -f ./hwameistor/values.yaml \
        -f ./hwameistor/values.extra.prod.yaml
    ```

2. If installing through the UI interface, please manually configure the above resources
   through the Resource value in YAML, otherwise it will not be configured by default:

