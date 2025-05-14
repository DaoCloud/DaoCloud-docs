---
MTPE: windsonsea
Date: 2024-08-05
---

# baizectl CLI Usage Guide

`baizectl` is a command line tool specifically designed for model developers and data scientists within
the DCE 5.0 AI Lab module. It provides a series of commands to help users manage
distributed training jobs, check job statuses, manage datasets, and more. It also supports connecting
to Kubernetes worker clusters and DCE 5.0 workspaces, aiding users in efficiently using and managing
Kubernetes platform resources.

## Installation

Currently, `baizectl` is integrated within DCE 5.0 AI Lab. Once you create a Notebook, you can directly use `baizectl` within it.

---

## Getting Started

### Basic Information

The basic format of the `baizectl` command is as follows:

```bash
jovyan@19d0197587cc:/$ baizectl
AI platform management tool

Usage:
  baizectl [command]

Available Commands:
  completion  Generate the autocompletion script for the specified shell
  data        Management datasets
  help        Help about any command
  job         Manage jobs
  login       Login to the platform
  version     Show cli version

Flags:
      --cluster string     Cluster name to operate
  -h, --help               help for baizectl
      --mode string        Connection mode: auto, api, notebook (default "auto")
  -n, --namespace string   Namespace to use for the operation. If not set, the default Namespace will be used.
  -s, --server string      DCE5 access base url
      --skip-tls-verify    Skip TLS certificate verification
      --token string       DCE5 access token
  -w, --workspace int32    Workspace ID to use for the operation

Use "baizectl [command] --help" for more information about a command.
```

The above provides basic information about `baizectl`. Users can view the help information using
`baizectl --help`, or view the help information for specific commands using `baizectl [command] --help`.

### View Versions

`baizectl` supports viewing version information using the `version` command.

```bash
(base) jovyan@den-0:~$ baizectl version 
baizectl version: v0.5.0, commit sha: ac0837c4
```

### Command Format

The basic format of the `baizectl` command is as follows:

```bash
baizectl [command] [flags]
```

Here, `[command]` refers to the specific operation command, such as `data` and `job`, and
`[flags]` are optional parameters used to specify detailed information about the operation.

### Common Options

- `--cluster string`: Specify the name of the cluster to operate on.
- `-h, --help`: Display help information.
- `--mode string`: Connection mode, optional values are `auto`, `api`, `notebook` (default value is `auto`).
- `-n, --namespace string`: Specify the namespace for the operation. If not set,
  the default namespace will be used.
- `-s, --server string`: Base URL for accessing DCE5.
- `--skip-tls-verify`: Skip TLS certificate verification.
- `--token string`: Access token for DCE5.
- `-w, --workspace int32`: Specify the workspace ID for the operation.

---

## Features

### Job Management

`baizectl` provides a series of commands to manage distributed training jobs,
including viewing job lists, submitting jobs, viewing logs, restarting jobs, deleting jobs, and more.

```bash
jovyan@19d0197587cc:/$ baizectl job
Manage jobs

Usage:
  baizectl job [command]

Available Commands:
  delete      Delete a job
  logs        Show logs of a job
  ls          List jobs
  restart     restart a job
  submit      Submit a job

Flags:
  -h, --help            help for job
  -o, --output string   Output format. One of: table, json, yaml (default "table")
      --page int        Page number (default 1)
      --page-size int   Page size (default -1)
      --search string   Search query
      --sort string     Sort order
      --truncate int    Truncate output to the given length, 0 means no truncation (default 50)

Use "baizectl job [command] --help" for more information about a command.
```

#### Submit Training Jobs

`baizectl` supports submitting a job using the `submit` command.
You can view detailed information by using `baizectl job submit --help`.

