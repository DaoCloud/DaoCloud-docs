---
hide:
  - toc
---

# baizectl 命令行工具使用指南

---

## 概述

`baizectl` 是在 DCE 的智能算力模块中专门服务于模型开发者与数据科学家们使用的工具。
它提供了一系列命令来帮助用户管理分布式训练作业、查看任务状态、管理数据集等操作，同时支持
连接 Kubernetes 工作集群和 DCE 的工作空间，帮助用户更高效地使用和管理 Kubernetes 平台资源。

## 安装

目前，`baizectl` 已经集成在 DCE5 平台中，在智能算力中，创建 Notebook 后，即可在 Notebook 中直接使用。

## 基础介绍

### 基本信息

`baizectl` 命令的基本格式如下：

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

以上是 `baizectl` 的基本信息，用户可以通过 `baizectl --help` 查看帮助信息，或者通过 `baizectl [command] --help` 查看具体命令的帮助信息。

### 查看版本信息

`baizectl` 支持通过 `version` 命令查看版本信息。

```bash
(base) jovyan@den-0:~$ baizectl version 
baizectl version: v0.5.0, commit sha: ac0837c4
```

### 命令格式

`baizectl` 命令的基本格式如下：

```bash
baizectl [command] [flags]
```

其中，`[command]` 是具体的操作命令，如 `data`、`job` 等，`[flags]` 是可选的参数，用于指定操作的详细信息。

### 常用选项

- `--cluster string`：指定要操作的集群名称。
- `-h, --help`：显示帮助信息。
- `--mode string`：连接模式，可选值为 `auto`、`api`、`notebook`（默认值为 `auto`）。
- `-n, --namespace string`：指定操作的命名空间。如果未设置，将使用默认命名空间。
- `-s, --server string`：DCE5 访问基础 URL。
- `--skip-tls-verify`：跳过 TLS 证书验证。
- `--token string`：DCE5 访问令牌。
- `-w, --workspace int32`：指定操作的工作区 ID。

## 功能介绍

### 任务管理

baizectl 提供了一系列命令来管理分布式训练任务，包含了查看任务列表，提交任务、查看日志、重启任务、删除任务等。

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

#### 提交训练任务

`baizectl` 支持使用 `submit` 命令提交一个任务，用户可以通过 `baizectl job submit --help` 查看详细信息。

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
  -x, --from-notebook string                          Define whether to read the configuration of the current Notebook and directly create tasks, including images, resources, Dataset, etc.
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

##### 提交任务命令参数

!!! note

    --name: 任务名称，如果为空，则会自动生成
    --image: 镜像名称，必须指定
    --priority: 任务优先级，支持 高=`baize-high-priority`、中=`baize-medium-priority`、低=`baize-low-priority`
    --resources: 任务资源，格式为 `cpu=1 memory=1Gi,nvidia.com/gpu=1`
    --workers: 任务工作节点数，默认为 1，当设置大于 1 时，任务将会分布式运行
    --queue: 任务队列，需要提前创建队列资源
    --working-dir: 工作目录，如果在 Notebook 模式下，会默认使用当前文件目录
    --datasets: 数据集，格式为 `datasetName:mountPath`，例如 `mnist:/data/mnist`
    --shm-size: 共享内存大小，在分布式训练任务时，可以启用，表示使用共享内存，单位为 MiB
    --labels: 任务标签，格式为 `key=value`
    --max-retries: 最大重试次数，任务失败后重试次数，失败后会重启任务，默认不限制
    --max-run-duration: 最大运行时间，任务运行时间超过指定时间后，会被系统终止，默认不限制
    --restart-policy: 重启策略，支持 `on-failure`、`never`、`always`，默认为 `on-failure`
    --from-notebook: 是否从 Notebook 中读取配置，支持 `auto`、`true`、`false`，默认为 `auto`

##### PyTorch 单机任务示例

