# HTTP to Dubbo Protocol Dynamic Routing

Using [Pixiu](https://cn.dubbo.apache.org/zh-cn/overview/mannual/dubbo-go-pixiu/overview/), it is possible to support protocol conversion. Currently, it supports proxying and conversion of HTTP, Dubbo2, Triple, and gRPC protocols. This article mainly introduces how to use it to convert HTTP protocol to Dubbo protocol.

## Configuration Instructions

The following content and comments only involve static configuration file configuration and do not involve configuration deployment. The static startup configuration file for Pixiu is as follows, and the meanings of the corresponding fields are all commented:

```yaml
---
static_resources:
  listeners:
    # Name, no actual meaning
    - name: "net/http"
      # Protocol type for port address listening, fixed to *HTTP* here
      protocol_type: "HTTP"
      # Not used in the actual code, seems like a bug, no need to handle, default is 20s
      #      config:
      #        read_timeout: 5s
      #        write_timeout: 5s
      #        idle_timeout: 5s
      # Listening address
      address:
        socket_address:
          address: "0.0.0.0"
          port: 8881
      # Filter chain
      filter_chains:
        filters:
          # Filter name, fixed to http connection manager here
          - name: dgp.filter.httpconnectionmanager
            config:
              # Route configuration, fixed fill in here
              route_config:
                routes:
                  - match:
                      prefix: "*"
              http_filters:
                # API configuration filter
                - name: dgp.filter.http.apiconfig
                  config:
                    # Indicates dynamic loading
                    dynamic: true
                    # Name of dynamic adapter
                    dynamic_adapter: test
                # Dubbo proxy filter
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
  # Timeout, invalid
  # timeout: 2s
  # Invalid
  # generate_request_id: false
  # Service name, field is invalid
  # server_name: "test_http_to_dubbo"
  # Adapter configuration, automatically configure dynamic API
  adapters:
    # Corresponds to the value of *dynamic_adapter* above
    - id: test
      name: dgp.adapter.dubboregistrycenter
      config:
        registries:
          # Registry center map configuration
          "nacos":
            # Protocol, supports nacos and zookeeper
            protocol: nacos
            # Registry center address
            address: "127.0.0.1:8848"
            # Registry center port
            timeout: "5s"
            # If the registry center has authentication logic, fill in the username here
            #  username: nacos
            # If the registry center has authentication logic, fill in the password here
            # password: nacos
            # Group of registry center to be listened to
            # group: test-group
            # Namespace of registry center
            # namespace: test-namespace
```

After completing this configuration, Pixiu will automatically obtain all available methods of all services from the registry center configured in the adapters and automatically assemble them into APIs. After that, you only need to request Pixiu in a fixed format, and Pixiu will forward the traffic to the corresponding method of the corresponding interface of the corresponding Dubbo service. The following introduces the format of requesting Pixiu in this way. It is necessary to strictly request according to the format, otherwise it will not be able to match the corresponding service.

!!! Info

    1. The request method must be POST.
    2. The request path format is:

        ```yaml
        IP: Port/Service Name/Interface Name/Version/Method Name
        ```

        where IP and Port are the IP and port exposed by Pixiu, and the service name, interface name, version, and method name are the attributes of the method you want to request.

    3. The request body must be in JSON format and contains two keys: types and values. types is the parameter type of the request method, a string type, multiple parameter types are separated by commas, and values is the corresponding value of the parameter type, an array type, multiple parameters are separated by commas.

## Demo Example

Demo example code address: <https://github.com/projectsesame/pixiu-demo-dubbo.git>

The test commands are as follows (assuming Pixiu is started locally and the access port is 8881):

```bash
# 127.0.0.1 is the IP of Pixiu deployment, 8881 is the port Pixiu is running on, dubbo3x-provider is the service name
# io.daocloud.skoala.dubboapi.DubboDemoService is the interface name, 0.1.1 is the version number, sayHello is the method name
# Here the sayHello method has a parameter of type String, since this is a demo developed in Java language, the full name of the type is java.lang.String
# The parameter value here is tt, so the parameter passed here is {\"types\":\"java.lang.String\",\"values\":[\"tt\"]}", the same applies to the examples below

curl -XPOST http://127.0.0.1:8881/dubbo3x-provider/io.daocloud.skoala.dubboapi.DubboDemoService/0.1.1/sayHello -d "{\"types\":\"java.lang.String\",\"values\":[\"tt\"]}" -H 'Content-Type: application/json'

"[dubbo3x-provider] : Hello, tt

curl -XPOST http://127.0.0.1:8881/dubbo3x-provider/io.daocloud.skoala.dubboapi.DubboDemoService/0.1.1/returnUserInfo -d "{\"types\":\"io.daocloud.skoala.dubboapi.User\",\"values\":[{\"name\":\"yang\",\"age\":10}]}" -H 'Content-Type: application/json'

{"age":10,"name":"yang"}

curl -XPOST http://127.0.0.1:8881/dubbo3x-provider/io.daocloud.skoala.dubboapi.DubboDemoService/0.1.1/returnUserInfoAndNameAndIntAge -d "{\"types\":\"java.lang.String,io.daocloud.skoala.dubboapi.User,int\",\"values\":[\"tt\",{\"name\":\"yang\",\"age\":10},20]}" -H 'Content-Type: application/json'

"method is returnUserInfoAndNameAndIntAge,userInfo is User{name='yang', age=10},name is tt,age is 20"

curl -XPOST http://127.0.0.1:8881/dubbo3x-provider/io.daocloud.skoala.dubboapi.DubboDemoService/0.1.1/returnUserInfoAndNameAndIntegerAge -d "{\"types\":\"java.lang.String,io.daocloud.skoala.dubboapi.User,java.lang.Integer\",\"values\":[\"tt\",{\"name\":\"yang\",\"age\":10},20]}" -H 'Content-Type: application/json'

""method is returnUserInfoAndNameAndIntegerAge,userInfo is User{name='yang', age=10},name is tt, age is 20"
```
