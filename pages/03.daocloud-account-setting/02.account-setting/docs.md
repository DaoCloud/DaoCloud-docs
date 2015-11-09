---
title: 用户账号设置
taxonomy:
    category:
        - docs
---

### 账户信息

<!-- TODO: 术语表：个人账户、组织账户、配额 -->

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


### 组织中心

组织中心提供了 DaoCloud 中组织账户的信息管理、组织管理和计费等服务。

「[账户信息](account.md)」选项卡中的内容已经在之前的章节介绍过，在这里不再赘述。

同时「交易记录」选项卡中的内容将在[账户充值](payment.md)中详细介绍。

#### 创建组织

在以组织的身份进行操作之前，您需要创建或加入一个组织。要创建组织请参考下面的步骤：

第一步：点击「创建组织」。

「创建组织」的按钮可以在任何页面右上角的下拉菜单中找到。

![控制台：账户管理](/img/screenshots/features/profiles/organization/dashboard-new.png)

也可以在[用户中心](user.md)内「我的组织」选项卡中找到。

![用户中心：我的组织](/img/screenshots/features/profiles/organization/user-profile-new.png)

---

<!-- FIXME: 与界面统一 -->

第二步：在创建组织的界面为组织指定「组织名称」，组织名称只能包含英文数字、下划线 `_`、小数点 `.`、和减号 `-`，并且不能与现有组织重名。

![创建组织](/img/screenshots/features/profiles/organization/new.png)

> 提示：请谨慎确定组织名称，一旦创建将无法再更改。

---

第三步：选择套餐。

---

第四步：点击「创建新组织」按钮。

---

至此您已经成功创建了一个新的组织。要完善组织信息或对组织进行管理，请参阅下面的章节。

#### 组织信息

在这里，您可以更改当前组织的头像、描述、地址和 URL。

![组织信息](/img/screenshots/features/profiles/organization/info.png)

#### 组织管理

在这里，您可以邀请新成员加入组织、管理当前成员的权限和删除成员。当然，在这里您也可以删除组织。

![组织管理](/img/screenshots/features/profiles/organization/management.png)

> 提示：在发送新成员邀请后，新成员可以将现有账户加入组织，也可以注册新账户加入组织。

> 注意：最后一位管理员无法更改自己的权限或离开组织。

> 警告：组织在删除前请先删除所有的项目、应用、服务实例和自有主机，组织在删除后**无法重新创建同名组织**并且**组织的余额将作废**。

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

#### 我的组织

在这里，您可以检视目前您所加入的组织，以及创建一个新的组织。

![组织信息](/img/screenshots/features/profiles/user/organization.png)

> 提示：关于创建和管理组织的细节请参考[组织中心](organization.md)。
