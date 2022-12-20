# Insight Release Notes

This page lists the Release Notes of Insight Observability, so that you can understand the evolution path and feature changes of each version.

## v0.12.0

Release date: 2022.11.28

### Optimization
- **Add** insight-agent Helm template installation supports form
- **Optimized** PromQL queries support raw metrics
- **Optimize** the style of the topology map
- **Upgrade** Built-in MySQL image version, upgraded from v5.7.34 to v8.0.29.
- **Upgrade** Fluentbit ARM architecture helm Chart version from
- **Upgrade** kube-prometheus-stack helm Chart version upgraded from v39.6.0 to v41.9.1
- **Update** Bitnami mirrors used, including: grafana-operator, grafana, kubernetes-event-exporter
- **Update** the API proxy address related to prometheus, change /prometheus to /apis/insight.io/prometheus

### Bugfixes

- **FIX** service list caching logic
- **Fix** the problem that the built-in rules do not take effect
- **FIX** request delay unit issue
- **Fix** Insight internal link issue
- **Disable** PSP resource in vm-stack
- **Fix** victoriaMetrics operator not available in Kubernetes 1.25.
- **Fix** browser compatibility issues with front-end mirroring

## v0.11

Release date: 2022-11-21

### Optimization

- **Added** link troubleshooting and monitoring dashboard for component `Jaeger`
- **Optimized** The alarm list and message template list support sorting
- **optimized** to filter out clusters without `insight-agent` installed
- **Optimize** sort by span start time by default when link query

### Bugfixes

- Fix `dashboard` with no data, including OpenTelemetry related dashboards
- Fix the problem that there is no content under some log paths
- Remove wrong alarm rule: KubeletPodStartUpLatencyHigh

### other

- `victoria-metrics-k8s-stack` helm chart updated to v0.12.6
- `opentelemetry-collector` helm chart upgraded from v0.23.0 to v0.37.2
- `jaeger` helm chart upgraded from v0.57.0 to v0.62.1
- `fluentbit` helm chart upgraded from v0.20.9 to v1.9.9
- `kubernetes-event-exporter` helm chart upgraded from v1.4.21 to v2.0.0

## v0.10

Release date: 2022-10-20

### Features

- Support for container-managed Service names associated with OTel service names to discern if service linking is enabled
- Support kpanda service name associated with the otel service name, identify whether the service tracing enabled.
- Updated the default tracking sample strategy in the global OTel column
- Update default tracing sample policies in global otel col.
- Change sumo (for audit logs) exporter port 8080 to 80
- Change sumologic (work for audit log) exporter port 8080 to 80.
- Use go-migrate to manage database migration versions
- Use go-migrate to manage db migration version.
- Fix multi-cluster and multi-namespace filters not working properly in graph API
- Fix multi cluster and multi namespaces filter not work well in graph API.
- Support for building ARM images
- Support build arm image.

### Install

- Fluentbit supports docker and containerd log parsers
- Fluentbit support parser both docker and containerd log.
- Fix var/log/UTC issues
- Fix var/log/UTC issue.
- Fluentbit supports elasticsearch output to skip TLS verification
- Fluentbit support elasticsearch output skip verify TLS.
- K8s audit log filter supports getting rules from Helm values
-kube audit log filter support getting rule from helm values.
- Fix the parsing problem of centos7/ubuntu20 host log time
- Fix parse centos7/ubuntu20 host log time.
- Upgrade the OTel Operator version and remove the cert-manager dependency deployed with the self-signed certificate in the Operator
- Bump up otel operator version, remove cert-manager dependencies in operator deploy within self-signed cert.
- Designed jaeger collector indicators
- Scrape jaeger collector metrics.
- Upgrade tailing-sidecar version
- Bump up tailing-sidecar version.
- Jaeger supports elasticsearch output to skip TLS verification
- Jaeger support elasticsearch output skip verify TLS.
- Disable jaeger components in A-mode
- Disable jaeger components in Mode A.

### other

- Added OTel collector grafana dashboard
- Add otel collector grafana dashboard.
- Add Insight overview Chinese page
- Add Insight Overview Chinese version.

## v0.9

Date: 2022-9-25

### Features

- Support kpanda service name associated with the otel service name, identify whether the service tracing enabled.
- Update default tracing sample policies in global otel col.
- Change sumologic(work for audit log) exporter port 8080 to 80.
- Use go-migrate to manage db migration version.
- Fix multi cluster and multi namespaces filter not work well in graph API.
- Support build arm image.

### Installation

- Fluentbit support parser both docker and containerd log.
- Fix /var/log/ UTC issue.
- Fluentbit support elasticsearch output skip verfify TLS.
- kube audit log filter support getting rule from helm values.
- Fix parse centos7/ubuntu20 host log time.
- Bump up otel operator version, remove cert-manager dependencies in operator deploy within self-signed cert.
- Scrape jaeger collector metrics.
- Bump up tailing-sidecar version.
- Jaeger support elasticsearch output skip verfify TLS.
- Disable jaeger components in Mode A.

### Other

- Add otel collector grafana dashboard.
- Add Insight Overview Chinese version.

## v0.8

Date: 2022-8-21

### Features

- Migrate graph server into insight server.
- Add cluster_name param to graph query request.
- Add userinfo api.
- Add GetREDMetrics API in GraphQueryService.
- Add GetHelmInstallConfig api to get global cluster service addresses for agent to use.
- Complete auth module.
- Add init cmd/initcontainer for elasticsearch alias and ilm policy

### Architecture

