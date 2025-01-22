# Tensorflow Jobs

Tensorflow, along with Pytorch, is a highly active open-source deep learning framework
that provides a flexible environment for training and deployment.

AI Lab provides support and adaptation for the Tensorflow framework.
You can quickly create Tensorflow jobs and conduct model training through graphical operations.

## Job Configuration

- The job types support both `Tensorflow Single` and `Tensorflow Distributed` modes.
- The runtime image already supports the Tensorflow framework by default,
  so no additional installation is required.

## Job Runtime Environment

Here, we use the `baize-notebook` base image and the `associated environment` as the basic runtime environment for jobs.

> For information on how to create an environment, refer to [Environment List](../dataset/environments.md).

## Creating a Job

### Example TFJob Single

<!-- add screenshot later -->

1. Log in to the AI Lab platform and click **Job Center** in the left navigation bar
   to enter the **Jobs** page.
2. Click the **Create** button in the upper right corner to enter the job creation page.
3. Select the job type as `Tensorflow Single` and click **Next** .
4. Fill in the job name and description, then click **OK** .

#### Pre-warming the Code Repository

Use **AI Lab** -> **Dataset List** to create a dataset and pull the code from a remote GitHub repository into the dataset. 
This way, when creating a job, you can directly select the dataset and mount the code into the job.

Demo code repository address: [https://github.com/d-run/training-sample-code/](https://github.com/d-run/training-sample-code/)

#### Parameters

- Launch command: Use `bash`
- Command parameters: Use `python /code/tensorflow/tf-single.py`

```python
"""
  pip install tensorflow numpy
"""

import tensorflow as tf
import numpy as np

# Create some random data
x = np.random.rand(100, 1)
y = 2 * x + 1 + np.random.rand(100, 1) * 0.1

# Create a simple model
model = tf.keras.Sequential([
    tf.keras.layers.Dense(1, input_shape=(1,))
])

# Compile the model
model.compile(optimizer='adam', loss='mse')

# Train the model, setting epochs to 10
history = model.fit(x, y, epochs=10, verbose=1)

# Print the final loss
print('Final loss: {' + str(history.history['loss'][-1]) +'}')

# Use the model to make predictions
test_x = np.array([[0.5]])
prediction = model.predict(test_x)
print(f'Prediction for x=0.5: {prediction[0][0]}')
```

#### Results

After the job is successfully submitted, you can enter the job details to see the resource usage. From the upper right corner, navigate to **Workload Details** to view log outputs during the training process.

### TFJob Distributed Job

1. Log in to **AI Lab** and click **Job Center** in the left navigation bar to enter the **Jobs** page.
2. Click the **Create** button in the upper right corner to enter the job creation page.
3. Select the job type as `Tensorflow Distributed` and click **Next**.
4. Fill in the job name and description, then click **OK**.

#### Example Job Introduction

<!-- add screenshot later -->

This job includes three roles: `Chief`, `Worker`, and `Parameter Server (PS)`.

- Chief: Responsible for coordinating the training process and saving model checkpoints.
- Worker: Executes the actual model training.
- PS: Used in asynchronous training to store and update model parameters.

Different resources are allocated to different roles. `Chief` and `Worker` use GPUs,
while `PS` uses CPUs and larger memory.

#### Parameters

- Launch command: Use `bash`
- Command parameters: Use `python /code/tensorflow/tensorflow-distributed.py`

```python
import os
import json
import tensorflow as tf

class SimpleModel(tf.keras.Model):
    def __init__(self):
        super(SimpleModel, self).__init__()
        self.fc = tf.keras.layers.Dense(1, input_shape=(10,))

    def call(self, x):
        return self.fc(x)

def train():
    # Print environment information
    print(f"TensorFlow version: {tf.__version__}")
    print(f"GPU available: {tf.test.is_gpu_available()}")
    if tf.test.is_gpu_available():
        print(f"GPU device count: {len(tf.config.list_physical_devices('GPU'))}")

    # Retrieve distributed training information
    tf_config = json.loads(os.environ.get('TF_CONFIG') or '{}')
    job_type = tf_config.get('job', {}).get('type')
    job_id = tf_config.get('job', {}).get('index')

    print(f"Job type: {job_type}, Job ID: {job_id}")

    # Set up distributed strategy
    strategy = tf.distribute.experimental.MultiWorkerMirroredStrategy()
    
    with strategy.scope():
        model = SimpleModel()
        loss_fn = tf.keras.losses.MeanSquaredError()
        optimizer = tf.keras.optimizers.SGD(learning_rate=0.001)

    # Generate some random data
    data = tf.random.normal((100, 10))
    labels = tf.random.normal((100, 1))

    @tf.function
    def train_step(inputs, labels):
        with tf.GradientTape() as tape:
            predictions = model(inputs)
            loss = loss_fn(labels, predictions)
        gradients = tape.gradient(loss, model.trainable_variables)
        optimizer.apply_gradients(zip(gradients, model.trainable_variables))
        return loss

    for epoch in range(10):
        loss = train_step(data, labels)
        if job_type == 'chief':
            print(f'Epoch {epoch}, Loss: {loss.numpy():.4f}')

if __name__ == '__main__':
    train()
```

#### Results

Similarly, you can enter the job details to view the resource usage and log outputs of each Pod.
