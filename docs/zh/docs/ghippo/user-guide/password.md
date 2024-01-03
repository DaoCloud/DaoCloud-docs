# 密码重置

如果您忘记密码，可以按本页面说明重置密码。

## 重置密码步骤

管理员最初创建一个用户时，会为其设置用户名和密码。
该用户登录后，在 __个人中心__ 填写邮箱并修改密码。
若该用户未设置邮箱，则只能联系管理员进行密码重置。

1. 如果用户忘记了密码，可以在登录界面点击 __忘记密码__ 。

    ![登录界面](https://docs.daocloud.io/daocloud-docs-images/docs/ghippo/images/password00.png)

1. 输入用户名，点击 __提交__ 。

    为防止滥发邮件，点击 __提交__ 后，该按钮将变灰并显示一个为期 1 分钟的倒计时。
    如果 1 分钟后还未收到邮件，请再次点击此按钮。

    ![密码重置流程](https://docs.daocloud.io/daocloud-docs-images/docs/ghippo/images/password02.png)

1. 在邮箱中找到密码重置邮件，点击 __密码重置__ 按钮。

    ![密码重置流程](https://docs.daocloud.io/daocloud-docs-images/docs/ghippo/images/password03.png)

1. 按照屏幕提示，设置新密码，点击 __确定__ 。设置新密码的要求与创建用户时的密码规则一致。

    ![密码重置流程](https://docs.daocloud.io/daocloud-docs-images/docs/ghippo/images/password04.png)

1. 屏幕提示密码修改成功。

    ![密码重置流程](https://docs.daocloud.io/daocloud-docs-images/docs/ghippo/images/password05.png)

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
        
send --> click[点击邮件中的链接] --> reset[重置密码]
--> success[成功重置密码]

classDef plain fill:#ddd,stroke:#fff,stroke-width:1px,color:#000;
classDef k8s fill:#326ce5,stroke:#fff,stroke-width:1px,color:#fff;
classDef cluster fill:#fff,stroke:#bbb,stroke-width:1px,color:#326ce5;

class pass,usern,button,tip1,send,tip2,send,click,reset,success plain;
class judge1,judge2 k8s
```
