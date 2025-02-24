---
hide:
  - toc
---

# Uninstalling EgressGateway

To ensure the uninstallation of `EgressGateway` does not disrupt active business applications, follow these steps carefully:

## Step 1: Check for Active EgressGateway Resources

Before uninstalling, verify that no active `EgressGateway` resources remain in the cluster.

Run the following commands to check if any `EgressClusterPolicy`, `EgressPolicy`, or `EgressGateway` objects exist:

```shell
kubectl get egressclusterpolicies.egressgateway.spidernet.io -o name | wc -l
kubectl get egresspolicies.egressgateway.spidernet.io -o name | wc -l
kubectl get egressgateways.egressgateway.spidernet.io -o name | wc -l
```

- If **all outputs are `0`**, there are no remaining resources, and you can proceed to **Step 2**.
- If any output is **greater than `0`**, continue checking the details of the remaining resources using:

```shell
kubectl get egressclusterpolicies.egressgateway.spidernet.io
kubectl get egresspolicies.egressgateway.spidernet.io -o wide
kubectl get egressgateways.egressgateway.spidernet.io
```

If you find any `EgressPolicy` resources still present, check their details:

```shell
kubectl get egresspolicies <resource-name> --namespace <resource-namespace> -o yaml
```

Example output:

```yaml
apiVersion: egressgateway.spidernet.io/v1beta1
kind: EgressPolicy
metadata:
  name: ns-policy
  namespace: default
spec:
  appliedTo:
    podSelector:
      matchLabels:
        app: mock-app
  egressGatewayName: egressgateway
status:
  eip:
    ipv4: 10.6.1.55
    ipv6: fd00::55
  node: workstation2
```

- Review the `appliedTo.podSelector` field to determine which Pods are using this policy.
- Ensure deleting the policy **will not disrupt active workloads**
- If safe, delete the policy:

```shell
kubectl delete egresspolicies <resource-name> --namespace <resource-namespace>
```

## Step 2: Locate Installed EgressGateway Instances

Run the following command to check installed `EgressGateway` Helm releases:

```shell
helm ls -A | grep -i egress
```

This will display the installed `EgressGateway` name, namespace, and version.

## Step 3: Uninstall EgressGateway

Once all dependent resources are deleted, uninstall `EgressGateway` using:

```shell
helm uninstall <egressgateway-name> --namespace <egressgateway-namespace>
```

Replace `<egressgateway-name>` and `<egressgateway-namespace>` with actual values.

💡 **Note**: Before proceeding with uninstallation, **ensure all related data is backed up** and confirm **no business impact**.

## Step 4: Resolve Stuck CRDs (if necessary)

In some cases, `EgressGateway` **Custom Resource Definitions (CRDs)**, such as `EgressTunnels`, might remain stuck in deletion.

If you experience this issue, run:

```shell
kubectl patch crd egresstunnels.egressgateway.spidernet.io -p '{"metadata":{"finalizers": []}}' --type=merge
```

This command **removes finalizers** from the CRD, allowing Kubernetes to delete it.

**⚠️ Warning**: This issue is related to the `controller-manager` behavior. The Kubernetes community is actively working on fixes.

## Conclusion

By following these steps, you can safely **uninstall EgressGateway** while ensuring minimal business disruption.
