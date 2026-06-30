# Kubean Cluster Integration with Karpenter for AWS Elastic Nodes (Preview, Including GPU)

## 1. Solution Positioning

The boundary of this solution is very clear: Kubean manages the **cluster lifecycle**, while Karpenter manages **elastic worker capacity in AWS**. Karpenter does **not** manage the control plane or etcd, nor does it replace Kubean for cluster upgrades, scaling, or day-to-day operations.

**Kubean is responsible for**

- Creating the control plane, etcd, and infra workers
- Maintaining the Kubernetes version, Kubespray configuration, and core components
- Providing stable infrastructure nodes to host the Karpenter controller

**Karpenter is responsible for**

- Provisioning AWS EC2 worker nodes based on pending Pods
- Managing CPU/GPU elastic node pools through EC2NodeClass and NodePool
- Automatically reclaiming idle, drifted, or underutilized nodes

| Component | Responsibilities |
| --- | ---- |
| **Kubean** | - Create the control plane, etcd, and infra workers<br>- Maintain the Kubernetes version, Kubespray configuration, and core components<br>- Provide stable infrastructure nodes to host the Karpenter controller |
| **Karpenter** | - Provision AWS EC2 worker nodes based on pending Pods<br>- Manage CPU/GPU elastic node pools through `EC2NodeClass` and `NodePool`<br>- Automatically reclaim idle, drifted, or underutilized nodes |

![](./images/archi.png)

## 2. Feasibility and Key Constraints

| Dimension | Feasibility | Deployment Requirements |
| :-- | :------- | :------ |
| Control Plane | Supported. Karpenter can use a custom Kubernetes API Server endpoint. | Configure `clusterEndpoint`, `clusterCABundle`, and `eksControlPlane=false`. |
| Node Bootstrap | Supported, but not through the EKS automatic bootstrap process. | Use `amiFamily: Custom` and perform `kubeadm join` (or an equivalent bootstrap process) in `userData`. |
| AWS Cloud Integration | Supported. | Install AWS Cloud Controller Manager, and configure the kubelet with `cloud-provider=external`. |
| GPU | Supported. | The GPU AMI should include the NVIDIA driver and container runtime, and the cluster should install the NVIDIA device plugin. |
| Production Boundary | Separation of responsibilities is recommended. | Kubean manages only fixed nodes, while Karpenter manages only elastic worker nodes. |

**Risk Notice:**
Do not allow Karpenter to manage the control plane, etcd, or the infra workers hosting the Karpenter controller. Otherwise, automatic node reclamation, drift handling, or configuration errors could compromise the cluster's self-healing capabilities.

## 3. Credentials and Placeholder Reference

| Category | Placeholder | Description |
| :--- | :--- | :--- |
| Kubean SSH | `<KUBEAN_NODE_SSH_USER>`, `<KUBEAN_NODE_SSH_PRIVATE_KEY>`, `<KUBEAN_NODE_SSH_PORT>` | Credentials used by Kubean/Kubespray to access the infrastructure nodes. |
| Kubernetes Bootstrap | `<KUBE_APISERVER_DNS_NAME>`, `<BASE64_CLUSTER_CA_BUNDLE>`, `<KUBEADM_BOOTSTRAP_TOKEN>`, `<KUBEADM_CA_CERT_HASH>` | Used for newly provisioned EC2 nodes to join the self-managed Kubernetes cluster. |
| AWS Controller | `<AWS_REGION>`, `<AWS_ACCESS_KEY_ID_FOR_KARPENTER_CONTROLLER>`, `<AWS_SECRET_ACCESS_KEY_FOR_KARPENTER_CONTROLLER>` | Static credentials used only when an Instance Profile cannot be used. |
| AWS Node Identity | `<KARPENTER_NODE_IAM_ROLE_NAME>`, `<KARPENTER_NODE_INSTANCE_PROFILE_NAME>` | IAM identity assigned to worker nodes provisioned by Karpenter. |
| AWS Networking | `<AWS_VPC_ID>`, `<AWS_PRIVATE_SUBNET_ID_A>`, `<KARPENTER_NODE_SECURITY_GROUP_ID>`, `<CONTROL_PLANE_SECURITY_GROUP_ID>` | Defines where EC2 instances are placed and how they connect to the Kubernetes API Server. |
| AMI | `<KARPENTER_CPU_WORKER_AMI_ID>`, `<KARPENTER_GPU_WORKER_AMI_ID>` | Separate AMIs are recommended for CPU and GPU worker nodes. |
| GPU | `<NVIDIA_DRIVER_VERSION>`, `<CUDA_VERSION>`, `<NVIDIA_DEVICE_PLUGIN_VERSION>` | Versions of the GPU image components and the NVIDIA device plugin. |

