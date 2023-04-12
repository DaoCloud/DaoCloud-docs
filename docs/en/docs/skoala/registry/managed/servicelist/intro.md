# list of microservices

The microservice list page lists all microservices under the current registry instance, and you can view the grouping, health status, protection threshold, request status, link tracking, and governance status of microservices. After clicking the microservice name in the list, you can further view the microservice instance list, monitoring information, interface list, metadata, etc.



Grouping: refers to the configuration file grouping of microservices. Separating configuration files and microservice instances from each other makes it easy to apply the same configuration to different services or components.

Protection Threshold: The protection threshold is a floating-point number between 0 and 1, indicating the minimum value of the proportion of healthy instances in the cluster. If the proportion of actual healthy instances is less than or equal to the threshold, threshold protection will be triggered, that is, whether the instance (Instance) is healthy or not, the instance (Instance) will be returned to the client. Threshold protection is mainly to prevent all traffic from flowing into the remaining instances when there are too many faulty instances, causing traffic pressure to overwhelm the remaining instances and form an avalanche effect.

Link Tracking: When creating a service through [Application Workbench](../../../../amamba/intro/WhatisAmamba.md), you can choose whether to access [OpenTelemetry](https://opentelemetry. io/docs/concepts/what-is-opentelemetry/) link tracing component. If the service is registered to the registration center through other means, you can refer to [Using OTel SDK to expose indicators for applications](../../../../insight/user-guide/01quickstart/otel/meter.md) Plug in the component manually. Access is recommended to obtain complete observable information.

Whether it can be governed: Determine whether the microservice meets the governance conditions, such as whether the governance plug-in is enabled, whether it is containerized, whether it is managed by the mesh, whether it is passed through [Application Workbench](../../../ ../amamba/01ProductBrief/WhatisAmamba.md) created a series of requirements such as <!--Detailed requirements to be improved later-->.