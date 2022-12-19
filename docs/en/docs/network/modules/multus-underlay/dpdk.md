#DPDK

This article mainly introduces how to quickly create the first DPDK application in DCE 5.0.

## pre-dependency

- Install Multus-underlay, and enable the installation of SRIOV components, refer to [Install](install.md)
- Hardware support is required: have a network card that supports SR-IOV series and set up a virtual function (VF), refer to [SR-IOV](sriov.md)
- Need to switch the network card driver to user mode driver

```shell
# Download dpdk source code
root@master:~/cyclinder/sriov/# wget https://fast.dpdk.org/rel/dpdk-22.07.tar.xz && cd dpdk-22.07/usertools
root@master:~/cyclinder/sriov/dpdk-22.07/usertools# ./dpdk-devbind.py --status
root@172-17-8-120:~/cyclinder/sriov/dpdk-22.07/usertools# ./dpdk-devbind.py --status
Network devices using kernel driver
=====================================
0000:01:00.0 'I350 Gigabit Network Connection 1521' if=eno1 drv=igb unused=vfio-pci
0000:01:00.1 'I350 Gigabit Network Connection 1521' if=eno2 drv=igb unused=vfio-pci
0000:01:00.2 'I350 Gigabit Network Connection 1521' if=eno3 drv=igb unused=vfio-pci
0000:01:00.3 'I350 Gigabit Network Connection 1521' if=eno4 drv=igb unused=vfio-pci
0000:04:00.0 'MT27800 Family [ConnectX-5] 1017' if=enp4s0f0np0 drv=mlx5_core unused=vfio-pci *Active*
0000:04:00.1 'MT27800 Family [ConnectX-5] 1017' if=enp4s0f1np1 drv=mlx5_core unused=vfio-pci *Active*
0000:04:00.2 'MT27800 Family [ConnectX-5 Virtual Function] 1018' if=enp4s0f0v0 drv=mlx5_core unused=vfio-pci
0000:04:00.3 'MT27800 Family [ConnectX-5 Virtual Function] 1018' if=enp4s0f0v1 drv=mlx5_core unused=vfio-pci
0000:04:00.4 'MT27800 Family [ConnectX-5 Virtual Function] 1018' if=enp4s0f0v2 drv=mlx5_core unused=vfio-pci
0000:04:00.5 'MT27800 Family [ConnectX-5 Virtual Function] 1018' if=enp4s0f0v3 drv=mlx5_core unused=vfio-pci
0000:04:00.6 'MT27800 Family [ConnectX-5 Virtual Function] 1018' if=enp4s0f0v4 drv=mlx5_core unused=vfio-pci
0000:04:00.7 'MT27800 Family [ConnectX-5 Virtual Function] 1018' if=enp4s0f0v5 drv=mlx5_core unused=vfio-pci
0000:04:01.1 'MT27800 Family [ConnectX-5 Virtual Function] 1018' if=enp4s0f0v6 drv=mlx5_core unused=vfio-pci
```

Take `0000:04:00.2 'MT27800 Family [ConnectX-5 Virtual Function] 1018' if=enp4s0f0v0 drv=mlx5_core unused=vfio-pci` as an example:

- 0000:04:00.2: The VF PCI address
- if=enp4s0f0v0: the VF NIC name
- drv=mlx5_core: current network card driver
- unused=vfio-pci: Switchable NIC driver

There are three types of user mode drivers supported by DPDK:

- vfio-pci: When IoMMU is enabled, this driver is recommended for best performance and security
- igb-uio: more applicable than uio_pci_generic, supports SR-IOV VF, but needs to manually compile the module and load it into the kernel
- uio_pci_generic: kernel native driver, not compatible with SR-IOV VF, but supports use on VM

Switch the NIC driver to vfio-pci:

```shell
root@172-17-8-120:~/cyclinder/sriov/dpdk-22.07/usertools# ./dpdk-devbind.py --bind=vfio-pci 0000:04:01.1
```

View binding results:

