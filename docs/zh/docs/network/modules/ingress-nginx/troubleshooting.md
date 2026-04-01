# ingress-nginx 排障指南

本页整理了 ingress-nginx 的常见故障现象、检查方式与处理建议，帮助您快速定位 Ingress 不生效、访问异常和配置未下发等问题。

## 排查思路

遇到 Ingress 访问问题时，建议按以下顺序检查：

1. 确认 `Ingress`、`Service`、`Endpoints`、`Pod` 资源是否正常。
2. 确认 `IngressClass` 是否正确，且被目标 ingress-nginx 实例监听。
3. 确认 ingress-nginx `Service` 已正确暴露地址，外部流量可以到达。
4. 查看 ingress-nginx Controller 日志，确认是否存在配置生成、证书加载或 Webhook 异常。
5. 检查注解、TLS、超时、转发等配置是否符合预期。

## 常用排查命令

```bash
# 查看 Ingress 规则
kubectl get ingress -A
kubectl describe ingress <ingress-name> -n <namespace>

# 查看 IngressClass
kubectl get ingressclass
kubectl describe ingressclass <ingressclass-name>

# 查看 ingress-nginx 控制器状态
kubectl get pods -n <ingress-nginx-namespace>
kubectl get svc -n <ingress-nginx-namespace>
kubectl logs -n <ingress-nginx-namespace> deploy/<ingress-nginx-controller>

# 查看后端服务与端点
kubectl get svc -n <namespace>
kubectl get endpoints -n <namespace> <service-name>
kubectl get pod -n <namespace> -o wide

# 查看生成的 nginx 配置
kubectl exec -n <ingress-nginx-namespace> <controller-pod> -- nginx -T
```

## Ingress 未生效

**现象：**

- 创建 Ingress 后，请求没有进入预期的 ingress-nginx 实例。
- `kubectl describe ingress` 中没有看到对应 Controller 处理后的状态信息。

**排查步骤：**

1. 检查 Ingress 是否指定了正确的 `ingressClassName`。

    ```bash
    kubectl get ingress <ingress-name> -n <namespace> -o yaml
    kubectl get ingressclass
    ```

2. 如果未指定 `ingressClassName`，检查集群中是否存在默认 `IngressClass`。
3. 检查 ingress-nginx 安装参数中是否启用了 `scope`，若启用，确认当前 Ingress 所在命名空间在监听范围内。
4. 查看 Controller 日志中是否有忽略该 Ingress 的提示。

    ```bash
    kubectl logs -n <ingress-nginx-namespace> deploy/<ingress-nginx-controller> | grep <ingress-name>
    ```

**处理建议：**

- 为 Ingress 显式指定正确的 `ingressClassName`。
- 集群存在多套 ingress-nginx 时，确保 `IngressClass`、`Election ID`、`scope` 配置不冲突。
- 如果希望用户创建 Ingress 时无需指定类名，可将目标 `IngressClass` 设置为默认类。

## 无法从集群外访问

**现象：**

- 域名无法解析到 ingress-nginx 地址。
- `curl` 外部地址超时、连接拒绝，或浏览器无法打开页面。

**排查步骤：**

1. 查看 ingress-nginx `Service` 类型及地址是否正常。

    ```bash
    kubectl get svc -n <ingress-nginx-namespace>
    ```

2. 若 `Service` 类型为 `LoadBalancer`，检查 `EXTERNAL-IP` 是否已分配。
3. 若 `Service` 类型为 `NodePort`，确认节点安全组、防火墙、上游负载均衡已放通对应端口。
4. 检查域名解析是否指向正确的 VIP 或节点地址。
5. 在集群内发起访问，区分是“集群内可达、集群外不可达”，还是“整体不可达”。

    ```bash
    kubectl run -it --rm test-curl --image=curlimages/curl -- sh
    curl -H "Host: <your-host>" http://<ingress-service-ip>
    ```

**处理建议：**

