---
hide:
  - toc
---

# Manage Virtual Machines

After a virtual machine is created, you can handle day-to-day operations on the same platform: secret configuration, snapshots and cloning, migration and drift, networking and storage changes, monitoring and health checks. This page groups the VM management documentation by task so you can jump directly to what you need.

<div class="grid cards" markdown>

-   :one: [Configuration & Security](#vm-config)
-   :two: [Snapshots & Cloning](#vm-snapshot)
-   :three: [Migration & Drift](#vm-migration)
-   :four: [Networking & Storage](#vm-network)
-   :five: [Monitoring & Health](#vm-health)

</div>

## Configuration & Security {: #vm-config }

<div class="grid cards" markdown>

-   :material-key-outline:{ .lg .middle } __[Create Secret](create-secret.md)__

    Create a Secret for S3 authentication when object storage is used as the image source

</div>

## Snapshots & Cloning {: #vm-snapshot }

<div class="grid cards" markdown>

-   :material-content-save-move:{ .lg .middle } __[Snapshot Management](snapshot.md)__

    Create VM snapshots and restore a VM from a snapshot

-   :material-calendar-clock:{ .lg .middle } __[Scheduled Snapshot](scheduled-snapshot.md)__

    Create snapshots automatically on a schedule

-   :material-content-copy:{ .lg .middle } __[Clone a Virtual Machine](clone.md)__

    Clone an existing VM into a new virtual machine

</div>

## Migration & Drift {: #vm-migration }

<div class="grid cards" markdown>

-   :material-swap-horizontal:{ .lg .middle } __[Live Migration](live-migration.md)__

    Move a running VM to another node

-   :material-arrow-right-bold-outline:{ .lg .middle } __[Cold Migration within a Cluster](migratiom.md)__

    Move a powered-off VM between nodes in the same cluster

-   :material-transit-connection-variant:{ .lg .middle } __[Migrate VM across Clusters](cross-cluster-migrate.md)__

    Migrate VMs between clusters by following the CLI steps; no UI is available yet

-   :material-autorenew:{ .lg .middle } __[Automatic VM Drifting](auto-migrate.md)__

    Automatically move VMs off a node after a power or network failure

</div>

## Networking & Storage {: #vm-network }

<div class="grid cards" markdown>

-   :material-lan:{ .lg .middle } __[Virtual Machine Networking](vm-network.md)__

    Configure network mode, multiple NICs and fixed IPs when creating a VM

-   :material-harddisk:{ .lg .middle } __[Storage for Virtual Machine](vm-sc.md)__

    Configure system disks, data disks and storage classes when creating a VM

</div>

## Monitoring & Health {: #vm-health }

<div class="grid cards" markdown>

-   :material-chart-line:{ .lg .middle } __[Virtual Machine Monitoring](monitor.md)__

    Per-VM dashboards based on the KubeVirt Grafana dashboard

-   :material-stethoscope:{ .lg .middle } __[Health Check](health-check.md)__

    Configure Liveness and Readiness probes through YAML

</div>

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
