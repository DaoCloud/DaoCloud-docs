# Canary Release Example

This section describes a full-process example of a canary release based on different traffic management types.

# Canary Release - Based on Istio

## Preparations

### Prepare an Application

It can be created through [Workbench] - [Wizard] -> "Build With Git Repo" and "Build With Image", and
enable **Enable Mesh** on the last step, the Advanced Settings page.

![Create an application and enable mesh](../../images/canary-istio01.png)

After an application with **Enable Mesh** is created, a `VirtualService` and a `DestinationRule` with
the same name will be created automatically.

![Automatically created custom resources](../../images/canary-istio02.png)

The specific YAML is as follows:

```yaml
# VirtualService
apiVersion: networking.istio.io/v1
kind: VirtualService
metadata:
  labels:
    app.kubernetes.io/part-of: myapp-istio
  name: myapp-istio
  namespace: for-amamba
...
spec:
  hosts:
    - myapp-istio
  http:
    - name: primary
      route:
        - destination:
            host: myapp-istio
            subset: stable
          weight: 100
        - destination:
            host: myapp-istio
            subset: canary
```

```yaml
# DestinationRule
apiVersion: networking.istio.io/v1
kind: DestinationRule
metadata:
  labels:
    app.kubernetes.io/part-of: myapp-istio
  name: myapp-istio
  namespace: for-amamba
...
spec:
  host: myapp-istio
  subsets:
    - labels:
        app: myapp-istio
      name: stable
    - labels:
        app: myapp-istio
      name: canary
```

### Prepare a Gateway

Manually apply the following YAML to create a Gateway.

```yaml
# Gateway
apiVersion: networking.istio.io/v1
kind: Gateway
metadata:
  name: myapp-istio # a custom gateway name
  namespace: for-amamba # the namespace where the application is deployed
spec:
  selector:
    istio: ingressgateway # the default gateway of istio
  servers:
    - hosts:
        - '*'
      port:
        name: http
        number: 8081 # the service port in the Service of the deployed application, that is, the port in the Service. It needs to be kept consistent
        protocol: HTTP
```

![Application service](../../images/canary-istio03.png)

### Prepare a VirtualService

Because a `VirtualService` with the same name has been created automatically, you only need to update
two fields of the `VirtualService`: `spec.gateways` and `spec.hosts`. Note that if the application is
created in another mode, you need to manually create the `VirtualService` and `DestinationRule`
according to the YAML in "Prepare an Application".

```yaml
spec:
  gateways:
  - myapp-istio # the name of the prepared custom Gateway
  hosts:
  - '*' # it was originally the name of the deployed application, and needs to be updated to '*'
  http:
  - name: primary
    route:
    - destination:
        host: myapp-istio
        subset: stable
      weight: 100
    - destination:
        host: myapp-istio
        subset: canary
```

### Configure the istio-ingressgateway Gateway

```shell
kubectl edit svc istio-ingressgateway -n istio-system

# Add the following fields to spec.ports
  - name: myapp-istio # an arbitrary name
    port: 18081      # an arbitrary port, which must not conflict with other ports in istio-ingressgateway
    protocol: TCP    # the protocol of the deployed application
    targetPort: 8081 # the port of the deployed application
```

### Verify that the Application Can Be Accessed Through istio-ingressgateway

After the update is complete, run the command `curl ${node_ip}:${the nodePort corresponding to the newly added port in istio-ingressgateway}` to verify whether the deployed application can be accessed through `istio-ingressgateway`.

![Access the application through istio-ingressgateway](../../images/canary-istio04.png)

## Based on Weight

Create a release job - canary release, select Istio as the traffic management type and "Based on Weight" as the traffic scheduling type.

![Based on weight](../../images/canary-istio05.png)

During the canary release, access `${node_ip}:${the nodePort corresponding to the newly added port in istio-ingressgateway}`.

## Based on Request Characteristics

Create a release job - canary release, select Istio as the traffic management type and "Based on Request Characteristics" as the traffic scheduling type.

![Based on request characteristics](../../images/canary-istio06.png)

During the canary release, access `${node_ip}:${the nodePort corresponding to the newly added port in istio-ingressgateway}`. Note that when accessing with the request header that satisfies the traffic scheduling policy, you can access the new version; otherwise, you will access the original version.

```shell
curl -H 'pre-key:pre-value'  10.6.14.20:31406  
curl -H 'pre-key:test'  10.6.14.20:31406       
curl -H 'reg-key:reg-value'  10.6.14.20:31406  
curl -H 'reg-key:test'  10.6.14.20:31406       
curl -H 'key:value'  10.6.14.20:31406          
curl -H 'key:test'  10.6.14.20:31406           
```

![Release process](../../images/canary-istio07.png)

![After the release succeeds](../../images/canary-istio08.png)

## Enable Monitoring Analysis

⚠️ After monitoring analysis is enabled, `argo-rollouts` will continuously calculate the success rate/failure rate of the current release according to the metrics in `AnalysisRun`. If no request has ever been made, the calculated result will also be wrong, causing the release to roll back. Therefore, you need to ensure that requests are continuously accessing the service during the release.

![Enable monitoring analysis](../../images/canary-istio09.png)

When monitoring analysis is enabled, a `ServiceMonitor` will be created automatically.

![ServiceMonitor](../../images/canary-istio10.png)

After the canary release process is executed, an `AnalysisRun` will be created automatically. During the
canary release, the call records of the application are collected by the observability module, and the
`AnalysisRun` calculates whether the conditions are met according to the expression. The expression is as follows:

![AnalysisRun](../../images/canary-istio11.png)

In "Observability" - "Metrics" - "Advanced Query", enter the above expression to query the corresponding
metrics. `destination_service` is the service corresponding to the canary release. 

![metrics](../../images/canary-istio12.png)

If the monitoring analysis succeeds, it will be displayed as follows:

![result](../../images/canary-istio13.png)

# Canary Release - Based on Nginx

## Preparations

### Install ingress-nginx

First, you need to install `ingress-nginx` in the current cluster.

![Install ingress-nginx](../../images/canary-nginx01.png)

The NodePort type is used here. Note that if `LoadBalancer` is selected as the Type, `metallb` needs to be installed in the current cluster.

![ingress-nginx installed successfully](../../images/canary-nginx02.png)

### Prepare an Application

It can be created through [Workbench] - [Wizard] -> "Build With Git Repo" and "Build With Image".

![Create an application](../../images/canary-nginx03.png)

### Create a Route for the Application

![Create a route](../../images/canary-nginx04.png)

After the creation is complete, access the NodePort corresponding to port 80 of ingress-nginx. A normal
response indicates success.

![Access through the route](../../images/canary-nginx05.png)

## Based on Nginx

![Create a release job](../../images/canary-nginx06.png)

After updating the image version to v2, access the NodePort corresponding to port 80 of ingress-nginx.

```shell
i=0; while true; do curl www.test-myapp.com:30828; i=$((i+1));echo ${i}; sleep 1; done
```

After the release, the ratio of v1 to v2 is roughly 50% each. After you manually continue the release,
the traffic all flows to the v2 version.

![Access the application during the release](../../images/canary-nginx07.png)

After continuing the release and waiting for 10 minutes, the release is complete.

![Release complete](../../images/canary-nginx08.png)
