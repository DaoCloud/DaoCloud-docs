# Co-located Workloads

Enterprises generally have two types of workloads: latency-sensitive services and batch jobs.
Latency-sensitive services, such as search, payment, and recommendation, are characterized by high processing priority, high latency sensitivity, low error tolerance, and high load during the day but low load at night.
Batch jobs, such as AI training and big data processing, are characterized by low processing priority, low latency sensitivity, high error tolerance, and consistently high runtime load.
Because these two types of workloads are naturally complementary, mixed deployment of online and offline workloads is an effective way to improve server resource utilization.

* You can co-locate offline workloads onto the servers running online services, so that offline workloads can make full use of the idle resources of those servers, improving the resource utilization of the online service servers and reducing costs while increasing efficiency.

* When a service temporarily requires a large amount of resources, you can elastically co-locate online services onto the servers running offline workloads, prioritizing the resource requirements of the online services and returning the resources to the offline workloads after the temporary demand ends.

Currently, the open-source project [Koordinator](https://koordinator.sh) is used as the co-location solution.

Koordinator is a QoS-based Kubernetes mixed-workload scheduling system.
It aims to improve the runtime efficiency and reliability of latency-sensitive workloads and batch jobs, simplify the complexity of resource-related configuration tuning, and increase Pod deployment density to improve resource utilization.

## Koordinator QoS

The Koordinator scheduling system supports five types of QoS:

| QoS                              | Features                                 | Description |
|----------------------------------|------------------------------------| -------------|
| SYSTEM                           | System processes, with limited resources                          | For system services such as DaemonSets, although the latency of system services needs to be guaranteed, the resource usage of these system service containers on nodes also needs to be limited to ensure that they do not occupy excessive resources. |
| LSE (Latency Sensitive Exclusive) | Reserves resources and prevents Pods of the same QoS from sharing resources            | Rarely used. Common in middleware-type applications, usually in a dedicated resource pool. |
| LSR (Latency Sensitive Reserved)  | Reserves resources for better determinism                      | Similar to the community Guaranteed, where CPU cores are bound. |
| LS (Latency Sensitive)            | Shares resources and provides better elasticity for burst traffic                   | The typical QoS level for microservice workloads, providing better resource elasticity and more flexible resource tuning capabilities. |
| BE (Best Effort)                  | Shares resources excluding LSE resources; the runtime quality of resources is limited and, in extreme cases, Pods can be killed | The typical QoS level for batch jobs, providing stable compute throughput over a period of time with low-cost resources. |

### Koordinator QoS CPU Orchestration Principles

- The Request and Limit of LSE/LSR Pods must be equal, and the CPU value must be an integer multiple of 1000.
- The CPUs allocated to LSE Pods are fully exclusive and must not be shared. If the node uses a hyper-threading architecture, only the logical core dimension is guaranteed to be isolated, but better isolation can be achieved with the CPUBindPolicyFullPCPUs policy.
- The CPUs allocated to LSR Pods can only be shared with BE Pods.
- LS Pods are bound to a shared CPU pool other than the CPUs exclusive to LSE/LSR Pods.
- BE Pods are bound to all CPUs on the node except those exclusive to LSE Pods.
- If the kubelet CPU manager policy is static, the already running K8s Guaranteed Pods are equivalent to Koordinator LSR.
- If the kubelet CPU manager policy is none, the already running K8s Guaranteed Pods are equivalent to Koordinator LS.
- Newly created K8s Guaranteed Pods without a specified Koordinator QoS are equivalent to Koordinator LS.

![koordinator_qos_cpu.png](../images/koordinator_qos_cpu.png)

## Quick Start

### Prerequisites

- The DCE container management platform has been deployed and is running properly.
- The container management module has been integrated with a Kubernetes cluster or a Kubernetes cluster has been created, and the cluster UI can be accessed.
- Koordinator has been installed on the current cluster and is running properly. For installation steps, refer to [Koordinator Offline Installation](./install.md).

### Procedure

In the following example, four Deployments with 1 replica each are created, with the QoS classes set to LSE, LSR, LS, and BE. After the Pods are created, observe the CPU allocation of each Pod.

1. Create a Deployment named nginx-lse with the QoS class set to LSE. The YAML file is as follows.

    ```yaml
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: nginx-lse
      labels:
        app: nginx-lse
    spec:
      replicas: 1
      selector:
        matchLabels:
          app: nginx-lse
      template:
        metadata:
          name: nginx-lse
          labels:
            app: nginx-lse
            koordinator.sh/qosClass: LSE # Set the QoS class to LSE
            # The scheduler evenly distributes logical CPUs across physical cores
          annotations:
              scheduling.koordinator.sh/resource-spec: '{"preferredCPUBindPolicy": "SpreadByPCPUs"}'
        spec:
          schedulerName: koord-scheduler # Use the koord-scheduler
          containers:
          - name: nginx
            image: release.daocloud.io/kpanda/nginx:1.25.3-alpine
            resources:
              limits:
                cpu: '2'
              requests:
                cpu: '2'
          priorityClassName: koord-prod

    ```

2. Create a Deployment named nginx-lsr with the QoS class set to LSR. The YAML file is as follows.

    ```yaml
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: nginx-lsr
      labels:
        app: nginx-lsr
    spec:
      replicas: 1
      selector:
        matchLabels:
          app: nginx-lsr
      template:
        metadata:
          name: nginx-lsr
          labels:
            app: nginx-lsr
            koordinator.sh/qosClass: LSR # Set the QoS class to LSR
            # The scheduler evenly distributes logical CPUs across physical cores
          annotations:
              scheduling.koordinator.sh/resource-spec: '{"preferredCPUBindPolicy": "SpreadByPCPUs"}'
        spec:
          schedulerName: koord-scheduler # Use the koord-scheduler
          containers:
          - name: nginx
            image: release.daocloud.io/kpanda/nginx:1.25.3-alpine
            resources:
              limits:
                cpu: '2'
              requests:
                cpu: '2'
          priorityClassName: koord-prod
    ```

3. Create a Deployment named nginx-ls with the QoS class set to LS. The YAML file is as follows.

    ```yaml
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: nginx-ls
      labels:
        app: nginx-ls
    spec:
      replicas: 1
      selector:
        matchLabels:
          app: nginx-ls
      template:
        metadata:
          name: nginx-ls
          labels:
            app: nginx-ls
            koordinator.sh/qosClass: LS # Set the QoS class to LS
            # The scheduler evenly distributes logical CPUs across physical cores
          annotations:
              scheduling.koordinator.sh/resource-spec: '{"preferredCPUBindPolicy": "SpreadByPCPUs"}'
        spec:
          schedulerName: koord-scheduler 
          containers:
          - name: nginx
            image: release.daocloud.io/kpanda/nginx:1.25.3-alpine
            resources:
              limits:
                cpu: '2'
              requests:
                cpu: '2'
          priorityClassName: koord-prod
    ```

4. Create a Deployment named nginx-be with the QoS class set to BE. The YAML file is as follows.

    ```yaml
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: nginx-be
      labels:
        app: nginx-be
    spec:
      replicas: 1
      selector:
        matchLabels:
          app: nginx-be
      template:
        metadata:
          name: nginx-be
          labels:
            app: nginx-be
            koordinator.sh/qosClass: BE # Set the QoS class to BE
            # The scheduler evenly distributes logical CPUs across physical cores
          annotations:
              scheduling.koordinator.sh/resource-spec: '{"preferredCPUBindPolicy": "SpreadByPCPUs"}'
        spec:
          schedulerName: koord-scheduler # Use the koord-scheduler
          containers:
          - name: nginx
            image: release.daocloud.io/kpanda/nginx:1.25.3-alpine
            resources:
              limits:
                kubernetes.io/batch-cpu: 2k
              requests:
                kubernetes.io/batch-cpu: 2k
          priorityClassName: koord-batch
    ```

    Check the Pod status. After the Pods are in the Running state, check the CPU allocation of each Pod.

    ```shell
    [root@controller-node-1 ~]# kubectl get pod
    NAME                         READY   STATUS    RESTARTS   AGE
    nginx-be-577c946b89-js2qn    1/1     Running   0          4h41m
    nginx-ls-54746c8cf8-rh4b7    1/1     Running   0          4h51m
    nginx-lse-56c9cd77f5-cdqbd   1/1     Running   0          4h41m
    nginx-lsr-c7fdb97d8-b58h8    1/1     Running   0          4h51m
    ```

    In this example, the get_cpuset.sh script is used to view the cpuset information of the Pods. The script content is as follows.

    ```shell
    #!/bin/bash
    
    # Take the Pod name and namespace as input parameters
    POD_NAME=$1
    NAMESPACE=${2-default}
    
    # Ensure that the Pod name and namespace are provided
    if [ -z "$POD_NAME" ] || [ -z "$NAMESPACE" ]; then
        echo "Usage: $0 <pod_name> <namespace>"
        exit 1
    fi
    
    # Use kubectl to get the UID and QoS class of the Pod
    POD_INFO=$(kubectl get pod "$POD_NAME" -n "$NAMESPACE" -o jsonpath="{.metadata.uid} {.status.qosClass} {.status.containerStatuses[0].containerID}")
    read -r POD_UID POD_QOS CONTAINER_ID <<< "$POD_INFO"
    
    # Check whether the UID and QoS class were obtained successfully
    if [ -z "$POD_UID" ] || [ -z "$POD_QOS" ]; then
        echo "Failed to get UID or QoS Class for Pod $POD_NAME in namespace $NAMESPACE."
        exit 1
    fi
    
    POD_UID="${POD_UID//-/_}"
    CONTAINER_ID="${CONTAINER_ID//containerd:\/\//cri-containerd-}".scope
    
    # Build the cgroup path based on the QoS class
    case "$POD_QOS" in
        Guaranteed)
            QOS_PATH="kubepods-pod.slice/$POD_UID.slice"
            ;;
        Burstable)
            QOS_PATH="kubepods-burstable.slice/kubepods-burstable-pod$POD_UID.slice"
            ;;
        BestEffort)
            QOS_PATH="kubepods-besteffort.slice/kubepods-besteffort-pod$POD_UID.slice"
            ;;
        *)
            echo "Unknown QoS Class: $POD_QOS"
            exit 1
            ;;
    esac
    
    CPUGROUP_PATH="/sys/fs/cgroup/kubepods.slice/$QOS_PATH"
    
    # Check whether the path exists
    if [ ! -d "$CPUGROUP_PATH" ]; then
        echo "CPUs cgroup path for Pod $POD_NAME does not exist: $CPUGROUP_PATH"
        exit 1
    fi
    
    # Read and print the cpuset value
    CPUSET=$(cat "$CPUGROUP_PATH/$CONTAINER_ID/cpuset.cpus")
    echo "CPU set for Pod $POD_NAME ($POD_QOS QoS): $CPUSET"
    ```

Check the cpuset allocation of each Pod.

1. A Pod with the LSE QoS class exclusively occupies cores 0-1 and does not share CPUs with Pods of other QoS classes.

    ```shell
    [root@controller-node-1 ~]# ./get_cpuset.sh nginx-lse-56c9cd77f5-cdqbd
    CPU set for Pod nginx-lse-56c9cd77f5-cdqbd (Burstable QoS): 0-1
    ```
    
2. A Pod with the LSR QoS class is bound to cores 2-3 and can share them with BE Pods.

    ```shell
    [root@controller-node-1 ~]# ./get_cpuset.sh nginx-lsr-c7fdb97d8-b58h8
    CPU set for Pod nginx-lsr-c7fdb97d8-b58h8 (Burstable QoS): 2-3
    ```

3. A Pod with the LS QoS class uses cores 4-15 and is bound to the shared CPU pool other than the CPUs exclusive to LSE/LSR Pods.

    ```shell
    [root@controller-node-1 ~]# ./get_cpuset.sh nginx-ls-54746c8cf8-rh4b7
    CPU set for Pod nginx-ls-54746c8cf8-rh4b7 (Burstable QoS): 4-15
    ```

4. A Pod with the BE QoS class can use the CPUs other than those exclusive to LSE Pods.

    ```shell
    [root@controller-node-1 ~]# ./get_cpuset.sh nginx-be-577c946b89-js2qn
    CPU set for Pod nginx-be-577c946b89-js2qn (BestEffort QoS): 2,4-12
    ```
