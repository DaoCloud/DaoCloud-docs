---
hide:
  - toc
---

# Microservices

Microservices can refer to an architectural style that combines multiple small services to build a single application, or it can refer to the individual small services that make up the application, that is, some small and autonomous services that work together.
The microservice architecture has the advantages of technical heterogeneity, fault isolation, agile development, independent deployment, elastic scaling, and code reusability. Therefore, more and more enterprises have begun to adopt the microservice architecture to develop applications.
However, as the business continues to expand, the business logic becomes more and more complex, and the number of microservices shows a trend of explosive growth. Intricate inter-service call relationships and dependencies affect the stability and availability of the entire application, greatly increasing the cost of operation and maintenance. Therefore, microservice governance tools came into being.

- Traditional microservices

    Traditional microservice refers to the microservice governance model and technical system developed based on the traditional microservice registration center.
    Traditional microservice frameworks mainly include Spring Cloud, Dubbo, etc. Traditional registry centers mainly include Eureka, Nacos, Zookeeper, Consul, etcd, etc.

- Cloud Native Microservices

    Cloud native microservices refer to the cross-technology stack microservice governance model developed based on Kubernetes, which has gradually developed into a service mesh since there was no framework.
    This model uses cloud native frameworks (such as Kubernetes, Istio, and Linkered), cloud native registries (such as Kubernetes registries and Mesh registries), and cloud native gateways (such as Nginx, Envoy, and Contour).

- Microservice framework

    Microservice frameworks can be divided into two types: intrusive and non-intrusive. Intrusive frameworks are represented by Spring Cloud and Dubbo, and old code needs to be transformed.
    The non-intrusive framework is represented by Istio and Linkerd, adding sidecars and service meshs on the original basis, without changing the old code.

- Spring Cloud framework

    Spring Cloud is a microservice framework based on Spring Boot.
    Spring Cloud integrates mature and proven microservice frameworks on the market, repackages them on the basis of Spring Boot, and shields complex configuration and implementation principles.
    Finally, a set of distributed system development kits that are easy to understand, easy to deploy and easy to maintain are provided for developers.
    Spring Cloud includes more than 20 sub-projects such as Spring Cloud Config and Spring Cloud Bus, and provides solutions in the fields of service governance, service gateway, intelligent routing, load balancing, circuit breaker, monitoring and tracking, distributed message queue, configuration management, etc.

- Dubbo framework

    The Apache Dubbo microservice development framework provides two key capabilities of RPC communication and microservice governance.
    This means that microservices developed using Dubbo will have the ability to remotely discover and communicate with each other.
    At the same time, using Dubbo's rich service governance capabilities, service governance demands such as service discovery, load balancing, and traffic scheduling can be realized.
    Dubbo is highly scalable, and users can customize their own implementation at almost any feature point, thereby changing the default behavior of the framework to meet their own business needs.
    Dubbo currently supports various open source components such as Consul, Nacos, ZooKeeper, and Redis as registry centers.