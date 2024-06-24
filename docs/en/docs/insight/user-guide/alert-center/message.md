# Notification Settings

On the __Notification Settings__ page, you can configure how to send messages to users through email, WeCom, DingTalk, Webhook, and SMS.

## Email Group

1. After entering __Insight__ , click __Alert Center__ -> __Notification Settings__ in the left navigation bar. By default, the email notification object is selected. Click __Add email group__ and add one or more email addresses.

2. Multiple email addresses can be added.

    ![WeCom](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/insight/images/notify02.png)

3. After the configuration is complete, the notification list will automatically return. Click __┇__ on the right side of the list to edit or delete the email group.

## WeCom

1. In the left navigation bar, click __Alert Center__ -> __Notification Settings__ -> __WeCom__ . Click __Add Group Robot__ and add one or more group robots.

    For the URL of the WeCom group robot, please refer to the [official document of WeCom: How to use group robots](https://developers.weixin.qq.com/doc/offiaccount/Getting_Started/Overview.html).

2. After the configuration is complete, the notification list will automatically return. Click __┇__ on the right side of the list, select __Send Test Information__ , and you can also edit or delete the group robot.

## DingTalk

1. In the left navigation bar, click __Alert Center__ -> __Notification Settings__ -> __DingTalk__ . Click __Add Group Robot__ and add one or more group robots.

    For the URL of the DingTalk group robot, please refer to the [official document of DingTalk: Custom Robot Access](https://developers.dingtalk.com/document/robots/custom-robot-access).

2. After the configuration is complete, the notification list will automatically return. Click __┇__ on the right side of the list, select __Send Test Information__ , and you can also edit or delete the group robot.

## Webhook

1. In the left navigation bar, click __Alert Center__ -> __Notification Settings__ -> __Webhook__ . Click __New Webhook__ and add one or more Webhooks.

    For the Webhook URL and more configuration methods, please refer to the [webhook document](https://github.com/webhooksite/webhook.site).

2. After the configuration is complete, the notification list will automatically return. Click __┇__ on the right side of the list, select __Send Test Information__ , and you can also edit or delete the Webhook.

## SMS Group

1. In the left navigation bar, click __Alert Center__ -> __Notification Settings__ -> __SMS__ . Click __Add SMS Group__ and add one or more SMS groups.

2. Enter the name, the object receiving the message, phone number, and notification server in the pop-up window.

    The notification server needs to be created in advance under __Notification Settings__ -> __Notification Server__ . Currently, two cloud servers, Alibaba Cloud and Tencent Cloud, are supported. Please refer to your own cloud server information for the specific configuration parameters.

3. After the SMS group is successfully added, the notification list will automatically return. Click __┇__ on the right side of the list to edit or delete the SMS group.
