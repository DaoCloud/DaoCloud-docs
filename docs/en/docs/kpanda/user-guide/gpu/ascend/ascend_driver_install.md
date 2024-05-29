# Installation of Ascend NPU Components

This chapter provides installation guidance for Ascend NPU drivers, Device Plugin, NPU-Exporter, and other components.

## Prerequisites

1. Before installation, confirm the supported NPU models. For details, please refer to the [Ascend NPU Matrix](../gpu_matrix.md).
2. Ensure that the kernel version required for the corresponding NPU model is compatible. For more details, refer to the [Ascend NPU Matrix](../gpu_matrix.md).
3. Prepare the basic Kubernetes environment.

## Installation Steps

Before using NPU resources, you need to complete the firmware installation, NPU driver installation, Docker Runtime installation, user creation, log directory creation, and NPU Device Plugin installation. Refer to the following steps for details.

### Install Firmware

1. Confirm that the kernel version is within the range corresponding to the "binary installation" method, and then you can directly install the NPU driver firmware.
2. For firmware and driver downloads, refer to: [Firmware Download Link](https://www.hiascend.com/zh/hardware/firmware-drivers/community?product=2&model=15&cann=6.3.RC2.alpha005&driver=1.0.20.alpha)
3. For firmware installation, refer to: [Install NPU Driver Firmware](https://www.hiascend.com/document/detail/zh/quick-installation/23.0.RC2/quickinstg/800_3000/quickinstg_800_3000_0001.html)

### Install NPU Driver

1. If the driver is not installed, refer to the official Ascend documentation for installation. For example, for Ascend910, refer to: [910 Driver Installation Document](https://www.hiascend.com/document/detail/zh/Atlas%20200I%20A2/23.0.RC3/EP/installationguide/Install_87.html).
2. Run the command `npu-smi info`, and if it returns NPU information normally, it indicates that the NPU driver and firmware are ready.

<!-- add screenshot later -->

### Install Docker Runtime

1. Download Ascend Docker Runtime

    Community edition download link: https://www.hiascend.com/zh/software/mindx-dl/community

    ```sh
    wget -c https://mindx.obs.cn-south-1.myhuaweicloud.com/OpenSource/MindX/MindX%205.0.RC2/MindX%20DL%205.0.RC2/Ascend-docker-runtime_5.0.RC2_linux-x86_64.run
    ```

    Install to the specified path by executing the following two commands in order, with parameters specifying the installation path:

    ```sh
    chmod u+x Ascend-docker-runtime_5.0.RC2_linux-x86_64.run 
    ./Ascend-docker-runtime_{version}_linux-{arch}.run --install --install-path=<path>
    ```

2. Modify the containerd configuration file

    If containerd has no default configuration file, execute the following three commands in order to create the configuration file:

    ```bash
    mkdir /etc/containerd 
    containerd config default > /etc/containerd/config.toml 
    vim /etc/containerd/config.toml
    ```

    If containerd has a configuration file:

    ```bash
    vim /etc/containerd/config.toml
    ```

    Modify the runtime installation path according to the actual situation, mainly modifying the runtime field:

    ```toml
    ... 
    [plugins."io.containerd.monitor.v1.cgroups"]
       no_prometheus = false  
    [plugins."io.containerd.runtime.v1.linux"]
       shim = "containerd-shim"
       runtime = "/usr/local/Ascend/Ascend-Docker-Runtime/ascend-docker-runtime"
       runtime_root = ""
       no_shim = false
       shim_debug = false
     [plugins."io.containerd.runtime.v2.task"]
       platforms = ["linux/amd64"]
    ...
    ```

    Execute the following command to restart containerd:

    ```bash
    systemctl restart containerd
    ```

### User Creation

Execute the following commands on the node where the components are installed to create a user.

```sh
# Ubuntu operating system
useradd -d /home/hwMindX -u 9000 -m -s /usr/sbin/nologin hwMindX
usermod -a -G HwHiAiUser hwMindX
# CentOS operating system
useradd -d /home/hwMindX -u 9000 -m -s /sbin/nologin hwMindX
usermod -a -G HwHiAiUser hwMindX
```

### Log Directory Creation

Create the parent directory for component logs and the log directories for each component on the corresponding node, and set the appropriate owner and permissions for the directories. Execute the following command to create the parent directory for component logs.

```bash
mkdir -m 755 /var/log/mindx-dl
chown root:root /var/log/mindx-dl
```

Execute the following command to create the Device Plugin component log directory.

```bash
mkdir -m 750 /var/log/mindx-dl/devicePlugin
chown root:root /var/log/mindx-dl/devicePlugin
```

!!! note

    Please create the corresponding log directory for each required component. In this example, only the Device Plugin component is needed.
    For other component requirements, please refer to the [official documentation](https://www.hiascend.com/document/detail/zh/mindx-dl/50rc3/clusterscheduling/clusterschedulingig/dlug_installation_016.html)

### Create Node Labels

Refer to the following commands to create labels on the corresponding nodes:

```shell
# Create this label on computing nodes where the driver is installed
kubectl label node {nodename} huawei.com.ascend/Driver=installed
kubectl label node {nodename} node-role.kubernetes.io/worker=worker
kubectl label node {nodename} workerselector=dls-worker-node
kubectl label node {nodename} host-arch=huawei-arm // or host-arch=huawei-x86, select according to the actual situation
kubectl label node {nodename} accelerator=huawei-Ascend910 // select according to the actual situation
# Create this label on control nodes
kubectl label node {nodename} masterselector=dls-master-node
```

### Install Device Plugin and NpuExporter

Functional module path: __Container Management__ -> __Cluster Management__, click the name of the target cluster, then click __Helm Applications__ -> __Helm Templates__ from the left navigation bar, and search for __ascend-mindxdl__.

<!-- add screenshot later -->

<!-- add screenshot later -->

-  __DevicePlugin__: Provides a general device plugin mechanism and standard device API interface for Kubernetes to use devices. It is recommended to use the default image and version.
-  __NpuExporter__: Based on the Prometheus/Telegraf ecosystem, this component provides interfaces to help users monitor the Ascend series AI processors and container-level allocation status. It is recommended to use the default image and version.
-  __ServiceMonitor__: Disabled by default. If enabled, you can view NPU-related monitoring in the observability module. To enable, ensure that the insight-agent is installed and running, otherwise, the ascend-mindxdl installation will fail.
-  __isVirtualMachine__: Disabled by default. If the NPU node is a virtual machine scenario, enable the isVirtualMachine parameter.

After a successful installation, two components will appear under the corresponding namespace, as shown below:

<!-- add screenshot later -->

At the same time, the corresponding NPU information will also appear on the node information:

<!-- add screenshot later -->

Once everything is ready, you can select the corresponding NPU device when creating a workload through the page, as shown below:

<!-- add screenshot later -->

!!! note

    For detailed usage steps, please refer to [Using Ascend (Ascend) NPU](https://docs.daocloud.io/kpanda/user-guide/gpu/Ascend_usage/).
