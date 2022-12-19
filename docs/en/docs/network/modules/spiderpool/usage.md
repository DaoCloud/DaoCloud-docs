---
hide:
  - toc
---

# use

This page explains how to use IP Pool (IPPool).

1. Create an IPv4 IP pool.

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

2. Use the Pod annotation `ipam.spidernet.io/ippool` to choose to allocate IP from the IP pool `standard-ipv4-ippool`, and create this Deployment.

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

3. Pods controlled by the Deployment `standard-ippool-deploy` are assigned IP addresses from the IP pool `standard-ipv4-ippool` and run successfully.

    ```bash
    kubectl get se
    NAME INTERFACE IPV4POOL IPV4 IPV6POOL IPV6 NODE CREATETION TIME
    standard-ippool-deploy-6967dcd8df-8b6zp eth0 standard-ipv4-ippool 172.18.41.47/24 spider-worker 7s
    standard-ippool-deploy-6967dcd8df-cvq79 eth0 standard-ipv4-ippool 172.18.41.50/24 spider-worker 7s
    standard-ippool-deploy-6967dcd8df-s58x9 eth0 standard-ipv4-ippool 172.18.41.41/24 spider-worker 7s
    ```