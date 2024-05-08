# Use Guomi Gateway to proxy DCE 5.0

Follow the steps below to configure the Guomi Gateway for DCE 5.0.

## Software Introduction

**[Tengine](https://github.com/alibaba/tengine):** Tengine is a web server project initiated by
taobao.com. Based on Nginx, it adds many advanced features and features for the needs of high-traffic websites.

**[Tongsuo](https://github.com/Tongsuo-Project/Tongsuo):** Formerly known as BabaSSL,
Tongsuo is an open-source cryptographic library that offers a range of modern cryptographic algorithms
and secure communication protocols. It is designed to support a variety of use cases, including
storage, network security, key management, and privacy computing. By providing foundational
cryptographic capabilities, Tongsuo ensures the privacy, integrity, and authenticity of data
during transmission, storage, and usage. It also enhances security throughout the data lifecycle,
offering robust privacy protection and security features.

## Preparation

A Linux host with Docker installed and internet access.

## Compile and install Tengine & Tongsuo

!!! note

    This configuration is for reference only.

```Dockerfile
FROM docker.m.daocloud.io/debian:11.3

# Version
ENV TENGINE_VERSION="2.3.4" \
    TONGSUO_VERSION="8.3.2"

# Install required system packages and dependencies
RUN apt update && \
    apt -y install \
    wget \
    gcc \
    make \
    libpcre3 \
    libpcre3-dev \
    zlib1g-dev \
    perl \
    && apt clean

# Build tengine
RUN mkdir -p /tmp/pkg/cache/ && cd /tmp/pkg/cache/ \
    && wget https://github.com/alibaba/tengine/archive/refs/tags/${TENGINE_VERSION}.tar.gz -O tengine-${TENGINE_VERSION}.tar.gz \
    && tar zxvf tengine-${TENGINE_VERSION}.tar.gz \
    && wget https://github.com/Tongsuo-Project/Tongsuo/archive/refs/tags/${TONGSUO_VERSION}.tar.gz -O Tongsuo-${TONGSUO_VERSION}.tar.gz \
    && tar zxvf Tongsuo-${TONGSUO_VERSION}.tar.gz \
    && cd tengine-${TENGINE_VERSION} \
    && ./configure \
        --add-module=modules/ngx_openssl_ntls \
        --with-openssl=/tmp/pkg/cache/Tongsuo-${TONGSUO_VERSION} \
        --with-openssl-opt="--strict-warnings enable-ntls" \
        --with-http_ssl_module --with-stream \
        --with-stream_ssl_module --with-stream_sni \
    && make \
    && make install \
    && ln -s /usr/local/nginx/sbin/nginx /usr/sbin/ \
    && rm -rf /tmp/pkg/cache

EXPOSE 80 443
STOPSIGNAL SIGTERM
CMD ["nginx", "-g", "daemon off;"]
```

```shell
docker build -t tengine:0.0.1 .
```

## Generate SM2 and RSA TLS Certificates

Here's how to generate SM2 and RSA TLS certificates and configure the Guomi gateway.

### SM2 TLS Certificate

!!! note

    This certificate is only for testing purposes.

You can refer to the [Tongsuo official documentation](https://www.yuque.com/tsdoc/ts) to use [OpenSSL to generate SM2 certificates](https://www.yuque.com/tsdoc/ts/pb5vqr),
or visit [Guomi SSL Laboratory to apply for SM2 certificates](https://www.gmssl.cn/gmssl/index.jsp?go=CA).

In the end, we will get the following files:

```shell
-rw-r--r-- 1 root root  749 Dec  8 02:59 sm2.*.enc.crt.pem
-rw-r--r-- 1 root root  258 Dec  8 02:59 sm2.*.enc.key.pem
-rw-r--r-- 1 root root  749 Dec  8 02:59 sm2.*.sig.crt.pem
-rw-r--r-- 1 root root  258 Dec  8 02:59 sm2.*.sig.key.pem
```

### RSA TLS Certificate

```shell
-rw-r--r-- 1 root root  216 Dec  8 03:21 rsa.*.crt.pem
-rw-r--r-- 1 root root 4096 Dec  8 02:59 rsa.*.key.pem
```

## Configure SM2 and RSA TLS Certificates for the Guomi Gateway

The Guomi gateway used in this article supports SM2 and RSA TLS certificates. The advantage of dual certificates is that when the browser does not support SM2 TLS certificates, it automatically switches to RSA TLS certificates.

For more detailed configurations, please refer to the [Tongsuo official documentation](https://www.yuque.com/tsdoc/ts).

We enter the Tengine container:

```shell
# Go to the nginx configuration file directory
cd /usr/local/nginx/conf

# Create the cert folder to store TLS certificates
mkdir cert

# Copy the SM2 and RSA TLS certificates to the `/usr/local/nginx/conf/cert` directory
cp sm2.*.enc.crt.pem sm2.*.enc.key.pem  sm2.*.sig.crt.pem  sm2.*.sig.key.pem /usr/local/nginx/conf/cert
cp rsa.*.crt.pem  rsa.*.key.pem /usr/local/nginx/conf/cert

# Edit the nginx.conf configuration
vim nginx.conf
...
server {
  listen 443          ssl;
  proxy_http_version  1.1;
  # Enable Guomi function to support SM2 TLS certificates
  enable_ntls         on;

  # RSA certificate
  # If your browser does not support Guomi certificates, you can enable this option, and Tengine will automatically recognize the user's browser and use RSA certificates for fallback
  ssl_certificate                 /usr/local/nginx/conf/cert/rsa.*.crt.pem;
  ssl_certificate_key             /usr/local/nginx/conf/cert/rsa.*.key.pem;

  # Configure two pairs of SM2 certificates for encryption and signature
  # SM2 signature certificate
  ssl_sign_certificate            /usr/local/nginx/conf/cert/sm2.*.sig.crt.pem;
  ssl_sign_certificate_key        /usr/local/nginx/conf/cert/sm2.*.sig.key.pem;
  # SM2 encryption certificate
  ssl_enc_certificate             /usr/local/nginx/conf/cert/sm2.*.enc.crt.pem;
  ssl_enc_certificate_key         /usr/local/nginx/conf/cert/sm2.*.enc.key.pem;
  ssl_protocols                   TLSv1 TLSv1.1 TLSv1.2 TLSv1.3;

  location / {
    proxy_set_header Host $http_host;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header REMOTE-HOST $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    # You need to modify the address here to the address of the Istio ingress gateway
    # For example, proxy_pass https://istio-ingressgateway.istio-system.svc.cluster.local
    # Or proxy_pass https://demo-dev.daocloud.io
    proxy_pass https://istio-ingressgateway.istio-system.svc.cluster.local;
  }
}
```

## Reload the Configuration of the Guomi Gateway

```shell
nginx -s reload
```

## Next Steps

After successfully deploying the Guomi gateway, [customize the DCE 5.0 reverse proxy server address](reverse-proxy.md).

## Verification

You can deploy a web browser that supports Guomi certificates.
For example, [Samarium Browser](https://github.com/guanzhi/SamariumBrowser),
and then access the DCE5 UI interface through Tengine to verify if the Guomi certificate is effective.
