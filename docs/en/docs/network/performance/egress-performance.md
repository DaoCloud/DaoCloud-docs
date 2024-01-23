# Egress Performance Test Report

EgressGateway uses a vxlan tunnel, and the test shows that the vxlan overhead is about 10%. If you find that the speed of EgressGateway is not up to standard, you can follow the steps below to check:

1. Make sure that the speed between the host nodes meets expectations.
    
    The offload settings of the host's network card used by vxlan will have a small impact on the speed of the vxlan interface (only a difference of 0.5 Gbits/sec in the test of a 10G network card). You can run `ethtool --offload host-interface-name rx on tx on` to enable offload.

2. The offload settings of the vxlan network card can have a greater impact on the speed of the vxlan interface (in the test of a 10G network card, 2.5 Gbits/sec without offload and 8.9 Gbits/sec with offload). You can run `ethtool -k egress.vxlan` to check if checksum offload is disabled, and enable offload by setting `feature.vxlan.disableChecksumOffload` to `false` in the helm values.

## Benchmark

### Physical Machine

The following data is obtained from load testing on physical servers.

| Name        | CPU                                       | MEM  | Interface    |
|:------------|:------------------------------------------|:-----|:-------------|
| Node 1      | Intel(R) Xeon(R) CPU E5-2680 v4 @ 2.40GHz | 128G | 10G Mellanox |
| Node 2      | Intel(R) Xeon(R) CPU E5-2680 v4 @ 2.40GHz | 128G | 10G Mellanox |
| Node Target | Intel(R) Xeon(R) CPU E5-2680 v4 @ 2.40GHz | 128G | 10G Mellanox |

| Case  | Item                         | Detail                                            |
|:------|:-----------------------------|:--------------------------------------------------|
| case1 | node -> node                 | `9.44 Gbits/sec sender - 9.41 Gbits/sec receiver` |
| case2 | egress vxlan -> egress vxlan | `9.11 Gbits/sec sender - 9.09 Gbits/sec receiver` |
| case3 | pod -> egress node -> target | `9.01 Gbits/sec sender - 8.98 Gbits/sec receiver` |

![egress-check](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/network/images/egressgateway/speed01.svg)

#### Virtual Machine

The following data is obtained from load testing on VMware virtual machines, with the Node restricted to 4C8G.

| Name        | CPU                                         | MEM | Interface |
|:------------|:--------------------------------------------|:----|:----------|
| Node 1      | Intel(R) Xeon(R) Gold 5118 CPU @ 2.30GHz 4C | 8G  | VMXNET3   |
| Node 2      | Intel(R) Xeon(R) Gold 5118 CPU @ 2.30GHz 4C | 8G  | VMXNET3   |
| Node Target | Intel(R) Xeon(R) Gold 5118 CPU @ 2.30GHz 4C | 8G  | VMXNET3   |

| Case  | Item                         | Detail                                            |
|:------|:-----------------------------|:--------------------------------------------------|
| case1 | node -> node                 | `2.99 Gbits/sec sender - 2.99 Gbits/sec receiver` |
| case2 | egress vxlan -> egress vxlan | `1.73 Gbits/sec sender - 1.71 Gbits/sec receiver` |
| case3 | pod -> egress node -> target | `1.23 Gbits/sec sender - 1.22 Gbits/sec receiver` |
