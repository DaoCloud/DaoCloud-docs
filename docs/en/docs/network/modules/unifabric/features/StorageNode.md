# Storage Node Access Guide

## Feature Overview

Unifabric supports connecting external bare-metal storage nodes to a Kubernetes cluster for
unified management and monitoring. By deploying the unifabric agent on a storage node, the agent
collects the RDMA network status and LLDP neighbor information of the storage node and reports
the data to the unifabric control plane in the Kubernetes cluster. You can also view the
monitoring data of storage nodes on the Grafana dashboard of the cluster.

## Basic Requirements

1. Docker must be installed on the storage node (docker compose support is required).
2. The storage node must be able to access the API Server of the Kubernetes cluster.
3. The storage node must be a bare-metal server with RDMA NICs.
4. The unifabric components must already be deployed and running in the Kubernetes cluster to be
   connected.

## Create the kubeconfig File

On the control node of the Kubernetes cluster to which the storage node will be connected, run
the following commands to generate the kubeconfig file:

```shell
# Specify the namespace in which unifabric is installed
UNIFABRIC_NAMESPACE="unifabric"

cat > cluster1-kubeconfig.yaml <<EOF
apiVersion: v1
kind: Config
clusters:
- cluster:
    certificate-authority-data: $(kubectl config view --raw -o jsonpath="{.clusters[0].cluster.certificate-authority-data}")
    server: $(kubectl config view --raw -o jsonpath="{.clusters[0].cluster.server}")
  name: $(kubectl config view --raw -o jsonpath="{.clusters[0].name}")
contexts:
- context:
    cluster: $(kubectl config view --raw -o jsonpath="{.clusters[0].name}")
    user: unifabric-sa-token
    namespace: ${UNIFABRIC_NAMESPACE}
  name: unifabric-sa-token@$(kubectl config view --raw -o jsonpath="{.clusters[0].name}")
current-context: unifabric-sa-token@$(kubectl config view --raw -o jsonpath="{.clusters[0].name}")
users:
- name: unifabric-sa-token
  user:
    token: $(kubectl get secret unifabric-sa-token -n ${UNIFABRIC_NAMESPACE} -o jsonpath='{.data.token}' | base64 -d)
EOF
```

This kubeconfig file is generated based on the ServiceAccount `unifabric-sa-token` in the
namespace where unifabric is installed, and contains only the minimum permissions required to
access unifabric.

Verify locally that the content of the kubeconfig file is correct:

```shell
kubectl --kubeconfig=cluster1-kubeconfig.yaml version
kubectl --kubeconfig=cluster1-kubeconfig.yaml get pods -A
```

Copy the kubeconfig file to the storage node server at
`/etc/unifabric/cluster1-kubeconfig.yaml` for use in the following steps.

## Deploy lldp and the unifabric Agent (Using Docker Compose)

This section describes how to use Docker Compose to deploy the lldp and unifabric agent services
on a storage node. Perform the following steps on each logical bare-metal storage node.

### 1. Run the lldp Service

Deploy the unifabric-lldp service on each storage host. Even if a host is connected to multiple
Kubernetes clusters, only one instance needs to be deployed. First, create the
`/etc/unifabric/lldp.yaml` file:

```shell
sudo mkdir -p /etc/unifabric
cat <<'EOF' | sudo tee /etc/unifabric/lldp.yaml > /dev/null
services:
  unifabric-lldp:
    image: ${UNIFABRIC_AGENT_IMAGE}
    container_name: unifabric-lldp
    command: ["/usr/bin/unifabric/entrypoint.sh"]
    network_mode: host
    restart: always
    privileged: true
    environment:
      # Node IP information (optional)
      NODE_IPADDRESS: ${NODE_IPADDRESS}
      # LLDP transmission interval in seconds (optional)
      LLDPD_TX_INTERVAL: 30
      # Interfaces on which to enable LLDP, as a comma-separated list
      # LLDPD_INTERFACE_PATTERN: ""
    volumes:
      - /var/run:/var/run
      - /etc/hostname:/etc/hostname:ro
    healthcheck:
      test: CMD-SHELL lldpcli -v || exit 1
      interval: 5s
      timeout: 3s
      retries: 5
EOF
```

Start the lldp service with the following command:

- Set the `UNIFABRIC_AGENT_IMAGE` environment variable to specify the Agent image version, using
  the version that matches the Kubernetes cluster.
- Optionally set the `NODE_IPADDRESS` environment variable to specify the node IP address. This
  IP address will be used for LLDP broadcasting.

