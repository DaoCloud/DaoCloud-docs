---
hide:
  - toc
---

# 使用

本页说明如何使用 IP 池（IPPool）。

1. 创建一个 IPv4 的 IP 池。

    ```yaml
    apiVersion: spiderpool.spidernet.io/v1
    kind: SpiderIPPool
    metadata:
      name: standard-ipv4-ippool
    spec:
      ipVersion: 4
      subnet: 172.18.41.0/24
      ips:
      - 172.18.41.40-172.18.41.50
    ```

2. 使用 Pod 注解 `ipam.spidernet.io/ippool` 选择从 IP 池 `standard-ipv4-ippool` 分配 IP，创建这个 Deployment。

    ```yaml
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: standard-ippool-deploy
    spec:
      replicas: 3
      selector:
        matchLabels:
          app: standard-ippool-deploy
      template:
        metadata:
          annotations:
            ipam.spidernet.io/ippool: |-
              {
                "ipv4": ["standard-ipv4-ippool"]
              }
          labels:
            app: standard-ippool-deploy
        spec:
          containers:
          - name: standard-ippool-deploy
            image: busybox
            imagePullPolicy: IfNotPresent
            command: ["/bin/sh", "-c", "trap : TERM INT; sleep infinity & wait"]
    ```

3. 由 Deployment `standard-ippool-deploy` 所控制的 Pod 均从 IP 池 `standard-ipv4-ippool` 分配 IP 地址且成功运行。

    ```bash
    kubectl get se
    NAME                                      INTERFACE   IPV4POOL               IPV4              IPV6POOL   IPV6   NODE            CREATETION TIME
    standard-ippool-deploy-6967dcd8df-8b6zp   eth0        standard-ipv4-ippool   172.18.41.47/24                     spider-worker   7s
    standard-ippool-deploy-6967dcd8df-cvq79   eth0        standard-ipv4-ippool   172.18.41.50/24                     spider-worker   7s
    standard-ippool-deploy-6967dcd8df-s58x9   eth0        standard-ipv4-ippool   172.18.41.41/24                     spider-worker   7s
    ```
