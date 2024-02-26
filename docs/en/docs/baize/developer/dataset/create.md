# Create Dataset

A dataset is a collection of files or objects that encapsulates various data sources to be efficiently accessed through Kubernetes, in order to support the quick use of data during development and training.

1. Click **Data Management** -> **Dataset List** in the left navigation bar, then click the **Create** button on the right.

    <!-- add image later -->

2. The system will pre-fill the cluster to deploy to, namespace, and other basic information. After adding a name, labels, annotations, etc., click **Next**.

    <!-- add image later -->

3. After selecting a data source type, click **Confirm**.

    <!-- add image later -->

    Currently supported data sources include:

    - GIT: Supports repositories such as GitHub, GitLab, Gitee, etc.
    - S3: Supports object storage services like Amazon S3.
    - HTTP: Directly input a valid HTTP URL.
    - PVC: Supports pre-created Kubernetes PersistentVolumeClaims.
    - NFS: Supports NFS shared storage.

4. Upon successful creation of the dataset, you will be returned to the dataset list.

!!! info

    The system will automatically perform a one-time data preloading immediately after the dataset is created; the dataset cannot be used until the preloading is complete.

## Example

**Training Code**

```yaml
apiVersion: "kubeflow.org/v1"
kind: PyTorchJob
metadata:
  name: pytorch-distributed-sample-v1 # update job name
  namespace: luchuanjia-p4 # update namespace
  annotations:
    baize.io/description: ""
  labels:
    jobs.baize.io/training-mode: DISTRIBUTED
    kueue.x-k8s.io/queue-name: p4-gpu # update queue name
spec:
  pytorchReplicaSpecs:
    Master:
      replicas: 1
      restartPolicy: OnFailure
      template:
        spec:
          containers:
            - name: pytorch
              image: dockerproxy.com/kubeflowkatib/pytorch-mnist:v1beta1-45c5727
              imagePullPolicy: Always
              command:
                - "python3"
                - "/opt/pytorch-mnist/mnist.py"
                - "--epochs=1"
              resources:
                limits:
                  cpu: "1"
                  memory: 2Gi
                  nvidia.com/gpu: '1' # use gpu
                requests:
                  cpu: "1"
                  memory: 2Gi
                  nvidia.com/gpu: '1'
          priorityClassName: baize-medium-priority
    Worker:
      replicas: 1
      restartPolicy: OnFailure
      template:
        spec:
          containers:
            - name: pytorch
              image: dockerproxy.com/kubeflowkatib/pytorch-mnist:v1beta1-45c5727
              imagePullPolicy: Always
              command:
                - "python3"
                - "/opt/pytorch-mnist/mnist.py"
                - "--epochs=1"
              resources:
                limits:
                  cpu: "1"
                  memory: 2Gi
                  nvidia.com/gpu: '1'
                requests:
                  cpu: "1"
                  memory: 2Gi
                  nvidia.com/gpu: '1'
          priorityClassName: baize-medium-priority
```

**Training Data** : <https://github.com/zalandoresearch/fashion-mnist>
