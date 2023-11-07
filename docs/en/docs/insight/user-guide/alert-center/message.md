# Notification Settings

On the `Notification Settings` page, you can configure how to send messages to users through email, WeCom, DingTalk, Webhook, and SMS.

## Email Group

1. After entering `Insight`, click `Alert Center` -> `Notification Settings` in the left navigation bar. By default, the email notification object is selected. Click `Add email group` and add one or more email addresses.

2. Multiple email addresses can be added.

    ![WeCom](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/insight/images/notify02.png)

3. After the configuration is complete, the notification list will automatically return. Click `︙` on the right side of the list to edit or delete the email group.

## WeCom

1. In the left navigation bar, click `Alert Center` -> `Notification Settings` -> `WeCom`. Click `Add Group Robot` and add one or more group robots.

    For the URL of the WeCom group robot, please refer to the [official document of WeCom: How to use group robots](https://developers.weixin.qq.com/doc/offiaccount/Getting_Started/Overview.html).

2. After the configuration is complete, the notification list will automatically return. Click `︙` on the right side of the list, select `Send Test Information`, and you can also edit or delete the group robot.

## DingTalk

1. In the left navigation bar, click `Alert Center` -> `Notification Settings` -> `DingTalk`. Click `Add Group Robot` and add one or more group robots.

    For the URL of the DingTalk group robot, please refer to the [official document of DingTalk: Custom Robot Access](https://developers.dingtalk.com/document/robots/custom-robot-access).

2. After the configuration is complete, the notification list will automatically return. Click `︙` on the right side of the list, select `Send Test Information`, and you can also edit or delete the group robot.

## Webhook

1. In the left navigation bar, click `Alert Center` -> `Notification Settings` -> `Webhook`. Click `New Webhook` and add one or more Webhooks.

    For the Webhook URL and more configuration methods, please refer to the [webhook document](https://github.com/webhooksite/webhook.site).

2. After the configuration is complete, the notification list will automatically return. Click `︙` on the right side of the list, select `Send Test Information`, and you can also edit or delete the Webhook.

## SMS Group

1. In the left navigation bar, click `Alert Center` -> `Notification Settings` -> `SMS`. Click `Add SMS Group` and add one or more SMS groups.

2. Enter the name, the object receiving the message, phone number, and notification server in the pop-up window.

    The notification server needs to be created in advance under `Notification Settings` -> `Notification Server`. Currently, two cloud servers, Alibaba Cloud and Tencent Cloud, are supported. Please refer to your own cloud server information for the specific configuration parameters.

3. After the SMS group is successfully added, the notification list will automatically return. Click `︙` on the right side of the list to edit or delete the SMS group.
