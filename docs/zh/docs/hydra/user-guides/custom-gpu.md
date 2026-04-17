# 自定义 GPU 类型

大模型服务平台支持通过修改 GPU 配置文件，自定义 GPU 类型，以满足不同硬件厂商和 GPU 型号的需求。本文档将介绍如何配置自定义 GPU，并以华为昇腾 910B GPU 为例进行说明。

## 概述

大模型服务平台内置了多种 GPU 类型的支持，包括 NVIDIA GPU、NVIDIA vGPU、MetaX GPU 和昇腾 910 等。当需要支持新的 GPU
类型时，可以通过 hydra-gpu-configs 配置项来扩展。

配置结构
自定义 GPU 配置包含以下主要部分：


gpu_type: GPU 类型标识符

vendor: GPU 厂商

kpanda_gpu_type: 在 Kpanda 中的 GPU 类型标识

gpu_resource_template_config: GPU 资源模板配置

gpu_parsing_config: GPU 解析配置


配置示例：华为昇腾 910B GPU

1. 在 Hydra Helm Chart 中配置
通过编辑 hydra-gpu-configs ConfigMap 添加自定义 GPU 类型（此处昇腾已经内置可跳过）：
apiVersion: v1
kind: ConfigMap
metadata:
  name: hydra-gpu-configs
  namespace: hydra-system
data:
  gpu-configs.yaml: |
    gpu_configs:
      # 内置 GPU 配置（nvidia-gpu, nvidia-vgpu, metax-gpu, ascend-gpu-910, cpu）
      # ...

      # 扩展示例：添加 Ascend 910B GPU
      - gpu_name: ascend-gpu-910b
        gpu_type: ascend-gpu-910b
        vendor: huawei
        kpanda_gpu_type: Ascend-910B
        gpu_resource_template_config:
          gpu_per_node:
            key: huawei.com/Ascend910B
        gpu_parsing_config:
          memory_parse_rules:
            fixed_capacity: 65536  # 64GB in MB
          per_node_parse_rules:
            direct_node_status_allocatable: true

2. 在 Hydra Agent 中配置部署模板
在 manifests/hydra-agent/values.yaml 中添加对应的部署模板：
global:
  config:
    deployment_templates:
      # 其他配置...
      # Ascend GPU 910B
      - match_runtimes: [ 'vllm' ]
        match_gpu_types: [ ascend-gpu-910b ]
        container_template:
          image:
            registry: swr.cn-central-221.ovaijisuan.com
            repository: mindspore/mindspore-serving
            tag: 2.3.1-910b
          env:
            - name: ASCEND_RT_VISIBLE_DEVICES
              value: "0"
            - name: ASCEND_AICPU_PATH
              value: /usr/local/Ascend/ascend-toolkit/latest

配置参数说明

GPU 基础配置


gpu_type: 自定义的 GPU 类型标识符，用于在系统中唯一标识该 GPU 类型

vendor: GPU 厂商名称

kpanda_gpu_type: 在 Kpanda 集群管理中使用的 GPU 类型标识


GPU 资源模板配置


gpu_per_node.key: GPU 每节点数量的 Kubernetes 资源键名，通常由厂商定义

gpu_memory.key: GPU 显存资源的 Kubernetes 资源键名（可选）


GPU 解析配置

显存解析规则 (memory_parse_rules)


fixed_capacity: 固定显存容量（MB），适用于所有该类型 GPU 都有相同显存的情况

memory_label_key: 从节点标签中解析显存信息的键名

direct_parse_mb: 是否直接按 MB 解析标签值

parse_as_quantity: 是否按 Kubernetes Quantity 格式解析

unit_conversions: 单位转换映射


每节点GPU数量解析规则 (per_node_parse_rules)


direct_node_status_allocatable: 是否直接从节点状态的 allocatable 资源中解析

fixed_capacity: 固定核心数量


使用场景

1. 固定显存容量的 GPU
对于显存容量固定的 GPU（如昇腾 910B 固定为 64GB），使用 fixed_capacity 配置：
gpu_parsing_config:
  memory_parse_rules:
    fixed_capacity: 65536  # 64GB in MB

2. 动态显存解析的 GPU
对于需要从节点标签动态解析显存的 GPU，使用 memory_label_key 配置：
gpu_parsing_config:
  memory_parse_rules:
    memory_label_key: "vendor.com/gpu.memory"
    direct_parse_mb: true
例如节点显存 8G 的 label ：vendor.com/gpu.memory: 8192