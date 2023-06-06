---
hide:
  - toc
---

# FAQs

1. **Can Istio be installed separately in the service mesh?**

    Yes, it is possible to install Istio control plane components separately on demand by the user. However, this approach is not recommended since the external mesh connection offers only the basic Istio functionalities compared to other modes.

2. **What are the available Istio component versions in the service mesh?**

    There are multiple Istio component versions that a user can select from while creating the mesh.

3. **Is it possible to upgrade Istio components in the service mesh?**

    Yes, users can perform independent upgrades of Istio components.

4. **Can sidecars injected in the mesh be upgraded?**

    Yes, hot upgrades of sidecars are supported.

5. **Can a 4th generation service mesh (DSM) be upgraded to a 5th generation service mesh?**

    It is not feasible to upgrade a 4th generation service mesh (DSM) to a 5th generation service mesh, but it is possible to connect it to the service mesh in the form of an external mesh. For optimal scalability and post-maintenance, it is recommended to adopt the reinstallation method.

6. **If different namespace sidecar injection policies and workload sidecar injection policies are set, what is the actual execution result?**

    In such a scenario, the following rules are matched in order, and if a valid rule is matched, the subsequent rules are not executed:

    - Disable sidecar injection if either one of the two is set to disabled
    - Enable sidecar injection if either one of the two is set to enabled
    - If neither is set, the mesh global sidecar injection strategy (values.sidecarInjectorWebhook.enableNamespacesByDefault) will be executed.

    For further details, please refer to [Install Sidecar](https://istio.io/latest/docs/setup/additional-setup/sidecar-injection/).

7. **What distinguishes traditional microservices from service mesh?**

    To incorporate a traditional microservice into a service mesh, it is simply necessary to inject the corresponding workload into a sidecar so that all of the mesh's capabilities, such as traffic management, security, observability, and more, can be leveraged. Due to the non-invasive nature of the mesh and varying microservice frameworks, the governance strategy of the original framework may require modification, but users need not implement these changes themselves.
