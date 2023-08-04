# 登录非安全镜像仓库

​当要从非安全的镜像仓库中进行 Pull、Push 时，会遇到
`x509: certificate signed by unknown authority` 错误提示；
这是由于镜像仓库是可能是 `http` 服务，或者 `https` 的证书是自签名的就会出现这个问题。

​我从如下三种运行时来说明如何解决这个问题；我们以要登录 `test.registry.com` 为例。

## Docker

​在 `/etc/docker/daemon.json` 文件中加入如下配置：

```json
{
  "insecure-registries": [
    "test.registry.com",
    "test.registry.com1"
  ]
}
```

​修改之后重启 `docker` 即可：`systemctl restart docker`

## containerd

containerd 配置非安全仓库有两种方法，一种是从 `1.4` 版本之后引入的新方法，一种是之前存在直到 `2.0` 版本的旧方法。

### 新方法

​编辑 `/etc/containerd/config.toml` 文件中的 `config_path` 配置项，默认值是 `/etc/containerd/certs.d`。

```yaml
[plugins."io.containerd.grpc.v1.cri".registry]
  config_path = "/etc/containerd/certs.d"
```

​在 `/etc/containerd/certs.d` 目录下创建一个以`registry` 命名的文件夹，并在其中创建一个 `hosts.tomo`的文件。

```sh
mkdir /etc/containerd/certs.d/test.registry.com
```

如果 `registry` 是带端口号的也需要运行：

```sh
mkdir /etc/containerd/certs.d/127.0.0.1:5000
```

```toml
server = "http://test.registry.com"

[host."http://test.registry.com"]
  capabilities = ["pull", "resolve", "push"]
  skip_verify = true
```

配置后不用重启，可以直接使用。

### 旧方法

​在 `/etc/containerd/config.toml` 文件中加入如下的配置：

```toml
[plugins."io.containerd.grpc.v1.cri".registry.configs."test.registry.com".tls]
  insecure_skip_verify = true

```

​配置之后需要重启 `containerd`，`system restart containerd`。

## CRI-O

​修改 `/etc/crio/crio.conf` 配置文件：

```conf
insecure_registries = ["test.registry.com"]
```

​重启 `crio`: `systemctl restart crio`。
