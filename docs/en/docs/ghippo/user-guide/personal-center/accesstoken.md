---
MTPE: windsonsea
date: 2024-01-11
---

# Access key

The access key can be used to access the openAPI and continuous delivery. Users can obtain the key and access the API by referring to the following steps in the personal center.

## Get key

Log in to DCE 5.0, find __Personal Center__ in the drop-down menu in the upper right corner, and you can manage the access key of the account on the __Access Keys__ page.

![key list](../../images/platform02.png)

![created a key](../../images/platform03.png)

!!! info

    Access key is displayed only once. If you forget your access key,
    you will need to create a new key.

## Use the key to access API

When accessing DCE 5.0 openAPI, add the header `Authorization:Bearer ${token}` to the request to identify the visitor, where `${token}` is the key obtained in the previous step. For the specific API, see [OpenAPI Documentation](https://docs.daocloud.io/openapi/).

**Request Example**

```bash
curl -X GET -H 'Authorization:Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IkRKVjlBTHRBLXZ4MmtQUC1TQnVGS0dCSWc1cnBfdkxiQVVqM2U3RVByWnMiLCJ0eXAiOiJKV1QifQ.eyJleHAiOjE2NjE0MTU5NjksImlhdCI6MTY2MDgxMTE2OSwiaXNzIjoiZ2hpcHBvLmlvIiwic3ViIjoiZjdjOGIxZjUtMTc2MS00NjYwLTg2MWQtOWI3MmI0MzJmNGViIiwicHJlZmVycmVkX3VzZXJuYW1lIjoiYWRtaW4iLCJncm91cHMiOltdfQ.RsUcrAYkQQ7C6BxMOrdD3qbBRUt0VVxynIGeq4wyIgye6R8Ma4cjxG5CbU1WyiHKpvIKJDJbeFQHro2euQyVde3ygA672ozkwLTnx3Tu-_mB1BubvWCBsDdUjIhCQfT39rk6EQozMjb-1X1sbLwzkfzKMls-oxkjagI_RFrYlTVPwT3Oaw-qOyulRSw7Dxd7jb0vINPq84vmlQIsI3UuTZSNO5BCgHpubcWwBss-Aon_DmYA-Et_-QtmPBA3k8E2hzDSzc7eqK0I68P25r9rwQ3DeKwD1dbRyndqWORRnz8TLEXSiCFXdZT2oiMrcJtO188Ph4eLGut1-4PzKhwgrQ' https://demo-dev.daocloud.io/apis/ghippo.io/v1alpha1/users?page=1&pageSize=10 -k
```

**Request result**

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
