---
hide:
  - toc
---

# 如何提交 DeepSpeed 训练任务

根据 [DeepSpeed 官方文档](https://www.deepspeed.ai/getting-started/)，我们推荐使用修改代码的方式实现。

即使用 `deepspeed.init_distributed()` 代替 `torch.distributed.init_process_group(...)`。
然后运行命令使用 `torchrun`，提交为 Pytorch 分布式任务，既可运行 DeepSpeed 任务。

是的，你可以使用 `torchrun` 运行你的 DeepSpeed 训练脚本。
`torchrun` 是 PyTorch 提供的一个实用工具，用于分布式训练。你可以结合 `torchrun` 和 DeepSpeed API 来启动你的训练任务。

以下是一个使用 `torchrun` 运行 DeepSpeed 训练脚本的示例：

1. 编写训练脚本：

    ```python title="train.py"
    import torch
    import deepspeed
    from torch.utils.data import DataLoader
    
    # 模型和数据加载
    model = YourModel()
    train_dataset = YourDataset()
    train_dataloader = DataLoader(train_dataset, batch_size=32)
    
    # 配置文件路径
    deepspeed_config = "deepspeed_config.json"
    
    # 创建 DeepSpeed 训练引擎
    model_engine, optimizer, _, _ = deepspeed.initialize(
        model=model,
        model_parameters=model.parameters(),
        config_params=deepspeed_config
    )
    
    # 训练循环
    for batch in train_dataloader:
        loss = model_engine(batch)
        model_engine.backward(loss)
        model_engine.step()
    ```

2. 创建 DeepSpeed 配置文件：

    ```json title="deepspeed_config.json"
    {
      "train_batch_size": 32,
      "gradient_accumulation_steps": 1,
      "fp16": {
        "enabled": true,
        "loss_scale": 0
      },
      "optimizer": {
        "type": "Adam",
        "params": {
          "lr": 0.00015,
          "betas": [0.9, 0.999],
          "eps": 1e-08,
          "weight_decay": 0
        }
      }
    }
    ```

3. 使用 `torchrun` 或者 `baizectl` 运行训练脚本：

    ```bash
    torchrun train.py
    ```
    
    通过这种方式，你可以结合 PyTorch 的分布式训练功能和 DeepSpeed 的优化技术，从而实现更高效的训练。
    您可以在 Notebook 中，使用 `baizectl` 提交命令：
    
    ```bash
    baizectl job submit --pytorch --workers 2 -- torchrun train.py
    ```
