---
hide:
  - toc
---

# 接入集群

通过接入集群操作，能够对众多云服务平台集群和本地私有物理集群进行统一纳管，形成统一治理平台，有效避免了被厂商锁定风险，助力企业业务安全上云。

容器管理模块支持接入多种主流的容器集群，例如 DaoCloud KubeSpray, DaoCloud ClusterAPI, DaoCloud Enterprise 4.0、Redhat Openshift, SUSE Rancher, VMware Tanzu, Amazon EKS, Aliyun ACK, Huawei CCE, Tencent TKE,标准 Kubernetes 集群。

## 前提条件

- 准备一个待接入的集群，确保容器管理集群和待接入集群之间网络通畅，并且集群的 Kubernetes 版本 1.22+。
- 当前操作用户应具有 [Kpanda Owner](../permissions/permission-brief.md) 或更高权限。

## 操作步骤

1. 进入 __集群列表__ 页面，点击右上角的 __接入集群__ 按钮。

    ![接入集群](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/join001.png)

2. 填写基本信息。

    - 集群名称：名称应具有唯一性，设置后不可更改。最长 63 个字符，只能包含小写字母、数字及分隔符("-")，且必须以小写字母或数字开头及结尾。
    - 集群别名：可输入任意字符，不超过 60 个字符。
    - 发行版：集群的发行厂商，包括市场主流云厂商和本地私有物理集群。

3. 填写目标集群的 KubeConfig，点击 __验证 Config__ ，验证通过后才能成功接入集群。

    > 如果不知道如何获取集群的 KubeConfig 文件，可以在输入框右上角点击 __如何获取 kubeConfig__ 查看对应步骤。
    ![接入集群](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/join003.png)

4. 确认所有参数填写正确，在页面右下角点击 __确定__ 。

    ![接入集群](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/join002.png)

!!! note

    - 新接入的集群状态为 __接入中__ ，接入成功后变为 __运行中__ 。
    - 如果集群状态一直处于 __接入中__ ，请确认接入脚本是否在对应集群上执行成功。有关集群状态的更多详情，请参考[集群状态](cluster-status.md)。
