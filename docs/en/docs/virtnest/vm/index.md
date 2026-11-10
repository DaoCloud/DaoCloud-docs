# Manage Virtual Machines

After a virtual machine is created, you can handle day-to-day operations on the same platform: secret configuration, snapshots and cloning, migration and drift, networking and storage changes, monitoring and health checks. This page groups the VM management documentation by task so you can jump directly to what you need.

## Documentation Index

| Category | Document | Description |
| --- | --- | --- |
| **Configuration & Security** | [Create Secret](create-secret.md) | Create a Secret for S3 authentication when object storage is used as the image source |
| **Snapshots & Cloning** | [Snapshot Management](snapshot.md) | Create VM snapshots and restore a VM from a snapshot |
| **Snapshots & Cloning** | [Scheduled Snapshot](scheduled-snapshot.md) | Create snapshots automatically on a schedule |
| **Snapshots & Cloning** | [Clone a Virtual Machine](clone.md) | Clone an existing VM into a new virtual machine |
| **Migration & Drift** | [Live Migration](live-migration.md) | Move a running VM to another node |
| **Migration & Drift** | [Cold Migration within a Cluster](migratiom.md) | Move a powered-off VM between nodes in the same cluster |
| **Migration & Drift** | [Migrate VM across Clusters](cross-cluster-migrate.md) | Migrate VMs between clusters by following the CLI steps; no UI is available yet |
| **Migration & Drift** | [Automatic VM Drifting](auto-migrate.md) | Automatically move VMs off a node after a power or network failure |
| **Networking & Storage** | [Virtual Machine Networking](vm-network.md) | Configure network mode, multiple NICs and fixed IPs when creating a VM |
| **Networking & Storage** | [Storage for Virtual Machine](vm-sc.md) | Configure system disks, data disks and storage classes when creating a VM |
| **Monitoring & Health** | [Virtual Machine Monitoring](monitor.md) | Per-VM dashboards based on the KubeVirt Grafana dashboard |
| **Monitoring & Health** | [Health Check](health-check.md) | Configure Liveness and Readiness probes through YAML |

## Related Documentation

<div class="grid cards" markdown>

-   :material-view-grid-outline:{ .lg .middle } __Feature Overview__

    ---

    See all operations supported by virtual machines and the VM state required for each one.

    [:arrow_forward: Virtual Machine Features](../intro/features.md)

-   :material-cube-outline:{ .lg .middle } __Create a Virtual Machine__

    ---

    Create VMs from an image, a template or YAML, and configure networking and storage.

    [:arrow_forward: Quick Start](../quickstart/index.md)

-   :material-monitor-eye:{ .lg .middle } __Connect to a Virtual Machine__

    ---

    Log in via VNC / terminal and view VM details and monitoring data.

    [:arrow_forward: Access Virtual Machines](../quickstart/access.md)

</div>

[Download Center](https://docs.daocloud.io/en/download/){ .md-button }
[Learn about d.run Token Factory](https://docs.daocloud.io/en/tf/){ .md-button }
[Learn about d.run AI OS](https://docs.daocloud.io/en/drun/){ .md-button }