```shell
root@172-17-8-120:~/cyclinder/sriov/dpdk-22.07/usertools# ./dpdk-devbind.py --status

Network devices using DPDK-compatible driver
===============================================
0000:04:01.1 'MT27800 Family [ConnectX-5 Virtual Function] 1018' drv=vfio-pci unused=mlx5_core

Network devices using kernel driver
=====================================
0000:01:00.0 'I350 Gigabit Network Connection 1521' if=eno1 drv=igb unused=vfio-pci
0000:01:00.1 'I350 Gigabit Network Connection 1521' if=eno2 drv=igb unused=vfio-pci
0000:01:00.2 'I350 Gigabit Network Connection 1521' if=eno3 drv=igb unused=vfio-pci
0000:01:00.3 'I350 Gigabit Network Connection 1521' if=eno4 drv=igb unused=vfio-pci
0000:04:00.0 'MT27800 Family [ConnectX-5] 1017' if=enp4s0f0np0 drv=mlx5_core unused=vfio-pci *Active*
0000:04:00.1 'MT27800 Family [ConnectX-5] 1017' if=enp4s0f1np1 drv=mlx5_core unused=vfio-pci *Active*
0000:04:00.2 'MT27800 Family [ConnectX-5 Virtual Function] 1018' if=enp4s0f0v0 drv=mlx5_core unused=vfio-pci
0000:04:00.3 'MT27800 Family [ConnectX-5 Virtual Function] 1018' if=enp4s0f0v1 drv=mlx5_core unused=vfio-pci
0000:04:00.4 'MT27800 Family [ConnectX-5 Virtual Function] 1018' if=enp4s0f0v2 drv=mlx5_core unused=vfio-pci
0000:04:00.5 'MT27800 Family [ConnectX-5 Virtual Function] 1018' if=enp4s0f0v3 drv=mlx5_core unused=vfio-pci
0000:04:00.6 'MT27800 Family [ConnectX-5 Virtual Function] 1018' if=enp4s0f0v4 drv=mlx5_core unused=vfio-pci
0000:04:00.7 'MT27800 Family [ConnectX-5 Virtual Function] 1018' if=enp4s0f0v5 drv=mlx5_core unused=vfio-pci
```

`0000:04:01.1`: changed to vfio-pci driver

- Set huge page memory and enable IoMMU (vfio-pci driver relies on IOMMU technology):

    Edit `/etc/default/grub` and add the following to `GRUB_CMDLINE_LINUX`:

    ```shell
    GRUB_CMDLINE_LINUX='default_hugepagesz=1GB hugepagesz=1GB hugepages=6 isolcpus=1-3 intel_iommu=on iommu=pt'
    update-grab && reboot
    ```

    !!! note

        To update the above configuration, you need to restart the system, it is best to back up before restarting the system.
        If the configuration cannot be updated, the driver needs to be switched to the igb-uio driver, and manual build && insmod && modprobe is required. For details, refer to https://github.com/atsgen/dpdk-kmod

## Configure SRIOV-Device-Plugin

- Update the configmap of SRIOV-Device-plugin: create a new resource pool sriov_netdevice_dpdk, so that it can find the VF that supports dpdk:

    ```shell
    kubectl edit cm -n kube-system sriov-0.1.1-config
    apiVersion: v1
    data:
      config.json: |-
        {
          "resourceList":
          [{
            "resourceName": "sriov_netdevice",
            "resourcePrefix": "intel.com",
            "selectors": {
              "device": ["1018"],
              "vendors": ["15b3"],
              "drivers": ["mlx5_core"],
              "pfNames": []
            }
          },{
            "resourceName": "sriov_netdevice_dpdk",
            "resourcePrefix": "intel.com",
            "selectors": {
              "drivers": ["vfio-pci"]
            }
          }]
        }
    ```

    Added sriov_netdevice_dpdk. Note that if the driver specifies vfio-pci in the selectors, the sriov-device-plugin will be restarted.

    ```shell
    kubectl delete po -n kube-system -l app=sriov-dp
    ```

    Wait for the restart to complete, and check whether Node loads the sriov_netdevice_dpdk resource:

    ```sh
    kubectl describe nodes 172-17-8-120
    ...
    Allocatable:
      cpu: 24
      ephemeral-storage: 881675818368
      hugepages-1Gi: 6Gi
      hugepages-2Mi: 0
      intel.com/sriov_netdevice: 6
      intel.com/sriov_netdevice_dpdk: 1 # It is displayed here to indicate that it is already available
    ```

