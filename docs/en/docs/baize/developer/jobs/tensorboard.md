# Job Analysis

DCE 5.0 AI Lab provides important visualization analysis tools provided for the model development
process, used to display the training process and results of machine learning models. This document will
introduce the basic concepts of Job Analysis (Tensorboard), its usage in the AI Lab system,
and how to configure the log content of datasets.

!!! note

    Tensorboard is a visualization tool provided by TensorFlow, used to display the
    training process and results of machine learning models.
    It can help developers more intuitively understand the training dynamics of
    their models, analyze model performance, debug issues, and more.

<!-- add screenshot later -->

The role and advantages of Tensorboard in the model development process:

- **Visualize Training Process** : Display metrics such as training and validation loss, and accuracy
  through charts, helping developers intuitively observe the training effects of the model.
- **Debug and Optimize Models** : By viewing the weights and gradient distributions of different layers,
  help developers discover and fix issues in the model.
- **Compare Different Experiments** : Simultaneously display the results of multiple experiments,
  making it convenient for developers to compare the effects of different models and hyperparameter configurations.
- **Track Training Data** : Record the datasets and parameters used during training to
  ensure the reproducibility of experiments.

## How to Create Tensorboard

In the AI Lab system, we provide a convenient way to create and manage Tensorboard.
Here are the specific steps:

### Enable Tensorboard When Creating a Notebook

1. **Create a Notebook** : Create a new Notebook on the AI Lab platform.
2. **Enable Tensorboard** : On the Notebook creation page, enable the **Tensorboard**
   option and specify the dataset and log path.

    <!-- add screenshot later -->

### Enable Tensorboard After Creating and Completing a Distributed Job

1. **Create a Distributed Job** : Create a new distributed training job on the AI Lab platform.
2. **Configure Tensorboard** : On the job configuration page, enable the **Tensorboard**
   option and specify the dataset and log path.
3. **View Tensorboard After Job Completion** : After the job is completed, you can view
   the Tensorboard link on the job details page. Click the link to see the visualized results
   of the training process.

    <!-- add screenshot later -->

### Directly Reference Tensorboard in a Notebook

In a Notebook, you can directly start Tensorboard through code. Here is a sample code snippet:

```python
# Import necessary libraries
import tensorflow as tf
import datetime

# Define log directory
log_dir = "logs/fit/" + datetime.datetime.now().strftime("%Y%m%d-%H%M%S")

# Create Tensorboard callback
tensorboard_callback = tf.keras.callbacks.TensorBoard(log_dir=log_dir, histogram_freq=1)

# Build and compile model
model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(512, activation='relu'),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(10, activation='softmax')
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Train model and enable Tensorboard callback
model.fit(x_train, y_train, epochs=5, validation_data=(x_test, y_test), callbacks=[tensorboard_callback])
```

## How to Configure Dataset Log Content

When using Tensorboard, you can record and configure different datasets and log content.
Here are some common configuration methods:

### Configure Training and Validation Dataset Logs

While training the model, you can use TensorFlow's `tf.summary` API to record logs
for the training and validation datasets. Here is a sample code snippet:

```python
# Import necessary libraries
import tensorflow as tf

# Create log directories
train_log_dir = 'logs/gradient_tape/train'
val_log_dir = 'logs/gradient_tape/val'
train_summary_writer = tf.summary.create_file_writer(train_log_dir)
val_summary_writer = tf.summary.create_file_writer(val_log_dir)

# Train model and record logs
for epoch in range(EPOCHS):
    for (x_train, y_train) in train_dataset:
        # Training step
        train_step(x_train, y_train)
        with train_summary_writer.as_default():
            tf.summary.scalar('loss', train_loss.result(), step=epoch)
            tf.summary.scalar('accuracy', train_accuracy.result(), step=epoch)

    for (x_val, y_val) in val_dataset:
        # Validation step
        val_step(x_val, y_val)
        with val_summary_writer.as_default():
            tf.summary.scalar('loss', val_loss.result(), step=epoch)
            tf.summary.scalar('accuracy', val_accuracy.result(), step=epoch)
```

### Configure Custom Logs

In addition to logs for training and validation datasets, you can also record other
custom log content such as learning rate and gradient distribution. Here is a sample code snippet:

```python
# Record custom logs
with train_summary_writer.as_default():
    tf.summary.scalar('learning_rate', learning_rate, step=epoch)
    tf.summary.histogram('gradients', gradients, step=epoch)
```

## Tensorboard Management

In AI Lab, Tensorboards created through various methods are uniformly
displayed on the job analysis page, making it convenient for users to view and manage.

<!-- add screenshot later -->

Users can view information such as the link, status, and creation time of Tensorboard
on the job analysis page and directly access the visualized results of Tensorboard through the link.
