# MXNet Jobs

!!! warning

    Since the Apache MXNet project has been archived, the Kubeflow MXJob will be deprecated and removed in a future version of Training Operator 1.9.

Apache MXNet is a high-performance deep learning framework that supports multiple programming languages. MXNet jobs can be trained in various ways, including single-machine mode and distributed mode. In AI Lab, we provide support for MXNet jobs, so you can quickly create MXNet jobs and perform model training through a graphical interface.

This tutorial will guide you on how to create and run single-machine and distributed MXNet jobs on the AI Lab platform.

## Job Configuration

- **Job Type**: `MXNet`, which supports both single-machine and distributed modes.
- **Runtime Environment**: Select an image that contains the MXNet framework, or install the necessary dependencies in the job.

## Job Runtime Environment

We use the `release-ci.daocloud.io/baize/kubeflow/mxnet-gpu:latest` image as the basic runtime environment for the job. This image has MXNet and its related dependencies preinstalled and supports GPU acceleration.

> **Note**: To learn how to create and manage an environment, refer to [Environment List](../dataset/environments.md).

## Create MXNet Jobs

<!-- ![mxnet](../../images/mxnet_job.png) -->

### MXNet Single Jobs

#### Steps to Create

1. **Log in to the platform**: Log in to the AI Lab platform, click **Job Center** in the left navigation bar to enter the **Training Jobs** page.
2. **Create a job**: Click the **Create** button in the upper right corner to enter the job creation page.
3. **Select the job type**: In the pop-up window, select the job type as `MXNet`, and then click **Next**.
4. **Fill in the job information**: Fill in the job name and description, for example, "MXNet single training job", and then click **OK**.
5. **Configure the job parameters**: Configure the runtime parameters, image, resources, and other information for the job according to your needs.

#### Parameters

- **Start Command**: `python3`
- **Command Parameters**:

    ```bash
    /mxnet/mxnet/example/gluon/mnist/mnist.py --epochs 10 --cuda
    ```

    **Explanation**:

    - `/mxnet/mxnet/example/gluon/mnist/mnist.py`: The MNIST handwritten digit recognition example script provided by MXNet.
    - `--epochs 10`: Sets the number of training epochs to 10.
    - `--cuda`: Uses CUDA for GPU acceleration.

#### Resource Configuration

- **Replicas**: 1 (single-machine job)
- **Resource Requests**:
    - **CPU**: 2 cores
    - **Memory**: 4 GiB
    - **GPU**: 1

#### Complete MXJob Configuration Example

The following is the YAML configuration of a single-machine MXJob:

```yaml
apiVersion: "kubeflow.org/v1"
kind: "MXJob"
metadata:
  name: "mxnet-single-job"
spec:
  jobMode: MXTrain
  mxReplicaSpecs:
    Worker:
      replicas: 1
      restartPolicy: Never
      template:
        spec:
          containers:
            - name: mxnet
              image: release-ci.daocloud.io/baize/kubeflow/mxnet-gpu:latest
              command: ["python3"]
              args:
                [
                  "/mxnet/mxnet/example/gluon/mnist/mnist.py",
                  "--epochs",
                  "10",
                  "--cuda",
                ]
              ports:
                - containerPort: 9991
                  name: mxjob-port
              resources:
                limits:
                  cpu: "2"
                  memory: 4Gi
                  nvidia.com/gpu: 1
                requests:
                  cpu: "2"
                  memory: 4Gi
                  nvidia.com/gpu: 1
```

**Configuration Explanation**:

- `apiVersion` and `kind`: Specify the API version and type of the resource. Here it is `MXJob`.
- `metadata`: The metadata, including the job name and other information.
- `spec`: The detailed configuration of the job.
    - `jobMode`: Set to `MXTrain`, indicating a training job.
    - `mxReplicaSpecs`: The replica configuration of the MXNet job.
        - `Worker`: Specify the configuration of the worker node.
            - `replicas`: The number of replicas. Here it is 1.
            - `restartPolicy`: The restart policy, set to `Never`, indicating that the job will not restart if it fails.
            - `template`: The Pod template, which defines the runtime environment and resources of the container.
                - `containers`: The container list.
                    - `name`: The container name.
                    - `image`: The image used.
                    - `command` and `args`: The start command and parameters.
                    - `ports`: The container port configuration.
                    - `resources`: The resource requests and limits.

#### Submit the Job

After the configuration is complete, click the **Submit** button to start running the MXNet single-machine job.

#### Results

After the job is successfully submitted, you can enter the **Job Details** page to view the resource usage and the running status of the job. From the upper right corner, go to **Workload Details** to view the log output during the run.

**Example Output**:

```bash
Epoch 1: accuracy=0.95
Epoch 2: accuracy=0.97
...
Epoch 10: accuracy=0.98
Training completed.
```

This indicates that the MXNet single-machine job ran successfully and model training was completed.

---

### MXNet Distributed Jobs

In distributed mode, an MXNet job can use multiple compute nodes to complete training together, improving training efficiency.

#### Steps to Create

1. **Log in to the platform**: Same as above.
2. **Create a job**: Click the **Create** button in the upper right corner to enter the job creation page.
3. **Select the job type**: Select the job type as `MXNet`, and then click **Next**.
4. **Fill in the job information**: Fill in the job name and description, for example, "MXNet distributed training job", and then click **OK**.
5. **Configure the job parameters**: Configure the runtime parameters, image, resources, and other information as needed.

#### Parameters

