# 使用 OTel 赋予应用可观测性

> 增强是使应用程序代码能够生成遥测数据的过程。即一些可以帮助您监视或测量应用程序的性能和状态的东西。

OpenTelemetry 是领先的开源项目，为主要编程语言和流行框架提供检测库。它是云原生计算基金会下的一个项目，得到了社区庞大资源的支持。
它为采集的数据提供标准化的数据格式，无需集成特定的供应商。

Insight 支持用于检测应用程序的 OpenTelemetry 来增强您的应用程序。

本指南介绍了使用 OpenTelemetry 进行遥测增强的基本概念。
OpenTelemetry 还有一个由库、插件、集成和其他有用工具组成的生态系统来扩展它。
您可以在 [Otel Registry](https://opentelemetry.io/registry/) 中找到这些资源。

您可以使用任何开放标准库进行遥测增强，并使用 Insight 作为可观察性后端来摄取、分析和可视化数据。

为了增强您的代码，您可以使用 OpenTelemetry 为特定语言提供的增强操作：

Insight 目前提供了使用 OpenTelemetry 增强 .Net NodeJS、Java、Python 和 Golang 应用程序的简单方法。请遵循以下指南。

## 链路增强

- 链路接入的最佳实践：[通过 Operator 实现应用程序无侵入增强](./operator.md)
- 以 Go 语言为例的手动埋点接入：[使用 OpenTelemetry SDK 增强 Go 应用程序](./golang/golang.md)
- [利用 ebpf 实现 Go 语言无侵入探针](https://github.com/keyval-dev/opentelemetry-go-instrumentation/blob/master/docs/getting-started/README.md)（实验性功能）

<!--
## 日志增强

TBD
-->
