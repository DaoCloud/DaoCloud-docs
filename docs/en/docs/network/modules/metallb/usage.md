# Instructions for IP pool use

## Cluster default IP pool

If the IP pool is not specified through Annotations: `metallb.universe.tf/address-pool` or the IP is specified through Annotation: `metallb.universe.tf/loadBalancerIPs` when creating `LoadBalancer Service`, then it will be from the existing IP pool Assign addresses in pools with `autoAssign=true`.

!!! note

    The created IP pool must be in the same namespace as `Metallb` component, otherwise `Metallb` cannot recognize it.

## Specify IP pool

When creating `LoadBalancer Service`, you can specify the IP pool through Annotations: `metallb.universe.tf/address-pool`:

```yaml
apiVersion: v1
kind: Service
metadata:
   name: metallb-ippool3
   labels:
     name: metallb-ippool3
   annotations:
     metallb.universe.tf/address-pool: default # default must be in the same namespace as metallb components
spec:
   type: LoadBalancer
   ...
```

Create `LoadBalancer Service`, please refer to: [Create Service](../../../kpanda/user-guide/services-routes/create-services.md).![metallb ip pool](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/network/images/metallb-use-1.png)

### Specify the IP address

When creating `LoadBalancer Service`, you can specify the IP through Annotations: `metallb.universe.tf/loadBalancerIPs`:

```yaml
apiVersion: v1
kind: Service
metadata:
   name: metallb-ippool3
   labels:
     name: metallb-ippool3
   annotations:
    metallb.universe.tf/loadBalancerIPs: 172.16.13.210 # This IP address must exist in an existing IP pool
spec:
   type: LoadBalancer
   ...
```

![specify ip](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/network/images/metallb-use-2.png)

## Shared IP address

Before `k8s v1.20`, `LoadBalancer Service` does not support configuring multiple protocols (`v1.24` supports it, it has become a Beta function), refer to [#issue 23880](https://github.com/kubernetes/kubernetes/issues/23880).

`Metalb` indirectly supports this feature by creating different services and sharing the service IP.

Create two Services:

```yaml
apiVersion: v1
kind: Service
metadata:
   name: dns-service-tcp
   namespace: default
   annotations:
     metallb.universe.tf/allow-shared-ip: "key-to-share-1.2.3.4"
spec:
   type: LoadBalancer
   loadBalancerIP: 1.2.3.4
   ports:
     - name: dnstcp
       protocol: TCP
       port: 53
       targetPort: 53
   selector:
     app: dns
---
apiVersion: v1
kind: Service
metadata:
   name: dns-service-udp
   namespace: default
   annotations:
     metallb.universe.tf/allow-shared-ip: "key-to-share-1.2.3.4"
spec:
   type: LoadBalancer
   loadBalancerIP: 1.2.3.4
   ports:
     - name: dnsudp
       protocol: UDP
       port: 53
       targetPort: 53
   selector:
     app: dns
```

!!! note

     As long as the Annotations (`metallb.universe.tf/allow-shared-ip`) key and value are the same, different `LoadBalancer Service` will have the same IP address (ipv4/ipv6).
     Of course, you can also specify ipv4/ipv6 addresses through Annotations (`metallb.universe.tf/loadBalancerIPs`), or specify through `.spec.loadBalancerIP` (only supports ipv4).
     Editing an Annotation after creation has no effect.

Another feature of shared IP is that the `LoadBalancer IP` address is insufficient, and multiple Services need to share the same IP, but note that the protocols and ports of different Services should be different, otherwise the connection cannot be distinguished.
