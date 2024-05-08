# Configure GPU (vGPU) for Virtual Machines

This page will explain the prerequisites for configuring GPU when creating a virtual machine.

The key to configuring GPU for virtual machines is to configure the GPU Operator to deploy different software components on the worker nodes, depending on the GPU workload configuration. Here are three example nodes:

- The controller-node-1 node is configured to run containers.
- The work-node-1 node is configured to run virtual machines with GPU passthrough.
- The work-node-2 node is configured to run virtual machines with virtual vGPU.

## Assumptions, Limitations, and Dependencies

The worker nodes can run GPU-accelerated containers, virtual machines with GPU passthrough, or virtual machines with vGPU. However, a combination of any of these is not supported.

1. The worker nodes can run GPU-accelerated containers, virtual machines with GPU passthrough, or virtual machines with vGPU individually, but not in any combination.
2. The cluster administrator or developer needs to have prior knowledge of the cluster and correctly label the nodes to indicate the type of GPU workload they will run.
3. The worker node that runs a GPU-accelerated virtual machine with GPU passthrough or vGPU is assumed to be a bare metal machine. If the worker node is a virtual machine, the GPU passthrough feature needs to be enabled on the virtual machine platform. Please consult your virtual machine platform provider for guidance.
4. Nvidia MIG is not supported for vGPU.
5. The GPU Operator does not automatically install GPU drivers in the virtual machine.

## Enable IOMMU

