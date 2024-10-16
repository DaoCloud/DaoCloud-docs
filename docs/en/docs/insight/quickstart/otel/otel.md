---
MTPE: windsonsea
Date: 2024-10-16
---

# Use OTel to provide the application observability

> Enhancement is the process of enabling application code to generate telemetry data. i.e. something that helps you monitor or measure the performance and status of your application.

OpenTelemetry is a leading open source project providing instrumentation libraries for major programming languages ​​and popular frameworks. It is a project under the Cloud Native Computing Foundation and is supported by the vast resources of the community.
It provides a standardized data format for collected data without the need to integrate specific vendors.

Insight supports OpenTelemetry for application instrumentation to enhance your applications.

This guide introduces the basic concepts of telemetry enhancement using OpenTelemetry.
OpenTelemetry also has an ecosystem of libraries, plugins, integrations, and other useful tools to extend it.
You can find these resources at the [OTel Registry](https://opentelemetry.io/registry/).

You can use any open standard library for telemetry enhancement and use Insight as an observability backend to ingest, analyze, and visualize data.

To enhance your code, you can use the enhanced operations provided by OpenTelemetry for specific languages:

Insight currently provides an easy way to enhance .Net NodeJS, Java, Python and Golang applications with OpenTelemetry. Please follow the guidelines below.

## Trace Enhancement

- Best practices for integrate trace: [Application Non-Intrusive Enhancement via Operator](./operator.md)
- Manual instrumentation with Go language as an example: [Enhance Go application with OpenTelemetry SDK](golang/golang.md)
- [Using ebpf to implement non-intrusive auto-instrumetation in Go language](./golang-ebpf.md) (experimental feature)

<!--
## Log Enhancement

TBD
-->