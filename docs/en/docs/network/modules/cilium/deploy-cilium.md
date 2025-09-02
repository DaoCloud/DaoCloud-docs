# Deploying Cilium

This document uses Cilium v1.17.6 as an example to explain how to deploy Cilium into your Kubernetes cluster.

1. Preparation

    1. If you install a new cluster using Kubespray, it is recommended to set the argument `kube_network_plugin=cni`.
      For clusters already installed with Calico, after Cilium is successfully installed, follow the [Uninstall Calico](#calico) steps to remove Calico.

    2. Copy the entire project to the master node and ensure the following CLIs are available: helm, kubectl, jq.

        Note: It is best to use Helm version higher than v3.17.3 (as v3.9.4 has been tested to cause syntax compatibility issues with the Cilium Chart).

    3. Ensure Kubernetes cluster is already installed.

        If you use Kubespray to install the cluster, you can specify the options `kube_network_plugin=cni` and `kube_proxy_remove=true`.

    4. Refer to the official [Cilium system requirements](https://docs.cilium.io/en/stable/operations/system_requirements/#admin-system-reqs).

2. Install Cilium

    Enter the Cilium subdirectory of the project and run the following command. This will complete the CLI installation and Chart installation.

    The Cilium installed in this way runs in vxlan tunnel mode by default, with all compatible features enabled.

    Images are pulled from DaoCloud online repository by default.

    Installing a single-stack cluster:

    ```bash
    export POD_v4CIDR="172.16.0.0/16"
    export POD_v4Block="24"
    export CLUSTER_NAME="cluster1"
    export CLUSTER_ID="10"
    export CLUSTERMESH_APISERVER_NODEPORT="31001"
    export K8S_API_IP="10.0.1.11"
    export K8S_API_PORT="6443"
    export HUBBLE_WEBUI_NODEPORT_PORT="31000"
    export INTEGRATE_ISTIO="false"
    ./setup.sh
    ```

    Installing a dual-stack cluster:

    ```bash
    export POD_v4CIDR="172.16.0.0/16"
    export POD_v4Block="24"
    export ENABLE_IPV6="true"
    export POD_v6CIDR="fd00::/48"
    export POD_v6Block="64"
    export CLUSTER_NAME="cluster1"
    export CLUSTER_ID="10"
    export CLUSTERMESH_APISERVER_NODEPORT="31001"
    export K8S_API_IP="10.0.1.11"
    export K8S_API_PORT="6443"
    export HUBBLE_WEBUI_NODEPORT_PORT="31000"
    export INTEGRATE_ISTIO="false"
    ./setup.sh
    ```

    | Argument | Description |
    | --------- | ----------- |
    | `POD_v4CIDR` | The Pod IPv4 CIDR of this cluster. Note: If you need to enable multi-cluster networking later, ensure the `POD_v4CIDR` of each cluster does not overlap. |
    | `POD_v4Block` | The size of the Pod subnet allocated to each node. |
    | `ENABLE_IPV6` | Whether to enable IPv6. If the cluster host NICs are not configured with IPv6 addresses and Kubernetes is not set to dual-stack, do not enable dual-stack. |
    | `CLUSTER_NAME` | The name of this cluster. Must be unique to avoid conflicts when enabling multi-cluster connectivity. |
    | `CLUSTER_ID` | The ID of this cluster (valid range: 1–255). Must also be unique. |
    | `CLUSTERMESH_APISERVER_NODEPORT` | The nodePort number used for Cilium multi-cluster networking. You can manually specify a value within the valid nodePort range (30000–32767). Note: This argument must be unique for each cluster, otherwise multi-cluster networking will fail. |
    | `K8S_API_IP` | The address of this cluster’s Kubernetes API server. This cannot be a clusterIP. It must be a single host’s physical address or a high-availability address provided by tools such as keepalived. |
    | `K8S_API_PORT` | The port of this cluster’s Kubernetes API server. This allows Cilium to access the API server and provide Service functionality even without kube-proxy. |
    | `HUBBLE_WEBUI_NODEPORT_PORT` | The nodePort number for the Cilium observability GUI. You can manually specify a value within the valid nodePort range (30000–32767). Cilium follows the clusterIP CIDR settings of the Kubernetes cluster and allows overlapping clusterIP CIDRs across different clusters. |
    | `INTEGRATE_ISTIO` | Whether Istio runs on the Cilium network. If set to `true`, Cilium’s working arguments will be tuned for Istio. |

3. After completing the Cilium installation, you can run the following commands to check the status of Cilium in this cluster:

    ```bash
    chmod +x ./showStatus.sh
    ./showStatus.sh
    ```

    After installation, you can access the Cilium observability GUI through the nodePort defined by `CLUSTERMESH_APISERVER_NODEPORT`.

4. (Optional) Uninstall Calico

    If your cluster has Calico installed, refer to the [Uninstall Calico](#calico) steps to remove it.

5. (Optional) Uninstall kube-proxy

    Since Cilium works in kube-proxy replacement mode, if kube-proxy is still running in the cluster, it has no effect and can be removed.

    ```bash
    # Replace the kube-proxy startup command so it only cleans up host rules
    kubectl patch daemonset kube-proxy -n kube-system --type='json' -p='[
      {
        "op": "replace",
        "path": "/spec/template/spec/containers/0/command",
        "value": [
          "/usr/local/bin/kube-proxy",
          "--cleanup"
        ]
      }
    ]'

    # Wait until all kube-proxy pods restart and exit, then uninstall
    kubectl delete daemonset kube-proxy -n kube-system

    # Or modify the nodename so it does not run on any node
    # kubectl patch daemonset kube-proxy -n kube-system --type='json' -p='[{"op": "add", "path": "/spec/template/spec/nodeName", "value": "notexsitednode"}]'
    ```

6. (Optional) Enable Cilium metrics and Grafana dashboards

    1. Ensure Grafana and Prometheus are installed (Grafana and Prometheus CRDs must already exist in the cluster).

    2. Enter the Cilium subdirectory of the project and run the following commands to enable metrics and dashboards:

        ```bash
        chmod +x ./setupMetrics.sh
        ./setupMetrics.sh
        ```

    3. Once metrics and dashboards are enabled, you can view Cilium dashboards in Grafana. You can also install the DCE-defined alert rules and curated dashboards:

        ```bash
        kubectl apply -n <Insight tenant> -f ./cilium/yamls/ciliumPrometheusRules.yaml
        ```

        ```bash
        kubectl apply -n <Insight tenant> -f ./cilium/yamls/ciliumGrafana.yaml

        # Restart Grafana Pod
        ```

7. (Optional) Enable multi-cluster connectivity

    Note: When applications between multiple Cilium clusters need to communicate via nodePort, port conflicts may occur, causing client clusters to resolve the Service to the local cluster, resulting in access errors. Therefore, always use this feature to connect clusters and rely on Services for east-west traffic to solve this problem.

    1. Create the `/root/clustermesh` directory and copy the `/root/.kube/config` from all clusters that need interconnection into this directory, naming them `/root/clustermesh/cluster1`, `/root/clustermesh/cluster2`, `/root/clustermesh/cluster3` …

    2. Enter the Cilium subdirectory of the project and run the following command to configure multi-cluster connectivity:

        ```bash
        chmod +x ./showClusterMesh.sh
        ./setupClusterMesh.sh  /root/clustermesh/cluster1  /root/clustermesh/cluster2 [/root/clustermesh/cluster3 ... ]
        ```

    3. Check the multi-cluster connectivity status:

        Enter the Cilium subdirectory of the project and run:

        ```bash
        ./showClusterMesh.sh
        ```

## Uninstall Cilium

```bash
chmod +x ./uninstall.sh
./uninstall.sh
```

## Uninstall Calico

1. First, on the **controller node with kubectl**, run the following commands to uninstall Calico Kubernetes resources:

    ```bash
    kubectl get crd | grep projectcalico | awk '{print $1}' | xargs kubectl delete crd || true
    kubectl delete deploy -n kube-system calico-kube-controllers || true
    kubectl delete ds -n kube-system calico-node || true
    kubectl delete sa -n kube-system calico-kube-controllers calico-cni-plugin calico-node || true
    kubectl delete clusterrolebinding calico-cni-plugin calico-kube-controllers calico-node || true
    ```

2. Enter the Cilium subdirectory and run `uninstall_calico.sh` on **each node** to clean up residual Calico networking resources, including its CNI config files and iptables rules:

    ```bash
    chmod +x ./uninstall_calico.sh
    ./uninstall_calico.sh
    ```

3. To quickly migrate existing Pods to the Cilium network, you can choose one of the following methods:

    * Reboot each host sequentially to fully clean up Calico’s residual network rules (recommended).
    * If rebooting is not possible, run `restartAllPods.sh` on each node. This will restart all Pod sandbox containers so Cilium can reset Pod networking. This will not restart application containers and will not affect logs, etc.

    ```bash
    chmod +x ./restartAllPods.sh
    ./restartAllPods.sh
    ```

## Running Cilium with Istio

When Istio and Cilium work together, refer to the
[Cilium official documentation](https://docs.cilium.io/en/latest/network/servicemesh/istio/) for required argument tuning.

* During Cilium installation, set `export INTEGRATE_ISTIO="true"` to adjust Cilium’s working arguments.
* Do not use Cilium and Istio L7 HTTP policy at the same time.
* When using Istio in sidecar mode with automatic sidecar injection, if combined with Cilium tunnel mode (VXLAN or GENEVE), ensure the istiod Pod runs with `hostNetwork=true` so it can be accessed by the API server.

## Operations and Troubleshooting

* Run `./cilium/showStatus.sh` to check the status of Cilium in the cluster.
* Run `cilium sysdump` to export a compressed package containing the status of all Cilium components in the cluster.
* Packet capture:

    1. Monitor real-time local node traffic. This is the most complete and lowest-level method, but it cannot show traffic records:

        ```bash
        kubectl -n kube-system exec ds/cilium -- cilium-dbg monitor -vv
        ```

    2. View real-time traffic and historical records filtered by hubble:

        ```bash
        kubectl -n kube-system exec ds/cilium -- hubble observe -f
        ```

    3. Using hubble on the host:

        View all cluster traffic events:

        ```bash
        cilium hubble port-forward &
        ```

        View all traffic:

        ```bash
        hubble observe -f
        ```

        View dropped traffic:

        ```bash
        hubble observe --verdict DROPPED --verdict ERROR  -f
        ```

        View traffic of a specific Pod:

        ```bash
        hubble observe --since 3m --pod default/tiefighter -f
        ```
