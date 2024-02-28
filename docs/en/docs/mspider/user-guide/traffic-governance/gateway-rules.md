# Gateway

Gateway is used to expose services outside the mesh. Compared with Kubernetes ingress objects, istio-gateway adds more features:

- L4-L6 load balancing
- Outgoing mTLS
- SNI support
- Other internal network features already implemented in Istio: Fault Injection, Traffic Shifting, Circuit Breaking, image

## Concepts

For L7 support, gateway rules are implemented in conjunction with virtual services. Several important main fields are as follows:

- Selector

    Select the istio gateway for north-south traffic, you can use multiple or share one with other rules.

- Servers

    Information about services exposed externally, including hosts, listening port, protocol type, etc.

- TLS

    Provide external mTLS protocol configuration, users can enable three TLS modes, and can customize CA certificate and other operations.

Example:

```yaml
spec:
  selector:
    istio: ingressgateway
  servers:
  - port:
      number: 80
      name: http
      protocol: HTTP
    hosts:
    - istio-grafana.frognew.com
```

## Steps

Service mesh provides two creation methods: wizard and YAML. The specific steps to create through the wizard are as follows:

1. In the left navigation bar, click __Traffic Management__ -> __Gateway__ , and click the __Create__ button in the upper right corner.

    ![Create Gateway](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/mspider/user-guide/images/gateway01.png)

2. In the __Create Gateway__ interface, configure the basic information, add the server as needed, and click __OK__ .

    ![Gateway Information](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/mspider/user-guide/images/gateway02.png)

3. Return to the list of gateway rules, and the screen prompts that the creation is successful.

    ![Successfully Created](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/mspider/user-guide/images/gateway03.png)

4. On the right side of the list, click __⋮__ in the operation column to perform more operations through the pop-up menu.

    ![Edit/Delete](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/mspider/user-guide/images/gateway04.png)
