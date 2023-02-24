# Mirror Traffic

Traffic mirroring is a powerful tool to verify service functions and performance. It can copy real-time traffic and send it to the mirroring service without creating data and without affecting online access.

| Configuration item | Description | Default value |
| -------------------------------------------------- | -------------------------------------------------- ----------- | ------ |
| `nginx.ingress.kubernetes.io/mirror-target` | Specifies the traffic target address. Support Service and external address, for example set to `https://test.env.com/$request_uri`, `$request_uri` can optionally add the URI of the original request to the end of the target URL. | `""` |
| `nginx.ingress.kubernetes.io/mirror-request-body` | Whether to mirror the Body of the request traffic. | `on` |
| `nginx.ingress.kubernetes.io/mirror-host` | Specifies the Host information for forwarding requests. | `""` |