# 从 ingress-nginx 迁移到 Higress 或 kgateway

本文介绍从 ingress-nginx 迁移到 Higress 或 kgateway 的选型思路、实施步骤和验证方法，
适用于希望尽量保留现有 Ingress YAML 与注解（Annotation）的存量用户。

!!! warning

    ingress-nginx 已于 2026 年 3 月退役。已有部署仍可继续运行，安装工件也仍然可用，
    但项目不再发布新版本、修复缺陷或处理新发现的安全漏洞。请尽快评估并迁移到仍在维护的入口网关。
    详情参见 [Ingress2Gateway 1.0 发布公告](https://kubernetes.io/zh-cn/blog/2026/03/20/ingress2gateway-1-0-release/)。

## 迁移背景与目标

Kubernetes Ingress API 只能表达基础的七层路由能力。ingress-nginx 通过大量私有注解扩展了流量治理能力，
但这些扩展与具体实现耦合，难以直接迁移到其他控制器。与此同时，Kubernetes 网络生态正在转向
[Gateway API](https://gateway-api.sigs.k8s.io/)，新的网关产品也优先围绕 Gateway API 构建。

迁移不只是替换控制器，还应达到以下目标：

- 尽量兼容现有 Ingress 资源及 `nginx.ingress.kubernetes.io/*` 注解。
- 尽量减少业务 YAML 改动、切换窗口和停机时间。
- 为后续采用 Gateway API、插件扩展、安全治理和灰度发布等能力奠定基础。

本文以 **Higress v2.2.0** 和 **kgateway v2.2** 为评估基线：

- **Higress** 对常见 ingress-nginx 注解兼容较好，适合优先降低存量迁移成本。
- **kgateway** 面向 Gateway API，适合计划采用标准 Gateway API 资源的集群。

!!! note

    没有任何网关能够完全兼容 ingress-nginx 的全部注解。选型脚本只能提供初步建议，
    迁移前仍需逐项检查不支持、部分兼容或需要等价配置的能力。

## 选择目标网关

建议遵循“先评估环境，再分析注解，最后选择目标网关”的顺序。

### 优先选择 Higress

以下情况建议优先选择 Higress：

- 集群尚未安装 Gateway API CRD，或暂不计划引入 Gateway API。
- 希望继续使用 Ingress 资源，并尽量少改现有 YAML。
- 大量使用 `canary`、`cors-*`、`redirect`、`affinity`、`proxy-ssl-*` 等
  ingress-nginx 风格注解。

Higress 支持较多常见的 ingress-nginx 注解。对于不兼容的能力，还可以评估
Higress 原生注解、内置 Wasm 插件或自定义 Wasm 插件。

### 优先选择 kgateway

同时满足以下条件时，可以优先选择 kgateway：

- 集群已安装 Gateway API CRD，并满足 kgateway 的版本要求。
- 现有配置主要使用重写、超时、限流和基础认证等通用能力。
- 计划将 Ingress 资源逐步转换为 Gateway API 资源。
- ingress2gateway 能够转换当前使用的大部分注解。

## 迁移前评估

### 准备工具

执行评估前，请准备：

- 能够访问目标集群的 kubeconfig。
- [`kubectl`](https://kubernetes.io/zh-cn/docs/tasks/tools/)。
- [`jq`](https://jqlang.github.io/jq/)。
- 下文提供的 `ingress_annotation_analyzer.sh`。
- 迁移到 kgateway 时需要
  [`ingress2gateway`](https://github.com/kubernetes-sigs/ingress2gateway)。

### 运行评估脚本

将以下内容保存为 `ingress_annotation_analyzer.sh`：

```bash
#!/usr/bin/env bash

set -euo pipefail

BASE_EVAL="kgateway v2.2 & Higress v2.2.0"
KUBECONFIG_PATH=${KUBECONFIG:-"$HOME/.kube/config"}
VERBOSE=false

GREEN="\033[0;32m"
YELLOW="\033[0;33m"
RED="\033[0;31m"
BOLD_BLUE="\033[1;34m"
NC="\033[0m"

HIGRESS_NATIVE_SUPPORTED=(
  canary
  canary-by-cookie
  canary-by-header
  canary-by-header-pattern
  canary-by-header-value
  canary-weight
  canary-weight-total
  default-backend
  custom-http-errors
  rewrite-target
  use-regex
  upstream-vhost
  app-root
  ssl-redirect
  force-ssl-redirect
  temporal-redirect
  permanent-redirect
  permanent-redirect-code
  enable-cors
  cors-allow-origin
  cors-allow-methods
  cors-allow-headers
  cors-expose-headers
  cors-allow-credentials
  cors-max-age
  proxy-next-upstream
  proxy-next-upstream-timeout
  proxy-next-upstream-tries
  backend-protocol
  proxy-ssl-secret
  proxy-ssl-verify
  proxy-ssl-name
  proxy-ssl-server-name
  load-balance
  upstream-hash-by
  affinity
  affinity-mode
  affinity-canary-behavior
  session-cookie-name
  session-cookie-path
  session-cookie-max-age
  session-cookie-expires
  whitelist-source-range
  auth-tls-secret
)

HIGRESS_EQUIVALENT_SUPPORTED=(
  proxy-connect-timeout
  proxy-read-timeout
  proxy-send-timeout
  limit-rps
  limit-rpm
  limit-burst-multiplier
  auth-type
  auth-secret
  auth-secret-type
  auth-realm
  auth-url
  auth-response-headers
  auth-tls-verify-client
  auth-tls-verify-depth
  auth-tls-match-cn
  auth-tls-pass-certificate-to-upstream
)

KGATEWAY_NATIVE_SUPPORTED=(
  canary
  canary-by-header
  canary-by-header-pattern
  canary-by-header-value
  canary-weight
  canary-weight-total
  rewrite-target
  use-regex
  force-ssl-redirect
  ssl-redirect
  enable-cors
  cors-allow-origin
  cors-allow-methods
  cors-allow-headers
  cors-expose-headers
  cors-allow-credentials
  cors-max-age
  limit-burst-multiplier
  limit-rpm
  limit-rps
  proxy-connect-timeout
  proxy-read-timeout
  proxy-send-timeout
  affinity
  load-balance
  session-cookie-domain
  session-cookie-expires
  session-cookie-max-age
  session-cookie-name
  session-cookie-path
  session-cookie-samesite
  session-cookie-secure
  backend-protocol
  proxy-ssl-name
  proxy-ssl-secret
  proxy-ssl-server-name
  proxy-ssl-verify
  auth-response-headers
  auth-secret
  auth-secret-type
  auth-type
  auth-url
  client-body-buffer-size
  proxy-body-size
)

KGATEWAY_EQUIVALENT_SUPPORTED=(
  default-backend
  custom-http-errors
  upstream-vhost
  app-root
  temporal-redirect
  permanent-redirect
  permanent-redirect-code
  proxy-next-upstream
  proxy-next-upstream-timeout
  proxy-next-upstream-tries
  auth-tls-secret
  whitelist-source-range
)

print_header() {
  echo -e "\n${BOLD_BLUE}$1${NC}"
}

contains() {
  local needle="$1"
  shift
  local item
  for item in "$@"; do
    [[ "$item" == "$needle" ]] && return 0
  done
  return 1
}

higress_equivalent_hint() {
  case "$1" in
    proxy-connect-timeout|proxy-read-timeout|proxy-send-timeout)
      echo "higress.io/timeout"
      ;;
    limit-rps)
      echo "higress.io/route-limit-rps"
      ;;
    limit-rpm)
      echo "higress.io/route-limit-rpm"
      ;;
    limit-burst-multiplier)
      echo "higress.io/route-limit-burst-multiplier"
      ;;
    auth-type|auth-secret|auth-secret-type|auth-realm)
      echo "basic-auth Wasm plugin"
      ;;
    auth-url|auth-response-headers)
      echo "auth plugin or external auth"
      ;;
    auth-tls-verify-client|auth-tls-verify-depth|auth-tls-match-cn|auth-tls-pass-certificate-to-upstream)
      echo "Higress mTLS or certificate auth"
      ;;
    *)
      echo "Higress equivalent capability"
      ;;
  esac
}

kgateway_equivalent_hint() {
  case "$1" in
    default-backend|custom-http-errors|upstream-vhost|app-root|temporal-redirect|permanent-redirect|permanent-redirect-code)
      echo "ingress2gateway"
      ;;
    proxy-next-upstream|proxy-next-upstream-timeout|proxy-next-upstream-tries|auth-tls-secret|whitelist-source-range)
      echo "kgateway policy"
      ;;
    *)
      echo "ingress2gateway or kgateway policy"
      ;;
  esac
}

parse_args() {
  while [[ $# -gt 0 ]]; do
    case "$1" in
      -v|--verbose)
        VERBOSE=true
        shift
        ;;
      --kubeconfig)
        [[ $# -ge 2 ]] || {
          echo "Error: --kubeconfig requires a path" >&2
          exit 2
        }
        KUBECONFIG_PATH="$2"
        shift 2
        ;;
      -h|--help)
        echo "Usage: $0 [--kubeconfig <path>] [-v|--verbose]"
        exit 0
        ;;
      *)
        echo "Error: unknown argument: $1" >&2
        exit 2
        ;;
    esac
  done
}

main() {
  parse_args "$@"

  [[ -f "$KUBECONFIG_PATH" ]] || {
    echo "Error: kubeconfig not found: $KUBECONFIG_PATH" >&2
    exit 1
  }
  command -v kubectl >/dev/null || {
    echo "Error: kubectl is required" >&2
    exit 1
  }
  command -v jq >/dev/null || {
    echo "Error: jq is required" >&2
    exit 1
  }

  local version_json k8s_ver k8s_major k8s_minor
  local gateway_crd_count ingress_json ingress_count annotations annotation_count

  version_json=$(kubectl --kubeconfig "$KUBECONFIG_PATH" version -o json)
  k8s_ver=$(jq -r '.serverVersion.gitVersion' <<<"$version_json")
  k8s_major=$(jq -r '.serverVersion.major' <<<"$version_json" | tr -cd '0-9')
  k8s_minor=$(jq -r '.serverVersion.minor' <<<"$version_json" | tr -cd '0-9')

  gateway_crd_count=$(
    kubectl --kubeconfig "$KUBECONFIG_PATH" get crd -o name |
      grep -c '\.gateway\.networking\.k8s\.io$' || true
  )
  ingress_json=$(kubectl --kubeconfig "$KUBECONFIG_PATH" get ingress -A -o json)
  ingress_count=$(jq '.items | length' <<<"$ingress_json")
  annotations=$(
    jq -r '
      .items[].metadata.annotations // {}
      | keys[]
      | select(startswith("nginx.ingress.kubernetes.io/"))
    ' <<<"$ingress_json" | sort -u
  )
  if [[ -n "$annotations" ]]; then
    annotation_count=$(wc -l <<<"$annotations" | tr -d ' ')
  else
    annotation_count=0
  fi

  local meets_version_baseline=false
  if (( k8s_major > 1 || (k8s_major == 1 && k8s_minor >= 26) )); then
    meets_version_baseline=true
  fi

  echo -e "${BOLD_BLUE}>>> Compatibility report based on ${BASE_EVAL} <<<${NC}"
  print_header "1. Cluster information"
  printf "%-32s %s\n" "Kubeconfig:" "$KUBECONFIG_PATH"
  printf "%-32s %s\n" "Kubernetes version:" "$k8s_ver"
  printf "%-32s %s\n" "Meets K8s v1.26+ baseline:" "$meets_version_baseline"
  printf "%-32s %s\n" "Gateway API CRDs:" "$gateway_crd_count"
  printf "%-32s %s\n" "Ingress resources:" "$ingress_count"
  printf "%-32s %s\n" "Unique NGINX annotations:" "$annotation_count"

  local kgateway_supported=0 higress_supported=0
  local full_key suffix kgateway_status higress_status

  if [[ "$VERBOSE" == true ]]; then
    print_header "2. Annotation compatibility details"
    printf "%-65s %-34s %s\n" "Annotation" "kgateway" "Higress"
  fi

  while IFS= read -r full_key; do
    [[ -n "$full_key" ]] || continue
    suffix="${full_key#nginx.ingress.kubernetes.io/}"
    kgateway_status="${RED}no${NC}"
    higress_status="${RED}no${NC}"

    if contains "$suffix" "${KGATEWAY_NATIVE_SUPPORTED[@]}"; then
      kgateway_status="${GREEN}yes${NC}"
      ((kgateway_supported += 1))
    elif contains "$suffix" "${KGATEWAY_EQUIVALENT_SUPPORTED[@]}"; then
      kgateway_status="${YELLOW}yes* ($(kgateway_equivalent_hint "$suffix"))${NC}"
      ((kgateway_supported += 1))
    fi

    if contains "$suffix" "${HIGRESS_NATIVE_SUPPORTED[@]}"; then
      higress_status="${GREEN}yes${NC}"
      ((higress_supported += 1))
    elif contains "$suffix" "${HIGRESS_EQUIVALENT_SUPPORTED[@]}"; then
      higress_status="${YELLOW}yes* ($(higress_equivalent_hint "$suffix"))${NC}"
      ((higress_supported += 1))
    fi

    if [[ "$VERBOSE" == true ]]; then
      printf "%-65s %-43b %b\n" "$full_key" "$kgateway_status" "$higress_status"
    fi
  done <<<"$annotations"

  print_header "2. Compatibility summary"
  printf "%-12s %s / %s\n" "kgateway:" "$kgateway_supported" "$annotation_count"
  printf "%-12s %s / %s\n" "Higress:" "$higress_supported" "$annotation_count"

  print_header "3. Recommendation"
  if [[ "$meets_version_baseline" != true || "$gateway_crd_count" -eq 0 ]]; then
    echo -e "Result: ${GREEN}Higress${NC}"
    echo "Reason: the cluster does not meet the recommended Gateway API prerequisites."
  elif (( kgateway_supported > higress_supported )); then
    echo -e "Result: ${GREEN}kgateway${NC}"
    echo "Reason: kgateway covers more of the annotations currently in use."
  else
    echo -e "Result: ${GREEN}Higress${NC}"
    echo "Reason: Higress covers at least as many annotations and usually requires fewer changes to existing Ingress resources."
  fi

  echo
  echo "yes: natively supported; yes*: requires conversion, an equivalent annotation, or a policy/plugin."
  echo "Review every partially supported or unsupported annotation before migration."
}

main "$@"
```

为脚本添加执行权限，然后运行：

```bash
chmod +x ingress_annotation_analyzer.sh

# 使用默认 kubeconfig
./ingress_annotation_analyzer.sh

# 指定 kubeconfig 并显示逐项兼容性
./ingress_annotation_analyzer.sh \
  --kubeconfig /path/to/cluster-kubeconfig \
  --verbose
```

脚本输出包括：

1. **集群信息**：Kubernetes 版本、Gateway API CRD、Ingress 资源和注解数量。
2. **兼容性汇总**：两个目标网关可以承接的注解数量。
3. **逐项明细**：使用 `--verbose` 时显示每个注解的兼容情况。
4. **初步建议**：结合环境条件和注解覆盖率推荐目标网关。

其中 `yes` 表示原生兼容，`yes*` 表示需要使用 ingress2gateway、等价注解、
kgateway 策略或 Higress 插件承接。

## 根据评估结果迁移

### 迁移到 Higress

如果脚本推荐 Higress，请按以下步骤操作：

1. 参考[安装 Higress](../higress/install.md)在目标集群安装 Higress。
2. 确认 Higress Pod、Service 和 IngressClass 状态正常。
3. 将测试 Ingress 切换到 Higress，并逐项验证注解行为。
4. 对不兼容或部分兼容的注解，使用 `higress.io/*` 注解、内置 Wasm 插件或自定义插件补齐。

Higress 官方兼容列表参见
[Nginx Ingress Annotation 兼容说明](https://higress.ai/docs/latest/user/annotation/)。

### 迁移到 kgateway

如果脚本推荐 kgateway，请按以下步骤操作：

1. 参考[安装 kgateway](../kgateway/install.md)安装组件，并确保 Gateway API CRD 已安装。
2. 确认 kgateway Controller 与目标 GatewayClass 状态正常。
3. 安装 [ingress2gateway](https://github.com/kubernetes-sigs/ingress2gateway)。
4. 转换现有 Ingress，审核生成的资源后再应用。

转换整个集群中的 ingress-nginx 资源：

```bash
ingress2gateway print \
  --all-namespaces \
  --providers=ingress-nginx \
  --emitter=kgateway \
  --output=yaml \
  > converted-gateway-api.yaml
```

显式指定 kubeconfig：

```bash
ingress2gateway print \
  --kubeconfig /path/to/cluster-kubeconfig \
  --all-namespaces \
  --providers=ingress-nginx \
  --emitter=kgateway \
  --output=yaml \
  > converted-gateway-api.yaml
```

!!! warning

    不要把生成和应用操作连接成一条命令。请先审核 `converted-gateway-api.yaml`，
    并处理 ingress2gateway 输出的警告，再将资源应用到测试环境。

审核完成后执行：

```bash
kubectl --kubeconfig /path/to/cluster-kubeconfig \
  apply -f converted-gateway-api.yaml
```

如需只转换一个命名空间，请将 `--all-namespaces` 替换为 `--namespace <namespace>`。
即使脚本推荐 kgateway，也应重点检查部分兼容或需要手动补齐的能力。

## 切换生产流量

卸载 ingress-nginx 前，请确认：

- Higress 或 kgateway 已安装且配置生效。
- 新网关 Service 已通过 LoadBalancer 等方式暴露。
- 已获取新的外部地址，并完成基础连通性验证。
- 监控、日志和回滚方案均已准备就绪。

### 切换到新的负载均衡地址

1. 保持 ingress-nginx 运行。
2. 安装并验证新网关。
3. 获取新网关 Service 的 LoadBalancer 地址。
4. 使用加权 DNS、外部负载均衡器或平台流量拆分能力，逐步将流量切换到新地址。
5. 观察访问日志、错误率、延迟和资源使用情况。
6. 确认业务稳定后，再下线 ingress-nginx。

### 复用原负载均衡 IP

如果基础设施支持保留负载均衡 IP：

1. 确认原 ingress-nginx 的 IP 可以解绑并重新绑定。
2. 通过静态 IP、Service 注解或云资源绑定，让新网关复用该 IP。
3. 在维护窗口内完成绑定切换。
4. 验证外部访问已由新网关承接。
5. 确认稳定后删除 ingress-nginx。

## 验证迁移结果

至少验证以下内容：

- **基础连通性**：DNS 解析、HTTP/HTTPS 访问和 TLS 证书。
- **路由行为**：Host、Path、重写与重定向。
- **流量治理**：CORS、灰度、超时、重试和限流。
- **安全策略**：Basic Auth、外部认证、mTLS 和 IP 访问控制。
- **可观测性**：访问日志、指标、错误率和延迟。
- **异常响应**：重点排查 404、503 和 TLS 握手失败。

只有在测试环境和生产流量验证均通过后，才应删除原 ingress-nginx 控制器及相关资源。
