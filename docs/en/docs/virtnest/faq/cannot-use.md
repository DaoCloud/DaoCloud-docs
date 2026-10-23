# VM Cannot Be Used Normally

If the created VM cannot be used normally, there are various reasons. Here are the troubleshooting directions:

## VM Creation Failed

When VM creation fails, check the detailed information of the VM in the target cluster:

```shell
kubectl -n your-namespace describe vm your-vm
```

If the detailed information involves storage such as PVC, PV, SC, etc., please check the SC status.
If the problem is not resolved, [consult developers](../../install/index.md#configure-helm-repo).

If the detailed information involves devices such as KVM, GPU, etc., please verify whether the target cluster nodes have completed [dependency checks](../install/install-dependency.md).
If all dependencies are installed, [consult developers](../../install/index.md#configure-helm-repo).

### Case 1

- Phenomenon: Error reported even with sufficient resources:

    ![Create VM error one](../images/createvm-error01.png)

- Solution: [Enable hardware virtualization for nodes](../install/install-dependency.md#all-nodes-having-hardware-virtualization-nested-virtualization-enabled)

### Case 2

![Create VM error two](../images/createvm-error02.png)

Solution: [Upgrade the node operating system kernel](../install/install-dependency.md)

### Case 3

![Create VM error three](../images/createvm-error03.png)

Solution: Run the following command in the worker cluster:

```bash
kubectl patch cdi cdi \
  --type merge \
  --patch '{"spec":{"config":{"insecureRegistries":["your registry ip"]}}}'
```

## VM Created Successfully but Cannot Be Used

If the VM is created successfully but cannot be used, check whether the VNC page of the VM works normally on the DCE page.
If only startup information is displayed, check the [dependencies](../install/install-dependency.md).
If the dependencies are complete, [consult developers](../../install/index.md#configure-helm-repo).

If the VNC page displays an abnormality, use the following command to view the detailed information of the VM:

```shell
kubectl -n your-namespace describe vm your-vm
```

When the detailed information involves storage such as PVC, PV, SC, etc., check the SC status.
If the problem is not resolved, [consult developers](../../install/index.md#configure-helm-repo).

## VNC Starts but the Network Is Unreachable

Follow the troubleshooting procedure below, record the relevant information, and report it to [the developers](../../install/index.md#configure-helm-repo).
Perform the following operations in the cluster where the VM is located:

1. Get the Pod IP of the VM.

    ```bash
    kubectl -n your-namespace get vmi your-vm -o wide
    ```

2. Log in to your VM via SSH on the node.

    ```bash
    ssh your-vm-username@xx.xx.xx.xx
    ```

    If it is unreachable, [consult developers](../../install/index.md#configure-helm-repo).

3. Check the network mode used by the VM.

    If it is the default network mode (masquerade), [consult developers](../../install/index.md#configure-helm-repo).

    If it is bridge + ovs, confirm the following information.

    - Check whether Spiderpool is installed successfully and make sure it is installed in the `kube-system` namespace.
    - Check whether ovs is installed successfully and whether the ovs bridge is configured successfully.

    If the information above is correct, [consult developers](../../install/index.md#configure-helm-repo).
