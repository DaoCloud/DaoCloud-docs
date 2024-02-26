---
hide:
   - toc
---

# Resource Usage for Different Mesh Scales

Different service meshes require different resource usage for their components. Here is a detailed introduction to the resource usage of each component under different mesh scales (which can be manually adjusted by default).

## Small Scale Mesh

| Component                   | Memory Request | Memory Limit | CPU Request | CPU Limit |
| --------------------------- | -------------- | ------------ | ----------- | --------- |
| mcpc-controller             | 50Mi           | 1600Mi       | 100m        | 300m      |
| reg-proxy                   | 50Mi           | 300Mi        | 100m        | 300m      |
| ckube-remote                | 50Mi           | 500Mi        | 100m        | 500m      |
| hosted-apiserver.etcd       | 100Mi          | 1000Mi       | 100m        | 500m      |
| hosted-apiserver.apiserver  | 100Mi          | 1000Mi       | 100m        | 1000m     |
| istiod                      | 200Mi          | 1500Mi       | 200m        | 1500m     |
| gateway                     | 50Mi           | 900Mi        | 50m         | 1000m     |

## Medium Scale Mesh

| Component                   | Memory Request | Memory Limit | CPU Request | CPU Limit |
| --------------------------- | -------------- | ------------ | ----------- | --------- |
| mcpc-controller             | 200Mi          | 1600Mi       | 100m        | 600m      |
| reg-proxy                   | 100Mi          | 600Mi        | 100m        | 500m      |
| ckube-remote                | 200Mi          | 1000Mi       | 200m        | 1000m     |
| hosted-apiserver.etcd       | 200Mi          | 1000Mi       | 100m        | 500m      |
| hosted-apiserver.apiserver  | 200Mi          | 1000Mi       | 100m        | 1000m     |
| istiod                      | 500Mi          | 2000Mi       | 400m        | 2000m     |
| gateway                     | 150Mi          | 1500Mi       | 300m        | 2000m     |

## Large Scale Mesh

| Component                   | Memory Request | Memory Limit | CPU Request | CPU Limit |
| --------------------------- | -------------- | ------------ | ----------- | --------- |
| mcpc-controller             | 300Mi          | 1000Mi       | 300m        | 1000m     |
| reg-proxy                   | 200Mi          | 1000Mi       | 100m        | 1000m     |
| ckube-remote                | 400Mi          | 2000Mi       | 200m        | 1500m      |
| hosted-apiserver.etcd       | 300Mi          | 1500Mi       | 100m        | 500m      |
| hosted-apiserver.apiserver  | 300Mi          | 1500Mi       | 400m        | 2000m     |
| istiod                      | 800Mi          | 3000Mi       | 600m        | 3000m     |
| gateway                     | 500Mi          | 2000Mi       | 600m        | 3000m     |
