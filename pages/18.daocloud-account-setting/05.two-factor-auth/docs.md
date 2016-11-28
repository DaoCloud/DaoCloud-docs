---
title: 动态口令认证
taxonomy:
    category:
        - docs
---

<!-- reviewed by fiona -->

动态口令认证是 DaoCloud 提供的一种保护 DaoCloud 账号安全的强有力工具，它依赖于与 DaoCloud 账号绑定的微信账号。如果需要使用**动态口令认证**功能，请先绑定微信账号。

>>>>> 绑定微信账号的方法，请参照「[用户账号设置](http://docs.daocloud.io/daocloud-account-setting/account-setting)」。

### 动态口令认证的作用

动态口令认证的作用类似于银行的电子密码器，每次登录 DaoCloud 账号时，DaoCloud 会发送一个随机的动态口令到与 DaoCloud 账号绑定的微信账号中，您需要使用这段动态口令进行登录。

开启此功能后，如果没有得到动态口令，即便知道了 DaoCloud 账号的密码，也无法登录到 DaoCloud 的服务后台，提高了 DaoCloud 账号的安全性。

### 如何开启动态口令认证

如需开启动态口令认证，需要打开个人账号页面，并进入「动态口令认证」标签页。

![开启动态口令认证](key-1.jpg)

如果已经将 DaoCloud 账号与微信账号绑定，直接点击切换开关即可。

###  使用动态口令认证登录

开启了动态口令认证之后，每次登录 DaoCloud 服务后台时，都需要通过已绑定的微信账号获取随机的动态口令。

![使用动态口令认证登录](key-2.jpg)

>>> 如您的微信账号出现问题，导致无法接收动态口令，请与我们的[技术支持团队](mailto:support@daocloud.io)联系。