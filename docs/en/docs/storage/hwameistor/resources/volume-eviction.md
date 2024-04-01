# Volume Eviction

Volume migration and eviction are important features of the HwameiStor system, ensuring the continuous and normal operation of HwameiStor in production environments.
HwameiStor migrates volumes from one node to another while ensuring that the data remains accessible.
When a Kubernetes node or application Pod is evicted for any reason, the system automatically discovers the HwameiStor volumes associated with the node or Pod and migrates them to other nodes, ensuring that the evicted Pod can be scheduled to other nodes and run normally.
In addition, operators can manually migrate volumes to balance system resources and ensure smooth operation of the system.

## Evicting a Node

In a Kubernetes system, you can use the following command to evict a node, removing and migrating the Pods running on that node to other nodes.
At the same time, the HwameiStor volumes used by the Pods are also migrated from the evicted node to other nodes, ensuring that the Pods can be scheduled and run on other nodes.

```bash
kubectl drain k8s-node-1 --ignore-daemonsets=true
```

You can use the following command to check if the associated HwameiStor volumes have been successfully migrated.

```bash
kubectl get LocalStorageNode k8s-node-1 -o yaml
```

The output will be similar to:

```yaml
apiVersion: hwameistor.io/v1alpha1
kind: LocalStorageNode
metadata:
  creationTimestamp: "2022-10-11T07:41:58Z"
  generation: 1
  name: k8s-node-1
  resourceVersion: "6402198"
  uid: c71cc6ac-566a-4e0b-8687-69679b07471f
spec:
  hostname: k8s-node-1
  storageIP: 10.6.113.22
  topogoly:
    region: default
    zone: default
status:
  ...
  pools:
    LocalStorage_PoolHDD:
      class: HDD
      disks:
      - capacityBytes: 17175674880
        devPath: /dev/sdb
        state: InUse
        type: HDD
      freeCapacityBytes: 16101933056
      freeVolumeCount: 999
      name: LocalStorage_PoolHDD
      totalCapacityBytes: 17175674880
      totalVolumeCount: 1000
      type: REGULAR
      usedCapacityBytes: 1073741824
      usedVolumeCount: 1
      volumeCapacityBytesLimit: 17175674880
      volumes: # Ensure that the volumes field is empty
  state: Ready
```

You can also use the following command to check if there are any HwameiStor volumes on the evicted node.

```bash
kubectl get localvolumereplica
```

The output will be similar to:

```console
NAME                                              CAPACITY     NODE         STATE   SYNCED   DEVICE                                                                  AGE
pvc-1427f36b-adc4-4aef-8d83-93c59064d113-957f7g   1073741824   k8s-node-3   Ready   true     /dev/LocalStorage_PoolHDD-HA/pvc-1427f36b-adc4-4aef-8d83-93c59064d113   20h
pvc-1427f36b-adc4-4aef-8d83-93c59064d113-qlpbmq   1073741824   k8s-node-2   Ready   true     /dev/LocalStorage_PoolHDD-HA/pvc-1427f36b-adc4-4aef-8d83-93c59064d113   30m
pvc-6ca4c0d4-da10-4e2e-83b2-19cbf5c5e3e4-scrxjb   1073741824   k8s-node-2   Ready   true     /dev/LocalStorage_PoolHDD/pvc-6ca4c0d4-da10-4e2e-83b2-19cbf5c5e3e4      30m
pvc-f8f017f9-eb09-4fbe-9795-a6e2d6873148-5t782b   1073741824   k8s-node-2   Ready   true     /dev/LocalStorage_PoolHDD-HA/pvc-f8f017f9-eb09-4fbe-9795-a6e2d6873148   30m
```

In some cases, when restarting a node, you may want to keep the volumes on that node. You can do this by adding the following label to the node:

```bash
kubectl label node k8s-node-1 hwameistor.io/eviction=disable
```

## Evicting a Pod

When a Kubernetes node is under heavy load, the system selectively evicts some Pods to free up system resources and ensure the normal operation of other Pods.
If a Pod that uses HwameiStor volumes is evicted, the system automatically captures this evicted Pod and migrates the associated HwameiStor volumes to other nodes, ensuring that the Pod can be scheduled and run on other nodes.

## Migrating a Pod

Operators can manually migrate application Pods and the associated HwameiStor volumes to balance system resources and ensure smooth operation of the system.
There are two ways to perform manual migration:

- Method 1

  ```bash
  kubectl label pod mysql-pod hwameistor.io/eviction=start
  kubectl delete pod mysql-pod
  ```

- Method 2

  ```console
  $ cat << EOF | kubectl apply -f -
  apiVersion: hwameistor.io/v1alpha1
  kind: LocalVolumeMigrate
  metadata:
    name: migrate-pvc-6ca4c0d4-da10-4e2e-83b2-19cbf5c5e3e4
  spec:
    sourceNode: k8s-node-1
    targetNodesSuggested: 
    - k8s-node-2
    - k8s-node-3
    volumeName: pvc-6ca4c0d4-da10-4e2e-83b2-19cbf5c5e3e4
    migrateAllVols: true
  EOF

  $ kubectl delete pod mysql-pod
  ```
