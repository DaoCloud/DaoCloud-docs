# Using RDMA in Workloads

This chapter mainly introduces how to configure and use RDMA resources in workloads.

!!! note

    This chapter is based on the example of using RoCE network cards with SR-IOV. To facilitate RDMA testing, the configured image should be `docker.io/mellanox/rping-test`, and the sh command should be run to prevent the Pod from exiting abnormally during the operation. Please refer to the following content for details.

## Prerequisites

- [SpiderPool has been successfully deployed](../modules/spiderpool/install/install.md)
- [RDMA installation and preparation have been completed](../modules/spiderpool/install/rdmapara.md)
- [Multus CR has been created](multus-cr.md)
- [IP Pool has been created](./ippool/createpool.md)

## UI Operations

1. Log in to the platform UI, click `Container Management` -> `Cluster List` in the left navigation bar, find the corresponding cluster. Then, select `Deployments` in the left navigation bar and click `Create Image`.

    ![Create Image](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/network/images/useippool01.png)

1. On the `Create Deployment` page, use the image `docker.io/mellanox/rping-test`. Set `Replica` to `2` to deploy a group of cross-node Pods.

1. Fill in the `Basic Information` and enter the following information in the `Container Configuration`.

    ![rdma_sriov](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/network/images/rdma_sriov01.jpg)

    - `Network Resource Parameters`:
      
        - When using RDMA based on Macvlan/VLAN CNI, the resource name is the custom name created in [RDMA Installation and Preparation](install/rdmapara.md) when creating Spiderpool. For more information, please refer to [Exposing RoCE Network Card based on Macvlan/IPVLAN](rdmapara.md/#exposing-roce-network-card-based-on-macvlan-ipvlan).

        - When using RDMA based on SRIOV CNI, the resource name is the `resourceName` defined in `SriovNetworkNodePolicy`. For more information, please refer to [Using RoCE Network Card based on SR-IOV](../modules/spiderpool/install/rdmapara.md#using-roce-network-card-based-on-sr-iov).

        The `spidernet.io/mellnoxrdma` in the example is an example of using RoCE network cards based on SR-IOV. The request and limit values are currently consistent, and the input value should not exceed the maximum available value.
        
    - `Run Command`: To prevent the Pod from starting and exiting abnormally, add the following run command:
    
        ```para
        - sh
        - -c
        - |
          ls -l /dev/infiniband /sys/class/net
          sleep 1000000
       ```
    
1. After completing the information input on the `Container Configuration` and `Service Configuration` pages, go to `Advanced Configuration` and click to configure `Container Network`.

    ![Container Network](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/network/images/useippool02.png)

1. Select the [created Multus CR](multus-cr.md), turn off the fixed IP pool creation function, select the [created IP Pool](ippool/createpool.md), and click `OK` to complete the creation.

    ![rdma_usage01](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/network/images/rdma_usage01.jpg)
