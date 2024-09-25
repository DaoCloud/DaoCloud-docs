# Create Inference Service

The AI Lab currently offers Triton and vLLM as inference frameworks. Users can quickly start a high-performance inference service with simple configurations.

## Inference Service Console

<!-- add screenshot later -->

## Prepare Model Dataset

In AI Lab, we use datasets for managing model files. This makes it convenient to directly mount the model files trained in tasks to the inference service.

By default, it is recommended to use `NFS` or `S3` services to store model files.

Once you successfully create the service, we will automatically preheat the model files to the local cluster.
**The preheating process does not consume GPU resources.**

> Here, `nfs` is used as an example.

<!-- add screenshot later -->

## Creation

Currently, form-based creation is supported, allowing you to create services with field prompts in the interface.

<!-- add screenshot later -->

### Configure Queue

### Configure Model Path

Referencing the model location in the dataset shown in the above image, choose the following:

- The dataset is `nfs-models`, and the model path is: `THUDM/chatglm2-6b`

## Model Configuration

<!-- add screenshot later -->

### Configure Authentication Policy

Supports API key-based request authentication. Users can customize and add authentication parameters.

### Advanced Settings: Affinity Scheduling

Supports automated affinity scheduling based on GPU resources and other node configurations. It also allows users to customize scheduling policies.

## Access

The model inference service provides multiple access methods by default, enabling clients to interact with the inference service through different protocols. You can access the service in the following ways:

1. **HTTP/REST API**

   - Triton provides a REST-based API, allowing clients to perform model inference via HTTP POST requests.
   - Clients can send requests with JSON-formatted bodies containing input data and related metadata.

2. **gRPC API**

   - Triton also provides a gRPC interface, a high-performance, open-source, general-purpose RPC framework.
   - gRPC supports streaming, making it more efficient for handling large amounts of data.

3. **C++ and Python Client Libraries**

   - Triton offers client libraries for C++ and Python, making it more convenient to write client code in these languages.
   - The client libraries encapsulate the details of HTTP/REST and gRPC, providing simple function calls to perform inference.

Each access method has its specific use cases and advantages. For instance, HTTP/REST API is typically used for simple and cross-language scenarios, while gRPC is suitable for high-performance and low-latency applications. The C++ and Python client libraries offer richer functionality and better performance, ideal for deep integration in these language environments.

### API Access

#### HTTP Access

1. **Send HTTP POST Request**: Use tools like `curl` or HTTP client libraries (e.g., Python's `requests` library) to send POST requests to the Triton Server.

2. **Construct Request Body**: The request body usually contains the input data for inference and model-specific metadata.

3. **Specify Model Name**: In the request, specify the model name you want to access, e.g., `chatglm2-6b`.

4. **Set HTTP Headers**: Include metadata about the model inputs and outputs in the HTTP headers.

##### Example curl Command

```bash
curl -X POST http://<host>:8000/v2/models/chatglm2-6b/infer \
    -H 'Content-Type: application/octet-stream' \
    --data-binary @input_data
```

- `<host>` is the host address where the Triton Inference Server is running.
- `8000` is the default HTTP port for Triton; change it if configured differently.
- `input_data` is your model input data file.

#### gRPC Access

1. **Generate Client Code**: Use the model definition files provided by Triton (usually `.pbtxt` files) to generate gRPC client code.

2. **Create gRPC Client Instance**: Use the generated code to create a gRPC client instance.

3. **Send gRPC Request**: Construct a gRPC request that includes the model input data.

4. **Receive Response**: Wait for the server to process the request and receive the response.

##### Example gRPC Access Code

```python
from triton_client.grpc import *
from triton_client.utils import *

# Initialize gRPC client
try:
    triton_client = InferenceServerClient('localhost:8001')
except Exception as e:
    logging.error("failed to create gRPC client: " + str(e))

# Construct input data
model_name = 'chatglm2-6b'
input_data = ...  # Your model input data

# Create input and output
inputs = [InferenceServerClient.Input('input_names', input_data.shape, "TYPE")]
outputs = [InferenceServerClient.Output('output_names')]

# Send inference request
results = triton_client.infer(model_name, inputs, outputs)

# Get inference result
output_data = results.as_numpy('output_names')
```

- `localhost:8001` is the default gRPC port for Triton; change it if configured differently.
- `input_data` is your model input data, which needs to be preprocessed according to the model requirements.
- `TYPE` is the data type of the model input, such as `FP32` and `INT32`.

Please note that the above example code needs to be adjusted according to your specific model and environment. The format and content of the input data must also comply with the model's requirements.

<!-- ### Web UI Access (Coming Soon)

> Web UI access is under development, stay tuned. -->
