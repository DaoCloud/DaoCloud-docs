---
hide:
  - toc
---

# 网格规模对应资源用量说明

对于不同的服务网格规模，所需要的组件资源不尽相同，此处详细介绍在各个网格规模下，各个组件的资源用量（默认可以手动调整）。

## 小型网格

| 组件                       | 内存请求 | 内存限制 | CPU 请求 | CPU 限制 |
| -------------------------- | -------- | -------- | -------- | -------- |
| mcpc-controller            | 50Mi     | 1600Mi   | 100m     | 300m     |
| reg-proxy                  | 50Mi     | 300Mi    | 100m     | 300m     |
| ckube-remote               | 50Mi     | 500Mi    | 100m     | 500m     |
| hosted-apiserver.etcd      | 100Mi    | 1000Mi   | 100m     | 500m     |
| hosted-apiserver.apiserver | 100Mi    | 1000Mi   | 100m     | 1000m    |
| istiod                     | 200Mi    | 1500Mi   | 200m     | 1500m    |
| gateway                    | 50Mi     | 900Mi    | 50m      | 1000m    |

## 中型网格

| 组件                       | 内存请求 | 内存限制 | CPU 请求 | CPU 限制 |
| -------------------------- | -------- | -------- | -------- | -------- |
| mcpc-controller            | 200Mi    | 1600Mi   | 100m     | 600m     |
| reg-proxy                  | 100Mi    | 600Mi    | 100m     | 500m     |
| ckube-remote               | 200Mi    | 1000Mi   | 200m     | 1000m    |
| hosted-apiserver.etcd      | 200Mi    | 1000Mi   | 100m     | 500m     |
| hosted-apiserver.apiserver | 200Mi    | 1000Mi   | 100m     | 1000m    |
| istiod                     | 500Mi    | 2000Mi   | 400m     | 2000m    |
| gateway                    | 150Mi    | 1500Mi   | 300m     | 2000m    |

## 大型网格

| 组件                       | 内存请求 | 内存限制 | CPU 请求 | CPU 限制 |
| -------------------------- | -------- | -------- | -------- | -------- |
| mcpc-controller            | 300Mi    | 1000Mi   | 300m     | 1000m    |
| reg-proxy                  | 200Mi    | 1000Mi   | 100m     | 1000m    |
| ckube-remote               | 400Mi    | 2000Mi   | 200m     | 500m     |
| hosted-apiserver.etcd      | 300Mi    | 1500Mi   | 100m     | 500m     |
| hosted-apiserver.apiserver | 300Mi    | 1500Mi   | 400m     | 2000m    |
| istiod                     | 800Mi    | 3000Mi   | 600m     | 3000m    |
| gateway                    | 500Mi    | 2000Mi   | 600m     | 3000m    |
