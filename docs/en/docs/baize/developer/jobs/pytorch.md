# Pytorch Jobs

Pytorch is an open-source deep learning framework that provides a flexible environment for training and deployment.
A Pytorch job is a job that uses the Pytorch framework.

In the AI Lab platform, we provide support and adaptation for Pytorch jobs. Through a graphical interface, you can quickly create Pytorch jobs and perform model training.

## Job Configuration

- Job types support both `Pytorch Single` and `Pytorch Distributed` modes.
- The runtime image already supports the Pytorch framework by default, so no additional installation is required.

## Job Runtime Environment

Here we use the `baize-notebook` base image and the `associated environment` as the basic runtime environment for the job.

> To learn how to create an environment, refer to [Environments](../dataset/environments.md).

## Create Jobs

### Pytorch Single Jobs

<!-- add screenshot later -->

1. Log in to the AI Lab platform, click **Job Center** in the left navigation bar to enter the **Jobs** page.
2. Click the **Create** button in the upper right corner to enter the job creation page.
3. Select the job type as `Pytorch Single` and click **Next** .
4. Fill in the job name and description, then click **OK** .

#### Parameters

- Start command: `bash`
- Command parameters:

```python
import torch
import torch.nn as nn
import torch.optim as optim

# Define a simple neural network
class SimpleNet(nn.Module):
    def __init__(self):
        super(SimpleNet, self).__init__()
        self.fc = nn.Linear(10, 1)

    def forward(self, x):
        return self.fc(x)

# Create model, loss function, and optimizer
model = SimpleNet()
criterion = nn.MSELoss()
optimizer = optim.SGD(model.parameters(), lr=0.01)

# Generate some random data
x = torch.randn(100, 10)
y = torch.randn(100, 1)

# Train the model
for epoch in range(100):
    # Forward pass
    outputs = model(x)
    loss = criterion(outputs, y)
    
    # Backward pass and optimization
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
    
    if (epoch + 1) % 10 == 0:
        print(f'Epoch [{epoch+1}/100], Loss: {loss.item():.4f}')

print('Training finished.')
```

#### Results

Once the job is successfully submitted, we can enter the job details to see the resource usage. From the upper right corner, go to **Workload Details** to view the log output during the training process.

```bash
[HAMI-core Warn(1:140244541377408:utils.c:183)]: get default cuda from (null)
[HAMI-core Msg(1:140244541377408:libvgpu.c:855)]: Initialized
Epoch [10/100], Loss: 1.1248
Epoch [20/100], Loss: 1.0486
Epoch [30/100], Loss: 0.9969
Epoch [40/100], Loss: 0.9611
Epoch [50/100], Loss: 0.9360
Epoch [60/100], Loss: 0.9182
Epoch [70/100], Loss: 0.9053
Epoch [80/100], Loss: 0.8960
Epoch [90/100], Loss: 0.8891
Epoch [100/100], Loss: 0.8841
Training finished.
[HAMI-core Msg(1:140244541377408:multiprocess_memory_limit.c:468)]: Calling exit handler 1
```

### Pytorch Distributed Jobs

1. Log in to the AI Lab platform, click **Job Center** in the left navigation bar to enter the **Jobs** page.
2. Click the **Create** button in the upper right corner to enter the job creation page.
3. Select the job type as `Pytorch Distributed` and click **Next**.
4. Fill in the job name and description, then click **OK**.

#### Parameters

- Start command: `bash`
- Command parameters:

```python
import os
import torch
import torch.distributed as dist
import torch.nn as nn
import torch.optim as optim
from torch.nn.parallel import DistributedDataParallel as DDP

class SimpleModel(nn.Module):
    def __init__(self):
        super(SimpleModel, self).__init__()
        self.fc = nn.Linear(10, 1)

    def forward(self, x):
        return self.fc(x)

def train():
    # Print environment information
    print(f'PyTorch version: {torch.__version__}')
    print(f'CUDA available: {torch.cuda.is_available()}')
    if torch.cuda.is_available():
        print(f'CUDA version: {torch.version.cuda}')
        print(f'CUDA device count: {torch.cuda.device_count()}')

    rank = int(os.environ.get('RANK', '0'))
    world_size = int(os.environ.get('WORLD_SIZE', '1'))
    
    print(f'Rank: {rank}, World Size: {world_size}')

    # Initialize distributed environment
    try:
        if world_size > 1:
            dist.init_process_group('nccl')
            print('Distributed process group initialized successfully')
        else:
            print('Running in non-distributed mode')
    except Exception as e:
        print(f'Error initializing process group: {e}')
        return

    # Set device
    try:
        if torch.cuda.is_available():
            device = torch.device(f'cuda:{rank % torch.cuda.device_count()}')
            print(f'Using CUDA device: {device}')
        else:
            device = torch.device('cpu')
            print('CUDA not available, using CPU')
    except Exception as e:
        print(f'Error setting device: {e}')
        device = torch.device('cpu')
        print('Falling back to CPU')

    try:
        model = SimpleModel().to(device)
        print('Model moved to device successfully')
    except Exception as e:
        print(f'Error moving model to device: {e}')
        return

    try:
        if world_size > 1:
            ddp_model = DDP(model, device_ids=[rank % torch.cuda.device_count()] if torch.cuda.is_available() else None)
            print('DDP model created successfully')
        else:
            ddp_model = model
            print('Using non-distributed model')
    except Exception as e:
        print(f'Error creating DDP model: {e}')
        return

    loss_fn = nn.MSELoss()
    optimizer = optim.SGD(ddp_model.parameters(), lr=0.001)

    # Generate some random data
    try:
        data = torch.randn(100, 10, device=device)
        labels = torch.randn(100, 1, device=device)
        print('Data generated and moved to device successfully')
    except Exception as e:
        print(f'Error generating or moving data to device: {e}')
        return

    for epoch in range(10):
        try:
            ddp_model.train()
            outputs = ddp_model(data)
            loss = loss_fn(outputs, labels)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
            
            if rank == 0:
                print(f'Epoch {epoch}, Loss: {loss.item():.4f}')
        except Exception as e:
            print(f'Error during training epoch {epoch}: {e}')
            break

    if world_size > 1:
        dist.destroy_process_group()

if __name__ == '__main__':
    train()
```

#### Number of Job Replicas

Note that `Pytorch Distributed` training jobs will create a group of `Master` and `Worker` training Pods,
where the `Master` is responsible for coordinating the training job, and the `Worker` is responsible for the actual training work.

!!! note

    In this demonstration: `Master` replica count is 1, `Worker` replica count is 2;
    Therefore, we need to set the replica count to 3 in the **Job Configuration** ,
    which is the sum of `Master` and `Worker` replica counts.
    Pytorch will automatically tune the roles of `Master` and `Worker`.

#### Results

Similarly, we can enter the job details to view the resource usage and the log output of each Pod.
