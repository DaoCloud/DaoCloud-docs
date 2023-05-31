---
hide:
   - toc
---

# Description of resource usage corresponding to mesh scale

For different service mesh scales, the required component resources are different. Here is a detailed introduction to the resource usage of each component under each mesh scale (by default, it can be manually adjusted).

## small mesh

| Components | Memory Requests | Memory Limits | CPU Requests | CPU Limits |
| -------------------------- | -------- | -------- | ---- ---- | -------- |
| mcpc-controller | 50Mi | 1600Mi | 100m | 300m |
| reg-proxy | 50Mi | 300Mi | 100m | 300m |
| ckube-remote | 50Mi | 500Mi | 100m | 500m |
| hosted-apiserver.etcd | 100Mi | 1000Mi | 100m | 500m |
| hosted-apiserver.apiserver | 100Mi | 1000Mi | 100m | 1000m |
| istiod | 200Mi | 1500Mi | 200m | 1500m |
| gateway | 50Mi | 900Mi | 50m | 1000m |

## medium mesh

| Components | Memory Requests | Memory Limits | CPU Requests | CPU Limits |
| -------------------------- | -------- | -------- | ---- ---- | -------- |
| mcpc-controller | 200Mi | 1600Mi | 100m | 600m |
| reg-proxy | 100Mi | 600Mi | 100m | 500m |
| ckube-remote | 200Mi | 1000Mi | 200m | 1000m |
| hosted-apiserver.etcd | 200Mi | 1000Mi | 100m | 500m |
| hosted-apiserver.apiserver | 200Mi | 1000Mi | 100m | 1000m |
| istiod | 500Mi | 2000Mi | 400m | 2000m |
| gateway | 150Mi | 1500Mi | 300m | 2000m |

## large mesh

| Components | Memory Requests | Memory Limits | CPU Requests | CPU Limits |
| -------------------------- | -------- | -------- | ---- ---- | -------- |
| mcpc-controller | 300Mi | 2000Mi | 300m | 1000m |
| reg-proxy | 200Mi | 1000Mi | 100m | 1000m |
| ckube-remote | 400Mi | 2000Mi | 200m | 500m |
| hosted-apiserver.etcd | 300Mi | 1500Mi | 100m | 500m |
| hosted-apiserver.apiserver | 300Mi | 1500Mi | 400m | 2000m |
| istiod | 800Mi | 3000Mi | 600m | 3000m |
| gateway | 500Mi | 2000Mi | 600m | 3000m |