---
MTPE: ModetaNiu
Date: 2023-07-09
---

# Reset Password

If you forget your password, you can reset it by following the instructions on this page.

## Steps to Reset Password

When an administrator initially creates a user, it sets a username and password for him.
After the user logs in, fill in the email address and change the password in __Personal Center__ .
If the user has not set an email address, he can only contact the administrator to reset the password.

1. If you forget your password, you can click __Forgot your password?__ on the login interface.

    ![Login Interface](../images/password01en.png)  

1. Enter your login email and click __Submit__ .

    ![Forgot your password](../images/password02en.png)  

1. Find the password reset email in the mailbox, and click the link in your email. The link is effective for 5 minutes.

    ![Click the link](../images/password03en.png)     

1. Install applications that support 2FA dynamic password generation (such as Google Authenticator) on mobile phone 
   or other devices. Set up a dynamic password to activate your account, and click __Submit__ .

    ![Config dynamic password](../images/password04en.png)    

1. Set a new password and click __Submit__ . The requirements for setting a new password are consistent with 
   the password rules when creating an account.

    ![Update password](../images/password04.png)   

1. The password is successfully reset, and you enter the home page directly.  

## Reset password process

The flow of the password reset process is as follows.

```mermaid
graph TB

pass[Forgot password] --> usern[Enter username]
--> button[Click button to send a mail] --> judge1[Check your username is correct or not]

    judge1 -.Correct.-> judge2[Check if you have bounded a mail]
    judge1 -.Wrong.-> tip1[Error of incorrect username]
    
        judge2 -.A mail has been bounded.-> send[Send a reset mail]
        judge2 -.No any mail bounded.-> tip2[No any mail bounded<br>Contact admin to reset password]
        
send --> click[Click the mail link] --> config[Config dynamic password]--> reset[Reset password]
--> success[Successfully reset]

classDef plain fill:#ddd,stroke:#fff,stroke-width:1px,color:#000;
classDef k8s fill:#326ce5,stroke:#fff,stroke-width:1px,color:#fff;
classDef cluster fill:#fff,stroke:#bbb,stroke-width:1px,color:#326ce5;

class pass,usern,button,tip1,send,tip2,send,click,config,reset,success plain;
class judge1,judge2 k8s
```
