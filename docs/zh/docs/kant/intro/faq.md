# 常见问题

本页面列出了一些在云边协同模块中可能遇到的问题，为您提供便利的故障排除解决办法。

1. 容器下载镜像发生 TLS 证书认证相关问题

    如果遇到上述问题，需要过滤私有 https 服务证书认证，不同运行时参考方案如下：

    **containerd:**

    配置 **/etc/containerd/config.toml** 文件，下列内容为参考配置，具体可以按需求定制化设置。

    ```config
    ...
    [plugins."io.containerd.grpc.v1.cri".registry.configs]
        [plugins."io.containerd.grpc.v1.cri".registry.configs."reg.xxx.cn".tls]
            insecure_skip_verify = true
    ```

    **Docker:**

    配置 **/etc/docker/daemon.json** 文件，下列内容为参考配置，具体可以按需求定制化设置。

    ```json
    {
        ...
        "insecure-registries": [
            "0.0.0.0/0"
        ],
        ...
    }
    ```

2. CNI 无法正确使用

    解决方案的操作步骤如下：

    1. 下载 CNI 插件包并解压

        访问 [containernetworking release](https://github.com/containernetworking/plugins/releases)
        页面，下载 **cri-plugins-{os}-{arch}-{version}.tar.gz** 的包，此包会包含 CNI 工具，
        使用命令将压缩包中的二进制文件解压到 **/opt/cni/bin** 目录。

        ```shell
        mkdir -p /opt/cni/bin 
        tar Cxzvf /opt/cni/bin cni-plugins-linux-amd64-v1.1.1.tgz
        ```

    1. 创建默认 CNI 配置文件

        创建默认 CNI 配置文件到 **/etc/cni/net.d/** 目录下，文件名如：10-mynet.conf，具体配置参考如下：

        ```json
        {
          "cniVersion": "1.0.0",
          "name": "mynet",
          "plugins": [
            {
              "type": "bridge",
              "bridge": "cni0",
              "isGateway": true,
              "ipMasq": true,
              "promiscMode": true,
              "ipam": {
                "type": "host-local",
                "ranges": [
                  [{
                    "subnet": "10.88.0.0/16"
                  }],
                  [{
                     "subnet": "2001:db8:4860::/64"
                  }]
                ],
                "routes": [
                  { "dst": "0.0.0.0/0" },
                  { "dst": "::/0" }
                ]
              }
            },
            {
              "type": "portmap",
              "capabilities": {"portMappings": true}
            }
          ]
        }
        ```
