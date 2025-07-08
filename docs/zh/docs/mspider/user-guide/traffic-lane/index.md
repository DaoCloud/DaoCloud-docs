# 流量泳道

流量泳道（Traffic Lane）功能用于实现多版本、灰度发布等场景下的 **精细化流量路由控制** 。
该机制的核心依赖以下三个关键要素：

- **Wasm 扩展模块**：在服务间请求中注入自定义 Header（如 `x-mspider-lane`），用于标识请求所属的泳道。
- **TraceID 链路追踪信息**：辅助识别请求来源，为泳道路由提供上下文支持。
- **Istio 路由配置**：通过 VirtualService（VS）和 DestinationRule（DR）基于 Header 实现泳道级流量分发。

## 场景示例

### 系统请求链路

```yaml
bookinfo-gw（Istio 网关）
    ↓
productpage
    ↓
details & reviews...
```

此链路中的每一跳服务均已接入 Istio Sidecar，并支持基于 Header 的子集路由。

### 泳道规划策略

- 定义两个泳道：`green` 和 `yellow`
- 使用 Header Key：`x-mspider-lane`（泳道标识字段）
- 默认泳道值：`green`

### 路由行为预期

| 请求 Header 示例 | 预期路由目标子集 |
| --------------- | ------------- |
| x-mspider-laneid: green | green |
| x-mspider-laneid: yellow | yellow |

- 请求到达时，Istio 会依据 Header 中的泳道标识将流量路由至对应的子集 Pod。
- 若 Header 缺失，系统可配置默认值或返回错误，具体取决于 VS/DR 策略。

### Header 重写说明

由于上游服务可能使用 `x-mspider-laneid` 字段，而系统内部标准识别字段为 `x-mspider-lane`，
建议在入口网关（如 `istio-cars-ingress`）的 VirtualService 中添加以下配置：

```yaml
http:
- match:
    ...
  headers:
    request:
      set:
        x-mspider-lane: "{{ request.headers['x-mspider-laneid'] }}"
```

!!! note

    如上操作用于将 `x-mspider-laneid` 统一映射为标准泳道标识 `x-mspider-lane`，仅当上游请求头不一致时才需配置；若已统一为 `x-mspider-lane`，可跳过这一步。

## 示例操作步骤

### 1. 开启网格链路追踪功能

![img](./images/lane01.png)

### 2. wasm plugin 定义流量泳道匹配 header

```yaml
apiVersion: extensions.istio.io/v1alpha1
kind: WasmPlugin
metadata:
  name: bookinfo
  namespace: bookinfo
spec:
  imagePullPolicy: Always
  phase: STATS
  pluginConfig:
    cache_size: 1024
    lane_header: x-mspider-lane # 流量泳道识别的通用 header key
    traffic_lane: green # 泳道默认 header value
    type: W3C
  selector:
    matchLabels:
      app: bookinfo # 泳道作用的工作负载共同 label
  url: oci://release.daocloud.io/mspider/mspider-traffic-lane:v0.30.4 # 泳道版本
```

如果是私有环境，记得提前将泳道的 Wasm 推送到镜像仓库。

### 3. 服务检查

- 端口协议配置, **端口协议定义一定要正确**
- 服务与多版本工作负载是否正确绑定
- 注入边车
- 服务是否正常运行（服务列表 UI 界面）

![img](./images/lane02.png)

### 4. 定义服务的 dr, 给每个服务都配置 green 和 yellow 两组 subset

要确认是否绑定了目标服务，可以通过服务网格界面辅助判断

![img](./images/lane03.png)

### 5. 南北网关定义 vs 路由规则

网关需要重写 header

```yaml
apiVersion: networking.istio.io/v1beta1
kind: VirtualService
metadata:
  name: bookinfo-gw
  namespace: bookinfo
spec:
  gateways:
    - bookinfo/bookinfo-gw # 网关入口服务
  hosts:
    - '*'
  http:
    - headers: # 将请求 header 重置为流量泳道通用 header 规则 <x-mspider-lane：green>
        request:
          set: # 重写
            x-mspider-lane: green
      match: # 访问服务，比如发起 http 的入口请求（postman），需要定义 header <green>
        - headers:
            x-mspider-laneid:
              exact: green
      name: green-lane
      route:
        - destination:
            host: productpage
            port:
              number: 9080
            subset: green
    - headers:
        request:
          set:
            x-mspider-lane: yellow
      match:
        - headers:
            x-mspider-laneid:
              exact: yellow
      name: yellow-lane
      route:
        - destination:
            host: productpage
            port:
              number: 9080
            subset: yellow
```

如果不需要重写 header，示例如下：

```yaml
apiVersion: networking.istio.io/v1beta1
kind: VirtualService
metadata:
  name: bookinfo-gw
  namespace: bookinfo
spec:
  gateways:
    - bookinfo/bookinfo-gw # 网关入口服务
  hosts:
    - '*'
  http:
    - match: # 访问服务，比如发起 http 的入口请求（postman），需要定义 header <green>
        - headers:
            x-mspider-lane:
              exact: green
      name: green-lane
      route:
        - destination:
            host: productpage
            port:
              number: 9080
            subset: green
    - match:
        - headers:
            x-mspider-lane:
              exact: yellow
      name: yellow-lane
      route:
        - destination:
            host: productpage
            port:
              number: 9080
            subset: yellow
```

### 6. 后续内部服务定义 VirtualService

```yaml
apiVersion: networking.istio.io/v1beta1
kind: VirtualService
metadata:
  name: details
  namespace: bookinfo
spec:
  gateways:
    - mesh # 全局服务
  hosts:
    - details # 内部服务
  http:
    - match: # 匹配泳道 通用 header 规则
        - headers:
            x-mspider-lane:
              exact: green
      name: green
      route:
        - destination:
            host: details
            port:
              number: 9080
            subset: green
    - match:
        - headers:
            x-mspider-lane:
              exact: yellow
      name: yellow
      route:
        - destination:
            host: details
            port:
              number: 9080
            subset: yellow
```

## 常见问题记录

### VS 端口错误导致服务无法访问

**VS 的目标端口选择错误** ，上面服务都是 http + grpc 两个端口，服务内部调用通过 grpc，默认选择了 http 端口，导致请求异常。

### no healthy upsteam - 工作负载匹配问题

错误一：DR 的 subset 中 label 匹配出错，导致无法找到 Pod

错误二： **服务和工作负载没有正确对应** ，导致无法找到对应的 Pod，可以在服务网格 UI 界面服务列表，检查服务与工作负载对应关系

### 没有开启链路追踪，导致服务访问错误

现象是 istio-proxy 有传入 header，但是没有 traceid
业务日志看到的请求 header x-mspider-lane 正常应该是：

![img](./images/lane05.png)

