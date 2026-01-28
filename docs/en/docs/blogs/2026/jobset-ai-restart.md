# Kubernetes x JobSet: How Co-evolution Makes AI Job Restarts 10× Faster

In the fast-moving world of AI infrastructure, a powerful synergy is emerging: the Kubernetes community develops core capabilities, while downstream projects such as [JobSet](https://github.com/kubernetes-sigs/jobset), [Ray](https://github.com/ray-project/ray), and [LeaderWorkerSet (LWS)](https://github.com/kubernetes-sigs/lws) adopt these features to deliver dramatic efficiency gains. We call this **co-evolution**—the entire ecosystem moving forward together.

Kubernetes has recently introduced a growing set of AI-related capabilities. However, to fully unlock their potential for AI workloads, other projects must adapt to them. Today, we explore a representative example:

**JobSet achieves a 92% restart speed improvement by leveraging Kubernetes in-place container restarts.**

## The Problem: Slow JobSet Restarts

When a distributed training job running on [JobSet](https://github.com/kubernetes-sigs/jobset) needs to restart—due to transient failures, configuration updates, or checkpoint recovery—the traditional approach involves:

1. **Deleting all Pods in the JobSet**
2. **Waiting for Pod termination** to complete
3. **Re-scheduling all Pods** via the Kubernetes scheduler
4. **Waiting for Pods to start** (including image pulls, init containers, etc.)

In a large-scale cluster with 5,000 nodes, this process takes about **2 minutes and 10 seconds**. For AI/ML workloads where fast recovery is critical, this overhead is significant.

## The Solution: In-Place Container Restarts

Kubernetes has introduced capabilities that allow containers to restart without recreating the Pod:

### KEP-5307: Container Restart Policy (Kubernetes 1.34)

[KEP-5307](https://github.com/kubernetes/enhancements/blob/master/keps/sig-node/5307-container-restart-policy/README.md)
introduces fine-grained control over restart behavior for individual containers within a Pod. This enables:

- Specifying restart policies per container (not just per Pod)
- Triggering container restarts without affecting the entire Pod
- Preserving Pod identity, IP, and volumes during restarts

### KEP-5532: Restart All Containers on Container Exit (Kubernetes 1.35)

[KEP-5532](https://github.com/kubernetes/enhancements/blob/master/keps/sig-node/5532-restart-all-containers-on-container-exits/README.md)
extends this capability to coordinated restarts:

- Restarting all containers in a Pod when a specific container exits
- Restarting init containers and sidecars as part of the Pod lifecycle
- Enabling Pod-level restart coordination without Pod recreation

## Real-World Results: JobSet In-Place Restarts

The JobSet team developed an [in-place restart prototype](https://github.com/kubernetes-sigs/jobset/compare/main...GiuseppeTT:jobset:in-place-restart-prototype) that demonstrates dramatic performance improvements:

| Metric | Traditional Restart | In-Place Restart | Improvement |
| --- | --- | --- | --- |
| Restart time | 2 min 10 sec | 10 sec | **92% faster** |
| Test scale | 5,000 nodes | 5,000 nodes | – |
| Scheduling overhead | High | None | Eliminated |
| Pod recreation | Required | Not required | Avoided |

For detailed design information, see the
[JobSet in-place restart design document](https://docs.google.com/document/d/16zexVooHKPc80F4dVtUjDYK9DOpkVPRNfSv0zRtfFpk/edit?tab=t.0#heading=h.y6xl7juq7465).

## Why This Matters for AI Workloads

### 1. Distributed Training Recovery

Large-scale distributed training jobs (PyTorch DDP, TensorFlow MultiWorkerMirroredStrategy) are especially sensitive to restart latency:

- **Checkpoint recovery**: After a failure, all workers must restart from the latest checkpoint. In-place restarts make worker recovery **12× faster**.
- **Gradient synchronization**: Training can only proceed when all workers are running. Faster restarts mean less wasted GPU time.
- **Cost savings**: On expensive GPU clusters ($2–10 per GPU-hour), saving 2 minutes per restart quickly adds up.

### 2. Job Dependencies

Many AI pipelines have complex job dependencies. When a job restarts:

- **Downstream jobs** wait for upstream completion
- **Gang scheduling constraints** require all workers to be present
- **Network connections** must be preserved for collective operations

In-place restarts preserve Pod identity and network connections, minimizing disruption to the overall pipeline.

### 3. Resource Efficiency

Traditional restarts involve:

- **Scheduler load**: Finding nodes for potentially thousands of Pods
- **API server load**: Creating and deleting Pod objects
- **Node preparation**: Image pulls, volume mounts, init containers

In-place restarts eliminate all of this overhead, reserving resources for actual workloads.

## How It Works

### Before: Traditional Restart Flow

```text
Trigger job restart
    ↓
Delete all Pods → wait for termination (30s+)
    ↓
Create new Pods → wait for scheduling (30s+)
    ↓
Pull images (if needed) → start containers (60s+)
    ↓
Total: ~2 min 10 sec
````

### After: In-Place Restart Flow

```text
Trigger job restart
    ↓
Send container exit signal → containers restart in place (10s)
    ↓
Total: ~10 sec
```

Key differences:

1. **No Pod deletion**: Pod objects are preserved, maintaining identity
2. **No re-scheduling**: Pods remain on their current nodes
3. **No image pulls**: Images are already cached on the node
4. **Immediate restart**: Container processes restart directly

## Implementation Considerations

### When to Use In-Place Restarts

* **Transient failures**: Container crashes, OOM kills, network timeouts
* **Configuration updates**: Restarting to pick up new environment variables
* **Checkpoint recovery**: Resuming training from saved state
* **Rolling restarts**: Gracefully restarting workers in sequence

### When Traditional Restarts Are Required

* **Node failures**: Pods must move to healthy nodes
* **Resource changes**: Pods need more or fewer resources (consider VPA)
* **Image updates**: A new container image is required
* **Topology changes**: Pods need different placement

### Integrating with JobSet

JobSet can leverage in-place restarts as follows:

```yaml
apiVersion: jobset.x-k8s.io/v1alpha2
kind: JobSet
metadata:
  name: distributed-training
spec:
  replicatedJobs:
  - name: workers
    replicas: 8
    template:
      spec:
        template:
          spec:
            restartPolicy: Always  # Enable in-place restarts
            containers:
            - name: trainer
              image: pytorch/pytorch:latest
```

## The Broader Co-evolution Pattern

This JobSet improvement is a classic example of co-evolution in cloud-native AI:

| Kubernetes Capability  | Project Adoption    | Benefit                    |
| ---------------------- | ------------------- | -------------------------- |
| In-place restart       | JobSet              | 92% faster recovery        |
| Gang scheduling (1.35) | Kueue, LWS          | All-or-nothing placement   |
| DRA (1.34 GA)          | NVIDIA GPU Operator | Flexible device allocation |
| Workload API (1.35)    | Volcano, YuniKorn   | Native workload support    |

As Kubernetes continues to add AI-friendly features, we expect more projects to adopt them, creating a virtuous cycle of improvement.

## Getting Started

### Prerequisites

* Kubernetes 1.34+ (for KEP-5307)
* Kubernetes 1.35+ (for KEP-5532 Pod-level restarts)
* A JobSet version that supports in-place restarts (check the latest release)

### Enable Feature Gates

```bash
# Enable KEP-5307 (Container Restart Policy, 1.34+) on kubelet
--feature-gates=ContainerRestartPolicy=true

# Enable KEP-5532 (Restart All Containers, 1.35+) on kubelet
--feature-gates=RestartAllContainersOnContainerExits=true
```

### Test In-Place Restarts

1. Deploy a JobSet with `restartPolicy: Always`
2. Trigger a container restart (e.g., `kubectl exec ... -- kill -TERM 1`)
3. Observe the restart time compared to Pod recreation

## Future Roadmap

In-place restart capabilities continue to evolve:

* **KEP-5307 graduation**: Moving toward Beta/GA
* **KEP-5532 enhancements**: More robust Pod-level restart control
* **JobSet integration**: Native support for in-place restart policies
* **Observability**: Better visibility into restart events
* **Kueue integration**: Workload-aware restart handling

## Conclusion

The JobSet in-place restart optimization showcases the power of co-evolution in the Kubernetes ecosystem. By adopting upstream Kubernetes capabilities, projects can achieve significant performance gains:

* **92% faster restarts** (2 min 10 sec → 10 sec)
* **Zero scheduling overhead**
* **Preserved Pod identity and networking**
* **Reduced API server load**

This is just one example of how the Kubernetes community and downstream projects collaborate to improve AI workload efficiency. As more AI-related features land in Kubernetes, we can expect JobSet, Ray, LWS, and others to deliver even more optimizations.

The future of AI infrastructure is co-evolution—and it’s already happening.

## References

### KEPs and Documentation

* [KEP-5307: Container Restart Policy](https://github.com/kubernetes/enhancements/blob/master/keps/sig-node/5307-container-restart-policy/README.md)
* [KEP-5532: Restart All Containers on Container Exit](https://github.com/kubernetes/enhancements/blob/master/keps/sig-node/5532-restart-all-containers-on-container-exits/README.md)
* [KEP-1287: In-Place Pod Vertical Scaling](https://github.com/kubernetes/enhancements/blob/master/keps/sig-node/1287-in-place-update-pod-resources/README.md)
* [JobSet In-Place Restart Design Doc](https://docs.google.com/document/d/16zexVooHKPc80F4dVtUjDYK9DOpkVPRNfSv0zRtfFpk/edit?tab=t.0#heading=h.y6xl7juq7465)
* [JobSet In-Place Restart Prototype](https://github.com/kubernetes-sigs/jobset/compare/main...GiuseppeTT:jobset:in-place-restart-prototype)

### Related Projects

* [JobSet](https://github.com/kubernetes-sigs/jobset) – Kubernetes SIG Apps
* [LeaderWorkerSet](https://github.com/kubernetes-sigs/lws) – Kubernetes SIG Apps
* [Kueue](https://github.com/kubernetes-sigs/kueue) – Kubernetes SIG Scheduling
* [Volcano](https://github.com/volcano-sh/volcano) – CNCF Incubating
