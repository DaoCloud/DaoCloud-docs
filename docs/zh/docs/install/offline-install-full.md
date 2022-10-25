# 离线安装 DCE 5.0 商业版

本页简要说明 DCE 5.0 商业版的离线安装步骤。

## 准备工作

- 准备一个火种机器，[安装依赖项](install-tools.md)

    !!! note

        - 火种机器是安装 DCE 5.0 的前提，DCE 5.0 非社版所有的资源都将通过火种机器执行安装部署。
        - 火种机器最低配置：CPU > 4 核、内存 > 8 GB、磁盘空间 > 100 GB

        - 如果已安装所有依赖项，请确保依赖项版本符合要求：
        
            - podman
            - helm ≥ 3.9.1
            - skopeo ≥ 1.9.2
            - kind 
            - kubectl ≥ 1.22.0
            - yq ≥ 4.27.5
            - minio client

        - 执行 `systemctl stop firewalld` 来关闭机器上的防火墙服务
        - 

- 准备至少一台管理集群（Mgmt）节点，一台全局服务集群（Global）节点（简约模式下可以将二者合并）

    !!! note

        - Global 集群的节点（可运行 DCE5 组件的节点）需要有至少一块没有分区的磁盘，总大小约 200G
        - Global 集群需要 3 台控制平面节点（Master 节点），工作节点最低配置：CPU > 8 核、内存 > 16 GB
        - Mgmt 集群单节点最低配置：CPU > 4 核、内存 > 4 GB（建议生产环境使用高可用的模式）

!!! note

    - 确保所有节点的时间同步，否则安装结束后，kube.conf 使用会报错 `Unable to connect to the server: x509: certificate has expired or is not yet`
    - 确保所有节点的 `/etc/resolv.conf` 至少有一个 nameserver，否则 coredns 报错 `plugin/forward: no nameservers found`

## 离线安装

1. 在火种机器上下载 dce5-installer 二进制文件。

    ```shell
    # 假定 VERSION 为 v0.3.24
    export VERSION=v0.3.24
    curl -Lo ./dce5-installer https://proxy-qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/dce5-installer-${VERSION}
    ```

    为 `dce5-installer` 添加可执行权限：

    ```bash
    chmod +x dce5-installer
    ```

2. 在火种机器上下载 offline 离线镜像包并解压。

    ```shell
    # 假定 VERSION 为 v0.3.24
    export VERSION=v0.3.24
    wget https://proxy-qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-${VERSION}.tar
    tar -zxvf offline-${VERSION}.tar
    ```

3. 设置集群配置文件 clusterConfig.yaml，可以在离线包 `offline/sample` 下获取该文件并根据需求进行修改。

    配置文件范例如下:

    ``` yaml
    apiVersion: provision.daocloud.io/v1alpha1
    kind: ClusterConfig
    metadata:
        creationTimestamp: null
    spec:
        loadBalancer: NodePort  # NodePort(default), metallb, cloudLB (Cloud Controller)
        istioGatewayVip: 10.6.127.254/32 # if loadBalancer is metallb，is requireded. Provides UI and OpenAPI access to DCE
        registryVip: 10.6.127.253/32 # if loadBalancer is metallb，is requireded. Access entry for the mirror repository of the Global cluster
        insightVip: 10.6.127.252/32 # if loadBalancer is metallb，is requireded. It is used for the insight data collection portal of the GLobal cluster, and the insight-agent of the sub-cluster can report data to this VIP
        compactClusterMode: false
        globalClusterName: my-global-cluster
        mgmtClusterName: my-mgmt-cluster
        mgmtMasterNodes:
            - nodeName: "rm-master1" # Node Name will override the hostName, should align with RFC1123 stsandard
            ip: 10.6.127.232
            ansibleUser: "root" # username
            ansiblePass: "123456" # password
        globalMasterNodes:
            - nodeName: "rg-master1"
            ip: 10.6.127.231
            ansibleUser: "root"
            ansiblePass: "123456"
        globalWorkerNodes:
            - nodeName: "rg-worker1"
            ip: 10.6.127.234
            ansibleUser: "root"
            ansiblePass: "123456"
        ntpServer:
            - "172.30.120.197 iburst" # time synchronization server
            - 0.pool.ntp.org
            - ntp1.aliyun.com
            - ntp.ntsc.ac.cn
        persistentRegistryDomainName: temp-registry.daocloud.io # The local image registry which images come from.
        imageConfig: # the kubean image config as below
            imageRepository: temp-registry.daocloud.io
            binaryRepository: http://temp-registry.daocloud.io:9000/kubean
        repoConfig: # the kubean rpm/deb source configuration as below
            # `centos` using CentOS, RedHat, AlmaLinux or Fedora
            # `debian` using Debian
            # `ubuntu` using Ubuntu
            repoType: centos
            dockerRepo: "http://temp-registry.daocloud.io:9000/kubean/centos/$releasever/os/$basearch"
            extraRepos:
            - http://temp-registry.daocloud.io:9000/kubean/centos-iso/\$releasever/os/\$basearch
            - http://temp-registry.daocloud.io:9000/kubean/centos/\$releasever/os/\$basearch
        # k8sVersion only take effect in online mode, dont set it in offline mode
        # k8sVersion: v1.24.6
        auditConfig:
            logPath: /var/log/audit/kube-apiserver-audit.log
            logHostPath: /var/log/kubernetes/audit
            # policyFile: /etc/kubernetes/audit-policy/apiserver-audit-policy.yaml
            # logMaxAge: 30
            # logMaxBackups: 10
            # logMaxSize: 100
            # policyCustomRules: >
            #   - level: None
            #     users: []
            #     verbs: []
            #     resources: []
        network:
            cni: calico
            clusterCIDR: 100.96.0.0/11
            serviceCIDR: 100.64.0.0/13
        cri:
            criProvider: containerd
            # criVersion only take effect in online mode, dont set it in offline mode
            # criVersion: 1.6.8
        addons:
            ingress:
            version: 1.2.3
            dns:
            type: CoreDNS
            version: v1.8.4
    ```

5. 安装 DCE 5.0。

    ``` shell
    ./dce5-installer cluster-create -c ./offline/sample/clusterConfig.yaml -m ./offline/sample/manifest.yaml  -p ./offline/
    ```

    !!! note

        命令需要指定 `-m` 参数，manifest.yaml 文件会在离线包 `offline/sample` 下。

6. 安装完成后，命令行会提示安装成功。恭喜您！:smile: 现在可以通过屏幕提示的 URL 使用默认的账户和密码（admin/changeme）探索全新的 DCE 5.0 啦！

    ![success](images/success.png)

    !!! success

         请记录好提示的 URL，方便下次访问。

7. 另外，安装 DCE 5.0 成功之后，您需要正版授权后使用，请参考[申请社区免费体验](../dce/license0.md)。
