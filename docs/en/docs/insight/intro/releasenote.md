# Insight Release Notes

This page lists the Release Notes of Insight Observability, so that you can understand the evolution path and feature changes of each version.

## 2023.04.04

### v0.15.4

#### Optimization

- **Optimization** Update the default number of primary shards for ES index to match the default number of ES nodes in the middleware.
- **Optimization** Modify the JVM information API response body structure.

#### fix

- **FIX** Fix multiple trigger alarm logging
- **Fix** Fluentbit CVE-2021-46848, upgrade from 2.0.5 to 2.0.8
- **FIX** task to check license resources
- **FIX** SQL statement to clear alert history
- **Fix** the Chinese problem in the English dashboard

## 2023.03.30

### v0.15.1

#### New

- **NEW** JVM indicator collection and integrated monitoring panel
- **NEW** Link Access Guidance
- **NEW** service topology supports error rate and request delay filtering
- **NEW** link supports Trace ID search
- **Add** Prometheus component to enable automatic vertical expansion

#### Optimization

- **Optimize** the style of the topology map virtual node
- **Optimized** service topology virtual node increase switch

#### fix

- **Fix** display style of pod running status
- **Fix** When the link function is not enabled, hide related configuration parameters
- **Fix** Some front-end styles do not take effect
- **Fix** collection pod indicators no data problem
- **FIXED** Unable to install insight-agent in OpenShift cluster

## 2023.02.27

### v0.14.6

#### New

- **NEW** Added a refresh button to the chart
- **New** service topology supports selecting multiple clusters and supports searching by service name
- **Add** service topology details and indicators of traffic egress and ingress
- **New** Click on the service name in the service topology details to jump to the details of the service
- **Add** list of service monitoring and indicators of traffic egress and ingress
- **New** system component monitoring list
- **NEW** CoreDNS monitoring panel
- **NEW** When installing Insight Agent, add whether to enable kubeAudit collection settings

#### Optimization

- **Optimize** filter conditions in link query and view links with Error
- **Optimized** The scatter diagram of the link query is updated to a bubble diagram
- **Optimized** reduce Prometheus's metrics retention time to 2 hours
- **Optimize** The default parameter of retentionPeriod of VMStorage is adjusted to 1 month
- **Upgrade** fluentbit helm chart version to 0.24.0
- **updated** `tailing-sidecar/operator` mirror
- **UPDATE** Global collection rule interval is 60 seconds

#### fix

- **FIXED** built-in vmcluster dashboard
- **Fix** When the link is not opened, the navigation bar cannot be loaded
- **Fix** System component jump to view details link error
- **FIXED** The quick installation/uninstallation link of the acquisition management list is wrong
- **FIXED** After advanced index query query, the overlapping part of the index association and chart in the drop-down box cannot be selected
- **Fix** Allow input of decimals when modifying the storage duration of historical alarms
- **FIXED** Send multiple notifications when an alert rule generates multiple alerts
- **Fixed** `configmap-reload` mirror error for `vmalert` and `vmalertmanager`
- **FIX** fluentbit for Insight Agent on ARM architecture

## 2023.01.10

### v0.13.2

#### fix

- **Fix** the problem that `kubernetes-event-exporter` image address in insight-agent is wrong
- **FIXED** Filter alerts API by resource name

## 2023.12.30

### v0.13.1

#### fix

- **FIXED** Build offline package to add `.relok8s-images` file
- **FIX** Adjust the port name corresponding to the component `otel-collector` port in insight-agent

## 2022.12.29

### v0.13.0

#### Features

- **Add** support for modifying the storage time of historical alarms
- **NEW** Added status details of collection management components
- **NEW** built-in message template
- **Add** Chart Indicator Calculation Instructions

### Optimization

- **Optimized** log list field display
- **Optimize** the judgment logic of insight-agent
- **Upgrade** Jaeger Chart version upgraded from v0.62.1 to 0.65.1

### fix

