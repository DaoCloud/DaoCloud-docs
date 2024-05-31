# FAQs

The virtual machine consists of two parts: apiserver and agent.
When you encounter an issue, you can refer to this page to perform troubleshooting.

*[kpanda]: Codename for container management in DCE 5.0
*[virtnest]: Codename for virtual machine in DCE 5.0
*[PVC]: PersistentVolumeClaim
*[PV]: PersistentVolume
*[VM]: Virtual Machine
*[KM]: Kernel-based Virtual Machine
*[SC]: Storage Class
*[VNC]: Virtual Network Console

## Page API Errors

If there is an API error with a page request, such as a 500 error or a cluster resource not found,
the first step is to check the logs of the virtual machine-related services in the Global cluster
for any keywords related to kpanda. If there are any, it is necessary to confirm whether the
kpanda-related services are running properly.

## VM Cannot Be Used Properly

If a created VM cannot be used properly, there can be various reasons.
Here are some troubleshooting directions:

### VM Creation Failure

When a VM creation fails, you should check the detailed information of the VM in the target cluster:

```shell
kubectl -n your-namespace describe vm your-vm
```

If the detailed information involves storage, such as PVC, PV, SC, etc., check the status of the SC.
If the problem is not resolved, consult with the [developers](../../install/index.md#contact-us).

If the detailed information involves devices, such as KVM, GPU, etc.,
verify whether the target cluster nodes have completed the dependency check.
If all dependencies are installed, consult with the [developers](../../install/index.md#contact-us).

### VM Creation Success but Cannot Be Used

If a VM is successfully created but cannot be used, check the VNC page of the VM in the DCE interface.
If it only shows the startup information, check the dependencies. If all dependencies are installed,
consult with the [developers](../../install/index.md#contact-us).

If the VNC page displays an error, use the following command to view detailed information about the VM:

```shell
kubectl -n your-namespace describe vm your-vm
```

If the detailed information involves storage, such as PVC, PV, SC, etc.,
check the status of the SC. If the problem is not resolved,
consult with the [developers](../../install/index.md#contact-us).

### VNC Can Start but Network is Unreachable

Follow the steps below to troubleshoot and document the relevant information.
Provide feedback to [developers](../../install/index.md#contact-us).
Execute the following steps in the cluster where the VM is located:

1. Obtain the Pod IP of the VM

    ```bash
    kubectl -n your-namespace get vmi your-vm -o wide
    ```

2. Perform SSH login to your VM on the node

    ```bash
    ssh your-vm-username@xx.xx.xx.xx
    ```

    If access is not possible, please [consult the developers](../../install/index.md#contact-us).

3. Check the network mode used by the VM

    If it is the default network mode (masquerade), [consult the developers](../../install/index.md#contact-us).

    If it is bridge + ovs, confirm the following information.

    - Ensure Spiderpool is installed successfully and is installed in the `kube-system` namespace.
    - Ensure ovs is installed successfully and the ovs bridge is configured correctly.

    If all the above information is confirmed to be correct, please [consult the developers](../../install/index.md#contact-us).
