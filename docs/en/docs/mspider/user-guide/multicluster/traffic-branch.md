# Multi-cloud network traffic distribution configuration under the mesh

This page describes how to configure different traffic flows for workloads in a multi-cloud network.

Preconditions:

- The service `helloworld` runs under the namespace `helloworld` of the mesh `hosted-mesh`
- Enable multi-cloud network interconnection
- Mesh provides ingressgatway gateway instance

Configuration steps:

1. Based on the cluster to which it belongs, the request traffic is divided by weight;

1. Label the `helloworld` workload of both clusters:

     | Belonging cluster | Label | Value |
     | ------------ | ------- | --- |
     | yl-cluster10 | version | v1 |
     | yl-cluster20 | version | v2 |

1. Click `Sidecar Management` -> `Workload Sidecar Management` in the left navigation bar to inject the sidecar into the helloworld workload of the two clusters.

1. On the left navigation bar, click `Traffic Governance` -> `Target Rules` -> `Create` to create two service versions.

     The corresponding YAML is as follows:

     ```yaml
     apiVersion: networking.istio.io/v1beta1
     kind: DestinationRule
     metadata:
       name: helloworld-version
       namespace: helloworld
     spec:
       host: helloworld
       subsets:
         - labels:
     ​ version: v1
     ​ name: v1
         - labels:
     ​ version: v2
           name: v2
     ```

1. On the left navigation bar, click `Traffic Governance` -> `Gateway Rules` -> `Create` to create a gateway rule.

     The corresponding YAML is as follows:

     ```yaml
     apiVersion: networking.istio.io/v1beta1
     kind: Gateway
     metadata:
       name: helloworld-gateway
       namespace: helloworld
     spec:
       selector:
         istio: ingressgateway
       servers:
         -hosts:
     ​ - hello.m.daocloud
           port:
     name: http
     ​number: 80
     ​ protocol: http
     ```

1. On the left navigation bar, click `Traffic Governance` -> `Virtual Service` -> `Create`, create routing rules, and divide traffic to two clusters based on the weight ratio:

     The corresponding YAML is as follows:

     ```yaml
     apiVersion: networking.istio.io/v1beta1
     kind: VirtualService
     metadata:
       name: helloworld-version
       namespace: helloworld
     spec:
       gateways:
         - helloworld-gateway
       hosts:
         - helloworld.helloworld.svc.cluster.local
       http:
         - match:
           - uri:
             exact: /hello
           name: helloworld-routes
           route:
             -destination:
               host: helloworld
               port:
                 number: 5000
               subset: v1
               weight: 30
             -destination:
               host: helloworld
               port:
                 number: 5000
                 subset: v2
               weight: 70
     ```

1. On the left navigation bar, click `mesh Configuration` -> `Multi-Cloud Network Interconnection` to enable multi-cloud network interconnection.

1. Initiate 1000 get requests through JMeter and set the assertion


1. View the request aggregation report (set the assertion helloworld v2), the success rate is 70%, and the exception rate is close to 30%.
