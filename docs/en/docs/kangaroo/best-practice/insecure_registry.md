# Login to an insecure container registry

When you need to Pull or Push images from an insecure container registry, you may encounter the
`x509: certificate signed by unknown authority` error. This occurs when the container registry is
either using the `http` protocol or the `https` certificate is self-signed.

I will explain how to resolve this issue using three different runtimes, using `test.registry.com` as an example.

## Docker

Add the following configuration to the `/etc/docker/daemon.json` file:

```json
{
  "insecure-registries": [
    "test.registry.com",
    "test.registry.com1"
  ]
}
```

After making the changes, restart Docker: `systemctl restart docker`

## containerd

There are two methods to configure an insecure registry in containerd: a new method introduced
in version `1.4`, and an old method that existed until version `2.0`.

### New Method

Edit the `/etc/containerd/config.toml` file and locate the `config_path` configuration option,
which has a default value of `/etc/containerd/certs.d`.

```yaml
[plugins."io.containerd.grpc.v1.cri".registry]
  config_path = "/etc/containerd/certs.d"
```

Create a folder inside the `/etc/containerd/certs.d` directory named after your registry,
such as `test.registry.com`, and create a `hosts.toml` file inside it.

```sh
mkdir /etc/containerd/certs.d/test.registry.com
```

If the registry includes a port number, you also need to run:

```sh
mkdir /etc/containerd/certs.d/127.0.0.1:5000
```

```toml
server = "http://test.registry.com"

[host."http://test.registry.com"]
  capabilities = ["pull", "resolve", "push"]
  skip_verify = true
```

After configuring, there is no need to restart. You can use it directly.

### Old Method

Add the following configuration to the `/etc/containerd/config.toml` file:

```toml
[plugins."io.containerd.grpc.v1.cri".registry.configs."test.registry.com".tls]
  insecure_skip_verify = true
```

After making the changes, restart containerd: `systemctl restart containerd`.

## CRI-O

Modify the `/etc/crio/crio.conf` configuration file:

```conf
insecure_registries = ["test.registry.com"]
```

Restart crio: `systemctl restart crio`.
