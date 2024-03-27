# IPPool 修改及新建

本章节介绍 Metallb 组件部署后，需要修改已经创建好的 IPPool 或者新建新的 IPPool。

## 前提条件

- [Metallb 已部署](install.md)

## 修改 IPPool 

创建 Metallb 创建时已开启 ARP 模式，并且 IP Pool 已创建，需要修改 IP Pool 中的信息。

![metallb-01](../../images/metallb-01.jpg) 

修改方式如下：

1. 点击对应集群名进入详情，选择 **自定义资源** ，搜索找到 `ipaddresspools.metallb.io` 点击 CRD 资源名称，进入详情。

    ![metallb -02](../../images/metallb-02.jpg)

2. 点击 CRD 名称，进入详情，选择 metallb 所部署的命名空间（示例中 metallb 部署在 `kube-system`），编辑 CR 示例（default-pool）YAML。

    ![metallb -02](../../images/metallb-03.jpg)

3. 修改 IP 地址及其他信息，并保存。

    ![metallb -02](../../images/metallb-04.jpg)

## 新建 IPPool 

如果创建 LB 类型 Service 需要使用新的 IP Pool ，创建方式如下：

1. 点击对应集群名进入详情，选择 **自定义资源** ，搜索找到 `ipaddresspools.metallb.io` 点击 CRD 资源名称，进入详情。

2. 点击 CRD 名称，进入详情，选择 metallb 所部署的命名空间（示例中 metallb 部署在 `kube-system`），点击 **YAML 创建** ，输入如下 YAML。

    YAML 创建 IP Pool 示例：

    ```yaml
    apiVersion: metallb.io/v1beta1
    kind: IPAddressPool
    metadata:
      annotations:
        helm.sh/hook: post-install
        helm.sh/resource-policy: keep
      name: custom-pool # IP Pool 名称
      namespace: kube-system # 部署命名空间，同 metallb 实例在同一个命名空间
    spec:
      addresses:
        - 10.5.10.240-10.5.10.245 # IP地址同指定网卡在同一个网段
      autoAssign: true
      avoidBuggyIPs: true
    ```

    创建时请注意，输入的 IP 地址需要同[创建 metallb 实例](install.md)时指定的网卡在同一个网段。

4. 点击确认完成创建，创建成功后可在 [LB 类型 Service 创建](../../../kpanda/user-guide/network/create-services.md)时选择对应 IP Pool。

    ![metallb-05](../../images/metallb-05.jpg)

更多使用方式可参考：[IPPool 使用说明](usage.md)
