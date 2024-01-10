# 微服务引擎网关认证服务器接入-ak/sk认证demo应用

demo应用包含两个模块，分别是模拟签名应用和模拟认证应用，模拟签名应用用来生成对应的签名信息，模拟认证应用是基于envoy的认证服务器的一个签名认证的实现。以下主要来讲述模拟签名应用的详细内容。

## 模拟认证应用

代码仓库地址：https://github.com/projectsesame/ak-sk-demo-java

模拟认证应用分为三个接口,分别是：

1. /signstr：根据当前时间生成签名信息
2. /signstrbytime：根据传入的时间生成签名信息
3. /mock：根据当前时间生成签名信息并模拟通过网关访问请求。

三个接口均需要使用post请求，需要传入json格式的body。具体字段如下表所示：

| 字段名称    | 字段含义              | 示例                                               | 备注                                                         |
| ----------- | -------------------- | -------------------------------------------------- | ------------------------------------------------------------ |
| url         | 完整的请求网关路径   | http://10.6.222.21:30080/yang?a=b                  | 格式为：scheme://gatewayIP:gatewayPort/path?param            |
| host        | 域名                 | 10.6.222.21:30080                                  |                                                              |
| method      | 请求方法             | GET/POST                                           | 只支持GET和POST                                              |
| headers     | 请求头               | {"User-Agent":"curl/8.1.2","Accept":"*/*","k":"v"} | 请求网关时携带的请求头                                       |
| signHeaders | 需要进行签名的请求头 | ["User-Agent","Accept"]                            | 需要进行签名的请求头，会对在headers中查找signHeaders中的请求头来进行签名 |
| requestBody | 请求体               | this is request body                               |                                                              |
| apiKey      | 请求认证的标识       | api-key                                            | 请求认证的标识                                               |
| secret      | 请求apiKey对应的密钥 | secret                                             | 不需要填写，demo程序默认为secret，可根据自己需要通过apiKey唯一获取到secret即可 |

demo应用会根据以上结构体进行签名，生成的签名字符串的结构为：

!!! quote

    x-data: 请求方法\n请求路径\n请求参数\n请求时间\n请求头\n请求体

    其中请求头按照字典序排序，多个请求头用逗号分隔，需要签名的请求头可以通过signHeaders字段指定，不指定则只对x-data请求头进行签名，x-data请求头为自定义请求头，为请求时间

    如果存在请求体，请求体为md5加密后再base64编码的值

    签名算法为根据secret对x-data进行hmac-sha1加密，然后base64编码

    签名认证信息字符串为id=apiKey,algorithm=签名算法,headers=签名请求头,signature=签名字符串

例子：

传入参数为：

 ```
    {
        "url":"http://10.6.222.21:30080/yang?a=b",
        "host":"10.6.222.21:30080",
        "apiKey": "key",
        "method":"POST",
        "headers":{"User-Agent":"curl/8.1.2","Accept":"*/*","k":"v"},
        "signHeaders":["User-Agent","Accept"],
        "requestBody":"hahha"

    }
```
第一步生成的签名字符串为：

 ```
     x-data: POST
     /yang
     a=b
    1703573142130
    accept: */*
    user-agent: curl/8.1.2
     x-date: 1703573142130
    ODc5NWEzY2QyY2ExZjdmMTUzMGIzYmI0ZThiYWY2NTA=
```

第二步根据第一步生成的签名字符串和自定义获取的secret进行加密，使用上述字符串根据hmac-sha1加密，然后base64编码结果为：

 ```
    SuRuXnwwgrv+0/TNbWQxkEIdnlA=
```
    
第三步生成签名认证信息，以上例子生成的签名认证信息为：

```
    id=key,algorithm=hmac-sha1,headers=User-Agent;Accept;x-date,signature=SuRuXnwwgrv+0/TNbWQxkEIdnlA=
 ```

如果请求/signstr接口，会返回当前时间对应的签名信息，例如：

```
    {
        "x-data": 1703573142130,
        "authorization": "id=key,algorithm=hmac-sha1,headers=User-Agent;Accept;x-date,signature=SuRuXnwwgrv+0/TNbWQxkEIdnlA="
    }
 ```
 将返回的两个请求头加入的想要访问网关的请求中即可   

 如果请求/signstrbytime接口，需要携带签名时间的毫秒值，会返回参数时间对应的签名信息，例如传入的时间参数为1703573152130，返回为：

```
    {
        "x-data": 1703573152130,
        "authorization": "id=key,algorithm=hmac-sha1,headers=User-Agent;Accept;x-date,signature=8zJJS6DVoGxlwi1K4vrK0QcdwVg="
    }
```

如果请求/mock接口，会以当前时间生成对应的签名字符串后模拟请求网关，网关地址为请求参数重填写的url。

以上是签名模拟应用的签名逻辑和接口简单结束，签名结束后需要和认证服务相结合才可以实现ak/sk的认证逻辑，如果采用以上签名模拟应用的签名，我们提供了相匹配的认证服务，只需要网关接入对应的认证服务即可进行认证。

## 认证服务器

代码仓库地址：https://github.com/projectsesame/envoy-authz-ak-sk-java

只需要根据 [envoy-auzhe-java-aksk.yaml](https://github.com/projectsesame/envoy-authz-ak-sk-java/blob/main/envoy-authz-java-aksk.yaml) 中的编排文件将其部署到网关所在的集群中，并根据[文档](https://docs.daocloud.io/skoala/best-practice/auth-server.html#_6)接入网关即可。