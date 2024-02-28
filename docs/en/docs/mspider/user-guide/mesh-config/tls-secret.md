# TLS key management

Secret is an object stored in the form of key/value pairs, containing sensitive information such as certificates, private keys, and credentials, and is used for link TLS encrypted communication between services.
The service mesh provides an interface for TLS key management.

## Prepare credentials and private key

Take helloworld as an example to create a certificate and a private key.

```shell
openssl req -out example_certs1/helloworld.example.com.csr -newkey rsa:2048 -nodes -keyout example_certs1/helloworld.example.com.key -subj "/CN=helloworld.example.com/O=helloworld organization"
openssl x509 -req -sha256 -days 365 -CA example_certs1/example.com.crt -CAkey example_certs1/example.com.key -set_serial 1 -in example_certs1/helloworld.example.com.csr -out example_certs1/helloworld.example.com.crt
```

The generated certificate looks like this:

```cert
-----BEGIN CERTIFICATE REQUEST-----
MIICiDCCAXACAQAwQzEfMB0GA1UEAwwWaGVsbG93b3JsZC5leGFtcGxlLmNvbTEg
MB4GA1UECgwXaGVsbG93b3JsZCBvcmdhbml6YXRpb24wggEiMA0GCSqGSIb3DQEB
AQUAA4IBDwAwggEKAoIBAQDHLmX2uLbgWyrGC1/FMVPCToOoFnM0kKCQyAEbYxqX
HJV4CQ3V7UlyEIdj/w0QK+eY8dD8QVKKLiX4DCNYM7Rv/X2Jltw0GHG6788VstGy
1tvNv9u/wsgHV7J0ybxn+iElgppLTKiLjuqZv/8HPNvE/CcvGmPbH2depd5nvYxq
kTNhYU1T8wPfSPSRoPZncwqjwnFy+IkjWzO/NBYYtVDU21VAuDJmqF8oO6cFSulm
OG0GDKaE0eXkYnRQSfssZHtGSEgb/R6feZNhIa4DajHYiGu37qqdS+gPodzGtRGI
ryc2gsXJNywnISpw78ne3GCgvCVshHV1a9+XaWo0nkN9AgMBAAGgADANBgkqhkiG
9w0BAQsFAAOCAQEAZiDs4ICVbmZhscdIE/vJINWLL77dAa2nstFQHrck0rINdqDF
YYF84J8OjNpaHkIzwQ+icKJ9j6FjdBkmCvfpd9nMnihe6XTbfNNEx4hyGCg1My5x
XmeKsd/4U5oJCle3qb0U/KDsIAbdv859DnSGHnf3rwx22FnaIlw2bnbyIkRXqIPO
QjCoOu9Yor2sxfDw+gVZdUnsKVQYrII4RPJrBL+DWs9uUu/LrfZx8VHyGQSSNaMY
ivThfuaDOSIWR1Rqd6+z13/nmJrV0HJWwOk18Of5O/Cqb9sx5aduML9zmd2hpv5a
qCLeUusdlSW12hVnudaP7TM3RE7R6r1TwwXE2As==
-----END CERTIFICATE REQUEST-----
```

The generated private key looks like this:

