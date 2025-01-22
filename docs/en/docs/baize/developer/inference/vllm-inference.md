# Create Inference Service Using vLLM Framework

AI Lab supports using vLLM as an inference service, offering all the capabilities of vLLM while fully adapting to the OpenAI interface definition.

## Introduction to vLLM

vLLM is a fast and easy-to-use library for inference and services. It aims to significantly improve the throughput and memory efficiency of language model services in real-time scenarios. vLLM boasts several features in terms of speed and flexibility:

- Continuous batching of incoming requests.
- Efficiently manages attention keys and values memory using PagedAttention.
- Seamless integration with popular HuggingFace models.
- Compatible with OpenAI's API server.

## Prerequisites

Prepare model data: Manage the model code in dataset management and ensure that the data is successfully preloaded.

## Create Inference Service

1. Select the `vLLM` inference framework. In the model module selection, choose the pre-created model dataset `hdd-models` and fill in the `path` information where the model is located within the dataset.

    This guide uses the ChatGLM3 model for creating the inference service.

    <!-- add screenshot later -->

2. Configure the resources for the inference service and adjust the parameters for running the inference service.

    <!-- add screenshot later -->

    | Parameter Name | Description |
    | -- | -- |
    | GPU Resources | Configure GPU resources for inference based on the model scale and cluster resources. |
    | Allow Remote Code | Controls whether vLLM trusts and executes code from remote sources. |
    | LoRA | **LoRA** is a parameter-efficient fine-tuning technique for deep learning models. It reduces the number of parameters and computational complexity by decomposing the original model parameter matrix into low-rank matrices. </br> </br>  1. `--lora-modules`: Specifies specific modules or layers for low-rank approximation. </br>  2. `max_loras_rank`: Specifies the maximum rank for each adapter layer in the LoRA model. For simpler tasks, a smaller rank value can be chosen, while more complex tasks may require a larger rank value to ensure model performance. </br> 3. `max_loras`: Indicates the maximum number of LoRA layers that can be included in the model, customized based on model size and inference complexity. </br> 4. `max_cpu_loras`: Specifies the maximum number of LoRA layers that can be handled in a CPU environment. |
    | Associated Environment | Selects predefined environment dependencies required for inference. |

    !!! info

        For models that support LoRA parameters, refer to [vLLM Supported Models](https://docs.vllm.ai/en/latest/models/supported_models.html).

3. In the **Advanced Configuration** , support is provided for automated affinity scheduling based on GPU resources and other node configurations. Users can also customize scheduling policies.

## Verify Inference Service

Once the inference service is created, click the name of the inference service to enter the details and view the API call methods. Verify the execution results using Curl, Python, and Node.js.

Copy the `curl` command from the details and execute it in the terminal to send a model inference request. The expected output should be:

<!-- add screenshot later -->
