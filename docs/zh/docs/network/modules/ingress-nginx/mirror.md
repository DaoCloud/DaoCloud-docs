# 镜像流量

流量镜像是验证服务功能和性能的有力工具，可以通过复制实时流量并发送到镜像服务，无需造数据且不会影响线上访问。

| 配置项                                            | 描述                                                         | 默认值 |
| ------------------------------------------------- | ------------------------------------------------------------ | ------ |
| `nginx.ingress.kubernetes.io/mirror-target`       | 指定流量目标地址。支持 Service 和外部地址，例如设置为 `https://test.env.com/$request_uri`，`$request_uri`可以选择将原始请求的 URI 添加到目标 URL 的末尾。 | `""`   |
| `nginx.ingress.kubernetes.io/mirror-request-body` | 是否镜像请求流量的 Body。                                    | `on`   |
| `nginx.ingress.kubernetes.io/mirror-host`         | 指定用于转发请求 Host 信息。                                 | `""`   |
