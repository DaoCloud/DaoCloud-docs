# Configure GPU Passthrough for Virtual Machines

This page will explain the prerequisites for configuring GPU when creating a virtual machine.

The key to configuring GPU for virtual machines is to configure the GPU Operator to deploy different
software components on the worker nodes, depending on the GPU workload configuration. Here are three example nodes:

- The controller-node-1 node is configured to run containers.
- The work-node-1 node is configured to run virtual machines with GPU passthrough.
- The work-node-2 node is configured to run virtual machines with virtual vGPU.

## Assumptions, Limitations, and Dependencies

The worker nodes can run GPU-accelerated containers, virtual machines with GPU passthrough, or virtual machines with vGPU. However, a combination of any of these is not supported.

1. The cluster administrator or developer needs to have prior knowledge of the cluster and correctly label the nodes to indicate the type of GPU workload they will run.
2. The worker node that runs a GPU-accelerated virtual machine with GPU passthrough or vGPU is assumed to
   be a bare metal machine. If the worker node is a virtual machine, the GPU passthrough feature needs to
   be enabled on the virtual machine platform. Please consult your virtual machine platform provider for guidance.
3. Nvidia MIG is not supported for vGPU.
4. The GPU Operator does not automatically install GPU drivers in the virtual machine.

## Enable IOMMU

To enable GPU passthrough, the cluster nodes need to have IOMMU enabled. Refer to
[How to Enable IOMMU](https://www.server-world.info/en/note?os=CentOS_7&p=kvm&f=10).
If your cluster is running on a virtual machine, please consult your virtual machine platform provider.

## Label the Cluster Nodes

Go to __Container Management__, select your working cluster, click __Node Management__, and then click __Modify Labels__ in the action bar to add labels to the nodes. Each node can only have one label.

You can assign the following values to the labels: container, vm-passthrough, and vm-vgpu.

## Install Nvidia Operator

1. Go to __Container Management__, select your working cluster, click __Helm Apps__ -> __Helm Chart__ ,
   and choose and install gpu-operator. Modify the relevant fields in the yaml.

    ```yaml
    gpu-operator.sandboxWorkloads.enabled=true
    gpu-operator.vfioManager.enabled=true
    gpu-operator.sandboxDevicePlugin.enabled=true
    gpu-operator.sandboxDevicePlugin.version=v1.2.4   // version should be >= v1.2.4
    gpu-operator.toolkit.version=v1.14.3-ubuntu20.04
    ```

2. Wait for the installation to succeed, as shown in the following image:

## Install virtnest-agent and Configure CR

1. Install virtnest-agent, refer to [Install virtnest-agent](../install/virtnest-agent.md).

2. Add vGPU and GPU passthrough to the Virtnest Kubevirt CR.
   The following example shows the relevant yaml after adding vGPU and GPU passthrough:

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

3. In the kubevirt CR yaml, `permittedHostDevices` is used to import VM devices.
   For vGPU, mediatedDevices needs to be added, with the following structure:

    ```yaml
    mediatedDevices:          
    - mdevNameSelector: GRID P4-1Q          # (1)!
      resourceName: nvidia.com/GRID_P4-1Q   # (2)!
    ```

    1. Device name
    2. vGPU information registered by GPU Operator on the node

4. For GPU passthrough, pciHostDevices needs to be added under `permittedHostDevices`,
   with the following structure:

    ```yaml
    pciHostDevices:           
    - externalResourceProvider: true            # (1)!
      pciVendorSelector: 10DE:1BB3              # (2)!
      resourceName: nvidia.com/GP104GL_TESLA_P4 # (3)!
    ```

    1. Do not change this by default
    2. Vendor ID of the current PCI device
    3. GPU information registered by GPU Operator on the node

5. Example of obtaining vGPU information (only applicable to vGPU):
   View the node information on the node marked as `nvidia.com/gpu.workload.config=vm-gpu`,
   such as `work-node-2`, in the Capacity section, `nvidia.com/GRID_P4-1Q: 8` indicates the available vGPU:

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

6. Get GPU passthrough information: On the node marked as `nvidia.com/gpu.workload.config=vm-passthrough`
   (work-node-1 in this example), view the node information.
   In the Capacity section, `nvidia.com/GP104GL_TESLA_P4: 2` represents the available vGPU:

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

    The resourceName should be "GRID_P4-1Q". How to obtain the pciVendorSelector?
    Use SSH to log in to the target node work-node-1 and use the `lspci -nnk -d 10de:` command
    to obtain the Nvidia GPU PCI information, as shown below: The red box indicates the pciVendorSelector information.


7. Edit the kubevirt CR note: If there are multiple GPUs of the same model,
   you only need to write one in the CR, there is no need to list every GPU.

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

The only difference from a regular virtual machine is adding GPU-related information in the devices section.

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
