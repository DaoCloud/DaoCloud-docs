# Registry

The registration center is equivalent to the "address book" in the microservice architecture, and is responsible for recording the mapping relationship between services and service addresses.
When the microservice starts, it registers its own network address and other information to the registration center, and the registration center stores these data.
The service consumer queries the address of the service provider from the registration center, and calls the interface of the service provider through the address.
Each microservice communicates with the registry using a certain mechanism. If the registry cannot communicate with a microservice for a long time, the instance will be logged off. If the microservice network address changes, it will be re-registered to the registration center.

## Traditional service registration and discovery

Service registration means that when a microservice starts, the integrated service discovery SDK sends registration information to the registration center, and the registration center stores the basic information of the service after receiving the service registration request.
Service discovery means that after a service is registered, if a service consumer wants to call the service, the caller can query the address list of the target microservice from the registration center through the service discovery component, and use the obtained service address list to The load policy initiates a call to the target microservice.
Traditional service registration and discovery are mainly supported by traditional registration centers, such as Nacos, Eureka, Zookeeper, etc.

- Eureka Registry

    Eureka is the registry officially recommended by Spring Cloud.
    Eureka is mainly suitable for distributed systems implemented by Java, or systems built with JVM-compatible languages.
    However, since the service governance mechanism of the Eureka server provides a complete RESTful API, it also supports incorporating microservice applications built in non-Java languages ​​into the Eureka service governance system.
    It's just that when using other language platforms, you need to implement Eureka's client program yourself.
    The Eureka cluster adopts a non-Master/Slave architecture. All nodes in the cluster have the same role. After data is written to any node in the cluster, the node replicates to other nodes in the cluster to achieve weak consistency synchronization.

- Nacos Registration Center

    Nacos Registry is an open source project launched by Alibaba, which can easily build cloud native applications and microservice platforms.
    Nacos is dedicated to discovering, configuring and managing microservices. Nacos provides a set of easy-to-use feature sets, mainly including service discovery and service health monitoring, dynamic configuration services, dynamic DNS services, services and their metadata management.
    Nacos supports almost all types of services, for example, Dubbo/gRPC services, Spring Cloud RESTful services or Kubernetes services, etc.

- Zookeeper Registry

    Apache ZooKeeper is an open source distributed application coordination component, software that provides consistent services for distributed applications.
    The functions provided by Zookeeper include configuration maintenance, domain name service, distributed synchronization, group service, etc.
    In the development of microservice projects, ZooKeeper is often used in conjunction with Dubbo to act as a service registry.

## Cloud native service registration and discovery

- Kubernetes Registry

    In Kubernetes, the basis for providing internal service registration and discovery for microservices is the resource of the Service type.
    Kubernetes uses DNS as a service registry.
    To meet this need, each Kubernetes cluster runs a DNS service (kube-dns/coredns) as a Pod in the kube-system namespace, commonly referred to as the cluster DNS.
    The service registration process is:
    
    1. Submit a new Service definition to the API Server by POST.
    2. The request will not be released until it has passed through authentication, authorization and other access policy checks.
    3. The Service gets a ClusterIP (virtual IP address) and saves it to the cluster data registry.
    4. Propagate the Service configuration across the cluster.
    5. The cluster DNS service learns about the creation of the Service and creates the necessary DNS records accordingly.
       After the Service object is registered in the cluster DNS, the Pods in the Service can be accessed through a single stable IP address.

## Service Mesh Registration Center

Service Mesh, as the registry of microservices, is implemented based on Kubernetes.
After installing Istio in a Kubernetes cluster environment, when Kubernetes creates a Pod,
It will call the Sidecar-Injector service of the control plane component through the Kube-API server, automatically modify the description information of the application and inject it into the Sidecar,
Then create a Sidecar proxy container in the Pod that created the business container. SideCar will connect to the components of the Istio control plane through the xDS protocol.