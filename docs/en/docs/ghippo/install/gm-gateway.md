# Use Guomi Gateway to proxy DCE 5.0

Follow the steps below to configure the National Secret Gateway for DCE 5.0.

## Software Introduction

**[Tengine](https://github.com/alibaba/tengine):** Tengine is a web server project initiated by Taobao.com. Based on Nginx, it adds many advanced functions and features for the needs of high-traffic websites.

**[Tongsuo](https://github.com/Tongsuo-Project/Tongsuo):** Tongsuo/Tongsuo (formerly BabaSSL) is an open source basic cryptographic library that provides modern cryptographic algorithms and secure communication protocols for storage, network, key management, privacy computing and many other business cases provide the basic capabilities of underlying cryptography to realize the privacy, integrity and authenticity of data in the process of transmission, use and storage, and provide privacy protection in the data life cycle. and security protection capabilities.

## Preparation

A Linux host with Docker installed and internet access

## Compile and install Tengine & Tongsuo

> Note: This configuration is for reference only

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

#Build tengine
RUN mkdir -p /tmp/pkg/cache/ && cd /tmp/pkg/cache/ \
     && wget https://github.com/alibaba/tengine/archive/refs/tags/${TENGINE_VERSION}.tar.gz -O tengine-${TENGINE_VERSION}.tar.gz \
     && tar zxvf tengine-${TENGINE_VERSION}.tar.gz\
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
STOP SIGNAL SIGTERM
CMD ["nginx", "-g", "daemon off;"]
```

```shell
docker build -t tengine:0.0.1 .
```

## Generate SSL certificates (SM2 and RSA certificates)

> Note: This certificate is only applicable to the test environment

You can [refer to the official document](https://www.yuque.com/tsdoc/ts/xuxk18ckbtpgvfdi) to use Tongsuo to generate an SSL certificate, or visit <https://www.gmssl.cn/gmssl/index.jsp?go =CA> application.

### SM2 Credentials

```shell
-rw-r--r-- 1 root root 749 Dec 8 02:59 sm2.*.io.enc.crt.pem
-rw-r--r-- 1 root root 258 Dec 8 02:59 sm2.*.io.enc.key.pem
-rw-r--r-- 1 root root 749 Dec 8 02:59 sm2.*.io.sig.crt.pem
-rw-r--r-- 1 root root 258 Dec 8 02:59 sm2.*.io.sig.key.pem
```

### RSA certificate (optional)

```shell
-rw-r--r-- 1 root root 216 Dec 8 03:21 rsa.*.io
-rw-r--r-- 1 root root 4096 Dec 8 02:59 sm2.*.io
```

## Configure SSL certificate for nginx

Both SM2 and RSA certificates are supported. The advantage of dual certificates is: when the browser does not support the national secret certificate, it will automatically switch to the RSA certificate.

For more detailed configuration, please refer to [Official Documentation](https://www.yuque.com/tsdoc/ts/eziua1).

```shell
# Enter the nginx configuration file storage directory
cd /usr/local/nginx/conf

# Create a cert folder for storing SSL certificates
mkdir cert

# Copy the SM2 and RSA (optional) certificates to `/usr/local/nginx/conf/cert` directory
cp sm2.*.enc.crt.pem sm2.*.io.enc.key.pem sm2.*.sig.crt.pem sm2.*.sig.key.pem /usr/local/nginx/conf/cert
cp rsa.*.crt.pem rsa.*.key.pem /usr/local/nginx/conf/cert

# Edit nginx.conf configuration
vim nginx.conf
...
server {
   listen 443 ssl;
   proxy_http_version 1.1;
   # Enable the national secret function
   enable_ntls on;

   # International RSA certificate (optional)
   ssl_certificate /usr/local/nginx/conf/cert/rsa.demo-dev.daocloud.io.crt.pem;
   ssl_certificate_key /usr/local/nginx/conf/cert/rsa.demo-dev.daocloud.io.key.pem;

   # National secret signature certificate
   ssl_sign_certificate /usr/local/nginx/conf/cert/sm2.demo-dev.daocloud.io.sig.crt.pem;
   ssl_sign_certificate_key /usr/local/nginx/conf/cert/sm2.demo-dev.daocloud.io.sig.key.pem;
   # National encryption certificate
   ssl_enc_certificate /usr/local/nginx/conf/cert/sm2.demo-dev.daocloud.io.enc.crt.pem;
   ssl_enc_certificate_key /usr/local/nginx/conf/cert/sm2.demo-dev.daocloud.io.enc.key.pem;
   ssl_protocols TLSv1 TLSv1.1 TLSv1.2 TLSv1.3;

   location / {
     proxy_set_header Host $http_host;
     proxy_set_header X-Real-IP $remote_addr;
     proxy_set_header REMOTE-HOST $remote_addr;
     proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
     proxy_pass https://istio-ingressgateway.istio-system.svc.cluster.local;
   }
}
```

## Reload nginx to make the configuration take effect

```shell
nginx -s reload
```

## Next step

After the successful deployment of the National Secret Gateway, [custom DCE 5.0 reverse proxy server address](reverse-proxy.md).
