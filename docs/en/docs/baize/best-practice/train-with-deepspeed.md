---
hide:
  - toc
---

# Submit a DeepSpeed Training Task

According to the [DeepSpeed official documentation](https://www.deepspeed.ai/getting-started/),
it's recommended to modifying your code to implement the training task.

Specifically, you can use `deepspeed.init_distributed()` instead of `torch.distributed.init_process_group(...)`.
Then run the command using `torchrun` to submit it as a PyTorch distributed task,
which will allow you to run a DeepSpeed task.

Yes, you can use `torchrun` to run your DeepSpeed training script. `torchrun` is a utility provided by
PyTorch for distributed training. You can combine `torchrun` with the DeepSpeed API to start your training task.

Below is an example of running a DeepSpeed training script using `torchrun`:

1. Write the training script:

    ```python title="train.py"
    import torch
    import deepspeed
    from torch.utils.data import DataLoader
    
    # Load model and data
    model = YourModel()
    train_dataset = YourDataset()
    train_dataloader = DataLoader(train_dataset, batch_size=32)
    
    # Configure file path
    deepspeed_config = "deepspeed_config.json"
    
    # Create DeepSpeed training engine
    model_engine, optimizer, _, _ = deepspeed.initialize(
        model=model,
        model_parameters=model.parameters(),
        config_params=deepspeed_config
    )
    
    # Training loop
    for batch in train_dataloader:
        loss = model_engine(batch)
        model_engine.backward(loss)
        model_engine.step()
    ```

2. Create the DeepSpeed configuration file:

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

3. Run the training script using `torchrun` or `baizectl`:

    ```bash
    torchrun train.py
    ```
    
    In this way, you can combine PyTorch's distributed training capabilities with
    DeepSpeed's optimization technologies for more efficient training.
    You can use the `baizectl` command to submit a job in a notebook:
    
    ```bash
    baizectl job submit --pytorch --workers 2 -- torchrun train.py
    ```