```bash
(base) jovyan@den-0:~$ baizectl job submit --help
Submit a job

Usage:
  baizectl job submit [flags] -- command ...

Aliases:
  submit, create

Examples:
# Submit a job to run the command "torchrun python train.py"
baizectl job submit -- torchrun python train.py
# Submit a job with 2 workers(each pod use 4 gpus) to run the command "torchrun python train.py" and use the image "pytorch/pytorch:1.8.1-cuda11.1-cudnn8-runtime"
baizectl job submit --image pytorch/pytorch:1.8.1-cuda11.1-cudnn8-runtime --workers 2 --resources nvidia.com/gpu=4 -- torchrun python train.py
# Submit a tensorflow job to run the command "python train.py"
baizectl job submit --tensorflow -- python train.py


Flags:
      --annotations stringArray                       The annotations of the job, the format is key=value
      --auto-load-env                                 It only takes effect when executed in Notebook, the environment variables of the current environment will be automatically read and set to the environment variables of the Job, the specific environment variables to be read can be specified using the BAIZE_MAPPING_ENVS environment variable, the default is PATH,CONDA_*,*PYTHON*,NCCL_*, if set to false, the environment variables of the current environment will not be read. (default true)
      --commands stringArray                          The default command of the job
  -d, --datasets stringArray                          The dataset bind to the job, the format is datasetName:mountPath, e.g. mnist:/data/mnist
  -e, --envs stringArray                              The environment variables of the job, the format is key=value
  -x, --from-notebook string                          Define whether to read the configuration of the current Notebook and directly create tasks, including images, resources, and dataset.
                                                      auto: Automatically determine the mode according to the current environment. If the current environment is a Notebook, it will be set to notebook mode.
                                                      false: Do not read the configuration of the current Notebook.
                                                      true: Read the configuration of the current Notebook. (default "auto")
  -h, --help                                          help for submit
      --image string                                  The image of the job, it must be specified if fromNotebook is false.
  -t, --job-type string                               Job type: PYTORCH, TENSORFLOW, PADDLE (default "PYTORCH")
      --labels stringArray                            The labels of the job, the format is key=value
      --max-retries int32                             number of retries before marking this job failed
      --max-run-duration int                          Specifies the duration in seconds relative to the startTime that the job may be active before the system tries to terminate it
      --name string                                   The name of the job, if empty, the name will be generated automatically.
      --paddle                                        PaddlePaddle Job, has higher priority than --job-type
      --priority string                               The priority of the job, current support baize-medium-priority, baize-low-priority, baize-high-priority
      --pvcs stringArray                              The pvcs bind to the job, the format is pvcName:mountPath, e.g. mnist:/data/mnist
      --pytorch                                       Pytorch Job, has higher priority than --job-type
      --queue string                                  The queue to used
      --requests-resources stringArray                Similar to resources, but sets the resources of requests
      --resources stringArray                         The resources of the job, it is a string in the format of cpu=1,memory=1Gi,nvidia.com/gpu=1, it will be set to the limits and requests of the container.
      --restart-policy string                         The job restart policy (default "on-failure")
      --runtime-envs baizectl data ls --runtime-env   The runtime environment to use for the job, you can use baizectl data ls --runtime-env to get the runtime environment
      --shm-size int32                                The shared memory size of the job, default is 0, which means no shared memory, if set to more than 0, the job will use the shared memory, the unit is MiB
      --tensorboard-log-dir string                    The tensorboard log directory, if set, the job will automatically start tensorboard, else not. The format is /path/to/log, you can use relative path in notebook.
      --tensorflow                                    Tensorflow Job, has higher priority than --job-type
      --workers int                                   The workers of the job, default is 1, which means single worker, if set to more than 1, the job will be distributed. (default 1)
      --working-dir string                            The working directory of job container, if in notebook mode, the default is the directory of the current file
```

!!! note

    Explanation of command parameters for submitting jobs:

    - --name: Job name. If empty, it will be auto-generated.
    - --image: Image name. This must be specified.
    - --priority: Job priority, supporting high=`baize-high-priority`, medium=`baize-medium-priority`,
      low=`baize-low-priority`.
    - --resources: Job resources, formatted as `cpu=1 memory=1Gi,nvidia.com/gpu=1`.
    - --workers: Number of job worker nodes. The default is 1. When set to greater than 1,
      the job will run in a distributed manner.
    - --queue: Job queue. Queue resources need to be created in advance.
    - --working-dir: Working directory. In Notebook mode, the current file directory will be used by default.
    - --datasets: Dataset, formatted as `datasetName:mountPath`, for example `mnist:/data/mnist`.
    - --shm-size: Shared memory size. This can be enabled for distributed training jobs,
      indicating the use of shared memory, with units in MiB.
    - --labels: Job labels, formatted as `key=value`.
    - --max-retries: Maximum retry count. The number of times to retry the job upon failure.
      The job will restart upon failure. Default is unlimited.
    - --max-run-duration: Maximum run duration. The job will be terminated by the system
      if it exceeds the specified run time. Default is unlimited.
    - --restart-policy: Restart policy, supporting `on-failure`, `never`, `always`. The default is `on-failure`.
    - --from-notebook: Whether to read configurations from the Notebook.
      Supports `auto`, `true`, `false`, with the default being `auto`.

