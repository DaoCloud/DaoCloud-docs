# 云原生自定义插件示例: envoy-extproc-method-conv-demo-go

[Envoy-extproc-method-conv-demo-go](https://github.com/projectsesame/envoy-extproc-method-conv-demo-go)是一个基于[envoy-extproc-sdk-go](https://github.com/wrossmorrow/envoy-extproc-sdk-go)实现的,用以展示如何在 Go 语言中使用 Envoy 提供的[ext_proc](https://www.envoyproxy.io/docs/envoy/latest/configuration/http/http_filters/ext_proc_filter)功能的示例.

## 功能

它的主要功能是将由 Downstream 发起的 **GET/POST** 请求转换为 **POST/GET** 请求,然后再发送到 Upstream, 以达到请求方法转换的目的.

## 前置条件

- 安装 Envoy (Version >= v1.29).
- 安装 Go (Verson >= v1.21) 如果只是运行,可跳过此步.
- 支持 HTTP Method:GET/POST 的目标服务(以下简称 Upstream),且假设其支持以下 route:

    - `/*`
      
    - `/no-extproc`

## 编译

进入项目根目录(如果只是运行,可跳过此步).

```bash
go build . -o extproc
```

## 运行

- Envoy:

    ```bash
    envoy -c ./envoy.yaml # 此文件位于项目根目录.
    ```

- Caching:

    - 裸金属:

        ```bash
        ./extproc method-conv --log-stream --log-phases
        ```

    - k8s:

        ```bash
        kubectl apply -f ./deployment.yaml # 此文件位于项目根目录.
        ```

- Curl

    ```bash
    curl 127.0.0.1:8000/no-extproc  # (1)!
    curl 127.0.0.1:8000/foo  # (2)!
    curl -XPOST 127.0.0.1:8000/bar  # (3)!
    ```

    1. Method-conv不会作用于此route,每次请求都会原样路由到Upstream.
    2. 此GET请求将被Method-conv转换成POST后再路由到Upstream
    3. 此POST请求将被Method-conv转换成GET后再路由到Upstream

## 参数说明:

- log-stream: 是否输出关于请求/响应流的日志.
- log-phases: 是否输出各处理阶段的日志.
- update-extproc-header: 是否在响应头中添加此插件的名字.
- update-duration-header: 在结束流时,响应头中添加总处理时间.

**以上参数默认均为 false.**

## 注意事项:

1. 此示例只支持 HTTP Method: GET、POST 之间的转换.

2. mutation_rules 的配置项中的**allow_all_routing**必须被设置为**true**,如**下图**红框中所示:

    ![添加自定义属性](../images/mutation_rules.png)