- **Fix** Some built-in alarm rules do not take effect
- **Fix** Fix the error that the name can be duplicated when creating a rule
- **Fix** DingTalk robot ending with '-'
- **FIX** case-insensitive fuzzy search in alert rules
- **FIXED** service indicator error delay calculation is not accurate
- **FIXED** Jaeger query has `too many open files` problem
- **FIXED** es index rollover alias and cleanup strategy not working

## 2022.11.28

### v0.12

#### Features

- **Add** insight-agent Helm template installation supports form

#### Optimization

- **Optimized** PromQL queries support raw metrics
- **Optimize** the style of the topology map
- **Upgrade** Built-in MySQL image version, upgraded from v5.7.34 to v8.0.29.
- **Upgrade** Fluentbit ARM architecture helm Chart version from
- **Upgrade** kube-prometheus-stack helm Chart version upgraded from v39.6.0 to v41.9.1
- **updated** used Bitnami mirror, including grafana-operator, grafana, kubernetes-event-exporter
- **Update** prometheus-related API proxy address, change `/prometheus` to `/apis/insight.io/prometheus`

#### fix

- **FIX** service list caching logic
- **Fix** the problem that the built-in rules do not take effect
- **FIX** request delay unit issue
- **Fix** Insight internal link issue
- **Disable** PSP resource in vm-stack
- **Fix** victoriaMetrics operator not available in Kubernetes 1.25.
- **Fix** browser compatibility issues with front-end mirroring

## 2022-11-21

### v0.11

#### Optimization

- **Added** link troubleshooting and monitoring dashboard for component `Jaeger`
- **Optimized** The alarm list and message template list support sorting
- **optimized** to filter out clusters without `insight-agent` installed
- **Optimize** sort by span start time by default when link query

#### Bugfixes

- **FIX** no data `dashboard`, including OpenTelemetry related dashboards
- **Fix** the problem that there is no content under some log paths
- **Fix** delete wrong alarm rule: KubeletPodStartUpLatencyHigh

#### other

- `victoria-metrics-k8s-stack` helm chart updated to v0.12.6
- `opentelemetry-collector` helm chart upgraded from v0.23.0 to v0.37.2
- `jaeger` helm chart upgraded from v0.57.0 to v0.62.1
- `fluentbit` helm chart upgraded from v0.20.9 to v1.9.9
- `kubernetes-event-exporter` helm chart upgraded from v1.4.21 to v2.0.0

## 2022-10-20

### v0.10

#### Features

- Support for container-managed Service names associated with OTel service names to discern if service linking is enabled
- Updated the default tracking sample strategy in the global OTel column
- Change sumo (for audit logs) exporter port 8080 to 80
- Use go-migrate to manage database migration versions
- Fix multi-cluster and multi-namespace filters not working properly in graph API
- Support for building ARM images

#### Install

- Fluentbit supports docker and containerd log parsers
- Fix var/log/UTC issues
- Fluentbit supports elasticsearch output to skip TLS verification
- K8s audit log filter supports getting rules from Helm values
- Fix the parsing problem of centos7/ubuntu20 host log time
- Upgrade the OTel Operator version and remove the cert-manager dependency deployed with the self-signed certificate in the Operator
- Designed jaeger collector indicators
- Upgrade tailing-sidecar version
- Jaeger supports elasticsearch output to skip TLS verification
- Disable jaeger components in A-mode

#### other

- Added OTel collector grafana dashboard
- Add Insight overview Chinese page

## 2022-9-25

### v0.9

#### Features

- Support kpanda service name associated with the otel service name, identify whether the service tracing enabled.
- Update default tracing sample policies in global otel col.
- Change sumologic(work for audit log) exporter port 8080 to 80.
- Use go-migrate to manage db migration version.
- Fix multi cluster and multi namespaces filter not work well in graph API.
- Support build arm image.

#### Install

