---
hide:
  - toc
---

# Traffic Management

Traffic management provides users with three types of resource configurations:
virtual services, destination rules, and gateway rules. By configuring corresponding rules,
various traffic governance functions such as routing, redirecting, outlier detection, and
traffic splitting can be achieved. Users can create and edit governance policies through
a wizard or in YAML format.

- Virtual services are mainly used to customize routing rules for request traffic and
  can perform actions such as traffic splitting, redirecting, and timeout returns on data streams.
- Destination rules focus more on the governance of the traffic itself and provide powerful
  load balancing, connection pool probing, outlier detection, and other features for request traffic.
- Gateway rules provide the exposure mode of services in the Istio gateway.

In practical applications, three types of policies need to be used together:

- Virtual services define routing rules and specify where requests that meet certain conditions should go.
- Destination rules define subsets and policies to describe how requests to the destination should be handled.
- If there is a need for communication with external services, the details such as port mapping in the gateway rules need to be configured to meet the requirements.

In the service mesh, both wizard-based and YAML-based creation/editing methods are provided.
Users can freely choose according to their preferences.

- The wizard-based creation method provides users with a simple and intuitive interactive
  approach, which reduces the learning curve to some extent.
- YAML creation format is more suitable for experienced users. Users can directly write
  YAML files to create governance policies. The creation window also provides commonly used
  governance policy templates to improve user writing speed.
