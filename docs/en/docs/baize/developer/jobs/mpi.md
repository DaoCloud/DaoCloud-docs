# MPI Jobs

MPI (Message Passing Interface) is a communication protocol for parallel computing that allows
multiple compute nodes to exchange messages and collaborate.
An MPI job is a job that performs parallel computing using the MPI protocol.
It is suitable for application scenarios that require large-scale parallel processing,
such as distributed training and scientific computing.

In AI Lab, we provide support for MPI jobs. Through a graphical interface, you can quickly create
MPI jobs and perform high-performance parallel computing.
This tutorial will guide you on how to create and run an MPI job in AI Lab.

## Job Configuration

- **Job Type**: `MPI`, used to run parallel computing jobs.
- **Runtime Environment**: Use an image with the MPI environment preinstalled, or specify the necessary dependencies to install in the job.
- **MPIJob Configuration**: Understand and configure the various parameters of the MPIJob, such as the number of replicas and resource requests.

## Job Runtime Environment

Here we use the `baize-notebook` base image and the **associated environment** as the basic runtime environment for the job.
Make sure the runtime environment includes MPI and related libraries, such as OpenMPI and `mpi4py`.

> **Note**: To learn how to create an environment, refer to [Environment List](../dataset/environments.md).

## Create MPI Jobs

### Steps to Create an MPI Job

<!-- ![MPI Job](../../images/job-mpi01.png) -->

1. **Log in to the platform**: Log in to the AI Lab platform, click **Job Center** in the left navigation bar to enter the **Training Jobs** page.
2. **Create a job**: Click the **Create** button in the upper right corner to enter the job creation page.
3. **Select the job type**: In the pop-up window, select the job type as `MPI`, and then click **Next**.
4. **Fill in the job information**: Fill in the job name and description, for example, "benchmarks-mpi", and then click **Next**.
5. **Configure the job parameters**: Configure the runtime parameters, image, resources, and other information for the job according to your needs.

#### Parameters

- **Start Command**: Use `mpirun`, which is the command for running MPI programs.
- **Command Parameters**: Enter the parameters of the MPI program you want to run.

**Example: Run TensorFlow Benchmarks**

In this example, we will run a TensorFlow benchmark program and use Horovod for distributed training.
First, ensure that the image you use contains the required dependencies, such as TensorFlow, Horovod, and Open MPI.

**Image Selection**: Use an image that contains TensorFlow and MPI, such as `mai.daocloud.io/docker.io/mpioperator/tensorflow-benchmarks:latest`.

**Command Parameters**:

```bash
mpirun --allow-run-as-root -np 2 -bind-to none -map-by slot \
  -x NCCL_DEBUG=INFO -x LD_LIBRARY_PATH -x PATH \
  -mca pml ob1 -mca btl ^openib \
  python scripts/tf_cnn_benchmarks/tf_cnn_benchmarks.py \
  --model=resnet101 --batch_size=64 --variable_update=horovod
```

**Explanation**:

- `mpirun`: The start command of MPI.
- `--allow-run-as-root`: Allows running as the root user (the container usually runs as root).
- `-np 2`: Specifies the number of processes to run as 2.
- `-bind-to none`, `-map-by slot`: The configuration for binding and mapping MPI processes.
- `-x NCCL_DEBUG=INFO`: Sets the debug information level of NCCL (NVIDIA Collective Communication Library).
- `-x LD_LIBRARY_PATH`, `-x PATH`: Passes the necessary environment variables in the MPI environment.
- `-mca pml ob1 -mca btl ^openib`: The configuration parameters of MPI, specifying the transport layer and message layer protocols.
- `python scripts/tf_cnn_benchmarks/tf_cnn_benchmarks.py`: Runs the TensorFlow benchmark script.
- `--model=resnet101`, `--batch_size=64`, `--variable_update=horovod`: The parameters of the TensorFlow script, specifying the model, batch size, and the use of Horovod for parameter updates.

#### Resource Configuration

In the job configuration, you need to allocate appropriate resources, such as CPU, memory, and GPU, for each node (Launcher and Worker).

**Resource Example**:

- **Launcher**:

    - **Replicas**: 1
    - **Resource Requests**:
        - CPU: 2 cores
        - Memory: 4 GiB

- **Worker**:

    - **Replicas**: 2
    - **Resource Requests**:
        - CPU: 2 cores
        - Memory: 4 GiB
        - GPU: Allocate as needed