##### Example of a PyTorch Single-Node Job

Example of submitting a training job. Users can modify parameters based on their actual needs.
Below is an example of creating a PyTorch job:

```bash
baizectl job submit --name demojob-v2 -t PYTORCH \
    --image release.daocloud.io/baize/baize-notebook:v0.5.0 \
    --priority baize-high-priority \
    --resources cpu=1,memory=1Gi \
    --workers 1 \
    --queue default \
    --working-dir /data \
    --datasets fashion-mnist:/data/mnist \
    --labels job_type=pytorch \
    --max-retries 3 \
    --max-run-duration 60 \
    --restart-policy on-failure \
    -- sleep 1000
```

##### Example of a Distributed PyTorch Job

Example of submitting a training job.
You can modify parameters based on their actual needs.
Below is an example of creating a distributed PyTorch job:

```bash
baizectl job submit --name demojob-v2 -t PYTORCH \
    --image release.daocloud.io/baize/baize-notebook:v0.5.0 \
    --priority baize-high-priority \
    --resources cpu=1,memory=1Gi \
    --workers 2 \   # Multiple job replicas will automatically create a distributed job.
    --shm-size 1024 \
    --queue default \
    --working-dir /data \
    --datasets fashion-mnist:/data/mnist \
    --labels job_type=pytorch \
    --max-retries 3 \
    --max-run-duration 60 \
    --restart-policy on-failure \
    -- sleep 1000
```

##### Example of a TensorFlow Job

Use the `-t` parameter to specify the job type. Below is an example of creating a TensorFlow job:

```bash
baizectl job submit --name demojob-v2 -t TENSORFLOW \
    --image release.daocloud.io/baize/baize-notebook:v0.5.0 \
    --priority baize-high-priority \
    --from-notebook auto \
    --workers 1 \
    --queue default \
    --working-dir /data \
    --datasets fashion-mnist:/data/mnist \
    --labels job_type=pytorch \
    --max-retries 3 \
    --max-run-duration 60 \
    --restart-policy on-failure \
    -- sleep 1000
```

You can also use the `--job-type` or `--tensorflow` parameter to specify the job type.

##### Example of a Paddle Job

```bash
baizectl job submit --name demojob-v2 -t PADDLE \
    --image release.daocloud.io/baize/baize-notebook:v0.5.0 \
    --priority baize-high-priority \
    --queue default \
    --working-dir /data \
    --datasets fashion-mnist:/data/mnist \
    --labels job_type=pytorch \
    --max-retries 3 \
    --max-run-duration 60 \
    --restart-policy on-failure \
    -- sleep 1000
```

#### View Job List

`baizectl job` supports viewing the job list using the `ls` command. By default,
it displays `pytorch` jobs, but users can specify the job type using the `-t` parameter.

```bash
(base) jovyan@den-0:~$ baizectl job ls  # View pytorch jobs by default
 NAME        TYPE     PHASE      DURATION  COMMAND    
 demong      PYTORCH  SUCCEEDED  1m2s      sleep 60   
 demo-sleep  PYTORCH  RUNNING    1h25m28s  sleep 7200 
(base) jovyan@den-0:~$ baizectl job ls demo-sleep  # View a specific job
 NAME        TYPE     PHASE      DURATION  COMMAND     
 demo-sleep  PYTORCH  RUNNING    1h25m28s  sleep 7200 
(base) jovyan@den-0:~$ baizectl job ls -t TENSORFLOW   # View tensorflow jobs
 NAME       TYPE        PHASE    DURATION  COMMAND    
 demotfjob  TENSORFLOW  CREATED  0s        sleep 1000 
```

The job list uses `table` as the default display format. If you want to view more information,
you can use the `json` or `yaml` format, which can be specified using the `-o` parameter.

