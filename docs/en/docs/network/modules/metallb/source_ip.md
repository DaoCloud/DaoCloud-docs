# Get client source IPs via Metallb + istio-ingressgateway

## Background

With Metallb ARP mode, users can view the real IP of the operator in `Global Management`->`Audit Log`, instead of the IP address after SNAT. The key step is to set the `spec.externalTrafficPolicy` of the Service to `Local` mode.

This method is also suitable for Istio high availability mode to get the source IP of the client.

However, this option has an impact on load balancing, please refer to Load Balancing in [L2 and BGP Mode](l2-bgp.md) for details.

After the commercial version is installed, the function of obtaining client source IP is enabled by default. If you want to disable this feature before installation
You can [modify the installer clusterConfigt.yaml](../../../install/commercial/cluster-config.md) to configure it (i.e. set SourceIP to false).

## Steps

### Enable getting client source IPs

1. Configure Metallb to declare the above node as the next hop for LB IPs.

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
      ipAddressPoolSelectors:
      - matchLabels:
          l2.ipaddress-pool.metallb.io: default-pool
      ipAddressPools:
      - default-pool
    ```

    Binding is achieved by configuring `spec.nodeSelectors`.

2. Change the field `spec.externalTrafficPolicy` = `Local` in the Service named `istio-ingressgateway`. This mode preserves the real source IP.

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

3. On the `Global Management`->`Audit Log` page, click `View Details` in any event to view the obtained client source IP.

    ![source-ip-1](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/network/images/source-ip1.png)

    ![source-ip-2](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/network/images/source-ip2.png)

### Disable getting client source IP

Modify the field `spec.externalTrafficPolicy` = `Cluster` in the Service named `istio-ingressgateway`.
