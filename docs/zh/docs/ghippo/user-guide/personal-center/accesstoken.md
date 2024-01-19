# 访问密钥

访问密钥（Access Key）可用于访问开放 API 和持续发布，用户可在个人中心参照以下步骤获取密钥并访问 API。

## 获取密钥

登录 DCE 5.0，在右上角的下拉菜单中找到 __个人中心__ ，可以在 __访问密钥__ 页面管理账号的访问密钥。

![ak list](https://docs.daocloud.io/daocloud-docs-images/docs/ghippo/images/platform02.png)

![created a key](https://docs.daocloud.io/daocloud-docs-images/docs/ghippo/images/platform03.png)

!!! info

    访问密钥信息仅显示一次。如果您忘记了访问密钥信息，您需要重新创建新的访问密钥。

## 使用密钥访问 API

在访问 DCE 5.0 openAPI 时，在请求中加上请求头 `Authorization:Bearer ${token}` 以标识访问者的身份，
其中 `${token}` 是上一步中获取到的密钥，具体接口信息参见 [OpenAPI 接口文档](https://docs.daocloud.io/openapi/index.html)。

**请求示例**

```bash
curl -X GET -H 'Authorization:Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IkRKVjlBTHRBLXZ4MmtQUC1TQnVGS0dCSWc1cnBfdkxiQVVqM2U3RVByWnMiLCJ0eXAiOiJKV1QifQ.eyJleHAiOjE2NjE0MTU5NjksImlhdCI6MTY2MDgxMTE2OSwiaXNzIjoiZ2hpcHBvLmlvIiwic3ViIjoiZjdjOGIxZjUtMTc2MS00NjYwLTg2MWQtOWI3MmI0MzJmNGViIiwicHJlZmVycmVkX3VzZXJuYW1lIjoiYWRtaW4iLCJncm91cHMiOltdfQ.RsUcrAYkQQ7C6BxMOrdD3qbBRUt0VVxynIGeq4wyIgye6R8Ma4cjxG5CbU1WyiHKpvIKJDJbeFQHro2euQyVde3ygA672ozkwLTnx3Tu-_mB1BubvWCBsDdUjIhCQfT39rk6EQozMjb-1X1sbLwzkfzKMls-oxkjagI_RFrYlTVPwT3Oaw-qOyulRSw7Dxd7jb0vINPq84vmlQIsI3UuTZSNO5BCgHpubcWwBss-Aon_DmYA-Et_-QtmPBA3k8E2hzDSzc7eqK0I68P25r9rwQ3DeKwD1dbRyndqWORRnz8TLEXSiCFXdZT2oiMrcJtO188Ph4eLGut1-4PzKhwgrQ' https://demo-dev.daocloud.io/apis/ghippo.io/v1alpha1/users?page=1&pageSize=10 -k
```

**请求结果**

```json
{
    "items": [
        {
            "id": "a7cfd010-ebbe-4601-987f-d098d9ef766e",
            "name": "a",
            "email": "",
            "description": "",
            "firstname": "",
            "lastname": "",
            "source": "locale",
            "enabled": true,
            "createdAt": "1660632794800",
            "updatedAt": "0",
            "lastLoginAt": ""
        }
    ],
    "pagination": {
        "page": 1,
        "pageSize": 10,
        "total": 1
    }
}
```
