---
title: 安全模式
---

#### 安全模式介绍

用户数据的安全是 DaoVoice 最关心的，我们默认强制启用 HTTPS 和内容加密可以保证通信安全，抵御中间人攻击。

启用安全模式可以抵御JS注入的基于页面的攻击。让您数据更安全。 


#### 使用聊天窗口认证

您可以在 DaoVoice 的应用设置界面找到安全模式的设置。

要想使用安全模式，您只需要在您集成的JS代码中加入一个`secure_digest`字段。这个字段的值是将 user_id 和 YOURS_APP_SECERT 通过 sha1 算法生成的数字签名。

一旦启用安全模式，注册用户的请求必须有`secure_digest`字段，没有正确的`secure_digest`的请求将被认为是非法请求。


##### 在动态页面中使用聊天窗口认证

您可以在动态页面模板中加入如下代码，完成安全模式的集成

**Python**

	"app_id": "YOURS_APP_ID",
	"user_id" : "{{ user_id }}" ,
	"secure_digest": "{{ hmac.new(YOURS_APP_SECERT, user_id, hashlib.sha1).hexdigest() }}",
	...


**PHP**

	"app_id": "YOURS_APP_ID",
	"user_id" : "<?php echo $user_id ?>" , 
	"secure_digest": "<?php echo hash_hmac("sha1", $user_id, "YOURS_APP_SECERT");?>",
	...



##### 在单页面页面中使用聊天窗口认证

如果您使用单页面应用，可以通过在后段API的用户认证的auth接口中，加入`secure_digest`字段。再添加到应用之中。`secure_digest`的计算方法可以参考下面的示例。


**AngularJS**

	"app_id": "YOURS_APP_ID",
	"user_id" : user_id , 
	"secure_digest": secure_digest ,
	...

##### 各语言中示例


**NodeJS**

    crypto.createHmac('sha1', YOURS_APP_SECERT).update(user_id).digest('hex')
    
**Python**

    hmac.new(YOURS_APP_SECERT, user_id, hashlib.sha1).hexdigest() 

**Ruby**

	OpenSSL::HMAC.digest('sha1', YOURS_APP_SECERT, user_id)
	
**PHP**

	hash_hmac("sha1", $user_id, "YOURS_APP_SECERT")
	
**GO**
	
	h := hmac.New(sha1.New, YOURS_APP_SECERT)
	h.Write(user_id)
	secure_digest := h.Sum(nil)
	
#### 注意事项

* 计算`secure_digest`的`user_id`和当前页面传入的`user_id`必须相同。
* 当启用安全模式后，注册用户必须有`user_id`,不能为空。未转化用户不受影响
* YOURS_APP_SECERT千万不能暴露在前端页面中，当然也不能公开出来。如果不小心泄漏，可以重置。


