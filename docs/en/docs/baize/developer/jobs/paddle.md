# PaddlePaddle Jobs

PaddlePaddle is a deep learning platform open-sourced by Baidu, supporting a rich set of neural network models and distributed training methods. PaddlePaddle jobs can be trained in single-machine or distributed mode. In the AI Lab platform, we provide support for PaddlePaddle jobs, so you can quickly create PaddlePaddle jobs and perform model training through a graphical interface.

This tutorial will guide you on how to create and run single-machine and distributed PaddlePaddle jobs on the AI Lab platform.

## Job Configuration

- **Job Type**: `PaddlePaddle`, which supports both single-machine and distributed modes.
- **Runtime Environment**: Select an image that contains the PaddlePaddle framework, or install the necessary dependencies in the job.

## Job Runtime Environment

We use the `registry.baidubce.com/paddlepaddle/paddle:2.4.0rc0-cpu` image as the basic runtime environment for the job. This image has the PaddlePaddle framework preinstalled and is suitable for CPU computing. If you need to use GPU, select the corresponding GPU version image.

> **Note**: To learn how to create and manage an environment, refer to [Environment List](../dataset/environments.md).

## Create PaddlePaddle Jobs

<!-- ![paddle](../../images/paddle_job.png) -->

### PaddlePaddle Single-Machine Training Jobs

#### Steps to Create

1. **Log in to the platform**: Log in to the AI Lab platform, click **Job Center** in the left navigation bar to enter the **Training Jobs** page.
2. **Create a job**: Click the **Create** button in the upper right corner to enter the job creation page.
3. **Select the job type**: In the pop-up window, select the job type as `PaddlePaddle`, and then click **Next**.
4. **Fill in the job information**: Fill in the job name and description, for example, "PaddlePaddle single-machine training job", and then click **OK**.
5. **Configure the job parameters**: Configure the runtime parameters, image, resources, and other information for the job according to your needs.

#### Parameters

- **Start Command**: `python`
- **Command Parameters**:

    ```bash
    -m paddle.distributed.launch run_check
    ```

    **Explanation**:

    - `-m paddle.distributed.launch`: Uses the distributed launch module provided by PaddlePaddle. It can also be used in single-machine mode, making it easier to migrate to distributed mode in the future.
    - `run_check`: The test script provided by PaddlePaddle for checking whether the distributed environment works properly.

#### Resource Configuration

- **Replicas**: 1 (single-machine job)
- **Resource Requests**:
    - **CPU**: Set as needed. At least 1 core is recommended.
    - **Memory**: Set as needed. At least 2 GiB is recommended.
    - **GPU**: If you need to use GPU, select a GPU version image and allocate the corresponding GPU resources.

#### Complete PaddleJob Configuration Example

The following is the YAML configuration of a single-machine PaddleJob:

```yaml
apiVersion: kubeflow.org/v1
kind: PaddleJob
metadata:
    name: paddle-simple-cpu
    namespace: kubeflow
spec:
    paddleReplicaSpecs:
        Worker:
            replicas: 1
            restartPolicy: OnFailure
            template:
                spec:
                    containers:
                        - name: paddle
                          image: registry.baidubce.com/paddlepaddle/paddle:2.4.0rc0-cpu
                          command:
                              [
                                  'python',
                                  '-m',
                                  'paddle.distributed.launch',
                                  'run_check',
                              ]
```

**Configuration Explanation**:

- `apiVersion` and `kind`: Specify the API version and type of the resource. Here it is `PaddleJob`.
- `metadata`: The metadata, including the job name and namespace.
- `spec`: The detailed configuration of the job.
    - `paddleReplicaSpecs`: The replica configuration of the PaddlePaddle job.
        - `Worker`: Specify the configuration of the worker node.
            - `replicas`: The number of replicas. Here it is 1, indicating single-machine training.
            - `restartPolicy`: The restart policy, set to `OnFailure`, indicating that the job will automatically restart if it fails.
            - `template`: The Pod template, which defines the runtime environment and resources of the container.
                - `containers`: The container list.
                    - `name`: The container name.
                    - `image`: The image used.
                    - `command`: The start command and parameters.

#### Submit the Job

After the configuration is complete, click the **Submit** button to start running the PaddlePaddle single-machine job.

#### Results

After the job is successfully submitted, you can enter the **Job Details** page to view the resource usage and the running status of the job. From the upper right corner, go to **Workload Details** to view the log output during the run.

**Example Output**:

