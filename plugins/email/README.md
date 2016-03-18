# Grav Email Plugin

The **email plugin** for [Grav](http://github.com/getgrav/grav) adds the ability to send email. This is particularly useful for the **admin** and **login** plugins.

# Installation

The email plugin is easy to install with GPM.

```
$ bin/gpm install email
```

# Configuration

Simply copy the `user/plugins/email/email.yaml` into `user/config/plugins/email.yaml` and make your modifications.

```
enabled: true
from:
from_name:
to:
to_name:
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
content_type: text/html
```

# Testing emails

A good way to test emails is to setup a fake SMTP server, for example using [https://mailtrap.io](https://mailtrap.io)

Setup the Email plugin to use that SMTP server with the fake inbox data. For example:

```
mailer:
  engine: smtp
  smtp:
    server: mailtrap.io
    port: 2525
    encryption: none
    user: YOUR_MAILTRAP_INBOX_USER
    password: YOUR_MAILTRAP_INBOX_PASSWORD
```

That service will intercept emails and show them on their web-based interface instead of sending them for real.

You can try and fine tune the emails there when testing.

# Programmatically send emails 

Add this code in your plugins:

```php

        $to = 'email@test.com';
        $from = 'email@test.com';

        $subject = 'Test';
        $content = 'Test';

        $message = $this->grav['Email']->message($subject, $content, 'text/html')
            ->setFrom($from)
            ->setTo($to);

        $sent = $this->grav['Email']->send($message);
```

# Email actions

When executing email actions (e.g. during form processing), all action parameters are inherited from the global configuration but may also be overridden on a per action basis.

```
title: Custom form

form:
  name: custom_form
  fields:

    # Any fields you'd like to add to the form:
    # Their values may be referenced in email actions via '{{ form.value.FIELDNAME|e }}'

  process:
    - email:
        subject: "[Custom form] {{ form.value.name|e }}"
        body: "{% include 'forms/data.txt.twig' %}"
        from: sender@example.com
        from_name: 'Custom sender name'
        to: recipient@example.com
        to_name: 'Custom recipient name'
        content_type: 'text/plain'
```

## Additional action parameters

To have more control over your generated email, you may also use the following additional parameters:

* ```reply_to```: Set one or more addresses that should be used to reply to the message.
* ```cc``` _(Carbon copy)_: Add one or more addresses to the delivery list. Many email clients will mark email in one's inbox differently depending on whether they are in the ```To:``` or ```Cc:``` list.
* ```bcc``` _(Blind carbon copy)_: Add one or more addresses to the delivery list that should (usually) not be listed in the message data, remaining invisible to other recipients.
* ```charset```: Explicitly set a charset for the generated email body (only takes effect if ```body``` parameter is a string, defaults to ```utf-8```)

### Specifying email addresses

Email-related parameters (```from```, ```to```, ```reply_to```, ```cc```and ```bcc```) allow different notations for single / multiple values:

#### Single email address string

```
to: mail@example.com
```

####  Multiple email address strings

```
to:
  - mail@example.com
  - mail+1@example.com
  - mail+2@example.com
```

#### Single email address with name

```
to:
  mail: mail@example.com
  name: Human-readable name
```

#### Multiple email addresses (with and without names)

```
to:
  -
    mail: mail@example.com
    name: Human-readable name
  -
    mail: mail+2@example.com
    name: Another human-readable name
  -
    mail+3@example.com
  -
    mail+4@example.com
```

## Mutil-part MIME messages

Apart from a simple string, an email body may contain different MIME parts (e.g. HTML body with plain text fallback). You may even specify a different charset for each part (default to ```utf-8```):

```
body:
  -
    content_type: 'text/html'
    body: "{% include 'forms/default/data.html.twig' %}"
  -
    content_type: 'text/plain'
    body: "{% include 'forms/default/data.txt.twig' %}"
    charset: 'iso-8859-1'
```
