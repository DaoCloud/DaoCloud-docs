---
MTPE: windsonsea
date: 2024-05-10
hide:
  - toc
---

# Control Plane Components

This page lists the various components in the control plane of the service mesh along with their locations, descriptions, and default resource settings.

<table>
    <tr>
        <th>Component Name</th>
        <th>Location</th>
        <th>Description</th>
        <th>Default Resource Settings</th>
    </tr>
    <tr>
        <td>mspider-ui</td>
        <td>Global Management Cluster</td>
        <td>Service Mesh Interface</td>
        <td>
            <ul>
                <li>requests: CPU: Not set; Memory: Not set</li>
                <li>limits: CPU: Not set; Memory: Not set</li>
            </ul>
        </td>
    </tr>
    <tr>
        <td>mspider-ckube</td>
        <td>Global Management Cluster</td>
        <td>Accelerator component for Kubernetes API Server, used to call resources related to the global cluster</td>
        <td>
            <ul>
                <li>requests: CPU: Not set; Memory: Not set</li>
                <li>limits: CPU: Not set; Memory: Not set</li>
            </ul>
        </td>
    </tr>
    <tr>
        <td>mspider-ckube-remote</td>
        <td>Global Management Cluster</td>
        <td>Used to call remote Kubernetes clusters, aggregate multi-cluster resources, and accelerate</td>
        <td>
            <ul>
                <li>requests: CPU: Not set; Memory: Not set</li>
                <li>limits: CPU: Not set; Memory: Not set</li>
            </ul>
        </td>
    </tr>
    <tr>
        <td>mspider-gsc-controller</td>
        <td>Global Management Cluster</td>
        <td>Service mesh management component for mesh creation, mesh configuration, and mesh control plane lifecycle management, as well as permissions management and other Mspider control plane capabilities</td>
        <td>
            <ul>
                <li>requests: CPU: Not set; Memory: Not set</li>
                <li>limits: CPU: Not set; Memory: Not set</li>
            </ul>
        </td>
    </tr>
    <tr>
        <td>mspider-api-service</td>
        <td>Global Management Cluster</td>
        <td>Provides interfaces for Mspider backend API interactions and control behaviors</td>
        <td>
            <ul>
                <li>requests: CPU: Not set; Memory: Not set</li>
                <li>limits: CPU: Not set; Memory: Not set</li>
            </ul>
        </td>
    </tr>
    <tr>
        <td>Hosted Mesh</td>
        <td></td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>istiod-{meshID}-hosted</td>
        <td>Control Plane Cluster</td>
        <td>Used for hosted mesh policy management</td>
        <td>
            <ul>
                <li>requests: CPU: 100m; Memory: 100m</li>
                <li>limits: CPU: Not set; Memory: Not set</li>
            </ul>
        </td>
    </tr>
    <tr>
        <td>mspider-mcpc-ckube-remote</td>
        <td>Control Plane Cluster</td>
        <td>Call remote mesh working clusters, accelerate, and aggregate multi-cluster resources</td>
        <td>
            <ul>
                <li>requests: CPU: 100m; Memory: 50m</li>
                <li>limits: CPU: 500m; Memory: 500m</li>
            </ul>
        </td>
    </tr>
    <tr>
        <td>mspider-mcpc-mcpc-controller</td>
        <td>Control Plane Cluster</td>
        <td>Aggregate multi-cluster data plane information</td>
        <td>
            <ul>
                <li>requests: CPU: 100m; Memory: 0</li>
                <li>limits: CPU: 300m; Memory: 1.56G</li>
            </ul>
        </td>
    </tr>
    <tr>
        <td>{meshID}-hosted-apiserver</td>
        <td>Control Plane Cluster</td>
        <td>Hosted control plane virtual cluster API Server</td>
        <td>
            <ul>
                <li>requests: CPU: Not set; Memory: Not set</li>
                <li>limits: CPU: Not set; Memory: Not set</li>
            </ul>
        </td>
    </tr>
    <tr>
        <td>{meshID}-etcd</td>
        <td>Control Plane Cluster</td>
        <td>Hosted control plane virtual cluster etcd, used for hosted mesh policy storage</td>
        <td>
            <ul>
                <li>requests: CPU: Not set; Memory: Not set</li>
                <li>limits: CPU: Not set; Memory: Not set</li>
            </ul>
        </td>
    </tr>
    <tr>
        <td>istiod</td>
        <td>Working Cluster</td>
        <td>Mainly used for sidecar lifecycle management in the local cluster</td>
        <td>
            <ul>
                <li>requests: CPU: 100; Memory: 100</li>
                <li>limits: CPU: Not set; Memory: Not set</li>
            </ul>
        </td>
    </tr>
    <tr>
        <td>Private Mesh</td>
        <td></td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>istiod</td>
        <td></td>
        <td>Used for strategy creation, deployment, and sidecar lifecycle management work</td>
        <td>
            <ul>
                <li>requests: CPU: 100; Memory: 100</li>
                <li>limits: CPU: Not set; Memory: Not set</li>
            </ul>
        </td>
    </tr>
    <tr>
        <td>mspider-mcpc-ckube-remote</td>
        <td>Working Cluster</td>
        <td>Call remote mesh working clusters</td>
        <td>
            <ul>
                <li>requests: CPU: 100m; Memory: 50m</li>
                <li>limits: CPU: 500m; Memory: 500m</li>
            </ul>
        </td>
    </tr>
    <tr>
        <td>mspider-mcpc-mcpc-controller</td>
        <td>Working Cluster</td>
        <td>Collect cluster data plane information</td>
        <td>
            <ul>
                <li>requests: CPU: 100m; Memory: 0</li>
                <li>limits: CPU: 300m; Memory: 1.56G</li>
            </ul>
        </td>
    </tr>
    <tr>
        <td>External Mesh</td>
        <td></td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>mspider-mcpc-ckube-remote</td>
        <td>Working Cluster</td>
        <td>Call remote mesh working clusters</td>
        <td>
            <ul>
                <li>requests: CPU: 100m; Memory: 50m</li>
                <li>limits: CPU: 500m; Memory: 500m</li>
            </ul>
        </td>
    </tr>
    <tr>
        <td>mspider-mcpc-mcpc-controller</td>
        <td>Working Cluster</td>
        <td>Collect cluster data plane information</td>
        <td>
            <ul>
                <li>requests: CPU: 100m; Memory: 0</li>
                <li>limits: CPU: 300m; Memory: 1.56G</li>
            </ul>
        </td>
    </tr>
</table>

These are the default resource settings for each control plane component of the service mesh.
You can customize CPU and memory resources for each workload in the
[Container Management](../../../kpanda/user-guide/workloads/create-deployment.md) module.
