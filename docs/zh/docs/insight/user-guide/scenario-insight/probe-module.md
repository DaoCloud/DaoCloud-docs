# 自定义探测方式

在本文中，我们将介绍如何在已有的 Blackbox ConfigMap 中配置自定义的探测方式。
我们将以 HTTP 探测方式作为示例，展示如何修改 ConfigMap 以实现自定义的 HTTP 探测。

## 操作步骤

1. 进入 __容器管理__ 的集群列表，点击进入目标集群的详情；
2. 点击左侧导航，选择 配置与密钥 > 配置项；
3. 找到名为 __insight-agent-prometheus-blackbox-exporter__ 的配置项，点击操作中的 __编辑 YAML__；

    - 在 __modules__ 下添加自定义探测方式。此处添加 HTTP 探测方式为例：

    ```yaml
    module:
      http_2xx:
        prober: http
        timeout: 5s
        http:
          valid_http_versions: [HTTP/1.1, HTTP/2]
          valid_status_codes: []  # Defaults to 2xx
          method: GET
    ```

!!! info

    更多探测方式可参考 [blackbox_exporter Configuration](https://github.com/prometheus/blackbox_exporter/blob/master/CONFIGURATION.md)。

## 友情参考

以下 YAML 文件中包含了 HTTP、TCP、SMTP、ICMP、DNS 等多种探测方式，可根据需求自行修改 `insight-agent-prometheus-blackbox-exporter` 的配置文件。

??? note "点击查看完整的 YAML 文件"

    ```yaml
    kind: ConfigMap
    apiVersion: v1
    metadata:
      name: insight-agent-prometheus-blackbox-exporter
      namespace: insight-system
      labels:
        app.kubernetes.io/instance: insight-agent
        app.kubernetes.io/managed-by: Helm
        app.kubernetes.io/name: prometheus-blackbox-exporter
        app.kubernetes.io/version: v0.24.0
        helm.sh/chart: prometheus-blackbox-exporter-8.8.0
      annotations:
        meta.helm.sh/release-name: insight-agent
        meta.helm.sh/release-namespace: insight-system
    data:
      blackbox.yaml: |
        modules:
          HTTP_GET:
            prober: http
            timeout: 5s
            http:
              method: GET
              valid_http_versions: ["HTTP/1.1", "HTTP/2.0"]
              follow_redirects: true
              preferred_ip_protocol: "ip4"
          HTTP_POST:
            prober: http
            timeout: 5s
            http:
              method: POST
              body_size_limit: 1MB
          TCP:
            prober: tcp
            timeout: 5s
          ICMP:
            prober: icmp
            timeout: 5s
            icmp:
              preferred_ip_protocol: ip4
          SSH:
            prober: tcp
            timeout: 5s
            tcp:
              query_response:
              - expect: "^SSH-2.0-"
          POP3S:
            prober: tcp
            tcp:
              query_response:
              - expect: "^+OK"
              tls: true
              tls_config:
                insecure_skip_verify: false
          http_2xx_example:               # http 探测示例
            prober: http
            timeout: 5s                   # 探测的超时时间
            http:
              valid_http_versions: ["HTTP/1.1", "HTTP/2.0"]                   # 返回信息中的 Version，一般默认即可
              valid_status_codes: []  # Defaults to 2xx                       # 有效的返回码范围，如果请求的返回码在该范围内，视为探测成功
              method: GET                 # 请求方法
              headers:                    # 请求的头部
                Host: vhost.example.com
                Accept-Language: en-US
                Origin: example.com
              no_follow_redirects: false  # 是否允许重定向
              fail_if_ssl: false   
              fail_if_not_ssl: false
              fail_if_body_matches_regexp:
                - "Could not connect to database"
              fail_if_body_not_matches_regexp:
                - "Download the latest version here"
              fail_if_header_matches: # Verifies that no cookies are set
                - header: Set-Cookie
                  allow_missing: true
                  regexp: '.*'
              fail_if_header_not_matches:
                - header: Access-Control-Allow-Origin
                  regexp: '(\*|example\.com)'
              tls_config:                  # 针对 https 请求的 tls 的配置
                insecure_skip_verify: false
              preferred_ip_protocol: "ip4" # defaults to "ip6"                 # 首选的 IP 协议版本
              ip_protocol_fallback: false  # no fallback to "ip6"            
          http_post_2xx:                   # 带 Body 的 http 探测的示例
            prober: http
            timeout: 5s
            http:
              method: POST                 # 探测的请求方法
              headers:
                Content-Type: application/json
              body: '{"username":"admin","password":"123456"}'                   # 探测时携带的 body
          http_basic_auth_example:         # 带用户名密码的探测的示例
            prober: http
            timeout: 5s
            http:
              method: POST
              headers:
                Host: "login.example.com"
              basic_auth:                  # 探测时要加的用户名密码
                username: "username"
                password: "mysecret"
          http_custom_ca_example:
            prober: http
            http:
              method: GET
              tls_config:                  # 指定探测时使用的根证书
                ca_file: "/certs/my_cert.crt"
          http_gzip:
            prober: http
            http:
              method: GET
              compression: gzip            # 探测时使用的压缩方法
          http_gzip_with_accept_encoding:
            prober: http
            http:
              method: GET
              compression: gzip
              headers:
                Accept-Encoding: gzip
          tls_connect:                     # TCP 探测的示例
            prober: tcp
            timeout: 5s
            tcp:
              tls: true                    # 是否使用 TLS
          tcp_connect_example:
            prober: tcp
            timeout: 5s
          imap_starttls:                   # 探测 IMAP 邮箱服务器的配置示例
            prober: tcp
            timeout: 5s
            tcp:
              query_response:
                - expect: "OK.*STARTTLS"
                - send: ". STARTTLS"
                - expect: "OK"
                - starttls: true
                - send: ". capability"
                - expect: "CAPABILITY IMAP4rev1"
          smtp_starttls:                   # 探测 SMTP 邮箱服务器的配置示例
            prober: tcp
            timeout: 5s
            tcp:
              query_response:
                - expect: "^220 ([^ ]+) ESMTP (.+)$"
                - send: "EHLO prober\r"
                - expect: "^250-STARTTLS"
                - send: "STARTTLS\r"
                - expect: "^220"
                - starttls: true
                - send: "EHLO prober\r"
                - expect: "^250-AUTH"
                - send: "QUIT\r"
          irc_banner_example:
            prober: tcp
            timeout: 5s
            tcp:
              query_response:
                - send: "NICK prober"
                - send: "USER prober prober prober :prober"
                - expect: "PING :([^ ]+)"
                  send: "PONG ${1}"
                - expect: "^:[^ ]+ 001"
          icmp_example:                    # ICMP 探测配置的示例
            prober: icmp
            timeout: 5s
            icmp:
              preferred_ip_protocol: "ip4"
              source_ip_address: "127.0.0.1"
          dns_udp_example:                 # 使用 UDP 进行 DNS 查询的示例
            prober: dns
            timeout: 5s
            dns:
              query_name: "www.prometheus.io"                 # 要解析的域名
              query_type: "A"              # 该域名对应的类型
              valid_rcodes:
              - NOERROR
              validate_answer_rrs:
                fail_if_matches_regexp:
                - ".*127.0.0.1"
                fail_if_all_match_regexp:
                - ".*127.0.0.1"
                fail_if_not_matches_regexp:
                - "www.prometheus.io.\t300\tIN\tA\t127.0.0.1"
                fail_if_none_matches_regexp:
                - "127.0.0.1"
              validate_authority_rrs:
                fail_if_matches_regexp:
                - ".*127.0.0.1"
              validate_additional_rrs:
                fail_if_matches_regexp:
                - ".*127.0.0.1"
          dns_soa:
            prober: dns
            dns:
              query_name: "prometheus.io"
              query_type: "SOA"
          dns_tcp_example:               # 使用 TCP 进行 DNS 查询的示例
            prober: dns
            dns:
              transport_protocol: "tcp" # defaults to "udp"
              preferred_ip_protocol: "ip4" # defaults to "ip6"
              query_name: "www.prometheus.io"
    ```
