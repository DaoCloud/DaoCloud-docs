# 托管harbor应该选择什么访问类型

在创建托管`harbor`时，需要选择访问类型，目前支持两种类型，分别是`Ingress`和`NodePort`，下面分别介绍这两种类型使用的优缺点；

|      | Ingress                                                      | NodePort                                                     |
| ---- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 优点 | 1.使用Ingress 方便管理和使用，域名易记住，服务易迁移。<br />2. 支持上传Https证书，可以实现拉镜像不用配置非安全仓库。 | 1. 不依赖任何组件，可快速启动服务进行Demo和试用。<br />2.  NodePort 性能较高，没有额外的路由处理 |
| 缺点 | 1. 在私有网络环境需要配合DNS服务做域名解析，需要依赖基础网络设施。<br />2.  Ingress 会对性能产生一定的损失，因为需要进行额外的路由处理。 | 1. 管理不便，IP和某一台宿主机强绑定，并且镜像地址变得不可迁移；<br />2. 只能使用自签证书，在拉取镜像时需要配置非安全仓库。 |

> 推荐Tips:
> - 在**生产**使用中，建议使用`Ingress`方式，因为`Ingress`可以使用`HTTPS`协议，可以使用自签证书或者购买证书，这样可以避免在拉取镜像时需要配置非安全仓库的问题。
> - 在**测试**使用中，建议使用`NodePort`方式，因为`NodePort`方式不依赖任何组件，可快速启动服务进行Demo和试用。


## 1. Ingress
> 要求Tips：
> - 集群必须安装`Ingress`组件，`Ingress`组件可以是`Nginx`、`Traefik`、`HAProxy`等，具体安装方法请参考[Ingress](https://docs.daocloud.io/network/modules/ingress-nginx/what/)。
> - 集群必须安装`DNS`服务，`DNS`服务可以是`CoreDNS`、`KubeDNS`、`Bind`等，具体安装方法请参考[DNS](https://kubernetes.io/docs/concepts/services-networking/dns-pod-service/)。
> - 集群必须安装`LoadBalancer`组件，`LoadBalancer`组件可以是`MetalLB`、`F5`、`Nginx`等，具体安装方法请参考[LoadBalancer](https://docs.daocloud.io/network/modules/metallb/what/)。

`Ingress`可以从集群外部暴露`HTTP`和`HTTPS`路由到集群内部的服务，流量路由由`Ingress`资源上定义的规则控制。在托管`Harbor`中`Ingress`使用流程如下图所示。
![](https://huatu.98youxi.com/markdown/work/uploads/upload_bf0ed72aea6fb746e2ef4e29d7a3f7a9.png)

在**私有云网络**下用户使用`Ingress`部署完托管`Harbor`之后，需要在`DNS`服务中添加域名解析，将域名解析到`LoadBalancer`的`IP`地址上，这样用户就可以通过域名访问`Harbor`了；添加`DNS`域名解析需要在`Kubernetes`集群内
和`Kubernetes`集群外分别进行操作，具体操作步骤如下：

### 1.1 在Kubernetes集群内添加DNS域名解析

在`Kubernetes`集群内，需要在`CoreDNS`组件中添加`DNS`域名解析，具体操作步骤如下：

- 1. 进入`CoreDNS`组件的`Configmap`中，执行如下命令：
```bash
kubectl -n kube-system edit configmap coredns
```

- 2. 进入`CoreDNS`组件的`Configmap`中后，执行如下命令，将`harbor.example.com`解析到`LoadBalancer`的`IP`地址上：
> 注意：`harbor.example.com`为用户自定义的域名，`LoadBalancer`的`IP`地址为`Ingress`的`IP`地址。
```bash
hosts {
    10.1.1.1 harbor.example.com
    fallthrough
}
```
- 3. 保存退出，会重新创建`CoreDNS Pod`：
```bash
kubectl get pod -n kube-system coredns-5c98db65d4-2t2l2
```

### 1.2 在Kubernetes集群外添加DNS域名解析
在集群外也是通过单独部署一个`CoreDNS`组件来实现`DNS`域名解析，然后配置域名步骤和上面的第二步是一样的。


**如果用户的域名是公网域名，那就不需要做上述步骤，公网域名能被解析。**

## 2. NodePort

`NodePort`是一种访问`Kubernetes`集群中`Service`的方法，它会在每个`Node`上打开一个端口，该端口会将流量转发到`Service`的端口上。`NodePort`使用流程如下图所示。

![](https://huatu.98youxi.com/markdown/work/uploads/upload_a983e597f8ac5d9a191f53bd1fa1c3d1.png)

