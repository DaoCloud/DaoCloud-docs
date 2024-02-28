# Multicluster grayscale release

The implementation logic of multicluster grayscale release is to deploy different business applications in different clusters, then configure corresponding policies through the service mesh to realize traffic adjustment between business versions, and then offline the versions according to the running conditions.

For pre-preparation, refer to the mesh multicloud deployment document to build the mesh infrastructure.

## Create a demo application and verify traffic

### Cluster deployment v1 version helloworld

First select a namespace (gray-demo), and enable the namespace sidecar injection on the mesh page.

Deploy the application on Workbench, here we take the helloworld of istio as an example.



Select the corresponding cluster (mdemo-cluster2) and namespace, and configure basic workload information.



- Select image: docker.m.daocloud.io/istio/examples-helloworld-v1
- version: latest

Configure service information:

- Access type: intra-cluster access
- port configuration

     - Protocol: TCP
     - Name: http-5000
     - container port: 5000
     - Service port: 5000





In order to distinguish different versions of workloads, you need to find the corresponding workloads in __Container Management Platform__ , click __Labels and Annotations__ , and add key-value pairs to pod tags:
"version": "v1"





### Cluster deployment v2 version helloworld

> Note that the service name must be the same as the namespace.

First select the above consistent namespace (gray-demo), and enable sidecar injection of this namespace on the mesh page.

The deployment process is the same as above, the main differences are:

- Image changed: `docker.m.daocloud.io/istio/examples-helloworld-v2` 
- Add label "version": "v2" to the corresponding **pod label** on the container platform

## Deploy grayscale application strategy

### Multicluster Destination Rules

First create a DestinationRule, and define the business versions of different clusters by defining SubSet.

Its label key-value pair is the pod label added above: __version: <VERSION>__ .

Policy: Istio Mutual TLS must be enabled





**Istio Mutual** TLS mode must be enabled



The target rule YAML is as follows:

```yaml
apiVersion: networking.istio.io/v1beta1
kind: DestinationRule
metadata:
   name: helloworld
   namespace: gray-demo
spec:
   host: helloworld
   subsets:
     - labels:
         version: v1
       name: v1
       trafficPolicy:
         tls:
           mode: ISTIO_MUTUAL
     - labels:
         version: v2
       name: v2
       trafficPolicy:
         tls:
           mode: ISTIO_MUTUAL
   trafficPolicy:
     tls:
       mode: ISTIO_MUTUAL
```

### Expose services through ingress

First you need to create a gateway rule:



The gateway rule YAML is as follows:

```yaml
apiVersion: networking.istio.io/v1alpha3
kind: Gateway
metadata:
   name: gray-demo-gateway
   namespace: gray-demo
spec:
   selector:
     istio: ingressgateway # use istio default controller
   servers:
     - port:
         number: 80
         name: http
         protocol: HTTP
       hosts:
         - "*"
```

Then configure the virtual service rules required to access the service.





The virtual service YAML is as follows:

```yaml
apiVersion: networking.istio.io/v1beta1
kind: VirtualService
metadata:
   name: gray-demo-vs
   namespace: gray-demo
spec:
   gateways:
     - gray-demo-gateway
   hosts:
     - "*"
   http:
     - name: http-5000
       route:
         -destination:
             host: helloworld.gray-demo.svc.cluster.local
             port:
               number: 5000
             subset: v1
           weight: 80
         -destination:
             host: helloworld.gray-demo.svc.cluster.local
             port:
               number: 5000
             subset: v2
           weight: 20
```

## Verify

**INGRESS_LB_IP** refers to the Ingress mesh load balancing address, which can be viewed in the container management platform. If there is no valid load balancing IP, it can be accessed through NodePort.



(Because the container management platform interface cannot directly view the external IP, so use the ability of the console to view)

Visit in browser: http://${INGRESS_LB_IP}/hello

Confirm that the access ratio of its v1 to v2 version is 8:2 with the ratio of the above policy