- `LoadBalancer` 场景下，先确认底层 LB 组件工作正常，例如 MetalLB 或云厂商负载均衡。
- `NodePort` 场景下，补齐节点网络放通与四层转发配置。
- 若域名配置正确但仍不通，优先检查外部网络到 ingress-nginx `Service` 的链路。

## 访问返回 404 或 default backend

**现象：**

- 请求已经到达 ingress-nginx，但返回 `404 Not Found`。
- 访问结果落入默认后端，而不是目标业务服务。

**排查步骤：**

1. 检查请求使用的 `Host` 是否与 Ingress 中定义的 `rules.host` 一致。
2. 检查请求路径与 `path`、`pathType` 是否匹配。
3. 检查是否存在多个 Ingress 使用相同域名和路径，导致规则覆盖或匹配冲突。
4. 查看生成的 nginx 配置，确认规则是否已下发。

    ```bash
    kubectl exec -n <ingress-nginx-namespace> <controller-pod> -- nginx -T | grep -n "<your-host>"
    ```

**处理建议：**

- 使用 `curl -H "Host: <your-host>" http://<address>/<path>` 模拟真实请求头进行验证。
- 确认 `pathType` 选择正确，常见场景优先使用 `Prefix`。
- 多个团队共用域名时，提前约定路径规划，避免路由冲突。

## 访问返回 503

**现象：**

- Ingress 规则存在，但访问返回 `503 Service Temporarily Unavailable`。

**排查步骤：**

1. 检查 Ingress 后端引用的 `Service` 名称与端口是否正确。

    ```bash
    kubectl describe ingress <ingress-name> -n <namespace>
    kubectl get svc <service-name> -n <namespace> -o yaml
    ```

2. 检查 `Endpoints` 是否存在可用地址。

    ```bash
    kubectl get endpoints <service-name> -n <namespace>
    ```

3. 检查业务 Pod 是否就绪，`readinessProbe` 是否持续失败。
4. 检查 `Service` 的 `selector` 是否能选中正确 Pod。

**处理建议：**

- `503` 通常表示请求已进入 ingress-nginx，但后端没有可用端点。
- 优先修复应用 Pod 未就绪、`Service` 端口不匹配、标签选择器错误等问题。
- 如果后端服务偶发 `503`，可结合 [超时配置](./timeout.md) 和应用日志进一步分析。

## 注解或配置不生效

**现象：**

- 已经为 Ingress 添加注解，但转发、超时、跨域、上传大小等行为没有变化。

**排查步骤：**

1. 检查注解名称、拼写和取值格式是否正确。
2. 确认这些注解属于 ingress-nginx 支持的注解，而非其他 Ingress 控制器的语法。
3. 查看 Controller 日志，确认是否出现注解解析失败、配置校验失败等错误。
4. 查看最终生成的 nginx 配置是否包含预期内容。

**处理建议：**

- 布尔值、数字、时长等注解建议按文档要求填写，避免格式错误。
- 全局配置与单个 Ingress 注解并存时，注意二者的优先级与覆盖关系。
- 如需配置日志、超时、上传限制、跨域等能力，可分别参考：
  - [日志配置](./log.md)
  - [超时配置](./timeout.md)
  - [上传限制](./upload.md)
  - [跨域配置](./cors.md)

## Admission Webhook 校验失败

**现象：**

- 创建或更新 Ingress 时出现类似如下报错：

```text
admission webhook "validate.nginx.ingress.kubernetes.io" denied the request
```

**排查步骤：**

1. 检查 Ingress YAML 是否存在非法字段、重复路径或错误注解。
2. 检查 admission webhook Pod、Service、证书 Secret 是否正常。

    ```bash
    kubectl get pods,svc,secret -n <ingress-nginx-namespace>
    ```

3. 查看 webhook 相关日志。
4. 确认 apiserver 到 webhook Service 的网络连通性正常。

**处理建议：**

- 先修复 Ingress 配置本身的问题，例如路径定义冲突、注解值非法等。
- 如果是 webhook 证书异常或组件未就绪，建议重新检查 ingress-nginx 安装状态。
- 升级、迁移或恢复集群后出现该问题时，重点检查 webhook 证书是否过期或未正确挂载。

