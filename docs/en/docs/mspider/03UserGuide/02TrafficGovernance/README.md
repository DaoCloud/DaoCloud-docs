---
hide:
  - toc
---

# traffic management

Traffic governance provides users with three resource configurations, virtual services, target rules, and gateway rules.
By configuring the corresponding rules, multiple traffic management functions such as routing, redirection, circuit breaker, and diversion can be realized. Users can create and edit governance policies through wizards or YAML.

- The virtual service is mainly used to customize the routing rules of the request traffic, and can process the data flow such as diversion, redirection, and timeout return
- The target rule pays more attention to the governance of the traffic itself, and provides more powerful functions such as load balancing, connection survival detection, and circuit breaker for request traffic
- Gateway rules provide the way the Istio gateway services are exposed on the gateway

In practice, three types of strategies need to be used together:

- It is up to the virtual service to define the routing rules and describe where the requests that meet the conditions go
- The target rule is to define subsets and strategies, describing how to deal with the request reaching the target
- If there are external service communication requirements, you need to configure details such as port mapping in the gateway rules to achieve the requirements

In the service mesh, users are provided with wizard and YAML two forms of creation/editing, and users can choose freely according to their personal habits.

- The wizard creation method provides users with a simple and intuitive interactive method, which reduces the learning cost of users to a certain extent
- The YAML creation form is more suitable for experienced users. Users can directly write YAML files to create governance policies, and the creation window also provides users with more commonly used governance policy templates to speed up user writing