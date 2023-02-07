# 流量代理配置指南

本文介绍 Ingress Nginx 如何配置基于域名、请求路径、请求头和 Cookie 的流量代理。

## 基于域名的流量负载

域名是一个字符串，用于标识互联网上的网站或资源，如 `www.example.com`。它是人类可读的，
而 IP 地址（如 10.6.0.1）是机器可读的。域名通过 DNS 服务器映射到对应的 IP 地址，使人
们可以通过浏览器访问特定网站。

Ingress Nginx 支持转发不同域名的流量。通过将域名系统映射到 Ingress Nginx 的 VIP，
实现域名到 IP 的映射。

通过使用以下配置定义，可以将不同域名的流量转发到相应的后端 Service。例如，将域名 A 的
流量转发到 Service A，域名 B 的流量转发到 Service B。

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: example-ingress
  annotations:
    nginx.ingress.kubernetes.io/rewrite-target: /
spec:
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
  - host: host-b.example.com
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: service-b
            port:
              name: http
```

## 基于请求路径的负载

URL 请求路径（URL Request Path）是在 URL 中指定的从域名或 IP 地址到达特定页面或资源的路径。
它是以 / 开头的字符串。
例如：`https://www.example.com/page-hello-world` 其中 `/page-hello-world` 是 URL 请求路径。

Ingress Nginx 支持使用将不同的 URL 请求路径指向不同的 Service。

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: example-ingress
  annotations:
    nginx.ingress.kubernetes.io/rewrite-target: /
spec:
  rules:
  - http:
      paths:
      - path: /path-a
        pathType: Prefix
        backend:
          service:
            name: service-a
            port:
              name: http
      - path: /path-b
        pathType: Prefix
        backend:
          service:
            name: service-b
            port:
              name: http
```

## 基于 Header 请求头的负载

以下是使用 `nginx.ingress.kubernetes.io/canary-by-header` 注解的示例。
可以在请求中添加版本头以将流量路由到应用程序的稳定版本或金丝雀版本。

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: example-ingress
  annotations:
    nginx.ingress.kubernetes.io/canary: "true"
    nginx.ingress.kubernetes.io/canary-by-header: "version"
    nginx.ingress.kubernetes.io/canary-by-header-value: "v2"
spec:
  rules:
    - host: example.com
      http:
        paths:
          - path: /
            pathType: Prefix
            backend:
              service:
                name: example-service-v2
                port:
                  name: http
```

在这个示例中，对 `example.com` 的流量将根据 Header 请求头 `version` 的值进行分割。
对于 Header 请求头值为 `v2` 的流量，请求将会路由到 `example-service-v2`。

## 基于 Cookie 会话的负载

基于 Cookie 的负载均衡策略，通过使用 Cookie 将客户端与后端服务绑定在一起，这种方法可以确保每个客户端的请求始终由相同的后端服务处理，从而使得服务变得更加稳定。

Cookie 负载均衡的工作原理如下：

1. 当客户端发送第一次请求时，Ingress Nginx 将使用负载均衡算法选择一个后端服务来处理请求。
2. Ingress Nginx 将一个名为 `example-cookie-name` 的 Cookie 发送回客户端。这个 Cookie 包含了后端服务的标识信息。
3. 客户端再次发送请求时，会带上这个 Cookie。Ingress Nginx 根据 Cookie 中的标识信息，将请求转发到对应的后端服务。

以下是配置示例：

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: example-ingress
  annotations:
    nginx.ingress.kubernetes.io/affinity: "cookie"
    nginx.ingress.kubernetes.io/session-cookie-name: "example-cookie-name"
    nginx.ingress.kubernetes.io/session-cookie-expires: "172800"
    nginx.ingress.kubernetes.io/session-cookie-max-age: "172800"
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
