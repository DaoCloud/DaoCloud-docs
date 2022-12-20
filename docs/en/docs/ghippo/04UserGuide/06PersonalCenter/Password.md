# Access key

An access key is required for every user login or access to a resource. Follow the steps below to obtain the key, token and access the API.

## get key

Log in to DCE 5.0, find `Personal Center` in the drop-down menu in the upper right corner, and you can manage the access key pair of the account on the `Platform Settings` page.

![img](../../images/platform01.png)

!!! note

    If there is no key on this page, click the `Create Key` button to create up to 2 pairs of keys.

## Generate token based on key pair

!!! note

    The token is valid for 3 days by default, and the parameter `cycle` can be modified when it is generated.

The request URL for generating token is:

```shell
/api/v1/cube/key/token?ak=&sk=&cycle=
```

Method: GET

Description: Generate a token based on the key pair, and the validity period of the token is generated according to the cycle, which is 3 days by default.

**Request parameters**

| Parameter name | Description | Parameter type | Required |
| :----- | :------- | :------- | :------- |
| ak | key pair Ak | string | yes |
| sk | key pair Sk | string | yes |
| cycle | lifetime | int | no |

**return parameters**

| Parameter name | Description | Parameter type |
| :----- | :--------------------------------- | :------ - |
| token | Token that can be used to access DCE 5.0 OpenAPI | string |

**Request Example**

```shell
curl https://demo-alpha.daocloud.io/apis/ghippo.io/v1alpha1/token?ak=0f70e597-31a7-4e34-a43c-400deadb4109&sk=1718672b-9c40-4538-a129-d9316a36ddff&cycle=7 -X GET
```

**request result**

```json
{
  "token": "eyJhbGciOiJSUzI1NiIsImtpZCI6IkRKVjlBTHRBLXZ4MmtQUC1TQnVGS0dCSWc1cnBfdkxiQVVqM2U3RVByWnMiLCJ0eXAiOiJKV1QifQ.eyJleHAiOjE2NjE0MTU5NjksImlhdCI6MTY2MDgxMTE2OSwiaXNzIjoiZ2hpcHBvLmlvIiwic3ViIjoiZjdjOGIxZjUtMTc2MS00NjYwLTg2MWQtOWI3MmI0MzJmNGViIiwicHJlZmVycmVkX3VzZXJuYW1lIjoiYWRtaW4iLCJncm91cHMiOltdfQ.RsUcrAYkQQ7C6BxMOrdD3qbBRUt0VVxynIGeq4wyIgye6R8Ma4cjxG5CbU1WyiHKpvIKJDJbeFQHro2euQyVde3ygA672ozkwLTnx3Tu-_mB1BubvWCBsDdUjIhCQfT39rk6EQozMjb-1X1sbLwzkfzKMls-oxkjagI_RFrYlTVPwT3Oaw-qOyulRSw7Dxd7jb0vINPq84vmlQIsI3UuTZSNO5BCgHpubcWwBss-Aon_DmYA-Et_-QtmPBA3k8E2hzDSzc7eqK0I68P25r9rwQ3DeKwD1dbRyndqWORRnz8TLEXSiCFXdZT2oiMrcJtO188Ph4eLGut1-4PzKhwgrQ"
}
```

## Use token to access API

When accessing DCE 5.0 openAPI, add the request header `Authorization:Bearer ${token}` to the request to identify the identity of the visitor, where `${token}` is the token value obtained in the previous step, the specific interface information See [Interface Documentation]().

**Request Example**

```sh
curl -X GET -H 'Authorization:Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IkRKVjlBTHRBLXZ4MmtQUC1TQnVGS0dCSWc1cnBfdkxiQVVqM2U3RVByWnMiLCJ0eXAiOiJKV1QifQ.eyJleHAiOjE2NjE0MTU5NjksImlhdCI6MTY2MDgxMTE2OSwiaXNzIjoiZ2hpcHBvLmlvIiwic3ViIjoiZjdjOGIxZjUtMTc2MS00NjYwLTg2MWQtOWI3MmI0MzJmNGViIiwicHJlZmVycmVkX3VzZXJuYW1lIjoiYWRtaW4iLCJncm91cHMiOltdfQ.RsUcrAYkQQ7C6BxMOrdD3qbBRUt0VVxynIGeq4wyIgye6R8Ma4cjxG5CbU1WyiHKpvIKJDJbeFQHro2euQyVde3ygA672ozkwLTnx3Tu-_mB1BubvWCBsDdUjIhCQfT39rk6EQozMjb-1X1sbLwzkfzKMls-oxkjagI_RFrYlTVPwT3Oaw-qOyulRSw7Dxd7jb0vINPq84vmlQIsI3UuTZSNO5BCgHpubcWwBss-Aon_DmYA-Et_-QtmPBA3k8E2hzDSzc7eqK0I68P25r9rwQ3DeKwD1dbRyndqWORRnz8TLEXSiCFXdZT2oiMrcJtO188Ph4eLGut1-4PzKhwgrQ' https://demo-dev.daocloud.io/api/v1/cube/ proxy/clusters/pivot-cluster/api/v1/pods -k
```

**request result**

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