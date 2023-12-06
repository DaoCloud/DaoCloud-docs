# 重定向

## 永久重定向

`nginx.ingress.kubernetes.io/permanent-redirect` 将访问请求永久重定向至某个目标网址，默认重定向状态码为 `301`。您可以使用注解 `nginx.ingress.kubernetes.io/permanent-redirect-code` 将重定向状态码更改为 `308`。

尽管规范要求在执行重定向时方法和主体保持不变，但并非所有的用户代理都满足这个要求。只有当响应为 GET 或 HEAD 方法时，才使用 301 状态码，而对于 POST 方法，应使用 308 永久重定向，因为这个状态明确禁止了方法的改变。

简单来说，这是在说明两种 HTTP 状态码的特性和适用情况：

* 301 状态码，HTTP 标准中定义为 "Moved Permanently"，通常用于 GET 和 HEAD 请求，表示请求的资源已经永久地移动到了新的位置。

* 308 状态码，HTTP 标准中定义为 "Permanent Redirect"，主要用于 POST 请求，表示请求的资源已经永久地移动到了新的位置，并且要求客户端在后续的请求中使用新的 URL，并保持原有的 HTTP 方法不变。这个状态码特别适用于需要保持 HTTP 方法不变的情况，例如 POST 方法。

这两个状态码的主要区别在于，308 状态码明确禁止了 HTTP 方法的改变，而 301 状态码在某些情况下可能会导致方法被改变为 GET。

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

## 临时重定向

`nginx.ingress.kubernetes.io/temporal-redirect` 将访问请求临时重定向至某个目标网址，状态码为 `302`。临时重定向暂时不支持自定义状态码，社区正在讨论。

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

## 重定向到 HTTPS

`nginx.ingress.kubernetes.io/ssl-redirect` 注解用于控制 Ingress 对于 HTTP 到 HTTPS 的重定向。当此注解设置为 true 时，所有的 HTTP 流量都将被重定向到 HTTPS。状态码 `308`。

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

## 强制重定向到 HTTPS

`nginx.ingress.kubernetes.io/force-ssl-redirect` 是一个特殊的注解，当此注解设置为 `true` 时，所有的 HTTP 流量都将被强制重定向到 HTTPS。当在集群外部使用 SSL offloading（例如，AWS ELB）时，即使没有可用的 TLS 证书，强制重定向到 HTTPS 可能也很有用。状态码 `308`。

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