!!! note

    In production environments, prioritize using EC2 Instance Profiles, AWS Systems Manager Parameter Store, or AWS Secrets Manager instead of embedding long-lived AWS access keys or kubeadm bootstrap tokens directly in manifests.

## 4. Deployment Workflow

![Deployment Workflow](./images/flow.png)

1. Use Kubean to create the control plane, etcd, and infra worker nodes.
2. Install and verify the CNI plugin, AWS Cloud Controller Manager, and the EBS CSI Driver.
3. Prepare the required AWS IAM role, Instance Profile, and subnet/security group discovery tags.
4. Create a kubeadm bootstrap token, or store the bootstrap configuration in AWS Systems Manager Parameter Store or AWS Secrets Manager.
5. Install Karpenter and configure the custom control plane endpoint and CA bundle.
6. Create the CPU EC2NodeClass and NodePool.
7. Create the GPU EC2NodeClass and NodePool, and install the NVIDIA device plugin.
8. Verify CPU and GPU elastic scaling using a standard workload and a CUDA sample workload, respectively.

## 5. Karpenter Installation Configuration

```yaml
settings:
  clusterName: &lt;CLUSTER_NAME&gt;
  clusterEndpoint: https://&lt;KUBE_APISERVER_DNS_NAME&gt;:6443
  clusterCABundle: &lt;BASE64_CLUSTER_CA_BUNDLE&gt;
  eksControlPlane: false
  isolatedVPC: false
  interruptionQueue: &lt;KARPENTER_INTERRUPTION_QUEUE_NAME_OR_EMPTY&gt;

controller:
  env:
    - name: AWS_REGION
      value: <AWS_REGION>
    - name: AWS_ACCESS_KEY_ID
      valueFrom:
        secretKeyRef:
          name: karpenter-aws-credentials
          key: AWS_ACCESS_KEY_ID
    - name: AWS_SECRET_ACCESS_KEY
      valueFrom:
        secretKeyRef:
          name: karpenter-aws-credentials
          key: AWS_SECRET_ACCESS_KEY

nodeSelector:
  node-role.kubernetes.io/infra: ""

tolerations:
  - key: CriticalAddonsOnly
    operator: Exists
```

**Recommendation:**
If the infra workers are running on AWS EC2, grant permissions to the Karpenter controller through the infra workers' Instance Profile whenever possible, rather than injecting static AWS access keys (AK/SK).

## 6. CPU Elastic Node Pool

```yaml
apiVersion: karpenter.k8s.aws/v1
kind: EC2NodeClass
metadata:
  name: kubean-aws-cpu
spec:
  amiFamily: Custom
  amiSelectorTerms:
    - id: &lt;KARPENTER_CPU_WORKER_AMI_ID&gt;
  subnetSelectorTerms:
    - tags:
        karpenter.sh/discovery: &lt;CLUSTER_NAME&gt;
  securityGroupSelectorTerms:
    - tags:
        karpenter.sh/discovery: &lt;CLUSTER_NAME&gt;
  role: &lt;KARPENTER_NODE_IAM_ROLE_NAME&gt;
  userData: |
    #!/bin/bash
    set -euxo pipefail
    INSTANCE_ID="$(curl -s http://169.254.169.254/latest/meta-data/instance-id)"
    AWS_AZ="$(curl -s http://169.254.169.254/latest/meta-data/placement/availability-zone)"
    PROVIDER_ID="aws:///${AWS_AZ}/${INSTANCE_ID}"
    mkdir -p /etc/systemd/system/kubelet.service.d
    cat &gt;/etc/systemd/system/kubelet.service.d/20-karpenter.conf &lt;&lt;EOF
    [Service]
    Environment="KUBELET_EXTRA_ARGS=--cloud-provider=external --provider-id=${PROVIDER_ID} --register-with-taints=karpenter.sh/unregistered:NoExecute --node-labels=node.lifecycle=karpenter"
    EOF
    systemctl daemon-reload
    systemctl enable containerd
    systemctl start containerd
    kubeadm join https://&lt;KUBE_APISERVER_DNS_NAME&gt;:6443 \
      --token &lt;KUBEADM_BOOTSTRAP_TOKEN&gt; \
      --discovery-token-ca-cert-hash sha256:&lt;KUBEADM_CA_CERT_HASH&gt; \
      --node-name "${INSTANCE_ID}"
    systemctl restart kubelet

---
apiVersion: karpenter.sh/v1
kind: NodePool
metadata:
  name: workload-general
spec:
  template:
    metadata:
      labels:
        node.lifecycle: karpenter
        workload-tier: general
    spec:
      nodeClassRef:
        group: karpenter.k8s.aws
        kind: EC2NodeClass
        name: kubean-aws-cpu
      requirements:
        - key: kubernetes.io/arch
          operator: In
          values: ["amd64"]
        - key: karpenter.sh/capacity-type
          operator: In
          values: ["spot", "on-demand"]
        - key: node.kubernetes.io/instance-type
          operator: In
          values: ["m6i.large", "m6i.xlarge", "m7i.large", "m7i.xlarge"]
  limits:
    cpu: "500"
    memory: 1000Gi
  disruption:
    consolidationPolicy: WhenEmptyOrUnderutilized
    consolidateAfter: 5m
```

