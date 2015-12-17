---
title: 'JavaScript API'
---

@ting

#### daovoice('init', daovoiceSettings)
初始化 daovoice 组件设置
当 DaoVoice 加载完成之后，您可以通过 init 方法来对 daovoice 初始化设置。
当用户信息加载完成，您可将用户信息加载到 daovoice 
```
daovoice('init', {  
    app_id: 'xxxxxxxx',   // 您的 APP 标识
    email: 'daovoice@example.com',  // 用户 Email
    signed_up: 1231231230, // 用户注册时间 (时间戳)
    name: 'DaoVoice', // 用户名称
    user_id: '123123123' // 用户标识
});
```

#### daovoice('update')
更新 daovoice 组件信息
当您调用 update 方法将会使 daovoice 组件与服务器同步消息，如果有未读消息将会将它展示出来。
```
daovoice('update')
```

如果您调用 update  方法时带上设置参数 (JSON object)， daovoice 组件将会更新设置信息，并向服务器发送更新信息、同步消息。
```
daovoice('update', {"name": "daovoice"});
```

#### daovoice('openMessages')
打开消息列表
```
daovoice('openMessages')
```

#### daovoice('openNewMessage')
打开新消息
```
daovoice('openNewMessage')
```

同时您可以在打开新消息窗口的时候，带上默认的内容
```
daovoice('openNewMessage', '我是打开时默认带上的内容')
```

#### daovoice('trackEvent')
发送事件
您可以通过 trackEvent 方法来发送自定义事件，daovoice 将会把该事件与当前的用户联系在一起。您也可以在第三个参数的位置上添加事件的数据 （可选参数）
```
daovoice('trackEvent', eventName);
```
发送事件时带上事件数据
```
daovoice('trackEvent', eventName, eventMetaData )
```