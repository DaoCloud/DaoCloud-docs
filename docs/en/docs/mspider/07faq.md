---
hide:
  - toc
---

# common problem

1. Can Istio in the service mesh be installed separately?

    Yes, but not recommended. The Istio control plane components installed separately by the user can be connected to the service grid through an external grid, but compared with other modes, it only provides basic Istio functions.

1. Istio component versions in the service mesh?

    There are several versions that the user can choose from when creating the grid.

1. Can the Istio of the service mesh be upgraded?

    Yes, users can upgrade independently.

1. Can the injected sidecars in the mesh be upgraded?

    Yes, it supports sidecar hot upgrade at the same time.

1. Can a 4th generation service mesh (DSM) be upgraded to a 5th generation service mesh?

    It cannot be upgraded, but it can be connected to the service grid in the form of an external grid. It is recommended to adopt the method of reinstallation to obtain the best scalability and post-maintenance.

1. If different namespace sidecar injection policies and workload sidecar injection policies are set, what is the actual execution effect?

    The following rules will be matched in order, and the following rules will not be executed if a valid rule is matched:

    - Disable sidecar injection if one of the two is set to disabled
    - Enable sidecar injection if one of the two is set to enabled
    - If neither is set, the mesh global sidecar injection strategy will be executed (values.sidecarInjectorWebhook.enableNamespacesByDefault)
    
    For details, please refer to [Install Sidecar](https://istio.io/latest/zh/docs/setup/additional-setup/sidecar-injection/)

1. What is the difference between traditional microservices and service mesh?

    Adding a traditional microservice to a service mesh simply requires injecting its corresponding workload into a sidecar so that the mesh can manage it.
    Based on different microservice frameworks and the non-invasive nature of the grid, the governance strategy of the original framework may be changed, but users do not need to implement it themselves.
    After accessing the grid, traditional microservices can obtain all the capabilities of the grid, including traffic management, security, observability, and so on.