- **Start Command**: `python3`
- **Command Parameters**:

    ```bash
    /mxnet/mxnet/example/image-classification/train_mnist.py --num-epochs 10 --num-layers 2 --kv-store dist_device_sync --gpus 0
    ```

    **Explanation**:

    - `/mxnet/mxnet/example/image-classification/train_mnist.py`: The image classification example script provided by MXNet.
    - `--num-epochs 10`: The number of training epochs is 10.
    - `--num-layers 2`: The number of layers of the model is 2.
    - `--kv-store dist_device_sync`: Uses the distributed device synchronization mode.
    - `--gpus 0`: Uses GPU for acceleration.

#### Resource Configuration

- **Number of job replicas**: 3 (including Scheduler, Server, and Worker)
- **Resource requests of each role**:
    - **Scheduler**:
        - **Replicas**: 1
        - **Resource Requests**:
            - CPU: 2 cores
            - Memory: 4 GiB
            - GPU: 1
    - **Server** (parameter server):
        - **Replicas**: 1
        - **Resource Requests**:
            - CPU: 2 cores
            - Memory: 4 GiB
            - GPU: 1
    - **Worker**:
        - **Replicas**: 1
        - **Resource Requests**:
            - CPU: 2 cores
            - Memory: 4 GiB
            - GPU: 1

#### Complete MXJob Configuration Example

The following is the YAML configuration of a distributed MXJob:

```yaml
apiVersion: "kubeflow.org/v1"
kind: "MXJob"
metadata:
  name: "mxnet-job"
spec:
  jobMode: MXTrain
  mxReplicaSpecs:
    Scheduler:
      replicas: 1
      restartPolicy: Never
      template:
        spec:
          containers:
            - name: mxnet
              image: release-ci.daocloud.io/baize/kubeflow/mxnet-gpu:latest
              ports:
                - containerPort: 9991
                  name: mxjob-port
              resources:
                limits:
                  cpu: "2"
                  memory: 4Gi
                  nvidia.com/gpu: 1
                requests:
                  cpu: "2"
                  memory: 4Gi
    Server:
      replicas: 1
      restartPolicy: Never
      template:
        spec:
          containers:
            - name: mxnet
              image: release-ci.daocloud.io/baize/kubeflow/mxnet-gpu:latest
              ports:
                - containerPort: 9991
                  name: mxjob-port
              resources:
                limits:
                  cpu: "2"
                  memory: 4Gi
                  nvidia.com/gpu: 1
                requests:
                  cpu: "2"
                  memory: 4Gi
    Worker:
      replicas: 1
      restartPolicy: Never
      template:
        spec:
          containers:
            - name: mxnet
              image: release-ci.daocloud.io/baize/kubeflow/mxnet-gpu:latest
              command: ["python3"]
              args:
                [
                  "/mxnet/mxnet/example/image-classification/train_mnist.py",
                  "--num-epochs",
                  "10",
                  "--num-layers",
                  "2",
                  "--kv-store",
                  "dist_device_sync",
                  "--gpus",
                  "0",
                ]
              ports:
                - containerPort: 9991
                  name: mxjob-port
              resources:
                limits:
                  cpu: "2"
                  memory: 4Gi
                  nvidia.com/gpu: 1
                requests:
                  cpu: "2"
                  memory: 4Gi
```

**Configuration Explanation**:

- **Scheduler**: Responsible for coordinating the job scheduling of each node in the cluster.
- **Server** (parameter server): Used to store and update model parameters and implement distributed parameter synchronization.
- **Worker**: Actually executes the training job.
- **Resource Configuration**: Allocate appropriate resources to each role to ensure the job runs smoothly.

#### Number of Job Replicas

When creating a distributed MXNet job, you need to correctly set the **number of job replicas** according to the replica count configured in `mxReplicaSpecs`.

- **Total replicas** = Scheduler replicas + Server replicas + Worker replicas
- In this example:
    - Scheduler replicas: 1
    - Server replicas: 1
    - Worker replicas: 1
    - **Total replicas**: 1 + 1 + 1 = 3

Therefore, in the job configuration, you need to set the **number of job replicas** to **3**.

#### Submit the Job

After the configuration is complete, click the **Submit** button to start running the MXNet distributed job.

#### Results

Enter the **Job Details** page to view the running status and resource usage of the job. You can view the log output of each role (Scheduler, Server, and Worker).

**Example Output**:

```bash
INFO:root:Epoch[0] Batch [50]     Speed: 1000 samples/sec   accuracy=0.85
INFO:root:Epoch[0] Batch [100]    Speed: 1200 samples/sec   accuracy=0.87
...
INFO:root:Epoch[9] Batch [100]    Speed: 1300 samples/sec   accuracy=0.98
Training completed.
```

This indicates that the MXNet distributed job ran successfully and model training was completed.

---

## Summary

Through this tutorial, you have learned how to create and run single-machine and distributed MXNet jobs on the AI Lab platform. We introduced the MXJob configuration in detail, as well as how to specify the commands to run and the resource requirements in the job. We hope this tutorial is helpful to you. If you have any questions, please refer to other documents provided by the platform or contact technical support.

---

## Appendix

- **Notes**:
    - Ensure that the image you use contains the required MXNet version and dependencies.
    - Adjust the resource configuration according to actual needs to avoid insufficient or wasted resources.
    - If you need to use a custom training script, modify the start command and parameters.

- **Reference Documents**:
    - [MXNet Official Documentation](https://mxnet.apache.org/)
    - [Kubeflow MXJob Guide](https://v1-8-branch.kubeflow.org/docs/components/training/mxnet/)
