# 开始安装

## 前提条件

- 请在开始安装前做好[部署规划以及环境准备](deploy-plan.md)
- 火种节点[安装依赖](../install-tools.md)
- 确保所有节点的时间同步，否则安装结束后，kube.conf 会报错 `Unable to connect to the server: x509: certificate has expired or is not yet`
- 确保所有节点的 `/etc/resolv.conf` 至少有一个 nameserver，否则 coredns 报错 `plugin/forward: no nameservers found`

## 离线安装

1.  在火种节点为 `dce5-installer` 二进制文件添加可执行权限：

    ```bash
    chmod +x dce5-installer
    ```

2.  设置集群配置文件 [clusterConfig.yaml](clusterconfig.md)，可以在离线包 `offline/sample` 下获取该文件，根据实际的部署模式需要来修改改文件。

3.  开始安装 DCE 5.0。

    ```shell
    ./dce5-installer cluster-create -c ./offline/sample/clusterConfig.yaml -m ./offline/sample/manifest.yaml  -p ./offline/
    ```

    !!! note

        命令需要指定 `-m` 参数，manifest.yaml 文件在离线包 `offline/sample` 下。

4.  安装完成后，命令行会提示安装成功。恭喜您！:smile: 现在可以通过屏幕提示的 URL 使用默认的账户和密码（admin/changeme）探索全新的 DCE 5.0 啦！

    ![success](../images/success.png)

    !!! success

        请记录好提示的 URL，方便下次访问。

5.  成功安装 DCE 5.0 商业版之后，请进行[正版授权](https://qingflow.com/f/e3291647)。
