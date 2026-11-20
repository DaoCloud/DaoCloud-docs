# Create a Work Cluster - Admin

Model inference and AI training workloads run on work clusters with GPUs. This tutorial creates a work cluster in Container Management and attaches GPU nodes,
which is the foundation for deploying model services and agents.

## Prerequisites

- Several nodes are ready, running the same OS and CPU architecture. It is recommended to use an [OS supported by the installer](../install/commercial/deploy-requirements.md).
- IPv4 forwarding is enabled on the nodes, and it is recommended to disable the firewall.
- Sign in to the console with a user who has the Container Management Module Admin role.
- The GPU nodes have the corresponding graphics drivers installed. During the node check, confirm that the GPU devices can be recognized.

## Steps

1. In the left navigation bar, click **Container Management** -> **Clusters**, then click **Create Cluster** in the upper right corner.

    ![Create cluster button](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/kpanda/images/cluster-create01.png)

2. Enter the basic cluster information and click **Next**:

    - **Cluster Name**: lowercase letters, digits, and hyphens (`-`), starting and ending with a lowercase letter or digit, up to 63 characters, e.g. `drun-gpu-cluster`.
    - **Managed By**: select the cluster that manages this cluster. The default is the global service cluster.
    - **Runtime**: `containerd` is recommended.
    - **Kubernetes Version**: choose a supported version; 1.29.5 is recommended.

3. Enter the node configuration: fill in the IP and SSH credentials of the GPU nodes in the node list, then click **Node Check**.
   Continue after the check passes; if it fails, fix the node information as prompted and check again.

4. Adjust other parameters (network, storage, etc.) as needed, then click **OK** to create the cluster. The creation takes about 10–20 minutes.

    ![Node check](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/kpanda/images/cluster-create03.png)

5. After the cluster is created, check that the cluster status is **Running** in the cluster list and that the GPU nodes are ready in the node list.

## Verify

Go to the cluster details page. If the GPU nodes show **Healthy** under **Node Management**, the cluster is ready to host AI workloads.

## Next step

Continue to [Deploy a Model Service](deploy-model.md).

To integrate an existing Kubernetes cluster instead of creating a new one, see [Integrate Cluster](../kpanda/user-guide/clusters/integrate-cluster.md). For more cluster and node management features, see [Container Management](../kpanda/intro/index.md).