- Bump up otel operator in agent chart.
- Add kibana as builtin tools.
- Reduce traces/logs chart's default values.
- Add Helm values parameters documentation.
- Polished Helm parameters.

### Installation

- Add audit log enable/disable feature.
- Move Fluentbit config to a ConfigMap.

## v0.7

Date: 2022-7-20

### Breaking Changes

- Modify QueryOperations and GetServiceApdex's API definition in Tracing service.
- Remove resolve alert api.
- fix NFD master crash when CRDs missed.

### Features

- Remove jaeger relate code in span-metric.
- Add index policy for skoala gateway logs.
- Add lua filter for Ghippo audit logs.
- Add global config api.
- Disable cache in vmselect component.
- Dock with ghippo roles.
- Expose metric `insight_cluster_info` in server.
- Add log.SearchLog API for SKoala, accept ES query DSL and return raw ES response.
- Bump up OTelcol helm chart version to 0.21.1 and update otelcol architecture.
- support mspider tracing.
- Bump up OTelcol helm chart version to 0.23.0.
- Add default tracing sample policies in global otel col.

### Architecture

- Use GrafanaOperator Stack to replace original Grafana Stack.
- Replace insight-overview dashboard.
- Add GrafanaDashboard, GrafanaDatasource CRDs.

## v0.6

Date: 2022-6-23

### Breaking Changes

- Modify insight deployment and service name to insight-server.
- Modify trace relate metric query API response type.
- Using the unified paging mechanism

### Features

- Add graph api through prometheus metrics of mesh layer.
- Add service graph api through prometheus metrics of general layer.
- Modify proto param, follow google style doc[https://developers.google.com/protocol-buffers/docs/style].
- Modify list api pagination and add sort.
- Add GProductVersion cr.
- Add insight metric config api.
- Manager insight license resource cr.
- Add traces api through access jaeger grpc endpoint with otlp/v2 protocol.
- Add service-detail api to get all metrics and scalars for a given service name.
- Add operation-detail api to get all metrics and scalars group by operation for a given service name.
- Add traces api through access jaeger grpc endpoint with jaeger v1 protocol.
- Add span metric protobuf style check

### Architecture

- Add node-feature-discovery subchart for License module.
- Add opentelemetry-collector subcharts to insight chart.
- Delete audit log OUTPUT config in fluent-bit.
- Add groupbytrace processor to generate trace/span number metrics.
- Add built-in Elasticsearch chart and enabled by default.

### Installation

- Upgrade victoria-metrics-k8s-stack chart version from 0.6.5 to 0.9.3.
- Add servicemonitor for components in victoria-metrics-k8s-stack.
- Modify insight components resource.

## v0.5

Date: 2022-5-18

### Features

- Add notification template API
- Complete rules and alerts API
- Add service API
- Add, delete, modify and check for vmrules
- Removed get query log API
- Support collecting kube audit logs with fluentbit
- Provide the function-related API of Service Graph
- Enhanced span_metric API: latencies, calls, errors three APIs support instance dimension query
- Enhanced span_metric API: Query Latency(with GroupByOperation) can return P99 P95 P90
- Enhanced span_metric API: latencies, calls, errors three APIs support extension_filters dimension query
- Added aggregated API for query latency, calls and errors
- Added apdex API
- Rename span_metric API URL

### Installation

- Added built-in mysql
- Upgrade GO version to 1.17
- Changed insight server service port from 8000 to 80
- Changed insight server/metrics port from 2022 to 81

### Documentation

- Added documentation station glossary
- Added 4 pages of basic concept tasks and examples, data model, query language, etc. of the document station
- Added user guides - documents such as scene monitoring, data query, alarm center, etc.
- Added to the document site: [Product Advantage](../03ProductBrief/benefits.md), [Metric Query](../06UserGuide/04dataquery/metricquery.md), [Link Query](../06UserGuide/04dataquery /tracequery.md), Dashboard, [Overview](../06UserGuide/overview.md)

## v0.4

Date: 2022-4-22

### Features

- Increase the main API of the alarm notification module
- Upgrade and adapt kpanda 0.4.x API
- Add the path information of the file to which the log belongs to the system log
- Add query single log context API
- Add query Kubernetes Event API
- Enhance Insight's own observability capabilities, provide its own indicator interface and query link information
- The API of Jaeger Query is used by the front end through the reverse proxy
- Add Query Tracing Operations related API
- Add Span Metric related API

### test

- Added E2E use case coverage badge
- Supplementary test case documents related to alarm notification
- Increase the E2E test of the log-related interface

### Documentation

- Add overall bilingual document station structure and main content
- Add plugins required for documents, optimize rendering
- Completion of ROADMAP content
- Merge document ROADMAP content into total ROADMAP file
- Update document structure

## v0.3

Date: 2022-3-18

### Features

- gRPC and http use the same port
- Modify api path from /api/insight/ to /api/insight.io/
- Add cluster resource api proxy from kpanda
- ginkgo upgrade from 1.x to 2.x
- Organize proto files under /api
- split insight service in insight.proto
- Update kpanda api to 0.3.41
- Complete cluster/namespace list and cluster summary
- Add bulk query immediate and range metrics api
- add node and all workload api
- Added Otel tracing to track insight
- Support for metrics queries with extraLabels
- Add metrics documentation.
- Realize basic scenario cases in monitor

### Helm Charts

- Add Jaeger helm chart
- Add OpenTelemetry collector helm chart
- Add tailing-sidecar-operator as an accessory/solution/plugin for log collection
- Add /variables/log/message collection in fluentbit
- Add kube exporter to collecot kube cluster event log