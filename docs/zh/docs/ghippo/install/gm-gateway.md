# 使用国密网关代理 DCE 5.0

参照以下步骤为 DCE 5.0 配置国密网关。

## 软件介绍

**[Tengine](https://github.com/alibaba/tengine):** Tengine 是由淘宝网发起的 Web 服务器项目。它在 Nginx 的基础上，
针对大访问量网站的需求，添加了很多高级功能和特性。

**[Tongsuo](https://github.com/Tongsuo-Project/Tongsuo):** 铜锁/Tongsuo（原 BabaSSL）是一个提供现代密码学算法和安全通信协议的开源基础密码库，
为存储、网络、密钥管理、隐私计算等诸多业务场景提供底层的密码学基础能力，实现数据在传输、使用、存储等过程中的私密性、完整性和可认证性，
为数据生命周期中的隐私和安全提供保护能力。

## 准备工作

一台安装了 Docker 的 Linux 主机，并且确保它能访问互联网。

## 编译和安装 Tengine & Tongsuo

!!! note

    此配置仅供参考。

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

## 生成 SSL 证书（SM2 和 RSA 证书）

!!! note

    此证书仅适用于测试环境。

您可以参考[语雀官方文档](https://www.yuque.com/tsdoc/ts/xuxk18ckbtpgvfdi)使用 Tongsuo 生成 SSL 证书，
或者访问[国密 SSL 实验室申请 SM2 证书](https://www.gmssl.cn/gmssl/index.jsp?go=CA)。

### SM2 证书

```shell
-rw-r--r-- 1 root root  749 Dec  8 02:59 sm2.*.io.enc.crt.pem
-rw-r--r-- 1 root root  258 Dec  8 02:59 sm2.*.io.enc.key.pem
-rw-r--r-- 1 root root  749 Dec  8 02:59 sm2.*.io.sig.crt.pem
-rw-r--r-- 1 root root  258 Dec  8 02:59 sm2.*.io.sig.key.pem
```

### RSA 证书（可选）

```shell
-rw-r--r-- 1 root root  216 Dec  8 03:21 rsa.*.io
-rw-r--r-- 1 root root 4096 Dec  8 02:59 sm2.*.io
```

## 给 nginx 配置 SSL 证书

支持 SM2 和 RSA 两种证书。双证书的优点是：当浏览器不支持国密证书时，自动切换到 RSA 证书。

更多详细配置，请参考[官方文档](https://www.yuque.com/tsdoc/ts/eziua1)。

```shell
# 进入 nginx 配置文件存放目录
cd /usr/local/nginx/conf

# 创建 cert 文件夹，用于存放 SSL 证书
mkdir cert

# 把 SM2、RSA（可选）证书拷贝到 `/usr/local/nginx/conf/cert` 目录下
cp sm2.*.enc.crt.pem sm2.*.io.enc.key.pem  sm2.*.sig.crt.pem  sm2.*.sig.key.pem /usr/local/nginx/conf/cert
cp rsa.*.crt.pem  rsa.*.key.pem /usr/local/nginx/conf/cert

# 编辑 nginx.conf 配置
vim nginx.conf
...
server {
  listen 443          ssl;
  proxy_http_version  1.1;
  # 开启国密功能
  enable_ntls         on;

  # RSA 证书（可选）
  # 如果您的浏览器不支持国密证书，那么您可以开启此选项，Tengine 会自动识别最终用户的浏览器，并使用 RSA 证书进行回退
  ssl_certificate                 /usr/local/nginx/conf/cert/rsa.demo-dev.daocloud.io.crt.pem;
  ssl_certificate_key             /usr/local/nginx/conf/cert/rsa.demo-dev.daocloud.io.key.pem;

  # 国密签名证书
  ssl_sign_certificate            /usr/local/nginx/conf/cert/sm2.demo-dev.daocloud.io.sig.crt.pem;
  ssl_sign_certificate_key        /usr/local/nginx/conf/cert/sm2.demo-dev.daocloud.io.sig.key.pem;
  # 国密加密证书
  ssl_enc_certificate             /usr/local/nginx/conf/cert/sm2.demo-dev.daocloud.io.enc.crt.pem;
  ssl_enc_certificate_key         /usr/local/nginx/conf/cert/sm2.demo-dev.daocloud.io.enc.key.pem;
  ssl_protocols                   TLSv1 TLSv1.1 TLSv1.2 TLSv1.3;

  location / {
    proxy_set_header Host $http_host;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header REMOTE-HOST $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    # 如果 Tengine 不与 Istio 同一集群，那么您需要将这里的地址修改为 Istio 网关的地址
    proxy_pass https://istio-ingressgateway.istio-system.svc.cluster.local;
  }
}
```

## 重新加载 nginx

重新加载，使其配置生效：

```shell
nginx -s reload
```

## 下一步

国密网关部署成功之后，[自定义 DCE 5.0 反向代理服务器地址](reverse-proxy.md)。

## 验证

您可以部署一个支持国密证书的 Web 浏览器。例如：[Samarium Browser](https://github.com/guanzhi/SamariumBrowser)，然后通过 Tengine 访问 DCE5 UI 界面，验证国密证书是否生效。
