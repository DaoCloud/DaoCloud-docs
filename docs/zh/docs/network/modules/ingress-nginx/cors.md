# 跨域

## 什么是跨域？

跨域是指在浏览器中，不同域名下的资源之间的请求会遇到跨域限制。

## 配置跨域示例

在 Kubernetes 安装 nginx-ingress 后，可以通过配置 Ingress CR 的 Nginx 配置来处理跨域问题。具体方法如下：

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: example-ingress
  annotations:
    nginx.ingress.kubernetes.io/add-headers: "Access-Control-Allow-Origin: *"
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

重新部署 Ingress CR：

```shell
kubectl apply -f example-ingress.yaml
```

这样，nginx-ingress 就会在每个请求的响应头中添加 `Access-Control-Allow-Origin: *`，实现跨域。

## 高级配置

### nginx.ingress.kubernetes.io/cors-allow-methods

`nginx.ingress.kubernetes.io/cors-allow-methods` 控制跨域接受哪些方法，默认为：`GET, PUT, POST, DELETE, PATCH, OPTIONS`。

### nginx.ingress.kubernetes.io/cors-max-age

`nginx.ingress.kubernetes.io/cors-max-age` 用于配置浏览器在多长时间内，不再向服务器发送预检请求（Preflight Request）。

预检请求是浏览器在发送跨域请求前，先向服务器发送的一个询问请求，询问服务器是否允许该跨域请求。

通过配置配置该选项，可以减少对服务器的询问次数，从而提高网页性能。

### nginx.ingress.kubernetes.io/cors-allow-credentials

`nginx.ingress.kubernetes.io/cors-allow-credentials` 用于配置是否允许浏览器发送凭证（Credentials）。

Credentials 包括诸如 Cookie、HTTP Authentication 或 Client-side SSL certificates 等数据。如果允许浏览器发送 Credentials，那么必须在服务器响应头中添加 `Access-Control-Allow-Credentials: true`。

### nginx.ingress.kubernetes.io/cors-allow-origin

`nginx.ingress.kubernetes.io/cors-allow-origin` 用于配置服务器允许请求的来源（origin）。

当浏览器发送一个请求时，会发送一个 origin 头，告知服务器请求来源。服务器可以通过检查请求头中的 origin 字段，判断是否允许跨域请求。

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: example-ingress
  annotations:
    nginx.ingress.kubernetes.io/cors-allow-origin: "https://example.com,https://www.example.com"
...
```

以上配置表示，只有来自 `https://example.com` 和 `https://www.example.com` 的请求会被允许。