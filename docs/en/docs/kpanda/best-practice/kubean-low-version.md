---
MTPE: windsonsea
date: 2024-01-09
---

# Deploy and Upgrade Compatible Versions of Kubean in Offline Scenarios

In order to meet the customer's demand for building Kubernetes (K8s) clusters with lower versions,
Kubean provides the capability to be compatible with lower versions and create K8s clusters with those versions.

Currently, the supported versions for self-built working clusters range from `1.26.0-v1.28`.
Please refer to the [DCE 5.0 Cluster Version Support System](./cluster-version.md) for more information.

This article will demonstrate how to deploy a K8s cluster with a lower version.

!!! note

    Node environment used in the document:

    - X86 architecture
    - CentOS 7 Linux distribution

## Prerequisites

- Prepare a management cluster where kubean resides, and the current environment has deployed the `podman`,
  `skopeo`, and `minio client` commands. If not supported, you can install the dependent components through
  the script, [Installing Prerequisite Dependencies](../install-tools.md).

- Go to [kubean](https://github.com/kubean-io/kubean) to view the released
  [artifacts](https://kubean-io.github.io/kubean/en/releases/artifacts/), and choose the specific artifact
  version based on the actual situation. The currently supported artifact versions and their corresponding
  cluster version ranges are as follows:

    | Artifact Version | Cluster Range | DCE 5.0 Support |
    | ----------- | ----------- | ------ |
    | release-2.21 | v1.23.0 ~ v1.25.6 | Supported since installer v0.14.0 |
    | release-2.22 | v1.24.0 ~ v1.26.9 | Expected to support from installer v0.15.0 |
    | release-2.23 | v1.25.0 ~ v1.27.7 | Expected to support from installer v0.16.0 |

    This article demonstrates the offline deployment of a K8s cluster with version 1.23.0 and the
    offline upgrade of a K8s cluster from version 1.23.0 to 1.24.0, so we choose the artifact `release-2.21`.

## Procedure

### Prepare the Relevant Artifacts for the Lower Version of Kubespray Release

Import the spray-job image into the registry of the offline environment.

```bash
# Assuming the registry address in the bootstrap cluster is 172.30.41.200
REGISTRY_ADDR="172.30.41.200"

# The image spray-job can use the accelerator address here, and the image address is determined based on the selected artifact version
SPRAY_IMG_ADDR="ghcr.m.daocloud.io/kubean-io/spray-job:2.21-d6f688f"

# skopeo parameters
SKOPEO_PARAMS=" --insecure-policy -a --dest-tls-verify=false --retry-times=3 "

# Online environment: Export the spray-job image of version release-2.21 and transfer it to the offline environment
skopeo copy docker://${SPRAY_IMG_ADDR} docker-archive:spray-job-2.21.tar

# Offline environment: Import the spray-job image of version release-2.21 into the bootstrap registry
skopeo copy ${SKOPEO_PARAMS} docker-archive:spray-job-2.21.tar docker://${REGISTRY_ADDR}/${SPRAY_IMG_ADDR}
```

### Create Offline Resources for the Earlier Versions of K8s

1. Prepare the manifest.yml file.

    ```bash
    cat > "manifest.yml" <<EOF
    image_arch:
      - "amd64" ## "arm64"
    kube_version: ## Fill in the cluster version according to the actual scenario
      - "v1.23.0"
      - "v1.24.0"
    EOF
    ```

2. Create the offline incremental package.

    ```bash
    # Create the data directory
    mkdir data
    # Create the offline package
    AIRGAP_IMG_ADDR="ghcr.m.daocloud.io/kubean-io/airgap-patch:2.21-d6f688f" # (1)
    podman run --rm -v $(pwd)/manifest.yml:/manifest.yml -v $(pwd)/data:/data -e ZONE=CN -e MODE=FULL ${AIRGAP_IMG_ADDR}
    ```

    1. The image spray-job can use the accelerator address here, and the image address is determined based on the selected artifact version

3. Import the offline images and binary packages for the corresponding K8s version.

    ```bash
    # Import the binaries from the data directory to the minio in the bootstrap node
    cd ./data/amd64/files/
    MINIO_ADDR="http://172.30.41.200:9000" # Replace IP with the actual repository url
    MINIO_USER=rootuser MINIO_PASS=rootpass123 ./import_files.sh ${MINIO_ADDR}
    
    # Import the images from the data directory to the image repository in the bootstrap node
    cd ./data/amd64/images/
    REGISTRY_ADDR="172.30.41.200"  ./import_images.sh # Replace IP with the actual repository url
    ```

4. Deploy the `manifest` and `localartifactset.cr.yaml` custom resources to the **management cluster where kubean resides or the Global cluster**. In this example, we use the Global cluster.

    ```bash
    # Deploy the localArtifactSet resources in the data directory
    cd ./data
    kubectl apply -f data/localartifactset.cr.yaml

    # Download the manifest resources corresponding to release-2.21
    wget https://raw.githubusercontent.com/kubean-io/kubean-manifest/main/manifests/manifest-2.21-d6f688f.yml
    
    # Deploy the manifest resources corresponding to release-2.21
    kubectl apply -f manifest-2.21-d6f688f.yml
    ```

### Deployment and Upgrade Legacy K8s Cluster

#### Deploy

1. Go to __Container Management__ and click the __Create Cluster__ button on the __Cluster List__ page.

2. Choose the `manifest` and `localartifactset.cr.yaml` custom resources deployed cluster as the `Managed` parameter. In this example, we use the Global cluster.


3. Refer to [Creating a Cluster](../user-guide/clusters/create-cluster.md) for the remaining parameters.


#### Upgrade

1. Select the newly created cluster and go to the details page.

2. Click __Cluster Operations__ in the left navigation bar, then click __Cluster Upgrade__ on the top right of the page.


3. Select the available cluster for upgrade.

