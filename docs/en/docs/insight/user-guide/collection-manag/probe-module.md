# Custom Probe Methods

In this page, we will explain how to configure custom probe methods in an existing Blackbox ConfigMap.
We will use the HTTP probe method as an example to demonstrate how to modify the ConfigMap to achieve custom HTTP probing.

## Procedure

1. Go to the cluster list in __Container Management__ and enter the details of the target cluster.
2. Click the left navigation pane and select __ConfigMaps & Secrets__ -> __ConfigMaps__ .
3. Find the ConfigMap named __insight-agent-prometheus-blackbox-exporter__ and click __Edit YAML__ .
   
    Add custom probe methods under __modules__ . Here we use the HTTP probe method as an example:

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

    For more probe methods, refer to [blackbox_exporter Configuration](https://github.com/prometheus/blackbox_exporter/blob/master/CONFIGURATION.md).

## Friendly Reference

The following YAML file contains various probe methods such as HTTP, TCP, SMTP, ICMP, DNS, etc. You can modify the configuration file of `insight-agent-prometheus-blackbox-exporter` according to your needs.

??? note "Click to view the complete YAML file"

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
          http_2xx_example:               # http probe example
            prober: http
            timeout: 5s                   # probe timeout
            http:
              valid_http_versions: ["HTTP/1.1", "HTTP/2.0"]                   # Version in the response, usually default
              valid_status_codes: []  # Defaults to 2xx                       # Valid range of response codes, probe successful if within this range
              method: GET                 # request method
              headers:                    # request headers
                Host: vhost.example.com
                Accept-Language: en-US
                Origin: example.com
              no_follow_redirects: false  # allow redirects
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
              tls_config:                  # tls configuration for https requests
                insecure_skip_verify: false
              preferred_ip_protocol: "ip4" # defaults to "ip6"                 # Preferred IP protocol version
              ip_protocol_fallback: false  # no fallback to "ip6"            
          http_post_2xx:                   # http probe example with body
            prober: http
            timeout: 5s
            http:
              method: POST                 # probe request method
              headers:
                Content-Type: application/json
              body: '{"username":"admin","password":"123456"}'                   # body carried during probe
          http_basic_auth_example:         # probe example with username and password
            prober: http
            timeout: 5s
            http:
              method: POST
              headers:
                Host: "login.example.com"
              basic_auth:                  # username and password to be added during probe
                username: "username"
                password: "mysecret"
          http_custom_ca_example:
            prober: http
            http:
              method: GET
              tls_config:                  # root certificate used during probe
                ca_file: "/certs/my_cert.crt"
          http_gzip:
            prober: http
            http:
              method: GET
              compression: gzip            # compression method used during probe
          http_gzip_with_accept_encoding:
            prober: http
            http:
              method: GET
              compression: gzip
              headers:
                Accept-Encoding: gzip
          tls_connect:                     # TCP probe example
            prober: tcp
            timeout: 5s
            tcp:
              tls: true                    # use TLS
          tcp_connect_example:
            prober: tcp
            timeout: 5s
          imap_starttls:                   # IMAP email server probe configuration example
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
          smtp_starttls:                   # SMTP email server probe configuration example
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
          icmp_example:                    # ICMP probe configuration example
            prober: icmp
            timeout: 5s
            icmp:
              preferred_ip_protocol: "ip4"
              source_ip_address: "127.0.0.1"
          dns_udp_example:                 # DNS query example using UDP
            prober: dns
            timeout: 5s
            dns:
              query_name: "www.prometheus.io"                 # domain name to resolve
              query_type: "A"              # type corresponding to this domain
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
          dns_tcp_example:               # DNS query example using TCP
            prober: dns
            dns:
              transport_protocol: "tcp" # defaults to "udp"
              preferred_ip_protocol: "ip4" # defaults to "ip6"
              query_name: "www.prometheus.io"
    ```
