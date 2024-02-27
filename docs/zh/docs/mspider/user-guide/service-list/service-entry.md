# 服务条目

服务条目可以将外部服务、Web API 或虚拟机添加到服务网格的内部服务注册表中。
以一个外部服务为例，添加服务条目后，Envoy 代理可以将流量发送到该外部服务，服务网格也可以通过虚拟服务和目标规则对该外部服务进行流量治理，就好像该服务条目是网格中的正常服务一样。

服务网格提供了两种创建方式：向导创建和 YAML 创建。

## 图形向导创建

这种创建方式比较简单直观。

1. 进入所选网格后，在左侧导航栏点击 __流量治理__ -> __服务条目__ ，点击右上角的 __创建__ 按钮。

    ![创建](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/images/entry01.png)

1. 在 __创建服务条目__ 页面中，配置各项参数后点击 __确定__ 。具体参数的含义，请参见[参数说明](#_3)。

    ![配置参数](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/images/entry02.png)

1. 返回服务条目列表，屏幕提示创建成功。

    ![创建成功](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/images/entry03.png)

1. 在列表右侧，点击操作一列的 __⋮__ ，可通过弹出菜单进行更多操作。

    ![更多操作](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/images/entry04.png)

## YAML 创建

1. 进入所选网格后，在左侧导航栏点击 __流量治理__ -> __服务条目__ ，点击右上角的 __YAML 创建__ 按钮。

    ![YAML 创建](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/images/entry05.png)

1. 选择命名空间，选择模板，修改各个字段参数，或者直接导入现有的 YAML 文件，参数确认无误后点击 __确定__ 。

    ![YAML 参数配置](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/images/entry06.png)

1. 返回服务条目列表，屏幕提示创建成功。

    ![创建成功](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/images/entry07.png)

以下是一个标准的服务条目 YAML 示例：

```yaml
apiVersion: networking.istio.io/v1beta1
kind: ServiceEntry
metadata:
  name: entry01
  namespace: istio-system
spec:
  addresses:
  - 127.10.18.65
  endpoints:
  - address: 127.10.18.78
    ports:
      test: 9980
  exportTo:
  - istio-system
  hosts:
  - test.service
  location: MESH_INTERNAL
  ports:
  - name: test
    number: 9980
    protocol: HTTP
  workloadSelector: {}
status: {}
```

## 字段参数说明

上述 YAML 文件和创建向导中各项参数的含义简单说明如下。

- Hosts

    服务名。可用于流量治理策略（虚拟服务、目标规则等）中的 hosts 字段匹配。

    - 在 HTTP 流量中，服务名将是 HTTP 主机或 Authority 头
    - 在具有 SNI 名称的 HTTP、TLS 流量中，服务名将是 SNI 名称

- Addresses

    服务地址。与服务关联的虚拟 IP 地址，也可以是 CIDR 前缀。

    - 如果设置了 Addresses 字段，将对请求 HTTP 流量的 服务名和 IP/CIDR 做匹配，确认是否属于该服务。
    - 如果 Addresses 字段为空，则仅根据目标端口识别流量。此时网格中的任何其他服务都不能共享使用该端口，边车将会转发所有该端口的传入流量至指定目标 IP/主机。

- Ports
  
    服务端口。与服务相关联的端口。如果端点是 Unix 域套接字地址，则必须有一个端口。

- Location
    
    服务地址。需要输入一个有效的 IP 地址。用于标明服务是否处于网格内部。

- Resolution

    解析方式。提供了对服务地址的多种解析方式：

    - NONE：直接将流量转发至服务地址或服务端点的地址（如果存在）。
    - STATIC：使用服务端点中的静态地址。
    - DNS：尝试通过异步查询环境 DNS 来解析 IP 地址。
    - 如果未设置服务端点，并且未使用通配符，将解析服务名字段中指定的 DNS 地址。
    - 如果指定了服务端点，将解析服务端点中指定的DNS地址。DNS 解析不能与 Unix 域套接字服务端点一起使用。
    - DNS_ROUND_ROBIN：尝试通过异步查询环境DNS来解析 IP 地址。与 DNS 方式不同的是，DNS_ROUND_ROBIN 方式仅使用连接建立后返回的第一个 IP 地址，而不依赖于 DNS 解析的完整结果。

- Endpoint

    服务端点。与服务相关的端点信息，包含 IP 地址、端口和服务端口名称等。

- WorkloadSelector

    工作负载选择标签。一个键值对，用于选择网格内部服务的工作负载，该项和服务端点为二选一。

<!-- 创建后如何使用这些服务条目？ -->