To enable GPU passthrough, the cluster nodes need to have IOMMU enabled. Please refer to [How to Enable IOMMU](https://www.server-world.info/en/note?os=CentOS_7&p=kvm&f=10). If your cluster is running on a virtual machine, please consult your virtual machine platform provider.

## Build vGPU Manager Image

Note: This step is only required when using NVIDIA vGPU. If you plan to use GPU passthrough only, skip this section.

Follow these steps to build the vGPU Manager image and push it to the image repository:

1. Download the vGPU software from the NVIDIA Licensing Portal.

    - Log in to the NVIDIA Licensing Portal and go to the **Software Downloads** page.
    - The NVIDIA vGPU software is located in the **Driver downloads** tab on the **Software Downloads** page.
    - Select **VGPU + Linux** in the filter criteria and click **Download** to get the Linux KVM package.
      Unzip the downloaded file (`NVIDIA-Linux-x86_64-<version>-vgpu-kvm.run`).


2. Open a terminal and clone the container-images/driver repository.

    ```bash
    git clone https://gitlab.com/nvidia/container-images/driver cd driver
    ```

3. Switch to the vgpu-manager directory corresponding to your operating system.

    ```bash
    cd vgpu-manager/<your-os>
    ```

4. Copy the .run file extracted in step 1 to the current directory.

    ```bash
    cp <local-driver-download-directory>/*-vgpu-kvm.run ./
    ```

5. Set the environment variables.

    - PRIVATE_REGISTRY: The name of the private registry to store the driver image.
    - VERSION: The version of the NVIDIA vGPU Manager, downloaded from the NVIDIA Software Portal.
    - OS_TAG: Must match the operating system version of the cluster nodes.
    - CUDA_VERSION: The base CUDA image version used to build the driver image.

    ```bash
    export PRIVATE_REGISTRY=my/private/registry VERSION=510.73.06 OS_TAG=ubuntu22.04 CUDA_VERSION=12.2.0
    ```

6. Build the NVIDIA vGPU Manager Image.

    ```bash
    docker build \
      --build-arg DRIVER_VERSION=${VERSION} \
      --build-arg CUDA_VERSION=${CUDA_VERSION} \
      -t ${PRIVATE_REGISTRY}``/vgpu-manager``:${VERSION}-${OS_TAG} .
    ```

7. Push the NVIDIA vGPU Manager image to your image repository.

    ```bash
    docker push ${PRIVATE_REGISTRY}/vgpu-manager:${VERSION}-${OS_TAG}
    ```

## Label the Cluster Nodes

Go to __Container Management__, select your working cluster, click __Node Management__, and then click __Modify Labels__ in the action bar to add labels to the nodes. Each node can only have one label.

You can assign the following values to the labels: container, vm-passthrough, and vm-vgpu.



## Install Nvidia Operator 

1. Go to __Container Management__, select your working cluster, click __Helm Apps__ -> __Helm Chart__, and choose and install gpu-operator. Modify the relevant fields in the yaml.

    ```yaml
    gpu-operator.sandboxWorkloads.enabled=true
    gpu-operator.vgpuManager.enabled=true
    gpu-operator.vgpuManager.repository=<your-register-url>      # (1)!
    gpu-operator.vgpuManager.image=vgpu-manager
    gpu-operator.vgpuManager.version=<your-vgpu-manager-version> # (2)!
    gpu-operator.vgpuDeviceManager.enabled=true
    ```

    1. The image repository address from the "Build vGPU Manager Image" step.
    2. The VERSION from the "Build vGPU Manager Image" step.

2. Wait for the installation to succeed, as shown in the following image:



## Install virtnest-agent and Configure CR

1. Install virtnest-agent, refer to [Install virtnest-agent](../install/virtnest-agent.md).

2. Add vGPU and GPU passthrough to the Virtnest Kubevirt CR. The following example shows the relevant yaml after adding vGPU and GPU passthrough:

    ```yaml
    spec:
      configuration:
        developerConfiguration:
          featureGates:
          - GPU
          - DisableMDEVConfiguration
        permittedHostDevices: # (1)!
          mediatedDevices:            # (2)!
          - mdevNameSelector: GRID P4-1Q
            resourceName: nvidia.com /GRID_P4-1Q
        pciHostDevices:             # (3)!
        - externalResourceProvider:  true
          pciVendorSelector: 10DE:1BB3
          resourceName: nvidia.com /GP104GL_TESLA_P4
    ```

    1. The following information needs to be filled in
    2. vGPU
    3. GPU passthrough

3. In the kubevirt CR yaml, `permittedHostDevices` is used to import VM devices. For vGPU, mediatedDevices needs to be added, with the following structure:

    ```yaml
    mediatedDevices:          
    - mdevNameSelector: GRID P4-1Q          # (1)!
      resourceName: nvidia.com/GRID_P4-1Q   # (2)!
    ```

    1. Device name
    2. vGPU information registered by the GPU Operator on the node

4. For GPU passthrough, pciHostDevices needs to be added under `permittedHostDevices`, with the following structure:

    ```yaml
    pciHostDevices:           
    - externalResourceProvider: true            # (1)!
      pciVendorSelector: 10DE:1BB3              # (2)!
      resourceName: nvidia.com/GP104GL_TESLA_P4 # (3)!
    ```

    1. Do not change this by default
    2. Vendor ID of the current PCI device
    3. GPU information registered by the GPU Operator on the node

5. Example of obtaining vGPU information (only applicable to vGPU): View the node information on the node marked as `nvidia.com/gpu.workload.config=vm-gpu`, such as `work-node-2`, in the Capacity section, `nvidia.com/GRID_P4-1Q: 8` indicates the available vGPU:

    ```bash
    kubectl describe node work-node-2
    ```
    ```output
    Capacity:
      cpu:                                 64
      devices.kubevirt.io/kvm:             1k
      devices.kubevirt.io/tun:             1k
      devices.kubevirt.io/vhost-net:       1k
      ephemeral-storage:                   102626232Ki
      hugepages-1Gi:                       0
      hugepages-2Mi:                       0
      memory:                              264010840Ki
      nvidia.com/GRID_P4-1Q :              8
      pods:                                110
    Allocatable:
      cpu:                               	64
      devices.kubevirt.io/kvm:           	1k
      devices.kubevirt.io/tun:           	1k
      devices.kubevirt.io/vhost-net:     	1k
      ephemeral-storage:                 	94580335255
      hugepages-1Gi:                     	0
      hugepages-2Mi:                     	0
      memory:                            	263908440Ki
      nvidia.com/GRID_P4-1Q:             	8
      pods:                              	110
    ```

    In this case, the mdevNameSelector should be "GRID P4-1Q" and the resourceName should be "GRID_P4-1Q".

6. Get GPU passthrough information: On the node marked as `nvidia.com/gpu.workload.config=vm-passthrough` (work-node-1 in this example), view the node information. In the Capacity section, `nvidia.com/GP104GL_TESLA_P4: 2` represents the available vGPU:

    ```bash
    kubectl describe node work-node-1
    ```
    ```output
    Capacity:
      cpu:                            64
      devices.kubevirt.io/kvm:        1k
      devices.kubevirt.io/tun:        1k
      devices.kubevirt.io/vhost-net:  1k
      ephemeral-storage:              102626232Ki
      hugepages-1Gi:                  0
      hugepages-2Mi:                  0
      memory:                         264010840Ki
      nvidia.com/GP104GL_TESLA_P4:    2
      pods:                           110
    Allocatable:
      cpu:                            64
      devices.kubevirt.io/kvm:        1k
      devices.kubevirt.io/tun:        1k
      devices.kubevirt.io/vhost-net:  1k
      ephemeral-storage:              94580335255
      hugepages-1Gi:                  0
      hugepages-2Mi:                  0
      memory:                         263908440Ki
      nvidia.com/GP104GL_TESLA_P4:    2
      pods:                           110
    ```

    The resourceName should be "GRID_P4-1Q". How to obtain the pciVendorSelector? SSH into the target node work-node-1 and use the `lspci -nnk -d 10de:` command to obtain the Nvidia GPU PCI information, as shown below: The red box indicates the pciVendorSelector information.


7. Edit the kubevirt CR note: If there are multiple GPUs of the same model, you only need to write one in the CR, there is no need to list every GPU.

    ```bash
    kubectl -n virtnest-system edit kubevirt kubevirt
    ```
    ```yaml
    spec:
      configuration:
        developerConfiguration:
          featureGates:
          - GPU
          - DisableMDEVConfiguration
        permittedHostDevices: # (1)!
          mediatedDevices:                    # (2)!
          - mdevNameSelector: GRID P4-1Q
            resourceName: nvidia.com/GRID_P4-1Q
        pciHostDevices:                       # (3)!
          - externalResourceProvider: true
            pciVendorSelector: 10DE:1BB3
            resourceName: nvidia.com/GP104GL_TESLA_P4 
    ```

    1. The following information needs to be filled in
    2. vGPU
    3. GPU passthrough; in the example above, there are two GPUs for TEESLA P4, so only one needs to be registered here

## Create VM Using YAML and Enable GPU Acceleration

The only difference from a regular virtual machine is adding the gpu-related information in the devices section.

??? note "Click to view the complete YAML"

    ```yaml
    apiVersion: kubevirt.io/v1
    kind: VirtualMachine
    metadata:
      name: testvm-gpu1
      namespace: default
    spec:
      dataVolumeTemplates:
      - metadata:
          creationTimestamp: null
          name: systemdisk-testvm-gpu1
          namespace: default
        spec:
          pvc:
            accessModes:
            - ReadWriteOnce
            resources:
              requests:
                storage: 10Gi
            storageClassName: www
          source:
            registry:
              url: docker://release-ci.daocloud.io/virtnest/system-images/debian-12-x86_64:v1
    runStrategy: Manual
    template:
        metadata:
          creationTimestamp: null
        spec:
          domain:
            cpu:
              cores: 1
              sockets: 1
              threads: 1
            devices:
              disks:
              - bootOrder: 1
                disk:
                  bus: virtio
                name: systemdisk-testvm-gpu1
              - disk:
                  bus: virtio
                name: cloudinitdisk
            gpus:
            - deviceName: nvidia.com/GP104GL_TESLA_P4
                name: gpu-0-0
            - deviceName: nvidia.com/GP104GL_TESLA_P4
              name: gpu-0-1
            interfaces:
            - masquerade: {}
              name: default
          machine:
            type: q35
          resources:
            requests:
              memory: 2Gi
        networks:
        - name: default
          pod: {}
        volumes:
        - dataVolume:
            name: systemdisk-testvm-gpu1
          name: systemdisk-testvm-gpu1
        - cloudInitNoCloud:
            userDataBase64: I2Nsb3VkLWNvbmZpZwpzc2hfcHdhdXRoOiB0cnVlCmRpc2FibGVfcm9vdDogZmFsc2UKY2hwYXNzd2Q6IHsibGlzdCI6ICJyb290OmRhbmdlcm91cyIsIGV4cGlyZTogRmFsc2V9CgoKcnVuY21kOgogIC0gc2VkIC1pICIvI1w/UGVybWl0Um9vdExvZ2luL3MvXi4qJC9QZXJtaXRSb290TG9naW4geWVzL2ciIC9ldGMvc3NoL3NzaGRfY29uZmlnCiAgLSBzeXN0ZW1jdGwgcmVzdGFydCBzc2guc2VydmljZQ==
            name: cloudinitdisk
    ```
