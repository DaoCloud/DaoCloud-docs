# Upgrade Notes

This page outlines important considerations when upgrading your Microservices Engine (Skoala) to a new version.

## Upgrading from v0.52.0 (or earlier) to v0.52.1

In Skoala v0.52.1, the AI Gateway Higress has been upgraded to v2.1.9, and its CRDs have changed.  
After the upgrade, please **manually update the CRDs** in the target cluster by following the steps below.

### Prerequisites

- The addon package has been updated to the latest version.

### Steps

1. Go to **Container Management** -> **Helm Apps** -> **Helm Templates** , find the **skoala-init** plugin in the plugin list, select the version 0.52.1, and download it locally.  
2. Extract the downloaded chart package locally, navigate to the `/charts/contour-provisioner/crds` directory, locate the `higress.gen.yaml` file, and copy the CRD content.  
3. In the cluster where `skoala-init` has been upgraded, run the following command to update the Higress CRDs in the target cluster.

```shell
kubectl apply -f - <<EOF
# your-CRD
EOF
```
