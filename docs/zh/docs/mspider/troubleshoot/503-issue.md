# 服务网格中常见的 503 报错

本文介绍服务网格中常见的 503 报错场景及解决办法。

## 偶发 503

### 使用自定义监控指标，每当配置变更时，日志监控发现少量请求出现 503

#### 问题原因

自定义指标功能的逻辑是通过生成一个对应的 EnvoyFiter 来进行 `istio.stats` 的配置更新。
该配置在 Envoy Listener 级别生效，即通过 LDS 同步生效。Envoy 在应用 Listener 级别的配置时，
需要断开已有连接。对应的在途请求因为连接被 Reset 或 Close 导致出现 503。

#### 解决办法

上游 Server 主动 Close 连接时，您看到的 503 并非上游 Server 发送，而是客户端边车因为上游连接主动断开，由本地返回的响应。

Istio 默认的重试配置中未包含“上游 Server 主动 Close 连接”的情况。EnvoyProxy 的重试条件中，
Reset 符合这种情况对应的触发条件。因此，您需要为对应服务的路由配置 retry Policy。
在 VirtualService 下的 retry Policy 配置包含 Reset 的触发条件。

配置示例如下。该配置仅针对 Ratings 服务生效。

```yaml
apiVersion: networking.istio.io/v1beta1
kind: VirtualService
metadata:
  name: ratings-route
spec:
  hosts:
    - ratings.prod.svc.cluster.local
  http:
    - route:
        - destination:
            host: ratings.prod.svc.cluster.local
            subset: v1
      retries:
        attempts: 2
        retryOn: connect-failure,refused-stream,unavailable,cancelled,retriable-status-codes,reset,503
```

#### 相关 FAQ

**为什么 Istio 默认的重试机制未生效？**

Istio 默认重试发生的条件如下。默认会重试 2 次。该场景未在重试条件内，因此未生效。

```yaml
"retry_policy":
  {
    "retry_on": "connect-failure,refused-stream,unavailable,cancelled,retriable-status-codes",
    "num_retries": 2,
    "retry_host_predicate":
      [{ "name": "envoy.retry_host_predicates.previous_hosts" }],
    "host_selection_retry_max_attempts": "5",
    "retriable_status_codes": [503],
  }
```

- **connect-failure**：连接失败。
- **refused-stream**：当 HTTP2 Stream 流返回 `REFUSED_STREAM` 错误码。
- **unavailable**：当 gRPC 请求返回 `unavailable` 错误码。
- **cancelled**：当 gRPC 请求返回 `cancelled` 错误码。
- **retriable-status-codes**：当请求返回的 `status_code` 和 `retriable_status_codes` 配置下定义的错误码匹配。

关于最新版本的 EnvoyProxy 完整的重试条件，请参见以下文档。

- HTTP 已有的重试条件配置（包含 HTTP2 和 HTTP3）：
  [Router](https://www.envoyproxy.io/docs/envoy/latest/configuration/http/http_filters/router_filter#x-envoy-retry-on)
- gRPC 独有的重试条件配置：
  [x-envoy-retry-grpc-on](https://www.envoyproxy.io/docs/envoy/latest/configuration/http/http_filters/router_filter#config-http-filters-router-x-envoy-retry-grpc-on)

### 偶发 503，没有规律，在此过程中并未发生配置变更

503 偶尔出现，但是在流量密集时，会持续出现。通常出现在边车的 Inbound 侧。

#### 问题原因

Envoy 的空闲连接保持时间和应用不匹配。Envoy 空闲连接时间默认为 1 小时。

- Envoy 空闲连接时间过长，应用相对较短：

    应用已经结束空闲连接，但是 Envoy 认为没有结束。此时如果有新的连接，就会报 503UC。

- Envoy 空闲连接时间过短，应用相对较长：

    这种情况不会导致 503。Envoy 认为之前的连接已经被关闭，因此会直接新建一个连接。

#### 解决办法

**方案一：在 DestinationRule 中配置 idleTimeout**

造成该问题的原因就是 idleTimeout 不匹配，因此在 DestinationRule 中配置 idleTimeout 属于比较根本的解决办法。

如果配置了 idelTimeout，在 Outbound 和 Inbound 两侧都会生效，即 Outbound 和 Inbound 的 Sidecar
都会存在 idleTimeout 的配置。如果客户端没有 Sidecar，idleTimeout 也会生效，并能够有效减少 503。

配置建议：此配置与业务相关，太短会导致连接数过高。建议您配置为略短于业务应用真正的 idleTimeout 时间。

**方案二：在 VirtualService 中配置重试**

重试会重建连接，可以解决此问题。具体操作，请参见[场景一](#503_2)的解决办法。

!!! important

    该操作为非幂等的请求，重试存在较大的风险，请谨慎操作。

### 边车生命周期相关

#### 问题原因

边车和业务容器生命周期导致，常发生于 Pod 重启。

#### 解决办法

具体操作，请参见[边车生命周期](./sidecar-lifecycle.md)。

## 必定 503

### 应用监听 localhost

#### 问题原因

当集群中的应用监听 localhost 网络地址时，如果 localhost 是本地地址，会导致集群中的其他 Pod 无法对其进行正常访问。

#### 解决办法

您可以通过对外暴露应用服务解决此问题。具体操作，请参见[如何使集群中监听 localhost 的应用被其他 Pod 访问](./localhost-by-pod.md)。

### 启用边车后，健康检查总是失败，报错 503

#### 问题原因

在服务网格开启 mTLS 后，kubelet 向 Pod 发送的健康检查请求被边车拦截，而 kubelet 没有对应的 TLS 证书，导致健康检查失败。

#### 解决办法

您可以通过配置端口健康检查流量免于经过边车代理解决此问题。