```bash
run check success, PaddlePaddle is installed correctly on this node :)
```

This indicates that the PaddlePaddle single-machine job ran successfully and the environment is configured properly.

---

### PaddlePaddle Distributed Training Jobs

In distributed mode, a PaddlePaddle job can use multiple compute nodes to complete training together, improving training efficiency.

#### Steps to Create

1. **Log in to the platform**: Same as above.
2. **Create a job**: Click the **Create** button in the upper right corner to enter the job creation page.
3. **Select the job type**: Select the job type as `PaddlePaddle`, and then click **Next**.
4. **Fill in the job information**: Fill in the job name and description, for example, "PaddlePaddle distributed training job", and then click **OK**.
5. **Configure the job parameters**: Configure the runtime parameters, image, resources, and other information as needed.

#### Parameters

- **Start Command**: `python`
- **Command Parameters**:

    ```bash
    -m paddle.distributed.launch train.py --epochs=10
    ```

    **Explanation**:

    - `-m paddle.distributed.launch`: Uses the distributed launch module provided by PaddlePaddle.
    - `train.py`: Your training script, which needs to be placed in the image or mounted into the container.
    - `--epochs=10`: The number of training epochs, set to 10 here.

#### Resource Configuration

- **Number of job replicas**: Set according to the `Worker` replica count. Here it is 2.
- **Resource Requests**:
    - **CPU**: Set as needed. At least 1 core is recommended.
    - **Memory**: Set as needed. At least 2 GiB is recommended.
    - **GPU**: If you need to use GPU, select a GPU version image and allocate the corresponding GPU resources.

#### Complete PaddleJob Configuration Example

The following is the YAML configuration of a distributed PaddleJob:

```yaml
apiVersion: kubeflow.org/v1
kind: PaddleJob
metadata:
    name: paddle-distributed-job
    namespace: kubeflow
spec:
    paddleReplicaSpecs:
        Worker:
            replicas: 2
            restartPolicy: OnFailure
            template:
                spec:
                    containers:
                        - name: paddle
                          image: registry.baidubce.com/paddlepaddle/paddle:2.4.0rc0-cpu
                          command:
                              [
                                  'python',
                                  '-m',
                                  'paddle.distributed.launch',
                                  'train.py',
                              ]
                          args:
                              - '--epochs=10'
```

**Configuration Explanation**:

- `Worker`:
    - `replicas`: The number of replicas, set to 2, indicating that 2 worker nodes are used for distributed training.
    - Other configurations are similar to those in single-machine mode.

#### Number of Job Replicas

When creating a distributed PaddlePaddle job, you need to correctly set the **number of job replicas** according to the replica count configured in `paddleReplicaSpecs`.

- **Total replicas** = `Worker` replicas
- In this example:
    - `Worker` replicas: 2
    - **Total replicas**: 2

Therefore, in the job configuration, you need to set the **number of job replicas** to **2**.

#### Submit the Job

After the configuration is complete, click the **Submit** button to start running the PaddlePaddle distributed job.

#### Results

Enter the **Job Details** page to view the running status and resource usage of the job. You can view the log output of each worker node to confirm whether the distributed training is running properly.

**Example Output**:

```bash
Worker 0: Epoch 1, Batch 100, Loss 0.5
Worker 1: Epoch 1, Batch 100, Loss 0.6
...
Training completed.
```

This indicates that the PaddlePaddle distributed job ran successfully and model training was completed.

---

## Summary

Through this tutorial, you have learned how to create and run single-machine and distributed PaddlePaddle jobs on the AI Lab platform. We introduced the PaddleJob configuration in detail, as well as how to specify the commands to run and the resource requirements in the job. We hope this tutorial is helpful to you. If you have any questions, please refer to other documents provided by the platform or contact technical support.

---

## Appendix

- **Notes**:
    - **Training Script**: Ensure that `train.py` (or another training script) exists in the container. You can put the script into the container by using a custom image or mounting persistent storage.
    - **Image Selection**: Select an appropriate image according to your needs, for example, use `paddle:2.4.0rc0-gpu` when using GPU.
    - **Parameter Adjustment**: You can pass different training parameters by modifying `command` and `args`.

- **Reference Documents**:
    - [PaddlePaddle Official Documentation](https://www.paddlepaddle.org.cn/documentation/docs/zh/2.6/guides/index_cn.html)
    - [Kubeflow PaddleJob Guide](https://www.kubeflow.org/docs/components/training/user-guides/paddle/)
