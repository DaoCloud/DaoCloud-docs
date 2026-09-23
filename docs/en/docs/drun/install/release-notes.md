# d.run AI Installer Release Notes

This page lists the Release Notes of the d.run AI installer, so that you can
understand the evolution path and feature changes of each version.

## 2026-08-31

### v0.44.0

- **Added** support for the basic framework of GitOps mode deployment
- **Added** support for minimal deployment of components in GitOps mode
- **Fixed** the serial detection issue of the Bootstrap Node image #3447
- **Fixed** the issue of the helm rollback process hanging #3461

## 2026-07-31

### v0.43.0

- **Added** support for the clean capability of offline images
- **Added** the agentclaw component to the installer
- **Improved** in MetalLB load balancing mode, ES and Kafka reuse insightVip for external exposure instead of falling back to node IPs
- **Fixed** the OCI index parsing failure and missed image collection when importing images by script

## 2026-06-30

### v0.42.0

- **Added** support for generating manifest configurations in Token Factory mode
- **Added** support for parsing the mgr image tag from the deployment
- **Improved** kube_version updated to v1.35.5
- **Improved** support for RHEL10 offline os package dependencies
- **Fixed** the offline conversion issue of the argocd image
