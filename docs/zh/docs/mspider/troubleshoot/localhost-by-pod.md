# 如何使集群中监听 localhost 的应用被其它 Pod 访问

本文介绍如何在应用监听 localhost 的情况下，通过配置边车资源，使监听 localhost 的应用可以被集群中其它 Pod 通过 Service 访问。

## 问题现象

当部署在集群中的应用监听 localhost 时，即使通过 Service 暴露应用的服务端口，该服务也无法被集群中的其他 Pod 访问。

不同语言的应用监听 localhost 示例如下：

- Golang：net.Listen("tcp", "localhost:8080")
- Node.js：http.createServer().listen(8080, "localhost")
- Python：socket.socket().bind(("localhost", 8083))

## 问题原因

当集群中应用监听 localhost 网络地址时，由于 localhost 是本地地址，集群中的其它 Pod 对其访问不通是正常现象。

## 解决办法

您可以任选以下方式，对外暴露应用服务。

- 方式一：修改应用监听的网络地址

    如果您希望应用提供的服务对外暴露，建议修改应用代码，将应用监听的网络地址从 localhost 改为 0.0.0.0。

- 方式二：使用服务网格暴露监听 localhost 的服务

    如果您不希望修改应用代码，同时需要将监听 localhost 的应用暴露给集群中的其它 Pod，可以在创建边车时进行配置。

    请您按照实际情况对以下字段进行替换。

     | **字段**           | **说明**                              |
     | ------------------ | ------------------------------------- |
     | `{namespace}`      | 替换为应用部署所在的命名空间。        |
     | `{container_port}` | 替换为应用监听 localhost 的容器端口。 |
     | `{port}`           | 替换为应用的 Service 端口。           |
     | `{key} : {value}`  | 替换为选中应用 Pod 的标签。           |

     ```yaml
     apiVersion: networking.istio.io/v1beta1
     kind: Sidecar
     metadata:
       name: localhost-access
       namespace: { namespace }
     spec:
       ingress:
         - defaultEndpoint: "127.0.0.1:{container_port}"
           port:
             name: tcp
             number: { port }
             protocol: TCP
       workloadSelector:
         labels:
           { key }: { value }
     ```
