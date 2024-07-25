# Fine-tune the ChatGLM3 Model by Using Intelligent Engine

This page uses the `ChatGLM3` model as an example to demonstrate how to use LoRA (Low-Rank Adaptation)
to fine-tune the ChatGLM3 model within the DCE 5.0 Intelligent Engine environment. The demo program is from the
[ChatGLM3](https://github.com/THUDM/ChatGLM3/blob/main/finetune_demo/lora_finetune.ipynb) official example.

The general process of fine-tuning is as follows:

<!-- add image later -->

## Environment Requirements

- GPU with at least 20GB memory, recommended RTX4090 or NVIDIA A/H series
- At least 200GB of available disk space
- At least 8-core CPU, recommended 16-core
- 64GB RAM, recommended 128GB

!!! info

    Before starting, ensure DCE 5.0 and [Intelligent Engine](../intro/install.md) are correctly installed,
    GPU queue resources are successfully initialized, and computing resources are sufficient.

## Prepare Data

Utilize the dataset management feature provided by DCE 5.0 Intelligent Engine to quickly preheat
and persist the data required for fine-tuning large models, reducing GPU resource occupation
due to data preparation, and improving resource utilization efficiency.

<!-- add image later -->

Create the required data resources on the dataset list page. These resources include
the ChatGLM3 code and data files, all of which can be managed uniformly through the dataset list.

### Code and Model Files

[ChatGLM3](https://github.com/THUDM/ChatGLM3) is a dialogue pre-training model jointly
released by [zhipuai.cn](https://www.zhipuai.cn/en/) and Tsinghua University KEG Lab.

First, pull the ChatGLM3 code repository and download the pre-training model for subsequent fine-tuning tasks.

<!-- add image later -->

DCE 5.0 Intelligent Engine will automatically preheat the data in the background to ensure
quick data access for subsequent tasks.

### AdvertiseGen Dataset

Domestic data can be directly obtained from
[Tsinghua Cloud](https://cloud.tsinghua.edu.cn/f/b3f119a008264b1cabd1/?dl=1)
using the `HTTP` data source method.

After creation, wait for the dataset to be preheated, which is usually
quick and depends on your network conditions.

### Fine-tune Output Data

You also need to prepare an empty dataset to store the model files output after
the fine-tuning task is completed. Here, create an empty dataset, using `PVC` as an example.

!!! warning

    Ensure to use a storage type that supports `ReadWriteMany` to allow quick access to resources for subsequent tasks.

## Set up Environment

For model developers, preparing the Python environment dependencies required for model development is crucial.
Traditionally, environment dependencies are either packaged directly into the development tool's image or
installed in the local environment, which can lead to inconsistency in environment dependencies and
difficulties in managing and updating dependencies.

DCE 5.0 Intelligent Engine provides environment management capabilities, decoupling Python environment
dependency package management from development tools and task images, solving dependency management
chaos and environment inconsistency issues.

Here, use the environment management feature provided by DCE 5.0 Intelligent Engine to
create the environment required for ChatGLM3 fine-tuning for subsequent use.

!!! warning

    1. The ChatGLM repository contains a `requirements.txt` file that includes
       the environment dependencies required for ChatGLM3 fine-tuning.
    2. This fine-tuning does not use the `deepspeed` and `mpi4py` packages.
       It is recommended to comment them out in the `requirements.txt` file to avoid compilation failures.

<!-- add image later -->

In the environment management list, you can quickly create a Python environment and complete
the environment creation through a simple form configuration; a Python 3.11.x environment is required here.

<!-- add image later -->

Since CUDA is required for this experiment, GPU resources need to be configured here
to preheat the necessary resource dependencies.

Creating the environment involves downloading a series of Python dependencies, and download speeds
may vary based on your location. Using a domestic mirror for acceleration can speed up the download.

## Use Notebook as IDE

DCE 5.0 Intelligent Engine provides Notebook as an IDE feature, allowing users to write, run, and view
code results directly in the browser. This is very suitable for development in data analysis,
machine learning, and deep learning fields.

You can use the JupyterLab Notebook provided by Intelligent Engine for the ChatGLM3 fine-tuning task.

### Create JupyterLab Notebook

<!-- add image later -->

In the Notebook list, you can create a Notebook according to the page operation guide. Note that you need to configure the corresponding Notebook resource parameters according to the resource requirements mentioned earlier to avoid resource issues affecting the fine-tuning process.

<!-- add image later -->

!!! note

    When creating a Notebook, you can directly mount the preloaded model code dataset and environment,
    greatly saving data preparation time.

#### Mount Dataset and Code

Note: The ChatGLM3 code files are mounted to the `/home/jovyan/ChatGLM3` directory, and you also need to
mount the `AdvertiseGen` dataset to the `/home/jovyan/ChatGLM3/finetune_demo/data/AdvertiseGen` directory
to allow the fine-tuning task to access the data.

<!-- add image later -->

#### Mount PVC to Model Output Folder

The model output location used this time is the `/home/jovyan/ChatGLM3/finetune_demo/output` directory.
You can mount the previously created `PVC` dataset to this directory, so the trained model can be saved
to the dataset for subsequent inference tasks.

After creation, you can see the Notebook interface where you can write, run, and view code results directly in the Notebook.

<!-- add image later -->

### Fine-tune ChatGLM3

Once in the Notebook, you can find the previously mounted dataset and code in the `File Browser`
option in the Notebook sidebar. Locate the ChatGLM3 folder.

You will find the fine-tuning code for ChatGLM3 in the `finetune_demo` folder.
Open the `lora_finetune.ipynb` file, which contains the fine-tuning code for ChatGLM3.

<!-- add image later -->

First, follow the instructions in the `README.md` file to understand the entire fine-tuning process.
It is recommended to read it thoroughly to ensure that the basic environment dependencies and
data preparation work are completed.

<!-- add image later -->

Open the terminal and use `conda` to switch to the preheated environment,
ensuring consistency with the JupyterLab Kernel for subsequent code execution.

<!-- add image later -->

### Preprocess Data

First, preprocess the `AdvertiseGen` dataset, standardizing the data to meet the
`Lora` pre-training format requirements. Save the processed data to the `AdvertiseGen_fix` folder.

```python
import json
from typing import Union
from pathlib import Path

def _resolve_path(path: Union[str, Path]) -> Path:
    return Path(path).expanduser().resolve()

def _mkdir(dir_name: Union[str, Path]):
    dir_name = _resolve_path(dir_name)
    if not dir_name.is_dir():
        dir_name.mkdir(parents=True, exist_ok=False)

def convert_adgen(data_dir: Union[str, Path], save_dir: Union[str, Path]):
    def _convert(in_file: Path, out_file: Path):
        _mkdir(out_file.parent)
        with open(in_file, encoding='utf-8') as fin:
            with open(out_file, 'wt', encoding='utf-8') as fout:
                for line in fin:
                    dct = json.loads(line)
                    sample = {'conversations': [{'role': 'user', 'content': dct['content']},
                                                {'role': 'assistant', 'content': dct['summary']}]}
                    fout.write(json.dumps(sample, ensure_ascii=False) + '\n')

    data_dir = _resolve_path(data_dir)
    save_dir = _resolve_path(save_dir)

    train_file = data_dir / 'train.json'
    if train_file is_file():
        out_file = save_dir / train_file.relative_to(data_dir)
        _convert(train_file, out_file)

    dev_file = data_dir / 'dev.json'
    if dev_file.is_file():
        out_file = save_dir / dev_file.relative_to(data_dir)
        _convert(dev_file, out_file)

convert_adgen('data/AdvertiseGen', 'data/AdvertiseGen_fix')
```

To save debugging time, you can reduce the number of entries in
`/home/jovyan/ChatGLM3/finetune_demo/data/AdvertiseGen_fix/dev.json` to 50.
The data is in JSON format, making it easy to process.

<!-- add image later -->

### Local LoRA Fine-tuning Test

After preprocessing the data, you can proceed with the fine-tuning test.
Configure the fine-tuning parameters in the `/home/jovyan/ChatGLM3/finetune_demo/configs/lora.yaml` file.
Key parameters to focus on include:

<!-- add image later -->

Open a new terminal window and use the following command for local fine-tuning testing.
Ensure that the parameter configurations and paths are correct:

```bash
!CUDA_VISIBLE_DEVICES=0 NCCL_P2P_DISABLE="1" NCCL_IB_DISABLE="1" python finetune_hf.py data/AdvertiseGen_fix ./chatglm3-6b configs/lora.yaml
```

In this command:

- `finetune_hf.py` is the fine-tuning script in the ChatGLM3 code
- `data/AdvertiseGen_fix` is your preprocessed dataset
- `./chatglm3-6b` is your pre-trained model path
- `configs/lora.yaml` is the fine-tuning configuration file

<!-- add image later -->

During fine-tuning, you can use the `nvidia-smi` command to check GPU memory usage:

<!-- add image later -->

After fine-tuning is complete, an `output` directory will be generated in the `finetune_demo` directory,
containing the fine-tuned model files. This way, the fine-tuned model files are saved to the
previously created `PVC` dataset.

## Submit Fine-tuning Tasks

After completing the local fine-tuning test and ensuring that your code and data are correct,
you can submit the fine-tuning task to the Intelligent Engine for large-scale training and fine-tuning tasks.

!!! note

    This is the recommended model development and fine-tuning process:
    first, conduct local fine-tuning tests to ensure that the code and data are correct.

### Submit Fine-tuning Tasks via UI

<!-- add image later -->

Use `Pytorch` to create a fine-tuning task. Select the resources of the cluster you need to use
based on your actual situation. Ensure to meet the resource requirements mentioned earlier.

<!-- add image later -->

- Image: You can directly use the model image provided by baizectl.
- Startup command: Based on your experience using LoRA fine-tuning in the Notebook,
  the code files and data are in the `/home/jovyan/ChatGLM3/finetune_demo` directory,
  so you can directly use this path:

    ```bash
    bash -c "cd /home/jovyan/ChatGLM3/finetune_demo && CUDA_VISIBLE_DEVICES=0 NCCL_P2P_DISABLE="1" NCCL_IB_DISABLE="1" python finetune_hf.py data/AdvertiseGen_fix ./chatglm3-6b configs/lora.yaml"
    ```

- Mount environment: This way, the preloaded environment dependencies can be used not only
  in the Notebook but also in the tasks.
- Dataset: Use the preheated dataset
    - Set the model output path to the previously created PVC dataset
    - Mount the `AdvertiseGen` dataset to the `/home/jovyan/ChatGLM3/finetune_demo/data/AdvertiseGen` directory
- Configure sufficient GPU resources to ensure the fine-tuning task runs smoothly

<!-- add image later -->

### Check Task Status

After successfully submitting the task, you can view the training progress of the task
in real-time in the task list. You can see the task status, resource usage, logs, and other information.

> View task logs

<!-- add image later -->

After the task is completed, you can view the fine-tuned model files in the
data output dataset for subsequent inference tasks.

### Submit Tasks via `baizectl`

DCE 5.0 Intelligent Engine's Notebook supports using the `baizectl` command-line tool without authentication.
If you prefer using CLI, you can directly use the `baizectl` command-line tool to submit tasks.

```bash
baizectl job submit --name finetunel-chatglm3 -t PYTORCH \
    --image release.daocloud.io/baize/baize-notebook:v0.5.0 \
    --priority baize-high-priority \
    --resources cpu=8,memory=16Gi,nvidia.com/gpu=1 \
    --workers 1 \
    --queue default \
    --working-dir /home/jovyan/ChatGLM3 \
    --datasets AdvertiseGen:/home/jovyan/ChatGLM3/finetune_demo/data/AdvertiseGen  \
    --datasets output:/home/jovyan/ChatGLM3/finetune_demo/output  \
    --labels job_type=pytorch \
    --restart-policy on-failure \
    -- bash -c "cd /home/jovyan/ChatGLM3/finetune_demo && CUDA_VISIBLE_DEVICES=0 NCCL_P2P_DISABLE="1" NCCL_IB_DISABLE="1" python finetune_hf.py data/AdvertiseGen_fix ./chatglm3-6b configs/lora.yaml"
```

For more information on using `baizectl`, refer to the
[baizectl Usage Documentation](../developer/notebooks/baizectl.md).

## Model Inference

After completing the fine-tuning task, you can use the fine-tuned model for inference tasks.
Here, you can use the inference service provided by Intelligent Engine to create an
inference service with the output model.

<!-- add image later -->

In the inference service list, you can create a new inference service.
When selecting the model, choose the previously output dataset and configure the model path.

<!-- add image later -->

Regarding model resource requirements and GPU resource requirements for inference services,
configure them based on the model size and inference concurrency. Refer to
the resource configuration of the previous fine-tuning tasks.

### Configure Model Runtime

Configuring the model runtime is crucial. Currently, DCE 5.0 Intelligent Engine supports
`vLLM` as the model inference service runtime, which can be directly selected.

!!! tip

    vLLM supports a wide range of large language models. Visit [vLLM](https://docs.vllm.ai)
    for more information. These models can be easily used within Intelligent Engine.

<!-- add image later -->

After creation, you can see the created inference service in the inference service list.
The model service list allows you to get the model's access address directly.

### Test the Model Service

Try using the `curl` command in the terminal to test the model service. Here,
you can see the returned results, enabling you to use the model service for inference tasks.

```bash
curl -X POST http://10.20.100.210:31118/v2/models/chatglm3-6b/generate \
  -d '{"text_input": "hello", "stream": false, "sampling_parameters": "{\"temperature\": 0.7, \"top_p\": 0.95, \'max_tokens\": 1024｝"｝'
```

<!-- add image later -->

## Wrap up

This page used `ChatGLM3` as an example to quickly introduce and get you started with
the **Intelligent Engine** for model fine-tuning, using `LoRA` to fine-tune the ChatGLM3 model.

DCE 5.0 Intelligent Engine provides a wealth of features to help model developers quickly conduct
model development, fine-tuning, and inference tasks. It also offers rich OpenAPI interfaces,
facilitating integration with third-party application ecosystems.
