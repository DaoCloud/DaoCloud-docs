# Nacos LDAP Integration for User Management

Nacos is called Service Registry in DCE 5.0 Microservice Engine.
This article explains how to manage users by integrating Nacos with LDAP (Lightweight Directory Access Protocol).

## Deploy LDAP on Kubernetes

First deploy ldap.yaml

```shell
kubectl apply -f ldap.yaml
```

```yaml title="ldap.yaml"
apiVersion: apps/v1
kind: Deployment
metadata:
  name: ldap
  labels:
    app: ldap
spec:
  replicas: 1
  selector:
    matchLabels:
      app: ldap
  template:
    metadata:
      labels:
        app: ldap
    spec:
...
