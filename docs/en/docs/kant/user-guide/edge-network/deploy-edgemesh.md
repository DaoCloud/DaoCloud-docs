# Deploy EdgeMesh

Before using the application mesh capabilities, you need to deploy EdgeMesh.
This page describes the specific workflow.

## Prerequisites

1. Remove the taint from the K8s master node

    If there are running business applications on the K8s master node that need to access other applications on the cluster nodes, you need to remove the taint from the K8s master node by executing the following command.

    ```shell
    kubectl taint nodes --all node-role.kubernetes.io/master-
    ```

    !!! note
    
        If no applications that need to be proxied on the K8s master node,
        you can skip this step.

2. Add filtering labels to the Kubernetes API service

    Normally, to prevent EdgeMesh from proxying the Kubernetes API service, you need to add filtering labels to it. For more information, please refer to [Service Filtering](https://edgemesh.netlify.app/en/advanced/hybrid-proxy.html#service-filtering).

    ```shell
    kubectl label services kubernetes service.edgemesh.kubeedge.io/service-proxy-name=""
    ```

## Install via Helm

The steps are as follows:

1. Select `Containers` -> `Container Management` in the left navigation bar to enter the cluster list page, and click the `Cluster Name` to enter the cluster details page.

2. Select `Helm Apps` -> `Helm Charts` in the left menu, and find the EdgeMesh plugin under the `addon repository`.

3. Click the `edgemesh` entry to enter the template details page.

4. Select the EdgeMesh version in the upper right corner of the page,
   and click the `Install` button to enter the EdgeMesh installation page.

5. Fill in the basic configuration for edgemesh.

    - Name: Consists of lowercase letters, numeric characters, or `-`, and must start with a letter and end with a letter or numeric character.
    - Namespace: The namespace where the EdgeMesh application is located. If the namespace has not been created, you can choose to `Create New Namespace`.
    - Version: Select the desired EdgeMesh version based on actual business needs.
    - On Failure Delete: When enabled, it will synchronize the installation and wait for it to be installed. It will delete the installation when the installation fails.
    - Ready Wait: When enabled, it will wait for all associated resources of the application to be ready before marking the application installation as successful.
    - Verbose Log: Enable detailed output of the installation process log.

6. YAML parameter configuration.

!!! note

    With the default YAML configuration, you need to supplement the authentication password (PSK)
    and relay node information, otherwise the deployment will fail.

**PSK and Relay Node Configuration**

```yaml
  # PSK: is an authentication password that ensures that each edgemesh-agent can only establish a connection if it has the same "PSK password". For more information, please refer to
  # [PSK](https://edgemesh.netlify.app/en/guide/security.html). It is recommended to generate it using openssl, or it can be set to a custom random string.
  psk: Juis9HP1XBouyO5pWGeZa8LtipDURrf17EJvUHcJGuQ=

  # Relay Node: is a node that forwards packets in network communication. It acts as a bridge between the source node and the destination node in communication,
  # helping packets to be transmitted in the network and bypassing certain restrictions or obstacles. In EdgeMesh, it is usually a cloud node, and multiple relay nodes can be added.

  relayNodes:
  - nodeName: masternode
    advertiseAddress:
    - 10.31.223.12
 # - nodeName: <your relay node name2>
 #   advertiseAddress:
 #   - 2.2.2.2
 #   - 3.3.3.3
```

**Here is an example:**

```yaml
agent:
  image: kubeedge/edgemesh-agent:v1.14.0
  affinity: {}
  nodeSelector: {}
  tolerations: []
  resources:
    limits:
      cpu: 1
      memory: 256Mi
    requests:
      cpu: 0.5
      memory: 128Mi

  psk: Juis9HP1XBouyO5pWGeZa8LtipDURrf17EJvUHcJGuQ=

  relayNodes:
  - nodeName: masternode
    advertiseAddress:
    - 10.31.223.12

  modules:
    edgeProxy:
      enable: true
    edgeTunnel:
      enable: true
```

## Verify the Deployment Result

After the deployment is complete, you can run the following command to check if the EdgeMesh is successfully deployed.

```shell
$ helm ls -A
NAME            NAMESPACE       REVISION        UPDATED                                 STATUS          CHART           APP VERSION
edgemesh        kubeedge        1               2022-09-18 12:21:47.097801805 +0800 CST deployed        edgemesh-0.1.0  latest

$ kubectl get all -n kubeedge -o wide
NAME                       READY   STATUS    RESTARTS   AGE   IP              NODE         NOMINATED NODE   READINESS GATES
pod/edgemesh-agent-7gf7g   1/1     Running   0          39s   192.168.0.71    k8s-node1    <none>           <none>
pod/edgemesh-agent-fwf86   1/1     Running   0          39s   192.168.0.229   k8s-master   <none>           <none>
pod/edgemesh-agent-twm6m   1/1     Running   0          39s   192.168.5.121   ke-edge2     <none>           <none>
pod/edgemesh-agent-xwxlp   1/1     Running   0          39s   192.168.5.187   ke-edge1     <none>           <none>

NAME                            DESIRED   CURRENT   READY   UP-TO-DATE   AVAILABLE   NODE SELECTOR   AGE   CONTAINERS       IMAGES                           SELECTOR
daemonset.apps/edgemesh-agent   4         4         4       4            4           <none>          39s   edgemesh-agent   kubeedge/edgemesh-agent:latest   k8s-app=kubeedge,kubeedge=edgemesh-agent
```

Next: [Create Services](service.md)