提交训练任务示例，用户可以根据实际需求修改参数，以下为创建一个 PyTorch 任务的示例：

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

##### PyTorch 分布式任务示例

提交训练任务示例，用户可以根据实际需求修改参数，以下为创建一个 PyTorch 任务的示例：

```bash
baizectl job submit --name demojob-v2 -t PYTORCH \
    --image release.daocloud.io/baize/baize-notebook:v0.5.0 \
    --priority baize-high-priority \
    --resources cpu=1,memory=1Gi \
    --workers 2 \   # 多任务副本会自动创建分布式任务
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

##### Tensorflow 任务示例

使用 `-t` 参数指定任务类型，以下为创建一个 Tensorflow 任务的示例：

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

也可以使用 `--job-type` 或者 `--tensorflow` 参数指定任务类型

##### Paddle 任务示例

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

#### 查看任务列表

`baizectl job` 支持通过 `ls` 命令查看任务列表，默认显示 `pytroch` 任务，用户可以通过 `-t` 指定任务类型。

```bash
(base) jovyan@den-0:~$ baizectl job ls  # 默认查看 pytorch 任务
 NAME        TYPE     PHASE      DURATION  COMMAND    
 demong      PYTORCH  SUCCEEDED  1m2s      sleep 60   
 demo-sleep  PYTORCH  RUNNING    1h25m28s  sleep 7200 
(base) jovyan@den-0:~$ baizectl job ls demo-sleep  # 查看指定任务
 NAME        TYPE     PHASE      DURATION  COMMAND     
 demo-sleep  PYTORCH  RUNNING    1h25m28s  sleep 7200 
(base) jovyan@den-0:~$ baizectl job ls -t TENSORFLOW   # 查看 tensorflow 任务
 NAME       TYPE        PHASE    DURATION  COMMAND    
 demotfjob  TENSORFLOW  CREATED  0s        sleep 1000 
```

任务列表默认情况下使用 `table` 作为展示形式，如果希望查看更多信息，可使用 `json` 或 `yaml` 格式展示，可以通过 `-o` 参数指定。

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

#### 查看任务日志

`baizectl job` 支持使用 `logs` 命令查看任务日志，用户可以通过 `baizectl job logs --help` 查看详细信息。

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

    - `--follow` 参数实时查看日志
    - `--tail` 参数指定查看日志的行数，默认为 50 行
    - `--timestamps` 参数显示时间戳

示例查看任务日志：

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

#### 删除任务

`baizectl job` 支持使用 `delete` 命令删除任务，并且同时支持删除多个任务。

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

示例删除任务：

```bash
(base) jovyan@den-0:~$ baizectl job ls
 NAME        TYPE     PHASE      DURATION  COMMAND    
 demong      PYTORCH  SUCCEEDED  1m2s      sleep 60   
 demo-sleep  PYTORCH  RUNNING    1h20m51s  sleep 7200 
 demojob     PYTORCH  FAILED     16m46s    sleep 1000 
 demojob-v2  PYTORCH  RUNNING    3m13s     sleep 1000 
 demojob-v3  PYTORCH  CREATED    0s        sleep 1000 
(base) jovyan@den-0:~$ baizectl job delete demojob      # 删除单个任务
Delete job demojob in ns-chuanjia-ndx successfully
(base) jovyan@den-0:~$ baizectl job delete demojob-v2 demojob-v3     # 删除多个任务
Delete job demojob-v2 in ns-chuanjia-ndx successfully
Delete job demojob-v3 in ns-chuanjia-ndx successfully
```

#### 重启任务

`baizectl job` 支持使用 `restart` 命令重启任务，用户可以通过 `baizectl job restart --help` 查看详细信息。

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

### 数据集管理

`baizectl` 支持管理数据集，目前支持查看数据集列表，方便在任务训练时，快速绑定数据集。

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

#### 查看数据集列表

`baizectl data` 支持通过 `ls` 命令查看数据集列表，默认显示 `table` 格式，用户可以通过 `-o` 参数指定输出格式。

```bash
(base) jovyan@den-0:~$ baizectl data ls
 NAME             TYPE  URI                                                    PHASE 
 fashion-mnist    GIT   https://gitee.com/samzong_lu/fashion-mnist.git         READY 
 sample-code      GIT   https://gitee.com/samzong_lu/training-sample-code....  READY 
 training-output  PVC   pvc://training-output                                  READY 
