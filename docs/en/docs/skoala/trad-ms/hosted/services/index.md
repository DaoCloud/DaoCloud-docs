# Microservice list

The micro-service list page lists all the micro-services under the current registry instance. You can view the group, health status, protection threshold, request status, link tracing, and governance status of the micro-services. You can click the micro-service name in the list to view the micro-service instance list, monitoring information, interface list, and metadata.

![](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/skoala/images/servicelist-1.png)

Group: Indicates the group of microservice configuration files. Separate configuration files and microservice instances to make it easier to apply the same configuration to different services or components.

Protection threshold: The protection threshold is a floating point number between 0 and 1, representing the minimum proportion of healthy instances in the cluster. If the proportion of the actual healthy instances is less than or equal to the threshold, threshold protection is triggered, that is, the Instance is returned to the client regardless of whether the Instance is healthy. Threshold protection is mainly to prevent all traffic from flowing into the remaining instances when there are too many faulty instances. As a result, the remaining instances will be crushed under the traffic pressure, resulting in an avalanche effect.

Link tracing: When creating a service using [Workbench](../../../../amamba/intro/index.md), you can select whether to access the [OpenTelemetry ](https://opentelemetry.io/docs/concepts/what-is-opentelemetry/) link tracing component. If the service is registered to the registry through other means, you can refer to [Use the OTel SDK to expose metrics for the application](../../../../insight/quickstart/otel/meter.md) to manually access the component. Access is recommended to obtain complete observable information.

Whether it can be governed: determine whether the micro-service meets the governance conditions, such as whether the governance plug-in is enabled, whether it is containerized, whether it is managed by the mesh, whether it is created by [Workbench](../../../../amamba/intro/index.md) and a series of requirements.
