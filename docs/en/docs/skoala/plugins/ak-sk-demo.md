---
MTPE: windsonsea
date: 2024-01-11
---

# A Demo to Integrate the AK/SK Authentication

The demo application consists of two modules: the simulated signature application and the simulated authentication application. The simulated signature application is used to generate corresponding signature information, and the simulated authentication application is an implementation of signature authentication based on the Envoy authentication server. The following mainly describes the details of the simulated signature application:

## Simulated Signature Application

Repo URL: <https://github.com/projectsesame/ak-sk-demo-java>

The simulated signature application is divided into three interfaces:

1. /signstr: Generates signature information based on the current time.
2. /signstrbytime: Generates signature information based on the specified time.
3. /mock: Generates signature information based on the current time and simulates integrating the request through the gateway.

All three interfaces require a POST request and need to pass in the Body in JSON format. The specific fields are shown in the following table:

| Field Name | Field Meaning | Example | Remarks |
| ---------- | ------------- | ------- | ------- |
| url | Complete gateway path | `http://10.6.222.21:30080/yang?a=b` | The format is: `scheme://gatewayIP:gatewayPort/path?param` |
| host | Domain | `10.6.222.21:30080` | |
| method | Request method | GET/POST | Only supports GET and POST |
| headers | Request headers | `{"User-Agent":"curl/8.1.2","Accept":"_/_","k":"v"}` | Request headers carried when integrating the gateway |
| signHeaders | Headers that need to be signed | ["User-Agent","Accept"] | Headers that need to be signed. The headers in signHeaders will be used to generate the signature from the headers field |
| requestBody | Request body | this is request body | |
| apiKey | Identification for request authentication | api-key | Identification for request authentication |
| secret | Secret key corresponding to apiKey | secret | No need to fill in. The demo program defaults to secret. You can obtain the secret uniquely according to your needs through the apiKey |

The demo application will generate a signature based on the above structure. The structure of the generated signature string is as follows:

!!! info

    x-data: Request method\nRequest path\nRequest parameters\nRequest time\nRequest headers\nRequest body

    The request headers are sorted in dictionary order and separated by commas. The headers specified in signHeaders field will be used for signature. If not specified, only the x-data request header will be signed. The x-data request header is a custom request header and represents the request time.

    If there is a request body, the request body is encrypted with MD5 and then encoded in Base64.

    The signature algorithm is to encrypt x-data with hmac-sha1 according to Secret, and then encode it in Base64.

    The signature authentication information string is:

    - id=apiKey
    - algorithm=signature algorithm
    - headers=signature headers
    - signature=signature string

## Interface Signature Method

1. Input parameters:

    ```json
    {
        "url":"http://10.6.222.21:30080/yang?a=b",
        "host":"10.6.222.21:30080",
        "apiKey": "key",
        "method":"POST",
        "headers":{"User-Agent":"curl/8.1.2","Accept":"*/*","k":"v"},
        "signHeaders":["User-Agent","Accept"],
        "requestBody":"hahha"
    }
    ```

1. Generate the signature string:

    ```http
    x-data: POST
    /yang
    a=b
    1703573142130
    accept: */*
    user-agent: curl/8.1.2
    x-date: 1703573142130
    ODc5NWEzY2QyY2ExZjdmMTUzMGIzYmI0ZThiYWY2NTA=
    ```

1. Encrypt the generated signature string with the Secret obtained through custom means. Use the above string to encrypt with hmac-sha1, and then encode it in Base64. The result is:

    ```key
    SuRuXnwwgrv+0/TNbWQxkEIdnlA=
    ```

1. Generate the signature authentication information:

    ```signature
    id=key,algorithm=hmac-sha1,headers=User-Agent;Accept;x-date,signature=SuRuXnwwgrv+0/TNbWQxkEIdnlA=
    ```

## Example Code Interface Return Result

- If the /signstr interface is requested, the signature information corresponding to the current time will be returned. For example:

    ```json
    {
        "x-data": 1703573142130,
        "authorization": "id=key,algorithm=hmac-sha1,headers=User-Agent;Accept;x-date,signature=SuRuXnwwgrv+0/TNbWQxkEIdnlA="
    }
    ```

    Add the returned two request headers to the request for integrating the gateway.

- If the /signstrbytime interface is requested, the signature information corresponding to the specified time parameter will be returned. For example, if the time parameter passed in is 1703573152130, the return result will be:

    ```json
    {
        "x-data": 1703573152130,
        "authorization": "id=key,algorithm=hmac-sha1,headers=User-Agent;Accept;x-date,signature=8zJJS6DVoGxlwi1K4vrK0QcdwVg="
    }
    ```

- If the /mock interface is requested, a signature string corresponding to the current time will be generated and a simulated request to the gateway will be made. The gateway address is the URL parameter passed in the request.

The above describes the signature logic and process of the simulated signature application. After the signature is completed, it needs to be combined with the authentication service to achieve the ak/sk authentication logic. If the signature of the simulated signature application is used, we provide a matching authentication service. You only need to connect the gateway to the corresponding authentication service to perform authentication.

## Authentication Server

Repo URL: <https://github.com/projectsesame/envoy-authz-ak-sk-java>

According to the orchestration file in [envoy-auzhe-java-aksk.yaml](https://github.com/projectsesame/envoy-authz-ak-sk-java/blob/main/envoy-authz-java-aksk.yaml), deploy it to the cluster where the gateway is located, and then [connect to the authentication server](./auth-server.md#_6).
