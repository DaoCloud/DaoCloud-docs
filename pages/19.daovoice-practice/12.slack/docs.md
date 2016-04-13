---
title: 'Slack 集成'
---

## 介绍

Slack 是一个很受欢迎的团队沟通工具，可以方便地与很多工具集成，例如 GitHub、Skype、Dropbox、Lucidchart，于是有人在 Slack 上通过聊天的方式发送命令，来管理机器、发布应用、查看监控等等，也被称为 ChatOps。这样可以提高团队沟通的效率，快速处理事件。
DaoCloud 最近 [开放了 API](http://docs.daocloud.io/api/)，所有人都可以免费使用。于是我们开发了一套基于 DaoCloud API 的 Slackbot，它可以在 Slack 上发送指令管理你在 DaoCloud 云平台上的应用。

## 功能

输入 list build-flows 就能显示我的项目，代码源。

![Screen Shot 2016-01-17 at 6.52.07 PM.png](http://7xi8kv.com5.z0.glb.qiniucdn.com/3765AED25EB46DB6352A6881B466F069.png)

输入 list apps 可以显示我的应用以及状态。

![Screen Shot 2016-01-17 at 6.53.03 PM.png](http://7xi8kv.com5.z0.glb.qiniucdn.com/8790E1C46F98EF94E7F2A2CD9DDFF401.png)

app info cntrains-web 显示某个应用的具体信息。

![Screen Shot 2016-01-17 at 6.53.59 PM.png](http://7xi8kv.com5.z0.glb.qiniucdn.com/8790E1C46F98EF94E7F2A2CD9DDFF401.png)

app redeploy slackbot v1.1.0 即可指定镜像版本重新部署应用。

![Screen Shot 2016-01-17 at 8.47.04 PM.png](http://7xi8kv.com5.z0.glb.qiniucdn.com/AD23165CD42FE8624FF9FB5607D63C28.png)

另外 DaoCloud 还支持 Webhook，git push 好代码，DaoCloud 开始自动构建镜像，Slack频道会收到提示。

![Screen Shot 2016-01-17 at 8.50.09 PM.png](http://7xi8kv.com5.z0.glb.qiniucdn.com/025B007692A456C14F9A6154FD8DE262.png)

## 试一试

首先在你的 Slack 频道里添加一个 Bot，得到API Token。

pull 我的镜像：`docker pull daocloud.io/greenmoon55/slackbot:latest` 再 push 到你的 DaoCloud 镜像仓库里。

填写三个环境变量：
`DAOCLOUD_TOKEN` 用于发请求给 DaoCloud API 验证用，进入 DaoCloud 用户中心->API页即可找到
`SLACK_CHANNEL_ID` 把 DaoCloud Webhook 的请求发给的 channel ID，例如：C0HT969S2
`SLACK_TOKEN` Slack 为 bot 提供的 API Token。

另外还需要在 DaoCloud 用户中心添加 Webhook URL，也就是 bot 的地址。

![Screen Shot 2016-01-18 at 2.52.24 PM.png](http://7xi8kv.com5.z0.glb.qiniucdn.com/9CCCEB0835541EB9B7817AFF6C0A3BEE.png)

## 实现
基于 Slack 官网文档推荐的 [Botkit](http://howdy.ai/botkit/)，用 node 很方便地写回复消息的逻辑，我的 bot 转发消息给 DaoCloud API，这样就实现了对应用的操作。

其实 Slack 原生支持 WebHook 的，不过 DaoCloud Webhook 返回的消息格式和 Slack 不同，所以还要写转发的逻辑。

代码见 [GitHub](https://github.com/greenmoon55/slackbot)

## 总结
Botkit 为开发者屏蔽了 Slack Real Time Messaging API 的细节，让我们方便地开发机器人，实现 ChatOps。
欢迎使用 DaoCloud API，后续我们会开放更多的 API 接口，更好地为开发者服务。

## 参考链接
[DaoCloud 开放 API 文档](http://docs.daocloud.io/api/)
[ChatOps at GitHub](https://speakerdeck.com/jnewland/chatops-at-github)