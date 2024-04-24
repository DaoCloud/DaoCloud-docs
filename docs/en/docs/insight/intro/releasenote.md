---
MTPE: windsonsea
date: 2024-02-19
---

# Insight Release Notes

This page lists the Release Notes of Insight, so that you can understand
the evolution path and feature changes of each version.

## 2024.03.31

!!! warning

    Due to breaking changes in Insight v0.25 version, when upgrading Insight Server to v0.25.x,
    Insight Agent version must also be upgraded to v0.25.x!!!

### v0.25.0

These changes are for Insight Server.

#### Improvements

- **Improved** Log correlation support for filtering based on TraceID and container groups
- **Improved** Support for encrypting sensitive information of notification objects
- **Improved** Split `insight-server` into `insight-server` and `insight-manager` components
- **Improved** High availability support for `opentelemetry-collector` component
- **Improved** Grafana and Jaeger are not accessible without login
- **Improved** Support for customizing whether to initialize log indexes during installation

#### Bug Fixes

- **Fixed** permission issues with alarm-related APIs
- **Fixed** issue with no data in overview query metrics
- **Fixed** validation issue when importing YAML for alarm policies
- **Fixed** limitation issue with Grafana access speed

## 2024.01.31

### Insight Server: v0.24.0

#### New Features

- **Added** Support for alarm suppression
- **Added** Support for alarm templates and creating alarm policies from templates

#### Improvements

- **Improved** Grafana supports adding data sources of JSON API type
- **Improved** Grafana prevents using the ECS key to exit fullscreen mode

#### Fixes

- **Fixed** Inaccurate preview queries when creating log alarms
- **Fixed** Error in listening IPv6 during insight-system deployment
- **Fixed** Issue with Grafana dashboards not being accessible without authentication
- **Fixed** Enabling InsecureSkipVerify for all SMTP emails

### Insight Agent: v0.23.0

#### Improvements

- **Improved** Upgraded image versions of related components for OpenTelemetry Collector

## 2023.12.31

### Insight Server: v0.23.0

#### New Features

- **Added** integration with network observation Deepflow Community Edition
- **Added** alert templates

#### Improvements

- **Improved** usage of DSL as the query statement for log alerts

#### Fixes

- **Fixed** an issue that topology graph does not have request latency data
- **Fixed** an issue where Insight Agent status is not updated when cluster status is abnormal
- **Fixed** an issue of missing `metadata` in the configuration file for probing
- **Fixed** inaccurate query and incorrect alert objects in the preview trend chart of log alerts
- **Fixed** duplicate occurrence of `app.kubernetes.io/name` field in Insight Server Chart

### Insight Agent: v0.23.0

#### Improvements

- **Improved** automatic injection of `k8s_namespce_name` for probe injection in distributed tracing
- **Improved** automatic generation and configuration of log indexes for each deployed Insight Agent cluster

## 2023.11.30

### Insight Server: v0.22.0

#### New Features

- **Added** support for network connectivity testing
- **Added** ability to import alert policies via YAML
- **Added** support for operation audit logging

#### Improvements

- **Improved** automatic deployment of OTel instrumentation CR during installation

#### Fixes

- **Fixed** an issue with Elasticsearch index initialization failure

### Insight Agent: v0.22.0

- **Fixed** compatibility issue with Fluentbit directory collection and DCE 4.0

## 2023.10.31

!!! note

    Insight Agent v0.21.0 has fixed the issue of collecting duplicate JVM metrics after
    configuring PodMonitor. It is recommended to upgrade to this version for the fix.
    For more details, refer to [Known Issues](../../insight/quickstart/install/knownissues.md).

### Insight Server: v0.21.0

#### New Features

- **Added** Namespace-level monitoring.

#### Improvements

- **Improved** navigation structure in Insight.
- **Improved** a behavior of clicking on a link distribution graph allows quick access to proper link details.

#### Fixes