- Fluentbit support parser both docker and containerd log.
- Fix /var/log/ UTC issue.
- Fluentbit support elasticsearch output skip verify TLS.
-kube audit log filter support getting rule from helm values.
- Fix parse centos7/ubuntu20 host log time.
- Bump up otel operator version, remove cert-manager dependencies in operator deploy within self-signed cert.
- Scrape jaeger collector metrics.
- Bump up tailing-sidecar version.
- Jaeger support elasticsearch output skip verfify TLS.
- Disable jaeger components in Mode A.

#### Other

- Add otel collector grafana dashboard.
- Add Insight Overview Chinese version.

## 2022-8-21

### v0.8

#### Features

- Migrate graph server into insight server.
- Add cluster_name param to graph query request.
- Add userinfo api.
- Add GetREDMetrics API in GraphQueryService.
- Add GetHelmInstallConfig api to get global cluster service addresses for agent to use.
- Complete auth module.
- Add init cmd/initcontainer for elasticsearch alias and ilm policy

#### Adjustment

- Bump up otel operator in agent chart.
- Add kibana as builtin tools.
- Reduce traces/logs chart's default values.
- Add Helm values parameters documentation.
- Polished Helm parameters.

#### Install

- Add audit log enable/disable feature.
- Move Fluentbit config to a ConfigMap.

## 2022-7-20

### v0.7

#### Break changes

- Modify QueryOperations and GetServiceApdex's API definition in Tracing service.
- Remove resolve alert api.
- fix NFD master crash when CRDs missed.

#### Features

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

#### Adjustment

- Use GrafanaOperator Stack to replace original Grafana Stack.
- Replace insight-overview dashboard.
- Add GrafanaDashboard, GrafanaDatasource CRDs.

## 2022-6-23

### v0.6

#### Break changes

- Modify insight deployment and service name to insight-server.
- Modify trace relate metric query API response type.
- Using the unified paging mechanism

#### Features

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

#### Adjustment

- Add node-feature-discovery subchart for License module.
- Add opentelemetry-collector subcharts to insight chart.
- Delete audit log OUTPUT config in fluent-bit.
- Add groupbytrace processor to generate trace/span number metrics.
- Add built-in Elasticsearch chart and enabled by default.

#### Install

- Upgrade victoria-metrics-k8s-stack chart version from 0.6.5 to 0.9.3.
- Add servicemonitor for components in victoria-metrics-k8s-stack.
- Modify insight components resource.

## 2022-5-18

### v0.5

#### Features

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

#### Install

- Added built-in mysql
- Upgrade GO version to 1.17
- Changed insight server service port from 8000 to 80
- Changed insight server/metrics port from 2022 to 81

#### Documentation

- Added documentation station glossary
- Added 4 pages of basic concept tasks and examples, data model, query language, etc. of the document station
- Added user guides - documents such as scene monitoring, data query, alarm center, etc.
- New additions to the document site: [Product Benefits](../intro/benefits.md), [Metric Query](../user-guide/data-query/metric.md), [Link Query](../user-guide/data-query/trace.md), dashboard, [overview](../user-guide/overview.md)

## 2022-4-22

### v0.4

#### Features

- Increase the main API of the alarm notification module
- Upgrade and adapt kpanda 0.4.x API
- Add the path information of the file to which the log belongs to the system log
- Add query single log context API
- Add query Kubernetes Event API
- Enhance Insight's own observability capabilities, provide its own indicator interface and query link information
- The API of Jaeger Query is used by the front end through the reverse proxy
- Add Query Tracing Operations related API
- Add Span Metric related API

#### test

- Added E2E use case coverage badge
- Supplementary test case documents related to alarm notification
- Increase the E2E test of the log-related interface

#### Documentation

- Add overall bilingual document station structure and main content
- Added plug-ins required for documents to optimize rendering
- Completion of ROADMAP content
- Merge document ROADMAP content into total ROADMAP file
- Update document structure

## 2022-3-18

### v0.3

#### Features

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

#### Helm Charts

- Add Jaeger helm chart
- Add OpenTelemetry collector helm chart
- Add tailing-sidecar-operator as an accessory/solution/plugin for log collection
- Add /variables/log/message collection in fluentbit
- Add kube exporter to collecot kube cluster event log