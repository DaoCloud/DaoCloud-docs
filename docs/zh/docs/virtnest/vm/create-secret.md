---
hide:
  - toc
---

# 创建密钥

当创建虚拟机使用对象存储（S3）作为镜像来源时，有时候需要填写密钥来获取通过 S3 的验证。以下将介绍如何创建符合虚拟机要求的密钥。

1. 点击左侧导航栏上的 __容器管理__ ，然后点击 __集群列表__ ，进入虚拟机所在集群详情，点击 __配置与密钥__ ，选择 __密钥__ ，点击 __创建密钥__ 。

    ![创建密钥](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/virtnest/images/secret01.png)

2. 进入创建页面，填写密钥名称，选择和虚拟机相同的命名空间，注意需要选择 __默认（Opaque）__ 类型。密钥数据需要遵循以下原则

    - accessKeyId: 需要以 Base64 编码方式表示的数据
    - secretKey: 需要以 Base64 编码方式表示的数据

    ![密钥要求](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/virtnest/images/secret02.png)

3. 创建成功后可以在创建虚拟机时使用所需密钥，最后通过验证。

    ![使用密钥](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/virtnest/images/secret03.png)