## 7. GPU Elastic Node Pool

It is recommended to completely separate GPU nodes from CPU nodes by using dedicated AMIs, EC2NodeClasses, NodePools, and taints. This prevents general-purpose Pods from consuming the CPU and memory resources of expensive GPU nodes.

| Workload | Recommended Instance Types | Scheduling Strategy |
| :-- | :------ | :------ |
| Inference / Video Processing | g6.xlarge, g6.2xlarge, g6.4xlarge, g6.8xlarge | Consider a mix of Spot and On-Demand instances. |
| Small to Medium Training / A10G Workloads | g5.xlarge, g5.12xlarge, g5.24xlarge, g5.48xlarge | Start with On-Demand instances, then introduce Spot instances once the workload is mature. |
| Large Language Model Training | p4d, p5, p5e, etc. | Use a dedicated NodePool combined with job queues, checkpointing, and capacity reservations. |

```yaml
apiVersion: karpenter.k8s.aws/v1
kind: EC2NodeClass
metadata:
  name: kubean-aws-gpu
spec:
  amiFamily: Custom
  amiSelectorTerms:
    - id: &lt;KARPENTER_GPU_WORKER_AMI_ID&gt;
  subnetSelectorTerms:
    - tags:
        karpenter.sh/discovery: &lt;CLUSTER_NAME&gt;
  securityGroupSelectorTerms:
    - tags:
        karpenter.sh/discovery: &lt;CLUSTER_NAME&gt;
  role: &lt;KARPENTER_NODE_IAM_ROLE_NAME&gt;
  blockDeviceMappings:
    - deviceName: /dev/xvda
      ebs:
        volumeSize: 200Gi
        volumeType: gp3
        encrypted: true
        deleteOnTermination: true
  userData: |
    #!/bin/bash
    set -euxo pipefail
    INSTANCE_ID="$(curl -s http://169.254.169.254/latest/meta-data/instance-id)"
    AWS_AZ="$(curl -s http://169.254.169.254/latest/meta-data/placement/availability-zone)"
    PROVIDER_ID="aws:///${AWS_AZ}/${INSTANCE_ID}"
    mkdir -p /etc/systemd/system/kubelet.service.d
    cat &gt;/etc/systemd/system/kubelet.service.d/20-karpenter.conf &lt;&lt;EOF
    [Service]
    Environment="KUBELET_EXTRA_ARGS=--cloud-provider=external --provider-id=${PROVIDER_ID} --register-with-taints=karpenter.sh/unregistered:NoExecute,gpu=true:NoSchedule --node-labels=node.lifecycle=karpenter,node.accelerator=nvidia-gpu"
    EOF
    systemctl daemon-reload
    systemctl enable containerd
    systemctl start containerd
    nvidia-smi || true
    kubeadm join https://&lt;KUBE_APISERVER_DNS_NAME&gt;:6443 \
      --token &lt;KUBEADM_BOOTSTRAP_TOKEN&gt; \
      --discovery-token-ca-cert-hash sha256:&lt;KUBEADM_CA_CERT_HASH&gt; \
      --node-name "${INSTANCE_ID}"
    systemctl restart kubelet

---
apiVersion: karpenter.sh/v1
kind: NodePool
metadata:
  name: workload-gpu-l4
spec:
  template:
    metadata:
      labels:
        node.lifecycle: karpenter
        node.accelerator: nvidia-gpu
        gpu.workload: inference
    spec:
      nodeClassRef:
        group: karpenter.k8s.aws
        kind: EC2NodeClass
        name: kubean-aws-gpu
      taints:
        - key: gpu
          value: "true"
          effect: NoSchedule
      requirements:
        - key: kubernetes.io/arch
          operator: In
          values: ["amd64"]
        - key: karpenter.sh/capacity-type
          operator: In
          values: ["spot", "on-demand"]
        - key: karpenter.k8s.aws/instance-family
          operator: In
          values: ["g6"]
        - key: karpenter.k8s.aws/instance-gpu-manufacturer
          operator: In
          values: ["nvidia"]
        - key: karpenter.k8s.aws/instance-gpu-name
          operator: In
          values: ["l4"]
        - key: karpenter.k8s.aws/instance-gpu-count
          operator: In
          values: ["1"]
  limits:
    nvidia.com/gpu: "20"
  disruption:
    consolidationPolicy: WhenEmpty
    consolidateAfter: 10m

---
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: nvidia-device-plugin
  namespace: kube-system
spec:
  selector:
    matchLabels:
      name: nvidia-device-plugin
  template:
    metadata:
      labels:
        name: nvidia-device-plugin
    spec:
      tolerations:
        - key: gpu
          operator: Equal
          value: "true"
          effect: NoSchedule
        - operator: Exists
          effect: NoExecute
      nodeSelector:
        node.accelerator: nvidia-gpu
      containers:
        - image: nvcr.io/nvidia/k8s-device-plugin:&lt;NVIDIA_DEVICE_PLUGIN_VERSION&gt;
          name: nvidia-device-plugin
          args:
            - --fail-on-init-error=false
          securityContext:
            privileged: true
          volumeMounts:
            - name: device-plugin
              mountPath: /var/lib/kubelet/device-plugins
      volumes:
        - name: device-plugin
          hostPath:
            path: /var/lib/kubelet/device-plugins

---
apiVersion: v1
kind: Pod
metadata:
  name: cuda-vectoradd-test
spec:
  restartPolicy: Never
  tolerations:
    - key: gpu
      operator: Equal
      value: "true"
      effect: NoSchedule
  nodeSelector:
    node.accelerator: nvidia-gpu
  containers:
    - name: cuda
      image: nvcr.io/nvidia/k8s/cuda-sample:vectoradd-cuda12.5.0
      resources:
        limits:
          nvidia.com/gpu: 1
```

