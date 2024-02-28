# The istio-ingressgateway is abnormal when hosting the mesh management cluster

## Situation analysis

It is common to see __istio-ingressgateway__ components become unhealthy when hosted meshs host workload clusters.

As shown below:

![unhealthy](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/troubleshoot/images/hosted01.png)

First check the istio-ingressgateway log error message:

```bash
2023-04-25T12:18:04.657568Z info JWT policy is third-party-jwt
2023-04-25T12:18:04.657573Z info using credential fetcher of JWT type in cluster.local trust domain
2023-04-25T12:18:06.658680Z info Workload SDS socket not found. Starting Istio SDS Server
2023-04-25T12:18:06.658716Z info CA Endpoint istiod.istio-system.svc:15012, provider Citadel
2023-04-25T12:18:06.658747Z info Using CA istiod.istio-system.svc:15012 cert with certs: var/run/secrets/istio/root-cert.pem
2023-04-25T12:18:06.667981Z info Opening status port 15020
2023-04-25T12:18:06.694111Z info ads All caches have been synced up in 2.053719558s, marking server ready
2023-04-25T12:18:06.694864Z info xdsproxy Initializing with upstream address "istiod-remote.istio-system.svc:15012" and cluster "yw55"
2023-04-25T12:18:06.696385Z info sds Starting SDS grpc server
2023-04-25T12:18:06.696568Z info starting Http service at 127.0.0.1:15004
2023-04-25T12:18:06.698950Z info Pilot SAN: [istiod-remote.istio-system.svc]
2023-04-25T12:18:06.705118Z info Starting proxy agent
2023-04-25T12:18:06.705177Z info starting
2023-04-25T12:18:06.705214Z info Envoy command: [-c etc/istio/proxy/envoy-rev.json --restart-epoch 0 --drain-time-s 45 --parent-shutdown-time- s 60 --local-address-ip-version v4 --file-flush-interval-msec 1000 --log-format %Y-%m-%dT%T.%fZ %l envoy %n %v -l warning --component-log-level misc:error]
2023-04-25T12:18:07.696708Z info cache generated new workload certificate latency=1.001557215s ttl=23h59m59.303308657s
2023-04-25T12:18:07.696756Z info cache Root cert has changed, start rotating root cert
2023-04-25T12:18:07.696785Z info ads XDS: Incremental Pushing:0 ConnectedEndpoints:0 Version:
2023-04-25T12:18:07.696896Z info cache returned workload trust anchor from cache ttl=23h59m59.303107754s
2023-04-25T12:19:07.664759Z warning envoy config StreamAggregatedResources gRPC config stream to xds-grpc closed since 40s ago: 14, connection error: desc = "transport: Error while dialing dial tcp 10.233.48.75 :15012: i/o timeout"
2023-04-25T12:19:29.530922Z warning envoy config StreamAggregatedResources gRPC config stream to xds-grpc closed since 62s ago: 14, connection error: desc = "transport: Error while dialing dial tcp 10.233.48.75 :15012: i/o timeout"
2023-04-25T12:19:51.228936Z warning envoy config StreamAggregatedResources gRPC config stream to xds-grpc closed since 84s ago: 14, connection error: desc = "transport: Error while dialing dial tcp 10.233.48.75 :15012: i/o timeout"
2023-04-25T12:20:11.732449Z warning envoy config StreamAggregatedResources gRPC config stream to xds-grpc closed since 104s ago: 14, connection error: desc = "transport: Error while dialing dial tcp 10.233.48.7 5:15012: i/o timeout"
2023-04-25T12:20:41.426914Z warning envoy config StreamAggregatedResources gRPC config stream to xds-grpc closed since 134s ago: 14, connection error: desc = "transport: Error while dialing dial tcp 10.233.48.7 5:15012: i/o timeout"
2023-04-25T12:21:15.199447Z warning envoy config StreamAggregatedResources gRPC config stream to xds-grpc closed since 168s ago: 14, connection error: desc = "transport: Error while dialing dial tcp 10.233.48.7 5:15012: i/o timeout"
```

The above error message shows that the connection to __10.233.48.75:15012__ is __istiod-remote__ ’s service ip:15012 timeout !!!.

At this point we look at the __endpoint__ of __istiod-remote__ under the __istio-system__ namespace.

```bash
kubectl get ep -n istio-system
```
```none
NAME ENDPOINTS AGE
istio-eastwestgateway 36s
istio-ingressgateway 10m
istiod 10.233.97.220:15012,10.233.97.220:15010,10.233.97.220:15017 + 1 more... 10m
istiod-remote 10.233.95.141:15012,10.233.95.141:15017 10m
```

It can be seen here that the __endpoint__ address assigned by __istio-remote__ is __istiod-remote 10.233.95.141:15012,10.233.95.141:15017__ . As shown below:

![timeout](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/troubleshoot/images/hosted02.png)

!!! note

     When the workload cluster is connected to the hosted mesh, the endpoint address of istiod-remote should be allocated as
     loadBalancer IP of istiod-xxxx-hosted-lb service: 15012,
     But here it is assigned as the istiod-xxxx-hosted-xxxx Pod IP of the control plane cluster.

## Solution

Update the control plane address in the mesh __basic information__ configuration:

1. Log in to the control plane cluster and run the following command to obtain this address:

     ```bash
     kubectl get svc -n istio-system istiod-ywistio-hosted-lb -o "jsonpath={.status.loadBalancer.ingress[0].ip}"
     ```

    ![get url](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/troubleshoot/images/hosted03.png)     

1. Click the menu on the right and select __Edit Basic Information__ .

     

1. Fill in the control plane address.

     

1. Check the __istio-ingressgateway__ of the workload cluster again, and find that it is normal now.

    ![view cluster status](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/troubleshoot/images/hosted06.png)

1. View __istiod-remote endpoint__ information is also normal.

    ![view info](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/troubleshoot/images/hosted07.png)
