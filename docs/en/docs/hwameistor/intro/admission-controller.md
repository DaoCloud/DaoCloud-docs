---
hide:
  - toc
---

# Admission controller

The admission controller is a webhook that can automatically authenticate HwameiStor data volumes and assist in modifying `schedulerName` to hwameistor-scheduler.
For details, see [Kubernetes Dynamic Admission Control](https://kubernetes.io/zh-cn/docs/reference/access-authn-authz/extensible-admission-controllers/).

- Identify HwameiStor data volume

    An admission controller can fetch all PVCs used by a pod and inspect each PVC [storage provisioner](https://kubernetes.io/en-us/docs/concepts/storage/storage-classes/#provisioner).
    If the name suffix of the producer is `*.hwameistor.io`, it means that the Pod is using the data volume provided by HwameiStor.

- Authenticate resources

    Admission controllers only validate `POD` resources and do so when they are created.

    !!! info

        To ensure that the Pods of HwameiStor can start smoothly, the Pods under the namespace where HwameiStor is located will not be verified.