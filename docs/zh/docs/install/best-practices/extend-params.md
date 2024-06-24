# 部署集群时如何配置扩展参数？

!!! note

    在生产环境场景下进行扩展参数配置之前，建议先充分了解相关参数的行为，明确配置可能存在的副作用后，再决定是否实际使用，建议先进行可行性验证后在上生产！

本文将从 DCE5.0 Global 集群、工作集群两个方面描述如何配置扩展参数。

## 支持的扩展参数

DCE5.0 部署集群依赖了开源软件 Kubespray，所以基本上 Kubespray 支持的配置参数都可以通过 DCE5.0 下配置。

关于 Kubespray 支持的可配置参数可查看[社区文档](https://github.com/kubernetes-sigs/kubespray/blob/v2.25.0/docs/ansible/vars.md#common-vars-that-are-used-in-kubespray)

**一些常用变量示例：**

- calico_ipip_mode - Configures Calico ipip encapsulation - valid values are 'Never', 'Always' and 'CrossSubnet' (default 'Never')
- calico_vxlan_mode - Configures Calico vxlan encapsulation - valid values are 'Never', 'Always' and 'CrossSubnet' (default 'Always')
- calico_network_backend - Configures Calico network backend - valid values are 'none', 'bird' and 'vxlan' (default 'vxlan')
- kube_network_plugin - Sets k8s network plugin (default Calico)
- kube_proxy_mode - Changes k8s proxy mode to iptables mode
- searchdomains - Array of DNS domains to search when looking up hostnames
- remove_default_searchdomains - Boolean that removes the default searchdomain
- nameservers - Array of nameservers to use for DNS lookup
- preinstall_selinux_state - Set selinux state, permitted values are permissive, enforcing and disabled.

## 安装 Global 集群时配置可扩展参数

参考[离线安装 DCE 5.0 商业版第二步](../commercial/start-install.md/#2-clusterconfigyaml)。

在 [ClusterConfig.yml](../commercial/cluster-config.md) 配置文件中，更新 kubeanConfig 参数信息，如下：

```yaml

apiVersion: provision.daocloud.io/v1alpha3
kind: ClusterConfig
metadata:
  creationTimestamp: null
spec:
  clusterName: my-cluster
    
  ...
  # 扩展参数添加在 kubeanConfig 当中
  kubeanConfig: |-
    preinstall_selinux_state: disabled
  ...
```

## 安装工作集群时配置可扩展参数

参考[创建工作集群](../../kpanda/user-guide/clusters/create-cluster.md)，第五步中的自定义参数中定义扩展参数，如下：

[extend-parames](../images/extend-%20parameters.png)
