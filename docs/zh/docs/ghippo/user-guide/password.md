# 密码重置

如果您忘记密码，可以按本页面说明重置密码。

## 重置密码步骤

管理员最初创建一个用户时，会为其设置用户名和密码。
该用户登录后，在 __个人中心__ 填写邮箱并修改密码。
若该用户未设置邮箱，则只能联系管理员进行密码重置。

1. 如果用户忘记了密码，可以在登录界面点击 __忘记密码__ 。

    ![登录界面](../images/password01zh.png)

1. 输入登录邮箱，点击 __提交__ 。

    ![输入登录邮箱](../images/password02zh.png)

1. 在邮箱中找到密码重置邮件，点击下方链接进行密码重置，链接时效 5 分钟。

    ![点击重置链接](../images/password03zh&en.png)

1. 在手机等终端设备安装支持 2FA 动态口令生成的应用（如 Google Authenticator），按照页面提示配置动态口令以激活账户，点击 __提交__ 。

    ![配置动态口令](../images/password04zh.png)

1. 设置新密码，点击 __提交__ 。设置新密码的要求与创建用户时的密码规则一致。

    ![更新密码](../images/password05zh.png)

1. 修改密码成功，直接跳转首页。

## 重置密码流程

整个密码重置的流程示意图如下。

```mermaid
graph TB

pass[忘记密码] --> usern[输入用户名]
--> button[点击发送验证邮件的按钮] --> judge1[判断用户名是否正确]

    judge1 -.正确.-> judge2[判断是否绑定邮箱]
    judge1 -.错误.-> tip1[提示用户名不正确]
    
        judge2 -.已绑定邮箱.-> send[发送重置邮件]
        judge2 -.未绑定邮箱.-> tip2[提示未绑定邮箱<br>联系管理员重置密码]
        
send --> click[点击邮件中的链接] --> config[配置动态口令] --> reset[重置密码]
--> success[成功重置密码]

classDef plain fill:#ddd,stroke:#fff,stroke-width:1px,color:#000;
classDef k8s fill:#326ce5,stroke:#fff,stroke-width:1px,color:#fff;
classDef cluster fill:#fff,stroke:#bbb,stroke-width:1px,color:#326ce5;

class pass,usern,button,tip1,send,tip2,send,click,config,reset,success plain;
class judge1,judge2 k8s
```