```bash
(base) jovyan@den-0:~$ baizectl job ls -t TENSORFLOW -o yaml
- baseConfig:
    args:
    - sleep
    - "1000"
    image: release.daocloud.io/baize/baize-notebook:v0.5.0
    labels:
      app: den
    podConfig:
      affinity: {}
      kubeEnvs:
      - name: CONDA_EXE
        value: /opt/conda/bin/conda
      - name: CONDA_PREFIX
        value: /opt/conda
      - name: CONDA_PROMPT_MODIFIER
        value: '(base) '
      - name: CONDA_SHLVL
        value: "1"
      - name: CONDA_DIR
        value: /opt/conda
      - name: CONDA_PYTHON_EXE
        value: /opt/conda/bin/python
      - name: CONDA_PYTHON_EXE
        value: /opt/conda/bin/python
      - name: CONDA_DEFAULT_ENV
        value: base
      - name: PATH
        value: /opt/conda/bin:/opt/conda/condabin:/command:/opt/conda/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
      priorityClass: baize-high-priority
      queue: default
  creationTimestamp: "2024-06-16T07:47:27Z"
  jobSpec:
    runPolicy:
      suspend: true
    tfReplicaSpecs:
      Worker:
        replicas: 1
        restartPolicy: OnFailure
        template:
          metadata:
            creationTimestamp: null
          spec:
            affinity: {}
            containers:
            - args:
              - sleep
              - "1000"
              env:
              - name: CONDA_EXE
                value: /opt/conda/bin/conda
              - name: CONDA_PREFIX
                value: /opt/conda
              - name: CONDA_PROMPT_MODIFIER
                value: '(base) '
              - name: CONDA_SHLVL
                value: "1"
              - name: CONDA_DIR
                value: /opt/conda
              - name: CONDA_PYTHON_EXE
                value: /opt/conda/bin/python
              - name: CONDA_PYTHON_EXE
                value: /opt/conda/bin/python
              - name: CONDA_DEFAULT_ENV
                value: base
              - name: PATH
                value: /opt/conda/bin:/opt/conda/condabin:/command:/opt/conda/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
              image: release.daocloud.io/baize/baize-notebook:v0.5.0
              name: tensorflow
              resources:
                limits:
                  memory: 1Gi
                requests:
                  cpu: "1"
                  memory: 2Gi
              workingDir: /home/jovyan
            priorityClassName: baize-high-priority
  name: demotfjob
  namespace: ns-chuanjia-ndx
  phase: CREATED
  roleConfig:
    TF_WORKER:
      replicas: 1
      resources:
        limits:
          memory: 1Gi
        requests:
          cpu: "1"
          memory: 2Gi
  totalResources:
    limits:
      memory: "1073741824"
    requests:
      cpu: "1"
      memory: "2147483648"
  trainingConfig:
    restartPolicy: RESTART_POLICY_ON_FAILURE
  trainingMode: SINGLE
  type: TENSORFLOW
```

#### View Job Logs

`baizectl job` supports viewing job logs using the `logs` command.
You can view detailed information by using `baizectl job logs --help`.

```bash
(base) jovyan@den-0:~$ baizectl job logs --help
Show logs of a job

Usage:
  baizectl job logs <job-name> [pod-name] [flags]

Aliases:
  logs, log

Flags:
  -f, --follow            Specify if the logs should be streamed.
  -h, --help              help for logs
  -t, --job-type string   Job type: PYTORCH, TENSORFLOW, PADDLE (default "PYTORCH")
      --paddle            PaddlePaddle Job, has higher priority than --job-type
      --pytorch           Pytorch Job, has higher priority than --job-type
      --tail int          Lines of recent log file to display.
      --tensorflow        Tensorflow Job, has higher priority than --job-type
      --timestamps        Show timestamps
```

!!! note

    - The `--follow` parameter allows for real-time log viewing.
    - The `--tail` parameter specifies the number of log lines to view, with a default of 50 lines.
    - The `--timestamps` parameter displays timestamps.

Example of viewing job logs:

