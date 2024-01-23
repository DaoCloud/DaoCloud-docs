# Ingress 性能测试报告

## 测试背景

验证 Ingress-nginx 水平扩容后吞吐量可以线性增长，了解其性能指标有助于用户合理管理资源。

## Benchmark

本文基于 DCE 5.0 安装 Ingress-Nginx，所有参数为默认配置，未开启 keepalive 等特性。

![ingress-arch](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/network/images/ingress-nginx-arch.png)

### 物理机

| Name        | CPU                                       |  CPU  | MEM  | Interface    |
|:------------|:------------------------------------------|:------|:-----|:-------------|
| Node 1      | Intel(R) Xeon(R) CPU E5-2680 v4 @ 2.40GHz |  56C  | 128G | 10G Mellanox |
| Node 2      | Intel(R) Xeon(R) CPU E5-2680 v4 @ 2.40GHz |  56C  | 128G | 10G Mellanox |
| wrk Client  | Intel(R) Xeon(R) CPU E5-2680 v4 @ 2.40GHz |  56C  | 128G | 10G Mellanox |

以下是我们使用物理服务器压测的数据。

| Ingress-nginx 的 CPU 数量 | （wrk）Requests/sec  |
| :----------------------: | :-----------------: |
|          1               |       3209.66       |
|          2               |       5709.07       |
|          4               |       9005.79       |
|          8               |       20696.19      |

#### Ingress-nginx CPU 与 RPS 关系图

![ingress-cpu-rps](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/network/images/ingress-cpu-rps.png)

### 虚拟机

| Name        | CPU                                       |  CPU  | MEM  |
|:------------|:------------------------------------------|:------|:-----|
| Node 1      | Intel(R) Xeon(R) Gold 5118 CPU @ 2.30GHz  |  16C  | 16G  |
| Node 2      | Intel(R) Xeon(R) Gold 5118 CPU @ 2.30GHz  |  16C  | 16G  |
| wrk Client  | Intel(R) Xeon(R) CPU E5-2680 v4 @ 2.40GHz |  56C  | 128G |

以下是我们使用虚拟服务器压测的数据。

| Ingress-nginx 的 CPU 数量 | （wrk）Requests/sec  |
| :----------------------: | :-----------------: |
|          1               |       3022.68       |
|          2               |       5556.20       |
|          4               |       8616.95       |
|          8               |       11006.89      |

#### 虚拟机 Ingress-nginx CPU 与 RPS 关系图

![vm-ingress-cpu-rps](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/network/images/ingress-vm-cpu-rps.png)
