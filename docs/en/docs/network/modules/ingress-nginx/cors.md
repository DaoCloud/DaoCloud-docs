---
MTPE: Jeanine-tw
Revised: Jeanine-tw
Pics: NA
Date: 2023-02-08
---

# Cross-Origin Resource Sharing (CORS)

## What is CORS

CORS means that requests between resources under different domains encounter cross-origin restrictions in the browser.

## Configure CORS

After installing nginx-ingress on Kubernetes, you can handle CORS issues by configuring the Nginx configuration of Ingress CR. This is done as follow:

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: example-ingress
  annotations:
    nginx.ingress.kubernetes.io/enable-cors: "true"
spec:
  rules:
  - host: example.com
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: example-service
            port:
              name: http
```

Redeploy Ingress CR:

```shell
kubectl apply -f example-ingress.yaml
```

This will cause nginx-ingress to add ``Access-Control-Allow-Origin: *`` to the response header of each request, enabling CORS.

## Advanced Configuration

- Configure which methods are accepted

    Control which methods are accepted  with `nginx.ingress.kubernetes.io/cors-allow-methods`. The default is: `GET, PUT, POST, DELETE, PATCH, OPTIONS`.

- Configure how long preflight requests can be cached

    `nginx.ingress.kubernetes.io/cors-max-age` is used to configure Controls how long preflight requests can be cached.

    A preflight request is a query request that the browser sends to the server before sending a CORS request, asking the server if the CORS request is allowed.

    By configuring this option, the number of queries to the server can be reduced, thus improving web page performance.

- Configure if credentials can be passed during CORS operations

    `nginx.ingress.kubernetes.io/cors-allow-credentials` if credentials can be passed during CORS operations.

    Credentials include cookies, HTTP Authentication or Client-side SSL certificates, etc. If the browser is allowed to send Credentials, then `Access-Control-Allow-Credentials: true` must be added to the server response header.

- Configure what's the accepted Origin for CORS

    `nginx.ingress.kubernetes.io/cors-allow-origin` is used to what's the accepted Origin for CORS.

    When a browser sends a request, an origin header is sent to inform the server of the request origin. The server can determine if CORS requests are allowed by checking the origin field in the request header.

    ```yaml
    apiVersion: networking.k8s.io/v1
    kind: Ingress
    metadata:
      name: example-ingress
      annotations:
        nginx.ingress.kubernetes.io/cors-allow-origin: "https://example.com,https://www.example.com"
    ...
    ```

    The above configuration means that only requests from `https://example.com` and `https://www.example.com` will be allowed.
