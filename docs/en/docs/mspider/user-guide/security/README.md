---
hide:
  - toc
---

# Security Governance

Istio provides an authorization mechanism and two authentication methods (request authentication and peer authentication),
Users can create and edit resource files in the service mesh through wizards and YAML writing.
And you can create rules for the three levels of mesh global, namespace, and workload. When the resources are successfully created, Istiod will convert them into configurations and distribute them to the sidecar agent for execution.

