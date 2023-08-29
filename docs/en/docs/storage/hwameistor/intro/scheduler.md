# Scheduler

The scheduler is one of the important components of HwameiStor. It automatically schedules Pods to the correct nodes with HwameiStor storage volumes. With the scheduler, Pods no longer have to use the NodeAffinity or NodeSelector fields to select nodes. The scheduler can handle LVM and Disk storage volumes.

## Install

The scheduler should be deployed in HA mode in the cluster, which is a best practice in production environments.

## Deploy via Helm Chart

The scheduler must be used with local disks and a local disk manager. It is recommended to install via [Helm Chart](../install/deploy-helm.md).

## Deploy via YAML (for development)

```bash
kubectl apply -f deploy/scheduler.yaml
```