```shell
UNIFABRIC_AGENT_IMAGE="release.daocloud.io/unifabric/unifabric-agent:latest" \
  sudo -E docker compose -f /etc/unifabric/lldp.yaml up -d
```

### 2. Start the unifabric-agent Service

Make sure that the kubeconfig created in the previous section exists at
`/etc/unifabric/cluster1-kubeconfig.yaml`.

Create the unifabric agent configuration file `/etc/unifabric/cluster1-agent-config.yaml`:

```shell
export METRICS_PORT=5025
export STORAGE_RDMA_NIC_FILTER="interface=*"

cat <<EOF | sudo tee /etc/unifabric/cluster1-agent-config.yaml > /dev/null
inStorageNode: true
metrics:
  port: ${METRICS_PORT}
rdmaNeighbor:
  # Matches the storage RDMA NIC, wildcards are supported
  storageRdmaNicFilter: "${STORAGE_RDMA_NIC_FILTER}"
EOF
```

- `inStorageNode` indicates that the Agent runs on an external storage node and must be set to
  `true`.
- The `metrics.port` parameter specifies the port used to expose metrics on the storage node. The
  default is `5025`. You can change it as needed. If you connect to different clusters, use
  different ports to avoid conflicts.
- The `storageRdmaNicFilter` parameter is used to match the RDMA NIC interface names of the
  storage node and supports wildcards. For example, `ens*` matches all interface names starting
  with `ens`. Adjust it according to the actual NIC naming rules of the storage node.

Create the Docker Compose file `/etc/unifabric/cluster1-agent-compose.yaml`:

```shell
cat <<'EOF' | sudo tee /etc/unifabric/cluster1-agent-compose.yaml > /dev/null
services:
  unifabric-agent:
    image: ${UNIFABRIC_AGENT_IMAGE}
    container_name: unifabric-agent
    network_mode: host
    restart: always
    privileged: true
    volumes:
      - /etc/unifabric/cluster1-kubeconfig.yaml:/root/.kube/config
      - /etc/unifabric/cluster1-agent-config.yaml:/etc/config/config.yaml
      - /var/run:/var/run
      - /etc/hostname:/etc/hostname:ro
      - /proc:/host/proc:ro
    command:
      - /usr/bin/unifabric/agent
      - -config
      - /etc/config/config.yaml
EOF


UNIFABRIC_AGENT_IMAGE="release.daocloud.io/unifabric/unifabric-agent:latest" \
  sudo -E docker compose -f /etc/unifabric/cluster1-agent-compose.yaml up -d
```

- Remember to replace `UNIFABRIC_AGENT_TAG` with the image version that matches the Kubernetes
  cluster. Different clusters may require different versions of the Agent image.
- If you need to connect to multiple clusters, copy this file and modify the service name and
  configuration file path, for example to `cluster1-agent-compose.yaml`, and use the
  corresponding kubeconfig and configuration file.

## Configure Storage Node Metrics Scraping in the Cluster

On the control node of the Kubernetes cluster, generate the storage node metrics scraping
configuration file `unifabric-metrics-external.yaml`:

```shell
# Set the list of storage node IPs, comma-separated
export STORAGE_NODE_IPS="1.1.1.1,2.2.2.2"
# Set the metrics port of the storage node RDMA Agent
export AGENT_PORT_METRICS="5025"
# Set the metrics port of the storage node RDMA latency
export RDMA_LATENCY_PORT_METRICS="5027"

# Generate the configuration file content
cat > unifabric-metrics-external.yaml << EOF
apiVersion: v1
kind: Service
metadata:
  name: unifabric-metrics-external
  namespace: unifabric
  labels:
    app: unifabric-metrics-external
spec:
  clusterIP: None
  ports:
    - name: metrics-agent
      port: ${AGENT_PORT_METRICS}
      targetPort: ${AGENT_PORT_METRICS}
    - name: metrics-rdma-latency-cluster1
      port: ${RDMA_LATENCY_PORT_METRICS}
      targetPort: ${RDMA_LATENCY_PORT_METRICS}
---
apiVersion: v1
kind: Endpoints
metadata:
  name: unifabric-metrics-external
  namespace: unifabric
subsets:
  - addresses:
$(IFS=',' read -ra IPS <<< "$STORAGE_NODE_IPS"; for ip in "${IPS[@]}"; do echo "      - ip: $ip"; done)
    ports:
      - name: metrics-agent
        port: ${AGENT_PORT_METRICS}
      - name: metrics-rdma-latency
        port: ${RDMA_LATENCY_PORT_METRICS}
---
apiVersion: monitoring.coreos.com/v1
kind: ServiceMonitor
metadata:
  name: unifabric-metrics-external
  namespace: unifabric
  labels:
    operator.insight.io/managed-by: insight
    release: kube-prometheus-stack
spec:
  selector:
    matchLabels:
      app: unifabric-metrics-external
  namespaceSelector:
    matchNames:
      - unifabric
  endpoints:
    - port: metrics-agent
      interval: 30s
      path: /metrics
    - port: metrics-rdma-latency
      interval: 30s
      path: /metrics
EOF
```

