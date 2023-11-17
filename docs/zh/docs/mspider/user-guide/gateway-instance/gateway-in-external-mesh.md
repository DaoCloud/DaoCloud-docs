# 外接网格的网关管理

外接网格的部署和生命周期管理是由用户自行负责的。网格网关的安装方式取决于具体的网格部署方式，您可以按照以下相应方式来安装网格网关。

## 使用 IstioOperator 方式

这种方法需要依赖已经安装和部署完成的 Istiod。您可以按照以下步骤执行操作：

首先，创建对应的 `ingress` 或 `egress` 配置文件：

```yaml
apiVersion: install.istio.io/v1alpha1
kind: IstioOperator
metadata:
  name: ingress
spec:
  profile: empty # 不安装 CRD 或控制平面
  components:
    ingressGateways:
    - name: istio-ingressgateway
      namespace: istio-ingress
      enabled: true
      label:
        # 为网关设置唯一标签。
        # 这是确保 Gateway 可以选择此工作负载所必需的。
        istio: ingressgateway
  values:
    gateways:
      istio-ingressgateway:
        # 启用网关注入
        injectionTemplate: gateway
```

然后，使用标准的 `istioctl` 命令进行安装：

```bash
kubectl create namespace istio-ingress
istioctl install -f ingress.yaml
```

## 使用 Helm 方式

### 标准 Kubernetes 集群

对于通过 Helm 部署和管理的网格，建议仍然使用 Helm 安装和维护网格网关。

在使用 Helm 安装网格网关之前，您可以查看支持的配置值以确认参数配置：

```bash
helm show values istioi/gateway
```

然后，使用 `helm install` 命令进行安装：

```bash
kubectl create namespace istio-ingress
helm install istio-ingressgateway istio/gateway -n istio-ingress
```

### OpenShift 集群

对于 OpenShift 集群，其参数配置与标准 Kubernetes 集群不同，Istio 官方提供了推荐配置：

```bash
helm install istio-ingressgateway istio/gateway -n istio-ingress -f manifests/charts/gateway/openshift-values.yaml
```

## 使用 YAML 方式

使用 YAML 单独安装网格网关，这种方式不会影响应用的部署，但需要用户自行管理网关的生命周期。

### 创建网关工作负载

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: istio-ingressgateway
  namespace: istio-ingress
spec:
  selector:
    matchLabels:
      istio: ingressgateway
  template:
    metadata:
      annotations:
        # 选择网关注入模板（而不是默认的 Sidecar 模板）
        inject.istio.io/templates: gateway
      labels:
        # 为网关设置唯一标签。这是确保 Gateway 可以选择此工作负载所必需的
        istio: ingressgateway
        # 启用网关注入。如果后续连接到修订版的控制平面，请替换为 `istio.io/rev: revision-name`
        sidecar.istio.io/inject: "true"
    spec:
      # 允许绑定到所有端口（例如 80 和 443）
      securityContext:
        sysctls:
        - name: net.ipv4.ip_unprivileged_port_start
          value: "0"
      containers:
      - name: istio-proxy
        image: auto # 每次 Pod 启动时，该镜像都会自动更新。
        # 放弃所有 privilege 特权，允许以非 root 身份运行
        securityContext:
          capabilities:
            drop:
            - ALL
          runAsUser: 1337
          runAsGroup: 1337
```

### 添加相应权限

```yaml
# 设置 Role 以允许读取 TLS 凭据
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: istio-ingressgateway-sds
  namespace: istio-ingress
rules:
- apiGroups: [""]
  resources: ["secrets"]
  verbs: ["get", "watch", "list"]
---
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: istio-ingressgateway-sds
  namespace: istio-ingress
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: Role
  name: istio-ingressgateway-sds
subjects:
- kind: ServiceAccount
  name: default
```

### 创建网关服务

```yaml
apiVersion: v1
kind: Service
metadata:
  name: istio-ingressgateway
  namespace: istio-ingress
spec:
  type: LoadBalancer
  selector:
    istio: ingressgateway
  ports:
  - port: 80
    name: http
  - port: 443
    name: https
```

自行管理网关工作负载将大大增加维护工作的复杂性，包括管理网关的生命周期和配置管理等。因此，建议用户使用 Helm 或 IstioOperator 的方式进行安装和管理。

## 更多安装方式

Istio 提供了丰富的部署方式，上述仅列举了几种主流的部署方式。如果您使用的方式与上述方式不同，请参阅 Istio 文档以获取更多详细信息：

* Istio Operator 安装：[https://istio.io/docs/setup/install/operator/](https://istio.io/docs/setup/install/operator/)
* Gateway 资源：[https://istio.io/docs/reference/config/networking/gateway/](https://istio.io/docs/reference/config/networking/gateway/)
