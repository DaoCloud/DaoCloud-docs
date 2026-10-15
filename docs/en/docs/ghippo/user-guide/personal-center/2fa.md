---
hide:
  - toc
---

# Two-Factor Authentication

Two-Factor Authentication (2FA) is a security verification process that enhances the security and reliability of user accounts.

## Enabling Two-Factor Authentication

The administrator enters **Security Policies**, selects **Enable Two-Factor Authentication**, and enables it.

> For details, refer to: [Security Policies](../platform-setting/security.md)

![Enable two-factor authentication](../../images/2fa00.png)

!!! note

    After two-factor authentication is enabled, users must perform a second verification when logging in.

## First Login

After two-factor authentication is enabled, users must initialize the two-factor authentication configuration when logging in for the first time. Follow the instructions in the figure below. You must install an application that generates 2FA dynamic passwords, such as Google Authenticator, on a mobile phone or other terminal device in advance.

![First login](../../images/2fa01.png)

After the application is added successfully, a 6-digit dynamic password refreshing every 30 seconds is displayed. Enter it and click **Submit** to log in successfully.

## Subsequent Logins

For subsequent logins, go to the login page and enter the username and password. Then open Google Authenticator or another dynamic password application, enter the dynamic password, and click Login to log in successfully.

![Subsequent login](../../images/2fa02.png)

If you forget the dynamic password, contact the administrator to reset it.
