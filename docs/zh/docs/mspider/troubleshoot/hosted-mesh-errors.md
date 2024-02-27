# 托管网格纳管集群时 istio-ingressgateway 异常

## 情况分析

当托管网格纳管工作负载集群时，常常会出现 __istio-ingressgateway__ 组件不健康。

如下图：

![不健康](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/troubleshoot/images/hosted01.png)

首先查看 istio-ingressgateway 日志报错信息：

```bash
2023-04-25T12:18:04.657568Z     info    JWT policy is third-party-jwt
2023-04-25T12:18:04.657573Z     info    using credential fetcher of JWT type in cluster.local trust domain
2023-04-25T12:18:06.658680Z     info    Workload SDS socket not found. Starting Istio SDS Server
2023-04-25T12:18:06.658716Z     info    CA Endpoint istiod.istio-system.svc:15012, provider Citadel
2023-04-25T12:18:06.658747Z     info    Using CA istiod.istio-system.svc:15012 cert with certs: var/run/secrets/istio/root-cert.pem
2023-04-25T12:18:06.667981Z     info    Opening status port 15020
2023-04-25T12:18:06.694111Z     info    ads     All caches have been synced up in 2.053719558s, marking server ready
2023-04-25T12:18:06.694864Z     info    xdsproxy        Initializing with upstream address "istiod-remote.istio-system.svc:15012" and cluster "yw55"
2023-04-25T12:18:06.696385Z     info    sds     Starting SDS grpc server
2023-04-25T12:18:06.696568Z     info    starting Http service at 127.0.0.1:15004
2023-04-25T12:18:06.698950Z     info    Pilot SAN: [istiod-remote.istio-system.svc]
2023-04-25T12:18:06.705118Z     info    Starting proxy agent
2023-04-25T12:18:06.705177Z     info    starting
2023-04-25T12:18:06.705214Z     info    Envoy command: [-c etc/istio/proxy/envoy-rev.json --restart-epoch 0 --drain-time-s 45 --parent-shutdown-time-s 60 --local-address-ip-version v4 --file-flush-interval-msec 1000 --log-format %Y-%m-%dT%T.%fZ      %l      envoy %n        %v -l warning --component-log-level misc:error]
2023-04-25T12:18:07.696708Z     info    cache   generated new workload certificate      latency=1.001557215s ttl=23h59m59.303308657s
2023-04-25T12:18:07.696756Z     info    cache   Root cert has changed, start rotating root cert
2023-04-25T12:18:07.696785Z     info    ads     XDS: Incremental Pushing:0 ConnectedEndpoints:0 Version:
2023-04-25T12:18:07.696896Z     info    cache   returned workload trust anchor from cache       ttl=23h59m59.303107754s
2023-04-25T12:19:07.664759Z     warning envoy config    StreamAggregatedResources gRPC config stream to xds-grpc closed since 40s ago: 14, connection error: desc = "transport: Error while dialing dial tcp 10.233.48.75:15012: i/o timeout"
2023-04-25T12:19:29.530922Z     warning envoy config    StreamAggregatedResources gRPC config stream to xds-grpc closed since 62s ago: 14, connection error: desc = "transport: Error while dialing dial tcp 10.233.48.75:15012: i/o timeout"
2023-04-25T12:19:51.228936Z     warning envoy config    StreamAggregatedResources gRPC config stream to xds-grpc closed since 84s ago: 14, connection error: desc = "transport: Error while dialing dial tcp 10.233.48.75:15012: i/o timeout"
2023-04-25T12:20:11.732449Z     warning envoy config    StreamAggregatedResources gRPC config stream to xds-grpc closed since 104s ago: 14, connection error: desc = "transport: Error while dialing dial tcp 10.233.48.75:15012: i/o timeout"
2023-04-25T12:20:41.426914Z     warning envoy config    StreamAggregatedResources gRPC config stream to xds-grpc closed since 134s ago: 14, connection error: desc = "transport: Error while dialing dial tcp 10.233.48.75:15012: i/o timeout"
2023-04-25T12:21:15.199447Z     warning envoy config    StreamAggregatedResources gRPC config stream to xds-grpc closed since 168s ago: 14, connection error: desc = "transport: Error while dialing dial tcp 10.233.48.75:15012: i/o timeout"
```

上面报错信息显示连接 `10.233.48.75:15012` 即 __istiod-remote__ 的 service ip:15012 timeout !!!。

此时我们查看 __istio-system__ 命名空间下 __istiod-remote__ 的 __endpoint__ 。

```bash
kubectl get ep -n istio-system
```
```none
NAME                    ENDPOINTS                                                                 AGE
istio-eastwestgateway                                                                             36s
istio-ingressgateway                                                                              10m
istiod                  10.233.97.220:15012,10.233.97.220:15010,10.233.97.220:15017 + 1 more...   10m
istiod-remote           10.233.95.141:15012,10.233.95.141:15017                                   10m
```

这里可以看出 __istio-remote__ 分配的 __endpoint__ 地址是 `istiod-remote 10.233.95.141:15012,10.233.95.141:15017` 。如下图：

![timeout](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/troubleshoot/images/hosted02.png)

!!! note

    工作负载集群接入托管网格时，istiod-remote 的 endpoint 地址分配的应该是
    istiod-xxxx-hosted-lb service 的 loadBalancer IP:15012，
    而这里却分配成控制面集群的 istiod-xxxx-hosted-xxxx Pod IP。

## 解决方案

更新网格 __基本信息__ 配置中的控制面地址：

1. 登录控制面集群执行以下命令获取这个地址：

    ```bash
    kubectl get svc -n istio-system istiod-ywistio-hosted-lb -o "jsonpath={.status.loadBalancer.ingress[0].ip}"
    ```

    ![获取地址](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/troubleshoot/images/hosted03.png)

1. 点击右侧菜单，选择 __编辑基本信息__ 。

    ![基本信息](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/troubleshoot/images/hosted04.png)

1. 填写控制面地址。

    ![填写地址](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/troubleshoot/images/hosted05.png)

1. 再次查看工作负载集群的 __istio-ingressgateway__ ，发现此时已经正常。

    ![查看集群状态](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/troubleshoot/images/hosted06.png)

1. 查看 __istiod-remote endpoint__ 信息也正常。

    ![查看信息](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/troubleshoot/images/hosted07.png)
