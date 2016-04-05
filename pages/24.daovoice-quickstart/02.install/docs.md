---
title: '如何安装 DaoVoice'
---

#### 接入目的

1. 通过在前端添加 DaoVoice 提供的若干代码，在您的网页页面右下方植入对话按钮，供网站用户与管理员交流
2. 页面按钮接入完成后，管理员可以登录 DaoVoice 后台，获取所有用户提交的消息，答复用户，并使用其它高级功能

DaoVoice 植入到页面的对话按钮
![](000.png?resize=800)

DaoVoice 后台管理界面
![DaoVoice 后台管理界面](1.png?resize=800)

#### 角色定义

* 管理员
	* 您，网站的开发者，后台管理员或运营客服
* 访客
 * 未登录的访客，如访客通过 DaoVoice 提交消息，在后台会显示为 XX 颜色的 XX（如粉色的茄子）
* 用户
 * 在您的网站完成登录的用户，您需要在 DaoVoice 的接入代码中提供用户的信息，在后台这些信息会被显示，并做集成、搜索和跟踪

#### 接入步骤

1. 访问 [DaoVoice 主页](http://www.daovoice.io)并注册成为 DaoCloud 用户获取 DaoVoice 公测资格
2. 访问 [DaoVoice 应用创建引导页面](http://dashboard.daovoice.io/#/get-started)
3. 根据您的网站结构和前后台程序类型，选择对应的接入代码，完成访客用户的接入
4. 针对**用户**，需要您**编写代码提供这些用户的信息**，DaoVoice 获取后，会与 DaoVoice 后台管理系统集成，您可以跟踪每个用户的具体会话和行为

**步骤一：注册成为 DaoVoice 公测用户** 

DaoVoice 目前处于公测阶段，如您有兴趣参与，请访问 [DaoVoice 网站](http://www.daovoice.io)。申请内测的条件如下：

* 拥有一个网站，渴望与您的网站用户进行实时交流
* 信奉持续交付，精益运营的理念，渴望通过用户「参与感」提升产品体验
* 注册成为 DaoCloud 用户

**步骤二：访问 DaoVoice 应用创建引导页面**

在注册成为 DaoCloud 用户获取 DaoVoice 公测资格之后，您需要登录 [DaoVoice 应用创建引导页面](http://dashboard.daovoice.io/#/get-started)。

该页面将引导您将 DaoVoice 安装到您的网站，植入的 JavaScript 代码经过了大量的优化，所有的调用和通信都采用异步方式完成，不会影响您的网站的加载速度和性能。

![](help-start-01.png)

**步骤三：根据 Web 类型选择对应的接入代码，完成访客接入**

接入方式选择的判断标准如下:

* 若您的网站是服务器端渲染页面，请选择 **多页面应用 (例如 JAVA, PHP, Rails 等)**
* 若您的网站是客户端渲染页面，请选择 **单页面应用 (例如 AnglarJS, ReactJS 等)**

**步骤四：提供用户信息，完成用户信息对接**

您可以向 DaoVoice 提供存储在您系统中的用户信息，DaoVoice 获取后，会与 DaoVoice 后台管理系统集成，您可以跟踪每个用户的具体会话和行为。

字段说明：

* user_id
 * 必填: 在您系统上登录用户的唯一ID，在 DaoVoice 上标识唯一用户
* email
 * 选填: 您系统上登录用户的主邮箱，DaoVoice 将根据该邮箱在各大社交平台上抓去用户信息，帮您描绘用户画像
* name
 * 选填: 在您系统上登录用户的用户名，DaoVoice 根据该字段帮您快速定位用户
* signed_up
 * 选填: 您系统上登录用户的注册时间，DaoVoice 根据该字段帮您统计您系统中每天新用户数量，并发送通知邮件到管理员邮箱。

##### **登录用户**接入示例代码

```
// AnglarJS 风格， 通过调用 Ajax 获取用户信息返回 Promise 对象
AuthService.user()
  .then(function(user) {// user {object} 当前登录的用户信息

    daovoice('init', {
        app_id: 'XXXXXX', 			// 您的 DaoVoice AppID，由 DaoVoice 提供，不需要修改
        user_id: user.user_uuid,	// 注册用户的唯一 ID，需要由您来通过编程提供
        name: user.name,			// 注册用户在您网站的用户名，需要由您来通过编程提供
        email: user.email,			// 注册用户在你网站保存的 email 地址，需要由您来通过编程提供
        signed_up: user.created_at,	// 用户的注册时间，需要由您来通过编程提供
      });
    daovoice('update');
  });

```

用户信息的对接是非常重要的一个步骤，对接完成后，您在控制台上与用户对话时，该用户的所有相关信息都会完整展示，帮助您了解用户情况，提供更具备场景化的服务。

#### 验证接入

在接入完成后，您可以采取以下步骤来验证 DaoVoice 是否工作正常：

1. 打开您的网页，您会在页面的右下角看到一个蓝色的按钮
2. 点击蓝色对话按钮，出现对话框
3. 在多个 Web 终端使用匿名身份访问网站并发起会话，您会在 DashBoard 后台看到多个标示为 X 颜色的 Y 的访客（如紫色的茄子），每个访客都被区分
4. 在多个终端使用正常的用户 ID 登录，并发起会话，您会在后台看到每个用户分别的会话，和您的用户的信息（用户的ID、Email、创建时间等，任何您在前端通过代码提供的信息，都会在后台显示）
5. 访问 DashBoard，会话会被在 DashBoard 记录保存，管理员和发起会话的用户都收到邮件提醒

#### 系统需求

DaoVoice Widget支持以下浏览器版本

* Chrome 
* Firefox
* Safari 6+
* Internet Explorer 9/10/11
* Android 4+
* IOS 6+

DaoVoice Widget 需要浏览器支持 HTTPS 和跨域。

#### 常见问题

* 对话按钮不显示
	* 您没有正确的将 DaoVoice Widget 接入您的网站，请参照上面重新接入
* 登录用户显示均为 道客船长 , 用户与用户之间没有区分
	* 您需要将您系统中的用户信息传入 DaoVoice ，请参照上面针对登录用户接入代码示例

#### 下一步

* 我们将跟您介绍 DaoVoice 的高级功能，使用 DaoVoice API 提供用户状态数据，触发事件，操作对话框按钮等。

[JavaScript API](/daovoice-configuring/javascript-api)

[安全设置](/daovoice-configuring/secure-mode)

[完善 DaoVoice 配置](/daovoice-configuring/do-more-in-daovoice)
