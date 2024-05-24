# Kubernetes 集群证书更新

为保证 Kubernetes 各组件之间的通信安全，组件之间的调用会进行 TLS 身份验证，执行验证操作需要配置集群 PKI 证书。

集群证书有效期为1年，为避免证书过期导致业务无法使用，请及时更新证书。

本文介绍如何手动进行证书更新。

## 检查证书是否过期

您可以执行以下命令查看证书是否过期：

```shell
kubeadm certs check-expiration
```

输出类似于以下内容：

```output
CERTIFICATE                EXPIRES                  RESIDUAL TIME   CERTIFICATE AUTHORITY   EXTERNALLY MANAGED
admin.conf                 Dec 14, 2024 07:26 UTC   204d                                    no      
apiserver                  Dec 14, 2024 07:26 UTC   204d            ca                      no      
apiserver-etcd-client      Dec 14, 2024 07:26 UTC   204d            etcd-ca                 no      
apiserver-kubelet-client   Dec 14, 2024 07:26 UTC   204d            ca                      no      
controller-manager.conf    Dec 14, 2024 07:26 UTC   204d                                    no      
etcd-healthcheck-client    Dec 14, 2024 07:26 UTC   204d            etcd-ca                 no      
etcd-peer                  Dec 14, 2024 07:26 UTC   204d            etcd-ca                 no      
etcd-server                Dec 14, 2024 07:26 UTC   204d            etcd-ca                 no      
front-proxy-client         Dec 14, 2024 07:26 UTC   204d            front-proxy-ca          no      
scheduler.conf             Dec 14, 2024 07:26 UTC   204d                                    no      

CERTIFICATE AUTHORITY   EXPIRES                  RESIDUAL TIME   EXTERNALLY MANAGED
ca                      Dec 12, 2033 07:26 UTC   9y              no      
etcd-ca                 Dec 12, 2033 07:26 UTC   9y              no      
front-proxy-ca          Dec 12, 2033 07:26 UTC   9y              no      
```

## 手动更新证书

您可以通过以下命令手动更新证书，只需带上合适的命令行选项。更新证书前请先备份当前证书。

更新指定证书：

```shell
kubeadm certs renew
```

更新全部证书：

```shell
kubeadm certs renew all
```

更新后的证书可以在 `/etc/kubernetes/pki` 目录下查看，有效期延续 1 年。
以下对应的几个配置文件也会同步更新：

- /etc/kubernetes/admin.conf
- /etc/kubernetes/controller-manager.conf
- /etc/kubernetes/scheduler.conf

!!! note

    - 如果您部署的是一个高可用集群，这个命令需要在所有控制节点上执行。
    - 此命令用 CA（或者 front-proxy-CA ）证书和存储在 `/etc/kubernetes/pki` 中的密钥执行更新。

## 重启服务

执行更新操作之后，你需要重启控制面 Pod。因为动态证书重载目前还不被所有组件和证书支持，所有这项操作是必须的。

静态 Pod 是被本地 kubelet 而不是 API 服务器管理，所以 kubectl 不能用来删除或重启他们。

要重启静态 Pod，你可以临时将清单文件从 `/etc/kubernetes/manifests/` 移除并等待 20 秒。
参考 [KubeletConfiguration 结构](https://kubernetes.io/zh-cn/docs/reference/config-api/kubelet-config.v1beta1/)中的 fileCheckFrequency 值。

如果 Pod 不在清单目录里，kubelet 将会终止它。
在另一个 fileCheckFrequency 周期之后你可以将文件移回去，kubelet 可以完成 Pod 的重建，而组件的证书更新操作也得以完成。

```shell
mv ./manifests/* ./temp/
mv ./temp/* ./manifests/
```

!!! note

    如果容器服务使用的是 Docker，为了让证书生效，可以使用以下命令对涉及到证书使用的几个服务进行重启：
    
    ```shell
    docker ps | grep -E 'k8s_kube-apiserver|k8s_kube-controller-manager|k8s_kube-scheduler|k8s_etcd_etcd' | awk -F ' ' '{print $1}' | xargs docker restart
    ```

## 更新 KubeConfig

构建集群时通常会将 **admin.conf** 证书复制到 **$HOME/.kube/config** 中，为了在更新 admin.conf 后更新 $HOME/.kube/config 的内容， 必须运行以下命令：

```shell
sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
sudo chown $(id -u):$(id -g) $HOME/.kube/config
```

## 为 kubelet 配置证书轮换

完成以上操作后，基本完成了集群所有证书的更新，但不包括 kubelet。

因为 kubernetes 包含特性 kubelet 证书轮换， 在当前证书即将过期时， 将自动生成新的秘钥，并从 Kubernetes API 申请新的证书。 一旦新的证书可用，它将被用于与 Kubernetes API 间的连接认证。

!!! note

    此特性适用于 Kubernetes 1.8.0 或更高的版本。

启用客户端证书轮换，配置参数如下：

- kubelet 进程接收 --rotate-certificates 参数，该参数决定 kubelet 在当前使用的 证书即将到期时，是否会自动申请新的证书。

- kube-controller-manager 进程接收 --cluster-signing-duration 参数
  （在 1.19 版本之前为 --experimental-cluster-signing-duration），用来控制签发证书的有效期限。

更多详情参考[为 kubelet 配置证书轮换](https://kubernetes.io/zh-cn/docs/tasks/tls/certificate-rotation/)。

## 自动更新证书

为了更高效便捷处理已过期或者即将过期的 kubernetes 集群证书，可参考
[k8s 版本集群证书更新](https://github.com/yuyicai/update-kube-cert/blob/master/README-zh_CN.md)。
