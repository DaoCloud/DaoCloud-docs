---
MTPE: Jeanine-tw
Revised: Jeanine-tw
Pics: NA
Date: 2022-12-23
---

# `IPPool`

`IPPool` indicates the set of addresses from which Calico expects to assign IPs to Pods. After pulling up Calico via Kubespray, a default IP pool is created for IPv4 and IPv6 respectively: `default-ipv4-ippool` and `default-ipv6-ippool`.

Run the command：

```shell
calicoctl get ippools  default-ipv4-ippool -o yaml
```

Output：

```yaml
apiVersion: crd.projectcalico.org/v1
kind: IPPool
metadata:
  annotations:
    projectcalico.org/metadata: '{"uid":"637e72f1-d4ff-433c-92c5-cafe3aef5753","creationTimestamp":"2022-05-12T14:34:03Z"}'
  creationTimestamp: "2022-05-12T14:34:03Z"
  generation: 1
  name: default-ipv4-pool
  resourceVersion: "689"
  uid: c94af437-5a37-46c8-b521-641724b86ff8
spec:
  allowedUses:
    - Workload
    - Tunnel
  blockSize: 26
  cidr: 10.244.0.0/18
  ipipMode: Never
  natOutgoing: true
  nodeSelector: all()
  vxlanMode: Always
```

## `BlockSize`

In Calico IPAM, `IPPool` is subdivided into Blocks, which are associated with specific nodes in the cluster.
Each node in a cluster can have one or more Blocks associated with it. Calico automatically creates and destroys Blocks as needed when the number of nodes or Pods in a cluster increases or decreases.

The presence of a Block allows Calico to efficiently aggregate Pod addresses assigned to the same node, which will reduce the size of the routing table.
By default, Calico will assign IPs from the Block associated with a node and create new Blocks as necessary.
Calico also supports assigning IP addresses from Blocks that are not associated with the node. By default, a Block created by Calico can hold 64 addresses (mask of /26), and this number of addresses supports custom settings.

!!! note

    In the case of a large number of cluster nodes and insufficient `IPPool Cidr`, we often need to plan the size of `IPPool` and `BlockSize` in advance according to the cluster size.
    Otherwise, some nodes may not be allocated to `Block`.

    - IPv6:116-128)。`BlockSize` defaults to 26, i.e. each block has 2^(32-26) = 64 addresses. This can be controlled by `calico node env`: `CALICO_IPV4POOL_BLOCK_SIZE` (IPv4: 20-32; IPv6:116-128).

    - Calico requires that `BlockSize` must be greater than or equal to the mask of the CIDR of `IPPool`, but in a real-world environment you should ensure that each node has at least one Block.
        So the number of Blocks should be greater than or equal to the number of nodes. That is, 2^(`BLOCK_SIZE-IPPool_MASK`) >= NUM(nodes).

## Specify multiple default ippools

As the cluster expands or the number of Pods increases, the default address pool may not have enough addresses.
This can result in Pods that may not have IPs available or some nodes may not have an assignable Block.
We can do this by modifying Calico's configuration file to select an alternative `IPPool` if there are not enough IP addresses.

### Create new `IPPool`

Run the command：

```shell
cat << EOF | calicoctl apply -f -
```

Output：

```yaml
apiVersion: projectcalico.org/v3
kind: IPPool
metadata:
  name: extra-ippool
spec:
  cidr: 192.168.0.0/20
  blockSize: 26
  vxlanMode: Always
  natOutgoing: true
EOF
```

- `cidr`: IP address range can be determined by the actual environment.

- `blockSize`: The default is 26, determined by the actual cluster size. Reducing `blockSize` means more addresses in each Block, but the total number of Blocks will be reduced.
    This is suitable for scenarios where the number of nodes is small but there are more Pods on each node. Increasing `blockSize` means that there are fewer addresses in each Block, but the total number of Blocks will increase.
    This is suitable for scenarios with a large number of nodes. But in general, as long as the CIDR of `IPPool` is large enough, you can leave `blockSize` untuned (just leave the default).

- `vxlanMode`: `vxlan` mode is used for cross-subnet communication

- `natOutgoing`: whether `snat` is required for cross-`IPPool` communication

## `IPPool` fine-grained control

By default, `IPPool` is shared globally by the cluster. However. It is also possible to assign `IPPool` to specific nodes, tenants, and Pods.

### Node filtering

Match specific nodes in `IPPool` based on the `nodeSelector` field, and only specific nodes can be assigned IPs from this `IPPool`.

- Label nodes

    ```shell
    kubectl label nodes node1 type=test
    ```

- Configure `nodeSelector` in `IPPool`

    Run the command：

    ```shell
    cat << EOF | calicoctl apply -f -
    ```

    ```yaml
    apiVersion: projectcalico.org/v3
    kind: IPPool
    metadata:
      name: extra-ippool
    spec:
      cidr: 192.168.0.0/20
      blockSize: 26
      vxlanMode: Always
      natOutgoing: true
      nodeSelector: type=="test"
    EOF
    ```

