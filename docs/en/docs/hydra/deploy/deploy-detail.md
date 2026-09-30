---
hide:
  - toc
---

# Model Service Details

*[Hydra]: Internal codename for LLM Studio

After a model is deployed, you can authenticate with an API Key and call the unified inference endpoint,
integrating model capabilities into your own applications or pipelines. This page describes the authentication
method, request examples, and response field descriptions.

## Authentication

1. Service APIs use an API Key for authentication.
2. It is strongly recommended that developers store the API Key on the backend, and never expose it in
   client-side code or public environments.
3. All API requests should carry the API Key in the `Authorization` HTTP header, for example:

```http
Authorization: Bearer {API_KEY}
```

## API Call Example

- Endpoint: The POST request URL is `https://<region>.d.run/v1/chat/completions`.

### Example Request: Call the API with curl

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

Parameter descriptions:

- `model`: The access path name of the model service (for example, `u-8105f7322477/test`).
- `messages`: The conversation history list, containing the user input.
- `temperature`: Controls the randomness of the generated result. A higher value makes the output more random,
  while a lower value makes it more stable.

### API Response Example

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

Response field descriptions:

- `id`: The unique identifier of the generated result.
- `model`: The ID of the model service that was called.
- `choices`: An array of generated results.
- `usage`: Token usage for this call.

## SDK Call Examples

### Python Example

```python
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

print(response.choices[0].message.content)
```

### Node.js Example

```js
const OpenAI = require('openai');

const openai = new OpenAI({
  baseURL: 'https://sh-02.d.run/v1',
  apiKey: '<Your API Key here>',
});

async function getData() {
  const chatCompletion = await openai.chat.completions.create({
    model: 'u-8105f7322477/test',
    messages: [
      { role: 'user', content: 'hello!' },
      { role: 'user', content: 'how are you?' },
    ],
  });

  console.log(chatCompletion.choices[0].message.content);
}

getData();
```
