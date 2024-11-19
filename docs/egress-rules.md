# Egress Rules in Service Mesh

Egress rules are used to control the outbound traffic from the services within a service mesh. They define how requests are routed from the services inside the mesh to external services.

## Concept and Purpose

Egress rules allow you to specify which external services can be accessed by the services within the mesh, providing a way to enforce security and compliance requirements.

## Use Cases


## Configuration Example

Here is a basic example of how to configure egress rules in a service mesh:

```yaml
apiVersion: networking.istio.io/v1alpha3
kind: ServiceEntry
Egress rules are useful in scenarios where you need to control access to external APIs, databases, or any service outside the mesh.
