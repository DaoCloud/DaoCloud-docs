# Model Deployment

Model Service is a solution that allows you to quickly deploy open-source or fine-tuned large language models as callable services.  
With one-click deployment, it simplifies complex model management into a standardized service format, enabling compatibility with mainstream API calls and ensuring immediate usability.

- Model services allow users to invoke selected models to perform tasks such as text generation, image understanding, and image generation.
- Online model trials are supported.

![service](../images/service01.png)

Click the model service name to enter the service details page.  
The service detail page includes basic information, authentication methods, and API call examples.

![service](../images/service02.png)

## Basic Information

- **Model Service Name**: The display name used to identify the model service.
- **Model Access Name**: A unique path name used for calling the model service.
- **Model Service ID**: Identifier used for billing and tracking.
- **Base Model**: The underlying model used by this service.
- **Instance Count**: Number of service instances deployed.
- **Status**: Current running status of the service.

## Authentication

- **API-Key Authorization**:
    - All API requests require the `Authorization` field in the HTTP header to authenticate identity.
    - Format: `Authorization: Bearer {API_KEY}`
    - You can obtain your key via the “View My API Key” link on the page.

- **Security Tip**: Store your API key securely on your backend server and avoid exposing it in client-side code to prevent leaks.

## API Call Example

- **Endpoint**: Send a POST request to `https://sh-02.d.run/v1/chat/completions`

### Example Request: Call the API with `curl`

```shell
curl 'https://sh-02.d.run/v1/chat/completions' \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer <Your API Key here>" \
  -d '{
    "model": "u-8105f7322477/test",
    "messages": [{"role": "user", "content": "Say this is a test!"}],
    "temperature": 0.7
  }'
```

**Parameter descriptions** :

* `model`: The model’s access path (e.g., `u-8105f7322477/test`)

* `messages`: List of conversation history, e.g.:

    ```json
    [{"role": "user", "content": "Say this is a test!"}]
    ```

* `temperature`: Controls the randomness of the output. Higher values lead to more creative responses, lower values to more stable ones.

### Example Response

```json
{
  "id": "cmp-1d033c426254417b7b0675303b1d300",
  "object": "chat.completion",
  "created": 1733724462,
  "model": "u-8105f7322477/test",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "I am a large language model. How can I assist you today?"
      },
      "tool_calls": []
    }
  ],
  "usage": {
    "prompt_tokens": 25,
    "completion_tokens": 15,
    "total_tokens": 40
  }
}
```

**Response field descriptions**:

* `id`: Unique identifier for the generation result.
* `model`: The model service ID used.
* `choices`: Array of generated results.

  * `message`: The generated message.
  * `content`: The generated text content.
* `usage`: Token usage for this request:

  * `prompt_tokens`: Number of tokens in the user input.
  * `completion_tokens`: Number of tokens in the model output.
  * `total_tokens`: Total number of tokens used.

## Development Integration Examples

### Python Example

```python
# Compatible with OpenAI Python library v1.0.0 and above

from openai import OpenAI

client = OpenAI(
    base_url="https://sh-02.d.run/v1/",
    api_key="<Your API Key here>"
)

messages = [
    {"role": "user", "content": "hello!"},
    {"role": "user", "content": "Say this is test?"}
]

response = client.chat.completions.create(
    model="u-8105f7322477/test",
    messages=messages
)

content = response.choices[0].message.content

print(content)
```

### Node.js Example

```js
const OpenAI = require('openai');

const openai = new OpenAI({
  baseURL: 'https://sh-02.d.run/v1',
  apiKey: '<Your API Key here>',
});

async function getData() {
  try {
    const chatCompletion = await openai.chat.completions.create({
      model: 'u-8105f7322477/test',
      messages: [
        { role: 'user', content: 'hello!' },
        { role: 'user', content: 'how are you?' },
      ],
    });

    console.log(chatCompletion.choices[0].message.content);
  } catch (error) {
    if (error instanceof OpenAI.APIError) {
      console.error('API Error:', error.status, error.message);
      console.error('Error details:', error.error);
    } else {
      console.error('Unexpected error:', error);
    }
  }
}

getData();
```

## Scaling

If you encounter resource shortages or latency during model usage, you can scale the service.

In the model service list, click the **┇** icon on the right and select **Scale** from the dropdown.

![Scaling](../images/service03.png)

Enter the desired number of additional instances (e.g., 2) and click Confirm.

![Scaling](../images/service04.png)

## Deletion

1. In the model service list, click the **┇** icon on the right and select **Delete**.
2. Enter the name of the service to confirm, then click **Delete**.

![Delete Service](../images/service05.png)
