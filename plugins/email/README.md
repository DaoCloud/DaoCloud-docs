# Grav Email Plugin

The **email plugin** for [Grav](http://github.com/getgrav/grav) adds the ability to send email. This is particularly useful for the **admin** and **login** plugins.

| IMPORTANT!!! This plugin is currently in development as is to be considered a **beta release**.  As such, use this in a production environment **at your own risk!**. More features will be added in the future.


# Installation

The email plugin is easy to install with GPM.

```
$ bin/gpm install email
```

# Configuration

Simply copy the `user/plugins/email/email.yaml` into `user/config/plugins/email.yaml` and make your modifications.

```
enabled: true
from: ''
to: ''
mailer:
  engine: mail
  smtp:
    server: localhost
    port: 25
    encryption: none
    user: ''
    password: ''
  sendmail:
    bin: '/usr/sbin/sendmail'
```  

