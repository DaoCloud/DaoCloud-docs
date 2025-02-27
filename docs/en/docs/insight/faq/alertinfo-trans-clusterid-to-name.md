# Prometheus Cluster Label Configuration

This document explains how to modify Prometheus (CR) to add a cluster label (`cluster_name`)
to monitoring metrics, improving the readability of metrics and alert messages.

## Method 1: Modify Prometheus Directly

1. Run the following command to locate the Prometheus (CR):

    ```shell
    kubectl get prometheus -n insight-system
    ```

    Expected output example:

    ```
    NAME                                    VERSION   DESIRED   READY   RECONCILED   AVAILABLE   AGE
    insight-agent-kube-prometh-prometheus   v2.44.0   1         1       True         True        73d
    ```

2. Edit the Prometheus CR and add `cluster_name` under the `spec.externalLabels` parameter.
   This value should match the registered cluster name in container management.

    ```diff
    apiVersion: monitoring.coreos.com/v1
    kind: Prometheus
    metadata:
      name: insight-agent-kube-prometh-prometheus
      namespace: insight-system
    spec:
      externalLabels:
        cluster: deb65d24-1090-40cf-b5e6-489fac2f2c1b
    +   cluster_name: kpanda-global-cluster
    ```

## Method 2: Modify via Helm (Recommended)

1. It is recommended to update the `Prometheus CR` via Helm to avoid losing these configurations
   during upgrades. Edit the relevant parameters in `values.yaml`:

    ```diff
    kube-prometheus-stack:
      prometheus:
        prometheusSpec:
          externalLabels:
            cluster: '{{ (lookup "v1" "Namespace" "" "kube-system").metadata.uid }}'
    +       cluster_name: 'kpanda-global-cluster'
    ```

2. Alternatively, you can set the value using the `--set` flag:

    ```shell
    --set kube-prometheus-stack.prometheus.prometheusSpec.externalLabels.cluster_name='kpanda-global-cluster'
    ```

## Additional Notes

Starting from container management v0.27, the cluster name is also recorded in the
`kpanda-system` namespace under the label `kpanda.io/cluster-name`.

```shell
kubectl get ns kpanda-system -o yaml
```

```yaml
apiVersion: v1
kind: Namespace
metadata:
  finalizers:
  - kpanda.io/kpanda-system
  labels:
    kpanda.io/cluster-name: kpanda-global-cluster
    kpanda.io/kube-system-id: deb65d24-1090-40cf-b5e6-489fac2f2c1b
    kubernetes.io/metadata.name: kpanda-system
    name: kpanda-system
  name: kpanda-system
spec:
  finalizers:
  - kubernetes
status:
  phase: Active
```
