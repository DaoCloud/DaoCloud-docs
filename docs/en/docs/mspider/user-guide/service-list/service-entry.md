# Service Entries

Service entries allow you to add external services, web APIs, or virtual machines to the internal service registry of the service mesh. Once a service entry is added, the Envoy proxy can route traffic to that external service, and the service mesh can perform traffic management on that external service using virtual services and destination rules, just like any other service within the mesh.

The service mesh provides two ways to create service entries: guided creation and YAML creation.

## Guided Creation

This method is straightforward and intuitive.

1. After entering the selected mesh, click __Traffic Management__ -> __Service Entries__ in the left navigation bar, and then click the __Create__ button at the top right corner.

    ![Create](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/mspider/images/entry01.png)

2. On the __Create Service Entry__ page, configure the parameters and click __OK__ . For the meaning of each parameter, please refer to the [Parameter Description](#_3) section.

    ![Configure Parameters](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/mspider/images/entry02.png)

3. Return to the service entry list, and you will see a message indicating successful creation.

4. On the right side of the list, click the __⋮__ icon in the Actions column to perform more operations through the pop-up menu.

## YAML Creation

1. After entering the selected mesh, click __Traffic Management__ -> __Service Entries__ in the left navigation bar, and then click the __YAML Creation__ button at the top right corner.

    ![YAML Creation](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/mspider/images/entry01.png)

2. Select a namespace, choose a template, modify the parameter values, or directly import an existing YAML file. After confirming the parameters are correct, click __OK__ .

    ![YAML Parameter Configuration](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/mspider/images/entry06.png)

3. Return to the service entry list, and you will see a message indicating successful creation.

Here is an example of a standard service entry YAML:

```yaml
apiVersion: networking.istio.io/v1beta1
kind: ServiceEntry
metadata:
  name: entry01
  namespace: istio-system
spec:
  addresses:
  - 127.10.18.65
  endpoints:
  - address: 127.10.18.78
    ports:
      test: 9980
  exportTo:
  - istio-system
  hosts:
  - test.service
  location: MESH_INTERNAL
  ports:
  - name: test
    number: 9980
    protocol: HTTP
  workloadSelector: {}
status: {}
```

## Parameter Description

The meanings of the parameters in the above YAML file and the guided creation are briefly explained below.

- Hosts

    The service name. It can be used to match the __hosts__ field in traffic management policies (virtual services, destination rules, etc.).

    - In HTTP traffic, the service name will be the HTTP host or Authority header.
    - In HTTP or TLS traffic with SNI names, the service name will be the SNI name.

- Addresses

    The service addresses. It is the virtual IP address associated with the service or a CIDR prefix.

    - If the __Addresses__ field is set, it matches the service name and IP/CIDR of incoming HTTP traffic to determine if it belongs to this service.
    - If the __Addresses__ field is empty, the traffic will be identified by the target port only. In this case, no other services in the mesh can share the same port, and the sidecar will forward all incoming traffic on that port to the specified target IP/host.

- Ports
  
    The service ports. They are the ports associated with the service. If the endpoint is a Unix domain socket address, there must be a port.

- Location
    
    The service location. It requires a valid IP address and indicates whether the service is within the mesh.

- Resolution

    The resolution mode. It provides various ways to resolve service addresses:

    - NONE: Directly forwards traffic to the service address or service endpoint address (if it exists).
    - STATIC: Uses the static addresses in the service endpoint.
    - DNS: Attempts to resolve the IP address by asynchronously querying the environment DNS.
    - If no service endpoint is set and no wildcard is used, it resolves the DNS address specified in the service name field.
    - If a service endpoint is specified, it resolves the DNS address specified in the service endpoint. DNS resolution cannot be used with Unix domain socket endpoints.
    - DNS_ROUND_ROBIN: Similar to DNS mode, it also attempts to resolve the IP address by asynchronously querying the environment DNS. The difference is that DNS_ROUND_ROBIN mode only uses the first IP address returned after establishing the connection, rather than relying on the complete result of DNS resolution.

- Endpoint

    The service endpoint. It contains information about the associated endpoints such as IP address, port, and service port name.

- WorkloadSelector

    Workload selector labels. A key-value pair used to select the workload of internal services within the mesh. This option is mutually exclusive with service endpoints.

<!-- How to use these service entries after creation? -->
