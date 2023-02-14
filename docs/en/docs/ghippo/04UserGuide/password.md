# Reset Password

If you forget your password, you can reset it by following the instructions on this page.

## Reset password steps

When an administrator initially creates a user, it sets a username and password for it.
After the user logs in, fill in the email address and change the password in `Personal Center`.
If the user has not set an email address, he can only contact the administrator to reset the password.

1. If you have forgotten your password, you can click `Forgot password?` on the login screen.

    ![Login Screen](../images/login02.png)

1. Enter your username and click `Submit`.

    To prevent spam, after clicking 'Submit', the button will be grayed out and a 1-minute countdown will be displayed.
    If you haven't received the email after 1 minute, please click this button again.

    ![Password reset process](../images/password02.png)

1. Find the password reset email in the mailbox, and click the link in your email.

    ![Password reset process](../images/password03.png)

1. Follow the screen prompts to set a new password and click `Submit`. The requirements for setting a new password are consistent with the password rules when creating a user.

    ![Password reset process](../images/password04.png)

1. The screen prompts that the password has been changed successfully or directly log in to the DCE main screen.

    ![Password reset process](../images/password05.png)

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
        
send --> click[Click the mail link] --> reset[Reset password]
--> success[Successfully reset]

classDef plain fill:#ddd,stroke:#fff,stroke-width:1px,color:#000;
classDef k8s fill:#326ce5,stroke:#fff,stroke-width:1px,color:#fff;
classDef cluster fill:#fff,stroke:#bbb,stroke-width:1px,color:#326ce5;

class pass,usern,button,tip1,send,tip2,send,click,reset,success plain;
class judge1,judge2 k8s
```
