---
hide:
  - toc
---

# Microservices

Microservices can refer to an architectural style where a single application is built by combining multiple small services, or it can refer to the individual small services that make up the application, which are collaborative, small, and autonomous.
Microservices architecture offers advantages such as technology heterogeneity, fault isolation, agile development, independent deployment, elastic scalability, and code reusability. As a result, more and more enterprises are adopting microservices architecture for application development.
However, as businesses expand and the complexity of business logic increases, the number of microservices is growing exponentially. The complex relationships and dependencies between services affect the stability and availability of the entire application, significantly increasing operational costs. Therefore, microservice governance tools have emerged.

- Traditional Microservices

    Traditional microservices refer to the mode and technical system of microservice governance that has evolved based on traditional microservice registries.
    Traditional microservice frameworks include Spring Cloud, Dubbo, etc., and traditional service registries include Eureka, Nacos, ZooKeeper, Consul, etcd, etc.

- Cloud-Native Microservices

    Cloud-native microservices refer to a cross-technology-stack microservice governance model that has evolved based on Kubernetes and is gradually moving towards service mesh.
    This approach utilizes cloud-native frameworks such as Kubernetes, Istio, Linkerd, cloud-native registries such as Kubernetes registry and mesh registry, and cloud-native gateways such as Nginx, Envoy, Contour.

- Microservice Frameworks

    Microservice frameworks can be divided into two types: invasive and non-invasive. Invasive frameworks, represented by Spring Cloud and Dubbo, require modification of existing code.
    Non-invasive frameworks, represented by Istio and Linkerd, add sidecars and service meshes to the existing infrastructure without modifying the existing code.

- Spring Cloud Framework

    Spring Cloud is a microservice framework based on Spring Boot.
    Spring Cloud integrates mature and validated microservice frameworks in the market and provides a simplified and encapsulated development toolkit on top of Spring Boot, shielding developers from complex configurations and implementation details.
    Spring Cloud includes more than 20 sub-projects, such as Spring Cloud Config and Spring Cloud Bus, providing solutions in the areas of service governance, service gateway, intelligent routing, load balancing, circuit breakers, monitoring and tracing, distributed messaging queues, and configuration management.

- Dubbo Framework

    Apache Dubbo is a microservice development framework that provides key capabilities in RPC communication and microservice governance.
    This means that microservices developed using Dubbo have the ability to discover and communicate with each other remotely.
    At the same time, leveraging Dubbo's rich service governance capabilities, it is possible to achieve service discovery, load balancing, traffic scheduling, and other service governance requirements.
    Dubbo is highly extensible, allowing users to customize their own implementations at almost any functional point, thereby changing the default behavior of the framework to meet their business needs.
    Dubbo currently supports multiple open-source components such as Consul, Nacos, ZooKeeper, and Redis as service registries.
