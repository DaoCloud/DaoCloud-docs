# FAQs

The virtual machine consists of two parts: apiserver and agent.
When you encounter an issues, you can refer to this page to perform troubleshooting.

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
If the problem is not resolved, consult with the developers.

If the detailed information involves devices, such as KVM, GPU, etc.,
verify whether the target cluster nodes have completed the dependency check.
If all dependencies are installed, consult with the developers.

### VM Creation Success but Cannot Be Used

If a VM is successfully created but cannot be used, check the VNC page of the VM in the DCE interface.
If it only shows the startup information, check the dependencies. If all dependencies are installed,
consult with the developers.

If the VNC page displays an error, use the following command to view detailed information about the VM:

```shell
kubectl -n your-namespace describe vm your-vm
```

If the detailed information involves storage, such as PVC, PV, SC, etc.,
check the status of the SC. If the problem is not resolved, consult with the developers.
