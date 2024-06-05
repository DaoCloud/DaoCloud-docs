# ETCD 备份

ETCD 备份是以集群数据为核心的备份。在硬件设备损坏，开发测试配置错误等场景中，可以通过 ETCD 备份恢复集群数据。

本文介绍如何为集群制作 ETCD 备份。

## 前提条件

- [接入](../clusters/integrate-cluster.md)或者[创建 Kubernetes 集群](../clusters/create-cluster.md)，且能够访问集群的 UI 界面。

- 创建[命名空间](../namespaces/createns.md)和[用户](../../../ghippo/user-guide/access-control/user.md)，并为用户授予 [NS Admin](../permissions/permission-brief.md#ns-admin) 或更高权限。详情可参考[命名空间授权](../permissions/cluster-ns-auth.md)。

- 准备一个 MinIO 实例。建议通过 DCE 5.0 的 MinIO 中间件进行创建，具体步骤可参考 [MinIO 对象存储](../../../middleware/minio/user-guide/create.md)。

## 创建 ETCD 备份

参照以下步骤创建 ETCD 备份。

1. 进入 __容器管理__ -> __备份恢复__ -> __ETCD 备份__ ，点击 __备份策略__ 页签，然后在右侧点击 __创建备份策略__ 。

    ![备份策略列表](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/etcd01.png)

2. 参考以下说明填写 __基本信息__ 。填写完毕后点击 __下一步__ ，系统将自动校验 ETCD 的联通性，校验通过之后可以进行下一步。

    - 备份集群：选择需要备份哪个集群的 ETCD 数据，并在终端登录
    - ETCD 地址: 格式为 `https://${节点IP}:${端口号}`。
 
        - 在标准 Kubernetes 集群中，ETCD 的默认端口号为 __2379__ 。
        - 在 DCE 4.0 集群中，ETCD 的默认端口号为 __12379__ 。
        - 在公有云托管集群中，需要联系相关开发人员获取 ETCD 的端口号。这是因为公有云集群的控制面组件由云服务提供商维护和管理，用户无法直接访问或查看这些组件，也无法通过常规命令（如 kubectl）无法获取到控制面的端口等信息。

        ??? note "获取端口号的方式"

            1. 在 __kube-system__ 命名空间下查找 ETCD Pod

                ```shell
                kubectl get po -n kube-system | grep etcd
                ```

            2. 获取 ETCD Pod 的 __listen-client-urls__ 中的端口号

                ```shell
                kubectl get po -n kube-system ${etcd_pod_name} -oyaml | grep listen-client-urls # 将 __etcd_pod_name__ 替换为实际的 Pod 名称
                ```
            
                预期输出结果如下，节点 IP 后的数字即为端口号:

                ```shell
                - --listen-client-urls=https://127.0.0.1:2379,https://10.6.229.191:2379
                ```

    - CA 证书：可通过如下命令查看证书，然后将证书内容复制粘贴到对应位置：

        === "标准的 Kubernetes 集群"
        
            ```shell
            cat /etc/kubernetes/ssl/etcd/ca.crt
            ```

        === "DCE 4.0 集群"
        
            ```shell
            cat /etc/daocloud/dce/certs/ca.crt
            ```

    - Cert 证书：可通过如下命令查看证书，然后将证书内容复制粘贴到对应位置：

        === "标准的 Kubernetes 集群"
        
            ```shell
            cat /etc/kubernetes/ssl/apiserver-etcd-client.crt
            ```

        === "DCE 4.0 集群"
        
            ```shell
            cat /etc/daocloud/dce/certs/etcd/server.crt
            ```

    - Key：可通过如下命令查看证书，然后将证书内容复制粘贴到对应位置：

        === "标准的 Kubernetes 集群"
        
            ```shell
            cat /etc/kubernetes/ssl/apiserver-etcd-client.key
            ```

        === "DCE 4.0 集群"
        
            ```shell
            cat /etc/daocloud/dce/certs/etcd/server.key
            ```

        ![创建基本信息](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/kpanda/images/etcd-get01.png)

    !!! note

        点击输入框下方的 __如何获取__ 可以在 UI 页面查看获取对应信息的方式。

3. 参考以下信息填写 __备份策略__ 。

    - 备份方式：选择手动备份或定时备份
    
        - 手动备份：基于备份配置立即执行一次 ETCD 全量数据的备份。
        - 定时备份：按照设置的备份频率对 ETCD 数据进行周期性全量备份。
    
    - 备份链长度：最多保留多少条备份数据。默认为 30 条。
    - 备份频率：支持小时、日、周、月级别和自定义方式。

        ![定时备份](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/etcd04.png)

4. 参考以下信息填写 __存储位置__ 。
   
    - 存储供应商：默认选择 S3 存储
    - 对象存储访问地址：MinIO 的访问地址
    - 存储桶：在 MinIO 中创建一个 Bucket，填写 Bucket 的名称
    - 用户名：MinIO 的登录用户名
    - 密码：MinIO 的登录密码

        ![存储位置](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/etcd05.png)

5. 点击 __确定__ 后页面自动跳转到备份策略列表，可以查看目前创建好的所有策略。

    - 在策略右侧点击 __ⵗ__ 操作按钮可以查看日志、查看 YAML、更新策略、停止策略、立即执行策略等。
    - 当备份方式为手动时，可以点击 __立即执行__ 进行备份。
    - 当备份方式为定时备份时，则会根据配置的时间进行备份。

        ![成功创建](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/etcd07.png)

## 查看备份策略日志

点击 __日志__ 可以查看日志内容，默认展示 100 行。若想查看更多日志信息或者下载日志，可在日志上方根据提示前往可观测性模块。

![查看日志](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/etcd06.png)

## 查看备份策略详情

进入 __容器管理__ -> __备份恢复__ -> __ETCD 备份__ ，点击 __备份策略__ 页签，接着点击策略名称可以查看策略详情。

![备份策略详情](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/etcd09.png)

## 查看备份点

1. 进入 __容器管理__ -> __备份恢复__ -> __ETCD 备份__ ，点击 __备份点__ 页签。
2. 选择目标集群后，可以查看该集群下所有备份信息。

    每执行一次备份，对应生成一个备份点，可通过成功状态的备份点快速恢复应用。

    ![备份点](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/etcd08.png)
