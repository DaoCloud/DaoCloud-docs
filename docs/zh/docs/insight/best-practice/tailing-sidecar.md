---
hide:
  - toc
---

# 通过 Sidecar 采集容器日志

Tailing Sidecar 是一个[流式 Sidecar 容器](https://kubernetes.io/zh-cn/docs/concepts/cluster-administration/logging/#streaming-sidecar-container)，
是 Kubernetes 集群级的日志代理。Tailing Sidercar 可以在容器无法写入标准输出或标准错误流时，无需更改，即可自动收取和汇总容器内日志文件。

Insight 支持通过 Sidercar 模式采集日志，即在每个 Pod 中运行一个 Sidecar 容器将日志数据输出到标准输出流，以便 FluentBit 收集容器日志。

Insight Agent 中默认安装了 __tailing-sidecar operator__ 。
若您想开启采集容器内文件日志，请通过给 Pod 添加注解进行标记， __tailing-sidecar operator__ 将自动注入 Tailing Sidecar 容器，
被注入的 Sidecar 容器读取业务容器内的文件，并输出到标准输出流。

具体操作步骤如下：

1. 修改 Pod 的 YAML 文件，在 __annotation__ 字段增加如下参数：

    ```yaml
    metadata:
      annotations:
        tailing-sidecar:  <sidecar-name-0>:<volume-name-0>:<path-to-tail-0>;<sidecar-name-1>:<volume-name-1>:<path-to-tail-1>
    ```

    字段说明：

    - __sidecar-name-0__ ：tailing sidecar 容器名称（可选，如果未指定容器名称将自动创建，它将以“tailing-sidecar”前缀开头）
    - __volume-name-0__ ：存储卷名称；
    - __path-to-tail-0__ ：日志的文件路径

    !!! note

        每个 Pod 可运行多个 Sidecar 容器，可以通过 __;__ 隔离，实现不同 Sidecar 容器采集多个文件到多个存储卷。

2. 重启 Pod，待 Pod 状态变成 __运行中__ 后，则可通过 __日志查询__ 界面，查找该 Pod 的容器内日志。