```bash
(base) jovyan@den-0:~$ baizectl job log -t TENSORFLOW tf-sample-job-v2-202406161632-evgrbrhn -f
2024-06-16 08:33:06.083766: I tensorflow/core/util/port.cc:110] oneDNN custom operations are on. You may see slightly different numerical results due to floating-point round-off errors from different computation orders. To turn them off, set the environment variable `TF_ENABLE_ONEDNN_OPTS=0`.
2024-06-16 08:33:06.086189: I tensorflow/tsl/cuda/cudart_stub.cc:28] Could not find cuda drivers on your machine, GPU will not be used.
2024-06-16 08:33:06.132416: I tensorflow/tsl/cuda/cudart_stub.cc:28] Could not find cuda drivers on your machine, GPU will not be used.
2024-06-16 08:33:06.132903: I tensorflow/core/platform/cpu_feature_guard.cc:182] This TensorFlow binary is optimized to use available CPU instructions in performance-critical operations.
To enable the following instructions: AVX2 AVX512F AVX512_VNNI FMA, in other operations, rebuild TensorFlow with the appropriate compiler flags.
2024-06-16 08:33:07.223046: W tensorflow/compiler/tf2tensorrt/utils/py_utils.cc:38] TF-TRT Warning: Could not find TensorRT
Model: "sequential"
_________________________________________________________________
 Layer (type)                Output Shape              Param #   
=================================================================
 Conv1 (Conv2D)              (None, 13, 13, 8)         80        
                                                                 
 flatten (Flatten)           (None, 1352)              0         
                                                                 
 Softmax (Dense)             (None, 10)                13530     
                                                                 
=================================================================
Total params: 13610 (53.16 KB)
Trainable params: 13610 (53.16 KB)
Non-trainable params: 0 (0.00 Byte)
...
```

#### Delete Jobs

`baizectl job` supports deleting jobs using the `delete` command and also supports
deleting multiple jobs simultaneously.

```bash
(base) jovyan@den-0:~$ baizectl job delete --help
Delete a job

Usage:
  baizectl job delete [flags]

Aliases:
  delete, del, remove, rm

Flags:
  -h, --help              help for delete
  -t, --job-type string   Job type: PYTORCH, TENSORFLOW, PADDLE (default "PYTORCH")
      --paddle            PaddlePaddle Job, has higher priority than --job-type
      --pytorch           Pytorch Job, has higher priority than --job-type
      --tensorflow        Tensorflow Job, has higher priority than --job-type
```

Here is an example to delete jobs:

```bash
(base) jovyan@den-0:~$ baizectl job ls
 NAME        TYPE     PHASE      DURATION  COMMAND    
 demong      PYTORCH  SUCCEEDED  1m2s      sleep 60   
 demo-sleep  PYTORCH  RUNNING    1h20m51s  sleep 7200 
 demojob     PYTORCH  FAILED     16m46s    sleep 1000 
 demojob-v2  PYTORCH  RUNNING    3m13s     sleep 1000 
 demojob-v3  PYTORCH  CREATED    0s        sleep 1000 
(base) jovyan@den-0:~$ baizectl job delete demojob      # delete a job
Delete job demojob in ns-chuanjia-ndx successfully
(base) jovyan@den-0:~$ baizectl job delete demojob-v2 demojob-v3     # delete several jobs
Delete job demojob-v2 in ns-chuanjia-ndx successfully
Delete job demojob-v3 in ns-chuanjia-ndx successfully
```

#### Restart Jobs

`baizectl job` supports restarting jobs using the `restart` command.
You can view detailed information by using `baizectl job restart --help`.

```bash
(base) jovyan@den-0:~$ baizectl job restart --help
restart a job

Usage:
  baizectl job restart [flags] job

Aliases:
  restart, rerun

Flags:
  -h, --help              help for restart
  -t, --job-type string   Job type: PYTORCH, TENSORFLOW, PADDLE (default "PYTORCH")
      --paddle            PaddlePaddle Job, has higher priority than --job-type
      --pytorch           Pytorch Job, has higher priority than --job-type
      --tensorflow        Tensorflow Job, has higher priority than --job-type
```

### Dataset Management

`baizectl` supports managing datasets. Currently, it supports viewing the dataset list,
making it convenient to quickly bind datasets during job training.

```bash
(base) jovyan@den-0:~$ baizectl data 
Management datasets

Usage:
  baizectl data [flags]
  baizectl data [command]

Aliases:
  data, dataset, datasets, envs, runtime-envs

Available Commands:
  ls          List datasets

Flags:
  -h, --help            help for data
  -o, --output string   Output format. One of: table, json, yaml (default "table")
      --page int        Page number (default 1)
      --page-size int   Page size (default -1)
      --search string   Search query
      --sort string     Sort order
      --truncate int    Truncate output to the given length, 0 means no truncation (default 50)

Use "baizectl data [command] --help" for more information about a command.
```