## 8. Validation and Troubleshooting Checklist

- [ ] All Kubean-managed cluster nodes are in the Ready state.
- [ ] The infra workers are labeled correctly and hosting the Karpenter controller.
- [ ] The Karpenter controller can access the AWS API.
- [ ] The EC2 node security group allows access to the Kubernetes API Server on port 6443.
- [ ] The kubelet `providerID` on newly provisioned nodes is correctly configured.
- [ ] CPU workloads can trigger NodeClaims.
- [ ] GPU workloads can trigger GPU NodeClaims.
- [ ] `nvidia-smi` runs successfully on GPU nodes.
- [ ] `nvidia.com/gpu` appears in the node allocatable resources.
- [ ] Idle nodes are reclaimed according to the configured disruption policy.

```bash
kubectl get pods -A
kubectl get nodes -o wide
kubectl get nodeclaims
kubectl get nodes -l node.lifecycle=karpenter
kubectl get nodes -l node.accelerator=nvidia-gpu
kubectl describe node &lt;GPU_NODE_NAME&gt; | grep -A5 "nvidia.com/gpu"
kubectl logs -n karpenter deploy/karpenter
kubectl logs cuda-vectoradd-test
```

**Common Failure Points:**

- The API server security group does not allow inbound access.
- The bootstrap token has expired.
- The CA certificate hash is incorrect.
- The Karpenter controller lacks the `iam:PassRole` permission.
- The GPU AMI is not configured with the NVIDIA container runtime.
- The NVIDIA device plugin does not tolerate the GPU taint.
