---
MPTE: WANG0608GitHub
Date: 2024-08-13
---

# Get Source IP in Audit Logs

The source IP in audit logs plays a critical role in system and network management.
It helps track activities, maintain security, resolve issues, and ensure system
compliance. However, getting the source IP can result in some performance overhead,
so that audit logs are not always enabled in DCE 5.0.
The default enablement of source IP in audit logs and the methods to enable it vary
depending on the installation mode. The following sections will explain the default
enablement and the steps to enable source IP in audit logs based on the installation mode.

!!! note

    Enabling audit logs will modify the replica count of the istio-ingressgateway, resulting in a certain performance overhead.
    Enabling audit logs requires disabling LoadBalance of kube-proxy and Topology Aware Routing, which can have a certain impact on cluster performance.
    After enabling audit logs, it is essential to ensure that the istio-ingressgateway exists on the proper node to the access IP. If the istio-ingressgateway drifts due to node health issues or other issues, it needs to be manually rescheduled back to that node. Otherwise, it will affect the normal operation of DCE 5.0.

## Determine the Installation Mode

```bash
kubectl get pod -n metallb-system
```

Run the above command in the cluster. If the result is as follows,
it means that the cluster is not in the MetalLB installation mode:

```console
No resources found in metallbs-system namespace.
```

## NodePort Installation Mode

In this mode, the source IP in audit logs is disabled by default.
The steps to enable it are as follows:

1. Set the minimum replica count of the __istio-ingressgateway__ HPA to be equal to the number of control plane nodes

    ```bash
    count=$(kubectl get nodes --selector=node-role.kubernetes.io/control-plane | wc -l)
    count=$((count-1))

    kubectl patch hpa istio-ingressgateway -n istio-system -p '{"spec":{"minReplicas":'$count'}}'
    ```

2. Modify the __externalTrafficPolicy__ and  __internalTrafficPolicy__ value of the __istio-ingressgateway__ service to "Local"

    ```bash
    kubectl patch svc istio-ingressgateway -n istio-system -p '{"spec":{"externalTrafficPolicy":"Local","internalTrafficPolicy":"Local"}}'
    ```

## MetalLB Installation Mode

In this mode, the source IP in audit logs is gotten by default after the installation.
For more information, refer to [MetalLB Source IP](../../../network/modules/metallb/source_ip.md).
