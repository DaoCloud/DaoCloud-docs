# 通过 Metallb + istio-ingressgateway 获取客户端源 IP

## 背景

通过 Metallb ARP 模式，用户可以在`全局管理`—>`审计日志`中查看操作者的真实 IP，而不是被 SNAT 后的 IP 地址。主要的关键步骤是设置 Service 的 `spec.externalTrafficPolicy` 为 `Local` 模式。

此方式同样适配 Istio 高可用模式下，获取客户端源 IP 。此方案下， VIP 只会漂移到具有 Endpoint 实例的节点上，所以可以保留客户端源 IP。但会影响负载均衡性(流量的只会打到具有 Endpoint 实例的节点)，可参考 [L2 和 BGP 模式说明](l2-bgp.md)中的负载均衡性寻求更多细节。

商业版安装后，默认开启获取客户端源 IP 功能。若期望安装前关闭该功能，
可[修改安装器 clusterConfig.yaml](../../../install/commercial/cluster-config.md) 来配置（即 SourceIP 设置为 false）。

## 操作步骤

### 开启获取客户端源 IP 功能

1. 确认已经创建 L2Advertisement，如未创建参考以下内容创建。

    ```shell
    [root@demo-dev-master-01 ~]# kubectl get l2advertisements.metallb.io -n metallb-system default-l2advertisement -o yaml
    apiVersion: metallb.io/v1beta1
    kind: L2Advertisement
    metadata:
      annotations:
        helm.sh/hook: post-install
        helm.sh/resource-policy: keep
      creationTimestamp: "2022-11-14T06:04:35Z"
      generation: 2
      labels:
        app.kubernetes.io/instance: metallb
        app.kubernetes.io/managed-by: Helm
        app.kubernetes.io/name: metallb
        app.kubernetes.io/version: 0.13.5
        helm.sh/chart: metallb-0.13.5
      name: default-l2advertisement
      namespace: metallb-system
      resourceVersion: "133681854"
      uid: c5301f5b-fb08-40ae-8a22-2b03e129a092
    spec:
      ipAddressPools:
      - default-pool
    ```

    > ipAddressPools 配置此 L2Advertisement 作用的 IP 池，默认为空表示作用所有 IP 池。

2. 修改名为 `istio-ingressgateway` 的 Service 中的字段 `spec.externalTrafficPolicy` = `Local`，此模式可以保留真实源 IP:

    ```shell
    [root@demo-dev-master-01 ~]# kubectl get svc -n istio-system istio-ingressgateway -o yaml
    apiVersion: v1
    kind: Service
    metadata:
      annotations:
        meta.helm.sh/release-name: istio-ingressgateway
        meta.helm.sh/release-namespace: istio-system
      creationTimestamp: "2022-11-25T08:27:35Z"
      labels:
        app: istio-ingressgateway
        app.kubernetes.io/managed-by: Helm
        app.kubernetes.io/name: istio-ingressgateway
        app.kubernetes.io/version: 1.15.0
        helm.sh/chart: gateway-1.15.0
        istio: ingressgateway
      name: istio-ingressgateway
      namespace: istio-system
      resourceVersion: "198389187"
      uid: 9308a4fa-88b2-48ff-9ccf-a9fa4d6c6bcf
    spec:
      allocateLoadBalancerNodePorts: true
      clusterIP: 10.233.32.214
      clusterIPs:
      - 10.233.32.214
      externalTrafficPolicy: Local
      healthCheckNodePort: 32109
      internalTrafficPolicy: Cluster
      ipFamilies:
      - IPv4
      ipFamilyPolicy: SingleStack
      ports:
      - name: status-port
        nodePort: 32082
        port: 15021
        protocol: TCP
        targetPort: 15021
      - name: http2
        nodePort: 30421
        port: 80
        protocol: TCP
        targetPort: 8080
      - name: https
        nodePort: 30483
        port: 443
        protocol: TCP
        targetPort: 8443
      selector:
        app: istio-ingressgateway
        istio: ingressgateway
      sessionAffinity: None
      type: LoadBalancer
    status:
      loadBalancer:
        ingress:
        - ip: 10.6.229.180
    ```

3. 在`全局管理`—>`审计日志`页面，在任意事件后点击`查看详情`，查看获取到的客户端源 IP：

    ![source-ip-1](https://docs.daocloud.io/daocloud-docs-images/docs/network/images/source-ip-1.png)

    ![source-ip-2](https://docs.daocloud.io/daocloud-docs-images/docs/network/images/source-ip-2.png)

### 关闭获取客户端源 IP 功能

修改名为 `istio-ingressgateway` 的 Service 中的字段 `spec.externalTrafficPolicy` = `Cluster`
