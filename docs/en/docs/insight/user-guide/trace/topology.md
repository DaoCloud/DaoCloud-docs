# Service Topology

Service topology is a visual representation of the connections, communication, and dependencies between services. It provides insights into the service-to-service interactions, allowing you to view the calls and performance of services within a specified time range. The connections between nodes in the topology represent the existence of service-to-service calls during the queried time period.

## Prerequisites

1. Insight Agent is [installed](../../quickstart/install/install-agent.md) in the cluster and the applications are in the __Running__ state.
2. Services have been instrumented for distributed tracing using
   [Operator](../../quickstart/otel/operator.md) or [OpenTelemetry SDK](../../quickstart/otel/golang.md).

## Steps

1. Go to the __Insight__ product module.

2. Select __Distributed Tracing > Service Topology__ from the left navigation pane.

3. In the topology graph, you can perform the following actions:

    - Click a node to slide out the details of the service on the right side. Here,
      you can view metrics such as request latency, throughput, and error rate for the service.
      Clicking on the service name takes you to the service details page.
    - Hover over the connections to view the traffic metrics between the two services.
    - In the "Display Settings" module, you can configure the display elements in the topology graph.
