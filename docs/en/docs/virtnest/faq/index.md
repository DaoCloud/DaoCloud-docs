# Virtual Machine FAQ

Virtual machine (virtnest) consists of two parts: apiserver and agent. When encountering problems, troubleshoot from these two parts.

*[kpanda]: Codename for container management in DCE
*[virtnest]: Codename for virtual machine in DCE
*[PVC]: PersistentVolumeClaim
*[PV]: PersistentVolume
*[VM]: Virtual Machine
*[KM]: Kernel-based Virtual Machine
*[SC]: Storage Class
*[VNC]: Virtual Network Console

## Page API Error

If the page requests API error 500 or cluster resource does not exist,
first check the logs of VM-related services in the [Global Service Cluster](../../kpanda/user-guide/clusters/cluster-role.md#global-service-cluster),
looking for keywords of kpanda. If they exist, confirm whether kpanda-related services are running normally.
