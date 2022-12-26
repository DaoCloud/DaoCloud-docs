# Falco

[Falco](https://falco.org) 是一个*云原生运行时安全*工具，旨在检测应用程序中的异常活动。 您可以使用 Falco 监控 Kubernetes 应用程序和内部组件的运行时安全性。您仅需为 Falco 撰写一套规则，即可持续监测并监控容器、应用、主机及网络的异常活动。

## Falco 能检测到什么？

Falco 可对任何涉及Linux系统调用的行为进行检测和报警。Falco 的警报可以通过使用特定的系统调用、其参数以及调用进程的属性来触发。例如，Falco 可以轻松检测到包括但不限于以下事件：

  - Kubernetes中的容器或pod内正在运行一个shell。
  - 容器以特权模式运行，或从主机挂载敏感路径，如/proc。
  - 一个服务器进程正在生成一个意外类型的子进程。
  - 意外读取一个敏感文件，如/etc/shadow。
  - 一个非设备文件被写到/dev。
  - 一个标准的系统二进制文件，如ls，正在进行一个外向的网络连接。
  - 在Kubernetes集群中启动一个有特权的pod。 
  
Falco 附带的默认规则的更多详细信息，请参考 [Rules 文档](https://github.com/falcosecurity/falco/blob/master/rules_inventory/rules_overview.md)。


## 什么是 Falco 规则？

Rules 定义 Falco 应监视的行为及事件；您可以在 Falco 规则文件或通用配置文件撰写规则，有关编写、管理和部署规则的更多信息，请参阅 Falco [Rules](https://falco.org/docs/rules/)。

## 什么是 Falco 警报？

警报是可配置的下游操作，可以像记录日志一样简单，也可以像STDOUT向客户端传递 gRPC 调用一样复杂。有关配置、理解和开发警报的更多信息，请参阅Falco [警报](https://falco.org/docs/alerts/)。Falco 可以将警报发送至：

 - 标准输出
 - 一份文件
 - 系统日志
 - 生成的程序
 - 一个 HTTP[s] 端点
 - 通过 gRPC API 的客户端


## Falco 由哪些部分组成？

Falco 由以下几个主要组件组成：

 - 用户空间程序 - 是CLI工具，你可以用它来与 Falco 交互。用户空间程序处理信号，解析来自Falco驱动的信息，并发送警报。

 - 配置 - 定义 Falco 的运行方式、要断言的规则以及如何执行警报。有关详细信息，请参阅[配置](https://falco.org/docs/configuration)。

 - Driver - 是一款遵循 Falco 驱动规范并发送系统调用信息流的软件。如果不安装驱动程序，您将无法运行 Falco。目前，Falco 支持以下驱动程序：：

    -（默认）基于C++ 库构建libscap的内核模块libsinsp
    - 由相同模块构建的 BPF 探针
    - 用户空间检测
   
   有关详细信息，请参阅 Falco [驱动程序](https://falco.org/docs/event-sources/drivers/)。

 - 插件 - 允许用户通过添加新的事件源和可以从事件中提取信息的新字段来扩展 falco libraries/falco 可执行文件的功能。有关详细信息，请参阅[插件](https://falco.org/docs/plugins/)。