# 云原生自定义插件示例 envoy-extproc-anti-replay-demo-go

[Envoy-extproc-anti-replay-demo-go](https://github.com/projectsesame/envoy-extproc-anti-replay-demo-go)
是一个基于 [envoy-extproc-sdk-go](https://github.com/wrossmorrow/envoy-extproc-sdk-go)
实现的，用于展示如何在 Go 语言中使用 Envoy 提供的
[ext_proc](https://www.envoyproxy.io/docs/envoy/latest/configuration/http/http_filters/ext_proc_filter) 功能示例。

## 功能

它的主要功能是在将 Downstream 提交的请求路由到 Upstream 之前，先审核其 sign、timestamp、nonce。
如果任何一个验证失败，则将直接应答 401，以达到防重放的目的。

## 前置条件

- 安装 Envoy (Version >= v1.29)
- 安装 Go (Verson >= v1.21)，如果只是运行，可跳过此步
- 支持 HTTP Method:POST 的目标服务（以下简称 Upstream），且假设其支持以下 route：
    
    - `/*`
    - `/no-extproc`

## 编译

进入项目根目录（如果只是运行，可跳过此步）。

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
        ./extproc anti-replay --log-stream --log-phases timespan "900"
        ```

    - k8s：

        ```bash
        kubectl apply -f ./deployment.yaml # 此文件位于项目根目录.
        ```

- Curl

    ```bash
      curl --request POST \
        --url http://127.0.0.1:8080/ \
        --data '{
          "key": "value",
          "key2": "",
          "sign": "659876b30987883efdf178e69f062896",
          "nonce": "6062",
          "timestamp": "1712480920"
        }'
     ```

!!! note "参数说明"

    - log-stream：是否输出关于请求/响应流的日志。
    - log-phases：是否输出各处理阶段的日志。
    - update-extproc-header：是否在响应头中添加此插件的名字。
    - update-duration-header：在结束流时，响应头中添加总处理时间。

    **以上参数默认均为 false。**

    - timespan 900：请求的时间跨度（以 s 计）。

## 注意事项

1. 此命令行参数中的前 4 个为全局配置参数，即所有基于
   [envoy-extproc-sdk-go](https://github.com/wrossmorrow/envoy-extproc-sdk-go)
   实现的插件都会默认支持它们；而 **timespan 900** 为插件 (envoy-extproc-anti-replay-demo-go) 特定参数，由此插件解析与使用。

2. 在此示例中使用 md5 作为"签名"算法，仅是为了演示方便，在正式产品中请使用 SHA256WithRSA 等算法。

3. 以下 3 个字段为每个请求**必填**字段：

    - **sign** ：计算方式为 `MD5(k1=v1&k2=v2...kN=vN)`，生成原始字符串时按 key 的字母升序排列，且忽略掉值为空的 key-value 对。

        ```text
        eg:  sign= MD5("key=value&nonce=6062&timestamp=1712480920") = 659876b30987883efdf178e69f062896
        ```

    - **nonce** ：在时间跨度内同一个 nonce 只可使用一次。
    - **timestamp** ：以 s 计的当前时间。

4. processing_mode 配置项中的 **request_body_mode** 必须配置为 **下图** 红框中的选项：

    ![添加自定义属性](../images/envoy-extproc-anti-replay-demo-go.png)
