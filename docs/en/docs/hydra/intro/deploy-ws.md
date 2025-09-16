# Deploying the LLM Studio(WS Mode)

*[Hydra]: Codename for the LLM Studio 
*[Mspider]: Codename for the service mesh

This document explains how to deploy the privatized WS (Workspace) mode of the LLM StudioHydra, which supports inference without GPUs.

## Global Service Cluster

In the [Global Service Cluster](../../kpanda/user-guide/clusters/cluster-role.md#_2), you need to install:

- Hydra: manually install or install via the installer
- [Service Mesh](../../mspider/install/install.md) (depends on Istio to create gateways for routing)
- [MySQL](../../middleware/mysql/intro/offline-install.md)
- [Redis](../../middleware/redis/intro/offline-install.md)

!!! tip

    - The Global Service Cluster installs a common MySQL and Redis by default.
    - If Hydra is installed via the installer, it will use the common MySQL and Redis by default.
    - If Hydra is installed manually, you need to specify MySQL and Redis in the installation parameters.

The installed result is as shown below:

<!-- ![Install Hydra and mspider](./images/deploy01.png) -->

## Worker Cluster

The worker cluster needs Hydra Agent and metallb installed.

### Install Hydra Agent

1. Create a worker cluster to deploy Hydra Agent (if resources are limited, you can also directly use the Global Service Cluster)

    <!-- ![Install Hydra Agent](./images/deploy02.png) -->

2. Deploy Hydra Agent in the worker cluster

    Pay attention to the following parameters:

    ```yaml
    global:
      config:
        cluster_name: 'jxj31-mspider'
        agent_base_url: 'http:/cn-sh-a1' # Gateway address accessible by the worker cluster
        agent_server:
          address: example.com:443 # DCE address of the Global Service Cluster
          plaintext: false
          insecure: true # For test environments, you can set this to true to bypass certificates
    ```


3. Deploy metallb in the worker cluster (used for routing access to the model) and allocate a LoadBalancer


### Create Service Mesh (Istio + Gateway API)

1. Create a dedicated mesh in the worker cluster (use default parameters when creating the mesh)

    Note: Managed meshes currently do not support gateway API.


1. Initialize Gateway API CRD

    ```shell
    root@controller-node-1:~# kubectl kustomize "github.com/kubernetes-sigs/gateway-api/config/crd?ref=v1.2.1" | kubectl apply -f -;

    customresourcedefinition.apiextensions.k8s.io/gatewayclasses.gateway.networking.k8s.io created
    customresourcedefinition.apiextensions.k8s.io/gateways.gateway.networking.k8s.io created
    customresourcedefinition.apiextensions.k8s.io/grpcroutes.gateway.networking.k8s.io created
    customresourcedefinition.apiextensions.k8s.io/httproutes.gateway.networking.k8s.io created
    customresourcedefinition.apiextensions.k8s.io/referencegrants.gateway.networking.k8s.io created
    ```

1. Create the gateway and routing rules

    ```shell
    root@controller-node-1:~# cat gateway.yaml
    ```
    ```yaml
    apiVersion: gateway.networking.k8s.io/v1
    kind: Gateway
    metadata:
      name: gateway
      namespace: default 
    spec:
      gatewayClassName: istio
      listeners:
      - allowedRoutes:
          namespaces:
            from: All
        name: default
        port: 80
        protocol: HTTP
    - allowedRoutes:
          namespaces:
            from: All
        hostname: 'cn-sh-a1'
        name: https
        port: 443
        protocol: HTTPS
        tls:
          certificateRefs:
          - group: ""
            kind: Secret
            name: cn-sh-a1
        mode: Terminate
    ```

    ```shell
    root@controller-node-1:~# kubectl apply -f gateway.yaml

    gateway.gateway.networking.k8s.io/gateway created
    ```

    ```shell
    root@controller-node-1:~# kubectl get po

    NAME                             READY   STATUS    RESTARTS   AGE
    gateway-istio-5c497d4b6d-9xmqp   1/1     Running   0          14s
    root@controller-node-1:~# kubectl  get svc
    NAME            TYPE           CLUSTER-IP     EXTERNAL-IP    PORT(S)                                      AGE
    gateway-istio   LoadBalancer   10.233.1.140   10.64.24.211   15021:32565/TCP,80:32053/TCP,443:32137/TCP   45s
    ```

    ```shell
    root@controller-node-1:~# cat httproute.yaml
    ```
    ```yaml
    apiVersion: gateway.networking.k8s.io/v1
    kind: HTTPRoute
    metadata:
      labels:
        app.kubernetes.io/managed-by: Helm
      name: hydra-agent-knoway
      namespace: hydra-system
    spec:
      parentRefs:
      - group: gateway.networking.k8s.io
        kind: Gateway
        name: gateway
        namespace: default 
      rules:
      - backendRefs:
        - group: ""
          kind: Service
          name: knoway-gateway
          port: 8080
          weight: 1
        filters:
        - responseHeaderModifier:
            add:
            - name: Access-Control-Allow-Headers
              value: '*'
            - name: Access-Control-Allow-Methods
              value: '*'
          type: ResponseHeaderModifier
        matches:
        - path:
            type: PathPrefix
            value: /v1
    ```
    
    ```shell
    root@controller-node-1:~# kubectl apply -f httproute.yaml

    httproute.gateway.networking.k8s.io/hydra-agent-knoway created
    ```

1. Configure domain name resolution, mapping the domain name to the Ingress gateway’s LB. Append the domain mapping to `/etc/hosts` on both the worker cluster and the local computer running the browser:

    ```shell
    echo "10.64.xx.xx cn-sh-a1" | sudo tee -a /etc/hosts
    ```

Set the local computer to trust the certificate:

## Worker Cluster Initialization

Insert vendor data into the database.  
For new versions of Hydra, this step is unnecessary because Hydra can automatically create vendors.

When implementing (only batch upload supported), use the `mcamel-system` workload `mcamel-common-mysql-cluster-mysql`.


Example:

```json
{"enUS": "Alibaba", "zhCN": "通义千问"}
```

### Register Model in Hydra Ops Platform

Configure model deployment parameters (adjust according to actual needs)

### Install nfs drive

The nfs drive is required when downloading model artifacts.

```shell
wget http://example.com/nfs-install.tar # replace with your download URL
tar xvf nfs-install.tar
./install.sh
```

## Worker Cluster Model Warm-up

Model warm-up refers to pre-downloading the model image.

When Hydra and AI Lab both exist, there will be two dataset CRDs.
Note: use `dataset.baizeai.io`.

```shell
root@controller-node-1:~# cat dataset-qwen3-06b.yaml
```

```yaml
apiVersion: dataset.baizeai.io/v1alpha1 # This should belong to the AI Lab group
kind: Dataset
metadata:
  name: qwen3-0.6b
  namespace: public # must be the public namespace
  labels:
    hydra.io/model-id: qwen3-0.6b # must match the model name
spec:
  dataSyncRound: 1
  share: true
  source:
    type: HTTP
    uri: http://example.com:81/model/qwen3-06b/ # replace with your address
    options:
      repoType: MODEL
  mountOptions:
    uid: 1000
    gid: 1000
    mode: "0774"
    path: /
  volumeClaimTemplate:
    spec:
      storageClassName: nfs-csi
```

```shell
root@jxj:~/hydra-deploy# kubectl create ns public

namespace/public created
```

```shell
root@jxj:~/hydra-deploy# kubectl apply -f dataset-qwen3-06b.yaml

dataset.dataset.baizeai.io/qwen3-0.6b created
```

## Try the Model

Try the model in DCE 5.0.

## Model Deployment

If running without GPUs, note:

1. Model deployment without GPU (deployment detects no GPU and fails)

    Therefore, deploy `gpu-operator-fake` (pulling external images requires proxy):

    1. Configure Node

        ```shell
        kubectl label node <node-name> run.ai/simulated-gpu-node-pool=default
        ```

    2. Install fake-gpu-operator

        For offline installation, first download the offline package and deploy:

        For online installation, run:

        ```shell
        helm upgrade -i gpu-operator oci://ghcr.io/run-ai/fake-gpu-operator/fake-gpu-operator --namespace gpu-operator --create-namespace --version=0.0.63
        ```

        After deployment, wait a few minutes, check that the Node has GPU labels, and refresh status to confirm detection passed.


2. After creating a model deployment task, modify deployment parameters:


    ```
    --dtype=half
    --device=cpu
    --max-model-len=8192
    release.daocloud.io/hydra/vllm-openai:0.8.5.dev940-cpu
    ```

3. When using CPU inference, the Qwen3 0.6b model occupies about 7GB memory. CPU allocation determines token speed.

    !!! tip

        For test environment model traffic, route directly through the knoway-gateway.

4. Create a NodePort type svc service for the gateway


5. When accessing DCE, only the HTTP port can be used

