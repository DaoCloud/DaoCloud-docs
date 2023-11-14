# Service Registry

A service registry acts as a "directory" in a microservices architecture, responsible for recording the mapping between services and their network addresses. When a microservice starts, it registers its network address and other information with the service registry, which stores this data. Service consumers can then query the service registry to discover the addresses of service providers and invoke their interfaces using those addresses. Various mechanisms are used for communication between microservices and the service registry. If a microservice fails to communicate with the registry for an extended period, it will be deregistered. When the network address of a microservice changes, it will re-register with the service registry.

## Traditional Service Registration and Discovery

Service registration involves microservices sending registration information to the service registry through an integrated service discovery SDK when they start up. The registry stores the basic information of the registered service upon receiving the registration request. Service discovery refers to the process where, after service registration, if a service consumer wants to invoke that service, it can query the registry via a service discovery component to obtain a list of addresses for the target microservice. The consumer can then use a load balancing strategy to make calls to the target microservice based on the obtained address list. Traditional service registration and discovery are mainly supported by traditional service registries such as Nacos, Eureka, and ZooKeeper.

- Eureka Service Registry

    Eureka is the recommended service registry by Spring Cloud. It is primarily suitable for distributed systems implemented in Java or systems built with JVM-compatible languages. However, since the service governance mechanism of the Eureka server provides a comprehensive RESTful API, it is also possible to include microservices built with non-Java languages in the Eureka service governance system. However, when using other language platforms, the client program for Eureka needs to be implemented separately. Eureka clusters adopt a non-Master/Slave architecture, where all nodes in the cluster have the same role. After data is written to any node in the cluster, it is replicated to other nodes in the cluster to achieve eventual consistency synchronization.

- Nacos Service Registry

    Nacos is an open-source project developed by Alibaba that makes it easy to build cloud-native applications and microservices platforms. Nacos focuses on service discovery, configuration management, and service health monitoring for microservices. It provides a set of simple and easy-to-use features, including service discovery, service health check, dynamic configuration, dynamic DNS service, and service and metadata management. Nacos supports almost all types of services, such as Dubbo/gRPC services, Spring Cloud RESTful services, or Kubernetes services.

- ZooKeeper Service Registry

    Apache ZooKeeper is an open-source distributed application coordination component that provides consistency services for distributed applications. ZooKeeper's features include configuration maintenance, domain name services, distributed synchronization, and group services. In microservices development, ZooKeeper is often used in conjunction with Dubbo as a service registry.

## Cloud-Native Service Registration and Discovery

- Kubernetes Service Registry

    In Kubernetes, the foundation for providing internal service registration and discovery for microservices is the Service resource type. Kubernetes uses DNS as the service registry. To meet this requirement, each Kubernetes cluster runs a DNS service (kube-dns/coredns) in the kube-system namespace, typically referred to as cluster DNS. The service registration process is as follows:

    1. Submit a new Service definition to the API Server using the POST method.
    2. The request goes through authentication, authorization, and other admission control processes before being allowed.
    3. The Service is assigned a ClusterIP (a virtual IP address) and stored in the cluster's data store.
    4. The Service configuration is propagated within the cluster.
    5. The cluster DNS service becomes aware of the Service's creation and creates the necessary DNS records accordingly.
       Once the Service object is registered in the cluster DNS, the Pod within the Service can be accessed through a single stable IP address.

## Service Mesh Service Registry

Service Mesh, as a service registry for microservices, is implemented based on Kubernetes. After installing Istio in a Kubernetes cluster environment, when Kubernetes creates Pods, it automatically modifies the application's description and injects a sidecar using the Sidecar-Injector service of the control plane components. A sidecar proxy container is created in parallel with the business container of the Pod. The sidecar connects to the Istio control plane components via the xDS protocol.