- **Fixed** an issue of unable to view container log context.
- **Fixed** an error when initializing event index.

### Insight Agent: v0.21.0

#### Bug Fixes

- **Fixed** an issue of abnormal span names appearing in link queries.
- **Fixed** an issue where containers started by the tailing-sidecar in
  the Bank Kirin Kylin-V10 (SP3) operating system could not start properly.

## 2023.08.31

### Insight Server: v0.20.0

#### New Features

- **Added** container event alerts
- **Added** linked query-related logs
- **Added** metadata added to event details
- **Added** support for Lucene syntax queries in logs

#### Improvements

- **Added** prompts for cluster status abnormalities
- **Improved** filtering conditions for logs
- **Improved** duplicate tags when creating silent alert conditions
- **Improved** node logs now support filtering by file path
- **Improved** built-in alerting policies for CoreDNS.

#### Bug Fixes

- **Fixed** creation time error for Elasticsearch in system components.
- **Fixed** discrepancy between the number of logs retrieved in contextual log queries and the actual count.
- **Fixed** redirection issue with repair suggestions in alerts.
- **Fixed** compatibility issues with certain data in event queries.
- **Fixed** color error in the legend of the topology graph.
- **Fixed** an issue where all nodes became external nodes in the topology diagram when canceling cluster and namespace boundaries.
- **Fixed** failure to send alerts if there is an error in the content of any notification type in the message template.

### Insight Agent: v0.20.0

#### Improvements

- **Improved** support for consuming log and linked data via Kafka

#### Bug Fixes

- **Fixed** compatibility issues with Openshift clusters
- **Fixed** compatibility issues with Kubernetes v0.18.20
- **Fixed** compatibility issues with DCE 4.0
- **Fixed** issue with abnormal metric calculations

## 2023.07.30

### v0.19.0

#### New Features

- **Added** kubernetes event analysis and query functionality.
- **Added** built-in alert policy provides suggestions for alert fixes.
- **Added** support for customizing log export fields and formats.

#### Improvements

- **Improved** logic for retrieving Elasticsearch component status in system components.
- **Improved** support for configuring whether to import default message templates in installation parameters.

#### Fixes

- **Fixed** a permissions issue for some roles when viewing alert rule details.
- **Fixed** a permissions issue for some roles when creating, editing, or previewing silent alerts.
- **Fixed** a permissions issue for some roles when viewing alert message details.
- **Fixed** time display issue in bubble chart for trace queries.
- **Fixed** an issue with missing namespace parameter when querying container logs.
- **Fixed** incorrect custom tag parameter for default variables in message templates.
- **Fixed** an issue of no new request sent when switching filter conditions.
- **Fixed** a permissions issue for creating, editing, or previewing silent alerts.
- **Fixed** an issue with log statistics value being displayed as 0 in overview.
- **Fixed** an issue with some built-in alert policies not taking effect.

## 2023.07.01

### v0.18.0

#### New Features

- **Added** log alerts.
- **Added** cluster status to collection management.
- **Added** silence conditions to the silent rule list.
- **Added** email configuration detection.
- **Added** support for PostgreSQL and Kingbase as system databases.
- **Added** Nvidia GPU monitoring dashboard.

#### Improvements

- **Updated** the legend for updating service topology.
- **Added** average value of metrics and sorting support to operation metrics in service details.
- **Added** sorting by span, latency, occurrence time, etc. to link queries.
- **Added** search functionality to the dropdown menu for notification configuration in alert policies.
- **Added** timezone formatting support to alert templates.
- **Upgraded** **opentelemetry collector** Chart version from **0.50.1** to **0.59.3** .
- **Upgraded** **opentelemetry Operator** Chart version from **0.26.1** to **0.30.1** .

#### Fixes

- **Fixed** an issue where the previewed silent alerts did not match the actual silenced alerts.
- **Fixed** an issue with incorrect component versions in system components.
- **Fixed** the error in the title of the list in the dashboard.
- **Fixed** an issue where no data was returned when previewing matching alerts while creating silence through the alert list.
- **Fixed** an issue where Fluentbit could not start for the first time in some environments.

