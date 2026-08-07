# Gateway API 实例访问配置

ClawOS 实例的 UI（OpenClaw web/ noVNC / filebrowser）与 MS Teams 回调可以通过 Gateway API 统一入口暴露。
管理员只需在集群里准备一个打了 label 的 Gateway，ClawOS 会在创建实例时自动挑中它并生成 HTTPRoute；
挑不到可用 Gateway 时，实例自动回退 NodePort 直连，不影响创建。

最小配置就两步：给 Gateway 打上 `agentclaw.io/gateway: "true"`，再用 `agentclaw.io/base-url` 注解
告诉 ClawOS 用户从外面访问的地址是什么。下面逐项说明。

## 前置条件

- 集群已安装 Gateway API CRD（`gateway.networking.k8s.io/v1`）及对应的 GatewayClass 控制器（如 kgateway、Envoy Gateway、Istio）。
- 控制器必须支持 WebSocket 透传：OpenClaw 与 noVNC 均走 WS。ClawOS 生成的实例 Service 已在对应端口标注
  `appProtocol: kubernetes.io/ws`，部分实现（kgateway）依赖它来放行 WebSocket。

## Gateway 需要满足的条件

下列条件缺一不可，不满足的 Gateway 会被跳过（不会报错，实例直接回退 NodePort）：

| 条件 | 说明 |
| --- | --- |
| label `agentclaw.io/gateway: "true"` | 值必须是字符串 `"true"` |
| 至少一个 listener 的 `protocol` 是 `HTTP` 或 `HTTPS` | TCP / TLS / UDP listener 承载不了 HTTPRoute |
| 该 listener 的 `allowedRoutes.namespaces.from` 为 `All` | 必须显式写 |
| 该 listener 的 `allowedRoutes.kinds` 未指定，或包含 `HTTPRoute` | 只声明了 GRPCRoute 的 listener 不可用 |
| 能确定对外访问地址 | 即"配了合法的 `agentclaw.io/base-url` 注解"或"`status.addresses` 非空"，详见下一节 |

!!! note

    ClawOS 不检查 Gateway 的 `Accepted` / `Programmed` condition。控制器还没把 Gateway 编程完成时，
    它依然可能被选中——此时 HTTPRoute 能创建成功，但要等控制器就绪后才真正可访问。

示例（HTTPS listener + 显式对外域名）：

```yaml
kind: Gateway
apiVersion: gateway.networking.k8s.io/v1
metadata:
  name: clawos-gateway
  namespace: public
  labels:
    agentclaw.io/gateway: "true"
  annotations:
    agentclaw.io/base-url: https://agentclaw.example.com
spec:
  gatewayClassName: kgateway
  listeners:
    - name: https
      port: 443
      protocol: HTTPS
      tls:
        mode: Terminate
        certificateRefs:
          - name: agentclaw-tls
      allowedRoutes:
        namespaces:
          from: All
```

## 对外访问地址（`agentclaw.io/base-url`）

这个地址会被直接拼上 `/agentclaw/<instanceID>/...` 前缀，作为下发给用户的访问链接，
所以它必须是**用户浏览器实际访问的地址**，而不是集群内部地址。

### 方式一：注解显式指定（推荐）

注解一旦存在就以它为准，不再看 `status.addresses`。格式必须是 `scheme://host[:port]`，
写得不合法会导致该 Gateway 整体不可用（回退 NodePort）。

### 方式二：不写注解，自动推导

取 `status.addresses` 中第一个非空 `value`，拼成 `<listener 协议小写>://<value>`；
listener 端口不是该协议的默认端口（HTTP 80 / HTTPS 443）时才追加 `:<port>`，IPv6 地址自动加方括号。

## 多个 Gateway 时怎么选

- 列出集群内所有打了 label 的 Gateway，按 `namespace/name` 字典序取**第一个满足上述条件**的。
  这个顺序只是为了让结果可复现，不代表"更合适"——**建议全集群只保留一个**打 label 的 Gateway。
- 同一个 Gateway 内有多个 listener 时，`HTTPS` 优先于 `HTTP`；同协议时按 listener `name` 字典序。
  该顺序只影响自动推导出的 scheme 与端口；配了注解时对最终地址没有影响。

## 生成的路由

实例创建时，ClawOS 在**实例所在 namespace** 下创建名为 `agent-route-<instanceID>` 的 HTTPRoute，
`parentRefs` 指向选中的 Gateway，并带 ownerReferences（实例删除时自动回收）。路径前缀：

| 路径前缀 | 后端 |
| --- | --- |
| `/agentclaw/<instanceID>/openclaw` | OpenClaw UI |
| `/agentclaw/<instanceID>/vnc` | noVNC |
| `/agentclaw/<instanceID>/files` | filebrowser |
| `/agentclaw/<callbackID>/msteams` | MS Teams 回调（端口 3978） |

各前缀通过 `ReplacePrefixMatch` 重写为 `/` 再转发到实例 Service。若 Gateway 前面还有一层反向代理，
务必把这些路径原样透传，不要再做前缀剥离。

## 生效时机与排查

- Gateway 只在**实例创建 / 更新**时评估一次。事后新增 Gateway 或修改注解，不会自动改写已有实例的
  HTTPRoute 和访问地址，需要更新实例才会重新选择。
- 任何一环失败（没有候选 Gateway、没有可用 listener、注解非法、拿不到地址）都不会阻断实例创建，
  只是回退成 NodePort 直连。
- 排查时把 apiserver 日志级别调到 `-v=2`，搜 `No usable access gateway`，`reason` 字段里是逐个 Gateway 的具体原因，
  例如 `invalid agentclaw.io/base-url annotation: gateway base URL must not contain a path`。
