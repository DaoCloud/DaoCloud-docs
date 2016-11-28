---
title: 团队沟通（瀑布IM）
---

近期 DaoCloud 与 瀑布IM 正式完成了接入，让沟通更高效，让持续交付更便捷。一般持续集成和构建流程时间相对较长，我们可以通过接入到像「瀑布IM」这种团队沟通工具来提高工作效率。

这里我们将以[瀑布](http://pubu.im/)（一款可以整合各种服务通知的新一代团队沟通工具）为例，来向用户说明如何在 IM 内收到 DaoCloud 的通知，从此让工作不用分心。

##在瀑布IM中添加服务－添加扩展界面

![](https://blog.pubu.im/content/images/2016/01/Image01.png)

##找到 DaoCloud 并添加

![](https://blog.pubu.im/content/images/2016/01/Image02.png)

##复制给出的地址

![](https://blog.pubu.im/content/images/2016/01/Image03.png)

##在 DaoCloud 找到 Webhook 地址

![](https://blog.pubu.im/content/images/2016/01/Image04.png)

##设置 Webhook

![](https://blog.pubu.im/content/images/2016/01/Image05.png)

这样整个接入流程就算完成了，来做个项目 build 测试一下。效果如图所示：

![](https://blog.pubu.im/content/images/2016/01/Image06.png)

##写在后面

持续集成和构建流程时间相对较长，可以通过接入到像「瀑布IM」这样工作中常见的 IM 中。减少等待时间，只需要等通知就好了。减少大脑对这块的记忆，让通知来分担工作中的信息流转负担。
