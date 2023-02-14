---
hide:
  - toc
---

# 离线安装 DCE 5.0 商业版

请在安装之前做好以下准备工作：

- [部署规划以及环境准备](deploy-plan.md)
- 为火种节点[安装依赖](../install-tools.md)
- 确保所有节点的时间同步，否则安装结束后，kube.conf 会报错 `Unable to connect to the server: x509: certificate has expired or is not yet`
- 确保所有节点的 `/etc/resolv.conf` 至少有一个 nameserver，否则 coredns 报错 `plugin/forward: no nameservers found`
- 确保所有节点上不存在的 ipv6  "dadfailed" 地址，可以通过 `ip address | grep dadfailed` 排查，如果存在需要进行删除

具体离线安装步骤如下：

1. 设置集群配置文件 [clusterConfig.yaml](clusterconfig.md)，可以在离线包 `offline/sample` 下获取该文件，根据实际的部署模式需要来修改该文件。

1. 执行以下命令开始安装 DCE 5.0：

    ```shell
    ./offline/dce5-installer cluster-create -c ./offline/sample/clusterConfig.yaml -m ./offline/sample/manifest.yaml  -p ./offline/
    ```

    !!! note

        ./offline/dce5-installer 是解压出来的离线包中自带的安装器二进制文件，
        命令需要指定 `-m` 参数，`manifest.yaml` 文件在离线包 `offline/sample` 下。

1. 安装完成后，命令行会提示安装成功。恭喜您！现在可以通过屏幕提示的 URL 使用默认的账户和密码（admin/changeme）探索全新的 DCE 5.0 啦！

    ![success](../images/success.png)

    !!! success

        请记录好提示的 URL，方便下次访问。

1. 成功安装 DCE 5.0 商业版之后，请进行[正版授权](https://qingflow.com/f/e3291647)。
