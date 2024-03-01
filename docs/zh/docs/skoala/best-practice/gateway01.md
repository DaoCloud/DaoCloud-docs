# 通过网关访问服务

本文演示如何将微服务接入 DCE 5.0 云原生网关并通过网关访问该服务。

## 前提条件

- 准备一个服务。本文使用的是 `my-otel-demo-adservice` 服务，部署在 `skoala-dev` 集群下的 `webstore-demo` 命名空间。
- 访问 `my-otel-demo-adservice` 服务根路径 `/` 理论上应该返回 `adservice-springcloud: hello world!`。

## 服务接入网关

DCE 5.0 云原生网关支持通过手动接入和自动发现两种方式导入服务，操作时根据自身情况二选一即可。

### 自动发现服务

1. 参考文档[创建网关](../gateway/index.md)创建一个网关。
   **将服务所在的命名空间添加为网关的管辖命名空间** 。
   此次演示使用的服务位于 `webstore-demo` 命名空间。所以创建网关时应该做如下配置:

    ![管辖命名空间](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/br-gw01.png)

2. 服务所在的命名空间被添加为`管辖命名空间`之后，该命名空间下的所有服务都会自动接入网关，无需手动添加。

    ![自动发现](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/br-gw02.png)

3. 参考[添加域名](../gateway/domain/index.md)在网关下面创建域名，例如`adservice.virtualhost`。
4. 参考[添加 API](../gateway/api/index.md)在网关下面创建 API。
   **需要将服务添加为 API 的后端服务** 。

    添加后端服务时，筛选`自动发现`类型的服务，然后勾选目标服务，点击 __确定__ 即可。

    ![后端服务](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/br-gw03.png)

### 手动接入服务

1. 参考[创建网关](../gateway/index.md)创建网关。

2. 参考[手动接入](../gateway/service/manual-integrate.md)文档将服务接入网关

    ![手动接入网关](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/br-gw04.png)

3. 参考[添加域名](../gateway/domain/index.md)在网关下面创建域名，例如`adservice.virtualhost`。
4. 参考[添加 API](../gateway/api/index.md)在网关下面创建 API。

   **需要将服务添加为 API 的后端服务** 。

    添加后端服务时，筛选`手工接入`类型的服务，然后勾选目标服务，点击 __确定__ 即可。

    ![后端服务](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/br-gw05.png)

## 获取网关地址

1. 登录到网关所在集群的控制节点，使用 `kubectl get po -n $Namespace` 命令查看网关所在的节点。
   以 `envoy` 开头的 Pod 是网关的数据面，查看这个 Pod 的位置即可。

2. 使用 `ping` 命令和网关所在节点通信，根据返回的数据得知该节点的 IP。

    在本次演示情形下，网关所在节点的 IP 为`10.6.222.24`。

    ![ping](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/br-gw06.png)

3. 使用 `kubectl get svc -n $Namespace` 命令查看网关暴露的端口。

    以 `envoy` 开头且以 `gtw` 结尾的便是网关对应的 Service。在本次演示情形下，网关 Service 的端口为 `30040`。

    ![nodeport](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/br-gw07.png)

4. 根据上述信息得出，网关的访问地址为 `10.6.222.24:30040`。

## 配置本地域名

使用 `vim /etc/hosts` 命令修改本地 hosts 文件，为网关访问地址配置本地域名。

![hosts](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/br-gw08.png)

## 访问服务

配置本地域名之后，即可使用域名通过外部和内部网络访问网关服务。此时应该可以正常访问，返回服务根路径下的 `hello world` 内容。

### 外部访问

在本次演示情形下，可以使用 `curl adservice.virtualhost:30040/`。

![internal visit](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/br-gw09.png)

### 内部访问

在网关所在集群的任意节点上都可以通过网关成功访问 `adservice` 服务。

在本次演示情形下，网关所在集群中有三个工作节点，分别名为 `dev-worker1`、`dev-worker2`、`dev-worker3`，
在这三个节点上，使用内网 IP 均可以访问成功。

![public visit](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/br-gw10.png)
