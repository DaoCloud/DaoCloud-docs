# RDMA Environment Preparation and Installation

This chapter mainly introduces the parameters and instructions for RDMA when installing Spiderpool. Currently, RDMA supports the following two usage modes:

- Based on Macvlan/IPVLAN CNI, using **RDMA Shared mode** to expose the RoCE network card on the host to the Pod. It is necessary to deploy the [Shared Device Plugin](https://github.com/Mellanox/k8s-rdma-shared-dev-plugin) to expose the RDMA network card resources and schedule Pods.

- Based on SR-IOV CNI, using **RDMA Exclusive mode** to expose the RoCE network card on the host to the Pod. The [RDMA CNI](https://github.com/k8snetworkplumbingwg/rdma-cni) needs to be used to achieve RDMA device isolation.

## Prerequisites

1. Please make sure that RDMA devices are available in the cluster environment.

2. Please make sure that the corresponding OFED driver is available in the cluster, in this example, we use the Mellanox ConnectX 5 network card with RoCE support. You can install the latest OFED driver according to the [NVIDIA official guide](https://developer.nvidia.com/networking/ethernet-software). You can use the following command to check the RDMA devices:

    ```sh
    rdma link show
    link mlx5_0/1 state ACTIVE physical_state LINK_UP netdev ens6f0np0
    link mlx5_1/1 state ACTIVE physical_state LINK_UP netdev ens6f1np1
    ```

    If you are using **SR-IOV CNI to isolate RDMA network cards**, please meet one of the following conditions:

    - The kernel version requires 5.3.0 or higher, and the RDMA module is loaded in the system. The **rdma-core** package provides the function of automatically loading the relevant modules at system startup.
    - Mellanox OFED requires version 4.7 or higher. In this case, it is not necessary to use a kernel version of 5.3.0 or higher.

## Exposing RoCE Network Card based on Macvlan/IPVLAN

1. When exposing the RoCE network card based on Macvlan/IPVLAN, you need to make sure that the RDMA subsystem on the host is working in **Shared mode**. Otherwise, please switch to **Shared mode**.

    ```sh
    # Check the RoCE network card mode
    rdma system
    netns shared copy-on-fork on

    # Switch to shared mode
    rdma system set netns shared
    ```

1. Confirm the information of the RDMA network card for subsequent device plugin discovery.

    Enter the following command to view the vendor of the network card, which is 15b3, and the deviceIDs, which is 1017. This information is required when deploying Spiderpool.

    ```sh
    $ lspci -nn | grep Ethernet
    af:00.0 Ethernet controller [0200]: Mellanox Technologies MT27800 Family [ConnectX-5] [15b3:1017]
    af:00.1 Ethernet controller [0200]: Mellanox Technologies MT27800 Family [ConnectX-5] [15b3:1017]
    ```

1. Install Spiderpool and configure the parameters related to the [Shared Device Plugin](https://github.com/Mellanox/k8s-rdma-shared-dev-plugin). Please refer to [Installing Spiderpool](install.md) for deployment details.

    | Parameter                                   | Value            | Description |
    | ------------------------------------------- | ---------------- | ----------- |
    | RdmaSharedDevicePlugin.install               | True             | Whether to enable **RdmaSharedDevicePlugin** |
    | rdmaSharedDevicePlugin.deviceConfig.resourceName | hca_shared_devices | Define the name of the Shared RDMA Device resource, which needs to be used when creating Workloads |
    | rdmaSharedDevicePlugin.deviceConfig.deviceIDs | 1017 | Device ID number, consistent with the information queried in the previous step |
    | rdmaSharedDevicePlugin.deviceConfig.vendors | 15b3 | Network card Vendors information, consistent with the information queried in the previous step |

    ![rdmamacvlan](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/network/images/rdma_macvlan01.jpg)

    After successful deployment, you can view the installed components.

    ![resource](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/network/images/rdma_macvlan02.jpg)

1. After the installation is complete, you can log in to the controller node to view the reported RDMA device resources.

    ```sh
    kubectl get no -o json | jq -r '[.items[] | {name:.metadata.name, allocable:.status.allocatable}]'
      [
        {
           "name": "10-20-1-10",
           "allocable": {
             "cpu": "40",
             "memory": "263518036Ki",
             "pods": "110",
             "spidernet.io/hca_shared_devices": "500", # Number of available hca_shared_devices
             ...
          }
        },
        ...
      ]
    ```

    If the reported resource count is 0, possible reasons are:

    - Please confirm that the **vendors** and **deviceID** in the Configmap **spiderpool-rdma-shared-device-plugin** match the actual ones.
    - Check the logs of **rdma-shared-device-plugin**. For network cards that support RDMA, if the following error is found in the log, you can try to run `apt-get install rdma-core` or `dnf install rdma-core` on the host to install rdma-core.

    ```console
    error creating new device: "missing RDMA device spec for device 0000:04:00.0, RDMA device \"issm\" not found"
    ```

1. If Spiderpool has been successfully deployed and the Device resources have been successfully discovered, please complete the following steps:

    - Complete the creation of Multus instances, refer to [Creating Multus CR](../../../config/multus-cr.md)
    - Complete the creation of IP Pool, refer to [Creating Subnets and IP Pool](../../../config/ippool/createpool.md)

1. After the creation is complete, you can use this resource pool to create workloads. Please refer to [Using RDMA in Workloads](../../../config/userdma.md) for details. For more usage methods, please refer to [Using IP Pool in Workloads](../../../config/use-ippool/usage.md).

## Using RoCE Network Card based on SR-IOV

1. When exposing the RoCE network card based on SR-IOV, you need to make sure that the RDMA subsystem on the host is working in **exclusive mode**. Otherwise, please switch to **exclusive mode**.

    ```sh
    # Switch to exclusive mode, invalid after restarting the host
    rdma system set netns exclusive

    # Persistently configure, please restart the machine after modification
    echo "options ib_core netns_mode=0" >> /etc/modprobe.d/ib_core.conf

    rdma system
    netns exclusive copy-on-fork on
    ```

1. Confirm that the network card has SR-IOV functionality and check the maximum number of VFs supported:

    ```sh
    cat /sys/class/net/ens6f0np0/device/sriov_totalvfs
    ```

    The output is similar to:

    ```output
    8
    ```

1. Confirm the information of the RDMA network card for subsequent Device Plugin discovery.

    In this demo environment, the network card **vendors** is 15b3, and the network card **deviceIDs** is 1017. These information will be used when creating **SriovNetworkNodePolicy** in the next step.

    ```sh
    lspci -nn | grep Ethernet
    ```

    The output is similar to:

    ```output
    04:00.0 Ethernet controller [0200]: Mellanox Technologies MT27800 Family [ConnectX-5] [15b3:1017]
    04:00.1 Ethernet controller [0200]: Mellanox Technologies MT27800 Family [ConnectX-5] [15b3:1017]
    ```

1. Install Spiderpool and enable RDMA CNI and SR-IOV CNI. Please refer to [Installing Spiderpool](install.md) for installation details.

    <table>
      <tr>
        <th>Parameter</th>
        <th>Value</th>
        <th>Description</th>
      </tr>
      <tr>
        <td>multus.multusCNI.defaultCniCRName</td>
        <td>sriov-rdma</td>
        <td>
          Default CNI name, specifies the name of the NetworkAttachmentDefinition instance used by multus by default.<br />
          <ul>
            <li>
              If the <code>multus.multusCNI.defaultCniCRName</code> option is not empty, an empty NetworkAttachmentDefinition corresponding instance will be automatically generated after installation.
            </li>
            <li>
              If the <code>multus.multusCNI.defaultCniCRName</code> option is empty, an attempt will be made to create a corresponding NetworkAttachmentDefinition instance based on the first CNI configuration in the <code>/etc/cni/net.d</code> directory. Otherwise, a NetworkAttachmentDefinition instance named <code>default</code> will be automatically generated to complete the installation of multus.
            </li>
          </ul>
        </td>
      </tr>
      <tr>
        <td>sriov.install</td>
        <td>true</td>
        <td>Enable SR-IOV CNI</td>
      </tr>
      <tr>
        <td>plugins.installRdmaCNI</td>
        <td>true</td>
        <td>Enable RDMA CNI</td>
      </tr>
    </table>

    ![sriov01](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/network/images/sriov01.jpg)

    ![sriov02](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/network/images/sriov02.jpg)

    ![sriov03](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/network/images/sriov03.jpg)

1. After the installation is complete, the installed components are as follows:

    ![sriov04](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/network/images/sriov04.jpg)

1. Refer to the following **SriovNetworkNodePolicy** configuration to allow the SR-IOV Operator to create VFs on the host and report resources.

    The YAML configuration is as follows:

    ```yaml
    apiVersion: sriovnetwork.openshift.io/v1
    kind: SriovNetworkNodePolicy
    metadata:
      name: policyrdma
      namespace: kube-system
    spec:
      nodeSelector:
        kubernetes.io/os: "linux"
      resourceName: mellanoxrdma  # Custom resource name, used when creating applications
      priority: 99
      numVfs: 8  # Number of available numVFS, cannot be greater than the maximum available number queried in step 2
      nicSelector:
        deviceID: "1017" # Device ID queried in step 3
        rootDevices: # rootDevices pfNames queried in step 3
        - 0000:04:00.0 
        vendor: "15b3" # Network card vendors queried in step 3
      deviceType: netdevice
      isRdma: true  # Enable RDMA
    ```

    Interface configuration:
   
    ![sriov05](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/network/images/sriov05.jpg)

    ![sriov06](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/network/images/sriov06.jpg)

1. After the installation is complete, check the available device resources:

    ```sh
    kubectl get no -o json | jq -r '[.items[] | {name:.metadata.name, allocable:.status.allocatable}]'
    [
     {
       "name": "10-20-1-220",
       "allocable": {
         "cpu": "56",
         "ephemeral-storage": "3971227249029",
         "hugepages-1Gi": "0",
         "hugepages-2Mi": "0",
         "memory": "131779740Ki",
         "pods": "110",
         "spidernet.io/hca_shared_devices": "0",
         "spidernet.io/mellanoxrdma": "8", # Number of available device resources
         ...
       }
     }
    ```

1. If Spiderpool has been successfully deployed and the Device resources have been successfully discovered, please complete the following steps:

    - Complete the creation of Multus instances, please refer to [Creating Multus CR](../../../config/multus-cr.md)
    - Complete the creation of IP Pool, please refer to [Creating Subnets and IP Pool](../../../config/ippool/createpool.md)

    After the creation is complete, you can use this resource pool to create workloads. Please refer to [Using RDMA in Workloads](../../../config/userdma.md) for details. For more usage methods, please refer to [Using IP Pool in Workloads](../../../config/use-ippool/usage.md).