#### Complete MPIJob Configuration Example

The following is a complete MPIJob configuration example for your reference.

```yaml
apiVersion: kubeflow.org/v1
kind: MPIJob
metadata:
  name: tensorflow-benchmarks
spec:
  slotsPerWorker: 1
  runPolicy:
    cleanPodPolicy: Running
  mpiReplicaSpecs:
    Launcher:
      replicas: 1
      template:
        spec:
          containers:
            - name: tensorflow-benchmarks
              image: mai.daocloud.io/docker.io/mpioperator/tensorflow-benchmarks:latest
              command:
                - mpirun
                - --allow-run-as-root
                - -np
                - "2"
                - -bind-to
                - none
                - -map-by
                - slot
                - -x
                - NCCL_DEBUG=INFO
                - -x
                - LD_LIBRARY_PATH
                - -x
                - PATH
                - -mca
                - pml
                - ob1
                - -mca
                - btl
                - ^openib
                - python
                - scripts/tf_cnn_benchmarks/tf_cnn_benchmarks.py
                - --model=resnet101
                - --batch_size=64
                - --variable_update=horovod
              resources:
                limits:
                  cpu: "2"
                  memory: 4Gi
                requests:
                  cpu: "2"
                  memory: 4Gi
    Worker:
      replicas: 2
      template:
        spec:
          containers:
            - name: tensorflow-benchmarks
              image: mai.daocloud.io/docker.io/mpioperator/tensorflow-benchmarks:latest
              resources:
                limits:
                  cpu: "2"
                  memory: 4Gi
                  nvidia.com/gpumem: 1k
                  nvidia.com/vgpu: "1"
                requests:
                  cpu: "2"
                  memory: 4Gi
```

**Configuration Explanation**:

- `apiVersion` and `kind`: The API version and type of the resource. `MPIJob` is a custom resource defined by Kubeflow for creating MPI-type jobs.
- `metadata`: The metadata, including the name of the job and other information.
- `spec`: The detailed configuration of the job.
    - `slotsPerWorker`: The number of slots per Worker node, usually set to 1.
    - `runPolicy`: The run policy, for example, whether to clean up Pods after the job is completed.
    - `mpiReplicaSpecs`: The replica configuration of the MPI job.
        - `Launcher`: The launcher, which is responsible for starting the MPI job.
            - `replicas`: The number of replicas, usually 1.
            - `template`: The Pod template, which defines the image, command, resources, and so on for the container to run.
        - `Worker`: The worker nodes, which are the compute nodes that actually execute the job.
            - `replicas`: The number of replicas, set according to the parallel requirements. Here it is set to 2.
            - `template`: The Pod template, which also defines the runtime environment and resources of the container.

#### Number of Job Replicas

When creating an MPI job, you need to correctly set the **number of job replicas** according to the replica count configured in `mpiReplicaSpecs`.

- **Total replicas** = `Launcher` replicas + `Worker` replicas
- In this example:

    - `Launcher` replicas: 1
    - `Worker` replicas: 2
    - **Total replicas**: 1 + 2 = 3

Therefore, in the job configuration, you need to set the **number of job replicas** to **3**.

#### Submit the Job

After the configuration is complete, click the **Submit** button to start running the MPI job.

## Results

After the job is successfully submitted, you can enter the **Job Details** page to view the resource usage and the running status of the job.
From the upper right corner, go to **Workload Details** to view the log output of each node during the run.

**Example Output**:

```bash
TensorFlow:  1.13
Model:       resnet101
Mode:        training
Batch size:  64
...

Total images/sec: 125.67
```

This indicates that the MPI job ran successfully and the TensorFlow benchmark program completed distributed training.

---

## Summary

Through this tutorial, you have learned how to create and run an MPI job on the AI Lab platform. We introduced the MPIJob configuration in detail,
as well as how to specify the commands to run and the resource requirements in the job. We hope this tutorial is helpful to you. If you have any questions, please refer to other documents provided by the platform or contact technical support.

---

**Appendix**:

- If your runtime environment does not have the required libraries preinstalled (such as `mpi4py` and Horovod), add an installation command to the job, or use an image with the relevant dependencies preinstalled.
- In actual applications, you can modify the MPIJob configuration as needed, for example, change the image, command parameters, and resource requests.
