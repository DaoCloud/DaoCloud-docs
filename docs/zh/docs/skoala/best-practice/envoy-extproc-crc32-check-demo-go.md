# 云原生自定义插件示例: envoy-extproc-crc32-check-demo-go

[Envoy-extproc-crc32-check-demo-go](https://github.com/projectsesame/envoy-extproc-crc32-check-demo-go)是一个基于[envoy-extproc-sdk-go](https://github.com/wrossmorrow/envoy-extproc-sdk-go)实现的,用以展示如何在 Go 语言中使用 Envoy 提供的[ext_proc](https://www.envoyproxy.io/docs/envoy/latest/configuration/http/http_filters/ext_proc_filter)功能的示例.

它的主要功能是在将 Downstream 提交的请求路由到 Upstream 之前，先对请求体执行 crc 校验，如果校验未通过，将直接应答 403。

## 前置条件

- 安装 Envoy (Version >= v1.29)
- 安装 Go (Verson >= v1.21)，如果只是运行，可跳过这一步
- 支持 HTTP Method:POST 的目标服务（以下简称 Upstream），且假设其支持以下 route：

    - `/*`

    - `/no-extproc`

## 编译

进入项目根目录（如果只是运行，可跳过这一步）。

```bash
go build . -o extproc
```

## 运行

- Envoy：

    ```bash
    envoy -c ./envoy.yaml # 此文件位于项目根目录.
    ```

- Caching：

    - 裸金属：

        ```bash
        ./extproc crc32-check --log-stream --log-phases poly "0x82f63b78"
        ```

    - k8s：

        ```bash
        kubectl apply -f ./deployment.yaml # 此文件位于项目根目录.
        ```

- Curl

    ```bash
    curl --request POST \
     --url http://127.0.0.1:8080/post \
     --data '{
      "data": "1234567890",
      "crc32": "E7C41C6B",
     }'
    ```

## 参数说明

- log-stream：是否输出关于请求/响应流的日志
- log-phases：是否输出各处理阶段的日志
- update-extproc-header：是否在响应头中添加此插件的名字
- update-duration-header：在结束流时,响应头中添加总处理时间

**以上参数默认均为 false.**

- poly 0x82f63b78：生成 checksum 时使用的多项式，默认为 IEEE。

## 注意事项

1.  此命令行参数中的前 4 个为全局配置参数,即所有基于[envoy-extproc-sdk-go](https://github.com/wrossmorrow/envoy-extproc-sdk-go)实现的插件都会默认支持它们；
    而 **poly 0x82f63b78** 为插件(envoy-extproc-crc32-check-demo-go)特定之参数,由此插件解析与使用.

3.  在此示例中使用 md5 作为"签名"算法,仅是为了演示方便,在正式产品中请使用 SHA256WithRSA 等算法.

4.  以下几个字段为每个请求 **必填** 字段：

    - **data** : 用以生成 crc32 的原始数据
    - **crc32**: 校验和，客户端计算时使用的 **多项式** ，必须与插件中的参数相同且其他配置参数**必须**为以下值，如下[图 1](#__tabbed_1_1)所示

        ```output
        + **Bit Width**:                32
        + **REFIN**:                    true
        + **REFOUT**:                   true
        + **XOROUT (HEX)**:             0xFFFFFFFF
        + **Initial Value (HEX)**:      0xFFFFFFFF
        + **Polynomial Formula (HEX)**: 0x82F63B78
        ```

5.  processing_mode 的配置项中的 **request_body_mode** 必须配置为下[图 2](#__tabbed_1_2)红框中的选项：

=== "图 1"

    ![添加自定义属性](../images/CRC1.png)

=== "图 2"

    ![添加自定义属性](../images/CRC2.png)
