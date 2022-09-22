# Benefits of Observability

- Multi-cluster Management

    Through the unified storage of metrics, logs and traces data in the Global clusters, the monitoring of multi-cluster can be realized and users can aggregate query of multi-cluster data.

- Out-of-the-box

    - Dashboard: Observability provides a variety of out-of-the-box prefabricated monitoring dashboards. You can comprehensively monitor clusters, nodes, workloads and other components through the built-in dashboards.

    - Alert rules: Observability provides built-in alarm rules that enable you to monitor cluster resources, system components, and other basic metrics out of the box without configuration.

- High Availability

    - Lightweight agent, which supports for one-click installation with Helm.

    - The data storage component supports multiple replicas to guarantee the high availability of your data.

- Open Source

    - Compatible with Prometheus and supporting for the native PromQL to query metrics.
    - Compatible with Prometheus YAML to collect profiles and suitable for customizing the `ServiceMonitor` rule in a Kubernetes cluster.
    - Follow the OpenTelemetry specification and support for data access with the Jaeger's link.
