---
title: 'JavaScript API'
---

#### 简介

在您的网站上安装 DaoVoice 上后就可以使用 JavaScript API 了。提供下面功能。

* 添加用户自定义属性
* 发送自定义事件
* 控制聊天窗口
* 显示、隐藏消息窗口
* 显示、隐藏方法钩子

如果您的程序不是 JavaScript，可以使用我们的 [开放API](http://docs.daovoice.io/api/)


#### 初始化JS Lib

初始化 daovoice 组件设置
当 DaoVoice 加载完成之后，您可以通过 daovoice('init') 方法来对 daovoice 初始化设置。
当用户信息加载完成，您可将用户信息字段添加到 DaoVoice。


DaoVoice 用户预定义属性有：

* user_id 
* email
* name
* phone
* signed_up
* company


同时 DaoVoice 还支持用户自定义属性哦！

例子：

```
/**
 * @param { String } 初始化用户信息
 * @param { Object } 用户信息
 */
daovoice('init', {  
    app_id: 'xxxxxxxx',   // 必填，您的 APP 标识
    user_id: '123456' // 可选，用户唯一标识
    email: 'daovoice@example.com',  // 可选，用户 Email
    name: '张三', // 可选，用户名称
    signed_up: 1450409868, // 可选，用户注册时间 (Unix时间戳)
    plan: 'pro' // 可选，自定义属性，用户当前订购的套餐
    company: '' // 可选，用户公司信息
});
```

#### 同步信息

更新 DaoVoice 组件，当您调用 daovoice('update') 方法将会使 DaoVoice 组件与服务器同步消息，如果有未读消息将会将它展示出来。一般配合初始化使用。

例子：
```
/**
 * @param { String } 同步用户信息
 */
daovoice('update')
```

#### 更新用户属性

如果您调用 update  方法时带上设置参数 (JSON object)， daovoice 组件将会更新用户属性信息，并向服务器发送更新信息、同步消息。

例子：

```
/**
 * @param { String } 同步用户信息
 * @param { Object } 用户信息
 */
daovoice('update', {
    "name": "李四",
    "paid": 200.00 // 自定义属性
});
```

#### 打开消息列表

```
/**
 * @param { String } 打开消息列表
 */
daovoice('openMessages')
```

#### 打开新消息

```
/**
 * @param { String } 打开新的消息
 */
daovoice('openNewMessage')
```

同时您可以在打开新消息窗口的时候，带上默认的内容
```
/**
 * @param { String } 打开新的消息
 * @param { String } 新消息内容
 */
daovoice('openNewMessage', '我是打开时默认带上的内容')
```

#### 发送事件


您可以通过 trackEvent 方法来发送自定义事件，daovoice 将会把该事件与当前的用户联系在一起。您也可以在第三个参数的位置上添加事件的数据 （可选参数）

```
/**
 * @param { String } 发送用户事件
 * @param { String } 事件名
 */
daovoice('trackEvent', 'createOrder');
```

发送事件时带上事件数据

```
/**
 * @param { String } 方法名
 * @param { String } 事件名
 * @param { Object } 事件的数据元
 */
daovoice('trackEvent', 'createOrder', {
  price: 100.00,
} )
```

#### 显示消息窗口


您可以通过show方法来打开消息列表。如果没有对话，它将打开新的消息视图，如果有它将打开消息列表。

```
/**
 * @param { String } 显示
 */
daovoice('show')
```

#### 隐藏消息窗口


您可以通过hide方法来关闭消息窗口。

```
/**
 * @param { String } 隐藏
 */
daovoice('hide')
```

#### 显示方法钩子


您可以通过onShow方法来添加show方法执行之后的事件。需要传入一个函数参数。

```
/**
 * @param { String } show方法钩子
 * @param { Function } show方法执行之后触发的事件
 */
daovoice('onShow', function() { // 做一些事情})
```

#### 隐藏方法钩子


您可以通过onHide方法添加hide方法执行之后触发的事件。需要传入一个函数参数。

```
/**
 * @param { String } hide方法钩子
 * @param { Function } hide方法执行之后触发的事件
 */
daovoice('onHide', function() { // 做一些事情})
```

### 小建议


* 检查您的接入网站是否加入<!DOCTYPE html>头文件
* 检查您的接入网站是否加入utf-8的编码格式
* 建议您的网站head标签内加入`<meta http-equiv="X-UA-Compatible" content="IE=11;IE=10;IE=9; IE8; IE=7; IE=EDGE">`为了产品在IE浏览器上有更好的用户体验.


### 小技巧

我们在完成 DaoVoice 对接的网站上，可以通过 **控制台** 中来调用 JS API，立即能看到效果，非常好用哦！