# Resource Quota

Cluster administrators can use [`ResourceQuota`](./quota.md) and `LimitRange` to constrain the amount of computing resources used in a project. This helps cluster administrators to better manage and allocate resources to ensure that project teams do not abuse resources.

Resource quotas are defined via `ResourceQuota` and constrain the maximum aggregate amount of resources per named namespace or workspace. They restrict the maximum number of objects that can be created within a namespace as well as the total amount of computational resources that can be consumed in the namespace.

Limits are defined via `LimitRange` and function as a security policy that constrains the amount of resources (limit and request) that can be assigned for every applicable object type in a named namespace.

In DCE 5.0, `LimitRange` provides the following resource limits:

- Minimum and maximum resource amounts that can be used by each pod or container in the namespace.
- Minimum and maximum storage requests that can be used by each PersistentVolumeClaim in the namespace.
- Ratios between resource requests and limits in the namespace.
- Default request/limit settings for computational resources in the namespace that are automatically injected into containers at runtime.