## 2023.06.01

### v0.17.0

!!! warning

    In version v0.17.x, the kube-prometheus-stack chart version has been upgraded from 41.9.1 to 45.28.1.
    There are also some field upgrades in the used CRDs, such as the __attachMetadata__ field of servicemonitor.
    Before upgrading Insight agent, please refer to:
    [Upgrading from v0.16.x (or lower) to v0.17.x](../quickstart/install/upgrade-note.md#v016x-v017x).

#### Added

- **Added** support for viewing active alert and history alert details.
- **Added** support for quickly creating silent rules through alerts.
- **Added** support for SMS notifications in alerts.
- **Added** support for sending test messages in email notifications.
- **Added** support for customizing email subjects in message templates for email notifications.
- **Added** variable explanations to message templates.
- **Added** default high availability support for Insight Server component.

#### Improvements

- **Improved** display full TraceID in trace query.
- **Improved** added prompt when service is empty in trace query.
- **Improved** added no data prompt for JVM monitoring.
- **Improved** alert policy details do not show other parameters if not notified.
- **Improved** added resource limits for OpenTelemetry Operator.
- **Improved** upgraded Grafana version to v9.3.14.
- **Improved** upgraded tailing sidecar version from v0.5.6 to v0.7.0.
- **Improved** upgraded kube-prometheus-stack version to v45.28.1.
- **Improved** upgraded prometheus version to v2.44.0.

#### Bug Fixes

- **Fixed** an issue where service topology was effective when namespace was empty.
- **Fixed** an issue with invalid documentation link in service topology status description.
- **Fixed** duplication of namespace and stateless workload in displayed namespace when creating alert policies.
- **Fixed** missing trigger value data in alert list and alert policy in alerts.
- **Fixed** validation error in required fields for type, keyword, and value when adding silence conditions in alert silencing.
- **Fixed** time zone not being effective in alert silencing time range.
- **Fixed** an issue where no alert object was created for promQL rules for workload types.
- **Fixed** an issue where modifications to built-in alert rules could not be saved.
- **Fixed** an issue with hardcoded time zone in components.

## 2023.04.28

### v0.16.0

!!! warning

     Insight v0.16.0 uses the new feature parameter __disableRouteContinueEnforce__ of vmalertmanagers CRD,
     before upgrading insight server, please refer to [Upgrade from v0.15.x (or earlier) to v0.16.x](../quickstart/install/upgrade-note.md)

#### New Features

- **Added** JVM monitoring for Java applications.
- **Added** Set alert silent notification.
- **Added** alert policy function, which supports adding multiple alert rules in an alert policy for management.
- **Added** nginx Ingress, Contour and other components monitoring dashboard.
- **Added** The service topology supports enabling or disabling virtual nodes.
- **Added** statistics on the number of currently active alerts.
- **Added** ServiceMonitor with built-in HwameiStor component.
- **Added** domain name supports access to sub path.
- **Added** [Dashboard] Add record information according to the global management configuration
- **Added** [Dashboard] domain name supports access to sub path.

#### Improvements

- **Improved** the content of the built-in message template.
- **Improved** Adjust the built-in alert rules to the corresponding policies.
- **Improved** The filter display problem when the service namespace is empty.
- **Improved** Add cache to service list.

#### Fixes

- **Fixed** The problem of Chinese invalid search.
- **Fixed** The problem that the service topology namespace permission cannot view the topology map.
- **Fixed** [Dashboard] Kylin icon style problem
- **Fixed** [dashboard] tooltip is too long

## 2023.04.04

### v0.15.4

#### Improvements

- **Improved** the default number of primary shards for ES index to match the default number of ES nodes in the middleware.
- **Improved** the JVM information API response body structure.

#### Fixes

- **Fixed** multiple trigger alert logging
- **Fixed** Fluentbit CVE-2021-46848, upgrade from 2.0.5 to 2.0.8
- **Fixed** task to check license resources
- **Fixed** SQL statement to clear alert history
- **Fixed** the Chinese problem in the English dashboard

## 2023.03.30

### v0.15.1

#### New Features

- **Added** JVM metric collection and integrated monitoring panel
- **Added** Link Access Guidance
- **Added** service topology supports error rate and request delay filtering
- **Added** link supports Trace ID search
- **Added** Prometheus component to enable automatic vertical expansion

#### Improvements

- **Improved** the style of the topology map virtual node
- **Improved** service topology virtual node increase switch

#### Fixes

- **Fixed** display style of pod running status
- **Fixed** When the link feature is not enabled, hide related configuration parameters
- **Fixed** some front-end styles do not take effect
- **Fixed** collection pod metrics no data problem
- **Fixed** an issue of unable to install insight-agent in OpenShift cluster

## 2023.02.27

### v0.14.6

#### New Features

- **Added** a refresh button to the chart
- **Added** service topology supports selecting multiple clusters and supports searching by service name
- **Added** service topology details and metrics of traffic egress and ingress
- **Added** a behavior of clicking the service name in the service topology details to jump to the details of the service
- **Added** list of service monitoring and metrics of traffic egress and ingress
- **Added** system component monitoring list
- **Added** CoreDNS monitoring panel
- **Added** an option to enable kubeAudit collection settings when installing Insight Agent

#### Improvements

- **Improved** filter conditions in trace query and view traces with Error
- **Improved** The scatter diagram of the trace query is updated to a bubble diagram
- **Improved** reduce Prometheus's metrics retention time to 2 hours
- **Improved** The default parameter of retentionPeriod of VMStorage is adjusted to 1 month
- **Upgraded** fluentbit helm chart version to 0.24.0
- **Updated** **tailing-sidecar/operator** mirror
- **Updated** Global collection rule interval is 60 seconds

#### Fixes

- **Fixed** built-in vmcluster dashboard
- **Fixed** When the link is not opened, the navigation bar cannot be loaded
- **Fixed** system component jump to view details link error
- **Fixed** The quick installation/uninstallation link of the acquisition management list is wrong
- **Fixed** After advanced index query query, the overlapping part of the index association and chart in the drop-down box cannot be selected
- **Fixed** Allow input of decimals when modifying the storage duration of historical alerts
- **Fixed** Send multiple notifications when an alert rule generates multiple alerts
- **Fixed** **configmap-reload** mirror error for **vmalert** and **vmalertmanager**
- **Fixed** fluentbit for Insight Agent on ARM architecture

## 2023.01.10

### v0.13.2

#### Fixes

- **Fixed** the problem that **kubernetes-event-exporter** image address in insight-agent is wrong
- **Fixed** filter alerts API by resource name

## 2023.12.30

### v0.13.1

#### Fixes

- **Fixed** build offline package to add **.relok8s-images** file
- **Fixed** adjust the port name corresponding to the component **otel-collector** port in insight-agent

## 2022.12.29

### v0.13.0

#### New Features

- **Added** support for modifying the storage time of historical alerts
- **Added** status details of collection management components
- **Added** built-in message template
- **Added** chart metric Calculation Instructions

### Improvements

- **Improved** log list field display
- **Improved** the judgment logic of insight-agent
- **Upgraded** Jaeger Chart version upgraded from v0.62.1 to 0.65.1

### Fixes

- **Fixed** Some built-in alert rules do not take effect
- **Fixed** an error that the name can be duplicated when creating a rule
- **Fixed** DingTalk robot ending with '-'
- **Fixed** case-insensitive fuzzy search in alert rules
- **Fixed** service metric error delay calculation is not accurate
- **Fixed** Jaeger query has **too many open files** problem
- **Fixed** es index rollover alias and cleanup strategy not working

## 2022.11.28

### v0.12

#### Features

- **Added** insight-agent Helm chart installation supports form

#### Improvements

- **Improved** PromQL queries support raw metrics
- **Improved** the style of the topology map
- **Upgraded** built-in MySQL image version, upgraded from v5.7.34 to v8.0.29.
- **Upgraded** Fluentbit ARM architecture helm Chart version from
- **Upgraded** kube-prometheus-stack helm Chart version upgraded from v39.6.0 to v41.9.1
- **Updated** used Bitnami mirror, including grafana-operator, grafana, kubernetes-event-exporter
- **Updated** prometheus-related API proxy address, change **/prometheus** to **/apis/insight.io/prometheus**

#### Fixes

- **Fixed** service list caching logic
- **Fixed** the problem that the built-in rules do not take effect
- **Fixed** request delay unit issue
- **Fixed** Insight internal link issue
- **Disabled** PSP resource in vm-stack
- **Fixed** victoriaMetrics operator not available in Kubernetes 1.25.
- **Fixed** browser compatibility issues with front-end mirroring

## 2022-11-21

### v0.11

#### Improvements

- **Added** link troubleshooting and monitoring dashboard for component **Jaeger**
- **Improved** The alert list and message template list support sorting
- **Improved** to filter out clusters without **insight-agent** installed
- **Improved** sort by span start time by default when trace query

#### Fixes

- **Fixed** no data **dashboard** , including OpenTelemetry related dashboards
- **Fixed** the problem that there is no content under some log paths
- **Fixed** delete wrong alert rule: KubeletPodStartUpLatencyHigh

#### Other

- **victoria-metrics-k8s-stack** helm chart updated to v0.12.6
- **opentelemetry-collector** helm chart upgraded from v0.23.0 to v0.37.2
- **jaeger** helm chart upgraded from v0.57.0 to v0.62.1
- **fluentbit** helm chart upgraded from v0.20.9 to v1.9.9
- **kubernetes-event-exporter** helm chart upgraded from v1.4.21 to v2.0.0

## 2022-10-20

### v0.10

#### Features

- Support for container-managed Service names associated with OTel service names to discern if service linking is enabled
- Updated the default tracking sample strategy in the global OTel column
- Change sumo (for audit logs) exporter port 8080 to 80
- Use go-migrate to manage database migration versions
- Fix multicluster and multi-namespace filters not working properly in graph API
- Support for building ARM images

#### Install

- Fluentbit supports docker and containerd log parsers
- Fix var/log/UTC issues
- Fluentbit supports elasticsearch output to skip TLS verification
- K8s audit log filter supports getting rules from Helm values
- Fix the parsing problem of centos7/ubuntu20 host log time
- Upgrade the OTel Operator version and remove the cert-manager dependency deployed with the self-signed certificate in the Operator
- Designed jaeger collector metrics
- Upgrade tailing-sidecar version
- Jaeger supports elasticsearch output to skip TLS verification
- Disable jaeger components in A-mode

#### Other

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
- kube audit log filter support getting rule from helm values.
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
- Expose metric **insight_cluster_info** in server.
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
- Added user guides - documents such as scene monitoring, data query, alert center, etc.
- New additions to the document site: [Product Benefits](../intro/benefits.md), [Metric Query](../user-guide/data-query/metric.md), [trace query](../user-guide/trace/trace.md), dashboard, [overview](../user-guide/dashboard/overview.md)

## 2022-4-22

### v0.4

#### Features

- Increase the main API of the alert notification module
- Upgrade and adapt kpanda 0.4.x API
- Add the path information of the file to which the log belongs to the system log
- Add query single log context API
- Add query Kubernetes Event API
- Enhance Insight's own observability capabilities, provide its own metric interface and query trace information
- The API of Jaeger Query is used by the front end through the reverse proxy
- Add Query Tracing Operations related API
- Add Span Metric related API

#### test

- Added E2E use case coverage badge
- Supplementary test case documents related to alert notification
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
