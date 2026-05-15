---
hide:
  - toc
---

# 模型服务详情

*[Hydra]: 大模型服务平台的开发代号

模型部署完成后，您可以通过 API Key 鉴权并调用统一推理接口，将模型能力接入自有应用或流水线。下文给出鉴权方式、请求示例与响应字段说明。

## 鉴权方式

1. Service API 使用 API Key 进行鉴权。
2. 强烈建议开发者将 API Key 保存在后端，不要暴露在客户端代码或公共环境中。
3. 所有 API 请求都应在 Authorization HTTP Header 中携带 API Key，例如：

```http
Authorization: Bearer {API_KEY}
```

## 调用 API 示例

- 请求地址：POST 请求地址为 `https://<region>.d.run/v1/chat/completions`

### 请求示例：使用 curl 调用 API

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

参数说明：

- `model`：模型服务的访问路径名称（如 `u-8105f7322477/test`）。
- `messages`：对话历史列表，包含用户输入。
- `temperature`：控制生成结果的随机性，值越高输出越随机，值越低输出越稳定。

### API 响应示例

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

响应字段说明：

- `id`：生成结果的唯一标识符。
- `model`：所调用的模型服务 ID。
- `choices`：模型生成结果数组。
- `usage`：本次调用的 Token 使用情况。

## SDK 调用示例

### Python 示例

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

### Node.js 示例

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

