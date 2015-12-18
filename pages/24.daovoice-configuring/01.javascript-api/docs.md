---
title: 'JavaScript API'
---

#### 简介

在您的网站上安装DaoVoice上后就可以使用JavaScript API了。提供下面功能。
* 自定义属性
* 发送事件
* 控制聊天窗口

如果您的程序不是JavaScript，可以使用我们的 [开放API](http://docs.daovoice.io/api/)

#### 初始化JS Lib

初始化 daovoice 组件设置
当 DaoVoice 加载完成之后，您可以通过 init 方法来对 daovoice 初始化设置。
当用户信息加载完成，您可将用户信息加载到 daovoice 。支持自定义属性

例子：

```
daovoice('init', {  
    app_id: 'xxxxxxxx',   // 必填，您的 APP 标识
    user_id: '123456' // 必填，用户标识
    email: 'daovoice@example.com',  // 可选，用户 Email
    name: '张三', // 可选，用户名称
    signed_up: 1450409868, // 可选，用户注册时间 (Unix时间戳),
    paid: 100.00 // 可选，自定义属性
});
```

#### 同步信息

更新 daovoice 组件，当您调用 update 方法将会使 daovoice 组件与服务器同步消息，如果有未读消息将会将它展示出来。一般配合初始化使用。

例子：
```
daovoice('update')
```

#### 更新用户属性

如果您调用 update  方法时带上设置参数 (JSON object)， daovoice 组件将会更新用户属性信息，并向服务器发送更新信息、同步消息。

例子：

```
daovoice('update', {
    "name": "李四",
    "paid": 200.00 // 自定义属性
});
```

#### 打开消息列表

```
daovoice('openMessages')
```

#### 打开新消息

```
daovoice('openNewMessage')
```

同时您可以在打开新消息窗口的时候，带上默认的内容
```
daovoice('openNewMessage', '我是打开时默认带上的内容')
```

#### 发送事件


您可以通过 trackEvent 方法来发送自定义事件，daovoice 将会把该事件与当前的用户联系在一起。您也可以在第三个参数的位置上添加事件的数据 （可选参数）
```
daovoice('trackEvent', event);
```
发送事件时带上事件数据
```
daovoice('trackEvent', event, metaData )
```