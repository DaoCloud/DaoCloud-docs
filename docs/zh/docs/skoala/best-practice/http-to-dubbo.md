# HTTP 转 Dubbo 协议动态路由

使用 [Pixiu](https://cn.dubbo.apache.org/zh-cn/overview/mannual/dubbo-go-pixiu/overview/)
可以支持协议转换功能，目前已支持 Http、Dubbo2、Triple、gRPC 协议代理和转换，本文主要介绍如何使用它将 HTPP 协议转换为 Dubbo 协议。

## 配置说明

以下内容以及注释仅涉及静态配置文件配置，不涉及配置下发。
Pixiu 静态启动配置文件，内容如下，相应字段含义均已注释：

```yaml
---
static_resources:
  listeners:
    # 名称，没有实际意义
    - name: "net/http"
      # 端口地址监听协议，这里固定为 *HTTP*
      protocol_type: "HTTP"
      # 实际代码未使用到，感觉是 bug，不需要处理，默认均为 20s
      #      config:
      #        read_timeout: 5s
      #        write_timeout: 5s
      #        idle_timeout: 5s
      # 监听地址
      address:
        socket_address:
          address: "0.0.0.0"
          port: 8881
      # 过滤器链
      filter_chains:
        filters:
          # 过滤器名称，这里固定http连接管理器
          - name: dgp.filter.httpconnectionmanager
            config:
              # 路由配置，这里固定填写即可
              route_config:
                routes:
                  - match:
                      prefix: "*"
              http_filters:
                # api配置filter
                - name: dgp.filter.http.apiconfig
                  config:
                    # 表明动态加载
                    dynamic: true
                    # 动态适配器的名称
                    dynamic_adapter: test
                # dubbo 代理 filter
                - name: dgp.filter.http.dubboproxy
                  config:
                    dubboProxyConfig:
                      registries:
                        "nacos":
                          protocol: "nacos"
                          timeout: "3s"
                          address: "127.0.0.1:8848"
                            # username: nacos
                            # password: nacos
                            # group: test-group
                            # namespace: test-namespace
  # 超时时间，无效
  # timeout: 2s
  # 无效
  # generate_request_id: false
  # 服务名称，字段无效
  # server_name: "test_http_to_dubbo"
  # 适配器配置,自动配置动态API
  adapters:
    # id 和上面的 *dynamic_adapter* 的值对应
    - id: test
      name: dgp.adapter.dubboregistrycenter
      config:
        registries:
          # 注册中心map配置
          "nacos":
            # 协议，支持 nacos 和 zookeeper
            protocol: nacos
            # 注册中心的地址
            address: "127.0.0.1:8848"
            # 注册中心端口
            timeout: "5s"
            # 如果注册中心存在认证逻辑这里填写用户名
            #  username: nacos
            # 如果注册中心存在认证逻辑这里填写密码
            # password: nacos
            # 需要监听的注册中心分组
            # group: test-group
            # 注册中心的命名空间
            # namespace: test-namespace
```

完成该配置后，Pixiu 会自动从 adapters 中配置的注册中心获取所有服务的可用方法，并自动装配成 API，之后只需要按照固定格式请求 Pixiu，
Pixiu 即可将流量转发到对应的 dubbo 服务的对应接口的对应方法，下面介绍这种方式下请求 Pixiu 的格式，一定要严格按照格式请求，否则无法匹配到对应的服务。

!!! info

    1. 请求方法必须为 POST
    2. 请求路径格式为：

        ```yaml
        IP: Port/服务名/接口名/版本号/方法名
        ```

        其中 IP 和 Port 均为 Pixiu 对外暴露的 IP 和端口，另外服务名、接口名、版本号和方法名均为对应想要请求的方法的属性.

    3. 请求体必需为 json 格式，存在两个键，分别是 types 和 values，其中 types 为请求方法的参数类型，字符串类型，
       多个参数类型以逗号分隔，values 为对应参数类型的对应值，数组类型，多个参数以逗号分隔。

## Demo 示例

Demo 示例代码地址：<https://github.com/projectsesame/pixiu-demo-dubbo.git>

测试命令如下（假定本地启动的 Pixiu，且访问端口为 8881）：

```bash
# 127.0.0.1 是 Pixiu 部署的 ip，8881 是 Pixiu 启动的端口，dubbo3x-provider 是服务名
# io.daocloud.skoala.dubboapi.DubboDemoService 是接口名称，0.1.1 是版本号，sayHello 是方法名称
# 这里 sayHello 方法存在一个 String 类型的参数，由于是 java 语言开发的 demo，因此类型的完整名称是 java.lang.String
# 这里参数传值为 tt，因此这里传参 {\"types\":\"java.lang.String\",\"values\":[\"tt\"]}，下面例子同理

curl -XPOST http://127.0.0.1:8881/dubbo3x-provider/io.daocloud.skoala.dubboapi.DubboDemoService/0.1.1/sayHello -d "{\"types\":\"java.lang.String\",\"values\":[\"tt\"]}" -H 'Content-Type: application/json'

"[dubbo3x-provider] : Hello, tt

curl -XPOST http://127.0.0.1:8881/dubbo3x-provider/io.daocloud.skoala.dubboapi.DubboDemoService/0.1.1/returnUserInfo -d "{\"types\":\"io.daocloud.skoala.dubboapi.User\",\"values\":[{\"name\":\"yang\",\"age\":10}]}" -H 'Content-Type: application/json'

{"age":10,"name":"yang"}

curl -XPOST http://127.0.0.1:8881/dubbo3x-provider/io.daocloud.skoala.dubboapi.DubboDemoService/0.1.1/returnUserInfoAndNameAndIntAge -d "{\"types\":\"java.lang.String,io.daocloud.skoala.dubboapi.User,int\",\"values\":[\"tt\",{\"name\":\"yang\",\"age\":10},20]}" -H 'Content-Type: application/json'

"method is returnUserInfoAndNameAndIntAge,userInfo is User{name='yang', age=10},name is tt,age is 20"

curl -XPOST http://127.0.0.1:8881/dubbo3x-provider/io.daocloud.skoala.dubboapi.DubboDemoService/0.1.1/returnUserInfoAndNameAndIntegerAge -d "{\"types\":\"java.lang.String,io.daocloud.skoala.dubboapi.User,java.lang.Integer\",\"values\":[\"tt\",{\"name\":\"yang\",\"age\":10},20]}" -H 'Content-Type: application/json'

""method is returnUserInfoAndNameAndIntegerAge,userInfo is User{name='yang', age=10},name is tt, age is 20"
```