#### View Datasets

`baizectl data` supports viewing the datasets using the `ls` command.
By default, it displays in `table` format, but users can specify the output format using the `-o` parameter.

```bash
(base) jovyan@den-0:~$ baizectl data ls
 NAME             TYPE  URI                                                    PHASE 
 fashion-mnist    GIT   https://gitee.com/samzong_lu/fashion-mnist.git         READY 
 sample-code      GIT   https://gitee.com/samzong_lu/training-sample-code....  READY 
 training-output  PVC   pvc://training-output                                  READY 
```

When submitting a training job, you can specify the dataset using the `-d` or `--datasets` parameter, for example:

```bash
baizectl job submit --image release.daocloud.io/baize/baize-notebook:v0.5.0 \
    --datasets sample-code:/home/jovyan/code \
    -- sleep 1000
```

To mount multiple datasets simultaneously, you can use the following format:

```bash
baizectl job submit --image release.daocloud.io/baize/baize-notebook:v0.5.0 \
    --datasets sample-code:/home/jovyan/code fashion-mnist:/home/jovyan/data \
    -- sleep 1000
```

#### View Dependencies (Environment)

The environment `runtime-env` is a unique environment management capability of DCE.
By decoupling the dependencies required for model development, training tasks, and inference,
it offers a more flexible way to manage dependencies without the need to repeatedly
build complex Docker images. You simply need to select the appropriate environment.

Additionally, `runtime-env` supports hot updates and dynamic upgrades, allowing you
to update environment dependencies without rebuilding the image.

`baizectl data` supports viewing the environment list using the `runtime-env` command.
By default, it displays in `table` format, but users can specify the output format using the `-o` parameter.

```bash
(base) jovyan@den-0:~$ baizectl data ls --runtime-env 
 NAME               TYPE   URI                                                    PHASE      
 fashion-mnist      GIT    https://gitee.com/samzong_lu/fashion-mnist.git         READY      
 sample-code        GIT    https://gitee.com/samzong_lu/training-sample-code....  READY      
 training-output    PVC    pvc://training-output                                  READY      
 tensorflow-sample  CONDA  conda://python?version=3.12.3                          PROCESSING 
```

When submitting a training job, you can specify the environment using the `--runtime-env` parameter:

```bash
baizectl job submit --image release.daocloud.io/baize/baize-notebook:v0.5.0 \
    --runtime-env tensorflow-sample \
    -- sleep 1000
```

---

## Advanced Usage

`baizectl` supports more advanced usage, such as generating auto-completion scripts,
using specific clusters and namespaces, and using specific workspaces.

### Generating Auto-Completion Scripts

```bash
baizectl completion bash > /etc/bash_completion.d/baizectl
```

The above command generates an auto-completion script for `bash` and saves it to the
`/etc/bash_completion.d/baizectl` directory. You can load the auto-completion script
by using `source /etc/bash_completion.d/baizectl`.

### Using Specific Clusters and Namespaces

```bash
baizectl job ls --cluster my-cluster --namespace my-namespace
```

This command will list all jobs in the `my-namespace` namespace within the `my-cluster` cluster.

### Using Specific Workspaces

```bash
baizectl job ls --workspace 123
```

## Frequently Asked Questions

- **Question**: Why can't I connect to the server?

    **Solution**: Check if the `--server` parameter is set correctly and ensure that the network connection
    is stable. If the server uses a self-signed certificate, you can use `--skip-tls-verify` to skip
    TLS certificate verification.
  
- **Question**: How can I resolve insufficient permissions issues?

    **Solution**: Ensure that you are using the correct `--token` parameter to log in and
    check if the current user has the necessary permissions for the operation.

- **Question**: Why can't I list the datasets?

    **Solution**: Check if the namespace and workspace are set correctly and ensure that
    the current user has permission to access these resources.

---

## Conclusion

With this guide, you can quickly get started with `baizectl` commands and efficiently manage AI platform
resources in practical applications. If you have any questions or issues, it is recommended to
use `baizectl [command] --help` to check more detailed information.
