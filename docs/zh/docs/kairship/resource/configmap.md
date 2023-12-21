# 多云配置项

配置项（ConfigMap）是一种 API 对象，用来将非机密性的数据保存到键值对中。
使用时，Pod 可以将其用作环境变量、命令行参数或者存储卷中的配置文件。

多云配置项可以将多云环境配置信息和容器镜像解耦，便于修改多云应用的配置。

目前提供了两种创建方式：向导创建和 YAML 创建。本文以向导创建为例，参照以下步骤操作。

1. 进入某一个多云实例后，在左侧导航栏中，点击 __资源管理__ -> __多云配置项__ ，点击右上角的 __创建配置项__ 按钮。

    ![点击按钮](https://docs.daocloud.io/daocloud-docs-images/docs/kairship/images/config01.png)

2. 在 __创建配置项__ 页面中，输入名称，选择命名空间等信息后，点击 __确定__ 。

    ![填写表单](https://docs.daocloud.io/daocloud-docs-images/docs/kairship/images/config02.png)

3. 返回多云配置项列表，新创建的默认位于第一个。点击列表右侧的 __⋮__ ，可以编辑 YAML、更新、导出和删除配置项。

    ![其他操作](https://docs.daocloud.io/daocloud-docs-images/docs/kairship/images/config03.png)

    !!! note

        若删除一个配置项，其相关信息将一并被删除，请谨慎操作。

## YAML 示例

此处列出一个多云配置项的 YAML 示例，您稍加修改就可以使用。

```yaml
kind: ConfigMap
apiVersion: v1
metadata:
  name: cluster-info
  namespace: default
  uid: e8bf0788-d5e6-4b1f-8588-1b58c6d010d5
  resourceVersion: '1647402'
  creationTimestamp: '2022-09-26T07:26:25Z'
  labels:
    a: '1'
    b: '2'
    c: c
  annotations:
    c: '3'
    kairship.io/describe: '123'
    kpanda.io/describe: '13243'
    shadow.clusterpedia.io/cluster-name: k-kairshiptest
data:
  jws-kubeconfig-8utcre: >-
    eyJhbGciOiJIUzI1NiIsImtpZCI6Ijh1dGNyZSJ9..7-9oX6oeZsV5QJ_VsxBKFE7LPFMmfYX4bQM3IDDBw80
  jws-kubeconfig-faw64f: >-
    eyJhbGciOiJIUzI1NiIsImtpZCI6ImZhdzY0ZiJ9..Hbtgm5MFOOfLekYn-NnGFCj4vm-D1QS1h-Tm3ywcMr4
  jws-kubeconfig-kew06y: >-
    eyJhbGciOiJIUzI1NiIsImtpZCI6ImtldzA2eSJ9..nOG2817zEvF8tkmPGrE_r1vWM4kvA-5v6i29EA73Jb0
  kubeconfig: |
    apiVersion: v1
    clusters:
    - cluster:
        certificate-authority-data: LS0tLS1CRUdJTiBDRVJUSUZJQ0FURS0tLS0tCk1JSUMvakNDQWVhZ0F3SUJBZ0lCQURBTkJna3Foa2lHOXcwQkFRc0ZBREFWTVJNd0VRWURWUVFERXdwcmRXSmwKY201bGRHVnpNQjRYRFRJeU1Ea3lOakF6TXprek5Wb1hEVE15TURreU16QXpNemt6TlZvd0ZURVRNQkVHQTFVRQpBeE1LYTNWaVpYSnVaWFJsY3pDQ0FTSXdEUVlKS29aSWh2Y05BUUVCQlFBRGdnRVBBRENDQVFvQ2dnRUJBTVhYCkNSS2F6QnlFRithVWNuVHFGVVFST0JxUXZabjc4Q3h5Rnl5QVdvU0NhK1hFTkZJZVBPaGdudmd2Z1VadzZ1bmYKZWN4ZHJRblltMzRNOE1rQ0dDK21hTDNtWXJHTUNpVGl0dnNqMllOd3NCMjh4TlZPQ052UG5iZWRKOTFIYWdhbAprQ3psWGR0STlNLzdCK0xoQWdYcXlPS0NpVTd4U1ZGKzl6dGYvTU9odGlXVmpGR3RxUjZNZUk3TnRaZmY2cXZxCkJmMUVpSlR2QXBVK0l4NWh6ajJJYUVHWStzTTUzSC8vSnhjVHFRdmRjVXJOUW5SbXVZS2t0eDV5TWwzTHh5K28KcjJkbElhTVRnQi9GeWF1ZEIrTmZzLzF2a3IxcTdnek5xc1NGSFVhQlhZWUlTYXQ5V1MwRmhpVXpHbENDZjFjdQpaRjBlNU10V2M2UXRVSXZZenI4Q0F3RUFBYU5aTUZjd0RnWURWUjBQQVFIL0JBUURBZ0trTUE4R0ExVWRFd0VCCi93UUZNQU1CQWY4d0hRWURWUjBPQkJZRUZMd0VUMm1PZlVQc3hjZHhTZ1Z1VVpvdVRtekRNQlVHQTFVZEVRUU8KTUF5Q0NtdDFZbVZ5Ym1WMFpYTXdEUVlKS29aSWh2Y05BUUVMQlFBRGdnRUJBQWRQSHlNSW1zc1JLOTY0eWExbQpHRXVBMzNwUU9wdkJzSWJRZHI4R1diRWoyakk1eUZ1UVBJV3loOGRJTjE1VnN0YldSekZSZkRHQ1pWSGh6RWdMCks1U1dsMFU3MDVzQUd4UGFaQ3hEVUx0alBRSEgwNVdodzBaUkYxdHB5K2RPNk5MeWJwTVdpU2FndlFqQmpTMy8KVjZZbHc2NDFMdDc0eU9QcUJDckFKWUtYOTUzanhEdWZNSjNVV0dBa1VpaVVLWTcycXBCWGxvNVkyU2RCTmVTZwo5ME1TQ25VdDA2YkRtQ0lMaGI0OVVnZTFvamdldVVFVHJkeGppNWplQWp3bHpvZTFRcmY1bnZnRnlNV0tlK05oCnRIajdHRktHRnArVHJxSVh1TmVPc1dER3o0WldtQ3Z1bm8zRXdhSUdRNThKZWk3YjM5d2F0ZWY1K3FlOStNTWIKZ1BzPQotLS0tLUVORCBDRVJUSUZJQ0FURS0tLS0tCg==
        server: https://10.6.168.131:6443
      name: ""
    contexts: null
    current-context: ""
    kind: Config
    preferences: {}
    users: null
```