## TLS 证书不生效

**现象：**

- HTTPS 访问证书不正确，浏览器提示证书不受信任、域名不匹配，或仍返回默认证书。

**排查步骤：**

1. 检查 Ingress `spec.tls.hosts` 与 `rules.host` 是否一致。
2. 检查证书 Secret 是否存在于 Ingress 所在命名空间。

    ```bash
    kubectl get secret <tls-secret-name> -n <namespace>
    kubectl describe ingress <ingress-name> -n <namespace>
    ```

3. 确认 Secret 类型为 `kubernetes.io/tls`。
4. 查看 Controller 日志，确认是否出现证书加载失败或证书链错误。

**处理建议：**

- 证书 Secret、域名和 Ingress 命名空间三者必须匹配。
- 如果返回的是默认证书，通常说明目标域名没有匹配到对应 TLS 配置，或者证书未被成功加载。

## Ingress 延迟有波动

**现象：**

- 业务访问偶发变慢，P95、P99 延迟明显抖动。
- 用户感知为接口时快时慢，但并非持续不可用。

**排查思路：**

先区分延迟波动发生在 ingress-nginx，还是发生在后端服务。

1. 对比 ingress-nginx 访问日志中的请求耗时与后端应用日志中的处理耗时。
2. 如果 ingress-nginx 侧耗时已经升高，优先排查 ingress-nginx 自身资源与调度问题。
3. 如果 ingress-nginx 转发耗时正常，但后端应用处理时间变长，则重点排查后端服务、数据库或依赖组件。

**排查步骤：**

1. 检查 ingress-nginx Pod 的 CPU、内存使用情况，确认是否接近资源上限。

    ```bash
    kubectl top pod -n <ingress-nginx-namespace>
    kubectl describe pod <controller-pod> -n <ingress-nginx-namespace>
    ```

2. 检查 ingress-nginx Deployment 或 Helm values 中配置的 `resources.requests` 与 `resources.limits` 是否合理，重点关注 CPU limit 是否过小。
3. 检查是否存在 CPU throttle。若 CPU limit 过低，即使平均 CPU 使用率不高，也可能因为突发流量导致 CFS 限流，从而引起延迟抖动。
4. 结合 DCE Insight 监控查看以下指标：

    - Pod CPU usage
    - Pod memory usage
    - CPU CFS throttled periods
    - CPU CFS throttled seconds
    - Nginx 请求处理耗时、请求量、状态码分布

5. 对比后端 Service、Pod 的延迟与资源指标：

    ```bash
    kubectl top pod -n <namespace>
    kubectl get endpoints <service-name> -n <namespace>
    ```

6. 如果怀疑是 ingress-nginx 自身处理变慢，可登录节点或容器进一步做性能分析，例如使用 `perf`、`top`、`pidstat` 等工具观察热点函数、系统调用和上下文切换情况。

**处理建议：**

- 如果确认是 ingress-nginx 本身延迟波动：
  - 提高 ingress-nginx Pod 的 CPU `requests/limits`，避免资源不足或 CFS throttle。
  - 检查副本数是否足够，必要时扩容 Controller 副本分摊流量。
  - 检查节点是否存在 CPU 抢占、负载过高或 noisy neighbor 问题。
  - 如需深入分析，可使用 `perf` 对 nginx worker 或相关进程做采样分析。

- 如果确认是后端服务延迟高：
  - 优先分析应用自身处理耗时、数据库访问、外部依赖调用和 GC 情况。
  - 检查后端 Pod 是否存在资源瓶颈、线程池排队或连接池耗尽。

## 日志排查建议

建议同时关注以下两类日志：

- ingress-nginx Controller 日志：用于检查配置同步、证书加载、Webhook 与路由生成异常。
- 业务服务日志：用于确认请求是否已经转发到后端，以及后端是否返回了业务错误。

如果需要进一步分析访问链路，可临时开启或调整日志配置，参考 [日志配置](./log.md)。
