---
hide:
  - toc
---

# Service Management

Service management displays all the services that have been injected with sidecars in the clusters under the current mesh. You can filter services based on namespaces.

![Service List](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/mspider/images/servicelist01.png)

The service mesh aggregates services in each cluster. Services with the same name in the same namespace are aggregated into one service. This facilitates unified traffic management for cross-cluster collaborative services.

The __Service Management__ performs __Diagnostic Configuration__ checks on the status of services in the list. The results and their meanings are as follows:

- Normal: All pods of the service in each cluster have been injected with sidecars, and all settings are identical.
- Warning: Some pods of the workloads under this service have not been injected with sidecars.
- Abnormal: The service will be displayed as __Abnormal__ if any of the following problems exist:

    - None of the pods have been injected with sidecars.
	  - The port settings of the service are inconsistent across clusters.
	  - The workload selector labels of the service are inconsistent across clusters.
	  - The access methods of the service are inconsistent across clusters.

!!! note

    It is recommended to ensure that services with the same name in different clusters have identical configurations; otherwise, some workloads may not function properly.

The service list also indicates services from other microservice registries.

![other microservice registries](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/mspider/images/servicelist02.png)

You can click a service name to enter the details page and view specific information such as service addresses and ports in each cluster. You can also modify the communication protocol in the __Address__ tab.

![Address](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/mspider/images/servicelist03.png)

Pay special attention to the __Diagnostic Configuration__ column in the service list. When the diagnostic information is __Abnormal__ , hovering over the __ⓘ__ will display the reason for the abnormality. Abnormal status will affect mesh-related capabilities such as traffic management in the next phase.

![Abnormal Prompt](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/mspider/images/servicelist04.png)

On the right side of the service list, click __⋮__ and select the corresponding menu item to navigate to traffic management and security governance.

![Menu Items](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/mspider/images/servicelist05.png)

For information on how to create and configure services, please refer to [Create Services](../../../kpanda/user-guide/network/create-services.md).
