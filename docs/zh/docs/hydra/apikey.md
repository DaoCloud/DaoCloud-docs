# API Key 管理

API Key 是调用模型服务的核心凭证，用于验证用户身份并保护数据安全。

![api keys](./images/apikey01.png)

## 功能说明

- API Key 作用：

    - API Key 是调用模型服务的必要凭证，用于身份验证
    - 通过 API Key，您可以安全地调用已部署的模型服务

- 安全提示：

    - 请妥善保管 API Key，避免暴露到客户端代码或公共环境中
    - 如果 API Key 泄露，请及时删除并重新生成新的 Key

## 创建 API Key

1. 在 **API Key 管理** 页面中，点击右上角的 **创建** 按钮
2. 在弹出的窗口中，填写 API Key 的名称（如 test-key），用于标识该 Key 的用途或所属项目
3. 点击 **确定** ，系统将生成一个新的 API Key

!!! note

    创建完成后请在首次显示时保存 API Key，后续不会再次显示完整密钥。

## 查看 API Key

- 在 API Key 列表中，会显示已创建的所有 API Key：
    - 名称：API Key 的标识名称，便于用户区分不同用途的 Key
    - API Key：部分显示密钥内容，仅用于参考
    - 创建时间：API Key 的生成时间
- 点击右上角的刷新 :material-refresh: 按钮可以更新 Key 列表

## 删除 API Key

1. 在列表中找到需要删除的 API Key。
2. 点击某一行，可以执行删除操作
3. 在弹窗中确认删除操作
4. 删除后，该 API Key 将立即失效，所有依赖于此 Key 的服务调用将被拒绝

## 使用 API Key 调用服务

在调用模型服务时，需在 HTTP 请求头中添加以下字段：

```http
Authorization: Bearer {API_KEY}
```

示例：

```shell
curl 'https://sh-02.d.run/v1/chat/completions' \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer sk-x1VDTAFB7Ra1hldATbncOa_dddVttDvRHQibTA-Oi7ucU" \
  -d '{
    "model": "u-8105f7322477/test",
    "messages": [{"role": "user", "content": "Hello, model!"}],
    "temperature": 0.7
  }'
```

## 注意事项

- API Key 数量限制：每个账号允许创建的 API Key 数量有限，请根据需要合理分配
- 密钥泄露处理：如果发现密钥泄露，请立即删除旧密钥并重新创建新密钥
- Key 的权限管理：不同的 API Key 可用于不同的项目或服务，便于权限隔离
- 定期更新密钥：为了安全性，建议定期删除旧 Key 并生成新 Key
