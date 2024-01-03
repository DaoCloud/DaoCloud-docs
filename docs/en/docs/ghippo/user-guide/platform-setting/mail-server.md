---
hide:
  - toc
---

# Mail Server

DCE 5.0 will send an e-mail to the user to verify the e-mail address if the user forgets the password to ensure that the user is acting in person.
In order for DCE 5.0 to be able to send email, you need to provide your mail server address first.

The specific operation steps are as follows:

1. Log in to DCE 5.0 as a user with __admin__ role. Click __Global Management__ at the bottom of the left navigation bar.

    

1. Click __Settings__ , select __Mail Server Settings__ .

    

    Complete the following fields to configure the mail server:

    | field | description | example value |
    | ----------------- | -------------------------------- ----------------------------- | ------------ |
    | SMTP server address | SMTP server address that can provide mail service | smtp.163.com |
    | SMTP server port | Port for sending mail | 25 |
    | Username | Name of the SMTP user | test@163.com |
    | Password | Password for the SMTP account | 123456 |
    | Sender's email address | Sender's email address | test@163.com |
    | Use SSL secure connection | SSL can be used to encrypt emails, thereby improving the security of information transmitted via emails, usually need to configure a certificate for the mail server | Disable |

1. After the configuration is complete, click __Save__ , and click __Test Mail Server__ .

    

1. A message indicating that the mail has been successfully sent appears in the upper right corner of the screen, indicating that the mail server has been successfully set up.

    

## Common problem

Q: What is the reason why the user still cannot retrieve the password after the mail server is set up?

Answer: The user may not have an email address or set a wrong email address; at this time, users with the admin role can find the user by username in __Global Management__ -> __Access Control__ , and set it as The user sets a new login password.

If the mail server is not connected, please check whether the mail server address, username and password are correct.