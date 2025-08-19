# 安装设备管理组件

设备管理模块需同时安装前端 UI 组件和后端服务组件，DCE 5.0 安装器 v0.33.0 及以上版本，支持安装设备管理前端 UI 组件，**无需自行安装** ；请联系交付支持团队获取商业版安装包。

操作流程如下：

1. 安装前端 UI 组件 topohub-dashboard

    商业版本安装流程请参考 [安装教程](../../install)。

    topohub-dashboard 组件默认不安装，请先修改 **manifest** 配置文件。

    manifest 示例如下：

    ```yaml title="manifest.yaml"
    apiVersion: manifest.daocloud.io/v1alpha1
    kind: DCEManifest
    metadata:
    global:
    helmRepo: https://release.daocloud.io/chartrepo
    imageRepo: release.daocloud.io
    infrastructures:
    hwameiStor:
        enable: true
        version: v0.10.4
        policy: drbd-disabled
    istio:
        version: 1.16.1
    metallb:
        version: 0.13.9
    contour:
        version: 10.2.2
        enable: false
    cert-manager:
        version: 1.11.0
        enable: false
    mysql:
        version: 8.0.29
        cpuLimit: 1
        memLimit: 1Gi
        enableAutoBackup: true
    redis:
        version: 6.2.6-debian-10-r120
        cpuLimit: 400m
        memLimit: 500Mi
    components:
    kubean:
        enable: true
        helmVersion: v0.6.6
        helmRepo: https://kubean-io.github.io/kubean-helm-chart
        variables:
    ghippo:
        enable: true
        helmVersion: 0.18.0
        variables:
    kpanda:
        enable: true
        helmVersion: 0.19.0+rc4
        variables:
    insight:
        enable: true
        helmVersion: 0.18.0-rc5
        variables:
    insight-agent:
        enable: true
        helmVersion: 0.18.0-rc5
        features: tracing
    topohub-dashboard:  #设备管理 UI 组件
        enable: true    # 默认为 false，不安装，需要安装设备管理模块时，请修改为 true
        helmVersion: 0.3.0

    ```

2. 安装后端服务组件 topohub

> 后端服务组件仅需安装在[全局服务集群](../../kpanda/user-guide/clusters/cluster-role.md#_2)

打开全局服务集群，然后在 __Helm 应用__ -> __Helm 模板__ 找到 `topohub` 执行安装步骤。

    - BMC 账号密码：连接主机 BMC 的默认账号和密码。
    - DHCP Sever：节点上能够访问所有管理设备网络的网卡名，其以 trunk 模式接入到交换机，例如 eth1。
    - Topohub working node：topohub 组件部署运行的节点名。

!!! note "注意事项"

    * 如果主机 BMC 账号密码不相同，请编辑 yaml 添加多个。


## 结语

以上步骤完成后，就可以在 DCE5.0 正常体验设备管理的全部功能了，祝你使用愉快！
