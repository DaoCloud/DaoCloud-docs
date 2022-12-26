---
hide:
  - toc
---

# Volume

Files in containers are stored temporarily on disk, which can cause problems for more important applications running in containers.

- Problem 1: Files are lost when the container crashes. The kubelet restarts the container, but the container restarts in a clean state.
- Problem 2: This problem occurs when running multiple containers in the same `Pod` and sharing files.

The abstraction of a Kubernetes volume (Volume) solves both of these problems.

Kubernetes supports many types of volumes. Pods can use any number of volume types concurrently.
Ephemeral volume types have the same lifetime as Pods, but persistent volumes can outlive Pods.
Kubernetes also destroys ephemeral volumes when the Pod no longer exists; however, Kubernetes does not destroy persistent volumes.
For any type of volume in a given Pod, there is no data loss across container restarts.

At its core, a volume is a directory in which data may be stored, and containers in a Pod can access the data in that directory.
The particular volume type employed will determine how the directory is formed, what media is used to hold the data, and what is contained within the directory.

When using volumes, set the volumes provided to Pods in the `.spec.volumes` field, and declare where the volumes will be mounted in containers in the `.spec.containers[*].volumeMounts` field.

Refer to the official Kubernetes documentation:

- [Volumes](https://kubernetes.io/docs/concepts/storage/volumes/)
- [Persistent Volumes](https://kubernetes.io/docs/concepts/storage/persistent-volumes/)
- [Ephemeral Volumes](https://kubernetes.io/docs/concepts/storage/ephemeral-volumes/)