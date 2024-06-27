---
MTPE: ModetaNiu
date: 2024-06-27
---

# How to Configure Extended Parameters When Deploying a Cluster?

!!! note

    Before configuring extended parameters in a production environment, it is recommended to fully understand the behavior 
    of the relevant parameters and be aware of any potential side effects. Only then should you decide whether to actually use them. 
    It is advisable to conduct feasibility verification before going live!

This article will describe how to configure extended parameters for both DCE 5.0 [global-service-clusters](../../kpanda/user-guide/clusters/cluster-role.md#global-service-cluster) and [worker clusters](../../kpanda/user-guide/clusters/cluster-role.md#worker-clusters).

## Supported Extended Parameters

DCE 5.0 relies on the open-source software Kubespray for cluster deployment, so basically, any configuration parameters 
supported by Kubespray can be configured under DCE 5.0.

For configurable parameters supported by Kubespray, refer to the [community documentation](https://github.com/kubernetes-sigs/kubespray/blob/v2.25.0/docs/ansible/vars.md#common-vars-that-are-used-in-kubespray).

**Examples of some common variables:**

| Parameter | Description | Valid Values | Default Value |
|-----------|-------------|--------------|---------------|
| calico_ipip_mode | Configures Calico IPIP encapsulation | 'Never', 'Always', 'CrossSubnet' | 'Never' |
| calico_vxlan_mode | Configures Calico VXLAN encapsulation | 'Never', 'Always', 'CrossSubnet' | 'Always' |
| calico_network_backend | Configures Calico network backend | 'none', 'bird', 'vxlan' | 'vxlan' |
| kube_network_plugin | Sets Kubernetes network plugin | | Calico |
| kube_proxy_mode | Changes Kubernetes proxy mode to iptables mode | | |
| searchdomains | Array of DNS domains to search when looking up hostnames | | |
| remove_default_searchdomains | Boolean that removes the default search domain | | |
| nameservers | Array of nameservers to use for DNS lookup | | |
| preinstall_selinux_state | Sets SELinux state | permissive, enforcing, disabled | |

## Configuring Extended Parameters When Installing a Global Cluster

Refer to [Step 2 of the Offline Installation of DCE 5.0 Commercial Version](../commercial/start-install.md/#step-2-edit-clusterconfigyaml).

In the [ClusterConfig.yml](../commercial/cluster-config.md) configuration file, update the `kubeanConfig` parameter information as follows:

```yaml
apiVersion: provision.daocloud.io/v1alpha3
kind: ClusterConfig
metadata:
  creationTimestamp: null
spec:
  clusterName: my-cluster
    
  ...
  # Add extended parameters under kubeanConfig
  kubeanConfig: |-
    preinstall_selinux_state: disabled
  ...
```

## Configuring Extended Parameters When Installing a Working Cluster

Refer to [creating work clusters](../../kpanda/user-guide/clusters/create-cluster.md), 
and define the extended parameters in the custom parameters in Step 5.