- Create a Multus DPDK CRD:

    ```shell
    cat EOF | kubectl apply -f -
    > apiVersion: k8s.cni.cncf.io/v1
    kind: NetworkAttachmentDefinition
    metadata:
      annotations:
        helm.sh/hook: post-install
        helm.sh/resource-policy: keep
        k8s.v1.cni.cncf.io/resourceName: intel.com/sriov_netdevice_dpdk
        v1.multus-underlay-cni.io/coexist-types: '["default"]'
        v1.multus-underlay-cni.io/default-cni: "false"
        v1.multus-underlay-cni.io/instance-type: sriov_dpdk
        v1.multus-underlay-cni.io/underlay-cni: "true"
        v1.multus-underlay-cni.io/vlanId: "0"
      name: sriov-dpdk-vlan0
      namespace: kube-system
    spec:
      config: |-
        {
          "cniVersion": "0.3.1",
          "name": "sriov-dpdk",
          "type": "sriov",
          "vlan": 0
        }
    > EOF
    ```

## Create DPDK Test Pod

```shell
cat << EOF | kubectl apply -f -
> apiVersion: v1
kind: Pod
metadata:
  name: dpdk-demo
  annotations:
    k8s.v1.cni.cncf.io/networks: kube-system/sriov-dpdk-vlan0
spec:
  containers:
  - name: sriov-dpdk
    image: docker.io/bmcfall/dpdk-app-centos
    securityContext:
      privileged: true
    volumeMounts:
    - mountPath: /etc/podnetinfo
      name: podnetinfo
      readOnly: false
    - mountPath: /dev/hugepages
      name: hugepage
    resources:
      requests:
        memory: 1Gi
        #cpu: "4"
        intel.com/sriov_netdevice_dpdk: '1'
      limits:
        hugepages-1Gi: 2Gi
        #cpu: "4"
        intel.com/sriov_netdevice_dpdk: '1'
    # Uncomment to control which DPDK App is running in container.
    # If not provided, l3fwd is default.
    # Options: l2fwd l3fwd testpmd
    env:
    - name: DPDK_SAMPLE_APP
      value: "testpmd"
    #
    # Uncomment to debug DPDK App or to run manually to change
    # DPDK command line options.
    command: ["sleep", "infinity"]
  volumes:
  - name: podnetinfo
    downwardAPI:
      items:
        - path: "labels"
          fieldRef:
            fieldPath: metadata. labels
        - path: "annotations"
          fieldRef:
            fieldPath: metadata.annotations
  - name: hugepage
    emptyDir:
      medium: HugePages
> EOF
```

Wait for Pod Running, then enter the Pod:

```shell
root@172-17-8-120:~# kubectl exec -it sriov-pod-2 sh
kubectl exec [POD] [COMMAND] is DEPRECATED and will be removed in a future version. Use kubectl exec [POD] -- [COMMAND] instead.
sh-4.4#dpdk-app
ENTER dpdk-app:
 argc=1
 dpdk-app
E1031 08:17:36.431877 116 resource.go:31] Error getting cpuset info: open /proc/116/root/sys/fs/cgroup/cpuset/cpuset.cpus: no such file or directory
E1031 08:17:36.432266 116 netutil_c_api.go:119] netlib.GetCPUInfo() err: open /proc/116/root/sys/fs/cgroup/cpuset/cpuset.cpus: no such file or directory
Couldn't get CPU info, err code: 1
  Interface[0]:
    IfName="" Name="kube-system/k8s-pod-network" Type=SR-IOV
    MAC="" IP="10.244.5.197" IP="fd00:10:244:0:eb50:e529:8533:7884"
    PCIAddress=0000:04:01.1
  Interface[1]:
    IfName="net1" Name="kube-system/sriov-dpdk-vlan0" Type=SR-IOV
    MAC=""

 myArgc=14
 dpdk-app -n 4 -l 1 --master-lcore 1 -w 0000:04:01.1 -- -p 0x1 -P --config="(0,0,1)" --parse-ptype
```

dpdk-app will print out the relevant information of the current Pod, including the IP, MAC and type of eth0.
It is worth noting that the net1 network card does not have any network information such as IP and MAC, which conforms to the characteristics of DPDK and can work without the kernel network protocol stack.