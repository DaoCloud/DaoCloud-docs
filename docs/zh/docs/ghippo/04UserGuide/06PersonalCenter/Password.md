# 访问密钥

每个用户登录或访问资源都需要一个访问密钥。参照以下步骤获取密钥、token 并访问 API。 

## 获取密钥

登录 DCE 5.0，在右上角的下拉菜单中找到`个人中心`，可以在`平台设置`页面管理账户的访问密钥对。

![img](../../images/platform01.png)

!!! note

    若进入到该页面中无密钥，则点击`创建密钥`按钮，最多可以创建 2 对密钥。

## 根据密钥对生成 token

!!! note

    token 有效期默认 3 天，可以在生成时修改参数 `cycle`。

生成 token 的请求 URL 为：

```shell
/api/v1/cube/key/token?ak=&sk=&cycle=
```

Method：GET

描述：根据密钥对生成 token，token 有效期根据 cycle 生成，默认为 3 天。

**请求参数**

| 参数名 | 说明     | 参数类型 | 是否必填 |
| :----- | :------- | :------- | :------- |
| ak     | 密钥对 Ak | string   | 是       |
| sk     | 密钥对 Sk | string   | 是       |
| cycle  | 生命周期 | int      | 否       |

**返回参数**

| 参数名 | 说明                               | 参数类型 |
| :----- | :--------------------------------- | :------- |
| token  | 可以用于访问DCE 5.0 OpenAPI的token | string   |

**请求示例**

```shell
curl https://demo-alpha.daocloud.io/apis/ghippo.io/v1alpha1/token?ak=0f70e597-31a7-4e34-a43c-400deadb4109&sk=1718672b-9c40-4538-a129-d9316a36ddff&cycle=7 -X GET 
```

**请求结果**

```json
{
  "token": "eyJhbGciOiJSUzI1NiIsImtpZCI6IkRKVjlBTHRBLXZ4MmtQUC1TQnVGS0dCSWc1cnBfdkxiQVVqM2U3RVByWnMiLCJ0eXAiOiJKV1QifQ.eyJleHAiOjE2NjE0MTU5NjksImlhdCI6MTY2MDgxMTE2OSwiaXNzIjoiZ2hpcHBvLmlvIiwic3ViIjoiZjdjOGIxZjUtMTc2MS00NjYwLTg2MWQtOWI3MmI0MzJmNGViIiwicHJlZmVycmVkX3VzZXJuYW1lIjoiYWRtaW4iLCJncm91cHMiOltdfQ.RsUcrAYkQQ7C6BxMOrdD3qbBRUt0VVxynIGeq4wyIgye6R8Ma4cjxG5CbU1WyiHKpvIKJDJbeFQHro2euQyVde3ygA672ozkwLTnx3Tu-_mB1BubvWCBsDdUjIhCQfT39rk6EQozMjb-1X1sbLwzkfzKMls-oxkjagI_RFrYlTVPwT3Oaw-qOyulRSw7Dxd7jb0vINPq84vmlQIsI3UuTZSNO5BCgHpubcWwBss-Aon_DmYA-Et_-QtmPBA3k8E2hzDSzc7eqK0I68P25r9rwQ3DeKwD1dbRyndqWORRnz8TLEXSiCFXdZT2oiMrcJtO188Ph4eLGut1-4PzKhwgrQ"
}
```

## 使用 token 访问 API

在访问 DCE 5.0 openAPI 时，在请求中加上请求头 `Authorization:Bearer ${token}` 以标识访问者的身份，其中 `${token}` 是上一步中获取到的 token 值，具体接口信息参见[接口文档]()。

**请求示例**

```sh
curl -X GET -H 'Authorization:Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IkRKVjlBTHRBLXZ4MmtQUC1TQnVGS0dCSWc1cnBfdkxiQVVqM2U3RVByWnMiLCJ0eXAiOiJKV1QifQ.eyJleHAiOjE2NjE0MTU5NjksImlhdCI6MTY2MDgxMTE2OSwiaXNzIjoiZ2hpcHBvLmlvIiwic3ViIjoiZjdjOGIxZjUtMTc2MS00NjYwLTg2MWQtOWI3MmI0MzJmNGViIiwicHJlZmVycmVkX3VzZXJuYW1lIjoiYWRtaW4iLCJncm91cHMiOltdfQ.RsUcrAYkQQ7C6BxMOrdD3qbBRUt0VVxynIGeq4wyIgye6R8Ma4cjxG5CbU1WyiHKpvIKJDJbeFQHro2euQyVde3ygA672ozkwLTnx3Tu-_mB1BubvWCBsDdUjIhCQfT39rk6EQozMjb-1X1sbLwzkfzKMls-oxkjagI_RFrYlTVPwT3Oaw-qOyulRSw7Dxd7jb0vINPq84vmlQIsI3UuTZSNO5BCgHpubcWwBss-Aon_DmYA-Et_-QtmPBA3k8E2hzDSzc7eqK0I68P25r9rwQ3DeKwD1dbRyndqWORRnz8TLEXSiCFXdZT2oiMrcJtO188Ph4eLGut1-4PzKhwgrQ' https://demo-dev.daocloud.io/api/v1/cube/proxy/clusters/pivot-cluster/api/v1/pods -k
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
