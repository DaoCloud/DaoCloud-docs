# Migrate to Higress or kgateway

This page describes the selection approach, implementation steps, and verification methods for
migrating from ingress-nginx to Higress or kgateway. It applies to existing users who want to
preserve their current Ingress YAML and annotations as much as possible.

!!! warning

    ingress-nginx was retired in March 2026. Existing deployments can continue to run and the
    installation artifacts are still available, but the project no longer releases new versions,
    fixes bugs, or handles newly discovered security vulnerabilities. Evaluate and migrate to a
    still-maintained ingress gateway as soon as possible. For details, see the
    [Ingress2Gateway 1.0 release announcement](https://kubernetes.io/blog/2026/03/20/ingress2gateway-1-0-release/).

## Migration Background and Goals

The Kubernetes Ingress API can only express basic Layer 7 routing capabilities. ingress-nginx extends
traffic governance capabilities through a large number of private annotations, but these extensions are
coupled to the specific implementation and are difficult to migrate directly to other controllers.
At the same time, the Kubernetes networking ecosystem is moving to the
[Gateway API](https://gateway-api.sigs.k8s.io/), and new gateway products are also built around
the Gateway API first.

Migration is not just about replacing the controller. It should also achieve the following goals:

- Preserve compatibility with existing Ingress resources and `nginx.ingress.kubernetes.io/*`
  annotations as much as possible.
- Minimize business YAML changes, the switching window, and downtime.
- Lay the foundation for later adoption of capabilities such as the Gateway API, plugin extensions,
  security governance, and canary releases.

This page uses **Higress v2.2.0** and **kgateway v2.2** as the evaluation baseline:

- **Higress** has good compatibility with common ingress-nginx annotations, and is suitable for
  prioritizing the reduction of existing migration costs.
- **kgateway** targets the Gateway API and is suitable for clusters that plan to adopt standard
  Gateway API resources.

!!! note

    No gateway can be fully compatible with all ingress-nginx annotations. The selection script
    can only provide preliminary suggestions. Before migration, you still need to check item by item
    the capabilities that are unsupported, partially compatible, or require equivalent configuration.

## Choose the Target Gateway

The recommended order is: evaluate the environment first, then analyze the annotations, and finally
choose the target gateway.

### Prefer Higress

Higress is recommended in the following cases:

- The Gateway API CRDs are not installed in the cluster, or there is no plan to introduce the Gateway API yet.
- You want to continue using Ingress resources and change the existing YAML as little as possible.
- You heavily use ingress-nginx style annotations such as `canary`, `cors-*`, `redirect`, `affinity`,
  and `proxy-ssl-*`.

Higress supports many common ingress-nginx annotations. For incompatible capabilities, you can also
evaluate Higress native annotations, built-in Wasm plugins, or custom Wasm plugins.

### Prefer kgateway

kgateway can be preferred when all of the following conditions are met:

- The Gateway API CRDs are installed in the cluster and the kgateway version requirements are met.
- The existing configuration mainly uses common capabilities such as rewrite, timeout, rate limiting,
  and basic authentication.
- You plan to gradually convert Ingress resources into Gateway API resources.
- ingress2gateway can convert most of the annotations currently in use.

## Pre-Migration Evaluation

### Prepare the Tools

Before performing the evaluation, prepare:

- A kubeconfig that can access the target cluster.
- [`kubectl`](https://kubernetes.io/docs/tasks/tools/).
- [`jq`](https://jqlang.github.io/jq/).
- The `ingress_annotation_analyzer.sh` provided below.
- [`ingress2gateway`](https://github.com/kubernetes-sigs/ingress2gateway), required when migrating
  to kgateway.

### Run the Evaluation Script

Save the following content as `ingress_annotation_analyzer.sh`:

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

Add the execution permission to the script and run it:

```bash
chmod +x ingress_annotation_analyzer.sh

# Use the default kubeconfig
./ingress_annotation_analyzer.sh

# Specify a kubeconfig and show per-item compatibility
./ingress_annotation_analyzer.sh \
  --kubeconfig /path/to/cluster-kubeconfig \
  --verbose
```

The script output includes:

1. **Cluster information**: Kubernetes version, Gateway API CRDs, Ingress resources, and annotation count.
2. **Compatibility summary**: The number of annotations that the two target gateways can take over.
3. **Per-item details**: When `--verbose` is used, the compatibility of each annotation is displayed.
4. **Preliminary recommendation**: The target gateway recommended based on the environment conditions
   and annotation coverage.

Here, `yes` means natively compatible, and `yes*` means it needs to be taken over by ingress2gateway,
an equivalent annotation, a kgateway policy, or a Higress plugin.

## Migrate Based on the Evaluation Result

### Migrate to Higress

If the script recommends Higress, perform the following steps:

1. Refer to [Install Higress](../higress/install.md) to install Higress in the target cluster.
2. Confirm that the Higress Pod, Service, and IngressClass are in a normal state.
3. Switch the test Ingress to Higress and verify the annotation behavior item by item.
4. For incompatible or partially compatible annotations, use `higress.io/*` annotations, built-in
   Wasm plugins, or custom plugins to fill the gaps.

For the official Higress compatibility list, see
[Nginx Ingress Annotation compatibility](https://higress.ai/docs/latest/user/annotation/).

### Migrate to kgateway

If the script recommends kgateway, perform the following steps:

1. Refer to [Install kgateway](../kgateway/install.md) to install the component, and make sure the
   Gateway API CRDs are installed.
2. Confirm that the kgateway Controller and the target GatewayClass are in a normal state.
3. Install [ingress2gateway](https://github.com/kubernetes-sigs/ingress2gateway).
4. Convert the existing Ingress resources, review the generated resources, and then apply them.

Convert the ingress-nginx resources in the entire cluster:

```bash
ingress2gateway print \
  --all-namespaces \
  --providers=ingress-nginx \
  --emitter=kgateway \
  --output=yaml \
  > converted-gateway-api.yaml
```

Specify the kubeconfig explicitly:

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

    Do not chain the generation and application operations into a single command. Review
    `converted-gateway-api.yaml` first and handle the warnings output by ingress2gateway before
    applying the resources to the test environment.

After the review is complete, run:

```bash
kubectl --kubeconfig /path/to/cluster-kubeconfig \
  apply -f converted-gateway-api.yaml
```

To convert only one namespace, replace `--all-namespaces` with `--namespace <namespace>`.
Even if the script recommends kgateway, you should still focus on checking the capabilities that are
partially compatible or require manual completion.

## Switch Production Traffic

Before uninstalling ingress-nginx, confirm that:

- Higress or kgateway is installed and the configuration takes effect.
- The new gateway Service is exposed through a LoadBalancer or another method.
- The new external address is obtained and basic connectivity verification is complete.
- Monitoring, logging, and rollback plans are ready.

### Switch to a New Load Balancer Address

1. Keep ingress-nginx running.
2. Install and verify the new gateway.
3. Obtain the LoadBalancer address of the new gateway Service.
4. Use weighted DNS, an external load balancer, or the platform traffic splitting capability to
   gradually switch traffic to the new address.
5. Observe access logs, error rate, latency, and resource usage.
6. After confirming that the business is stable, take ingress-nginx offline.

### Reuse the Original Load Balancer IP

If the infrastructure supports preserving the load balancer IP:

1. Confirm that the IP of the original ingress-nginx can be unbound and rebound.
2. Let the new gateway reuse that IP through a static IP, a Service annotation, or cloud resource binding.
3. Complete the binding switch within the maintenance window.
4. Verify that external access is taken over by the new gateway.
5. After confirming stability, delete ingress-nginx.

## Verify the Migration Result

At least verify the following:

- **Basic connectivity**: DNS resolution, HTTP/HTTPS access, and TLS certificates.
- **Routing behavior**: Host, Path, rewrite, and redirect.
- **Traffic governance**: CORS, canary release, timeout, retry, and rate limiting.
- **Security policies**: Basic Auth, external authentication, mTLS, and IP access control.
- **Observability**: Access logs, metrics, error rate, and latency.
- **Abnormal responses**: Focus on troubleshooting 404, 503, and TLS handshake failures.

Only after both the test environment and production traffic verification pass should you delete the
original ingress-nginx controller and its related resources.
