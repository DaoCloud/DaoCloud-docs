# Link Collection Troubleshooting Guide

Before trying to troubleshoot the problem of link data collection, you need to understand the transmission path of link data. The following is a schematic diagram of link data transmission:

```mermaid
graph TB

sdk[Language problem / SDK] --> workload[Workload cluster otel collector]
--> otel[Global cluster otel collector]
--> jaeger[Global cluster jaeger collector]
--> es[Elasticsearch cluster]

classDef plain fill:#ddd,stroke:#fff,stroke-width:1px,color:#000;
classDef k8s fill: #326ce5, stroke: #fff, stroke-width: 1px, color: #fff;
classDef cluster fill:#fff,stroke:#bbb,stroke-width:1px,color:#326ce5;

class sdk,workload,otel,jaeger,es cluster
```

As shown in the figure above, if the transmission fails at any step, the link data cannot be queried. If you find no link data after applying Link Boost, follow these steps:

1. Use the DCE 5.0 platform, enter `Observability`, and select `Dashboard` in the left navigation bar.

    

2. Click on the dashboard title `Overview`.

    

3. Switch to `insight-system` -> `insight tracing debug` dashboard.

    

4. You can see that the dashboard consists of three blocks, which are responsible for monitoring the data status of different clusters and transmission links of different components. Through the generated timing chart, check whether there is any problem with the data transmission of the link.

    -workload opentelemetry collector
    -global opentelemetry collector
    -global jaeger collector

    

## Block introduction

1. **workload opentelemetry collector**

    It shows that `opentelemetry collector` of different working clusters is receiving language probe/SDK link data and sending aggregated link data. You can select the cluster you are in through the `Cluster` selection box in the upper left corner.

    

    !!! note

        According to these four timing diagrams, it can be judged whether the `opentelemetry collector` of the cluster is running normally.

2. **global opentelemetry collector**

    It shows how `opentelemetry collector` of `global service cluster` receives link data from `otel collector` in `working cluster` and sends aggregated link data.

    

    !!! note

        The `opentelemetry collector` of the `global management cluster` is also responsible for sending the [audit log](../../ghippo /04UserGuide/03AuditLog.md) and Kubernetes audit logs (not collected by default) to the `audit server` component of the global management module.
        For example, you can check whether this function is normal through the timing diagram in the lower right corner.

3. **global jaeger collector**

    Show that `jaeger collector` of `global management cluster` is receiving data from `otel collector` in `global management cluster`, and sending link data to [ElasticSearch cluster](../../middleware/elasticsearch/intro /what.md).

    