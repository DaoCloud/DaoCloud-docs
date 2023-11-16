# Gateway Management for External Mesh

The deployment and lifecycle management of the external mesh are the responsibility of the user. The installation method for the mesh gateway depends on the specific mesh deployment approach. You can follow the respective methods below to install the mesh gateway.

## Using the IstioOperator Approach

This method requires a pre-installed and deployed Istiod. You can perform the following steps:

First, create the corresponding configuration file for `ingress` or `egress`:

```yaml
apiVersion: install.istio.io/v1alpha1
kind: IstioOperator
metadata:
  name: ingress
spec:
  profile: empty # Do not install CRDs or control plane
  components:
    ingressGateways:
    - name: istio-ingressgateway
      namespace: istio-ingress
      enabled: true
      label:
        # Set a unique label for the gateway.
        # This ensures that the Gateway can select this workload when necessary.
        istio: ingressgateway
  values:
    gateways:
      istio-ingressgateway:
        # Enable gateway injection
        injectionTemplate: gateway
```

Then, install using the standard `istioctl` command:

```bash
kubectl create namespace istio-ingress
istioctl install -f ingress.yaml
```

## Using the Helm Approach

### Standard Kubernetes Cluster

For mesh deployments managed and deployed using Helm, it is recommended to continue using Helm for installing and maintaining the mesh gateway.

Before installing the mesh gateway with Helm, you can review the supported configuration values to confirm parameter settings:

```bash
helm show values istioi/gateway
```

Then, use the `helm install` command for installation:

```bash
kubectl create namespace istio-ingress
helm install istio-ingressgateway istio/gateway -n istio-ingress
```

### OpenShift Cluster

For an OpenShift cluster, the parameter configuration differs from a standard Kubernetes cluster. Istio provides recommended configurations in their official documentation:

```bash
helm install istio-ingressgateway istio/gateway -n istio-ingress -f manifests/charts/gateway/openshift-values.yaml
```

## Using the YAML Approach

Using YAML to install the mesh gateway separately does not affect the deployment of applications, but it requires the user to manage the gateway's lifecycle.

### Creating the Gateway Workload

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
        # Select the gateway injection template (instead of the default sidecar template)
        inject.istio.io/templates: gateway
      labels:
        # Set a unique label for the gateway. This ensures that the Gateway can select this workload when necessary.
        istio: ingressgateway
        # Enable gateway injection. If connected to a revised control plane, replace with `istio.io/rev: revision-name`
        sidecar.istio.io/inject: "true"
    spec:
      # Allow binding to all ports (e.g., 80 and 443)
      securityContext:
        sysctls:
        - name: net.ipv4.ip_unprivileged_port_start
          value: "0"
      containers:
      - name: istio-proxy
        image: auto # The image is automatically updated each time the Pod starts.
        # Drop all privilege capabilities, allowing it to run without root privilege
        securityContext:
          capabilities:
            drop:
            - ALL
          runAsUser: 1337
          runAsGroup: 1337
```

### Adding the Appropriate Permissions

```yaml
# Set the Role to allow reading TLS credentials
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

### Creating the Gateway Service

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

Managing the gateway workload independently significantly increases the complexity of maintenance tasks, including managing the gateway's lifecycle and configuration management. Therefore, it is recommended to use the Helm or IstioOperator methods for installation and management.

## More Installation Methods

Istio provides a variety of deployment approaches, and the above examples only mention a few popular ones. If you are using a different approach, please refer to the Istio documentation for more detailed information:

* Istio Operator Installation: [https://istio.io/docs/setup/install/operator/](https://istio.io/docs/setup/install/operator/)
* Gateway Resource: [https://istio.io/docs/reference/config/networking/gateway/](https://istio.io/docs/reference/config/networking/gateway/)
  