# Model Invocation

*[Hydra]: The codename for LLM Studio

Hydra offers two ways to host large models. You can choose either based on your needs:

- **MaaS by Token**: Token-based usage with shared resources. Users can invoke models without deploying their own instances.
- **Model Service**: Dedicated model instances for users, with unlimited API calls.

## Currently Supported Models and Hosting Methods

| Model Name                   | MaaS by Token | Model Service |
| ---------------------------- | ------------- | -------------- |
| 🔥 DeepSeek-R1               | ✅            |                |
| 🔥 DeepSeek-V3               | ✅            |                |
| Phi-4                        |               | ✅             |
| Phi-3.5-mini-instruct        |               | ✅             |
| Qwen2-0.5B-Instruct          |               | ✅             |
| Qwen2.5-7B-Instruct          | ✅            | ✅             |
| Qwen2.5-14B-Instruct         |               | ✅             |
| Qwen2.5-Coder-32B-Instruct   |               | ✅             |
| Qwen2.5-72B-Instruct-AWQ     | ✅            | ✅             |
| baichuan2-13b-Chat           |               | ✅             |
| Llama-3.2-11B-Vision-Instruct| ✅            | ✅             |
| glm-4-9b-chat                | ✅            | ✅             |

## Model Endpoint

A model endpoint is a URL or API address through which users can send requests to perform inference with the model.

| Invocation Type   | Endpoint         |
| ----------------- | ---------------- |
| MaaS by Token     | `chat.d.run`     |
| Model Service     | `<region>.d.run` |

## API Invocation Examples

### Using MaaS by Token

To invoke a model using MaaS by Token:

1. **Get an API Key**: Log in to the user console and [create a new API Key](./apikey.md).
2. **Set the Endpoint**: Set your SDK endpoint to `chat.d.run`.
3. **Call the Model**: Use the official model name and your API Key.

**Sample Code (Python)**:

```python
import openai

openai.api_key = "your-api-key"  # Replace with your actual API Key
openai.api_base = "https://chat.d.run"

response = openai.Completion.create(
  model="public/deepseek-r1",
  prompt="What is your name?"
)

print(response.choices[0].text)
```

### Using Dedicated Model Service

To invoke a self-deployed model instance:

1. **Deploy a Model Instance**: Deploy a model in a designated region, such as `sh-02`.
2. **Get an API Key**: Log in to the user console and create a new API Key.
3. **Set the Endpoint**: Replace the SDK endpoint with `<region>.d.run`, e.g., `sh-02.d.run`.
4. **Call the Model**: Use the official model name and your API Key.

**Sample Code (Python)**:

```python
import openai

openai.api_key = "your-api-key"  # Replace with your actual API Key
openai.api_base = "https://sh-02.d.run"  # Replace with your model region

response = openai.Completion.create(
  model="u-1100a15812cc/qwen2",  # Replace with your deployed model name
  prompt="What is your name?"
)

print(response.choices[0].text)
```

## Frequently Asked Questions

### Q1: How do I choose an invocation method?

* **MaaS by Token**: Best for lightweight or infrequent use cases.
* **Instance (Model Service)**: Ideal for high-performance, frequent usage scenarios.

### Q2: How do I view my API Key?

Log in to the user console and go to the API Key management page. See [API Key Management](apikey.md) for details.

### Q3: How do I get the model name?

* For **MaaS by Token**, the model name uses the format `public/<model-name>`, e.g., `public/deepseek-r1`, and can be found on the model details page.
* For **Model Service**, the model name includes your username, e.g., `u-1100a15812cc/qwen2`, and can be copied directly from the model list.
