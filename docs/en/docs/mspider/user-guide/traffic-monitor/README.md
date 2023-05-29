---
hide:
  - toc
---

# Traffic monitoring

The traffic monitoring chart uses Istio's native grafana chart, and currently uses the following four chart sections:

- mesh global monitoring: Statistics of various mesh resources

- mesh performance monitoring: mesh control plane and data plane component performance display, and performance statistics based on component versions

- Service monitoring: All service performance statistics information injected into the sidecar in the mesh, and provide multiple filtering methods, users can filter and display content from multiple latitudes such as namespace, request source, and service version

- Workload monitoring: performance statistics of all workloads injected into the sidecar in the mesh, and provide multiple filtering methods. Users can filter and display content from multiple latitudes such as namespace, service, request source, and service version