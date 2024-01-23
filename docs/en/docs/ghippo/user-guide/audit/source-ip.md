# Get Source IP in Audit Logs

The source IP in audit logs plays a critical role in system and network management.
It helps track activities, maintain security, troubleshoot issues, and ensure system
compliance. However, obtaining the source IP can result in some performance overhead.
Therefore, in DCE 5.0, audit logs are not always enabled.

The default enablement of source IP in audit logs and the methods to enable it vary
depending on the installation mode. The following sections will explain the default
enablement and the steps to enable source IP in audit logs based on the installation mode.

## Determining the Installation Mode

```bash
kubectl get pod -n metallb-system
```

Run the above command in the cluster. If the result is as follows,
it means that the cluster is not in the Metallb installation mode:

```console
No resources found in metallbs-system namespace.
```

## NodePort Installation Mode

In this mode, the source IP in audit logs is disabled by default.
The steps to enable it are as follows:

1. Set the maximum and minimum replicas of the __istio-ingressgateway__ HPA to the number of nodes:

    ```bash
    count=$(kubectl get node | wc -l)
    count=$((count-1))

    if [ $count -gt 5 ]; then
        kubectl patch hpa istio-ingressgateway -n istio-system -p '{"spec":{"maxReplicas":'$count',"minReplicas":'$count'}}'
    else
        kubectl patch hpa istio-ingressgateway -n istio-system -p '{"spec":{"minReplicas":'$count'}}'
    fi
    ```

2. Modify the __externalTrafficPolicy__ value of the __istio-ingressgateway__ service to "Local":

    ```bash
    kubectl patch svc istio-ingressgateway -n istio-system -p '{"spec":{"externalTrafficPolicy":"Local"}}'
    ```

## Metallb Installation Mode

In this mode, source IP in audit logs is obtained by default after the installation.
For more information, refer to [Metallb Source IP](../../../network/modules/metallb/source_ip.md).