However, this `IPPool` does not affect Pods already created by this node, and to update its Pod to assign addresses from this `IPPool`, you need to `recreate pod`.
Learn more about [advanced selector syntax](https://projectcalico.docs.tigera.io/reference/resources/ippool).

### Tenant filtering

Pods under the namespace can be assigned IPs from the `ippool` corresponding to this label by typing a specific annotation in the namespace.

To add an annotation to the namespace, edit the namespace and add the following key-value pair to the annotation:

```shell
kubectl annotate namespace test-ns "cni.projectcalico.org/ipv4pools"='["extra-ippool"]'
```

Value is a list of names for `ippool`. If it is ipv6, then the key is: `cni.projectcalico.org/ipv6pools`.

!!! note
    
    This action only ensures that Pods under this namespace will be assigned IPs from `extra-ippools`.
    However, Pods in other namespaces can still assign IPs from `extra-ippools`.

### Pod filtering

Pods can be assigned addresses from an `ippool` by specifying the `ippool` in the Annotation of the Pod.

```shell
kubectl annotate pod test-pod "cni.projectcalico.org/ipv4pools"='["extra-ippool"]'
```

## Change `BlockSize`

> Before installing Calico, you should define `blockSize` beforehand. Because the value of `BlockSize` cannot be edited after installation.
Therefore, it is recommended to change the size of the IPPool block before installation to minimize disruptions to Pod connections.

How to change `BlockSize`:

1. Create a temporary `ippool`

    ```yaml
    apiVersion: projectcalico.org/v3
    kind: IPPool
    metadata:
      name: temporary-pool
    spec:
      cidr: 10.0.0.0/16
      ipipMode: Always
      natOutgoing: true
    ```

    !!! note
    
        Be careful not to conflict with the existing `ippool` subnet.

2. Set `default-ipv4-ippool` to `disable`

    ```shell
    calicoctl patch ippool default-ipv4-ippool -p '{"spec": {"disabled": true}}'
    ```

    `default-ipv4-ippool` is the name of the ippool to be modified.

3. Check the status of `ippool`

    Run the command：

    ```shell
    $ calicoctl get ippool -o wide
    NAME                  CIDR             NAT    IPIPMODE   DISABLED
    default-ipv4-ippool   192.168.0.0/16   true   Always     true
    temporary-pool        10.0.0.0/16      true   Always     false
    ```

    `default-ipv4-ippool` is `DISABLED`. Newly created Pods will not be assigned addresses from this `ippool`.

4. Delete all previous Pods

    !!! note
    
        This step needs to delete all Pods under `default-ipv4-ippool`, so the connectivity of Pods will be temporarily interrupted, please do this operation at the right time.

    To delete all Pods under default namespace.

    ```shell
    kubectl delete po --all
    ```

    Wait for the Pod rebuild to complete and the Pod will use the ``temporary-pool`` address.

5. Delete `default-ipv4-ippool`

    ```shell
    calicoctl delete ippool default-ipv4-ippool
    ```

6. Recreate `default-ipv4-ippool` and change `cidr` or `blockSize`

    Run the command：

    ```shell
    calicoctl create -f -<<EOF
    ```

    ```yaml
    apiVersion: projectcalico.org/v3
    kind: IPPool
    metadata:
      name: default-ipv4-ippool
    spec:
      blockSize: 27   # change blockSize from 26 to 27
      cidr: 192.0.0.0/16
      ipipMode: Always
      natOutgoing: true
    EOF
    ```

    !!! note
    
        `cidr` and `blockSize` can be modified as appropriate.

7. Disable `temporary-pool`

    ```shell
    calicoctl patch ippool temporary-pool -p '{"spec": {"disabled": true}}'
    ```

8. Recreate all pods

    Delete all Pods under default namespace.

    ```shell
    kubectl delete po --all
    ```

    Wait for the Pod rebuild to complete and the Pod will use the ``default-ipv4-ippool`` address.

9. Delete temporary-pool

## Migrate `IPPool`

The original address pool is running low on IP addresses and needs to be migrated to a new `IPPOOL`.

!!! note

    If the old IP pool is deleted before the new one is created and verified, the connectivity of the existing Pod will be affected. When the Pod is deleted, the service may be disrupted.

How to migrate `IPPool`：

1. Create a new `ippool`

!!! note

    It is recommended that the new `ippool` be in the CIDR of the Kubernetes cluster. If Pod IPs are assigned from outside the Kubernetes cluster CIDR, NAT may be applied unnecessarily to some traffic, resulting in unexpected behavior. 2.

2. Disable the old ``ippool`

    ```shell
    calicoctl patch ippool default-ipv4-ippool -p '{"spec": {"disabled": true}}' # Assume default-ipv4-ippool is the old IPPool
    ```''

3. Recreate all Pods under the old IP pool

    The goal is to have all Pods assigned addresses from the new `IPPool`.

4. Verify

    Start a new Pod, and see if the IPs are assigned from the new pool and test the connectivity.

5. Delete the old `ippool`.

## Q&A

- Do different `ippool`s support overlapping subnets?

    No. When creating an `ippool`, Calico checks if the `cidr` of the `ippool` is subnetted with an existing `ippool`.

- Can `BlockSize` be modified after `ippool` is created?

    No, it cannot be modified. After `ippool` is created, all `blocks` of the cluster have been created based on CIDR and `BlockSize`. So it is not effective to modify `BlockSize` manually.
