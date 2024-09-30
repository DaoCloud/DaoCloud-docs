---
MTPE: windsonsea
Date: 2024-07-22
---

# Local Queue Initialization Failed

## Issue Description

When creating a Notebook, training task, or inference service, if the queue is being used for
the first time in that namespace, there will be a prompt to initialize the queue with one click.
However, the initialization fails.

![local-queue-initialization-failed](./images/kueue-init-localqueue.png)

## Issue Analysis

In the AI Lab environment, the queue management capability is provided by
[Kueue](https://kueue.sigs.k8s.io/). Kueue provides two types of queue management resources:

- **ClusterQueue**: A cluster-level queue mainly used to manage resource quotas within
  the queue, including CPU, memory, and GPU.
- **LocalQueue**: A namespace-level queue that needs to point to a ClusterQueue
  for resource allocation within the queue.

In the AI Lab environment, if a service is created and the specified
namespace does not have a `LocalQueue`, there will be a prompt to initialize the queue.

In rare cases, the `LocalQueue` initialization might fail due to special reasons.

### Solution

Check if Kueue is running normally. If the `kueue-controller-manager` is not running,
you can check it with the following command:

```bash
kubectl get deploy kueue-controller-manager -n baize-system
```

If the `kueue-controller-manager` is not running properly, fix Kueue first.

### References

- [ClusterQueue](https://kueue.sigs.k8s.io/docs/concepts/cluster_queue/)
- [LocalQueue](https://kueue.sigs.k8s.io/docs/concepts/local_queue/)
