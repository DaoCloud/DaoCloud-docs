# 如何将客户系统集成到 DCE 5.0（OEM IN）

OEM IN 是指合作伙伴的平台作为子模块嵌入 DCE 5.0，出现在 DCE 5.0 一级导航栏。
用户通过 DCE 5.0 进行登录和统一管理。实现 OEM IN 共分为 5 步，分别是：

1. [统一域名](#_2)
1. [打通用户体系](#_3)
1. [对接导航栏](#_4)
1. [定制外观](#_5)
1. [打通权限体系（可选）](#_6)

具体操作演示请参见：[OEM IN 最佳实践视频教程](../../../videos/use-cases.md#dce-50_3)。

!!! note

    以下使用开源软件 Label Studio 来做嵌套演示。实际场景需要自己解决客户系统的如下问题：

    1. 客户系统需要自己添加一个 Subpath，用于区分哪些是 DCE 5.0 的服务，哪些是客户系统的服务。

## 环境准备

1. 部署 DCE 5.0 环境：
 
    `https://10.6.202.177:30443` 作为 DCE 5.0

    ![DCE 5.0](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/ghippo/best-practice/oem/images/oem-dce5.png)

1. 部署客户系统环境：

    `http://10.6.202.177:30123` 作为客户系统

    应用过程中对客户系统的操作请根据实际情况进行调整。

1. 规划客户系统的 Subpath 路径： `http://10.6.202.177:30123/label-studio`（建议使用辨识度高的名称作为 Subpath，不能与主 DCE 5.0 的 HTTP router 发生冲突）。请确保用户通过 `http://10.6.202.177:30123/label-studio` 能够正常访问客户系统。

    ![Label Studio](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/ghippo/best-practice/oem/images/oem-label-studio.png)

## 统一域名和端口

1. SSH 登录到 DCE 5.0 服务器。

    ```bash
    ssh root@10.6.202.177
    ```

1. 使用 vim 命令创建 __label-studio.yaml__ 文件

     ```bash
     vim label-studio.yaml
     ```

     ```yaml title="label-studio.yaml"
     apiVersion: networking.istio.io/v1beta1
     kind: ServiceEntry
     metadata:
       name: label-studio
       namespace: ghippo-system
     spec:
       exportTo:
       - "*"
       hosts:
       - label-studio.svc.external
       ports:
       # 添加虚拟端口
       - number: 80
         name: http
         protocol: HTTP
       location: MESH_EXTERNAL
       resolution: STATIC
       endpoints:
       # 改为客户系统的域名（或IP）
       - address: 10.6.202.177
         ports:
           # 改为客户系统的端口号
           http: 30123
     ---
     apiVersion: networking.istio.io/v1alpha3
     kind: VirtualService
     metadata:
       # 修改为客户系统的名字
       name: label-studio
       namespace: ghippo-system
     spec:
       exportTo:
       - "*"
       hosts:
       - "*"
       gateways:
       - ghippo-gateway
       http:
       - match:
           - uri:
               exact: /label-studio # 修改为客户系统在 DCE5.0 Web UI 入口中的路由地址
           - uri:
               prefix: /label-studio/ # 修改为客户系统在 DCE5.0 Web UI 入口中的路由地址
         route:
         - destination:
             # 修改为上文 ServiceEntry 中的 spec.hosts 的值
             host: label-studio.svc.external
             port:
               # 修改为上文 ServiceEntry 中的 spec.ports 的值
               number: 80
     ---
     apiVersion: security.istio.io/v1beta1
     kind: AuthorizationPolicy
     metadata:
       # 修改为客户系统的名字
       name: label-studio
       namespace: istio-system
     spec:
       action: ALLOW
       selector:
         matchLabels:
           app: istio-ingressgateway
       rules:
       - from:
         - source:
             requestPrincipals:
             - '*'
       - to:
         - operation:
             paths:
             - /label-studio # 修改为 VirtualService 中的 spec.http.match.uri.prefix 的值
             - /label-studio/* # 修改为 VirtualService 中的 spec.http.match.uri.prefix 的值（注意，末尾需要添加 "*"）
     ```

1. 使用 kubectl 命令应用 label-studio.yaml：

    ```bash
    kubectl apply -f label-studio.yaml
    ```

1. 验证 Label Studio UI 的 IP 和 端口是否一致：
   
    ![Label Studio](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/ghippo/best-practice/oem/images/label-studio-2.png)

## 打通用户体系

将客户系统与 DCE 5.0 平台通过 OIDC/OAUTH 等协议对接，使用户登录 DCE 5.0 平台后进入客户系统时无需再次登录。

1. 在两套 DCE 5.0 的场景下，可以在 DCE 5.0 中通过 __全局管理__ -> __用户与访问控制__ -> __接入管理__ 创建 SSO 接入。

    ![接入管理列表](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/ghippo/best-practice/oem/images/oemin-jierulist.png)

    ![接入管理列表](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/ghippo/best-practice/oem/images/oem-out01.png)

2. 创建后将详情中的客户端 ID、密钥、单点登录 URL 等填写到客户系统的 __全局管理__ -> __用户与访问控制__ -> __身份提供商__ -> __OIDC__ 中，完成用户对接。

    ![oidc](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/ghippo/best-practice/oem/images/oeminoidc.png)

3. 对接完成后，客户系统登录页面将出现 OIDC（自定义）选项，首次从 DCE 5.0 平台进入客户系统时选择通过 OIDC 登录，
   后续将直接进入客户系统无需再次选择。

    ![登录页](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/ghippo/best-practice/oem/images/oeminlogin.png)

## 对接导航栏

参考文档下方的 tar 包来实现一个空壳的前端子应用，把客户系统以 iframe 的形式放进该空壳应用里。

1. 下载 gproduct-demo-main.tar.gz 文件，将 src 文件夹下 App-iframe.vue 中的 src 属性值改为用户进入客户系统的绝对地址，如：
   __src="https://10.6.202.177:30443/label-studio" (DCE 5.0 地址 + Subpath)__ 或相对地址，如： __src="./external-anyproduct/insight"__ 

    ![src 地址](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/ghippo/best-practice/oem/images/src-2.png)

1. 删除 src 文件夹下的 App.vue 和 main.ts 文件，同时将：
    
    - App-iframe.vue 重命名为 App.vue
    - main-iframe.ts 重命名为 main.ts

1. 按照 readme 步骤构建镜像（注意：执行最后一步前需要将 __demo.yaml__ 中的镜像地址替换成构建出的镜像地址）

   ![构建镜像](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/ghippo/best-practice/oem/images/oemin-image-2.png)

对接完成后，将在 DCE 5.0 的一级导航栏出现 __客户系统__ ，点击可进入客户系统。

![客户系统](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/ghippo/best-practice/oem/images/oemin-menu.png)

## 定制外观

!!! note

    DCE 5.0 支持通过写 CSS 的方式来实现外观定制。实际应用中客户系统如何实现外观定制需要根据实际情况处理。

登录客户系统，通过 __全局管理__ -> __平台设置__ -> __外观定制__ 可以自定义平台背景颜色、logo、名称等，
具体操作请参照[外观定制](../../user-guide/platform-setting/appearance.md)。

## 打通权限体系（可选）

**方案思路一：**

定制化团队可实现一定制模块，DCE 5 将每一次的用户登录事件通过 Webhook 的方式通知到定制模块，
定制模块可自行调用 AnyProduct 和 DCE 5.0 的 [OpenAPI](https://docs.daocloud.io/openapi/index.html) 作该用户的权限信息同步。

**方案思路二：**

通过 Webhook 方式，将每一次的授权变化都通知到 AnyProduct (如有需求，后续可实现)。

### AnyProduct 使用 DCE 5.0 的其他能力(可选)

方法为：调用 DCE 5.0 [OpenAPI](https://docs.daocloud.io/openapi/index.html)

## 参考资料

- 参考 [OEM OUT 文档](./oem-out.md)
- 参阅 [gProduct-demo-main 对接 tar 包](./examples/gproduct-demo-main.tar.gz)
