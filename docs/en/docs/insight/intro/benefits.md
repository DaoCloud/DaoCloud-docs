# Benefits of Insight

- Multicluster Management

    Through the unified storage of metrics, logs and traces data in the Global clusters, the monitoring of multicluster can be realized and users can aggregate query of multicluster data.

- Out-of-the-box

    - Dashboard: Insight provides a variety of out-of-the-box prefabricated monitoring dashboards. You can comprehensively monitor clusters, nodes, workloads and other components through the built-in dashboards.

    - Alert rules: Insight provides built-in alert rules that enable you to monitor cluster resources, system components, and other basic metrics out of the box without configuration.

- High Availability

    - Lightweight agent, which supports for one-click installation with Helm.

    - The data storage component supports multiple replicas to guarantee the high availability of your data.

- Open Source

    - Compatible with Prometheus and supporting for the native PromQL to query metrics.
    - Compatible with Prometheus YAML to collect profiles and suitable for customizing the __ServiceMonitor__ rule in a Kubernetes cluster.
    - Follow the OpenTelemetry specification and support for data access with the Jaeger's link.
