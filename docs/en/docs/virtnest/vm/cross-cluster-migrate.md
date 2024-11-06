---
MTPE: WANG0608GitHub
Date: 2024-09-27
---

# Migrate VM across Clusters

This feature currently does not have a UI, so you can follow the steps in the documentation.

## Use Cases

- A VM needs to be migrated to another cluster when the original cluster experiences a failure or performance degradation that makes the VM inaccessible.
- A VM needs to be migrated to another cluster when perform planned maintenance or upgrades on the cluster.
- A VM needs to be migrated to another cluster to match more appropriate resource configurations when the performance requirements of specific applications change and resource allocation needs to be adjusted.

## Prerequisites

Before performing migration of a VM across cluster, the following prerequisites must be met:

- Cluster network connectivity: Ensure that the network between the original cluster and the target migration cluster is accessible.
- Same storage type: The target migration cluster must support the same storage type as the original cluster. For example, if the exporting cluster uses rook-ceph-block type StorageClass, the importing cluster must also support this type.
- Enable VMExport Feature Gate in KubeVirt of the original cluster.

## Enable VMExport Feature Gate

To activate the VMExport Feature Gate, run the following command in the original cluster. You can refer to [How to activate a feature gate](https://kubevirt.io/user-guide/cluster_admin/activating_feature_gates/#how-to-activate-a-feature-gate)

```sh
kubectl edit kubevirt kubevirt -n virtnest-system
```

This command modifies the `featureGates` to include `VMExport`.

```yaml
apiVersion: kubevirt.io/v1
kind: KubeVirt
metadata:
  name: kubevirt
  namespace: virtnest-system
spec:
  configuration:
    developerConfiguration:
      featureGates:
        - DataVolumes
        - LiveMigration
        - VMExport
```

## Configure Ingress for the Original Cluster

Using Nginx Ingress as an example, configure Ingress to point to the `virt-exportproxy` Service:

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: ingress-vm-export
  namespace: virtnest-system
spec:
  tls:
    - hosts:
        - upgrade-test.com
      secretName: nginx-tls
  rules:
    - host: upgrade-test.com
      http:
        paths:
          - path: /
            pathType: Prefix
            backend:
              service:
                name: virt-exportproxy
                port:
                  number: 8443
  ingressClassName: nginx
```

## Migration Steps

1. Create a VirtualMachineExport CR.

    - If cold migration is performed while **the VM is powered off** :

        ```yaml
        apiVersion: v1
        kind: Secret
        metadata:
          name: example-token # Export Token used by the VM
          namespace: default # Namespace where the VM resides
        stringData:
          token: 1234567890ab # Export the used Token (Modifiable)
    
        ---
        apiVersion: export.kubevirt.io/v1alpha1
        kind: VirtualMachineExport
        metadata:
          name: example-export # Export name (Modifiable)
          namespace: default # Namespace where the VM resides
        spec:
          tokenSecretRef: example-token # Must match the name of the token created above
          source:
            apiGroup: "kubevirt.io"
            kind: VirtualMachine
            name: testvm # VM name
        ```

    - If hot migration is performed using a VM snapshot while the **VM is powered on** :

        ```yaml
        apiVersion: v1
        kind: Secret
        metadata:
          name: example-token # Export Token used by VM
          namespace: default # Namespace where the VM resides
        stringData:
          token: 1234567890ab # Export the used Token (Modifiable)
    
        ---
        apiVersion: export.kubevirt.io/v1alpha1
        kind: VirtualMachineExport
        metadata:
          name: export-snapshot # Export name (Modifiable)
          namespace: default # Namespace where the VM resides
        spec:
          tokenSecretRef: export-token # Must match the name of the token created above
          source:
            apiGroup: "snapshot.kubevirt.io"
            kind: VirtualMachineSnapshot
            name: export-snap-202407191524 # Name of the proper VM snapshot
        ```

2. Check if the VirtualMachineExport is ready:

    ```sh
    # Replace example-export with the name of the created VirtualMachineExport
    kubectl get VirtualMachineExport example-export -n default
    
    NAME             SOURCEKIND       SOURCENAME   PHASE
    example-export   VirtualMachine   testvm       Ready
    ```

3. Once the VirtualMachineExport is ready, export the VM YAML.

    - If **virtctl** is installed, you can use the following command to export the VM YAML:

        ```sh
        # Replace example-export with the name of the created VirtualMachineExport
        # Specify the namespace with -n
        virtctl vmexport download example-export --manifest --include-secret --output=manifest.yaml
        ```

    - If **virtctl** is not installed, you can use the following commands to export the VM YAML:

        ```sh
        # Replace example-export with the name and  namespace of the created VirtualMachineExport
        manifesturl=$(kubectl get VirtualMachineExport example-export -n default -o=jsonpath='{.status.links.internal.manifests[0].url}')
        secreturl=$(kubectl get VirtualMachineExport example-export -n default -o=jsonpath='{.status.links.internal.manifests[1].url}')
        # Replace with the secret name and namespace
        token=$(kubectl get secret example-token -n default -o=jsonpath='{.data.token}' | base64 -d)
    
        curl -H "Accept: application/yaml" -H "x-kubevirt-export-token: $token"  --insecure  $secreturl > manifest.yaml
        curl -H "Accept: application/yaml" -H "x-kubevirt-export-token: $token"  --insecure  $manifesturl >> manifest.yaml
        ```

4. Import VM.

    Copy the exported `manifest.yaml` to the target migration cluster and run the following command.(If the namespace does not exist, it need to be created in advance) :

    ```sh
    kubectl apply -f manifest.yaml
    ```
    After successfully creating a VM, you need to restart it. Once the VM is running successfully, the original VM need to be deleted in the original cluster (Do not delete the original VM if it has not started successfully).