```key
-----BEGIN PRIVATE KEY-----
MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDHLmX2uLbgWyrG
C1/FMVPCToOoFnM0kKCQyAEbYxqXHJV4CQ3V7UlyEIdj/w0QK+eY8dD8QVKKLiX4
DCNYM7Rv/X2Jltw0GHG6788VstGy1tvNv9u/wsgHV7J0ybxn+iElgppLTKiLjuqZ
v/8HPNvE/CcvGmPbH2depd5nvYxqkTNhYU1T8wPfSPSRoPZncwqjwnFy+IkjWzO/
NBYYtVDU21VAuDJmqF8oO6cFSulmOG0GDKaE0eXkYnRQSfssZHtGSEgb/R6feZNh
Ia4DajHYiGu37qqdS+gPodzGtRGIryc2gsXJNywnISpw78ne3GCgvCVshHV1a9+X
aWo0nkN9AgMBAAECggEASMh/oeRljx5BRxUo7dnUjZA7M9TgTDj9M2qiXOud79IW
HELSt3V5/SBlGPk+QMaKXq0efM8x5iRu43EsCTL7oGC02u4xkSfNh03SEk/BqOQy
dcDCABShG23EXEDLhAM20Yoj75gXjseumng6LN7kP9sURnYSPyP+letuleIByX6Y
is/bKKGcs4L5txH6KpMJL8hOW/6nK1AREeDVmd4Y98CoU+OC2R9ThR2FFRXgdYxh
2xCZ68+XQ1bUf2+24YI9/73iPvKRPe9zZKPhMak1kd7Lnuy3DEXAvjhpPs2eqiJ9
J7n6DkDn/fAMN6yvkm07vBbWS8AV421iKX+rf7b3AQKBgQDjm4Zg+/NXj+egrJio
Qt7UfIklp1dGje60OfKSZj7F3pBh/R1+HHmXh0YHOvDy0OEBUY9h97XyYHIBvPMf
fnyr2S0czk/HpcS6TnFj9QaVjtQdZ8h7Sf+3uPWHgqvu+gBJarA5fQZSgNRezEBo
5mqh+wXvzQioTrm3E1nBYUxw8QKBgQDgBxoD0DrLgypIiqR95i4lyf4YI5MzgurO
F2MLFkQ6QWdMfzZnh7Cs/CdqUD3weZTqPFom3zDe1NFHG5xnGrdIoKzUMZ5JVG8t
xznpckq7mPnm8ghGZ6R515SFl5l5iEyy15ct1v+nKcjRNHmYe0d5tIWRDrfGcXJu
DfC73CT7TQKBgGJjlqFSCI0vbeds9Mi3r2+XLgoS3o1nSWqrKgrTHAuY/Dz/l8Iu
OPmhxknV1taAKOPTB/JHjGVr/5x0u3w/x1DaHsA3BxG8vN/0jNuyzdfU2Cil9mol
QN+AmtKrT/uMIpeaAPe47gS4IBWioa02/Z1rz9MrhLSM44caXFBV6R9hAoGAaUgN
GsOuDdw7b9HwEdat00aFKjT1xZx92pK1Eg3JzJLWB+Y03Byxk+oAX/8LzMpmiFoK
iAAVyHK9UyyPqQiuH+yarDIRUCblBN9+wM3cfyMaNkWCTAwDCNueSdX/41SBrv6Q
ZpOGm7mQTXjauCUfZvvGVXBUP2crPrtAahjALHUCgYEAxGvVH0I6Uphpf4gGqqcm
1ge0R6nGtPeKn6/Nh2Y3sHVxGvByFkuRXqZ2gSw6etleSJhQLLcvZm/K6FZu0sMQ
C4jSbYTJupuL8x4uSCEH5X/na/6AwUfmwA0P7jGuKKhHgsHpH8OHly6eHonM7pzn
WQuRxan+FuKE3RiKHFXkslks=
-----END PRIVATE KEY-----
```

## Create key

1. After entering a mesh, click __Mesh Configuration__ -> __TLS Key Management__ in the left navigation bar, and click the __Create__ button.

     

1. Fill in the name, select the namespace, fill in the newly created certificate and private key, add labels according to the situation, and click __OK__ .

     

1. The screen prompts that the creation is successful. Click the __⋮__ button on the right to perform operations such as editing, YAML editing, and deletion.

     

The key YAML after successful creation in this example is as follows:

```yaml
metadata:
  name: secret001
  namespace: default
  uid: 1b43fc33-7898-40f9-9868-b65570f35a3d
  resourceVersion: '450493'
  creationTimestamp: '2023-04-20T07:09:33Z'
  labels:
    mspider.io/managed: 'true'
    test: teston0422
  annotations:
    ckube.daocloud.io/indexes: >-
      {"cluster":"nicole-hosted-mesh-hosted","createdAt":"2023-04-20T07:09:33Z","is_deleted":"false","labels":"\"mspider.io/managed=true\",\"test=teston0422\",","name":"secret001","namespace":"default","type":"kubernetes.io/tls"}
    ckube.doacloud.io/cluster: nicole-hosted-mesh-hosted
  managedFields:
    - manager: cacheproxy
      operation: Update
      apiVersion: v1
      time: '2023-04-20T07:09:33Z'
      fieldsType: FieldsV1
      fieldsV1:
        f:data:
          .: {}
          f:tls.crt: {}
          f:tls.key: {}
        f:metadata:
          f:labels:
            .: {}
            f:mspider.io/managed: {}
            f:test: {}
        f:type: {}
data:
  tls.crt: >-
    TUlJQ2lEQ0NBWEFDQVFBd1F6RWZNQjBHQTFVRUF3d1dhR1ZzYkc5M2IzSnNaQzVsZUdGdGNHeGxMbU52YlRFZwpNQjRHQTFVRUNnd1hhR1ZzYkc5M2IzSnNaQ0J2Y21kaGJtbDZZWFJwYjI0d2dnRWlNQTBHQ1NxR1NJYjNEUUVCCkFRVUFBNElCRHdBd2dnRUtBb0lCQVFESExtWDJ1TGJnV3lyR0MxL0ZNVlBDVG9Pb0ZuTTBrS0NReUFFYll4cVgKSEpWNENRM1Y3VWx5RUlkai93MFFLK2VZOGREOFFWS0tMaVg0RENOWU03UnYvWDJKbHR3MEdIRzY3ODhWc3RHeQoxdHZOdjl1L3dzZ0hWN0oweWJ4bitpRWxncHBMVEtpTGp1cVp2LzhIUE52RS9DY3ZHbVBiSDJkZXBkNW52WXhxCmtUTmhZVTFUOHdQZlNQU1JvUFpuY3dxanduRnkrSWtqV3pPL05CWVl0VkRVMjFWQXVESm1xRjhvTzZjRlN1bG0KT0cwR0RLYUUwZVhrWW5SUVNmc3NaSHRHU0VnYi9SNmZlWk5oSWE0RGFqSFlpR3UzN3FxZFMrZ1BvZHpHdFJHSQpyeWMyZ3NYSk55d25JU3B3NzhuZTNHQ2d2Q1ZzaEhWMWE5K1hhV28wbmtOOUFnTUJBQUdnQURBTkJna3Foa2lHCjl3MEJBUXNGQUFPQ0FRRUFaaURzNElDVmJtWmhzY2RJRS92SklOV0xMNzdkQWEybnN0RlFIcmNrMHJJTmRxREYKWVlGODRKOE9qTnBhSGtJendRK2ljS0o5ajZGamRCa21DdmZwZDluTW5paGU2WFRiZk5ORXg0aHlHQ2cxTXk1eApYbWVLc2QvNFU1b0pDbGUzcWIwVS9LRHNJQWJkdjg1OURuU0dIbmYzcnd4MjJGbmFJbHcyYm5ieUlrUlhxSVBPClFqQ29PdTlZb3Iyc3hmRHcrZ1ZaZFVuc0tWUVlySUk0UlBKckJMK0RXczl1VXUvTHJmWng4Vkh5R1FTU05hTVkKaXZUaGZ1YURPU0lXUjFScWQ2K3oxMy9ubUpyVjBISld3T2sxOE9mNU8vQ3FiOXN4NWFkdU1MOXptZDJocHY1YQpxQ0xlVXVzZGxTVzEyaFZudWRhUDdUTTNSRTdSNnIxVHd3WEUyQT09s
  tls.key: >-
    TUlJRXZRSUJBREFOQmdrcWhraUc5dzBCQVFFRkFBU0NCS2N3Z2dTakFnRUFBb0lCQVFESExtWDJ1TGJnV3lyRwpDMS9GTVZQQ1RvT29Gbk0wa0tDUXlBRWJZeHFYSEpWNENRM1Y3VWx5RUlkai93MFFLK2VZOGREOFFWS0tMaVg0CkRDTllNN1J2L1gySmx0dzBHSEc2Nzg4VnN0R3kxdHZOdjl1L3dzZ0hWN0oweWJ4bitpRWxncHBMVEtpTGp1cVoKdi84SFBOdkUvQ2N2R21QYkgyZGVwZDVudll4cWtUTmhZVTFUOHdQZlNQU1JvUFpuY3dxanduRnkrSWtqV3pPLwpOQllZdFZEVTIxVkF1REptcUY4b082Y0ZTdWxtT0cwR0RLYUUwZVhrWW5SUVNmc3NaSHRHU0VnYi9SNmZlWk5oCklhNERhakhZaUd1MzdxcWRTK2dQb2R6R3RSR0lyeWMyZ3NYSk55d25JU3B3NzhuZTNHQ2d2Q1ZzaEhWMWE5K1gKYVdvMG5rTjlBZ01CQUFFQ2dnRUFTTWgvb2VSbGp4NUJSeFVvN2RuVWpaQTdNOVRnVERqOU0ycWlYT3VkNzlJVwpIRUxTdDNWNS9TQmxHUGsrUU1hS1hxMGVmTTh4NWlSdTQzRXNDVEw3b0dDMDJ1NHhrU2ZOaDAzU0VrL0JxT1F5CmRjRENBQlNoRzIzRVhFRExoQU0yMFlvajc1Z1hqc2V1bW5nNkxON2tQOXNVUm5ZU1B5UCtsZXR1bGVJQnlYNlkKaXMvYktLR2NzNEw1dHhINktwTUpMOGhPVy82bksxQVJFZURWbWQ0WTk4Q29VK09DMlI5VGhSMkZGUlhnZFl4aAoyeENaNjgrWFExYlVmMisyNFlJOS83M2lQdktSUGU5elpLUGhNYWsxa2Q3TG51eTNERVhBdmpocFBzMmVxaUo5Cko3bjZEa0RuL2ZBTU42eXZrbTA3dkJiV1M4QVY0MjFpS1grcmY3YjNBUUtCZ1FEam00WmcrL05YaitlZ3JKaW8KUXQ3VWZJa2xwMWRHamU2ME9mS1NaajdGM3BCaC9SMStISG1YaDBZSE92RHkwT0VCVVk5aDk3WHlZSElCdlBNZgpmbnlyMlMwY3prL0hwY1M2VG5GajlRYVZqdFFkWjhoN1NmKzN1UFdIZ3F2dStnQkphckE1ZlFaU2dOUmV6RUJvCjVtcWgrd1h2elFpb1RybTNFMW5CWVV4dzhRS0JnUURnQnhvRDBEckxneXBJaXFSOTVpNGx5ZjRZSTVNemd1ck8KRjJNTEZrUTZRV2RNZnpabmg3Q3MvQ2RxVUQzd2VaVHFQRm9tM3pEZTFORkhHNXhuR3JkSW9LelVNWjVKVkc4dAp4em5wY2txN21Qbm04Z2hHWjZSNTE1U0ZsNWw1aUV5eTE1Y3QxdituS2NqUk5IbVllMGQ1dElXUkRyZkdjWEp1CkRmQzczQ1Q3VFFLQmdHSmpscUZTQ0kwdmJlZHM5TWkzcjIrWExnb1MzbzFuU1dxcktnclRIQXVZL0R6L2w4SXUKT1BtaHhrblYxdGFBS09QVEIvSkhqR1ZyLzV4MHUzdy94MURhSHNBM0J4Rzh2Ti8wak51eXpkZlUyQ2lsOW1vbApRTitBbXRLclQvdU1JcGVhQVBlNDdnUzRJQldpb2EwMi9aMXJ6OU1yaExTTTQ0Y2FYRkJWNlI5aEFvR0FhVWdOCkdzT3VEZHc3YjlId0VkYXQwMGFGS2pUMXhaeDkycEsxRWczSnpKTFdCK1kwM0J5eGsrb0FYLzhMek1wbWlGb0sKaUFBVnlISzlVeXlQcVFpdUgreWFyRElSVUNibEJOOSt3TTNjZnlNYU5rV0NUQXdEQ051ZVNkWC80MVNCcnY2UQpacE9HbTdtUVRYamF1Q1VmWnZ2R1ZYQlVQMmNyUHJ0QWFoakFMSFVDZ1lFQXhHdlZIMEk2VXBocGY0Z0dxcWNtCjFnZTBSNm5HdFBlS242L05oMlkzc0hWeEd2QnlGa3VSWHFaMmdTdzZldGxlU0poUUxMY3ZabS9LNkZadTBzTVEKQzRqU2JZVEp1cHVMOHg0dVNDRUg1WC9uYS82QXdVZm13QTBQN2pHdUtLaEhnc0hwSDhPSGx5NmVIb25NN3B6bgpXUXVSeGFuK0Z1S0UzUmlLSEZYa3Nsaz0s=
type: kubernetes.io/tls
```

## Use Cases

Created TLS keys can be used to:

1. __Destination Rules__ . When adding policy configuration, after enabling client TLS, you can choose the created key in the following two modes:

     - Simple mode
     - Bidirectional mode

     

1. __Gateways__ . After enabling the server-side TLS mode, you can choose the created key in the following 3 modes:

     - Simple mode
     - Bidirectional mode
     - Istio bidirectional mode

     