Deploy the configuration file:

```shell
kubectl apply -f unifabric-metrics-external.yaml
```

## Verify the Storage Node Access Status

1. Run the following command to see the newly connected node:

    ```shell
    kubectl get fabricnode
    ```

    Then check the fabricnode YAML information of the storage node to confirm that the RDMA NIC
    and LLDP neighbor information have been collected:

    ```yaml
    apiVersion: unifabric.io/v1beta1
    kind: FabricNode
    metadata:
      name: l-oss-2
    status:
      rdmaHealthy: true
      scaleUp:
        scaleUpHealthy: false
      storageNics:
        - ipv4: 172.16.1.41/24
          ipv6: ""
          lldpNeighbor:
            description:
              "SONiC Software Version: SONiC.CuOS_4.0-0.R_X86_64_ztp - HwSku:
              ds730-32d - Distribution: 10.13 - Kernel: 4.19.0-12-2-amd64"
            hostname: StorageSW
            mac: 70:06:92:6e:32:64
            mgmtIP: 10.193.77.211
            port: Ethernet200
          name: ens2np0
          rdma: true
          state: up
        - ipv4: ""
          ipv6: ""
          lldpNeighbor:
            description:
              "SONiC Software Version: SONiC.CuOS_4.0-0.R_X86_64_ztp - HwSku:
              ds730-32d - Distribution: 10.13 - Kernel: 4.19.0-12-2-amd64"
            hostname: StorageSW
            mac: 70:06:92:6e:32:64
            mgmtIP: 10.193.77.211
            port: Ethernet192
          name: ens1np0
          rdma: true
          state: up
    ```

2. Check the lldp neighbor information on the switch to confirm that the storage node is
   broadcasting through LLDP:

    ```shell
    lldpcli show neighbors
    ```

3. Check the metrics data of the storage node:

    ```shell
    curl http://localhost:5025/metrics
    ```

4. On the Grafana of kube-prometheus-stack, view the monitoring dashboards related to storage
   nodes and make sure that the metrics data of storage nodes can be viewed.

## Connect to Multiple Clusters

If you need to connect a storage node to multiple Kubernetes clusters, you can create a separate
kubeconfig and agent configuration file for each cluster, and then create the corresponding
Docker Compose files to start multiple unifabric agent instances.
For example, you can create `cluster2-kubeconfig.yaml`, `cluster2-agent-config.yaml`, and
`cluster2-agent-compose.yaml`, and use different metrics ports to avoid conflicts.

## Uninstall the Storage Node Agent

Run the following commands to uninstall the unifabric services on the storage node:

```shell
# Uninstall the unifabric agent service
# If multiple clusters are connected, uninstall the corresponding agent service separately, for example cluster2-agent-compose.yaml
docker compose down -f /etc/unifabric/cluster1-agent-compose.yaml

# If you need to uninstall the lldp service, run:
docker compose down -f /etc/unifabric/lldp.yaml

# If you need to delete all configuration files, run:
sudo rm -rf /etc/unifabric
```

## Troubleshooting

If the storage node is not connected properly, check the Agent logs for troubleshooting:

```shell
docker compose logs -f /etc/unifabric/cluster1-agent-compose.yaml
docker compose logs -f /etc/unifabric/lldp.yaml
```

If the logs indicate that the Kubernetes cluster cannot be connected, check whether the content of
the `/etc/unifabric/cluster1-kubeconfig.yaml` file is correct.
You can use the kubectl command to test the connection:

```shell
KUBECONFIG=/etc/unifabric/cluster1-kubeconfig.yaml kubectl get pods
```

If there is no metrics data, check the firewall settings of the storage node and make sure that
port 5025 is open.
Also test metrics scraping with curl:

```shell
curl http://localhost:5025/metrics
```
