# 上传限制

## 全局配置

当客户端请求 Body 大小超过限制时，将向客户端返回一个状态码 413 的 Request Entity Too Large 错误。
全局设置可以通过参数 `client_max_body_size` 进行配置，默认为 `1m`。

```yaml
proxy-body-size: 1m
```

## 特定资源限制

要为特定 Ingress 资源实现这一限制，可以通过添加注解 `nginx.ingress.kubernetes.io/proxy-body-size` 的方式实现。

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
