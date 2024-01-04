# 自定义探测方式

在本文中，我们将介绍如何在已有的 Blackbox ConfigMap 中配置自定义的探测方式。
我们将以 HTTP 探测方式作为示例，展示如何修改 ConfigMap 以实现自定义的 HTTP 探测。

## 操作步骤

1. 进入 __容器管理__ 的集群列表，点击进入目标集群的详情；
2. 点击左侧导航，选择 配置与密钥 > 配置项；
3. 找到名为 __insight-agent-prometheus-blackbox-exporter__ 的配置项，点击操作中的 __编辑 YAML__ ；

    - 在 __modules__ 下添加自定义探测方式。此处添加 HTTP 探测方式为例：

    ```yaml
    module:
      http_2xx:
        prober: http
        timeout: 5s
        http:
          valid_http_versions: [HTTP/1.1, HTTP/2]
          valid_status_codes: []  # Defaults to 2xx
          method: GET
    ```

!!! info

    更多探测方式可参考 [blackbox_exporter Configuration](https://github.com/prometheus/blackbox_exporter/blob/master/CONFIGURATION.md)。
