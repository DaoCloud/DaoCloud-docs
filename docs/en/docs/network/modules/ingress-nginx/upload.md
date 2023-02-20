# Upload Limit

## Global configuration

When the client request Body size exceeds the limit, a Request Entity Too Large error with status code 413 will be returned to the client.
The global setting can be configured via the parameter `client_max_body_size`, which defaults to `1m`.

```yaml
proxy-body-size: 1m
```

## Specific resource limits

This limit can be implemented for a specific Ingress resource by adding the annotation `nginx.ingress.kubernetes.io/proxy-body-size`.

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
   name: example-ingress
   annotations:
     nginx.ingress.kubernetes.io/proxy-body-size: 8m
     nginx.ingress.kubernetes.io/rewrite-target: /
spec:
   ingressClassName: nginx
   rules:
   - host: host-a.example.com
     http:
       paths:
       - path: /
         pathType: Prefix
         backend:
           service:
             name: service-a
             port:
               name: http
```