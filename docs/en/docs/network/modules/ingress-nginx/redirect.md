# Redirect

## Permanent Redirect

`nginx.ingress.kubernetes.io/permanent-redirect` permanently redirects a request to a target URL, with the default redirect status code being `301`. The `nginx.ingress.kubernetes.io/permanent-redirect-code` annotation can be used to change the redirect status code to `308`.

Although the specification requires the method and body to remain unchanged during redirection, not all user agents meet this requirement. Only when the response is GET or HEAD method, the 301 status code is used, and for the POST method, the 308 permanent redirect should be used because this status explicitly prohibits the change of the method.

In simple terms, this is an explanation of the characteristics and applicable situations of two HTTP status codes:

* Status code 301, defined in the HTTP standard as "Moved Permanently", is typically used for GET and HEAD requests, indicating that the requested resource has permanently moved to a new location.

* Status code 308, defined in the HTTP standard as "Permanent Redirect", is mainly used for POST requests, indicating that the requested resource has permanently moved to a new location and requires the client to use the new URL in subsequent requests and keep the original HTTP method unchanged. This status code is particularly suitable for situations where the HTTP method needs to be maintained, such as the POST method.

The main difference between these two status codes is that the 308 status code explicitly prohibits the change of the HTTP method, while the 301 status code may lead to a change to GET in some cases.

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  annotations:
    nginx.ingress.kubernetes.io/permanent-redirect: http://your-desired-url.com
  name: ingress-301-redirect
  namespace: default
spec:
  rules:
  - host: my-host.com
    http:
      paths:
      - path: /path-to-redirect
        pathType: Prefix
        backend:
          service:
            name: my-service-name
            port:
              number: 80
```

## Temporary Redirect

`nginx.ingress.kubernetes.io/temporal-redirect` temporarily redirects a request to a target URL, with a status code of `302`. Temporary redirects do not currently support custom status codes, and this is under discussion in the community.

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  annotations:
    nginx.ingress.kubernetes.io/temporal-redirect: "http://your-redirect-url.com"
  name: name-of-your-ingress
  namespace: your-namespace
spec:
  rules:
  - host: your-domain.com
    http:
      paths:
      - pathType: Prefix
        path: "/"
        backend:
          service:
            name: your-service-name
            port:
              number: your-service-port
```

## Redirect to HTTPS

The `nginx.ingress.kubernetes.io/ssl-redirect` annotation is used to control the Ingress's redirection from HTTP to HTTPS. When this annotation is set to true, all HTTP traffic is redirected to HTTPS. Status code `308`.

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  annotations:
    nginx.ingress.kubernetes.io/ssl-redirect: "true"
  name: example-ingress
spec:
  rules:
  - host: myapp.example.com
    http:
      paths:
      - pathType: Prefix
        path: "/my-app"
        backend:
          service:
            name: my-service
            port:
              number: 80
```

## Force Redirect to HTTPS

`nginx.ingress.kubernetes.io/force-ssl-redirect` is a special annotation. When this annotation is set to `true`, all HTTP traffic is forcibly redirected to HTTPS. This can be useful when using SSL offloading outside the cluster (for example, AWS ELB), even if there are no available TLS certificates. Status code `308`.

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  annotations:
    nginx.ingress.kubernetes.io/force-ssl-redirect: "true"
  name: example-ingress
spec:
  rules:
  - host: myapp.example.com
    http:
      paths:
      - pathType: Prefix
        path: "/my-app"
        backend:
          service:
            name: my-service
            port:
              number: 80
```
