# 接入管理

当两个或两个以上平台相互对接或嵌入时，通常需要进行用户体系打通。在用户打通过程中，接入管理主要提供 SSO 接入能力，当你需要将 DaoCloud Enterprise 5.0 作为用户源接入客户平台时，你可以通过在接入管理模块创建 SSO 接入来实现。

## 创建 SSO 接入
  
前提：拥有平台管理员 Admin 权限或者用户与访问控制管理员 IAM admin 权限。
  
1、 管理员进入`用户与访问控制`，选择`接入管理`，进入接入管理列表，点击右上方的`创建 SSO 接入`。
  
![创建sso接入](./docs/zh/docs/ghippo/images/sso1.png/)
  
2、在`创建 SSO 接入`页面填写客户端 ID。
![创建 SSO 接入](./docs/zh/docs/ghippo/images/sso2.png)

3、创建 SSO 接入成功后，在`接入管理`管理列表，点击刚创建的客户端 ID 进入详情，复制客户端 ID、密钥和单点登录 URL 信息，填写至客户平台完成用户体系打通。

![SSO 接入详情](./docs/zh/docs/ghippo/images/sso3.png)
