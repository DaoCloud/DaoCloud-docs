# Accessing a Service through Gateway

This article demonstrates how to integrate a microservice with DCE 5.0 Cloud Native Gateway and access the service through the gateway.

## Prerequisite

- Prepare a service. In this article, we use the `my-otel-demo-adservice` service deployed in the `webstore-demo` namespace of the `skoala-dev` cluster.
- Accessing `/` of the `my-otel-demo-adservice` service should theoretically return `adservice-springcloud: hello world!`.

## Integrate Service with Gateway

DCE 5.0 Cloud Native Gateway supports two methods for importing services: manual integration and automatic discovery. Choose one according to your situation.

### Automatic Discovery of Services

1. Refer to the documentation [Creating a Gateway](../gateway/index.md) to create a gateway. **Add the namespace where the service is located as the jurisdictional namespace of the gateway**.

2. After the namespace where the service is located is added as a "jurisdictional namespace", all services under that namespace will be automatically integrated with the gateway without the need for manual intervention.

3. Refer to [Adding Domain Names](../gateway/domain/index.md) to create a domain name under the gateway, such as `adservice.virtualhost`.
4. Refer to [Adding APIs](../gateway/api/index.md) to create an API under the gateway. **Add the service as the backend service of the API**.

    When adding a backend service, select the target service from the "auto-discovered" services, and click `OK`.

### Manual Integration of Services

1. Refer to [Creating a Gateway](../gateway/index.md) to create a gateway.
2. Refer to the document [Manual Integration](../gateway/service/manual-integrate.md) to integrate the service with the gateway.

3. Refer to [Adding Domain Names](../gateway/domain/index.md) to create a domain name under the gateway, such as `adservice.virtualhost`.
4. Refer to [Adding APIs](../gateway/api/index.md) to create an API under the gateway. **Add the service as the backend service of the API**.

    When adding a backend service, select the target service from the "manually integrated" services, and click `OK`.

## Obtain Gateway Address

1. Log in to the control node of the cluster where the gateway is located, and use the command `kubectl get po -n $Namespace` to view the node where the gateway is located. The Pod starting with `envoy` is the data plane of the gateway. You can find out its location based on this Pod.

2. Use the `ping` command to communicate with the node where the gateway is located, and obtain the IP address of that node based on the returned data.

    In this demo, the IP address of the node where the gateway is located is `10.6.222.24`.

    ![ping](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/skoala/images/br-gw06.png)

3. Use the `kubectl get svc -n $Namespace` command to view the port exposed by the gateway.

    The Service corresponding to the gateway starts with `envoy` and ends with `gtw`. In this demo, the port of the gateway Service is `30040`.

    ![nodeport](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/skoala/images/br-gw07.png)

4. Based on the above information, the access address of the gateway is `10.6.222.24:30040`.

## Configure Local Domain

Use the command `vim /etc/hosts` to modify the local hosts file and configure a local domain name for the gateway access address.

![hosts](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/skoala/images/br-gw08.png)

## Accessing Services

After configuring the local domain name, you can use the domain name to access the gateway service through external and internal networks. You should now be able to access the root path of the service and receive the "hello world" content.

### External Access

In this demo, you can use `curl adservice.virtualhost:30040/`.

![public visit](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/skoala/images/br-gw09.png)

### Internal Access

You can access the `adservice` service through the gateway from any node in the cluster where the gateway is located.

In this demo, there are three worker nodes in the gateway cluster named `dev-worker1`, `dev-worker2`, and `dev-worker3`. On these three nodes, you can use their internal

![internal visit](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/skoala/images/br-gw10.png)
