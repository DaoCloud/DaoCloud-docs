---
title: 用户账号设置
taxonomy:
    category:
        - docs
---

<!-- TODO

本文的结构，以此介绍每一个用户中心的 Tab 页的功能，和注意事项

1. 账户信息
2. 个人信息
3. 邮箱
4. 第三方账户（强调绑定微信总资源，GitHub、等代码仓库可以留到后续章节详细介绍）
5. 交易记录（你需要在自己的主账号充值，可以使用的代金券我稍后提供给你）
6. 我的组织（后面单独文章详细介绍，这里简单提一句即可）
7. 动态口令认证（为了安全，后文详细介绍）
8. 通知（再次推荐用户绑定微信和验证邮箱）

-->
---

在完成了 DaoCloud 账号的注册后，您大可不著急使用 DaoCloud 所提供的服务，而是可以先对您的 DaoCloud 账号进行一些必要了解和设置。

### 账户信息

在个人设置页面中，第一个标签页便是账户的基本信息设置页面。在这个页面中，您可以对您的账户当前使用套餐进行查看和更改。

![](http://ww1.sinaimg.cn/large/7287333fgw1exx5k01qj5j20ss0hi402.jpg)

一个新注册的账号默认使用的是免费套餐，DaoCloud 云资源的配额为 **2x**。

<!-- 需要解析云资源的配额 -->

您也可以根据您的实际需要随时更改账号的套餐，如专业套餐（8x、16x和64x）和企业套餐（128x、256x和512x）。

![](http://ww3.sinaimg.cn/large/7287333fgw1exx6f67uh4j20sr0hj407.jpg)

若您要在 DaoCloud 上部署大型 Docker 容器集群，可以选择企业套餐中的 512x 集群。DaoCloud 提供非常便捷的账户余额充值方式，提供支付宝、微信和银行转账的付款方式（详细请浏览「[DaoCloud 的收费方案](http://docs.daocloud.io/pricing-plan)」），方便个人用户和企业用户体验更优质的 DaoCloud 服务。

![](http://ww2.sinaimg.cn/large/7287333fgw1exxbp0fpv1j20h107pt8y.jpg)

如果您在各种渠道获得了 DaoCloud 发放的礼券，便可以在这个页面的下方「我的礼券」栏目中将其使用到您的 DaoCloud 账户中。

![](http://ww1.sinaimg.cn/large/7287333fgw1exxbxtj773j20st0hk0ub.jpg)

### 个人信息

在这个页面中，您可以对您的 DaoCloud 账号基本信息进行查看和修改，如上传头像、设置手机号和更改密码等。

![](http://ww1.sinaimg.cn/large/7287333fgw1exxd4i83hvj20t70hiq43.jpg)

如果您需要更改密码，请点击「更改密码」，然后按提示输入**原密码**和**新密码**，并点击「保存」即可。

![](http://ww3.sinaimg.cn/large/7287333fgw1exxdfkgr3qj20hf08vwem.jpg)

### 邮箱

DaoCloud 的用户系统允许您将多个电子邮箱绑定到同一个 DaoCloud 账号上，以发挥不同的用途。在这个「邮箱」标签页中，您可以关联和修改您的邮件地址，并设置其中的一个为主邮箱。您的主邮箱将被用于登陆账户以及接收相关的邮件通知（例如，账户提醒和计费收据）。

![](http://ww2.sinaimg.cn/large/7287333fgw1exxe00fzqjj20t60hkq4i.jpg)

如果您需要将其他电子邮箱与您的 DaoCloud 账号绑定，您可以将新的电子邮箱地址填写到「新邮件...」输入框中，并点击「添加」按钮。DaoCloud 会向新的电子邮箱中发送一封验证邮件，按照提示将新的电子邮箱验证即可。

![](http://ww1.sinaimg.cn/large/7287333fgw1exxe1y3i8dj20t70hi75s.jpg)

<!--
![](FileName11_10_2015_09_34_50_1447119290.jpg)### 账户信息

TODO: 术语表：个人账户、组织账户、配额

DaoCloud 提供了两种管理账户的方式，一种为个人账户，另一种为组织账户。

[用户中心](user.md)提供了当前用户的个人账户信息而[组织中心](organization.md)则提供了当前用户所选择组织的账户信息。

「用户中心」中的账户信息：

![用户中心：账户信息](/img/screenshots/features/profiles/account/user-account-info.png)

「组织中心」中的账户信息：

![组织中心：账户信息](/img/screenshots/features/profiles/account/org-account-info.png)

#### 账户余额

账户余额在「用户中心」和「组织中心」中分别显示了当前用户和所选择组织的账户余额。

> 提示：关于充值支付的细节请参考[账户充值](payment.md)。

> 注意：个人账户与组织账户的余额是完全独立的，也就是说个人账户的余额无法给组织使用，反之亦然。

#### 账户配额

接下来的列表在「用户中心」和「组织中心」中分别显示了当前用户和所选择组织的配额与使用情况。

> 注意：个人账户与组织账户的配额也是完全独立的，也就是说扩充个人账户的配额并无法增加组织的配额，反之亦然。



### 账户充值

DaoCloud 为个人和组织分别提供一个小配额的套餐以供试用，如果需要切换到更大配额的套餐，请先为账户充值。

#### 充值

充值前，先切换到要充值的个人或组织账号。

接下来在「用户中心」或「组织中心」内选中「账户信息」选项卡。

点击「充值」按钮后，可以输入要充值的金额并使用微信支付或支付宝进行二维码扫码充值。

![充值](/img/screenshots/features/profiles/payment/pay.png)

在微信或支付宝确认支付后，将成功充值。

![充值成功](/img/screenshots/features/profiles/payment/success.png)

> 注意：个人账户与组织账户的余额和配额是完全独立的，所以请在充值前**务必**确认充值到的账户，充值后将无法将余额转移到其他账户。

#### 交易记录

想要查询交易的历史记录或者给等待付款的订单付款，请在「用户中心」或「组织中心」内选中「交易记录」选项卡。

在这里，您可以检视历史订单的金额和状态。

![交易记录](/img/screenshots/features/profiles/payment/history.png)

> 提示：如果在充值时没有成功，订单会在交易记录中显示「等待付款」。等待付款的订单将在一天后过期，如果还需充值，请重新执行充值操作。

### 用户中心

用户中心提供了 DaoCloud 中个人账户的信息管理、邮箱管理、第三方服务和计费等服务。

「[账户信息](account.md)」选项卡中的内容已经在之前的章节介绍过，在这里不再赘述。

同时「交易记录」选项卡中的内容将在[账户充值](payment.md)中详细介绍。

#### 个人信息

在这里，您可以更改当前用户的头像、手机号和密码。

![组织信息](/img/screenshots/features/profiles/user/info.png)

#### 邮箱

在这里，您可以添加邮箱并设置主邮箱。

![组织信息](/img/screenshots/features/profiles/user/email.png)

#### 第三方账户

DaoCloud 目前支持 GitHub、Bitbucket、Coding、GitCafe 等国内外代码托管库。

> 注意：每个代码库的账号只能关联唯一的用户账户。

![组织信息](/img/screenshots/features/profiles/user/third-party.png)

> 提示：为了更好地服务开发者，我们使用微信作为客服渠道之一。如果您将微信账号与自己的 DaoCloud 账号绑定，我们即赠送两个项目、一个容器实例和一个服务实例。

-->