```

在提交训练任务时，可以使用 `-d` 或者 `--datasets` 参数指定数据集，例如：

```bash
baizectl job submit --image release.daocloud.io/baize/baize-notebook:v0.5.0 \
    --datasets sample-code:/home/jovyan/code \
    -- sleep 1000
```

同时挂载多个数据集，可以按照如下格式：

```bash
baizectl job submit --image release.daocloud.io/baize/baize-notebook:v0.5.0 \
    --datasets sample-code:/home/jovyan/code fashion-mnist:/home/jovyan/data \
    -- sleep 1000
```

#### 查看依赖库（环境）

环境 `runtime-env` 是 DCE 的特色环境管理能力，通过将模型开发、训练任务以及推理中所需的依赖库解耦，
提供了一种更加灵活的依赖库管理方式，无需重复构建复杂的 Docker 镜像，只需选择合适的环境即可。

同时 `runtime-env` 支持热更新，动态升级，无需重新构建镜像，即可更新环境依赖库。

`baizectl data` 支持通过 `runtime-env` 命令查看环境列表，默认显示 `table` 格式，用户可以通过 `-o` 参数指定输出格式。

```bash
(base) jovyan@den-0:~$ baizectl data ls --runtime-env 
 NAME               TYPE   URI                                                    PHASE      
 fashion-mnist      GIT    https://gitee.com/samzong_lu/fashion-mnist.git         READY      
 sample-code        GIT    https://gitee.com/samzong_lu/training-sample-code....  READY      
 training-output    PVC    pvc://training-output                                  READY      
 tensorflow-sample  CONDA  conda://python?version=3.12.3                          PROCESSING 
```

在提交训练任务时，可以使用 `--runtime-env` 参数指定环境，例如：

```bash
baizectl job submit --image release.daocloud.io/baize/baize-notebook:v0.5.0 \
    --runtime-env tensorflow-sample \
    -- sleep 1000
```

## 高级用法

baizectl 支持更多高级用法，例如自动补全脚本生成、使用特定集群和命名空间、使用特定工作空间等。

### 自动补全脚本生成

```bash
baizectl completion bash > /etc/bash_completion.d/baizectl
```

上述命令生成 `bash` 的自动补全脚本，并将其保存到 `/etc/bash_completion.d/baizectl` 目录中，用户可以通过 `source /etc/bash_completion.d/baizectl` 加载自动补全脚本。

### 使用特定集群和命名空间

```bash
baizectl job ls --cluster my-cluster --namespace my-namespace
```

该命令将列出 `my-cluster` 集群中 `my-namespace` 命名空间下的所有作业。

### 使用特定工作空间

```bash
baizectl job ls --workspace 123
```

## 常见问题

- **问题**：为什么无法连接到服务器？
  **解决方法**：检查 `--server` 参数是否正确设置，并确保网络连接正常。如果服务器使用自签名证书，可以使用 `--skip-tls-verify` 跳过 TLS 证书验证。
  
- **问题**：如何解决权限不足的问题？
  **解决方法**：确保使用正确的 `--token` 参数登录，并检查当前用户是否具有相应的操作权限。

- **问题**：为什么无法列出数据集？
  **解决方法**：检查命名空间和工作区是否正确设置，确保当前用户有权限访问这些资源。

## 结语

通过以上指南，用户可以快速上手 `baizectl` 命令，并在实际应用中高效地管理 AI 平台资源。如果有任何疑问或问题，建议参考 `baizectl [command] --help` 获取更多详细信息。
