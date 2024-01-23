# Troubleshooting on joining DCE 4.0

This page lists some common issues encountered when joining DCE 4.0 with service mesh.

## LimitRange Issue

### Symptoms

1. When joining DCE 4.0, an error occurs:

    ```console
    message: 'unable to retrieve Pods: Unauthorized'
    ```

2. Control plane cluster:

    The following error is displayed:

    ```console
    mspider-mcpc-mcpc-controller-5bd6d54c4-df6kg  CrashLoopBackOff
    ```

    Checking the logs of the control plane:

    ```shell
    kubectl logs -n istio-system mspider-mcpc-mcpc-controller-5bd6d54c4-df6kg
    ```

    ```console
    time="2022-10-19T06:35:49Z" level=error msg="Unable to get kube configs of multi clusters: Get \"http://mspider-mcpc-ckube-remote/api/v1/namespaces/istio-system/configmaps/mspider-mcpc-remote-kube-api-server?resourceVersion=dsm-cluster-dce4-mspider\": dial tcp: lookup mspider-mcpc-ckube-remote: i/o timeout" func="cmholder.NewConfigHolder()" file="holder.go:52"
    panic: unable to get kube configs of multi clusters: Get "http://mspider-mcpc-ckube-remote/api/v1/namespaces/istio-system/configmaps/mspider-mcpc-remote-kube-api-server?resourceVersion=dsm-cluster-dce4-mspider": dial tcp: lookup mspider-mcpc-ckube-remote: i/o timeout

    goroutine 1 [running]:
    main.main()
        /app/cmd/control-plane/mcpc/main.go:62 +0x694
    ```

3. rs: istio-operator-*** error:

    ```console
    message: 'pods "istio-operator-5fbbf5bbd-hf2q2" is forbidden: memory max limit
        to request ratio per Container is 1, but provided ratio is 2.000000'
    ```

### Solution

Manually set the limit range in the `istio-operator` and `istio-system` namespaces to set the overallocation ratio to 0.

Run the following command to view the limit range in the `istio-operator` namespace:

```shell
kubectl describe limits -n istio-operator dce-default-limit-range
```

Run the following command to view the limit range in the `istio-system` namespace:

```shell
kubectl describe limits -n istio-system dce-default-limit-range
```

## istiod and ingressgateway are always in ContainerRunning state

Root cause analysis: DCE 4.0 uses Kubernetes version 1.18, which is relatively outdated for the new version of the service mesh.

Symptom 01: 'istio-managed-istio-hosted' fails to start, indicating that the Configmap of 'istio-token' does not exist.

To resolve this issue, manually for grid instance of CR ` GlobalMesh ` add corresponding parameters: `istio.custom_params.values.global.jwtPolicy`.

![params](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/mspider/troubleshoot/images/dce4-01.png)

!!! tip

    1. Before integrating with the new version of the service mesh, deploy coreDNS in advance for DCE 4.0.
    2. The `Global Mesh` configuration is in Global Cluster, not in the access cluster.
